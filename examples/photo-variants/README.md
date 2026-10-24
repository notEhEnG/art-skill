# Four photographs, six styles each

This gallery contains **24 generated images**: each of the four supplied photographs is independently interpreted in ASCII & Pixels, Sketch & Scribble, Digital Impressionism, Lo-fi Film, Generative Flow and Off-white Minimalism.

| Photo set | Original photograph | Final images | Actual calls |
| --- | --- | ---: | ---: |
| [Building and Rainbow](building-rainbow/README.md) | [building-rainbow.jpg](originals/building-rainbow.jpg) | 6 | 6 |
| [Hillside garden](hillside-garden/README.md) | [hillside-garden.jpg](originals/hillside-garden.jpg) | 6 | 6 |
| [Sunset bay](sunset-bay/README.md) | [sunset-bay.jpg](originals/sunset-bay.jpg) | 6 | 6 |
| [Towering cumulus](cumulus-clouds/README.md) | [cumulus-clouds.jpg](originals/cumulus-clouds.jpg) | 6 | 6 |

Each photo page shows all six versions. Every style page links to its actual prompt, brief, offline plan, frozen recipe and generation/review manifest. The same original photograph is used directly for all six versions; variants do not reference one another or combine the four scenes.

## Recorded generation

24 built-in image calls produced 24 saved and visually inspected native PNGs, with no repair calls or observed moderation blocks. Native sizes and SHA-256 hashes are recorded for each output. Source orientation is preserved; requested planner sizes and tool-returned sizes differ, so the actual dimensions are recorded rather than inferred. The tool exposed neither a model identifier nor monetary cost; both remain `null`.

Visual checks covered recognizable subject/composition, distinct medium, palette/texture, and unwanted additions. Some outputs retain source colors or dense detail beyond a recipe's suggestions; those departures are recorded on their style pages. Exact geometry, pixel grids, glyph text, seeds and camera/film calibration are not claimed.

## Source notes

The four original photographs are included byte-for-byte under descriptive filenames in `originals/` and displayed on their photo pages. The files in Downloads are unchanged. Their SHA-256 hashes are recorded in the photo manifests. Authors and source licenses were not supplied. [building-rainbow.jpg](originals/building-rainbow.jpg) visibly carries the “Redamancy.” signature; it is preserved without inferring authorship or licensing. The repository's MIT license covers its original code and instructions, not an asserted license for these photographs.

Archived prompts, briefs and plans retain the input names used during the recorded generation. Each manifest's `generation_input_filename` maps that historical name to the descriptive `filename` and original-image `path`; the actual prompts have not been rewritten.

## Try the workflow

```text
Use $art-skill to reinterpret each of my four photos in the six original styles listed above.
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

Use the linked original references, or supply your own photos. When rerunning, use the descriptive filenames in your new prompts. `plan.json` describes intended work; `manifest.json` records the actual result. Code/instruction licensing does not establish rights in source photographs or generated imagery.

[More styles and workflow ideas](../../docs/art-ideas.md) · [Generation index](manifest.json) · [Back to Art Skill](../../README.md)
