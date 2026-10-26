#!/usr/bin/env python3
"""package.py - build release files. Run from the repo root (python3, or python on Windows).

    python3 scripts/package.py            # writes dist/

dist/claude-ai/<skill>.zip   one self-contained zip per skill, for claude.ai / Claude Desktop
                             (Settings -> Capabilities -> Skills -> upload). Shared references and the
                             polish tool are copied inside each zip and the paths rewritten, because an
                             uploaded skill cannot see files outside its own folder.
dist/<name>-skills-all.zip   every claude.ai zip in one download
dist/<name>-plugin.zip       the whole repo as a Claude Code plugin (for offline install)
"""
import json
import os
import re
import shutil
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIST = os.path.join(ROOT, "dist")
SKILLS = os.path.join(ROOT, "skills")
PLAYBOOK = os.path.join(SKILLS, "instagram-playbook")
POLISH = os.path.join(SKILLS, "polish", "scripts")
SKIP = {".git", "dist", "__pycache__", "tests"}


def zip_dir(src, dest, arc_root):
    with zipfile.ZipFile(dest, "w", zipfile.ZIP_DEFLATED) as z:
        for dirpath, dirs, files in os.walk(src):
            dirs[:] = [d for d in dirs if d not in SKIP]
            for f in files:
                full = os.path.join(dirpath, f)
                z.write(full, os.path.join(arc_root, os.path.relpath(full, src)))


def self_contained(name, out):
    """Copy a skill into out/name with references/ and the polish tool inside it."""
    dst = os.path.join(out, name)
    shutil.copytree(os.path.join(SKILLS, name), dst, ignore=shutil.ignore_patterns("__pycache__"))
    if name != "instagram-playbook":
        shutil.copytree(PLAYBOOK, os.path.join(dst, "references"), ignore=shutil.ignore_patterns("SKILL.md"))
    md = os.path.join(dst, "SKILL.md")
    text = open(md, encoding="utf-8").read()
    text = text.replace("../instagram-playbook/", "references/")
    # tools borrowed from sibling skills are copied into this skill's scripts/
    for sibling, files in (("polish", ("polish.py", "rules.json")), ("growth-audit", ("outliers.py",))):
        ref = f"../{sibling}/scripts/"
        if ref in text:
            os.makedirs(os.path.join(dst, "scripts"), exist_ok=True)
            for f in files:
                shutil.copy(os.path.join(SKILLS, sibling, "scripts", f), os.path.join(dst, "scripts", f))
            text = text.replace(ref, "scripts/")
    if "../" in text:
        left = sorted(set(re.findall(r"\.\./[\w./-]+", text)))
        raise SystemExit(f"{name}: SKILL.md still points outside the skill folder: {left}")
    open(md, "w", encoding="utf-8").write(text)
    return dst


def main():
    plugin = json.load(open(os.path.join(ROOT, ".claude-plugin", "plugin.json"), encoding="utf-8"))
    name = plugin["name"]
    shutil.rmtree(DIST, ignore_errors=True)
    stage = os.path.join(DIST, "_stage")
    os.makedirs(os.path.join(DIST, "claude-ai"))
    skills = sorted(d for d in os.listdir(SKILLS) if os.path.isfile(os.path.join(SKILLS, d, "SKILL.md")))
    for s in skills:
        folder = self_contained(s, stage)
        zip_dir(folder, os.path.join(DIST, "claude-ai", f"{s}.zip"), s)
    with zipfile.ZipFile(os.path.join(DIST, f"{name}-skills-all.zip"), "w", zipfile.ZIP_DEFLATED) as z:
        for s in skills:
            z.write(os.path.join(DIST, "claude-ai", f"{s}.zip"), f"{s}.zip")
    zip_dir(ROOT, os.path.join(DIST, f"{name}-plugin.zip"), name)
    shutil.rmtree(stage)
    print(f"{len(skills)} skills packaged into {os.path.relpath(DIST, ROOT)}/")


if __name__ == "__main__":
    main()
