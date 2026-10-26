#!/usr/bin/env python3
"""polish.py - clean and lint creator copy before it ships.

Stdlib only. Runs offline on your text. Nothing is uploaded.
Use `python3` on macOS/Linux and `python` on Windows.

    python3 polish.py draft.txt                    # lint a caption (default mode)
    python3 polish.py hooks.txt --mode hook        # score hook lines, one per line
    python3 polish.py script.txt --mode script     # time a reel script ([0:03] timestamps are fine)
    python3 polish.py dm.txt --mode dm             # check a DM against Instagram limits
    python3 polish.py bio.txt --mode bio           # check a profile bio
    python3 polish.py draft.txt --fix              # print the cleaned text too
    python3 polish.py draft.txt --fix --write      # overwrite the file with the cleaned text
    echo "one hook" | python3 polish.py - --mode hook

Exit code 0 = PASS, 1 = WARN, 2 = FAIL. Usable as a pre-publish gate.
"""
import argparse
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
RULES = json.load(open(os.path.join(HERE, "rules.json"), encoding="utf-8"))

for stream in (sys.stdout, sys.stdin):
    if hasattr(stream, "reconfigure"):
        stream.reconfigure(encoding="utf-8")

FEED_FOLD = 125           # characters a caption shows before "... more"
CAPTION_MAX = 2200
HASHTAG_CAP = 5           # Instagram's per-post hashtag cap (see references/algorithm.md)
DM_MAX = 1000             # Instagram text DM limit
BUTTON_TEXT_MAX = 640     # button template body limit
BIO_MAX = 150
WPM = 180                 # typical reel delivery; override with --wpm
HOOK_MAX_S = 3.0          # spoken hook should land inside 3 seconds (~9 words at 180 wpm)

# Non-ASCII characters are built with chr() so this file stays plain ASCII.
EM, EN, ELLIPSIS = chr(0x2014), chr(0x2013), chr(0x2026)
LDQ, RDQ, LSQ, RSQ = chr(0x201C), chr(0x201D), chr(0x2018), chr(0x2019)
RUPEE = chr(0x20B9)
DEVANAGARI = chr(0x0900) + "-" + chr(0x097F)
INVISIBLE = re.compile("[" + "".join(chr(c) for c in (
    0x200B, 0x200C, 0x200D, 0x2060, 0x2061, 0x2062, 0x2063, 0x2064, 0xFEFF, 0x00AD, 0x180E))
    + chr(0x202A) + "-" + chr(0x202E) + chr(0x2066) + "-" + chr(0x2069)
    + chr(0xE0000) + "-" + chr(0xE007F) + "]")
ODD_SPACES = re.compile("[" + "".join(chr(c) for c in (0x00A0, 0x202F, 0x2007, 0x2009, 0x200A)) + "]")
EMOJI = re.compile("[" + chr(0x1F300) + "-" + chr(0x1FAFF) + chr(0x2600) + "-" + chr(0x27BF) + "]")
QUOTE = "[\"'" + LDQ + RDQ + LSQ + RSQ + "]"

NUMBER_WORDS = "|".join(re.escape(w) for w in RULES["number_words"])
NUMBER = re.compile(r"(\d|" + RUPEE + r"|\b(" + NUMBER_WORDS + r")\b)", re.I)
TENSION = re.compile(r"\b(" + "|".join(re.escape(w) for w in RULES["tension_words"]) + r")\b", re.I)
HASHTAG = re.compile(r"(?<!\w)#[\w" + DEVANAGARI + "]+")
URL = re.compile(r"https?://\S+|www\.\S+|\b\w+\.(com|in|io|ai|co|link|me)\b/?\S*", re.I)
# Verb is case-insensitive; the keyword must be a standalone CAPS word ("DMs" never matches "DM").
KEYWORD_CTA = re.compile(r"(?i:\b(?:comment|type|reply|dm me|send me)\b)[^.\n]{0,25}?" + QUOTE + r"?\b([A-Z][A-Z0-9]{1,15})\b")
KEYWORD_STOP = {"YOU", "I", "IF", "AND", "THE", "ME", "MY", "US", "OK", "OR", "TO", "IT", "IS", "A", "AN"}
ASKS = re.compile(r"\b((?i:comment) " + QUOTE + r"?[A-Z]{2,}\b|(?i:comment below|save (this|it)|share (this|it)|"
                  r"send (this|it) to|follow (me|for)|tag (a|someone|your)|link in bio|click the link|dm me))")
TIMESTAMP = re.compile(r"^\[?\(?\d{1,2}:\d{2}(\.\d+)?\)?\]?\s*[-:]?\s*")


