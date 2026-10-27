# Worked example: one idea → a post with a live funnel

> **Fictional creator, real tool output.** "Meera" is a made-up home baker with 8K followers. Every number here is an example, not a result. The hook rankings, beat sheet and lint results below are the actual output of `polish.py` on the files in this folder. Run them yourself.

The request:

```
/fliqr:viral-engine  reel about how home bakers undercharge. I have a free pricing sheet.
```

## 1. FIND: the evidence

In connected mode, `growth-audit` and `comment-mining` run first. In this example they turned up:

- Meera's best post in 30 days was a 4.2x outlier: a reel about the cost of ingredients.
- Her most common comment question is *"how much do you charge for a cake like this?"*, which came up 63 times.

The idea picked: **pricing, goal LEAD, keyword PRICE, delivering the free pricing sheet.**

## 2. HOOK: five formulas, scored

[`hooks.txt`](hooks.txt) → `python3 skills/polish/scripts/polish.py examples/home-baker/hooks.txt --mode hook`

```
HOOK RANKING
======================================================================
->  93.0 STRONG  You're losing $30 on every cake you sell.
    82.0 STRONG  I undercharged for cakes for 2 years. Here's the math.
    70.0 STRONG  Nobody tells home bakers this about pricing.
                 no number or specific
    70.0 STRONG  Stop selling cakes at a loss
                 no number or specific
     5.0 WEAK    Hi everyone, today we will talk about cake pricing
                 dealbreaker: opens with 'hi everyone'. Nobody came to the feed to be greeted
```

Picked: **#13 The Hidden Cost**. The on-screen text is `-$30 / CAKE`, and frame 1 shows a cake being sliced with a price tag ripping.

## 3. BUILD: the script, timed

[`script.txt`](script.txt) → `--mode script --target 25`

```
BEAT SHEET  ·  180 wpm  ·  target 25s
  0:00.0   2.7s  HOOK  You're losing $30 on every cake you sell.
  0:02.7   3.0s        I did it for two years. Here's the math.
  0:05.7   2.0s        Ingredients, $28. Box and board, $6.
  ...
  0:21.0   3.7s  CTA   Comment PRICE and I'll send it. Stop losing $30
  PASS  HOOK LENGTH        2.7s
  PASS  LOOP               last line echoes 'cake'
  PASS  PACING             0 beat(s) over 4s
  PASS  RUNTIME            24.7s vs 25s target (-0.3s)
```

The payoff ($77 real cost against $47 charged) is held until 0:15. The last line echoes the hook, so the replay loops cleanly.

## 4. CAPTION: linted against the feed fold

[`caption.txt`](caption.txt) → `--keywords "cake pricing,home baker"`

The first draft got `WARN SEARCH TERMS 1/2 present. Missing: cake pricing`. One line was rewritten to include it, and the second pass gave:

```
  WHAT THE FEED SHOWS
  +--------------------------------------------------------+
  | I charged $47 for a cake that cost me $77 to make. For |
  |  2 years. Comment "PRICE" and I'll DM you my free pric |
  | ing sheet 🎂  Most                                      |
  +---------------------------------------------- ... more +
  PASS  KEYWORD CTA        'PRICE' found before the fold
  PASS  HASHTAGS           4 tags #homebaker #cakepricing #homebakingbusiness #cakebusiness
  VERDICT  PASS
```

## 5. FUNNEL: shown, approved, created paused, switched on

```
FUNNEL  ·  "Reel: pricing sheet (PRICE)"
post:          next post you publish (is_next)
trigger:       KEYWORDS  PRICE, price, pricing, price pls, prices
public reply:  6 variations ("Sent! check your DMs 🎂", "In your inbox 📩", …), limit 300
opening DM:    "Hi! Here's the pricing sheet you asked for. Tap below and I'll send it 🎂"  [Send it 📩]
follow gate:   off
delivery DM:   BUTTON  (dm.txt)  [Open pricing sheet → https://…]
AI fallback:   off
Approve?
```

The delivery DM, [`dm.txt`](dm.txt), passes `--mode dm`. It's 175 characters with one question, *"What's the cake you sell the most?"*. That question starts the conversation `dm-closer` takes over.

After a **yes**, the skill calls `create_automation` (paused), checks that each block came back with `is_active: true`, and asks *"Switch it on now?"*. On **"on"** it calls `set_automation_status: active`, then adds a line to Meera's post log (formula #13, keyword PRICE).

## 6. A week later: MEASURE

`growth-audit 7d` reads the post log, compares the reel's views with Meera's median and its 3-second hold with her other reels, and checks PRICE triggers against comments. Its findings go into the "What's worked before" section of her `creator-profile.md`, so the next idea starts from evidence.
