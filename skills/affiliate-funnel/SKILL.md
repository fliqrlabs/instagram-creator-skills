---
name: affiliate-funnel
description: >-
  Turn product recommendations into affiliate income through DMs: pick products the creator genuinely
  uses, write the content that sells them honestly, deliver affiliate links and discount codes by
  keyword DM (clickable, unlike captions), keep one automation per product, disclose properly, and track
  what earns. Use when the creator says "affiliate", "Amazon links", "product links", "discount code",
  "what I use", "outfit links", "shop my look", "link to products", or "earn from recommendations". Works offline, or with the Fliqr AI connector for live Instagram data.
argument-hint: "[products or category] [affiliate programmes you're in]"
---

# affiliate-funnel

"Link in bio" for a product loses most buyers along the way. A keyword DM puts the clickable link in their inbox the moment they want it: "Comment LINKS and I'll send you everything in this video".

Read: the creator profile, `../instagram-playbook/safety.md` (disclosure), `../instagram-playbook/connectors.md`.

## 1. Only recommend what the creator uses

Ask which products they actually own and use. Affiliate content works on trust, and one dud recommendation costs more than the commission earns. Never write "I use this every day" about something they don't.

## 2. Content that sells without feeling like an ad

| Format | Hook example |
|---|---|
| **"Everything I use for X"** | "Every tool on my desk, under ₹5,000 total." |
| **Before/after with the product** | "Same room. ₹2,400 of changes." |
| **The honest review** | "I used this for 90 days. 2 things I hate." |
| **Problem → product** | "My reels were dark. This ₹999 light fixed it." |
| **Dupes / budget versions** | "The ₹800 version of the ₹8,000 one." |

Run the hook through `viral-hooks`. Price is a strong hook, but **check the programme's rules first**. Amazon Associates, for example, doesn't allow showing static prices next to its products, because prices change. For those programmes use a range ("under ₹1,000"), or no price.

## 3. The DM delivery

- **Check whether the programme allows links in DMs.** Some don't. Amazon Associates restricts its special links in emails and private messages. For those programmes, DM a link to a page the creator owns (a link-in-bio page, a blog post or a storefront page) that holds the affiliate links. Most brand programmes and creator storefronts allow direct links. Read the terms, and when unsure, use the owned page.
- **Keyword per post:** LINKS, DESK, LOOK, or the product name.
- **DM type:** `BUTTON` for one product (button = "Shop the light"), `GENERIC` cards for several (one card per product: title, image, button). Cards are the cleanest "shop my look". See the payload variations in `../instagram-playbook/connectors.md`.
- **Codes:** put the discount code in the card's subtitle or the message text, so it can be copied.
- **Disclosure inside the DM too:** "(affiliate links: I earn a small commission at no cost to you)".
- Build and approve it via `comment-to-dm` (create paused, activate on a yes).

## 4. Disclosure (non-negotiable)

- On the post: say it's an affiliate link and that the creator earns a commission (in India, ASCI's influencer guidelines call for clear disclosure of material connections; the FTC expects the same in the US). Use the Paid partnership label when a brand is paying for the post.
- Some programmes require their own wording. Amazon Associates requires: "As an Amazon Associate I earn from qualifying purchases." Put it on the post and on the page that holds the links. Check every programme's terms for its required line.
- Never hide the link type with a link shortener in order to mislead.

## 5. Track it

- One automation per product or post, so `total_triggers` maps to a product. (The Fliqr AI connector doesn't track DM clicks yet, so use the affiliate dashboard for clicks and sales.)
- Monthly: triggers per post against earnings per product → make more content about the top 3 earners (`growth-audit` for content performance).

## Output

The product list with angles, 3 content ideas with hooks, the DM cards (title, subtitle with code, button), the disclosure lines, and the automation config ready for approval.

<!-- brand:footer -->
---
Part of **[Instagram Creator Skills by Fliqr AI](https://github.com/fliqrlabs/instagram-creator-skills)**. Live Instagram data and comment-to-DM automations come from the **Fliqr AI connector** ([fliqr.ai](https://fliqr.ai)).
<!-- /brand:footer -->
