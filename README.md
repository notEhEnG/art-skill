# Art Skill

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](#install-by-host)
[![Tests](https://github.com/notEhEnG/art-skill/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/notEhEnG/art-skill/actions/workflows/tests.yml)
[![GitHub Release](https://img.shields.io/github/v/release/notEhEnG/art-skill)](https://github.com/notEhEnG/art-skill/releases/latest)

Reusable art direction for turning briefs and photographs into raster artwork and visual asset packs with an AI agent.

For developers and creators who want reusable styles, bounded image batches and reviewable outputs in Codex, Claude Code or Cursor.

**Status:** 34 bundled recipes and 52 visually reviewed photo-to-style examples; offline planning and project installation are tested. See the [known gaps and roadmap](#known-gaps-and-roadmap) for checks still pending.

## Contents

[Install](#quick-install) · [First run](#first-run-60-second-setup) · [Hosts](#install-by-host) · [Actions](#actions) · [Gallery](#gallery) · [Recipes](#recipes) · [Roadmap](#known-gaps-and-roadmap) · [Troubleshooting](#troubleshooting) · [Contributing](#contributing) · [Releases](#releases) · [Evidence and changelog](#evidence-and-changelog)

## Quick install

Invoke the installer in **Codex chat**, not in a terminal:

```text
$skill-installer install the art-skill skill from https://github.com/notEhEnG/art-skill/tree/main/skills/art-skill
```

Then browse the available styles:

```text
$art-skill styles
```

The installable package is [`skills/art-skill`](skills/art-skill). For project-local copies or another host, use [Install by host](#install-by-host).

## First run: 60-second setup

After installation, send this in **agent chat**, not a terminal:

```text
$art-skill make one landscape sunset bay in watercolor-wash, with no people or lettering. Save the image as artwork.png and the brief, recipe, plan and review manifest in output/art-skill/first-run.
```

The agent reads the recipe, generates one image with its available image tool, reviews it and saves the result. Expected files after a successful run:

```text
output/art-skill/first-run/
  artwork.png       generated image at its native dimensions
  brief.json        subject, purpose and constraints
  style.json        frozen recipe
  plan.json         offline generation plan
  manifest.json     actual prompt, dimensions, hashes and review notes
```

Allow about a minute to choose and send the brief. Generation time depends on the host and can take several minutes. [See a reviewed watercolor sunset example](examples/expanded-styles/watercolor-wash/README.md).

If no image backend is available, the agent saves the brief, prompts and a `requires_backend` plan instead. Installation alone does not provide image generation.

## Install by host

| Host | Install | Invoke in agent chat | Image backend |
| --- | --- | --- | --- |
| Codex | Quick-install prompt above, or `--agent codex` below | `$art-skill styles` | Built-in image tool when available in your session |
| Claude Code | Project installer with `--agent claude` | `/art-skill styles` | Requires a separately configured image tool or provider |
| Cursor | Project installer with `--agent cursor` | `/art-skill styles` | Requires a separately configured image tool or provider |

For project-local installation, first clone the repository and enter its directory in your terminal:

```text
git clone https://github.com/notEhEnG/art-skill.git
cd art-skill
```

Then run the matching command below. **Python 3.10+** is required for these helpers; they use only the standard library. Replace `/path/to/project` with an existing project folder, and quote paths containing spaces.

```text
python tools/install.py --project /path/to/project --agent codex
python tools/install.py --project /path/to/project --agent claude
python tools/install.py --project /path/to/project --agent cursor
```

Choose the command for your host. Add `--dry-run` to preview destinations, or repeat `--agent` to install for multiple hosts. The installer copies the complete skill and refuses to overwrite an existing installation. If a copy fails or is interrupted, it rolls back copies and empty parent directories created by that invocation, preserving existing content. A forced process termination or power loss can still leave partial files; cleanup failures are reported.

Codex project copies go into `.agents/skills/art-skill/`; Claude Code uses `.claude/skills/art-skill/`; Cursor uses `.cursor/skills/art-skill/`.

Host syntax: [OpenAI skills](https://learn.chatgpt.com/docs/build-skills), [Claude Code skills](https://code.claude.com/docs/en/skills), [Cursor skills](https://cursor.com/help/customization/skills). [Host support and testing limits](skills/art-skill/references/hosts.md).

## Actions

These are arguments to the skill, not standalone shell commands. The examples use Codex syntax; replace `$art-skill` with `/art-skill` in Claude Code or Cursor.

| Action | Result | One-line example |
| --- | --- | --- |
| `help` | Explain actions and host invocation | `$art-skill help` |
| `styles` | Show recipes and practical limits | `$art-skill styles` |
| `brief` | Save a brief and plan without generating images | `$art-skill brief a four-image rainy reading-room pack in digital-impressionism` |
| `make` | Generate and review one image | `$art-skill make a sunlit desk in sketch-scribble, no people or text` |
| `pack` | Generate a set with a shared style and anchor | `$art-skill pack four views of a quiet garden in felt-collage` |
| `remix` | Restyle a supplied image while preserving stated details | `$art-skill remix this attached photo in watercolor-wash; preserve its composition` |
| `inspect` | Review existing outputs without generating images | `$art-skill inspect output/art-skill/first-run` |
| `export` | Package reviewed native files and a manifest | `$art-skill export output/art-skill/first-run as a ZIP` |

Attach a photo when using the remix example. Natural language also works: “Use Art Skill to make one clay-diorama image of a reading nook.” See the [command contract](skills/art-skill/references/commands.md) and [pack contract](skills/art-skill/references/pack-contract.md).

## Gallery

The examples use these four unchanged original photographs. Click an original to view it; expand a collection for style thumbnails. Each artwork links to its exact source, prompt, recipe and review notes on the full example page.

| Building and Rainbow | Hillside Garden | Cumulus Clouds | Sunset Bay |
| --- | --- | --- | --- |
| [<img src="examples/photo-variants/originals/building-rainbow.jpg" alt="Original photograph: Building and Rainbow" width="150">](examples/photo-variants/originals/building-rainbow.jpg) | [<img src="examples/photo-variants/originals/hillside-garden.jpg" alt="Original photograph: Hillside Garden" width="150">](examples/photo-variants/originals/hillside-garden.jpg) | [<img src="examples/photo-variants/originals/cumulus-clouds.jpg" alt="Original photograph: Cumulus Clouds" width="150">](examples/photo-variants/originals/cumulus-clouds.jpg) | [<img src="examples/photo-variants/originals/sunset-bay.jpg" alt="Original photograph: Sunset Bay" width="150">](examples/photo-variants/originals/sunset-bay.jpg) |

<details>
<summary>Core styles — 6 recipes</summary>

[Full collection](examples/photo-variants/README.md)

<table>
<tr>
<td width="33%" align="center"><a href="examples/photo-variants/building-rainbow/ascii-pixels/README.md"><img src="examples/photo-variants/building-rainbow/ascii-pixels/artwork.png" alt="ASCII & Pixels generated example" height="150"><br>ASCII & Pixels</a></td>
<td width="33%" align="center"><a href="examples/photo-variants/sunset-bay/sketch-scribble/README.md"><img src="examples/photo-variants/sunset-bay/sketch-scribble/artwork.png" alt="Sketch & Scribble generated example" height="150"><br>Sketch & Scribble</a></td>
<td width="33%" align="center"><a href="examples/photo-variants/hillside-garden/digital-impressionism/README.md"><img src="examples/photo-variants/hillside-garden/digital-impressionism/artwork.png" alt="Digital Impressionism generated example" height="150"><br>Digital Impressionism</a></td>
</tr>
<tr>
<td width="33%" align="center"><a href="examples/photo-variants/sunset-bay/lofi-film/README.md"><img src="examples/photo-variants/sunset-bay/lofi-film/artwork.png" alt="Lo-fi Film Imagery generated example" height="150"><br>Lo-fi Film Imagery</a></td>
<td width="33%" align="center"><a href="examples/photo-variants/cumulus-clouds/generative-flow/README.md"><img src="examples/photo-variants/cumulus-clouds/generative-flow/artwork.png" alt="Generative Flow generated example" height="150"><br>Generative Flow</a></td>
<td width="33%" align="center"><a href="examples/photo-variants/building-rainbow/off-white/README.md"><img src="examples/photo-variants/building-rainbow/off-white/artwork.png" alt="Off-white Minimalism generated example" height="150"><br>Off-white Minimalism</a></td>
</tr>
</table>

</details>

<details>
<summary>Additional styles — 12 recipes</summary>

[Full collection](examples/expanded-styles/README.md)

<table>
<tr>
<td width="33%" align="center"><a href="examples/expanded-styles/watercolor-wash/README.md"><img src="examples/expanded-styles/watercolor-wash/artwork.png" alt="Watercolor Wash generated example" height="150"><br>Watercolor Wash</a></td>
<td width="33%" align="center"><a href="examples/expanded-styles/gouache-poster/README.md"><img src="examples/expanded-styles/gouache-poster/artwork.png" alt="Gouache Poster generated example" height="150"><br>Gouache Poster</a></td>
<td width="33%" align="center"><a href="examples/expanded-styles/linocut/README.md"><img src="examples/expanded-styles/linocut/artwork.png" alt="Linocut generated example" height="150"><br>Linocut</a></td>
</tr>
<tr>
<td width="33%" align="center"><a href="examples/expanded-styles/risograph/README.md"><img src="examples/expanded-styles/risograph/artwork.png" alt="Risograph generated example" height="150"><br>Risograph</a></td>
<td width="33%" align="center"><a href="examples/expanded-styles/stained-glass/README.md"><img src="examples/expanded-styles/stained-glass/artwork.png" alt="Stained Glass generated example" height="150"><br>Stained Glass</a></td>
<td width="33%" align="center"><a href="examples/expanded-styles/cyanotype/README.md"><img src="examples/expanded-styles/cyanotype/artwork.png" alt="Cyanotype generated example" height="150"><br>Cyanotype</a></td>
</tr>
<tr>
<td width="33%" align="center"><a href="examples/expanded-styles/clay-diorama/README.md"><img src="examples/expanded-styles/clay-diorama/artwork.png" alt="Clay Diorama generated example" height="150"><br>Clay Diorama</a></td>
<td width="33%" align="center"><a href="examples/expanded-styles/felt-collage/README.md"><img src="examples/expanded-styles/felt-collage/artwork.png" alt="Felt Collage generated example" height="150"><br>Felt Collage</a></td>
<td width="33%" align="center"><a href="examples/expanded-styles/embroidery/README.md"><img src="examples/expanded-styles/embroidery/artwork.png" alt="Embroidery generated example" height="150"><br>Embroidery</a></td>
</tr>
<tr>
<td width="33%" align="center"><a href="examples/expanded-styles/ink-wash/README.md"><img src="examples/expanded-styles/ink-wash/artwork.png" alt="Ink Wash generated example" height="150"><br>Ink Wash</a></td>
<td width="33%" align="center"><a href="examples/expanded-styles/geometric-facets/README.md"><img src="examples/expanded-styles/geometric-facets/artwork.png" alt="Geometric Facets generated example" height="150"><br>Geometric Facets</a></td>
<td width="33%" align="center"><a href="examples/expanded-styles/ceramic-mosaic/README.md"><img src="examples/expanded-styles/ceramic-mosaic/artwork.png" alt="Ceramic Mosaic generated example" height="150"><br>Ceramic Mosaic</a></td>
</tr>
</table>

</details>

<details>
<summary>Optical and material styles — 9 recipes</summary>

[Full collection](examples/optical-material-styles/README.md)

<table>
<tr>
<td width="33%" align="center"><a href="examples/optical-material-styles/x-ray-transparency/README.md"><img src="examples/optical-material-styles/x-ray-transparency/artwork.png" alt="X-Ray Transparency generated example" height="150"><br>X-Ray Transparency</a></td>
<td width="33%" align="center"><a href="examples/optical-material-styles/macro-microscopy/README.md"><img src="examples/optical-material-styles/macro-microscopy/artwork.png" alt="Macro Microscopy generated example" height="150"><br>Macro Microscopy</a></td>
<td width="33%" align="center"><a href="examples/optical-material-styles/technical-schematic/README.md"><img src="examples/optical-material-styles/technical-schematic/artwork.png" alt="Technical Schematic generated example" height="150"><br>Technical Schematic</a></td>
</tr>
<tr>
<td width="33%" align="center"><a href="examples/optical-material-styles/thermal-infrared/README.md"><img src="examples/optical-material-styles/thermal-infrared/artwork.png" alt="Thermal Infrared generated example" height="150"><br>Thermal Infrared</a></td>
<td width="33%" align="center"><a href="examples/optical-material-styles/gel-lit/README.md"><img src="examples/optical-material-styles/gel-lit/artwork.png" alt="Gel-Lit generated example" height="150"><br>Gel-Lit</a></td>
<td width="33%" align="center"><a href="examples/optical-material-styles/chiaroscuro/README.md"><img src="examples/optical-material-styles/chiaroscuro/artwork.png" alt="Chiaroscuro generated example" height="150"><br>Chiaroscuro</a></td>
</tr>
<tr>
<td width="33%" align="center"><a href="examples/optical-material-styles/aquatic-caustics/README.md"><img src="examples/optical-material-styles/aquatic-caustics/artwork.png" alt="Aquatic Caustics generated example" height="150"><br>Aquatic Caustics</a></td>
<td width="33%" align="center"><a href="examples/optical-material-styles/chrome-futurism/README.md"><img src="examples/optical-material-styles/chrome-futurism/artwork.png" alt="Chrome Futurism generated example" height="150"><br>Chrome Futurism</a></td>
<td width="33%" align="center"><a href="examples/optical-material-styles/wabi-sabi/README.md"><img src="examples/optical-material-styles/wabi-sabi/artwork.png" alt="Wabi-Sabi generated example" height="150"><br>Wabi-Sabi</a></td>
</tr>
</table>

</details>

<details>
<summary>Dream and glow styles — 7 recipes</summary>

[Full collection](examples/dream-glow-styles/README.md)

<table>
<tr>
<td width="33%" align="center"><a href="examples/dream-glow-styles/hyper-bloom/README.md"><img src="examples/dream-glow-styles/hyper-bloom/artwork.png" alt="Hyper Bloom generated example" height="150"><br>Hyper Bloom</a></td>
<td width="33%" align="center"><a href="examples/dream-glow-styles/retro-glow/README.md"><img src="examples/dream-glow-styles/retro-glow/artwork.png" alt="Retro Glow generated example" height="150"><br>Retro Glow</a></td>
<td width="33%" align="center"><a href="examples/dream-glow-styles/hyperglow/README.md"><img src="examples/dream-glow-styles/hyperglow/artwork.png" alt="Hyperglow generated example" height="150"><br>Hyperglow</a></td>
</tr>
<tr>
<td width="33%" align="center"><a href="examples/dream-glow-styles/modern-gradient/README.md"><img src="examples/dream-glow-styles/modern-gradient/artwork.png" alt="Modern Gradient generated example" height="150"><br>Modern Gradient</a></td>
<td width="33%" align="center"><a href="examples/dream-glow-styles/ethereal-core/README.md"><img src="examples/dream-glow-styles/ethereal-core/artwork.png" alt="Ethereal Core generated example" height="150"><br>Ethereal Core</a></td>
<td width="33%" align="center"><a href="examples/dream-glow-styles/xpiritualism/README.md"><img src="examples/dream-glow-styles/xpiritualism/artwork.png" alt="Xpiritualism generated example" height="150"><br>Xpiritualism</a></td>
</tr>
<tr>
<td width="33%" align="center"><a href="examples/dream-glow-styles/webcore/README.md"><img src="examples/dream-glow-styles/webcore/artwork.png" alt="Webcore generated example" height="150"><br>Webcore</a></td>
</tr>
</table>

</details>

Macro Microscopy is an intentional detail study. Other recipes may simplify or abstract the scene; each example records its preservation choices and limitations. The core collection includes all 24 source-photo variants, while the thumbnails above show one example per recipe.

## Recipes

Choose an exact ID with `make`, `remix` or `pack`. All 34 directions are available as recipes. Their palettes and textures are prompt guidance; the linked files contain full review checks and limitations.

### Core styles

| Recipe ID | Direction | Practical limit |
| --- | --- | --- |
| [`ascii-pixels`](skills/art-skill/assets/styles/ascii-pixels.json) | Pixel blocks and glyph-like stippling. | Raster aesthetic; no exact ASCII or pixel-grid guarantee. |
| [`sketch-scribble`](skills/art-skill/assets/styles/sketch-scribble.json) | Gestural pencil and ink with sparse color accents. | Strokes and fine geometry can change during edits. |
| [`digital-impressionism`](skills/art-skill/assets/styles/digital-impressionism.json) | Broken-color brushwork with warm light and cool shadows. | Brushwork and consistency across images need visual review. |
| [`lofi-film`](skills/art-skill/assets/styles/lofi-film.json) | Soft focus, restrained grain and subtle light leaks. | An analog mood, not calibrated film simulation. |
| [`generative-flow`](skills/art-skill/assets/styles/generative-flow.json) | Layered contours, flowing filaments and open space. | Raster art; no executable algorithm or reproducible seed. |
| [`off-white`](skills/art-skill/assets/styles/off-white.json) | Warm neutrals, subtle material texture and spare composition. | Artwork; no functional website or UI contrast guarantee. |

### Additional styles

| Recipe ID | Direction | Practical limit |
| --- | --- | --- |
| [`watercolor-wash`](skills/art-skill/assets/styles/watercolor-wash.json) | Translucent pigment washes with visible paper and soft edges. | Paper and pigment are visual approximations, not a physical simulation. |
| [`gouache-poster`](skills/art-skill/assets/styles/gouache-poster.json) | Opaque matte color shapes with bold light-dark separation. | A poster aesthetic; no print layout or exact typography. |
| [`linocut`](skills/art-skill/assets/styles/linocut.json) | Carved-looking silhouettes and directional relief-print hatching. | Raster art; no cutting template or separated printing plates. |
| [`risograph`](skills/art-skill/assets/styles/risograph.json) | Limited spot-color-like layers, grain and offset edges. | No calibrated inks, color separations or press-ready files. |
| [`stained-glass`](skills/art-skill/assets/styles/stained-glass.json) | Jewel-colored translucent panes with dark leading. | No fabrication pattern or structurally validated glazing design. |
| [`cyanotype`](skills/art-skill/assets/styles/cyanotype.json) | Deep blue and pale-paper tones with botanical print texture. | An image aesthetic, not a photographic exposure process. |
| [`clay-diorama`](skills/art-skill/assets/styles/clay-diorama.json) | Rounded clay miniatures with handmade surface marks. | No 3D model, construction plan or physically accurate material. |
| [`felt-collage`](skills/art-skill/assets/styles/felt-collage.json) | Layered colored felt with fibrous edges and shallow shadows. | No fabric cutting template or stitch pattern. |
| [`embroidery`](skills/art-skill/assets/styles/embroidery.json) | Thread-like contours and directional stitches on woven fabric. | No machine embroidery file or repeatable stitch geometry. |
| [`ink-wash`](skills/art-skill/assets/styles/ink-wash.json) | Restrained grayscale washes, expressive edges and blank paper. | Tonal detail may drift; physical ink diffusion is not simulated. |
| [`geometric-facets`](skills/art-skill/assets/styles/geometric-facets.json) | Flat polygon-like color planes with a clear shape hierarchy. | Raster art; no vector paths or exact polygon topology. |
| [`ceramic-mosaic`](skills/art-skill/assets/styles/ceramic-mosaic.json) | Irregular tile-like shapes, visible grout and glazed highlights. | No tile schedule, fabrication pattern or exact tessellation. |

### Optical and material styles

| Recipe ID | Direction | Practical limit |
| --- | --- | --- |
| [`x-ray-transparency`](skills/art-skill/assets/styles/x-ray-transparency.json) | Translucent shells, ghosted edges and layered inner forms. | Invented layers; not a real X-ray or structural inspection. |
| [`macro-microscopy`](skills/art-skill/assets/styles/macro-microscopy.json) | Enlarged botanical details with translucent cell-like chambers. | May change framing; imagined structures are not biological evidence. |
| [`technical-schematic`](skills/art-skill/assets/styles/technical-schematic.json) | Fine construction lines, sparse guides and blueprint contrast. | Illustrative raster plate; not CAD or verified engineering documentation. |
| [`thermal-infrared`](skills/art-skill/assets/styles/thermal-infrared.json) | False-color zones with soft halos and warm-cool separation. | Artistic colors convey no measured temperature or infrared radiation. |
| [`gel-lit`](skills/art-skill/assets/styles/gel-lit.json) | Cool and warm colored light across clear surface planes. | No calibrated lighting rig or product color-accuracy guarantee. |
| [`chiaroscuro`](skills/art-skill/assets/styles/chiaroscuro.json) | Selective raking light and rich, compressed shadow masses. | Fine shadow detail may be deliberately lost. |
| [`aquatic-caustics`](skills/art-skill/assets/styles/aquatic-caustics.json) | Liquid refraction and interlacing water-light patterns. | No physically validated optics or seamless water texture. |
| [`chrome-futurism`](skills/art-skill/assets/styles/chrome-futurism.json) | Reflective silver shells with restrained iridescent highlights. | Contemporary chrome imagery; no usable 3D material. |
| [`wabi-sabi`](skills/art-skill/assets/styles/wabi-sabi.json) | Muted earth tones, asymmetry and weathered natural surfaces. | A broad visual interpretation, not the full cultural philosophy. |

### Dream and glow styles

| Recipe ID | Direction | Practical limit |
| --- | --- | --- |
| [`hyper-bloom`](skills/art-skill/assets/styles/hyper-bloom.json) | Surreal luminous flowers, translucent petals and glowing pollen. | Imagined blooms are not a botanical record. |
| [`retro-glow`](skills/art-skill/assets/styles/retro-glow.json) | Nostalgic airbrush gradients and sparse star-filter glints. | An illustration aesthetic, not a calibrated film process. |
| [`hyperglow`](skills/art-skill/assets/styles/hyperglow.json) | Spectral contours, saturated halos and prismatic light trails. | No HDR luminance, emissive material or animation. |
| [`modern-gradient`](skills/art-skill/assets/styles/modern-gradient.json) | Broad feathered color fields with subtle, uniform grain. | Intentional abstraction; no exact color profile or vector mesh. |
| [`ethereal-core`](skills/art-skill/assets/styles/ethereal-core.json) | Delicate mist, soft halation and luminous woodland light. | Atmospheric fantasy; hidden photographic detail is not recovered. |
| [`xpiritualism`](skills/art-skill/assets/styles/xpiritualism.json) | Gauzy light veils, fine particles and suspended filaments. | A descriptive aesthetic label, not an established movement or spiritual evidence. |
| [`webcore`](skills/art-skill/assets/styles/webcore.json) | Early-web dithering, mesh patterns, glossy accents and glints. | A static bitmap; no functional UI or exact pixel grid. |

## Known gaps and roadmap

- [x] Offline planning and project-local installation contract tests.
- [x] One visually reviewed example per recipe, with 52 examples across four source photos.
- [ ] Interactive skill discovery and invocation smoke tests in each host/version.
- [ ] A same-style multi-asset pack that verifies shared-anchor consistency.
- [ ] A cutout demo that verifies edge quality and actual transparent pixels.
- [ ] An agent-invoked ZIP/export smoke test across the intended hosts.

The existing galleries are independent style studies. They do not establish consistency across a same-style pack or prove every host can generate images. [Validation details](docs/validation.md).

## Troubleshooting

| Problem | What to try |
| --- | --- |
| Skill does not appear in Codex | Restart Codex. For a project install, check `.agents/skills/art-skill/SKILL.md` in the project you opened. |
| A slash menu does not list the skill | Use the explicit invocation in the host table. In Codex, type `$art-skill help`; natural-language invocation is also available. Interactive menu coverage remains on the roadmap. |
| A brief is saved but no image appears | Check whether the session has an image tool. A `requires_backend` plan means generation could not run; configure a provider for hosts that need one. |
| Installer reports an existing target | Keep the installed copy or choose a different project. The helper deliberately refuses to overwrite it. |
| Planner rejects a style, path or format | Use an exact recipe ID, a quoted existing input path, and PNG or WebP for transparent assets. [Pack contract](skills/art-skill/references/pack-contract.md). |

To check the helpers without generating artwork, run these terminal commands from the repository checkout:

```text
python skills/art-skill/scripts/plan_pack.py examples/rainy-reading-room.brief.json
python -m unittest discover -s tests -v
```

The sample plans four assets with a six-call cap, including two repair slots. Planning makes no image calls. [Tests](tests/test_contracts.py) cover recipe planning, budgets, shared-anchor dependencies, filenames, format compatibility, installation copies, overwrite protection, failed/interrupted-copy rollback and dry-run behavior.

## Contributing

To add your own recipe, start with [the recipe format](docs/recipe-format.md):

1. Add `skills/art-skill/assets/styles/<id>.json` with original trait descriptions, concrete review checks and practical limits.
2. Run the offline planner with the new ID and run the helper tests.
3. Generate and visually review at least one example before describing the recipe as tested. Save its source link, exact prompt, recipe lock, native dimensions, hashes and review notes.
4. Add the example to the relevant collection, then update this README and the [style catalog](skills/art-skill/references/styles.md).

Keep the canonical skill under `skills/art-skill/`; project-local copies are installation outputs. Keep source photographs and existing reviewed images unchanged. See [visual acceptance guidance](skills/art-skill/references/quality.md).

## Releases

The latest release is [v0.2.0](https://github.com/notEhEnG/art-skill/releases/tag/v0.2.0). Download the [installable skill ZIP](https://github.com/notEhEnG/art-skill/releases/download/v0.2.0/art-skill-v0.2.0.zip) and [SHA-256 checksums](https://github.com/notEhEnG/art-skill/releases/download/v0.2.0/SHA256SUMS.txt), or install this exact version through Codex chat:

```text
$skill-installer install the art-skill skill from https://github.com/notEhEnG/art-skill/tree/v0.2.0/skills/art-skill
```

The ZIP contains an `art-skill/` folder with the complete skill, all 34 recipes, the offline planner, license and version. For manual installation, copy that folder into your host's project skill directory listed in [Install by host](#install-by-host). The 52 example images are available in the repository and GitHub source archives; they are excluded from the smaller installable ZIP.

See the [release notes](docs/releases/v0.2.0.md) for changes, verification and known issues. The [v0.1.0 release](https://github.com/notEhEnG/art-skill/releases/tag/v0.1.0) remains available.

## Evidence and changelog

- [Validation record](docs/validation.md): completed checks and outstanding smoke tests.
- [Changelog](CHANGELOG.md): dated changes and unreleased work.
- [Workflow ideas](docs/art-ideas.md): postcard sets, seasonal scenes, wallpaper pairs and place-inspired texture packs.

## License

The [MIT license](LICENSE) covers this repository's original code and instructions. It does not establish rights in source photographs or generated outputs. The four source photographs are preserved unchanged.
