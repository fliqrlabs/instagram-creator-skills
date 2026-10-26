---
name: instagram-seo
description: >-
  Make a creator findable in Instagram search and Explore: keyword research from what people type,
  the name field and username, keyword-rich bio, captions, on-screen text, spoken words, alt text,
  sized hashtags (5 max) and location tags, mapped into a keyword plan per content pillar. Use when the
  creator says "Instagram SEO", "show up in search", "keywords for Instagram", "nobody finds my
  account", "hashtag research", "what should my name field say", "searchable captions", or "alt text".
argument-hint: "[niche] [city/region if local] [@handle optional]"
---

# instagram-seo

Instagram search now leans on words, not just hashtags: the name field, bio, caption and on-screen text. Creators *report* that what's said out loud (through auto-captions) helps too, though Instagram hasn't confirmed it. A post that uses the words people search for can keep getting found for months.

Read: the creator profile, `../../references/algorithm.md`, `../../references/connectors.md`.

## 1. Keyword research (no tool needed)

1. **Seed list:** 10-15 phrases the audience would type. "cake pricing", "home bakery business", "eggless cake Indore". Use the audience's language: Hinglish searches are real searches.
2. **Instagram search autocomplete:** the creator types each seed into Instagram search and screenshots the suggestions. Those are real searches. Ask for the screenshots, and never invent search volumes.
3. **The audience's own words:** run `comment-mining` (connected) or read the comments. The phrases people use to ask are the phrases they search with.
4. **Size each keyword:** look at the top posts under it. Huge accounts only → too broad for now. Accounts the creator's size or smaller → winnable.

Output: a **keyword map** with 1 primary keyword per pillar and 3-5 secondary ones.

## 2. Where keywords go

| Place | Rule |
|---|---|
| **Name field** | the most important searchable spot. "Meera · Home Baking Coach" beats "Meera ✨🎂". Use the primary keyword. |
| **Username** | include it only if it's still easy to say and spell. Don't rename an established handle for SEO. |
| **Bio** | the primary keyword plus the location, if local, written for humans |
| **Caption first line** | the keyword in the hook, naturally. "Cake pricing is why most home bakers stay broke." |
| **On-screen text** | the keyword on the hook card |
| **Spoken** | say the keyword naturally in the first 5 seconds (*reported* to help through auto-captions, and it helps viewers anyway) |
| **Alt text** | photos and carousels only: Advanced settings → Accessibility → Write alt text. Describe what's in the image for people using screen readers first. Use the keyword only if it truly describes the image. Never stuff it in. |
| **Hashtags** | 5 max, sized as in `caption`: 1-2 niche, 2 mid, 1 broad. Make one of them the primary keyword. A local business can swap the broad tag for a location tag. |
| **Location tag** | always, for local businesses |

## 3. Audit (connected)

`get_profile` → check the name field and bio. `list_media` with `limit: 25` → for each post, does the caption's first line contain a pillar keyword? Report the % of posts that are findable for each pillar, and the 5 best posts to re-caption. Editing an old caption to add keywords is allowed and costs nothing.

## Output

The keyword map, the name field and bio rewrite (lint with `python3 ../polish/scripts/polish.py bio.txt --mode bio`, `python` on Windows), a caption keyword checklist for future posts, and the audit fixes. Never stuff keywords in. Written for humans first, it still has to read naturally.
