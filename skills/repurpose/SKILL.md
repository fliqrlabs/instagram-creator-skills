---
name: repurpose
description: >-
  Turn one long piece (YouTube video, podcast, webinar, live replay, blog, newsletter, thread) into a
  week of native content: 5-10 standalone reels with timestamps to clip, carousels, stories and
  captions, then adapt the best ones for YouTube Shorts, Threads, LinkedIn and X, each written for its
  own platform. Use when the creator says "repurpose", "clip my podcast", "turn this video into reels",
  "cut this live", "content from my blog", "cross-post", "post this on LinkedIn too", or "Shorts".
argument-hint: "[transcript, link + transcript, or the article text] [platforms]"
---

# repurpose

One good hour of talking holds 10 reels. Most creators post one clip and move on. This skill finds every standalone moment, and rewrites rather than resizes each one for where it's going.

Read: the creator profile, `../../references/hooks.md`, `../../references/algorithm.md`.

## 1. Input

A transcript with timestamps is ideal (YouTube's transcript, a podcast host's export, or any transcription tool). A link alone can't be watched, so ask for the transcript. Articles and threads can be pasted as they are.

## 2. Find the moments

Read the whole thing and pull out **standalone moments**. Each must make sense with zero context:
- a story with a result
- a contrarian claim and its proof
- a specific how-to (steps, numbers)
- a quotable line
- a strong answer to a common question

For each: the timestamp range, its goal (SEND / SAVE / COMMENT / LEAD), a hook formula, and the **new opening line**. A clip almost never starts with a hook, so add a text hook on screen, or a 2-second voiceover, before the clip.

## 3. Build the week

| From | Make |
|---|---|
| a story moment | a reel (clip + text hook + captions) |
| a how-to or list | a carousel (`carousel`) |
| a strong opinion | a talking-head re-record (better than the clip) + a Threads/X post |
| a Q&A answer | a reel + a question-sticker story ("what else should I answer?") |
| the whole piece | one LEAD post: "Comment FULL and I'll DM you the full episode / notes" |

## 4. Adapt per platform (rewrite, never just reformat)

| Platform | What changes |
|---|---|
| **Instagram Reels** | hook in 3s, captions burned in, keyword CTA, ≤5 hashtags |
| **YouTube Shorts** | a searchable title (keywords first), vertical, up to 3 minutes (but shorter still wins), link the long version with the "related video" setting (links in Shorts descriptions aren't clickable), no Instagram watermark |
| **Threads** | text-first, conversational, a question at the end; split a long take into a 3-5 post thread |
| **LinkedIn** | professional framing, a first line that earns "see more", the story plus the lesson, no hashtag walls, a link in the comments |
| **X** | one sharp line, or a numbered thread; the hook is the whole tweet |

**Remove other apps' watermarks.** Instagram suppresses reposted video carrying another platform's logo. Export clean files.

## Output

A table of moments (timestamp, goal, formula, new hook, format, platform), then the full copy for the top 3 (reel script or on-screen text, caption, and the platform versions). Lint the Instagram captions with `python3 ../polish/scripts/polish.py caption.txt` (`python` on Windows). LEAD pieces go to `comment-to-dm`.

<!-- brand:footer -->
---
Part of **[Instagram Creator Skills by Fliqr AI](https://github.com/fliqrlabs/instagram-creator-skills)**. Live Instagram data and comment-to-DM automations come from the **Fliqr AI connector** ([fliqr.ai](https://fliqr.ai)).
<!-- /brand:footer -->