def clean(text):
    """Return (cleaned, changes). Only mechanical, judgement-free fixes."""
    changes = []

    def sub(pattern, repl, label, s):
        new, n = re.subn(pattern, repl, s)
        if n:
            changes.append(f"{n} x {label}")
        return new

    t = text.replace("\r\n", "\n")
    t = sub(INVISIBLE, "", "invisible character removed", t)
    t = sub(ODD_SPACES, " ", "non-standard space normalised", t)
    t = sub(r"(\d)\s*[" + EM + EN + r"]\s*(\d)", r"\1-\2", "dash in a number range -> hyphen", t)
    t = sub(r"\s*" + EM + r"\s*", ", ", "em dash -> comma", t)
    t = sub(r"\s*" + EN + r"\s*", "-", "en dash -> hyphen", t)
    t = sub("[" + LDQ + RDQ + "]", '"', "curly double quote straightened", t)
    t = sub("[" + LSQ + RSQ + "]", "'", "curly single quote straightened", t)
    t = sub(ELLIPSIS, "...", "ellipsis character -> three dots", t)
    t = re.sub(r",\s*([,.!?])", r"\1", t)
    t = re.sub(r"[ \t]+\n", "\n", t)
    for bad, good in RULES["replace"].items():
        pat = re.compile(r"\b" + re.escape(bad) + r"\b", re.I)
        t, n = pat.subn(good, t)
        if n:
            changes.append(f"{n} x '{bad}' -> '{good}'" if good else f"{n} x '{bad}' cut")
    t = re.sub(r"  +", " ", t)
    return t, changes


def find_slop(text):
    hits = [p for p in RULES["flag"] if re.search(r"(?<!\w)" + re.escape(p) + r"(?!\w)", text, re.I)]
    tells = [name for name, pattern in RULES["tells"].items() if re.search(pattern, text, re.M)]
    return hits, tells


class Report:
    def __init__(self):
        self.rows = []

    def add(self, level, label, msg):
        self.rows.append((level, label, msg))

    def worst(self):
        order = {"PASS": 0, "WARN": 1, "FAIL": 2}
        return max((order[r[0]] for r in self.rows), default=0)

    def print(self):
        for level, label, msg in self.rows:
            print(f"  {level:<5} {label:<18} {msg}")


def fold_box(text, width=54):
    shown = text[:FEED_FOLD].replace("\n", " ")
    lines = [shown[i:i + width] for i in range(0, len(shown), width)] or [""]
    out = ["  WHAT THE FEED SHOWS", "  +" + "-" * (width + 2) + "+"]
    for ln in lines:
        out.append("  | " + ln.ljust(width) + " |")
    tail = " ... more " if len(text) > FEED_FOLD else "-" * 10
    out.append("  +" + "-" * (width + 2 - len(tail)) + tail + "+")
    return "\n".join(out)


def find_keyword(text):
    for m in KEYWORD_CTA.finditer(text):
        if m.group(1) not in KEYWORD_STOP:
            return m.group(1), m.start(1)
    return None, -1


def lint_caption(text, keywords, r):
    body = text.strip()
    first_line = body.split("\n", 1)[0]
    visible = body[:FEED_FOLD]
    print(fold_box(body))
    print()
    r.add("PASS" if len(body) <= CAPTION_MAX else "FAIL", "LENGTH", f"{len(body)} / {CAPTION_MAX} characters")
    if len(first_line) > FEED_FOLD:
        r.add("WARN", "FIRST LINE", f"{len(first_line)} chars, cut at {FEED_FOLD} mid-thought")
    else:
        r.add("PASS", "FIRST LINE", f"{len(first_line)} chars, lands before the fold")
    concrete = NUMBER.search(visible)
    r.add("PASS" if concrete else "WARN", "CONCRETE HOOK",
          "number or specific in the visible window" if concrete
          else "nothing concrete before the fold. Add a number, name or result")
    tags = HASHTAG.findall(body)
    if len(tags) > HASHTAG_CAP:
        r.add("FAIL", "HASHTAGS", f"{len(tags)} tags. Instagram caps posts at {HASHTAG_CAP}")
    else:
        r.add("PASS", "HASHTAGS", f"{len(tags)} tags {' '.join(tags)}".rstrip())
    if HASHTAG.sub("", body).strip() == "":
        r.add("FAIL", "NO WORDS", "the caption is only hashtags")
    if URL.search(body):
        r.add("WARN", "LINK", "links in captions are not clickable. Deliver it by keyword DM instead")
    kw, pos = find_keyword(body)
    if kw:
        before = pos < FEED_FOLD
        r.add("PASS" if before else "WARN", "KEYWORD CTA",
              f"'{kw}' found " + ("before the fold" if before else f"at character {pos}, after the fold. Move it into the first 2 lines"))
    asks = len(ASKS.findall(body))
    r.add("PASS" if asks <= 1 else "WARN", "ONE ASK", f"{asks} call(s) to action" + ("" if asks <= 1 else ". Pick one"))
    if len(EMOJI.findall(body)) > 4:
        r.add("WARN", "EMOJI", f"{len(EMOJI.findall(body))} emoji. Three placed with intent beats a sprinkle")
    if keywords:
        missing = [k for k in keywords if k.lower() not in body.lower()]
        r.add("PASS" if not missing else "WARN", "SEARCH TERMS",
              f"{len(keywords) - len(missing)}/{len(keywords)} present" + (f". Missing: {', '.join(missing)}" if missing else ""))


