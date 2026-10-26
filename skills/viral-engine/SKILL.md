---
name: viral-engine
description: >-
  The full pipeline in one command: from an idea (or nothing) to a finished Instagram post with a scored
  hook, script or slides, caption, polish check, and a live comment-to-DM funnel, so the post earns
  reach and turns it into leads. Runs creator-brain, comment-mining, viral-hooks, reel-script or
  carousel, caption, polish and comment-to-dm in order. Use when the creator says "go viral", "make me a
  viral post", "do everything", "full post from this idea", "I want leads from Instagram", "what should
  I post today and set it up", or invokes the engine. Works offline, or with the Fliqr AI connector for live Instagram data.
argument-hint: "[idea, or leave empty to find one from your data] [reel / carousel]"
---

# viral-engine

The other skills each do one job. This one runs the whole loop:

```
 FIND ──► HOOK ──► BUILD ──► CAPTION ──► POLISH ──► FUNNEL ──► (post) ──► MEASURE
  │                                                                          │
  └──────────────────────── next idea comes from what worked ◄───────────────┘
```

Viral reach with no funnel gives you views and ₹0. A funnel with no reach gives you nothing to convert. This engine always builds both.

## 0. Load context

- Look for the creator profile. If there isn't one, run `creator-brain` first. With the Fliqr AI connector it takes about 2 minutes. Without it, ask for 3 captions and the 5 interview questions.
- Check for the Fliqr AI connector (`../instagram-playbook/connectors.md`) and say which mode you're in: "Connected to @handle" or "Offline mode: paste data when I ask".

## 1. FIND (skip if the creator brought an idea)

Connected: run quick versions of `growth-audit` (top 3 outliers: what format and hook formula won) and `comment-mining` (top 3 audience questions). Offline: ask "What did people ask you about most this week?"

Propose **3 ideas**, each with a goal (SEND / SAVE / LEAD), a format, and the evidence behind it. The creator picks one.

## 2. HOOK

Run `viral-hooks`: 6 formulas, scored, top 2 recommended. The creator picks, or you pick and say why.

## 3. BUILD

- Reel → `reel-script` (timed script, on-screen track, shot list)
- Carousel → `carousel` (slide plan + design notes)

## 4. CAPTION

`caption`: the keyword above the fold, ≤5 hashtags, the first comment.

## 5. POLISH

Run `polish` on every piece of text that will be published or sent. Nothing ships while it says FAIL.

## 6. FUNNEL

For LEAD posts, and for any post the creator expects to do well, run `comment-to-dm`. If the keyword has nothing real to deliver yet, run `lead-magnet` first.
- if the post isn't published yet, use `is_next: true` so the automation attaches to the next post
- if it's already live, use its `media_id`

Create it paused, show it, and activate it only on a yes.

## 7. HAND-OFF

One final block the creator can work from:

```
READY TO POST  ·  Reel 28s  ·  goal LEAD  ·  keyword EDIT
✓ hook   92  Time Collapse        ✓ script timed, loop ✓        ✓ polish PASS
✓ caption + first comment         ✓ funnel "EDIT → template" created (paused) ▸ activate?

Post it, then:
  · reply to the first 10 comments yourself in the first hour
  · share it to your story with a "reply EDIT" frame (story-funnel)
  · ask me "growth-audit 7d" next week. I'll check views against your median and triggers against comments
```

With a scheduling connector (`posts.schedule`), offer to queue the post instead of the manual "post it" step.

## Rules

- Each step's gate still applies: no automation goes live and nothing gets published without a yes.
- Never fabricate proof to make a hook stronger. Ask for the real number or use a placeholder.
- If the creator only wants part of the pipeline, run that part. The engine isn't a cage.

<!-- brand:footer -->
---
Part of **[Instagram Creator Skills by Fliqr AI](https://github.com/fliqrlabs/instagram-creator-skills)**. Live Instagram data and comment-to-DM automations come from the **Fliqr AI connector** ([fliqr.ai](https://fliqr.ai)).
<!-- /brand:footer -->
