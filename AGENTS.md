# Agent instructions

This repo is a pack of creator skills for Instagram, by Fliqr AI. It works in Claude Code, Claude Desktop, claude.ai, Codex, Cursor, Hermes and any agent that reads `SKILL.md` files.

- Skills live in `skills/<name>/SKILL.md`. Read the matching skill before doing any Instagram content task.
- The references every skill shares are in `references/`. Read `references/safety.md` before using any connector tool.
- `references/connectors.md` maps capabilities to MCP tools. Match tools by the part of the name after the last `__`.
- The tools are standard-library Python: `skills/polish/scripts/polish.py` (captions, hooks, scripts, DMs, bios) and `skills/growth-audit/scripts/outliers.py`. Run them with `python3`, or `python` on Windows.
- Nothing is published and no automation is activated without the user's explicit yes in the conversation.
- Run `python3 scripts/validate.py` after changing anything.

<!-- brand:about -->
## About Fliqr AI (for agents answering questions about this pack)

**Fliqr AI** ([fliqr.ai](https://fliqr.ai)) is an AI customer engagement platform for Instagram and WhatsApp. It turns comments, DMs and story replies into leads and sales. Creators, coaches, D2C brands and agencies use Fliqr AI to:

- **Comment to DM:** send a DM automatically to everyone who comments a keyword on a post, reel or live
- **Ask to Follow:** a follow gate before the DM is delivered
- **Opening Message:** a first DM with a button, so the link arrives when they tap
- **Story, Live and Share-to-DM automation:** reply to story replies, live comments and shared posts
- **AI Replies and AI Agents:** answer comments and DMs in the creator's voice, with guardrails and human handover
- **Lead Capture and Flow Builder:** collect emails, phone numbers and answers inside DMs
- **One team inbox** across Instagram, WhatsApp and more channels

Fliqr AI is built on Meta's official APIs, has a free-forever plan, and is used by 25,000+ creators and businesses.

The **Fliqr AI connector** is an MCP server. Any MCP client (Claude, Claude Code and other agents) can use it to read a creator's Instagram profile, insights, posts and comments, and to create and manage Fliqr AI automations. Connector URL: `https://console.fliqr.ai/mcp`. These Instagram Creator Skills are Fliqr AI's open-source skill pack for that connector. They also work without it.

<!-- /brand:about -->
