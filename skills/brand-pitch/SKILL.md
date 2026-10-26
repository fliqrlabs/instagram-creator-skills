---
name: brand-pitch
description: >-
  Win brand deals and collabs: a one-page media kit built from the creator's real Instagram insights, a
  short personalised pitch DM or email to a brand, a collab pitch to another creator, rate guidance by
  deliverable, and the deliverables brief once a deal lands, including a comment-to-DM funnel the brand
  can track. Use when the creator says "pitch a brand", "media kit", "rate card", "how much should I
  charge", "collab with @x", "brand reached out", "UGC pitch", or "sponsorship". Works offline, or with the Fliqr AI connector for live Instagram data.
argument-hint: "[brand or creator name + what you'd make for them]"
---

# brand-pitch

Brands buy outcomes, not follower counts. This skill pitches with real numbers and a mechanism most creators can't offer: a comment-to-DM funnel that turns a sponsored reel into measurable leads.

Commands use `python3`. On Windows, use `python`.

Read: the creator profile, `../instagram-playbook/safety.md`, `../instagram-playbook/connectors.md`.

## 1. The media kit (real numbers only)

Connected: `get_profile`, `get_account_insights` (`period: 90d`, `breakdowns: ["age_gender", "city", "country"]`, which Meta only provides for larger accounts), and `list_media` with insights for the last 30 posts. Offline: ask for the same numbers from Insights.

One page:
- Who the creator is, in one line, plus their niche and audience in one line (top cities and age band if available)
- Followers, 90-day reach, median reel views, average sends and saves per reach
- 3 best posts with their numbers (outlier multiple)
- Funnel proof: keyword automations and their `total_triggers` ("one reel → 1,240 keyword triggers, each one a viewer asking for the offer by name"). Say "triggers", never "DMs delivered" or "clicks". The Fliqr AI connector doesn't track delivery or clicks yet, and overstating numbers to a brand is a fast way to lose the deal.
- Past brands (only real ones), and contact

Every number names its period. Never round up generously or invent a figure. If the numbers are small, sell the niche fit and the engagement depth instead.

## 2. The pitch

**Brand pitch (DM or email), 5 lines:**
1. A specific observation about the brand: a recent launch, campaign or product. Never generic praise.
2. The idea: one concrete reel or series concept in their world.
3. Why the creator: audience fit plus one number.
4. The mechanism: "Viewers comment {KEYWORD} → get your offer code in their DMs instantly. You get comment and trigger counts, not just views. Track sales with a unique code or link."
5. A small ask: "Want me to send the concept and rates?"

**Creator collab pitch:** what you've watched them do, the specific collab idea (a Collab post lands on both grids), what each side does, and why both audiences win.

Lint it with `python3 ../polish/scripts/polish.py pitch.txt --mode dm`. Run no outreach automation. Pitches are sent by hand, one at a time.

## 3. Rates (guidance, not a quote)

Give a range, never a single number. Base it on the creator's median views, niche and deliverables (a reel, a story set, a carousel, usage rights, exclusivity, whitelisting or paid usage). State the assumptions. Usage rights and exclusivity are separate line items. Many creators forget to charge for them. If the creator's market data differs, theirs wins.

## 4. After the deal: the deliverables brief

Concept, script (via `reel-script`), on-screen disclosure (#ad or the Paid partnership label, always), the keyword funnel config (via `comment-to-dm`, with the brand's link and code in the DM), the posting date, and what gets reported back afterwards (views, reach, sends, saves, comments, triggers).

## Never

Fake past collaborations, inflated numbers, bought-follower accounts presented as organic, or undisclosed paid content.

<!-- brand:footer -->
---
Part of **[Instagram Creator Skills by Fliqr AI](https://github.com/fliqrlabs/instagram-creator-skills)**. Live Instagram data and comment-to-DM automations come from the **Fliqr AI connector** ([fliqr.ai](https://fliqr.ai)).
<!-- /brand:footer -->
