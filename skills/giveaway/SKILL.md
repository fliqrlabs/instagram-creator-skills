---
name: giveaway
description: >-
  Run an Instagram giveaway or contest that grows the right audience without wrecking engagement:
  prize choice, entry mechanics, official-rules text, Meta promotion-guideline compliance, a comment
  automation that confirms every entry by DM, the winner-pick process, and the post-giveaway plan so
  new followers stay. Use when the creator says "giveaway", "contest", "win a", "collab giveaway",
  "brand giveaway", "how do I run a giveaway", or "giveaway rules". Works offline, or with the Fliqr AI connector for live Instagram data.
argument-hint: "[prize] [solo or with a brand/creator] [goal: followers / leads / launch buzz]"
---

# giveaway

Most giveaways bring in prize hunters who unfollow the day the winner is announced, and the account's engagement rate drops for months. This skill designs one that attracts the creator's actual audience and keeps them.

Read: the creator profile, `../../references/safety.md`, `../../references/connectors.md`.

## 1. The prize decides who shows up

- ✓ The creator's own product, service or a niche tool: attracts people who want **that**.
- ✗ An iPhone or cash: attracts everyone, keeps no one.
- Collab giveaway: partner with a creator or brand whose audience overlaps, not just a big one. Use a Collab post so it lands on both grids.

## 2. Entry mechanics

Keep it to **2 steps**. Every extra step costs entries:
1. Follow @{creator} (and the partner, if a collab)
2. Comment {KEYWORD} (or answer a question related to the niche, which filters for real fans)

Think twice about "tag 3 friends". Instagram's promotion guidelines forbid encouraging people to tag themselves or others **inaccurately** (tagging a friend who isn't in the photo, for example). Tag-to-enter also fills the thread with low-quality comments from people who'll never buy. If the creator wants tags, make it "tag one friend who'd actually use this". "Share to your story for an extra entry" is fine. It can't be checked automatically, so say it's honour-based.

## 3. The comment automation

Every entrant gets a DM confirming the entry: "You're in! 🎉 Winner announced {date} on my stories. Rules: {link}". End it with an easy question ("What would you use it for first?"). If they reply, that's a real conversation the creator can continue. Instagram only lets businesses message within 24 hours of the person's last message, so plan no follow-up outside that window. Never put entrants on a message sequence.

Build it with `comment-to-dm`, using the full payload in `../../references/connectors.md`: the keyword trigger, public reply variations ("You're in! 🍀"), a reply limit for big posts, and a delivery DM with the rules link. A follow gate is natural here, since following is an entry step. Same gate as always: approve, create paused, activate.

## 4. Official rules (required)

Meta's promotion guidelines make the person running the giveaway responsible for it being lawful, and require the rules to include **both**:
1. **a complete release of Instagram by each entrant**, for example: "By entering, each participant releases Instagram (Meta Platforms, Inc.) from any and all liability in connection with this promotion."
2. **an acknowledgement that the promotion is not sponsored, endorsed or administered by, or associated with, Instagram.**

Draft rules covering:
- who can enter (age 18+, country or countries), the start and end date and time with timezone
- how to enter, and that no purchase is necessary
- the prize, its value, and how and when it's delivered
- how the winner is picked (a random draw from valid entries) and notified (only from the official account, never asking for payment or passwords)
- the release of Instagram and the not-sponsored acknowledgement above (both)
- organiser contact details

Prize promotions are regulated differently by country, and some Indian states restrict games of chance. Flag it: **"Have these rules checked for your country before posting."** This skill drafts the rules. It is not legal advice.

## 5. Winner and after

- Pick randomly from valid entries (export the comments with `get_media_comments`, filter for the keyword, de-duplicate by username). Record the screen while picking.
- Announce on stories and DM the winner from the official account. **Warn followers about fake "you won" accounts.** They show up on every giveaway.
- **Keep the new followers:** post the creator's best evergreen content in the next 5 days, plus a consolation offer: "Didn't win? Comment CODE for 20% off for 48 hours", but only if that offer is real.

## Output

The concept, the post copy (`caption` rules apply), the automation config, the official rules draft, the winner-pick steps and the 5-day retention plan.

<!-- brand:footer -->
---
Part of **[Instagram Creator Skills by Fliqr AI](https://github.com/fliqrlabs/instagram-creator-skills)**. Live Instagram data and comment-to-DM automations come from the **Fliqr AI connector** ([fliqr.ai](https://fliqr.ai)).
<!-- /brand:footer -->
