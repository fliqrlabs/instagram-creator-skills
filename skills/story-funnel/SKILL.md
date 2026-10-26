---
name: story-funnel
description: >-
  Write a day's Instagram Story sequence that sells without a feed post: frame-by-frame copy, which
  sticker goes where, and a "reply WORD" story automation that turns replies into DM leads (set up live
  through the Fliqr AI connector after approval). Use when the creator says "stories", "what do I post
  on my story", "story sequence", "sell on stories", "launch on stories", "poll idea", or "story reply
  automation".
argument-hint: "[what you want stories to do today: warm up / sell / launch / collect questions]"
---

# story-funnel

Feed posts find strangers. Stories turn followers into buyers. A story reply is already a DM, so the shortest path from attention to a conversation on Instagram is: story → reply with a keyword → an automated DM delivers.

Read: the creator profile, `../../references/safety.md`, and `../../references/connectors.md` if connected.

## The sequence (3-7 frames)

```
1  OPEN     something happening today, with a face or hands. Text on a flat colour gets tapped through.
2  PROBLEM  name the pain in your audience's words ("DMs piling up and you're replying at 1 AM?")
3  PROOF    a result, a screenshot, a before/after, a customer message (real, with permission)
4  ASK      ONE sticker or one keyword: "Reply PLAN and I'll send it" / poll / question box
5  CLOSE    the answer, the outcome, or tomorrow's teaser
```

Put the ask on frame 4, not 7. Completion drops with every tap.

## Stickers, and what they're for

| Sticker | Job |
|---|---|
| **Poll** | the cheapest tap, and it warms the story ranking. "Do you reply to DMs yourself? Yes / Ugh, yes" |
| **Question box** | collects their exact words. Feed the answers to `comment-mining` and `viral-hooks` (formula #20). |
| **Quiz** | teaches by letting them be wrong |
| **Link** | the only clickable story element. Use it when there's somewhere real to go. |
| **Countdown** | launches, lives, deadlines. People can subscribe for a reminder. |
| **"Reply with WORD"** (text) | the lead engine. Pair it with a story automation. |

## Story automation (connected mode)

A story automation fires when someone replies to the story with the keyword. In the Fliqr AI connector it's `create_automation` with:

- `media_type: "STORY"`, `media_id` from `list_media` with `kind: "stories"` (live stories only), **or** `is_next: true` for the next story posted
- `trigger_config`: `KEYWORDS` with the keyword and its variants
- `dm_message`: the delivery, usually `BUTTON` with the link
- `opening_message` and `follow_message` as in `comment-to-dm`. Skip `public_reply`, stories have no public thread.
- AI fallback on stories can only send a private reply.

Same gate as always: show the config, get a yes, create paused, then ask whether to activate. Story automations can be plan-gated. If so, say what unlocks them.

## Output

A frame-by-frame table (frame, visual, text overlay ≤ 10 words, sticker), then the automation config if one is used, then the polish check. Keep overlays inside the stories safe zone in `../../references/algorithm.md`.

## Rules

- Talk to one person: "you", singular.
- Selling sequence: context (open + problem), then proof, then the ask, as in the sequence above. That beats a sales feed post and costs no reach.
- No fake scarcity ("only 3 left" when it isn't true).
- Never DM people who didn't reply. The automation only answers people who replied.

<!-- brand:footer -->
---
Part of **[Instagram Creator Skills by Fliqr AI](https://github.com/fliqrlabs/instagram-creator-skills)**. Live Instagram data and comment-to-DM automations come from the **Fliqr AI connector** ([fliqr.ai](https://fliqr.ai)).
<!-- /brand:footer -->
