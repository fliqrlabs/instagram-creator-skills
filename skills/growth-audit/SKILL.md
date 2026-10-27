---
name: growth-audit
description: >-
  Audit what a creator has already posted and say what to do next: real outliers against the account's
  own median, hold at 3 seconds, non-follower reach, which hook formulas win (from the post log), a
  hook-vs-profile-vs-topic diagnosis, funnel performance, and a "do more / stop / test" plan with stated
  confidence. Reads live insights through the Fliqr AI
  connector, or works from pasted insights and screenshots. Use when the creator says "what's working",
  "audit my account", "why did this flop", "why is my reach down", "read my analytics", "monthly review",
  "what should I do more of", or "how are my automations doing".
argument-hint: "[period: 7d / 30d / 90d] [@account]"
license: MIT
metadata:
  author: Fliqr AI
  version: "1.3.0"
  category: analytics
  homepage: https://fliqr.ai
---

# growth-audit

Every rule in every Instagram guide, this pack included, is a starting assumption. A creator's own last 30 posts are the evidence. This skill reads that evidence and turns it into three decisions.

Read: `../instagram-playbook/algorithm.md` (the metrics), `../instagram-playbook/connectors.md` and `../instagram-playbook/post-log.md`.

## Collect

**Connected:**
1. `get_profile`: followers and plan.
2. `get_account_insights` with `period: 30d` (or whatever the creator asked for): reach, views, accounts engaged, interactions, profile views, website clicks, follower growth. Run it a second time for the previous equal-length period (`since`/`until`) to get the trend.
3. `list_media` with `limit: 25, include_insights: true` (only the first 25 items on a page get insights). For more history, fetch the next page with `next_cursor` and merge. Save the items to `posts.json`.
4. `list_automations`: each automation's `total_triggers` and which post it's attached to.

**Offline:** ask for per-post insights (views, reach, saves, shares, comments, follows) for the last 15-30 posts. Screenshots are fine; transcribe them into a table first.

**Two numbers the connector can't give you, worth asking for** (from each reel's insights in the Instagram app, for the top 5 and bottom 5 reels):
- **Hold at 3 seconds:** the share of viewers still watching at 3s. Newer app versions show a **skip rate**, and hold at 3s = 100% minus the skip rate. Otherwise read it off the retention graph. This is the hook's real grade.
- **Non-follower reach:** the % of accounts reached who don't follow the creator. It shows whether the post travelled or only reached existing followers.

**The post log** (`../instagram-playbook/post-log.md`): if it exists, join it to the posts (by `media_id`, otherwise by date and the first words of the caption) so every post carries its hook formula, format, pillar and keyword.

## Compute

Run the ranker instead of eyeballing it (`python` on Windows):
```bash
python3 scripts/outliers.py posts.json --top 5
python3 scripts/outliers.py posts.csv --group-by formula   # once the post log gives each post a formula
python3 scripts/outliers.py posts.csv --group-by type      # reel vs carousel vs image
```
It ranks every post by its multiple of the account's median views (falling back to reach), and prints sends, saves and comments per reach. Posts with no insights are left out, and it says how many. `--group-by` gives the median multiple per formula, format or pillar, and flags any group with fewer than 3 posts as an anecdote.

**Retention graphs** (if the creator shares screenshots): read where the curve drops. A cliff in the first 3s means the hook failed. A slow slide in the middle means the beats are too long or nothing changes on screen. A bump near the end means people rewatched the payoff, so the loop worked. Name the second where each drop happens and the line of script it matches.

Then compare the top 5 with the bottom 5 on: hold at 3s, hook formula (from the log, or classify it with `../instagram-playbook/hooks.md`), format, length, topic or pillar, keyword CTA (yes/no), posting day and time. Check day and time **last**, and only if nothing else explains the difference. It's almost never the cause, and it's where people most want it to be.

## Diagnose before you prescribe

Different failures need different fixes. Work out which one it is before recommending anything:

