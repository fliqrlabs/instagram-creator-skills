---
name: growth-audit
description: >-
  Audit what a creator has already posted and say what to do next: real outliers against the account's
  own median, sends/saves/comments per reach, formats and hooks that win, automation funnel performance,
  follower growth, and a short "do more / stop / test" plan. Reads live insights through the Fliqr AI
  connector, or works from pasted insights and screenshots. Use when the creator says "what's working",
  "audit my account", "why did this flop", "why is my reach down", "read my analytics", "monthly report",
  "what should I do more of", or "how are my automations doing".
argument-hint: "[period: 7d / 30d / 90d] [@account]"
---

# growth-audit

Every rule in every Instagram guide, this pack included, is a starting assumption. A creator's own last 30 posts are the evidence. This skill reads that evidence and turns it into three decisions.

Read: `../../references/algorithm.md` (the metrics) and `../../references/connectors.md`.

## Collect

**Connected:**
1. `get_profile`: followers and plan.
2. `get_account_insights` with `period: 30d` (or whatever the creator asked for): reach, views, accounts engaged, interactions, profile views, website clicks, follower growth. Run it a second time for the previous equal-length period (`since`/`until`) to get the trend.
3. `list_media` with `limit: 25, include_insights: true` (only the first 25 items on a page get insights). For more history, fetch the next page with `next_cursor` and merge. Save the items to `posts.json`.
4. `list_automations`: each automation's `total_triggers` and which post it's attached to.

**Offline:** ask for per-post insights (views, reach, saves, shares, comments, follows) for the last 15-30 posts. Screenshots are fine; transcribe them into a table first. The single most valuable screenshot is the retention graph of the best and the worst recent reel.

## Compute

Run the ranker instead of eyeballing it (`python` on Windows):
```bash
python3 scripts/outliers.py posts.json --top 5
```
It ranks every post by its multiple of the account's median views (falling back to reach), and prints sends, saves and comments per reach. Posts with no insights are left out, and it says how many. It also takes a CSV export.

**Retention graphs** (if the creator shares screenshots): read where the curve drops. A cliff in the first 3s means the hook failed. A slow slide in the middle means the beats are too long or nothing changes on screen. A bump near the end means people rewatched the payoff, so the loop worked. Name the second where each drop happens and the line of script it matches.

Then compare the top 5 with the bottom 5 on: format (reel / carousel / image), hook formula (classify it with `../../references/hooks.md`), length, topic or pillar, keyword CTA (yes/no), posting day and time. Check day and time **last**, and only if nothing else explains the difference.

## Funnel check (connected)

For each automation attached to a post: `total_triggers` against that post's comment count.
- triggers ≈ keyword-like comments → the funnel is healthy
- far fewer triggers than comments asking for the thing → the keyword variants are missing (send to `comment-mining`)
- a top post with **no automation** → leads left on the table. Flag it first.

DM opens and link clicks are not tracked by the connector yet. Don't claim them.

## Output

```
GROWTH AUDIT  ·  @handle  ·  last 30d vs previous 30d  ·  sources: get_account_insights, list_media, list_automations

PULSE      reach 182K (+34%)  ·  followers +1,204  ·  profile views 9.1K  ·  website clicks 312
OUTLIERS   2 posts at 3x+ median (median views 4.1K)
  11.2x  "Your reel went viral. You made ₹0."   reel 24s  hook #13  keyword ✓  sends 2.1%/reach
   4.0x  "3 DM mistakes"                         carousel  hook #8   keyword ✗  saves 3.4%/reach
FLOPS      0.3x  talking-head tips with no number in the hook (3 of the bottom 5)
FUNNELS    "PLAN": 318 triggers on 402 comments ✓ · top carousel has NO automation ✗

DO MORE    1. Hidden-cost hooks (#13) with a keyword CTA. Both outliers had a specific ₹ number
STOP       2. Generic tips with no number. 3 of the bottom 5
TEST       3. Next carousel: add keyword GUIDE + automation. Compare comment rate with the last one
```

**Three actions, no more.** Each one names the evidence it's based on. With fewer than 10 posts, say the sample is too small and keep the conclusions provisional.

## After

Offer to write the findings into the creator profile's "What's worked before" section (needs their yes), then point to `content-plan` to plan next week around the DO MORE line.

## Rules

- Rank by multiple and sends per reach, never by raw views alone.
- Every number names its source tool and period. Never estimate a missing metric.
- Meta only returns audience breakdowns (age, gender, city) for larger accounts. If they're empty, say so.
- Conclusions the creator won't like are still conclusions. Say them kindly and clearly.
