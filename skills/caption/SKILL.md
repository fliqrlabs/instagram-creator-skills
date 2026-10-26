---
name: caption
description: >-
  Write an Instagram caption that earns the tap on "more": a hook in the first 125 characters, the keyword
  CTA above the fold, searchable keywords, up to 5 sized hashtags, and a pinned first comment, linted by a
  local checker that shows exactly what the feed displays. Use when the creator asks for "a caption",
  "caption this", "write the description", "hashtags for this", "fix my caption", or has a finished reel,
  carousel or photo and needs the words.
argument-hint: "[what the post is about, or the reel script] [CTA keyword if any]"
---

# caption

Instagram shows about 125 characters before "... more", and most people never tap. A caption that fails, fails there. This skill writes for that window first.

Read: the creator profile, `../../references/algorithm.md`, `../../references/safety.md`. Commands use `python3`. On Windows, use `python`.

## Structure

```
LINE 1     the hook. Concrete, under ~110 characters. Pick up where the reel's hook left off, don't repeat it.
LINE 2     the keyword CTA if it's a LEAD post: Comment "PLAN" and I'll DM you the planner 📩
           (above the fold, or 90% of people never see it)
BODY       the value: the steps, the story, the context the reel only teased. Short lines. White space.
CLOSE      one ask, matched to the goal (save / send / comment KEYWORD / follow)
TAGS       up to 5 hashtags, sized to the account
```

## Rules

- **The keyword goes in the first 2 lines.** Repeat it once at the end for people who read everything.
- **Searchable words early.** Instagram search is keyword-led. Use the words a person would type ("reel editing template", "home baking business"), not just clever ones.
- **Hashtags: 5 at most** (Instagram's current cap). Mix 1-2 niche tags (under 100K posts), 2 mid (100K-1M), and 1 broad. A small account can't rank on #love.
- **No links.** Links in captions don't click. Deliver links by DM (`comment-to-dm`).
- **One ask.** Two CTAs is no CTA.
- **Emoji with intent.** 0-3 that do a job (📩 next to the DM promise), not sprinkled on every line.
- **Collab / paid?** Add the disclosure (#ad, or the Paid partnership label) and remind the creator once.

## The first comment

Write a pinned first comment too. It's a second shot at the fold and seeds the thread:
- LEAD posts: "Comment PLAN below 👇 sending it to everyone today". That makes the first comment model the action.
- Discussion posts: a genuine question that's easy to answer.

## Lint it

```bash
python3 ../polish/scripts/polish.py caption.txt --keywords "reel editing,editing template"
```

It prints the exact feed window as a box, then checks length, the first line, a concrete hook, the hashtag cap, links, the keyword's position, one ask, and AI slop. Fix every FAIL. Fix the WARNs unless there's a reason not to.

## Output

Give 2 caption options (different first lines), the first comment, and the lint result for the recommended one. End with:
```
Next: set up the funnel → comment-to-dm keyword "PLAN" (only if it isn't live yet)
```

<!-- brand:footer -->
---
Part of **[Instagram Creator Skills by Fliqr AI](https://github.com/fliqrlabs/instagram-creator-skills)**. Live Instagram data and comment-to-DM automations come from the **Fliqr AI connector** ([fliqr.ai](https://fliqr.ai)).
<!-- /brand:footer -->