def score_hook(line):
    """Heuristic 0-100. Kills weak hooks; it cannot pick winners."""
    words = re.findall(r"[\w'$%" + RUPEE + DEVANAGARI + "]+", line)
    n = len(words)
    score = 50
    notes = []
    low = line.lower().strip()
    for opener in RULES["dead_openers"]:
        if low.startswith(opener):
            return 5, [f"dealbreaker: opens with '{opener}'. Nobody came to the feed to be greeted"]
    has_number = bool(NUMBER.search(line))
    has_tension = bool(TENSION.search(line))
    if has_number:
        score += 15
    else:
        notes.append("no number or specific")
    if re.search(r"\b(you|your|you're|aap|aapka|aapki|tum|tumhara|tera|teri)\b", low):
        score += 8
    if re.search(r"\b(i|my|we|maine|mera|meri|hum)\b", low) and has_number:
        score += 7  # first-person proof with a number
    if has_tension:
        score += 10
    else:
        notes.append("no tension word (mistake, lost, nobody, actually, galti...)")
    if n <= 9:
        score += 10
    elif n > 14:
        score -= 15
        notes.append(f"{n} words, past ~3 seconds spoken")
    hits, _ = find_slop(line)
    if hits:
        score -= 12 * len(hits)
        notes.append("slop: " + ", ".join(hits))
    if not has_number and not has_tension:
        score = min(score, 40)  # vague and tension-free: nothing to stop the thumb
    if line.strip().endswith("?") and n < 6:
        score -= 8
        notes.append("short bare question, easy to answer 'no' and scroll")
    return max(0, min(100, score)), notes


def lint_hooks(text, r):
    lines = [l.strip() for l in text.splitlines() if l.strip()]
    ranked = sorted(((score_hook(l), l) for l in lines), key=lambda x: -x[0][0])
    print("HOOK RANKING")
    print("=" * 70)
    for i, ((s, notes), line) in enumerate(ranked):
        band = "STRONG" if s >= 70 else "OK" if s >= 50 else "WEAK"
        arrow = "->" if i == 0 else "  "
        print(f"{arrow} {s:5.1f} {band:<6}  {line[:58]}")
        for note in notes:
            print(f"                 {note}")
    print()
    top = ranked[0][0][0] if ranked else 0
    r.add("PASS" if top >= 70 else "WARN" if top >= 50 else "FAIL", "TOP HOOK",
          f"{top:.0f}/100" + ("" if top >= 50 else ". You do not have the hook yet"))


def script_lines(text):
    out = []
    for raw in text.splitlines():
        line = TIMESTAMP.sub("", raw.strip())
        if not line or (line.startswith("[") and line.endswith("]")):
            continue  # blank, or a stage direction like [cut to screen]
        out.append(line)
    return out


def lint_script(text, target, r):
    lines = script_lines(text)
    t = 0.0
    print(f"BEAT SHEET  ·  {WPM} wpm" + (f"  ·  target {target:.0f}s" if target else ""))
    print("=" * 72)
    long_beats = 0
    for i, line in enumerate(lines):
        dur = max(1.0, len(line.split()) / WPM * 60)
        tag = "HOOK" if i == 0 else "CTA" if i == len(lines) - 1 else ""
        flag = "   ^ over 4s on one beat, split it or change the frame" if dur > 4 and i else ""
        long_beats += bool(flag)
        print(f"  {int(t // 60)}:{t % 60:04.1f}  {dur:4.1f}s  {tag:<5} {line[:48]}{flag}")
        t += dur
    print("-" * 72)
    if not lines:
        r.add("FAIL", "SCRIPT", "no spoken lines found")
        return
    hook_dur = max(1.0, len(lines[0].split()) / WPM * 60)
    lvl = "PASS" if hook_dur <= HOOK_MAX_S else "WARN" if hook_dur <= HOOK_MAX_S + 1 else "FAIL"
    r.add(lvl, "HOOK LENGTH", f"{hook_dur:.1f}s" + ("" if lvl == "PASS" else f", aim to land the hook inside {HOOK_MAX_S:.0f}s"))
    first = set(w.lower() for w in re.findall(r"\w{4,}", lines[0]))
    last = set(w.lower() for w in re.findall(r"\w{4,}", lines[-1]))
    shared = first & last
    r.add("PASS" if shared else "WARN", "LOOP", f"last line echoes '{sorted(shared)[0]}'" if shared
          else "last line does not echo the hook. Replays are free reach")
    r.add("PASS" if not long_beats else "WARN", "PACING", f"{long_beats} beat(s) over 4s")
    if target:
        diff = t - target
        r.add("PASS" if abs(diff) <= 5 else "WARN", "RUNTIME", f"{t:.1f}s vs {target:.0f}s target ({diff:+.1f}s)")
    else:
        r.add("PASS" if 7 <= t <= 60 else "WARN", "RUNTIME", f"{t:.1f}s")


