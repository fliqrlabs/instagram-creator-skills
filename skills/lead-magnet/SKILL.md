---
name: lead-magnet
description: >-
  Create the free thing a keyword delivers: a checklist, template, swipe file, mini-guide, calculator,
  resource list or mini-course, with a title that makes people comment, the full content written in the
  creator's voice, a one-page layout, the delivery format, and a bridge to the paid offer. Use when the
  creator says "lead magnet", "freebie", "what should my keyword send", "make a free guide", "I need
  something to give away in DMs", "comment X to get Y but I don't have Y yet", or before any
  comment-to-dm funnel that has nothing to deliver.
argument-hint: "[topic] [who it's for] [the paid offer it should lead to]"
---

# lead-magnet

A keyword CTA is only as strong as what it promises. "Comment GUIDE for my guide" gets shrugs. "Comment PRICE for the sheet that told me I was losing ₹300 a cake" gets hundreds. This skill designs the promise and then writes the thing itself, so the funnel has something worth sending.

Read: the creator profile (offer, audience, proof), `../instagram-playbook/safety.md`.

## 1. Pick the format

| Format | Best when | Effort to make |
|---|---|---|
| **Checklist** | the audience keeps missing steps | 30 min |
| **Template / swipe file** | they need words or a structure (scripts, DMs, captions, contracts) | 1 hr |
| **Calculator / sheet** | money, time or quantities are involved (pricing, macros, budgets) | 1-2 hr |
| **Resource list** | the creator has tested tools, suppliers, places | 30 min |
| **Mini-guide (5-7 pages)** | a process that needs explaining | 2-3 hr |
| **Video mini-lesson / 3-day DM course** | the creator teaches better on camera | 1-2 hr |

Rule: **solve one specific problem fast.** A 40-page ebook loses to a 1-page checklist almost every time. People comment for a quick win.

## 2. Name it so people comment

Title formula: **[specific result] + [specific format] + [proof or speed]**.
- ✗ "Baking Business Guide"
- ✓ "The Cake Pricing Sheet (finds your real cost in 2 minutes)"
- ✓ "31 DM Replies That Booked My Calls"

The keyword is one word from the title: PRICE, REPLIES, PLAN.

## 3. Write it

Write the **whole thing**, not an outline, in the creator's voice:

- **Page 1:** title, a one-line promise, and who it's for. Then straight into the value. No three-paragraph intro.
- **Body:** numbered steps, fill-in-the-blank templates, or a table. Every line usable. Add a real example under each step, from the creator's proof bank or clearly marked `{{your example}}`.
- **Quick win in the first 2 minutes.** Put the most useful item first.
- **Last page, the bridge:** "Want me to do this with you? {offer} → {link}". One line, no pressure.

For calculators, give the exact column layout and the formulas (Google Sheets syntax), so the creator can build it in 10 minutes.

## 4. Delivery

- **Where it lives:** a Google Doc or Sheet, a Notion page, a Canva PDF, or a hosted page. Pick what the creator already uses. For Google Docs and Sheets: set sharing to "Anyone with the link can view", then change the end of the link from `/edit` to `/copy`. People get their own copy instead of requesting edit access.
- **If they want emails or phone numbers:** say so honestly in the opening DM ("I'll send it to your email so you can keep it"), and collect them with a lead-capture flow in the dashboard (the Fliqr AI connector can't build these yet). Ask for clear consent and say what it's for: "Can I email you the sheet and my weekly baking tips? You can unsubscribe anytime". India's DPDP Act and most privacy laws require consent for a stated purpose. Never secretly gate a "free" promise.
- **Test the link** from a logged-out browser before the funnel goes live.

## Output

```
LEAD MAGNET  ·  checklist  ·  for {who}  ·  bridges to {offer}
TITLE        "{title}"
KEYWORD      {WORD}  (+ variants)
PROMISE LINE "Comment {WORD} and I'll DM you {title}"   (for caption + reel CTA)

--- CONTENT ---
{the full thing}

DELIVERY     {format + where + sharing setting}
NEXT         comment-to-dm with keyword {WORD} → this link
```

Run the copy through `python3 ../polish/scripts/polish.py magnet.txt --mode caption` (`python` on Windows). Ignore the fold and hashtag checks for this.

## Never

- Never promise something the magnet doesn't contain.
- Never invent results or testimonials to make it look proven.
- Never write a regulated claim (health outcomes, income, investment returns) as a promise.

<!-- brand:footer -->
---
Part of **[Instagram Creator Skills by Fliqr AI](https://github.com/fliqrlabs/instagram-creator-skills)**. Live Instagram data and comment-to-DM automations come from the **Fliqr AI connector** ([fliqr.ai](https://fliqr.ai)).
<!-- /brand:footer -->
