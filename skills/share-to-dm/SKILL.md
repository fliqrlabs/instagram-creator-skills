---
name: share-to-dm
description: >-
  Design a share-to-DM campaign: content people forward into the creator's DMs, with an automated reply
  that delivers something when they do. Covers the post concept that earns the share, the "send this to
  me" CTA, the auto-reply copy, and the dashboard setup checklist. Use when the creator says "share to
  DM", "get people to share my post", "send this reel to me", "forward to DM campaign", or wants a
  campaign beyond comment keywords.
argument-hint: "[what people get when they share] [the post or idea]"
---

# share-to-dm

Comment keywords work in public. Share-to-DM works in private: the viewer forwards the post into the creator's DMs and an automated reply delivers what was promised. It suits content people would rather not comment on publicly (money, health, relationships, "I need this but don't want my friends to see").

Read: the creator profile, `../../references/safety.md`, `../../references/connectors.md`.

**Connector note:** share-to-DM triggers aren't in the connector's automation types yet (it supports POST, STORY and LIVE). This skill writes everything, then gives a setup checklist for the dashboard's Share to DM section. When a connector capability for it appears in `connectors.md`, use it instead. Share to DM is often a higher-plan feature.

## 1. When to use it instead of a keyword

| Use share-to-DM | Use comment-to-DM |
|---|---|
| a private or sensitive topic | you want public comments in the thread |
| the audience is shy (B2B, finance, health) | the audience is chatty |
| a story or reel the viewer is already forwarding | a post built for discussion |

Don't promise it does more for reach than it does. Instagram hasn't said whether a share to the creator counts like a share to a friend. Treat it as a lead mechanic. Sends to friends still come from content worth sending (see `../../references/algorithm.md`).

## 2. The CTA

Make the action dead clear, because sharing takes more taps than commenting:

- Spoken: "Tap share, send this reel to me, and I'll send you the sheet."
- On screen, last 3 seconds: `SHARE → SEND TO @{handle} → GET THE SHEET` with an arrow at the paper-plane icon.
- Caption, first line: "Send this post to my DMs and I'll reply with {thing} 📩".

## 3. The auto-reply

Same rules as a keyword delivery (see `comment-to-dm`, section 3d): deliver first, one line on how to use it, one easy question. Add one line that acknowledges how they got there: "Got your share! Here's the {thing} 🙌".

## 4. Dashboard setup checklist

```
[ ] Automation type: Share to DM (on the post / reel: {which})
[ ] Reply type: button message → {link}
[ ] Opening message with a button (optional, recommended): "{text}" [{button}]
[ ] Follow gate: on / off
[ ] Test: share the post to the account from a second account, and check the reply arrives
```

## Output

The concept and CTA lines (spoken, on-screen, caption), the reply copy (linted with `python3 ../polish/scripts/polish.py dm.txt --mode dm`, or `python` on Windows), and the checklist above, filled in.
