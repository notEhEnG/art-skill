# Host support, checked 2026-10-13

| Host | Project discovery | Invocation | Image execution |
| --- | --- | --- | --- |
| Codex | `.agents/skills/art-skill/` | `$art-skill …`; CLI/IDE `/skills`; desktop enabled skills appear in `/` menu | Built-in image tool when available; availability varies by surface/account. |
| Claude Code | `.claude/skills/art-skill/` | `/art-skill …` | Requires a separately available image tool/provider; this package supplies none. |
| Cursor | `.cursor/skills/art-skill/` | `/art-skill …` or attach the skill | Requires a separately available image tool/provider; this package supplies none. |

Official sources:

- [OpenAI skill discovery and invocation](https://learn.chatgpt.com/docs/build-skills)
- [OpenAI desktop slash menu](https://learn.chatgpt.com/docs/reference/slash-commands)
- [Claude Code skills and arguments](https://code.claude.com/docs/en/skills)
- [Cursor skills](https://cursor.com/help/customization/skills)

This portable skill uses only standard `name` and `description` frontmatter. Claude Code appends arguments when the body has no argument placeholder. No provider-specific shell interpolation or broad tool grants are needed. `agents/openai.yaml` is optional Codex UI metadata.

The installer makes a full project-local copy so references and recipes travel with each installation. It refuses an existing target. It does not edit permissions, configure providers, register arbitrary slash aliases, or establish communication between running agents.

Host support above is documentation-backed. Interactive menu discovery and live generation require a smoke test in each intended host/version.
