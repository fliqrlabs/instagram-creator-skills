---
name: content-plan
description: >-
  Plan a week or month of Instagram content where every post has a goal, a format, a hook formula, a
  CTA and (for lead posts) a keyword funnel, built on the creator's pillars and real performance data.
  Use when the creator says "plan my week", "content calendar", "what should I post this week", "30 days
  of content", "content pillars", "posting schedule", "launch plan", or "I'm inconsistent". With the
  Fliqr AI connector it plans around the creator's actual winners and comment demand.
argument-hint: "[week / month] [goal: growth / leads / launch] [posts per week]"
---

# content-plan

Consistency beats volume, and a plan beats both. This skill plans posts that each do one job, and wires the lead posts to funnels before they go out.

Read: the creator profile (pillars, offer, what's worked), `../instagram-playbook/hooks.md`, `../instagram-playbook/algorithm.md`.

## Inputs

- **Goal** for the period: growth, leads, launch or brand deals. It sets the mix below.
- **Capacity:** realistic posts per week. Fewer and better wins. Default to 4 feed posts plus daily stories.
- **Evidence:** in connected mode, run a quick version of `growth-audit` (top 5 outliers) and `comment-mining` (top 5 questions). Offline, ask what did well recently and what people keep asking.
- **Dates that matter:** a launch, sale, holiday or seasonal moment your audience celebrates (Black Friday, Christmas, Lunar New Year, Ramadan, Diwali, back-to-school), or an event in the niche.

## The mix

| Goal | Reach (SEND/FOLLOW) | Trust (SAVE) | Convert (LEAD) |
|---|---|---|---|
| Growth | 60% | 30% | 10% |
| Leads | 30% | 30% | 40% |
| Launch (the week before) | 30% | 20% | 50%, plus a story-funnel every day |

Every **LEAD** post gets a keyword and a lead magnet that exists. Missing a magnet? Plan the magnet first (a checklist, template or mini-guide). It can be one carousel's content repackaged as a PDF.

## Planning rules

- **Read the post log** (`../instagram-playbook/post-log.md`) if it exists. No pillar or formula repeats from the last 2 weeks, and the formulas `growth-audit` found winning get the big-swing slots.

- **Rotate pillars and formulas.** No pillar twice in a row, and no hook formula repeated within a week.
- **Series beat one-offs.** "Day 1/7", "Part 2", recurring formats ("DM Teardown Tuesday") give people a reason to follow. Design one with `series-planner`.
- **Launching something?** Use `launch-campaign` for the launch window instead. It plans the warm-up, open-cart and close phases and their automations.
- **Have long-form content?** `repurpose` turns one video or podcast into a week of posts.
- **Reels drive reach, carousels drive saves, stories drive sales.** Use each for its job.
- **One big swing a week:** the post you'd be proud of if it blew up. Give it the best hook and a funnel.
- **20 minutes of engagement a day**, before posting rather than after: the `engagement-round` list of 10 accounts. It's growth that doesn't need another post.
- **Timing matters far less than the first two seconds.** Post when the audience is awake (check insights), but if the creator is optimising posting times before their hooks hold, say so.
- **Reuse winners.** A 5x outlier from last month deserves a sequel, a new angle, or the carousel version.

## Output

```
WEEK OF {date}  ·  goal LEADS  ·  4 posts + daily stories  ·  evidence: 2 outliers, top question "how to set up auto-DM"

DAY  FORMAT    PILLAR      GOAL   HOOK (formula)                                   CTA / FUNNEL
Mon  Reel      Automation  SEND   "Your reel went viral. You made $0." (#13)      comment "DM" → setup guide [new automation]
Tue  Story     —           LEAD   problem → poll → "reply GUIDE"                  story automation GUIDE
Wed  Carousel  DMs         SAVE   "7 DM mistakes (I made #4 for a year)" (#8)     save + comment "GUIDE" [reuse automation]
Fri  Reel      Results     FOLLOW "I let AI reply to my comments for 7 days" (#10) "Day 8 tomorrow"
Sun  Reel      Personal    SEND   POV (#16)                                        send to a friend
FUNNELS TO SET UP: 2 (DM, GUIDE). Run comment-to-dm when each post is ready.
ENGAGE DAILY: 20 min before posting · 5 reach / 3 peers / 2 buyers → engagement-round
```

Then offer: script the big swing now (`reel-script`), write the carousel (`carousel`), or set up the funnels (`comment-to-dm`, needs the posts live or `is_next`). With a scheduling connector (`posts.schedule` in `../instagram-playbook/connectors.md`), offer to queue the finished posts. Without one, give a copy-ready list.

<!-- brand:footer -->
---
Part of **[Instagram Creator Skills by Fliqr AI](https://github.com/fliqrlabs/instagram-creator-skills)**. Live Instagram data and comment-to-DM automations come from the **Fliqr AI connector** ([fliqr.ai](https://fliqr.ai)).
<!-- /brand:footer -->
