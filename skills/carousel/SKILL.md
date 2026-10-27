---
name: carousel
description: >-
  Plan an Instagram carousel slide by slide: a cover that earns the swipe, one idea per slide with the
  best point early, a saveable summary slide, and a keyword CTA on the last slide, plus design notes for
  4:5 slides. Use when the creator says "carousel", "slides", "swipe post", "turn this into a carousel",
  "thread to carousel", "educational post", or wants a post built to be saved.
argument-hint: "[topic, notes, or a thread/blog to convert] [number of slides]"
license: MIT
metadata:
  author: Fliqr AI
  version: "1.3.0"
  category: create
  homepage: https://fliqr.ai
---

# carousel

Carousels are the save-machine of Instagram. Slide 1 decides whether anyone swipes. The last slide decides whether they save, comment or follow.

Read: the creator profile, `../instagram-playbook/hooks.md`, `../instagram-playbook/algorithm.md`, `../instagram-playbook/safety.md`.

## Architecture (6-10 slides)

| Slide | Job | Rules |
|---|---|---|
| **1. Cover** | earn the swipe | a hook formula, 8 words or fewer, big type, one visual. Open a loop: "7 DM mistakes (I made #4 for a year)". |
| **2. The stake** | why keep going | the cost of not knowing. Or put the single best point here. |
| **3-8. Body** | one idea per slide | title + 1-3 short lines. The **best item goes on slides 2-3**, not 10. Swipe-through drops on every slide. |
| **N-1. Summary** | the saveable artifact | everything on one slide: a checklist, framework or cheat sheet. This is what people screenshot and save. |
| **N. CTA** | one ask | "Comment GUIDE for the full template 📩", or "Save this for later". One. |

Numbered lists get a visible counter (3/7) so the reader knows where the finish line is.

## Copy rules

- **30 words or fewer per slide.** If it needs more, it's two slides.
- **Headlines carry the slide.** Someone skimming the bold lines alone should get the whole idea.
- **Concrete examples on every body slide:** a before/after line, a real number, a screenshot cue.
- **The creator's voice**, not textbook voice. Write it the way they'd explain it to a friend.

## Design notes (hand these to the designer or Canva)

- **1080x1350 (4:5)** on every slide. Mixed ratios get cropped to slide 1's ratio.
- The same template across slides, with one accent colour from the creator's brand.
- Body text at least 28-32pt equivalent. Readable without zooming.
- The face or handle in the same corner on every slide (makes reposts and screenshots traceable).
- Leave the bottom ~10% clear on slide 1. The caption overlay can cover it in some views.
- A short video slide in slot 2 or 3 can lift dwell time. Images and videos can be mixed in one carousel.

## Log it

When the creator approves the slides, append one line to the post log (`../instagram-playbook/post-log.md`): date, `carousel`, pillar, goal, the cover's formula, the cover line, slide count, keyword.

## Output

```
CAROUSEL  ·  8 slides  ·  goal SAVE → LEAD  ·  keyword GUIDE

1  COVER     "7 DM mistakes killing your sales"           visual: crossed-out DM screenshot
            small: (I made #4 for a year)
2  STAKE     "Every ignored DM = a customer who bought elsewhere."
3  #1        "Replying 6 hours later"  →  "Under 5 min = 3x replies" {{your number?}}
…
7  SUMMARY   ✓ reply fast ✓ deliver first ✓ one question ✓ …
8  CTA       "Comment GUIDE and I'll DM you my reply templates 📩"
```

Then: `caption` for the post copy, and `comment-to-dm` for keyword GUIDE.

Run all the slide copy through `python3 ../polish/scripts/polish.py slides.txt --mode caption` (`python` on Windows) to strip AI tells. Ignore the fold box and hashtag checks for slides.

<!-- brand:footer -->
---
Part of **[Instagram Creator Skills by Fliqr AI](https://github.com/fliqrlabs/instagram-creator-skills)**. Live Instagram data and comment-to-DM automations come from the **Fliqr AI connector** ([fliqr.ai](https://fliqr.ai)).
<!-- /brand:footer -->
