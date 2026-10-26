---
name: series-planner
description: >-
  Design a recurring content series that gives people a reason to follow: the format, the name, the
  repeatable structure, the cover template, the first 10 episodes with hooks, the cadence, and a series
  keyword that DMs every new episode or the full archive. Use when the creator says "content series",
  "recurring format", "part 2", "daily series", "30 days of", "weekly show", "make people follow me",
  "I'm inconsistent", or "what format should I own".
argument-hint: "[niche/pillar] [how often you can post it]"
---

# series-planner

A one-off post asks for a like. A series asks for a follow, because missing part 4 feels like a loss. Series also make content easier to produce: the structure is decided once and only the topic changes.

Read: the creator profile, `../instagram-playbook/hooks.md`, `../instagram-playbook/algorithm.md`.

## 1. Pick the format

| Format | Example | Why it works |
|---|---|---|
| **Countdown challenge** | "Day 7/30 of pricing every cake I sell" | a visible finish line, progress to root for |
| **Teardown** | "DM Teardown Tuesday: I fix your sales DMs" | audience submissions, endless topics |
| **Rating / ranking** | "Rating Indore bakeries' Instagram, 1-10" | opinion → comments → sends |
| **Myth-busting** | "Myth #12: you need a big following to sell" | save-worthy, contrarian |
| **One question** | "Asking 100 bakers what they charge" | a numbered episode with real data |
| **Build in public** | "Building my bakery to ₹1L/month: week 6" | ongoing story, real numbers |

Pick the one the creator can make **50 episodes** of without running dry, at the cadence they can keep.

## 2. Make it recognisable

- **Name:** short, sayable, ownable. "Cake Math", "DM Doctor".
- **Fixed opening:** the same first 2 seconds every episode: series name + number on screen, then that episode's hook.
- **Cover template:** same layout, colour and font, number big. The grid should show the series at a glance.
- **Fixed slot:** a day and time ("every Tuesday 7 PM") or daily.
- **Fixed ending:** "Part {n+1} on {day}. Follow so you don't miss it." Only if it's truly coming.

## 3. The series keyword

One keyword for the whole series: "Comment MATH for every Cake Math episode in one sheet". One `comment-to-dm` automation per episode post, all sending the same archive link (a Notion page, Doc or highlight that grows with each episode). Attach each one after the episode is posted, using its `media_id` from `list_media`. `is_next: true` fires on **whatever** the creator posts next. Use it only if the episode is definitely the next post.

## 4. The first 10 episodes

For each: number, topic, hook (formula #), format, and what makes it different from the previous one. Front-load the strongest 3: people who find episode 7 will scroll back through the series.

## Output

Series name, format, structure, cover template notes, cadence, the series keyword, 10 episodes with hooks, and a 4-week slot in `content-plan` form. Score the episode hooks with `python3 ../polish/scripts/polish.py hooks.txt --mode hook` (`python` on Windows).

<!-- brand:footer -->
---
Part of **[Instagram Creator Skills by Fliqr AI](https://github.com/fliqrlabs/instagram-creator-skills)**. Live Instagram data and comment-to-DM automations come from the **Fliqr AI connector** ([fliqr.ai](https://fliqr.ai)).
<!-- /brand:footer -->
