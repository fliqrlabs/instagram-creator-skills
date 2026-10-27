# The post log

One line per post the creator approved: what it was, which hook formula it used, and which keyword funnel it had. Weeks later, `growth-audit` joins these lines to the post's real numbers and can say *"Hidden Cost hooks average 8x your median, numbered lists 0.9x"*. Without a log, it can only guess which formula a reel used.

## Where it lives

Next to the creator profile: `post-log.md` in the working folder, otherwise `~/.fliqr/post-log.md`. On claude.ai, where there's no file system, print the line for the creator to paste into a Project knowledge file called `post-log.md`.

## When to write

- **Only after the creator approves** the final draft (or says "log it"). Drafts that were never posted don't go in.
- **Append, never rewrite.** One line per post. Fix a wrong line by adding a corrected line marked `(fix)`.
- If a funnel is created later for the same post, add the keyword and automation id to that post's line, or add a `(funnel)` line.
- Never log other people's data: no commenter names, no DM text.

## Format

A markdown table, so it's readable by people and by `outliers.py`:

```
| date       | format   | pillar  | goal | formula             | hook                                         | length | keyword | automation | media_id |
|------------|----------|---------|------|---------------------|----------------------------------------------|--------|---------|------------|----------|
| 2026-10-28 | reel     | pricing | LEAD | #13 Hidden Cost     | You're losing $30 on every cake you sell.    | 25     | PRICE   | a1b2…      |          |
| 2026-10-30 | carousel | process | SAVE | #21 Numbered System | 7 pricing mistakes (I made #4 for a year)    | 8      |         |            |          |
```

- `formula`: the number and name from `hooks.md`. Use `unclassified` if it doesn't fit one. Those are worth reading by hand, because they may be a new formula.
- `media_id`: fill it in once the post is live (from `list_media`). Until then, `growth-audit` matches on date and the first words of the caption.

## Reading it

- `growth-audit`: joins the log to post insights, then runs `outliers.py --group-by formula` (and `format`, `pillar`).
- `viral-hooks`: skips any formula used in the last 3 posts.
- `content-plan`: avoids a pillar or formula used in the last 2 weeks, and plans more of what the audit says wins.
