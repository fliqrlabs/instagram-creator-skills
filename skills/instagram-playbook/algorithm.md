# How reach works (2026 field notes)

These notes come from Instagram's public statements (Mosseri's creator posts and the Creators account) and from patterns creators have measured. Items marked *reported* come from creators, not from Instagram. Platform numbers change. If this file disagrees with what Instagram is doing today, Instagram is right. Update the file.

## What the ranker rewards, strongest first

| Signal | Weight | Built by |
|---|---|---|
| **Sends** (shared in DM, reshared to a story) | highest | relatable truths, "you need to see this", contrarian takes, things that make the sender look smart |
| **Watch time / completion / rewatch** (Reels) | very high | a hook that lands in under 2s, a beat change every 2-4s, a payoff held until the end, a loop |
| **Saves** | high | lists, frameworks, templates, steps, before/after, anything future-you needs |
| **Comments, especially with a reply from the creator** | high | questions, takes people want to argue with, and **keyword CTAs** |
| **Profile visit, then follow** | high | a series, a clear niche, a payoff that promises more |
| Likes | low | anything |
| "Not interested", hide, unfollow, report | heavy penalty | bait, misleading hooks, reposted watermarked video |

Before every post, ask: **would someone send this to one specific friend, or save it for later?** If neither, rework it before posting.

## Why keyword CTAs work twice

A "comment WORD" CTA gives you two wins at once.
1. **Comments go up.** A one-word comment costs the viewer nothing, so many more people comment, and comments are a high-weight signal in the first hour.
2. **Leads come in.** Every comment triggers a DM, so the viewer becomes a conversation you can follow up.

Creators often report that keyword CTAs get 5-15% of viewers to act, against 1-3% for "link in bio" (*reported*). Two conditions make it work: the thing promised is worth one word, and the DM delivers it instantly. A keyword the automation does not deliver on is worse than no CTA at all.

What hurts reach is **engagement bait**: "comment YES if you agree", "tag 3 friends", "double tap if". The difference is honesty. A keyword CTA delivers something real. Bait asks for engagement and gives nothing back.

## The first 60 minutes

- Early sends, saves and comments decide whether a post gets pushed to non-followers.
- Replying to comments in the first hour doubles the conversation signal. Keyword automations with a **public reply** ("sent, check your DMs") count toward this too.
- Do not delete and re-upload a post that is underperforming in its first hour. It resets nothing and trains nothing.

## Reels

- **Frame 1 is the hook.** Motion plus on-screen text, legible on mute. The visual has to stop the thumb in about 1.5 seconds. Most people watch muted at first.
- **Spoken hook inside 3 seconds:** about 9 words at a normal reel pace (~180 wpm). This is the standard every skill and `polish.py` uses.
- **Re-hook at the dips**, around 4s, 9s and 15s: "but here's the part nobody tells you".
- **Promise the payoff early and deliver it last.** That one move does more for completion than anything else.
- **Loop it.** If the last line flows back into the first, rewatches follow, and rewatches are free reach.
- **Length:** 15-45s is where most creators win. Up to 3 minutes is allowed. Longer only works if the retention graph says so.
- **Originality:** reposted clips, other apps' watermarks and stitched compilations get suppressed. Copy the structure, never the content.
- **Cover:** pick a cover frame with the hook text on it. In the grid it's cropped to 3:4 (1080x1440 from the centre), so keep the words central.
- **Trial reels** show a reel to non-followers first. Use them to A/B test a hook without risking the main feed.

### Safe zones (1080x1920, approximate; the UI shifts between app versions)

| Surface | Keep text out of |
|---|---|
| Reels | top ~230px, bottom ~480px (caption and audio strip), right ~230px (action rail) |
| Stories | top ~250px (profile row), bottom ~320px (reply bar) |

## Carousels

- **Slide 1 is the whole funnel.** It makes a promise and opens a loop.
- Put the best point on slide 2 or 3. Swipe-through drops off with every slide.
- 6-10 slides for teaching. 4:5 portrait. One idea per slide.
- **The last slide earns the save:** a summary slide plus one ask.
- Carousels resurface. A viewer who skipped can be shown slide 2 later, so they have a long tail.

## Stories

- Stories build trust with existing followers. They do not reach new people.
- Stickers drive taps. Taps keep you at the front of the story tray.
- A **story reply** is a DM. Story automations turn "reply with WORD" into a lead, with no link sticker needed.

## Captions and hashtags

- About 125 characters show before "... more". The hook and the keyword go there.
- **Hashtag cap: 5 per post.** Instagram lowered the cap from 30 to 5 in late 2025. If the app accepts more by the time you read this, the cap changed again: update `HASHTAG_CAP` in `polish.py` and this line. Pick tags that fit your account's size and niche over tags with big numbers.
- Instagram search is keyword-led now. Use the words people actually search for in the first lines and in on-screen text.
- Links in captions do not click. Deliver links by DM.

## Measuring what worked (use this, not raw views)

| Metric | Formula | Tells you |
|---|---|---|
| **Outlier multiple** | views / the account's median views (last 20-30 posts) | a real hit (3x and up) or a normal day |
| **Sends per reach** | shares / reach | whether it travelled. The strongest signal. |
| **Saves per reach** | saved / reach | whether it was useful |
| **Comment rate** | comments / reach | how well the CTA and the topic did |
| **Automation conversion** | automation total_triggers / comments | how many commenters took the funnel |
| **Follows per reach** | follows / reach | whether the profile converted the attention |

A reel with 4,000 views and 90 sends beat a reel with 60,000 views and 11 sends.

## Timing

Consistency beats volume. 3-5 strong posts a week on a steady cadence beats daily filler. For timing, use the creator's own insights. As a starting guess for Indian audiences, *reported* windows are 12-2 PM and 7-10 PM IST, with Sunday evening strong.
