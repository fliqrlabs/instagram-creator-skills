#!/usr/bin/env python3
"""validate.py - checks the pack before every release. Run from the repo root.

    python3 scripts/validate.py

1. every skills/*/SKILL.md has frontmatter with name == folder and a description <= 1024 chars
2. every relative path a skill mentions (../../references/x.md, scripts/x.py, ../polish/...) exists
3. no secrets or tokens are committed
4. every capability a skill relies on is listed in references/connectors.md
5. the bundled tools run on the fixtures and give the expected verdicts
"""
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS = os.path.join(ROOT, "skills")
errors = []


def err(msg):
    errors.append(msg)
    print("  FAIL", msg)


def frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None
    fm, key = {}, None
    for line in m.group(1).splitlines():
        km = re.match(r"^([a-zA-Z_-]+):\s*(.*)$", line)
        if km:
            key = km.group(1)
            fm[key] = km.group(2).strip()
        elif key and line.startswith("  "):
            fm[key] = (fm[key] + " " + line.strip()).strip()
    for k, v in fm.items():
        fm[k] = re.sub(r"^>-?\s*", "", v).strip('"')
    return fm


print("skills")
names = sorted(d for d in os.listdir(SKILLS) if os.path.isdir(os.path.join(SKILLS, d)))
connectors = open(os.path.join(ROOT, "references", "connectors.md"), encoding="utf-8").read()
tool_names = set(re.findall(r"`([a-z_]+)`", connectors))

for name in names:
    path = os.path.join(SKILLS, name, "SKILL.md")
    if not os.path.exists(path):
        err(f"{name}: no SKILL.md")
        continue
    text = open(path, encoding="utf-8").read().replace("\r\n", "\n")
    fm = frontmatter(text)
    if not fm:
        err(f"{name}: missing frontmatter")
        continue
    if fm.get("name") != name:
        err(f"{name}: frontmatter name '{fm.get('name')}' != folder")
    desc = fm.get("description", "")
    if not (50 <= len(desc) <= 1024):
        err(f"{name}: description is {len(desc)} chars (want 50-1024)")
    if len(text.splitlines()) > 500:
        err(f"{name}: SKILL.md over 500 lines, move detail to references/")
    base = os.path.join(SKILLS, name)
    for rel in set(re.findall(r"(\.\./[\w./-]+\.(?:md|py|json)|scripts/[\w.-]+\.(?:py|json))", text)):
        if not os.path.exists(os.path.normpath(os.path.join(base, rel))):
            err(f"{name}: references missing file {rel}")
    for tool in set(re.findall(r"`((?:list|get|create|update|set|delete|restore)_[a-z_]+)`", text)):
        if tool not in tool_names:
            err(f"{name}: uses tool `{tool}` not listed in references/connectors.md")
    print(f"  ok   {name}  ({len(desc)} char description)")

print("connector")
import json as _json
mcp = _json.load(open(os.path.join(ROOT, ".mcp.json"), encoding="utf-8"))
servers = mcp.get("mcpServers", {})
if not servers:
    err(".mcp.json has no mcpServers")
for key, cfg in servers.items():
    if cfg.get("type") != "http" or not str(cfg.get("url", "")).startswith("https://") or not cfg["url"].rstrip("/").endswith("/mcp"):
        err(f".mcp.json server '{key}' needs type http and an https://.../mcp url")
    else:
        print(f"  ok   {key} -> {cfg['url']}")
if re.search(r"\{\{[A-Z_]*MCP_URL\}\}", open(os.path.join(ROOT, "README.md"), encoding="utf-8").read()):
    err("README.md still has an MCP URL placeholder")

print("secrets")
SECRET = re.compile(r"(EAA[A-Za-z0-9]{40,}|IGQV[A-Za-z0-9_-]{40,}|sk-[A-Za-z0-9]{32,}|eyJ[A-Za-z0-9_-]{30,}\.[A-Za-z0-9_-]{30,})")
for dirpath, _, files in os.walk(ROOT):
    if ".git" in dirpath:
        continue
    for f in files:
        if f.endswith((".md", ".py", ".json", ".txt", ".yml", ".sh")):
            p = os.path.join(dirpath, f)
            if SECRET.search(open(p, encoding="utf-8", errors="ignore").read()):
                err(f"possible secret in {os.path.relpath(p, ROOT)}")
print("  ok   scanned")

print("tools")
polish = os.path.join(SKILLS, "polish", "scripts", "polish.py")
fx = os.path.join(ROOT, "tests", "fixtures")
cases = [
    # (args, expected exit code or None, text that must appear in the output)
    (["bad-caption.txt"], 2, "FAIL  HASHTAGS"),
    (["good-caption.txt"], 0, "'SETUP' found before the fold"),
    (["hooks.txt", "--mode", "hook"], None, "WEAK    Hey guys"),
    (["hinglish-hook.txt", "--mode", "hook"], 0, "STRONG"),
    (["script.txt", "--mode", "script", "--target", "20"], None, "PASS  LOOP"),
    (["bio.txt", "--mode", "bio"], 0, "PASS  CTA"),
]
for args, want, expect in cases:
    r = subprocess.run([sys.executable, polish, os.path.join(fx, args[0])] + args[1:], capture_output=True, text=True, encoding="utf-8")
    if r.returncode not in (0, 1, 2) or "VERDICT" not in r.stdout:
        err(f"polish.py {' '.join(args)} crashed: {r.stderr.strip()[-300:]}")
    elif want is not None and r.returncode != want:
        err(f"polish.py {args[0]} exit {r.returncode}, expected {want}")
    elif expect not in r.stdout:
        err(f"polish.py {' '.join(args)}: expected '{expect}' in output")
    elif args[0] == "script.txt" and "0.0s" in r.stdout.split("RUNTIME")[-1][:20]:
        err("polish.py script mode timed nothing (timestamps skipped?)")
    else:
        print(f"  ok   polish.py {' '.join(args)} -> exit {r.returncode}")
r = subprocess.run([sys.executable, os.path.join(SKILLS, "growth-audit", "scripts", "outliers.py"), os.path.join(fx, "posts.json")],
                   capture_output=True, text=True, encoding="utf-8")
if r.returncode != 0 or "10.2x" not in r.stdout:
    err(f"outliers.py did not rank the fixture: {r.stdout[-300:]} {r.stderr[-300:]}")
else:
    print("  ok   outliers.py posts.json")

print()
if errors:
    print(f"{len(errors)} problem(s)")
    sys.exit(1)
print(f"all good: {len(names)} skills")
