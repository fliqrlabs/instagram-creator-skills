---
name: reel-script
description: >-
  Turn one raw idea into a shoot-ready Instagram Reel: a scored hook, the spoken script in the creator's
  voice, on-screen text with timings, shot notes per beat, a payoff held to the end, a loop, and a keyword
  CTA wired to a comment-to-DM funnel. Use when the creator says "write a reel", "script this", "make a
  reel about X", "what should I say in this video", "voiceover for", "turn this into a reel", or is about
  to record and has no script.
argument-hint: "[the idea, story or result] [length: 15/30/45s]"
license: MIT
metadata:
  author: Fliqr AI
  version: "1.3.0"
  category: create
  homepage: https://fliqr.ai
---

# reel-script

A Reel is decided in 2 seconds, kept by the next 5, and finished only if the payoff is held to the end. This skill writes all three, then connects the reel to a funnel so the views turn into DMs.

Read: the creator profile, `../instagram-playbook/hooks.md`, `../instagram-playbook/algorithm.md`, `../instagram-playbook/safety.md`. Commands use `python3`. On Windows, use `python`.

## 1. Before writing

- **One idea per reel.** If the idea has two, you have two reels. Say so and pick one.
- **Get the specific.** What happened, the number, the before and after. Ask once, in a batch, if it's missing.
- **Pick the goal:** SEND / SAVE / COMMENT / FOLLOW / LEAD. LEAD means a keyword CTA and a funnel.
- **Format:** talking head, voiceover with B-roll, screen recording, faceless text, or a skit. Take it from the profile, or ask.

## 2. The shape

```
0:00-0:03   HOOK      motion in frame 1 + on-screen line at once; spoken line (~9 words) lands inside 3s
0:03-0:06   STAKE     why this matters to the viewer. One line. "If you sell on Instagram, this is costing you."
0:06-…      BODY      one point per beat, a new visual every 2-4s, re-hook at ~4s, ~9s and ~15s
LAST 4s     PAYOFF    deliver exactly what the hook promised
LAST LINE   CTA+LOOP  one ask. Echo a word from the hook so the replay feels seamless.
```

**Hold the payoff to the end.** Promise it early ("the third one is the one that worked") and make them wait for it. Number the beats so they can see where the finish line is. Never resolve the loop in the middle.

## 3. Write it

1. Write 3 hooks from 3 different formulas. Score them with `python3 ../polish/scripts/polish.py hooks.txt --mode hook`, then pick the top one.
2. Write the script on the winner, in the creator's spoken voice: contractions, short lines, their language mix. Nothing they'd need to rehearse.
3. **Time it:**
   ```bash
   python3 ../polish/scripts/polish.py script.txt --mode script --target 30
   ```
   One line per beat. Fix every flag: a hook over 3s, a beat over 4s, no loop. Re-run until it's clean.
4. Write the **on-screen text** as a separate track. 6 words or fewer per card, the hook card up at frame 1, burned-in captions for the body. Keep it inside the safe zone (out of the top ~230px, the bottom ~480px and the right ~230px of 1080x1920).
5. **Shot notes** per beat: what's on screen. Face, hands, screen recording, B-roll or text. A static shot for more than 4s is where people leave.
6. **Cover frame:** the hook text, big and centred (the grid crops reels to 3:4). The cover is the reel's thumbnail on the profile, so it needs to sell on its own.

## 4. The CTA

Pick **one**:
- **LEAD:** "Comment PLAN and I'll send you the template." Then hand off to `comment-to-dm`. The caption's first line repeats the keyword.
- **SAVE:** "Save this for your next shoot."
- **SEND:** "Send this to the friend who still edits for 6 hours."
- **FOLLOW:** "Part 2 tomorrow." Only if part 2 actually exists.

For LEAD reels, say the keyword out loud **and** put it on screen in the last 3 seconds.

## 5. Output

````
REEL  ·  30s  ·  goal LEAD  ·  talking head + screen recording

HOOK (scored 92, Time Collapse)
  spoken:     "Editing one reel took me 6 hours. Now it's 40 minutes."
  on-screen:  6 HRS → 40 MIN
  frame 1:    timeline scrubbing at 4x

SCRIPT
```
[0:00] Editing one reel took me 6 hours. Now it's 40 minutes.
[0:03] And it's not a new app.
[0:05] It's the order I edit in.
…
[0:26] Comment EDIT and I'll send you my exact template. Six hours, gone.
```

ON-SCREEN TRACK      0:00 6 HRS → 40 MIN · 0:05 IT'S THE ORDER · … · 0:26 COMMENT "EDIT"
SHOT LIST            beat-by-beat
CAPTION              → run `caption` next (keyword in line 1)
FUNNEL               → run `comment-to-dm` with keyword EDIT → the template link
CHECKS               hook 2.6s ✓ · loop "six hours" ✓ · longest beat 3.4s ✓ · polish PASS
````

## 6. Log it

When the creator approves the final script, append one line to the post log (format in `../instagram-playbook/post-log.md`): date, `reel`, pillar, goal, hook formula, the spoken hook, length, and keyword. That's what lets `growth-audit` say which formulas win for this creator.

## Rules

- No greeting, no intro, no "in this video".
- Don't build a script around trending audio the creator can't use. Original audio with a voiceover is safer, and it's original.
- Never fabricate results. Use `{{your number}}`.
- When remixing someone else's viral reel, copy the **structure**, never the words. Use `trend-remix`.

<!-- brand:footer -->
---
Part of **[Instagram Creator Skills by Fliqr AI](https://github.com/fliqrlabs/instagram-creator-skills)**. Live Instagram data and comment-to-DM automations come from the **Fliqr AI connector** ([fliqr.ai](https://fliqr.ai)).
<!-- /brand:footer -->
