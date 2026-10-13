# Art Skill

An art-direction skill for Codex and other AI agents, with reusable styles and slash-command workflows for images and visual asset packs.

**Status:** usable skill with tested offline planning, installation, and 24 visually reviewed photo-to-style examples. Cross-host slash-menu discovery, a same-style multi-asset pack and cutout transparency still need smoke tests.

## Four photos × six styles

**24 generated reference images.** Each supplied photo has its own six-style gallery, using that original directly for every version. Click any artwork to open its prompt, recipe and recorded result.

### Building and rainbow — `444444.jpg`

| ASCII & Pixels | Sketch & Scribble |
| --- | --- |
| [![ASCII & Pixels](examples/photo-variants/building-rainbow/ascii-pixels/artwork.png)](examples/photo-variants/building-rainbow/ascii-pixels/README.md) | [![Sketch & Scribble](examples/photo-variants/building-rainbow/sketch-scribble/artwork.png)](examples/photo-variants/building-rainbow/sketch-scribble/README.md) |

| Digital Impressionism | Lo-fi Film Imagery |
| --- | --- |
| [![Digital Impressionism](examples/photo-variants/building-rainbow/digital-impressionism/artwork.png)](examples/photo-variants/building-rainbow/digital-impressionism/README.md) | [![Lo-fi Film Imagery](examples/photo-variants/building-rainbow/lofi-film/artwork.png)](examples/photo-variants/building-rainbow/lofi-film/README.md) |

| Generative Flow | Off-white Minimalism |
| --- | --- |
| [![Generative Flow](examples/photo-variants/building-rainbow/generative-flow/artwork.png)](examples/photo-variants/building-rainbow/generative-flow/README.md) | [![Off-white Minimalism](examples/photo-variants/building-rainbow/off-white/artwork.png)](examples/photo-variants/building-rainbow/off-white/README.md) |

### Hillside garden — `11111111.jpg`

| ASCII & Pixels | Sketch & Scribble |
| --- | --- |
| [![ASCII & Pixels](examples/photo-variants/hillside-garden/ascii-pixels/artwork.png)](examples/photo-variants/hillside-garden/ascii-pixels/README.md) | [![Sketch & Scribble](examples/photo-variants/hillside-garden/sketch-scribble/artwork.png)](examples/photo-variants/hillside-garden/sketch-scribble/README.md) |

| Digital Impressionism | Lo-fi Film Imagery |
| --- | --- |
| [![Digital Impressionism](examples/photo-variants/hillside-garden/digital-impressionism/artwork.png)](examples/photo-variants/hillside-garden/digital-impressionism/README.md) | [![Lo-fi Film Imagery](examples/photo-variants/hillside-garden/lofi-film/artwork.png)](examples/photo-variants/hillside-garden/lofi-film/README.md) |

| Generative Flow | Off-white Minimalism |
| --- | --- |
| [![Generative Flow](examples/photo-variants/hillside-garden/generative-flow/artwork.png)](examples/photo-variants/hillside-garden/generative-flow/README.md) | [![Off-white Minimalism](examples/photo-variants/hillside-garden/off-white/artwork.png)](examples/photo-variants/hillside-garden/off-white/README.md) |

### Sunset bay — `222222222.jpg`

| ASCII & Pixels | Sketch & Scribble |
| --- | --- |
| [![ASCII & Pixels](examples/photo-variants/sunset-bay/ascii-pixels/artwork.png)](examples/photo-variants/sunset-bay/ascii-pixels/README.md) | [![Sketch & Scribble](examples/photo-variants/sunset-bay/sketch-scribble/artwork.png)](examples/photo-variants/sunset-bay/sketch-scribble/README.md) |

| Digital Impressionism | Lo-fi Film Imagery |
| --- | --- |
| [![Digital Impressionism](examples/photo-variants/sunset-bay/digital-impressionism/artwork.png)](examples/photo-variants/sunset-bay/digital-impressionism/README.md) | [![Lo-fi Film Imagery](examples/photo-variants/sunset-bay/lofi-film/artwork.png)](examples/photo-variants/sunset-bay/lofi-film/README.md) |

| Generative Flow | Off-white Minimalism |
| --- | --- |
| [![Generative Flow](examples/photo-variants/sunset-bay/generative-flow/artwork.png)](examples/photo-variants/sunset-bay/generative-flow/README.md) | [![Off-white Minimalism](examples/photo-variants/sunset-bay/off-white/artwork.png)](examples/photo-variants/sunset-bay/off-white/README.md) |

### Towering cumulus — `33333333.jpg`

| ASCII & Pixels | Sketch & Scribble |
| --- | --- |
| [![ASCII & Pixels](examples/photo-variants/cumulus-clouds/ascii-pixels/artwork.png)](examples/photo-variants/cumulus-clouds/ascii-pixels/README.md) | [![Sketch & Scribble](examples/photo-variants/cumulus-clouds/sketch-scribble/artwork.png)](examples/photo-variants/cumulus-clouds/sketch-scribble/README.md) |

