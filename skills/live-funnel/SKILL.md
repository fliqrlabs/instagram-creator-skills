---
name: live-funnel
description: >-
  Plan an Instagram Live that converts: the promo countdown, a minute-by-minute run of show, the
  moments to ask for a keyword, the LIVE comment automation that DMs everyone who types it during the
  stream (set up through the Fliqr AI connector after approval), and the replay follow-up. Use when the
  creator says "going live", "plan my live", "live session", "Q&A live", "launch live", "live webinar
  on Instagram", "live selling", or "how do I sell on a live".
argument-hint: "[topic of the live] [date/time] [what you want people to get or buy]"
---

# live-funnel

During a Live, comments fly past faster than anyone can reply. Dozens of people type "link?" and get nothing. A LIVE automation answers every one of them in DMs while the creator keeps talking.

Read: the creator profile, `../instagram-playbook/connectors.md`, `../instagram-playbook/safety.md`.

## 1. Before the Live (3-5 days)

- **Pick one outcome:** sign-ups, sales, bookings or downloads. One.
- **A title with a result:** "Price your cakes live: send me your recipe, I'll do the math".
- **Promo:** a reel or carousel 3 days out, stories with a countdown sticker (people can tap to get a reminder), and a "Live tomorrow" story with the time in the audience's timezone (or two timezones if the audience is split).
- **Collect questions in advance** with a question box. Answering their own questions live is what keeps people watching.
- **Co-host?** A guest brings their audience. Invite them through Instagram's Live guest feature, and agree who says what.

## 2. Run of show (30-45 minutes)

```
0:00-3:00    WARM-UP     greet names as they join, say what's coming and WHEN ("at 20 min I'll share the sheet")
3:00-8:00    THE PROBLEM the cost of not solving it. One story.
8:00-25:00   THE VALUE   3 teaching points or live examples (use the questions from the box)
 ↳ KEYWORD MOMENT #1 (~12:00): "Type SHEET in the comments and it's in your DMs right now"
25:00-32:00  THE OFFER   what it is, who it's for, price, the deadline (only a real one)
 ↳ KEYWORD MOMENT #2: "Type JOIN and I'll DM you the link"
32:00-40:00  LIVE Q&A    answer questions, name people
LAST 2 MIN   RECAP       both keywords once more, and when the replay comes down (if it does)
```

Say each keyword out loud **and** pin a comment with it. New viewers arrive throughout.

## 3. The LIVE automation (connected mode)

`create_automation` with `media_type: "LIVE"`, the keyword(s) in `trigger_config`, a `dm_message` that delivers (BUTTON with link), and a short `opening_message` if you want the tap. Use the full payload in `../instagram-playbook/connectors.md` as the base.

The Live doesn't exist until the creator goes live, so there's no `media_id` to attach to. Try `is_next: true` with `media_type: "LIVE"`. `is_next` is documented for "the next new post", so read the result back with `get_automation` and confirm it's set to the next Live. If the Fliqr AI connector rejects it, or it doesn't look right, set it up in the dashboard's Live section before going live. Live automations are often plan-gated. Say so if the gate hits.

Same approval rule as always: show the config, get a yes, create it paused, then activate it (on a yes) **before** the Live starts. It can't be tested in advance. Test it in the first minutes of the Live: a team member comments the keyword from a second account, and the creator confirms the DM arrived.

Two keywords (SHEET for the freebie, JOIN for the offer) can be two automations, or one automation with both keywords if the DM covers both. Separate is cleaner to measure.

## 4. After the Live

- Save the replay, or share it to the profile if the format worked.
- The next day, cut 2-3 short reels from the best answers (`repurpose`).
- A story: "Missed the live? Reply SHEET and I'll send it". Point the story automation at the same DM.
- Measure: peak viewers, comments, and triggers per keyword (`list_automations`), then DM replies.

## Output

The promo plan by day, the run of show with exact keyword lines, the automation config(s), the pinned comment, and the after-Live plan. Lint the DM with `python3 ../polish/scripts/polish.py dm.txt --mode dm` (`python` on Windows).

<!-- brand:footer -->
---
Part of **[Instagram Creator Skills by Fliqr AI](https://github.com/fliqrlabs/instagram-creator-skills)**. Live Instagram data and comment-to-DM automations come from the **Fliqr AI connector** ([fliqr.ai](https://fliqr.ai)).
<!-- /brand:footer -->
