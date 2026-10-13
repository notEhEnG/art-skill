# Four photographs, six styles each

This gallery contains **24 generated images**: each of the four supplied photographs is independently interpreted in ASCII & Pixels, Sketch & Scribble, Digital Impressionism, Lo-fi Film, Generative Flow and Off-white Minimalism.

| Photo set | Supplied filename | Final images | Actual calls |
| --- | --- | ---: | ---: |
| [Building and rainbow](building-rainbow/README.md) | `444444.jpg` | 6 | 6 |
| [Hillside garden](hillside-garden/README.md) | `11111111.jpg` | 6 | 6 |
| [Sunset bay](sunset-bay/README.md) | `222222222.jpg` | 6 | 6 |
| [Towering cumulus](cumulus-clouds/README.md) | `33333333.jpg` | 6 | 6 |

Each photo page shows all six versions. Every style page links to its actual prompt, brief, offline plan, frozen recipe and generation/review manifest. The same original photograph is used directly for all six versions; variants do not reference one another or combine the four scenes.

## Recorded generation

24 built-in image calls produced 24 saved and visually inspected native PNGs, with no repair calls or observed moderation blocks. Native sizes and SHA-256 hashes are recorded for each output. Source orientation is preserved; requested planner sizes and tool-returned sizes differ, so the actual dimensions are recorded rather than inferred. The tool exposed neither a model identifier nor monetary cost; both remain `null`.

Visual checks covered recognizable subject/composition, distinct medium, palette/texture, and unwanted additions. Some outputs retain source colors or dense detail beyond a recipe's suggestions; those departures are recorded on their style pages. Exact geometry, pixel grids, glyph text, seeds and camera/film calibration are not claimed.

## Source notes

The four original photographs are user-supplied local references and are not redistributed. Their filenames and hashes are recorded in the photo manifests. Authors and source licenses were not supplied. `444444.jpg` visibly carries the “Redamancy.” signature; that visible attribution is recorded without inferring authorship or licensing.

## Try the workflow

```text
Use $art-skill to reinterpret each of my four photos in all six styles.
Create four separate sets, six images each. Use each original photo
directly for all its variants, preserve its orientation and main
composition, and do not combine the scenes. Save the native images,
actual prompts, frozen recipes and review manifests. Allow up to eight
image calls per photo set, including repairs only for concrete defects.
```

The planner remains offline. For example:

```text
python skills/art-skill/scripts/plan_pack.py examples/photo-variants/building-rainbow/ascii-pixels/brief.json
```

Supply your own reference images and replace the filenames in the prompts. `plan.json` describes intended work; `manifest.json` records the actual result. Code/instruction licensing does not establish rights in source photographs or generated imagery.

[Generation index](manifest.json) · [Back to Art Skill](../../README.md)
