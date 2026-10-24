# Art Skill

An art-direction skill for Codex and other AI agents, with reusable styles and slash-command workflows for images and visual asset packs.

**Status:** usable skill with tested offline planning and installation, 34 bundled recipes, and 52 visually reviewed photo-to-style examples. Cross-host slash-menu discovery, a same-style multi-asset pack and cutout transparency still need smoke tests.

## Quick install

Copy this into Codex:

```text
Hey Codex, please install this skill for me: https://github.com/notEhEnG/art-skill
```

The installable skill is in [`skills/art-skill`](https://github.com/notEhEnG/art-skill/tree/main/skills/art-skill). Codex's skill installer supports GitHub repositories; if a newly installed skill does not appear, restart Codex. [Official installation guidance](https://learn.chatgpt.com/docs/build-skills).

After installation, try `$art-skill styles`. See the invocation and manual project installation options below.

## Six featured styles

One generated example per core style, paired with its original photo. Click an artwork for its prompt, recipe and review notes, or an original to view the source photograph.

### ASCII & Pixels — Building and Rainbow

| Original photo | Generated example |
| --- | --- |
| [<img src="examples/photo-variants/originals/building-rainbow.jpg" alt="Original photograph: Building and Rainbow" width="360">](examples/photo-variants/originals/building-rainbow.jpg) | [<img src="examples/photo-variants/building-rainbow/ascii-pixels/artwork.png" alt="ASCII & Pixels: Building and Rainbow" width="360">](examples/photo-variants/building-rainbow/ascii-pixels/README.md) |

### Sketch & Scribble — Sunset Bay

| Original photo | Generated example |
| --- | --- |
| [<img src="examples/photo-variants/originals/sunset-bay.jpg" alt="Original photograph: Sunset Bay" width="360">](examples/photo-variants/originals/sunset-bay.jpg) | [<img src="examples/photo-variants/sunset-bay/sketch-scribble/artwork.png" alt="Sketch & Scribble: Sunset Bay" width="360">](examples/photo-variants/sunset-bay/sketch-scribble/README.md) |

### Digital Impressionism — Hillside Garden

| Original photo | Generated example |
| --- | --- |
| [<img src="examples/photo-variants/originals/hillside-garden.jpg" alt="Original photograph: Hillside Garden" width="360">](examples/photo-variants/originals/hillside-garden.jpg) | [<img src="examples/photo-variants/hillside-garden/digital-impressionism/artwork.png" alt="Digital Impressionism: Hillside Garden" width="360">](examples/photo-variants/hillside-garden/digital-impressionism/README.md) |

### Lo-fi Film Imagery — Sunset Bay

| Original photo | Generated example |
| --- | --- |
| [<img src="examples/photo-variants/originals/sunset-bay.jpg" alt="Original photograph: Sunset Bay" width="360">](examples/photo-variants/originals/sunset-bay.jpg) | [<img src="examples/photo-variants/sunset-bay/lofi-film/artwork.png" alt="Lo-fi Film Imagery: Sunset Bay" width="360">](examples/photo-variants/sunset-bay/lofi-film/README.md) |

### Generative Flow — Cumulus Clouds

| Original photo | Generated example |
| --- | --- |
| [<img src="examples/photo-variants/originals/cumulus-clouds.jpg" alt="Original photograph: Cumulus Clouds" width="360">](examples/photo-variants/originals/cumulus-clouds.jpg) | [<img src="examples/photo-variants/cumulus-clouds/generative-flow/artwork.png" alt="Generative Flow: Cumulus Clouds" width="360">](examples/photo-variants/cumulus-clouds/generative-flow/README.md) |

### Off-white Minimalism — Building and Rainbow

| Original photo | Generated example |
| --- | --- |
| [<img src="examples/photo-variants/originals/building-rainbow.jpg" alt="Original photograph: Building and Rainbow" width="360">](examples/photo-variants/originals/building-rainbow.jpg) | [<img src="examples/photo-variants/building-rainbow/off-white/artwork.png" alt="Off-white Minimalism: Building and Rainbow" width="360">](examples/photo-variants/building-rainbow/off-white/README.md) |

## Twelve additional styles

One example for each of these twelve recipes, using the same four original photos. Every artwork is paired with the exact photograph used to generate it. Click an artwork for its prompt, recipe and recorded review.

### Watercolor Wash — Sunset Bay

| Original photo | Generated example |
| --- | --- |
| [<img src="examples/photo-variants/originals/sunset-bay.jpg" alt="Original photograph: Sunset Bay" width="360">](examples/photo-variants/originals/sunset-bay.jpg) | [<img src="examples/expanded-styles/watercolor-wash/artwork.png" alt="Watercolor Wash: Sunset Bay" width="360">](examples/expanded-styles/watercolor-wash/README.md) |

### Gouache Poster — Hillside Garden

| Original photo | Generated example |
| --- | --- |
| [<img src="examples/photo-variants/originals/hillside-garden.jpg" alt="Original photograph: Hillside Garden" width="360">](examples/photo-variants/originals/hillside-garden.jpg) | [<img src="examples/expanded-styles/gouache-poster/artwork.png" alt="Gouache Poster: Hillside Garden" width="360">](examples/expanded-styles/gouache-poster/README.md) |

### Linocut — Hillside Garden

| Original photo | Generated example |
| --- | --- |
| [<img src="examples/photo-variants/originals/hillside-garden.jpg" alt="Original photograph: Hillside Garden" width="360">](examples/photo-variants/originals/hillside-garden.jpg) | [<img src="examples/expanded-styles/linocut/artwork.png" alt="Linocut: Hillside Garden" width="360">](examples/expanded-styles/linocut/README.md) |

### Risograph — Building and Rainbow

| Original photo | Generated example |
| --- | --- |
| [<img src="examples/photo-variants/originals/building-rainbow.jpg" alt="Original photograph: Building and Rainbow" width="360">](examples/photo-variants/originals/building-rainbow.jpg) | [<img src="examples/expanded-styles/risograph/artwork.png" alt="Risograph: Building and Rainbow" width="360">](examples/expanded-styles/risograph/README.md) |

### Stained Glass — Cumulus Clouds

| Original photo | Generated example |
| --- | --- |
| [<img src="examples/photo-variants/originals/cumulus-clouds.jpg" alt="Original photograph: Cumulus Clouds" width="360">](examples/photo-variants/originals/cumulus-clouds.jpg) | [<img src="examples/expanded-styles/stained-glass/artwork.png" alt="Stained Glass: Cumulus Clouds" width="360">](examples/expanded-styles/stained-glass/README.md) |

### Cyanotype — Hillside Garden

| Original photo | Generated example |
| --- | --- |
| [<img src="examples/photo-variants/originals/hillside-garden.jpg" alt="Original photograph: Hillside Garden" width="360">](examples/photo-variants/originals/hillside-garden.jpg) | [<img src="examples/expanded-styles/cyanotype/artwork.png" alt="Cyanotype: Hillside Garden" width="360">](examples/expanded-styles/cyanotype/README.md) |

### Clay Diorama — Building and Rainbow

| Original photo | Generated example |
| --- | --- |
| [<img src="examples/photo-variants/originals/building-rainbow.jpg" alt="Original photograph: Building and Rainbow" width="360">](examples/photo-variants/originals/building-rainbow.jpg) | [<img src="examples/expanded-styles/clay-diorama/artwork.png" alt="Clay Diorama: Building and Rainbow" width="360">](examples/expanded-styles/clay-diorama/README.md) |

### Felt Collage — Hillside Garden

| Original photo | Generated example |
| --- | --- |
| [<img src="examples/photo-variants/originals/hillside-garden.jpg" alt="Original photograph: Hillside Garden" width="360">](examples/photo-variants/originals/hillside-garden.jpg) | [<img src="examples/expanded-styles/felt-collage/artwork.png" alt="Felt Collage: Hillside Garden" width="360">](examples/expanded-styles/felt-collage/README.md) |

### Embroidery — Cumulus Clouds

| Original photo | Generated example |
| --- | --- |
| [<img src="examples/photo-variants/originals/cumulus-clouds.jpg" alt="Original photograph: Cumulus Clouds" width="360">](examples/photo-variants/originals/cumulus-clouds.jpg) | [<img src="examples/expanded-styles/embroidery/artwork.png" alt="Embroidery: Cumulus Clouds" width="360">](examples/expanded-styles/embroidery/README.md) |

### Ink Wash — Cumulus Clouds

| Original photo | Generated example |
| --- | --- |
| [<img src="examples/photo-variants/originals/cumulus-clouds.jpg" alt="Original photograph: Cumulus Clouds" width="360">](examples/photo-variants/originals/cumulus-clouds.jpg) | [<img src="examples/expanded-styles/ink-wash/artwork.png" alt="Ink Wash: Cumulus Clouds" width="360">](examples/expanded-styles/ink-wash/README.md) |

### Geometric Facets — Sunset Bay

| Original photo | Generated example |
| --- | --- |
| [<img src="examples/photo-variants/originals/sunset-bay.jpg" alt="Original photograph: Sunset Bay" width="360">](examples/photo-variants/originals/sunset-bay.jpg) | [<img src="examples/expanded-styles/geometric-facets/artwork.png" alt="Geometric Facets: Sunset Bay" width="360">](examples/expanded-styles/geometric-facets/README.md) |

### Ceramic Mosaic — Sunset Bay

| Original photo | Generated example |
| --- | --- |
| [<img src="examples/photo-variants/originals/sunset-bay.jpg" alt="Original photograph: Sunset Bay" width="360">](examples/photo-variants/originals/sunset-bay.jpg) | [<img src="examples/expanded-styles/ceramic-mosaic/artwork.png" alt="Ceramic Mosaic: Sunset Bay" width="360">](examples/expanded-styles/ceramic-mosaic/README.md) |

More examples: [four photos in all six core styles](examples/photo-variants/README.md) · [twelve additional styles](examples/expanded-styles/README.md) · [all 34 recipes](skills/art-skill/references/styles.md).

## Optical and material styles

9 more recipes using the original repository photos. [Browse the collection](examples/optical-material-styles/README.md) for prompts, recipes and recorded reviews.

### X-Ray Transparency — Building Rainbow

| Original photo | Generated example |
| --- | --- |
| [<img src="examples/photo-variants/originals/building-rainbow.jpg" alt="Original building rainbow photograph" width="360">](examples/photo-variants/originals/building-rainbow.jpg) | [<img src="examples/optical-material-styles/x-ray-transparency/artwork.png" alt="X-Ray Transparency generated example" width="360">](examples/optical-material-styles/x-ray-transparency/README.md) |

### Macro Microscopy — Hillside Garden

| Original photo | Generated example |
| --- | --- |
| [<img src="examples/photo-variants/originals/hillside-garden.jpg" alt="Original hillside garden photograph" width="360">](examples/photo-variants/originals/hillside-garden.jpg) | [<img src="examples/optical-material-styles/macro-microscopy/artwork.png" alt="Macro Microscopy generated example" width="360">](examples/optical-material-styles/macro-microscopy/README.md) |

### Technical Schematic — Building Rainbow

| Original photo | Generated example |
| --- | --- |
| [<img src="examples/photo-variants/originals/building-rainbow.jpg" alt="Original building rainbow photograph" width="360">](examples/photo-variants/originals/building-rainbow.jpg) | [<img src="examples/optical-material-styles/technical-schematic/artwork.png" alt="Technical Schematic generated example" width="360">](examples/optical-material-styles/technical-schematic/README.md) |

### Thermal Infrared — Sunset Bay

| Original photo | Generated example |
| --- | --- |
| [<img src="examples/photo-variants/originals/sunset-bay.jpg" alt="Original sunset bay photograph" width="360">](examples/photo-variants/originals/sunset-bay.jpg) | [<img src="examples/optical-material-styles/thermal-infrared/artwork.png" alt="Thermal Infrared generated example" width="360">](examples/optical-material-styles/thermal-infrared/README.md) |

### Gel-Lit — Building Rainbow

| Original photo | Generated example |
| --- | --- |
| [<img src="examples/photo-variants/originals/building-rainbow.jpg" alt="Original building rainbow photograph" width="360">](examples/photo-variants/originals/building-rainbow.jpg) | [<img src="examples/optical-material-styles/gel-lit/artwork.png" alt="Gel-Lit generated example" width="360">](examples/optical-material-styles/gel-lit/README.md) |

### Chiaroscuro — Cumulus Clouds

| Original photo | Generated example |
| --- | --- |
| [<img src="examples/photo-variants/originals/cumulus-clouds.jpg" alt="Original cumulus clouds photograph" width="360">](examples/photo-variants/originals/cumulus-clouds.jpg) | [<img src="examples/optical-material-styles/chiaroscuro/artwork.png" alt="Chiaroscuro generated example" width="360">](examples/optical-material-styles/chiaroscuro/README.md) |

### Aquatic Caustics — Sunset Bay

| Original photo | Generated example |
| --- | --- |
| [<img src="examples/photo-variants/originals/sunset-bay.jpg" alt="Original sunset bay photograph" width="360">](examples/photo-variants/originals/sunset-bay.jpg) | [<img src="examples/optical-material-styles/aquatic-caustics/artwork.png" alt="Aquatic Caustics generated example" width="360">](examples/optical-material-styles/aquatic-caustics/README.md) |

### Chrome Futurism — Building Rainbow

| Original photo | Generated example |
| --- | --- |
| [<img src="examples/photo-variants/originals/building-rainbow.jpg" alt="Original building rainbow photograph" width="360">](examples/photo-variants/originals/building-rainbow.jpg) | [<img src="examples/optical-material-styles/chrome-futurism/artwork.png" alt="Chrome Futurism generated example" width="360">](examples/optical-material-styles/chrome-futurism/README.md) |

### Wabi-Sabi — Hillside Garden

| Original photo | Generated example |
| --- | --- |
| [<img src="examples/photo-variants/originals/hillside-garden.jpg" alt="Original hillside garden photograph" width="360">](examples/photo-variants/originals/hillside-garden.jpg) | [<img src="examples/optical-material-styles/wabi-sabi/artwork.png" alt="Wabi-Sabi generated example" width="360">](examples/optical-material-styles/wabi-sabi/README.md) |

## Dream and glow styles

7 more recipes using the original repository photos. [Browse the collection](examples/dream-glow-styles/README.md) for prompts, recipes and recorded reviews.

### Hyper Bloom — Hillside Garden

| Original photo | Generated example |
| --- | --- |
| [<img src="examples/photo-variants/originals/hillside-garden.jpg" alt="Original hillside garden photograph" width="360">](examples/photo-variants/originals/hillside-garden.jpg) | [<img src="examples/dream-glow-styles/hyper-bloom/artwork.png" alt="Hyper Bloom generated example" width="360">](examples/dream-glow-styles/hyper-bloom/README.md) |

### Retro Glow — Sunset Bay

| Original photo | Generated example |
| --- | --- |
| [<img src="examples/photo-variants/originals/sunset-bay.jpg" alt="Original sunset bay photograph" width="360">](examples/photo-variants/originals/sunset-bay.jpg) | [<img src="examples/dream-glow-styles/retro-glow/artwork.png" alt="Retro Glow generated example" width="360">](examples/dream-glow-styles/retro-glow/README.md) |

### Hyperglow — Cumulus Clouds

| Original photo | Generated example |
| --- | --- |
| [<img src="examples/photo-variants/originals/cumulus-clouds.jpg" alt="Original cumulus clouds photograph" width="360">](examples/photo-variants/originals/cumulus-clouds.jpg) | [<img src="examples/dream-glow-styles/hyperglow/artwork.png" alt="Hyperglow generated example" width="360">](examples/dream-glow-styles/hyperglow/README.md) |

### Modern Gradient — Sunset Bay

| Original photo | Generated example |
| --- | --- |
| [<img src="examples/photo-variants/originals/sunset-bay.jpg" alt="Original sunset bay photograph" width="360">](examples/photo-variants/originals/sunset-bay.jpg) | [<img src="examples/dream-glow-styles/modern-gradient/artwork.png" alt="Modern Gradient generated example" width="360">](examples/dream-glow-styles/modern-gradient/README.md) |

### Ethereal Core — Hillside Garden

| Original photo | Generated example |
| --- | --- |
| [<img src="examples/photo-variants/originals/hillside-garden.jpg" alt="Original hillside garden photograph" width="360">](examples/photo-variants/originals/hillside-garden.jpg) | [<img src="examples/dream-glow-styles/ethereal-core/artwork.png" alt="Ethereal Core generated example" width="360">](examples/dream-glow-styles/ethereal-core/README.md) |

### Xpiritualism — Cumulus Clouds

| Original photo | Generated example |
| --- | --- |
| [<img src="examples/photo-variants/originals/cumulus-clouds.jpg" alt="Original cumulus clouds photograph" width="360">](examples/photo-variants/originals/cumulus-clouds.jpg) | [<img src="examples/dream-glow-styles/xpiritualism/artwork.png" alt="Xpiritualism generated example" width="360">](examples/dream-glow-styles/xpiritualism/README.md) |

### Webcore — Building Rainbow

| Original photo | Generated example |
| --- | --- |
| [<img src="examples/photo-variants/originals/building-rainbow.jpg" alt="Original building rainbow photograph" width="360">](examples/photo-variants/originals/building-rainbow.jpg) | [<img src="examples/dream-glow-styles/webcore/artwork.png" alt="Webcore generated example" width="360">](examples/dream-glow-styles/webcore/README.md) |

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
| `watercolor-wash` | Watercolor Wash | Paper and pigment behavior are visual approximations, not a physical watercolor simulation. |
| `gouache-poster` | Gouache Poster | A poster aesthetic does not supply print layouts or guarantee exact typography. |
| `linocut` | Linocut | Raster art only; no cutting template, separated plates or carve-ready geometry is supplied. |
| `risograph` | Risograph | No actual spot-color separations, calibrated inks or press-ready print files are generated. |
| `stained-glass` | Stained Glass | No fabrication pattern, cut lines or structurally validated glazing design is supplied. |
| `cyanotype` | Cyanotype | This is an image aesthetic, not a real photographic exposure or calibrated cyanotype process. |
| `clay-diorama` | Clay Diorama | Raster visualization only; no 3D model, mesh, construction plan or physically accurate material is supplied. |
| `felt-collage` | Felt Collage | No fabric cutting template or stitch pattern is supplied. |
| `embroidery` | Embroidery | No machine embroidery file, thread specification or repeatable stitch geometry is generated. |
| `ink-wash` | Ink Wash | Wash edges and tonal detail may drift during edits; physical ink diffusion is not simulated. |
| `geometric-facets` | Geometric Facets | Raster illustration only; no vector paths or exact polygon topology is supplied. |
| `ceramic-mosaic` | Ceramic Mosaic | No tile schedule, fabrication pattern, seamless texture or exact tessellation is supplied. |
| `aquatic-caustics` | Aquatic Caustics: water-refraction and caustic-light-inspired image | Refraction and caustics are visual approximations; no physically validated optical simulation or seamless water texture is supplied. |
| `chiaroscuro` | Chiaroscuro: dramatic light-and-shadow tonal image | Fine shadow details may be deliberately lost; this is an artistic tonal treatment rather than recovered photographic information. |
| `chrome-futurism` | Chrome Futurism: contemporary liquid-chrome speculative material image | A contemporary chrome interpretation, not an art-historical reconstruction or a usable 3D material. |
| `gel-lit` | Gel-Lit: colored-gel studio-lighting-inspired architectural image | A lighting aesthetic; it does not specify a calibrated light rig, product color accuracy or a physical miniature. |
| `macro-microscopy` | Macro Microscopy: microscopy-inspired botanical macro illustration | Cell-like structures are imagined; the image cannot identify species, demonstrate biological anatomy or substitute for microscopy. |
| `technical-schematic` | Technical Schematic: architectural technical-drawing-inspired raster plate | An illustrative raster plate, not CAD, a dimensioned drawing, a buildable blueprint or verified engineering documentation. |
| `thermal-infrared` | Thermal Infrared: false-color thermal-imaging-inspired landscape | False colors are artistic choices; ordinary photographs do not establish temperature, emissivity or measured infrared radiation. |
| `wabi-sabi` | Wabi-Sabi: quiet weathered-material landscape interpretation | A broad visual interpretation of weathering and restraint; it does not represent the full cultural or philosophical meaning of wabi-sabi. |
| `x-ray-transparency` | X-Ray Transparency: editorial radiograph-inspired translucent material study | Invented interior layers are artistic; this is not a real X-ray, inspection result or accurate structural disclosure. |
| `ethereal-core` | Ethereal Core: dreamlike luminous woodland landscape | Atmospheric fantasy treatment; it cannot restore hidden detail and does not certify a photographic location or physical lighting conditions. |
| `hyper-bloom` | Hyper Bloom: surreal luminous botanical landscape | Flower forms and colors are imagined; this is not a botanical record or a guarantee of realistic plant morphology. |
| `hyperglow` | Hyperglow: high-energy spectral glow abstraction | A raster light effect; no HDR luminance, emissive material, animation or calibrated spectral behavior is provided. |
| `modern-gradient` | Modern Gradient: contemporary soft-grain gradient abstraction | The scene is intentionally abstracted; no exact color profile, banding-free display guarantee or vector gradient mesh is supplied. |
| `retro-glow` | Retro Glow: retro-fantasy airbrushed landscape with star-filter highlights | A nostalgic illustration aesthetic, not a calibrated film process or an exact reconstruction of any historical advertisement. |
| `webcore` | Webcore: early-web-inspired raster collage aesthetic | A static bitmap aesthetic; it is not a functional website, UI implementation, exact pixel grid or guaranteed readable text. |
| `xpiritualism` | Xpiritualism: speculative luminous-particle and veil abstraction | A descriptive aesthetic label, not a standardized art movement or evidence of spiritual phenomena. |

The recipes are original descriptions of broad visual traits. No presenter images, video collages, artist works or brand marks are included. The gallery includes four user-provided reference photographs and their generated artwork. Source names are descriptive; the supplied files and visible credits are preserved.

## More art ideas

The twelve additional directions are now bundled recipes with live examples: **watercolor wash, gouache poster, linocut, risograph, stained glass, cyanotype, clay diorama, felt collage, embroidery, ink wash, geometric facets, and ceramic mosaic**.

[See the added styles and four asset-pack workflow ideas](docs/art-ideas.md). All 34 recipes are available now; the workflow ideas describe ways to use them. Same-style pack consistency still needs a separate smoke test.

## Repository map

```text
skills/art-skill/
  SKILL.md
  agents/openai.yaml
  assets/styles/                  34 JSON recipes
  scripts/plan_pack.py            offline planning
  references/                    commands, hosts, contracts, visual checks
examples/
  rainy-reading-room.brief.json
  rainy-reading-room.plan.json    actual planner output; no artwork
  photo-variants/                 four originals × six styles, prompts and manifests
    originals/                    unchanged photos with descriptive filenames
  expanded-styles/                twelve more recipes, one live example each
  dream-glow-styles/             recipes with reviewed original-photo examples
  optical-material-styles/       recipes with reviewed original-photo examples
tools/install.py
tests/test_contracts.py
docs/research-evidence.json
docs/recipe-format.md
docs/art-ideas.md                  twelve added styles and four pack ideas
docs/validation.md
LICENSE
```

Keep one canonical skill under `skills/`; project copies are installation outputs. A later plugin or MCP adapter can distribute the workflow or supply tools without changing its pack contract.

MIT license covers this original starter's code and instructions. It does not establish rights in third-party references or future generated outputs.
