# Agent instructions

This repo is a pack of creator skills for Instagram, by Fliqr AI. It works in Claude Code, Claude Desktop, claude.ai, Codex, Cursor, Hermes and any agent that reads `SKILL.md` files.

- Skills live in `skills/<name>/SKILL.md`. Read the matching skill before doing any Instagram content task.
- The references every skill shares are in `references/`. Read `references/safety.md` before using any connector tool.
- `references/connectors.md` maps capabilities to MCP tools. Match tools by the part of the name after the last `__`.
- The tools are standard-library Python: `skills/polish/scripts/polish.py` (captions, hooks, scripts, DMs, bios) and `skills/growth-audit/scripts/outliers.py`. Run them with `python3`, or `python` on Windows.
- Nothing is published and no automation is activated without the user's explicit yes in the conversation.
- Run `python3 scripts/validate.py` after changing anything.
