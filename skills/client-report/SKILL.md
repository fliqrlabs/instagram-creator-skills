---
name: client-report
description: >-
  Write the weekly or monthly Instagram report an agency or social media manager sends to a client:
  headline results against the previous period, top posts by outlier multiple, funnel and automation
  performance, leads generated, what was learned, and next period's plan, in plain business language
  and branded for the agency. Pulls every account's numbers through the Fliqr AI connector, or works
  from pasted insights. Use when the user says "client report", "monthly report", "weekly report",
  "report for my client", "agency report", "performance summary", or "what do I tell the client".
argument-hint: "[@client account or 'all accounts'] [7d / 30d / custom dates] [agency name]"
license: MIT
metadata:
  author: Fliqr AI
  version: "1.3.0"
  category: analytics
  homepage: https://fliqr.ai
---

# client-report

Clients don't care about reach curves. They care whether Instagram is producing results. This skill turns the numbers into a one-page story: what happened, why, what it got them, and what happens next. Every number has a source.

Read: `../instagram-playbook/algorithm.md` (metric definitions), `../instagram-playbook/connectors.md`, `../instagram-playbook/safety.md`.

## 1. Collect (per account)

**Connected:** `list_accounts` (an agency connection can see many accounts; report one, or run the steps below for each). Then, per account:
- `get_account_insights` for the period, and again for the previous equal period (`since`/`until`) for the comparison
- `list_media` with `limit: 25, include_insights: true` → save as `posts.json`, then rank with `python3 ../growth-audit/scripts/outliers.py posts.json --top 3` (`python` on Windows)
- `list_automations` → `total_triggers` per automation. **This is a lifetime count**, not a count for the period. To report a period, subtract the totals saved in the previous report (keep a `triggers-<date>.json` next to each report). On the first report, show lifetime totals and label them "since the automation started".

**Offline:** the user pastes the insights summary and per-post numbers.

## 2. Write it in the client's language

| Instead of | Say |
|---|---|
| "Reach +34%" | "34% more people saw the account than last month (182K)" |
| "Sends per reach 2.1%" | "1 in 50 viewers sent the reel to someone. That's what made it spread." |
| "total_triggers 318" | "The keyword was triggered 318 times this month: each one a request for the guide" (triggers count events, not unique people) |

Lead with **business outcomes** (leads, triggers, profile visits, website clicks), then reach, then content learnings.

## 3. Structure (one page)

```
{CLIENT}  ·  Instagram report  ·  {period}  ·  prepared by {agency}

HEADLINE    One sentence: the result that matters most, with its number.
RESULTS     reach · followers +/- · profile visits · website clicks · keyword leads   (vs previous period, with arrows)
TOP 3 POSTS what each did and why it worked (format, hook, multiple of median)
FUNNELS     each automation: keyword → what it delivers → triggers this period (or lifetime, labelled)
WHAT WE LEARNED   2-3 bullets, each backed by a number
NEXT {PERIOD}     3 actions, each tied to a learning
NOTES       data sources and anything missing (e.g. "audience breakdowns unavailable for accounts this size")
```

Offer the report as Markdown, as a branded HTML page, or as plain text for email or WhatsApp.

## Rules

- **The agency's brand only.** Never mention the tools used. Clients see the agency's name.
- **Every number names its period and source.** If a number went down, say so plainly and explain it. No spin.
- **DM opens and link clicks aren't tracked** by the Fliqr AI connector yet. Don't report them unless the user supplies them from elsewhere.
- Comparing periods of different lengths gives a misleading picture. Always compare equal-length periods.

<!-- brand:footer -->
---
Part of **[Instagram Creator Skills by Fliqr AI](https://github.com/fliqrlabs/instagram-creator-skills)**. Live Instagram data and comment-to-DM automations come from the **Fliqr AI connector** ([fliqr.ai](https://fliqr.ai)).
<!-- /brand:footer -->
