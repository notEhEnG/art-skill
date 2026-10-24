# Codex build prompt — Art Skill

The current repository includes 34 recipes and 52 reviewed example images across the core, additional, optical/material and dream/glow collections. Preserve the full catalog when continuing the build. See [the current catalog](../skills/art-skill/references/styles.md) and [gallery](../README.md#gallery).

Paste the instructions below into Codex with the starter folder open. They also describe the repository well enough to scaffold it from scratch.

---

Build **Art Skill**, GitHub repository name **art-skill**, skill name **art-skill**. Its primary output is generated raster images and cohesive visual asset packs. The six core families are ASCII/pixels, sketch/scribble, digital impressionism, lo-fi film, generative-flow raster art, and off-white minimalism; the additional, optical/material and dream/glow collections extend them. Do not implement a website builder or reproduce reference collages.

Use the current starter when present. Complete and verify a small Codex-first v0.1; do not replace it with an ambitious platform. Keep an offline planner and portable SKILL.md. Use the installed skill-creator instructions when creating or updating the skill. Preserve the host's normal implicit invocation behavior.

## Repository layout

```text
art-skill/
  README.md
  LICENSE
  .gitignore
  CHANGELOG.md
  .github/workflows/tests.yml
  skills/art-skill/
    SKILL.md
    agents/openai.yaml
    assets/styles/                 34 JSON recipes across four collections
    references/
      commands.md
      hosts.md
      pack-contract.md
      quality.md
    scripts/plan_pack.py
  tools/install.py
  examples/
    rainy-reading-room.brief.json
    rainy-reading-room.plan.json
    photo-variants/                four originals and 24 core-style examples
    expanded-styles/               12 additional-style examples
    optical-material-styles/       9 optical/material examples
    dream-glow-styles/             7 dream/glow examples
  tests/test_contracts.py
  docs/
    recipe-format.md
    validation.md
```

Use Python 3.10+ and standard-library JSON/hash/file helpers. No runtime package is required for planning or installation. Do not add a database, login flow, hosted app, background scheduling or mandatory MCP server.

## SKILL.md requirements

Preserve the current canonical [`SKILL.md`](../skills/art-skill/SKILL.md) when extending this repository. For a new scaffold, use standard frontmatter such as:

```yaml
---
name: art-skill
description: "Create cohesive generated images and visual asset packs using reusable recipes, a shared reference, bounded batches and visual review. Use for pixel, drawn, painterly, film, abstract-flow, graphic-print, crafted-material, optical and luminous dream aesthetics, including remixing or packaging an image series. Does not implement websites, interactive generative code, exact ASCII text, vector systems or fabrication files."
---
```

Keep the body focused on these rules:

1. Route actions `help`, `styles`, `brief`, `make`, `pack`, `remix`, `inspect`, `export` from the invocation arguments or natural language.
2. Read only the relevant recipe; capture the actual subject, intended use, palette, asset roles, orientations, backgrounds, references and preservation constraints.
3. `brief`, `inspect` and `export` do not generate images. `make` defaults to one image. An unspecified pack defaults to four assets total, with six maximum image calls including repairs.
4. Save a brief, recipe copy and plan before execution. Treat recipe hashes as configuration provenance, not model seeds.
5. Use the available host image backend. On Codex apply the installed imagegen skill and use its built-in tool by default. Do not create a private built-in-tool HTTP endpoint or silently switch to a paid API runner.
6. If no backend exists, complete the prompts and mark `requires_backend`. No fabricated image paths or placeholder artwork presented as generated output.
7. Generate and inspect the anchor first. Freeze it and use it directly for every derivative; do not chain variants.
8. Inspect local reference images before edits and label their roles. Use actual documented tool arguments only. A requested size is not an enforced size when the backend exposes no size control.
9. Review subject, palette, medium, texture, crop, unwanted lettering/marks, invariants and actual transparency. Record failures. A returned image does not automatically pass visual review.
10. Repairs must address a specific defect and count against the same cap. Respect moderation failures and deliver useful partial packs honestly.
11. Persist project-bound images in the workspace. Record real dimensions, format, hashes, prompts, references, backend/model when known, calls used, review outcomes and actual cost when available. Unknown values remain null.
12. Export reviewed native originals and their manifest, optionally as a ZIP. Preserve alpha; do not silently crop/upscale or label them print-ready.

Put host details and examples in references rather than bloating the main skill. `agents/openai.yaml` should have display name Art Skill, a short UI description, and a default prompt mentioning `$art-skill`. Do not add broad tool grants or disable implicit invocation just because slash commands are requested.

## Real host command support

- Codex: install at `<project>/.agents/skills/art-skill/`; use `$art-skill` or CLI/IDE `/skills`. The desktop app lists enabled skills in its slash menu; check the exact displayed alias in the installed version.
- Claude Code: install at `<project>/.claude/skills/art-skill/`; `/art-skill pack …` invokes the skill. Arguments are appended by the host when no placeholder is present.
- Cursor: install at `<project>/.cursor/skills/art-skill/`; `/art-skill …` invokes it.

One entry point plus action arguments is enough. Do not claim that SKILL.md can register arbitrary commands across all hosts. Do not overwrite native `/review`, `/status` or `/init`.

The installer must copy the complete skill/resources into explicitly selected project directories, support `--dry-run`, reject an existing target, and refuse targets resolving outside the named project. If copying fails or is interrupted, roll back copies and empty parent directories created by that invocation; preserve existing content and report cleanup failures. This is error rollback, not a crash-atomic filesystem transaction. Installing a skill must not change provider or permission configuration.

Official references to verify before changing host behavior:

- https://learn.chatgpt.com/docs/build-skills
- https://learn.chatgpt.com/docs/reference/slash-commands
- https://code.claude.com/docs/en/skills
- https://cursor.com/help/customization/skills

## Recipe files

Use this JSON format:

```json
{
  "schema_version": "1.0",
  "id": "digital-impressionism",
  "version": "1.0.0",
  "label": "Digital Impressionism",
  "traits": {
    "medium": "Original painterly raster illustration using broken-color strokes",
    "palette": ["#ECDCB8", "#557C91", "#71978A", "#B67A53", "#E4B75E"],
    "texture": "Short layered brush marks with coherent brush scale",
    "composition": "Readable forms, softened edges and breathing room",
    "lighting": "Warm scattered highlights balanced with cool shadows"
  },
  "avoid": ["real people", "copyrighted characters", "logos and brand marks", "copied artworks", "unrequested lettering"],
  "review_checks": ["broken-color brushwork", "warm/cool balance", "matching brush scale"],
  "limitations": ["Palette and geometry require visual review across images"]
}
```

Use original descriptive traits, not named-artist imitation or copied prompt catalogs. ASCII/pixels is a raster aesthetic and does not guarantee valid text or exact grids. Generative flow is a raster aesthetic and supplies no executable algorithm. Lo-fi film is not a calibrated film simulation. Off-white assets are not functional UIs.

## Example and plan

The example subject is an empty original reading room with a rain-streaked window, an unbranded terracotta mug and an open book, with no people, logos or lettering. Purpose: an illustrated pack for a reading journal and its website. Use `digital-impressionism`, four assets and six total calls:

| ID | Role | Requested size | Background | Reference |
| --- | --- | --- | --- | --- |
| anchor | Landscape hero | 1536x1024 | opaque | none |
| cover | Square cover | 1024x1024 | opaque | anchor |
| poster | Portrait composition | 1024x1536 | opaque | anchor |
| mug-cutout | Mug/book vignette | 1024x1024 | transparent | anchor |

The planner validates IDs, known recipe, required fields, unique assets, supported target sizes, transparency/format compatibility, first-asset anchor, direct anchor references and a total cap from the asset count to 12. The twelve-call ceiling is this product's MVP limit, not a model limit.

Generate a deterministic JSON plan with prompts, requested output properties, planned filenames, recipe version/hash, anchor ID, base calls, repair allowance and `generation_performed: false`. It makes no network calls and does not overwrite an existing output file.

## Live execution and sample output

After helper checks pass, use Codex's available image tool to create the four-asset demonstration. This prompt authorizes that demo within the six-call cap. If the tool is unavailable, do not silently invoke an API; leave the demo explicitly pending and complete all offline checks.

Save actual artwork under `output/art-skill/rainy-reading-room/images/`; create `manifest.json` from real results. Review all four files and include a preview when possible. Derive dimensions and hashes from the returned files. For transparency, verify transparent pixels, not merely an alpha-capable format. The backend/model/cost can be null when unexposed.

Export reviewed originals and manifest to a new `export/` directory; make an export ZIP. Use available normal file/image-inspection utilities for metadata and packaging. Make image edits through the image tool; do not use a local drawing script as a substitute for the requested generated raster artwork.

## Tests and acceptance

Run the existing helper tests, or implement equivalent checks for:

- Four planned jobs, two repair slots, zero executed calls, and unknown monetary cost.
- Every bundled recipe can plan the example.
- Chained derivatives fail; all derivatives must use the anchor.
- Total cap includes repairs and rejects undersized caps, excessive caps and booleans.
- Transparent JPEG, duplicate/unsafe IDs and unknown styles fail clearly.
- Planning cannot overwrite an existing result.
- Project installation copies the full resources for all three hosts and preserves existing installations.
- Failed or interrupted copies roll back this invocation's installations and empty parent directories; a target appearing after preflight remains untouched.
- Dry runs create no installation directories.

Run the skill-creator validator; if its YAML dependency is missing, use a workspace-local validation dependency rather than adding an unnecessary runtime requirement. Check reference links and recipe paths.

Manually confirm host discovery and command routing when each host is available. Report unsupported smoke tests as pending. Structural tests do not prove image quality or native command registration.

Acceptance: the skill loads on Codex; `styles` shows all 34 bundled recipes; `brief` emits a plan without generation; `pack` preserves the shared anchor and call cap; `inspect` records observed outcomes; `export` packages reviewed native files and their manifest. Preserve all 52 reviewed examples. Four reviewed same-style demo assets are a separate release target, not a result to fabricate when generation fails.

Finish with saved artifact paths, tests run, image calls used, demo outcomes and any pending host checks. Keep GitHub creation, publishing and plugin-directory submission outside this build task. The repo should be ready for the user to review and publish.
