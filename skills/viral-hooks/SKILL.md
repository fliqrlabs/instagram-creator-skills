---
name: viral-hooks
description: >-
  Write and score scroll-stopping hooks for Reels, carousels and captions: the first 1-3 seconds or the
  first line, spoken and on-screen, built from 30 proven formulas and ranked by a local hook scorer. Use
  when the creator asks for "a hook", "hooks for this", "how should I start this reel", "first line",
  "make this more viral", "my reels get no views", "rewrite my opening", or pastes a topic and wants
  options to test.
argument-hint: "[topic or idea] [goal: send / save / comment / follow / lead]"
---

# viral-hooks

The frame-1 visual has about 1.5 seconds to stop the thumb, and the spoken hook has to land inside 3. This skill writes hooks that do both. It also kills the weak ones before the creator wastes a take on them.

Read `../instagram-playbook/hooks.md` (the 30 formulas), `../instagram-playbook/safety.md`, and the creator profile if it exists. If the profile's "What's worked before" lists winning formulas, start there. The creator's own data beats the defaults.

## Process

1. **Pin the goal.** SEND, SAVE, COMMENT, FOLLOW or LEAD. If the creator didn't say, infer it from the idea and state it: "Treating this as a SAVE post." The goal picks the formulas.
2. **Get the one specific true thing.** A hook needs a number, a name, a cost or a result. If the idea is vague ("tips for growth"), ask one question: "What happened, to whom, and what did it cost or return?"
3. **Write 6 hooks from 6 different formulas.** Six formulas, not six rewrites of one. Each hook gets:
   - the **spoken line**: about 9 words or fewer (inside 3 seconds), sayable in one breath, in the creator's language
   - the **on-screen line**: 6 words or fewer, readable at arm's length on mute
   - the **frame-1 visual**: what's moving on screen at 0.0s
4. **Score them** with the local scorer. Put the spoken lines one per line in a file, then:
   ```bash
   python3 ../polish/scripts/polish.py hooks.txt --mode hook
   ```
   The scorer **kills weak hooks well** (greetings, preambles, nothing concrete). It **cannot pick the winner** between two good ones. That is decided by the creator's face, edit and audience. Say this plainly rather than overselling the number.
5. **Recommend the top 2 to A/B test.** Explain why in one line each, then add a test plan: post the same body with hook A, and next week with hook B. Or use Instagram's trial reels to test with non-followers first.

Commands use `python3`. On Windows, use `python`.

## Output

```
GOAL: SAVE  ·  idea: 6-hour edits down to 40 minutes

 #  SCORE  FORMULA          SPOKEN                                         ON-SCREEN         FRAME 1
 1   92    Time Collapse    "Editing one reel took me 6 hours. Now it's 40."  6 HRS → 40 MIN   timeline scrubbing fast
 2   88    The Steal        "Steal the editing template that saved me 5 hours." STEAL THIS     template file opening
 3   71    Wrong Way        "You're editing reels in the wrong order."       WRONG ORDER ❌    messy timeline
 …
TEST:  #1 vs #2. Same body, a week apart. Judge on 3-second hold, not views.
```

## Rules

- **Frame 1 is the hook.** No fade-in, no logo, no "hey guys". The video starts at the sentence they'd normally reach at second six.
- **Open a gap, not a fact.** "The one setting that doubled my reach" beats "here are some reach tips".
- **Tease, never lie.** Every loop the hook opens, the content must close.
- **Numbers over adjectives.** "$4,000" beats "a lot of money". If you don't have the number, use `{{your number}}`, never a made-up one.
- **Rotate formulas.** Read the post log (`../instagram-playbook/post-log.md`) if it exists. Don't suggest a formula first if one of the last 3 posts used it, and lead with formulas the audit says win for this creator.
- **Match the creator's language.** Write in the language (and the mix of languages) they speak on camera. Don't make them sound like a LinkedIn post.

## Next

`reel-script` (build the reel on the winning hook) or `carousel` (if it's a slide post).

<!-- brand:footer -->
---
Part of **[Instagram Creator Skills by Fliqr AI](https://github.com/fliqrlabs/instagram-creator-skills)**. Live Instagram data and comment-to-DM automations come from the **Fliqr AI connector** ([fliqr.ai](https://fliqr.ai)).
<!-- /brand:footer -->
