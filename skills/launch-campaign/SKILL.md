---
name: launch-campaign
description: >-
  Plan a 7-21 day Instagram launch for a course, product, cohort, ebook, event or brand drop: warm-up,
  waitlist keyword, open-cart days, honest urgency and close, with a day-by-day calendar of reels,
  carousels, stories and lives, plus every comment-to-DM and story automation it needs (set up through
  the Fliqr AI connector after approval). Use when the creator says "launch", "launching my course",
  "product drop", "pre-launch", "waitlist", "open cart", "sell out my cohort", "Diwali sale", or
  "festival sale".
argument-hint: "[what you're launching] [price] [launch date] [cart close date]"
---

# launch-campaign

Launches fail in two ways: nobody knew it was coming, or everyone knew and nothing made them act. This skill builds the three phases that fix both, and it wires each one to a keyword, so interest becomes a list of people who raised their hand.

Read: the creator profile, `../../references/algorithm.md`, `../../references/safety.md`, `../../references/connectors.md`.

## Inputs (one batch)

What's launching and the price · launch date and cart-close date · seat or stock limits (only real ones) · the bonus for early buyers (only a real one) · a lead magnet for warm-up (or build one with `lead-magnet`) · who the buyer is.

## The three phases

```
WARM-UP  (7-14 days before)   teach the problem, show proof, grow the waitlist
   keyword: WAITLIST / NOTIFY → DM: "You're on the list. You'll hear first + get the early price."
OPEN CART (3-5 days)          the offer, objections answered, social proof, live Q&A
   keyword: JOIN / LINK → DM: offer + button to checkout
CLOSE    (last 24-48 hours)   honest deadline, final FAQ, last call
   story automation: reply LAST → DM with the link
```

**Content mix:**
- **Warm-up:** 70% teaching (reels and carousels on the problem the product solves), 30% story (why you built it, behind the scenes). No hard selling yet.
- **Open cart:** daily stories (`story-funnel`), one objection-crusher reel a day ("Do I need X to join? No, here's why"), a results or proof post (real only), a live on day 1 or 2 (`live-funnel`).
- **Close:** a countdown sticker, a "doors close tonight" reel, and the FAQ answered in stories.

## Urgency, honestly

Only real deadlines, real seat limits and real bonuses. "Only 3 spots left" when it isn't true breaks trust. In India it's also a "false urgency" dark pattern, banned under the CCPA's Guidelines for Prevention and Regulation of Dark Patterns (2023), and it can breach ASCI's code on misleading claims. Good honest urgency: early-bird pricing that actually ends, a cohort start date, a bonus live call for the first 48 hours.

## Automations to set up

List every automation the campaign needs, each with its keyword, the post it's attached to (or `is_next`), and its DM. Build each one with `comment-to-dm` or `story-funnel`. Each one is approved and created paused. Then, **each step on its own yes** (approval for the plan doesn't approve the individual changes):
- **Activate** warm-up automations as their posts go live.
- When cart opens, **update** the warm-up automations' DMs to point at checkout (`update_automation`): people who comment on an old warm-up reel should now get the open-cart offer. Show each patch first.
- After close, **update** the DMs again ("Doors are closed. Join the waitlist for next time"), or **pause** them (`set_automation_status: paused`). Never leave a "buy now" DM pointing at a closed cart. Put the close-day changes in the plan as a reminder, because nothing switches over by itself.

## Output

```
LAUNCH  ·  {product} ₹{price}  ·  warm-up {dates} · open {dates} · close {date}

DAY   PHASE    FEED                                   STORIES                      AUTOMATION
-10   warm-up  Reel: "{hook}" (#13)                   poll: problem check          WAITLIST on this reel [new]
…
 0    OPEN     Carousel: what's inside + price        5-frame sell sequence        JOIN on carousel [new] · WAITLIST DMs → checkout [update]
…
+4    CLOSE    Reel: "Doors close tonight"            countdown · FAQ · last call  story LAST [new]
+5    after    —                                       thank-you + results          pause JOIN · WAITLIST → next-cohort list [update]

AUTOMATIONS: 4 new · 2 updates · 1 pause. Each needs your yes when it's built.
METRICS to watch: waitlist triggers / day · JOIN triggers vs sales · reel saves on objection posts
```

Then offer to build day 1 (`reel-script` and `comment-to-dm`).

<!-- brand:footer -->
---
Part of **[Instagram Creator Skills by Fliqr AI](https://github.com/fliqrlabs/instagram-creator-skills)**. Live Instagram data and comment-to-DM automations come from the **Fliqr AI connector** ([fliqr.ai](https://fliqr.ai)).
<!-- /brand:footer -->