def lint_dm(text, r):
    body = text.strip()
    n = len(body)
    r.add("PASS" if n <= DM_MAX else "FAIL", "LENGTH", f"{n} / {DM_MAX} characters")
    if n > BUTTON_TEXT_MAX:
        r.add("WARN", "BUTTON TEXT", f"over {BUTTON_TEXT_MAX}, too long for a button message body")
    paras = [p for p in body.split("\n\n") if p.strip()]
    r.add("PASS" if len(paras) <= 4 else "WARN", "SHAPE", f"{len(paras)} paragraph(s)" + ("" if len(paras) <= 4 else ". A screen of text gets skimmed"))
    if re.search(r"\b(before i send|first tell me|follow me first and)\b", body, re.I):
        r.add("WARN", "GATE", "asks for something before delivering. Deliver first, ask after")
    q = len(re.findall(r"\?+", body))
    r.add("PASS" if q <= 1 else "WARN", "ONE QUESTION", f"{q} question(s)")


def lint_bio(text, r):
    body = text.strip()
    n = len(body)
    r.add("PASS" if n <= BIO_MAX else "FAIL", "LENGTH", f"{n} / {BIO_MAX} characters")
    lines = [l for l in body.splitlines() if l.strip()]
    r.add("PASS" if len(lines) <= 4 else "WARN", "LINES", f"{len(lines)} line(s)")
    has_cta = re.search(r"\b(dm|comment|tap|click|book|join|get|grab|download|shop)\b", body, re.I) or chr(0x1F447) in body
    r.add("PASS" if has_cta else "WARN", "CTA", "has a call to action" if has_cta else "no action for a visitor to take")
    r.add("PASS" if NUMBER.search(body) else "WARN", "PROOF", "has a number or specific" if NUMBER.search(body)
          else "no proof. Add a real number or credential if you have one")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("file", help="text file, or - for stdin")
    ap.add_argument("--mode", choices=["caption", "hook", "script", "dm", "bio"], default="caption")
    ap.add_argument("--keywords", default="", help="comma-separated search terms the caption should contain")
    ap.add_argument("--target", type=float, default=0, help="target reel length in seconds (script mode)")
    ap.add_argument("--wpm", type=int, default=0, help="speaking pace in words per minute (script mode)")
    ap.add_argument("--fix", action="store_true", help="print the cleaned text")
    ap.add_argument("--write", action="store_true", help="with --fix, overwrite the input file")
    a = ap.parse_args()

    global WPM
    if a.wpm:
        WPM = a.wpm
    raw = sys.stdin.read() if a.file == "-" else open(a.file, encoding="utf-8-sig").read()
    cleaned, changes = clean(raw)
    text = cleaned
    r = Report()

    if not text.strip():
        r.add("FAIL", "INPUT", "nothing to check, the text is empty")
    elif a.mode == "caption":
        lint_caption(text, [k.strip() for k in a.keywords.split(",") if k.strip()], r)
    elif a.mode == "hook":
        lint_hooks(text, r)
    elif a.mode == "script":
        lint_script(text, a.target, r)
    elif a.mode == "bio":
        lint_bio(text, r)
    else:
        lint_dm(text, r)

    hits, tells = find_slop(text)
    r.add("PASS" if not hits else "WARN", "SLOP WORDS", ", ".join(hits) if hits else "none")
    r.add("PASS" if not tells else "WARN", "AI TELLS", ", ".join(tells) + " (rewrite by hand)" if tells else "none")
    r.add("PASS", "AUTO-CLEANED", "; ".join(changes) if changes else "nothing to clean")
    r.print()

    verdict = ["PASS", "WARN", "FAIL"][r.worst()]
    print(f"\n  VERDICT  {verdict}")
    if a.fix:
        if a.write and a.file != "-":
            open(a.file, "w", encoding="utf-8").write(cleaned)
            print(f"  wrote cleaned text to {a.file}")
        else:
            print("\n--- CLEANED ---\n" + cleaned)
    sys.exit(r.worst())


if __name__ == "__main__":
    main()
