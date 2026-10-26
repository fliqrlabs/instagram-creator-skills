# Contributing

PRs are welcome, especially:

- **Hook formulas** backed by real examples (`references/hooks.md`)
- **Slop words and phrases** for your language or niche (`skills/polish/scripts/rules.json`)
- **Platform changes.** When Instagram changes a limit, update `references/algorithm.md` and link the source.
- **New connectors.** Add rows to `references/connectors.md`. Skills ask for capabilities, so most connectors need no skill changes.

Rules for skills:

1. One job per skill. `SKILL.md` stays under 500 lines, and long material moves to `references/`.
2. Every skill works in offline mode (pasted data) and gets better in connected mode.
3. Never fabricate. Placeholders look like `{{your number}}`.
4. Anything that writes (publish, automation, DM) shows the exact payload and waits for a yes.
5. `python3 scripts/validate.py` passes.