| Digital Impressionism | Lo-fi Film Imagery |
| --- | --- |
| [![Digital Impressionism](examples/photo-variants/cumulus-clouds/digital-impressionism/artwork.png)](examples/photo-variants/cumulus-clouds/digital-impressionism/README.md) | [![Lo-fi Film Imagery](examples/photo-variants/cumulus-clouds/lofi-film/artwork.png)](examples/photo-variants/cumulus-clouds/lofi-film/README.md) |

| Generative Flow | Off-white Minimalism |
| --- | --- |
| [![Generative Flow](examples/photo-variants/cumulus-clouds/generative-flow/artwork.png)](examples/photo-variants/cumulus-clouds/generative-flow/README.md) | [![Off-white Minimalism](examples/photo-variants/cumulus-clouds/off-white/artwork.png)](examples/photo-variants/cumulus-clouds/off-white/README.md) |

[All photo sets and source notes](examples/photo-variants/README.md) · [Recorded generation index](examples/photo-variants/manifest.json)

Recorded run: 24 built-in image calls, 24 native PNGs, zero repairs. Actual dimensions and review notes are recorded per image; model identity and monetary cost were not exposed. Originals remain local.

## Start in a project

Requires Python 3.10+ for the helpers. They use only the standard library.

From this repository, install the full skill into an existing project:

```text
python tools/install.py --project /path/to/project --agent codex --dry-run
python tools/install.py --project /path/to/project --agent codex
```

On Windows, quote a project path with spaces. Replace `/path/to/project` with the actual existing folder. The installer refuses an existing `art-skill` skill rather than replacing it.

For another host, use `--agent claude` or `--agent cursor`; repeat `--agent` to install for multiple hosts.

## Invoke the skill

- Codex: `$art-skill styles` or CLI/IDE `/skills` then select it. In the desktop app, enabled skills appear in the `/` menu; verify the exact displayed alias locally.
- Claude Code / Cursor: `/art-skill styles`.
- Natural language: “Use Art Skill to make a digital impressionist image pack for a rainy reading room.”

The actions are `help`, `styles`, `brief`, `make`, `pack`, `remix`, `inspect`, and `export`. They are arguments to the skill, not separate global commands.

Official invocation sources: [OpenAI skills](https://learn.chatgpt.com/docs/build-skills), [OpenAI desktop slash menu](https://learn.chatgpt.com/docs/reference/slash-commands), [Claude Code skills](https://code.claude.com/docs/en/skills), [Cursor skills](https://cursor.com/help/customization/skills).

Skill installation and image-tool availability are separate. Codex uses its available built-in image workflow. Claude Code and Cursor need a separately configured image backend. Without one, the skill produces prompts and a `requires_backend` plan. This repository does not bundle an API client or make network requests.

## Preview the example without generating images

```text
python skills/art-skill/scripts/plan_pack.py examples/rainy-reading-room.brief.json
python skills/art-skill/scripts/plan_pack.py examples/rainy-reading-room.brief.json --out output/plan.json
python -m unittest discover -s tests -v
```

The sample requests four assets: landscape anchor, square cover, portrait composition and transparent mug/book vignette. Its six-call cap includes up to two repairs. Every derivative references the same anchor. The planner refuses unsupported combinations such as transparent JPEG and never overwrites an existing plan.

## Recipes

| ID | Direction | Practical limit |
| --- | --- | --- |
| `ascii-pixels` | Pixel blocks and glyph-like stippling | Raster aesthetic; no exact ASCII/grid guarantee |
| `sketch-scribble` | Gestural pencil/ink on paper | Strokes can change during edits |
| `digital-impressionism` | Broken-color strokes and warm/cool light | Visual consistency needs review |
| `lofi-film` | Soft focus, restrained grain and light leaks | Aesthetic, not calibrated film simulation |
| `generative-flow` | Layered contours and filaments | Raster art, not executable seeded code |
| `off-white` | Warm neutral still life and empty space | Artwork, not a functional website |

The recipes are original descriptions of broad visual traits. No presenter images, video collages, artist works or brand marks are included. The gallery contains generated artwork inspired by user-provided landscape photographs; the originals are not bundled.

## Repository map

```text
skills/art-skill/
  SKILL.md
  agents/openai.yaml
  assets/styles/                  six JSON recipes
  scripts/plan_pack.py            offline planning
  references/                    commands, hosts, contracts, visual checks
examples/
  rainy-reading-room.brief.json
  rainy-reading-room.plan.json    actual planner output; no artwork
  photo-variants/                 four photos × six styles, prompts and manifests
tools/install.py
tests/test_contracts.py
docs/research-evidence.json
docs/recipe-format.md
docs/validation.md
LICENSE
```

Keep one canonical skill under `skills/`; project copies are installation outputs. A later plugin or MCP adapter can distribute the workflow or supply tools without changing its pack contract.

MIT license covers this original starter's code and instructions. It does not establish rights in third-party references or future generated outputs.
