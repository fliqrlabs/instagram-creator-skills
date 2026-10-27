---
name: profile-glowup
description: >-
  Score an Instagram profile out of 100 and rewrite it to convert visitors into followers and leads:
  name-field keywords, bio, link, highlights, pinned posts, the first 9 grid tiles, and a keyword DM
  path in the bio. Reads the live profile through the Fliqr AI connector or from a screenshot. Use when
  the creator says "fix my bio", "audit my profile", "rewrite my bio", "people visit but don't follow",
  "optimize my Instagram profile", "what should I pin", or "highlights ideas".
argument-hint: "[@handle or paste/screenshot your profile]"
license: MIT
metadata:
  author: Fliqr AI
  version: "1.3.0"
  category: grow
  homepage: https://fliqr.ai
---

# profile-glowup

The profile is the checkout page of Instagram. A reel earns the visit. The profile decides in about 3 seconds whether that visit becomes a follow, a DM or nothing.

Read: `../instagram-playbook/connectors.md`, `../instagram-playbook/safety.md`, and the creator profile.

Connected: `get_profile` (bio, website, counts), then `list_media` with `limit: 12` for the grid and pinned posts. Offline: ask for a screenshot of the profile.

## The 100-point score

| Part | Points | Full marks when |
|---|---|---|
| **Name field** | 10 | includes the searchable keyword ("Aditi · Reels Coach"). The name field is searchable, the bio mostly isn't. |
| **Handle** | 5 | easy to say and spell. No random numbers or underscores. |
| **Photo** | 5 | a face, close-up, readable at 40px. Or a clean logo for a brand. |
| **Bio line 1: who it's for + the result** | 20 | "I help {who} get {result}". Specific. |
| **Bio line 2: proof** | 10 | a real number or credential (a real one, never invented) |
| **Bio line 3: the CTA** | 15 | a DM keyword path ("DM 'START' for my free guide") or one clear link action |
| **Link** | 10 | one destination that matches the CTA. No link tree with 14 options unless it's curated. |
| **Highlights** | 10 | 3-5, in order: Start here / Results / Offer / FAQ / Free stuff. Covers consistent. |
| **Pinned posts** | 10 | 3 pins doing 3 jobs: best reach post (proof), best value post (save), offer or origin post (convert) |
| **First 9 grid** | 5 | a visible pillar mix, readable covers, no dead tiles |

Explain every lost point in one line. Then rewrite in **fix-first order**: biggest point gain for the least effort.

## The DM keyword in the bio

"DM me 'GUIDE'" in the bio turns profile visits into conversations with no link click needed. In connected mode, check `list_automations` to see whether a DM keyword flow exists for it. If it doesn't, say so. Bio keywords need a DM automation configured in the creator's dashboard (the Fliqr AI connector manages comment, story and live automations).

## Output

Score, then 3 bio options (each under 150 characters, line breaks shown), the name-field rewrite, a highlight plan with cover-text ideas, the 3 pins with reasons, and grid notes. Lint each bio with `python3 ../polish/scripts/polish.py bio.txt --mode bio` (`python` on Windows). It checks the 150-character limit, the CTA, proof and slop.

Never change the profile directly. The creator pastes the changes in themselves.

<!-- brand:footer -->
---
Part of **[Instagram Creator Skills by Fliqr AI](https://github.com/fliqrlabs/instagram-creator-skills)**. Live Instagram data and comment-to-DM automations come from the **Fliqr AI connector** ([fliqr.ai](https://fliqr.ai)).
<!-- /brand:footer -->