| What the numbers show | The problem | Send to |
|---|---|---|
| Low views **and** low hold at 3s | **Hook.** People leave in the first seconds. | `viral-hooks` |
| Good hold at 3s, views still low | **The middle or the topic.** It holds, but nobody sends it. Check sends per reach. | `reel-script` (pacing), `comment-mining` (topics) |
| High views and high non-follower reach, but few follows | **Profile.** The reel worked; the profile didn't convert the visit. Stop rewriting hooks. | `profile-glowup` |
| High reach, low sends and saves | **Not worth sharing.** Watched, then forgotten. | `instagram-playbook` (what earns sends), `viral-hooks` (SEND formulas) |
| Comments asking for the thing, few triggers | **Funnel.** Missing keyword variants, or no automation. | `comment-mining`, `comment-to-dm` |

## Say how sure you are

State the sample size with every conclusion, in plain words:
- **Under 10 posts:** too few to conclude anything. Say so, and suggest what to test instead.
- **10-30 posts:** an early signal. Keep it provisional, and name what would confirm it.
- **30+ posts:** a pattern you can act on.

A group of 2 posts in `--group-by` is an anecdote, however big its multiple.

## Funnel check (connected)

For each automation attached to a post: `total_triggers` against that post's comment count.
- triggers ≈ keyword-like comments → the funnel is healthy
- far fewer triggers than comments asking for the thing → the keyword variants are missing (send to `comment-mining`)
- a top post with **no automation** → leads left on the table. Flag it first.

DM opens and link clicks are not tracked by the Fliqr AI connector yet. Don't claim them.

## Output

```
GROWTH AUDIT  ·  @handle  ·  last 30d vs previous 30d  ·  sources: get_account_insights, list_media, list_automations

PULSE      reach 182K (+34%)  ·  followers +1,204  ·  profile views 9.1K  ·  website clicks 312
OUTLIERS   2 posts at 3x+ median (median views 4.1K)
  11.2x  "Your reel went viral. You made $0."   reel 24s  #13  hold@3s 71%  58% non-follower  sends 2.1%/reach
   4.0x  "3 DM mistakes"                         carousel  #8                                  saves 3.4%/reach
FLOPS      0.3x  talking-head tips, no number in the hook: hold@3s 34% (3 of the bottom 5)
BY FORMULA #13 Hidden Cost 6.8x (n=4) · #21 Numbered 0.9x (n=6) · unclassified 1.1x (n=9)   [post log, 28 posts: early signal]
DIAGNOSIS  Hook problem, not a topic problem: the top 5 hold 66% at 3s, the bottom 5 hold 33%
           Profile check: "DM mistakes" reached 41% non-followers but converted 0.1% to follows → profile-glowup
FUNNELS    "PLAN": 318 triggers on 402 comments ✓ · top carousel has NO automation ✗

DO MORE    1. Hidden-cost hooks (#13) with a keyword CTA. 6.8x median across 4 posts
STOP       2. Numbered lists with no number in the hook. 0.9x across 6 posts
TEST       3. Next carousel: add keyword GUIDE + automation. Compare comment rate with the last one
CONFIDENCE 28 posts: an early signal. Re-run at 30+.
```

**Three actions, no more.** Each one names its evidence and its sample size.

## After

Offer to write the findings into the creator profile's "What's worked before" section (needs their yes), then point to `content-plan` to plan next week around the DO MORE line, and to `niche-research` to find formulas the creator hasn't tried yet.

## Rules

- Rank by multiple and sends per reach, never by raw views alone.
- Every number names its source tool and period. Never estimate a missing metric.
- Meta only returns audience breakdowns (age, gender, city) for larger accounts. If they're empty, say so.
- Conclusions the creator won't like are still conclusions. Say them kindly and clearly.

<!-- brand:footer -->
---
Part of **[Instagram Creator Skills by Fliqr AI](https://github.com/fliqrlabs/instagram-creator-skills)**. Live Instagram data and comment-to-DM automations come from the **Fliqr AI connector** ([fliqr.ai](https://fliqr.ai)).
<!-- /brand:footer -->
