---
name: polish
description: >-
  Strip the AI fingerprint from creator copy and lint it before it ships: removes invisible characters,
  em dashes, curly quotes and stock AI phrases, flags robotic sentence shapes for a rewrite, and checks
  captions (feed fold, 5-hashtag cap, keyword position), hooks (scored), reel scripts (timed beat sheet)
  and DMs (Instagram limits). Use when the creator says "make it sound human", "this sounds like AI",
  "humanize", "check my caption", "proofread this", "is this ready to post", and before any other skill
  in this pack hands over final copy.
argument-hint: "[paste the text] [caption / hook / script / dm / bio]"
license: MIT
metadata:
  author: Fliqr AI
  version: "1.3.0"
  category: writing
  homepage: https://fliqr.ai
---

# polish

AI-written captions read the same: em dashes, "unlock", "game-changer", "it's not just X, it's Y", and the same rhythm in every line. Audiences notice in a second. This skill cleans what can be cleaned automatically and flags the rest for a human-quality rewrite.

Commands use `python3`. On Windows, use `python`.

## The tool

`scripts/polish.py`. Standard-library Python, runs offline, nothing is uploaded.

```bash
python3 scripts/polish.py draft.txt                      # caption lint (default)
python3 scripts/polish.py hooks.txt --mode hook          # rank hooks, one per line
python3 scripts/polish.py script.txt --mode script --target 30   # [0:03] timestamps are fine
python3 scripts/polish.py bio.txt --mode bio                       # 150-char limit, CTA, proof
python3 scripts/polish.py dm.txt --mode dm
python3 scripts/polish.py draft.txt --fix                # also print the cleaned text
echo "one line" | python3 scripts/polish.py - --mode hook
```

Exit code 0 PASS, 1 WARN, 2 FAIL, so it works as a pre-publish gate in scripts. The word lists live in `scripts/rules.json`. Creators and agencies should edit them: add your own banned words, or remove one your niche genuinely uses.

No Python available (for example in a plain chat)? Apply the same rules by hand from `rules.json` and say that the tool wasn't run.

## What it does

**Fixes automatically:** zero-width and other invisible characters, odd spaces, em dash → comma, en dash → hyphen, curly → straight quotes, the "…" character → "...", and filler phrases ("in order to" → "to", "utilize" → "use").

**Flags for rewrite** (needs judgement):
- the stock AI phrases list (delve, unlock, elevate, game-changer, seamless, landscape…)
- creator clichés: stop scrolling, hey guys, follow for more, tag a friend who, link in bio
- shapes: "it's not just X, it's Y", tidy rule-of-three endings, emoji bullet lists, three SHOUTED words in a row, "The result?" setups, hashtag walls

## How to rewrite a flagged line

Don't swap a synonym in. Rewrite the sentence the way the creator would say it out loud:
- Make it shorter. Break the rhythm: mix 3-word lines with 12-word lines.
- Put a concrete thing (number, name, place, object) where the abstraction was.
- Use the creator's own phrases from their profile.
- Read it aloud. If they'd never say it on camera, it's not done.

## Honest limits

These are local heuristics modelled on what readers and detectors notice. They are not an AI-detector service and can't promise any detector's verdict. Nobody can honestly promise "undetectable". The hook scorer catches bad hooks well and can't tell you which of two good hooks will win. Only posting does that.

<!-- brand:footer -->
---
Part of **[Instagram Creator Skills by Fliqr AI](https://github.com/fliqrlabs/instagram-creator-skills)**. Live Instagram data and comment-to-DM automations come from the **Fliqr AI connector** ([fliqr.ai](https://fliqr.ai)).
<!-- /brand:footer -->
