# Post-release verification — 2026-10-25

Audited version: [v0.1.0 source commit ec9f229](https://github.com/notEhEnG/art-skill/tree/ec9f2296b9a1a9b9664347864419a155e60174b0). This record documents inspection and executed checks; it does not claim that the findings have been fixed.

## Executed checks

| Check | Result |
| --- | --- |
| Helper contracts | All 14 tests passed with Python 3.14 on Windows. |
| Real Codex installer | The precise `tree/main/skills/art-skill` URL installed successfully into an isolated destination using sparse Git checkout. All 42 canonical skill files matched the source, including all 34 recipes. |
| Project installer dry-run | Exit 0, destination `<project>/.agents/skills/art-skill`, no installation directories created. |
| First saved-plan invocation | Exit 0; missing `output/` parent created automatically. |
| Repeated saved-plan invocation | Exit 2 with File exists; the original plan's SHA-256 remained unchanged. |
| Recipe inventory | The 34 JSON recipe IDs match both README and catalog IDs. |
| Current documentation | Descriptive README rows and consistent Building and Rainbow headings were present. The older name-only rows and inconsistent photo headings were not reproduced. |

Commands used, with isolated output directories substituted for the placeholders:

```text
python -m unittest discover -s tests -v
python tools/install.py --project <empty-project> --agent codex --dry-run
python <repo>/skills/art-skill/scripts/plan_pack.py <repo>/examples/rainy-reading-room.brief.json --out output/plan.json
python <system-skill-installer>/scripts/install-skill-from-github.py --url https://github.com/notEhEnG/art-skill/tree/main/skills/art-skill --dest <isolated-folder> --method git
```

The saved-plan command was run twice from an isolated working folder. The installer smoke test did not replace an active installation. Live image generation and interactive host discovery were not exercised.

## Confirmed recipe issues

All 12 additional recipes contain scene-specific composition instructions inherited from their example photographs. A test brief requested a single ceramic cup against a plain gray studio background, explicitly excluding landscape elements. The generated plan still included:

- `ceramic-mosaic`: a sunset seascape with cloud bands, an island horizon and rippling water.
- `embroidery`: a cloud landscape, cloud volume and blue sky.
- `risograph`: a diagonal roofline, railing and window rhythm.
- `cyanotype`: garden depth and tall conifers.

The [planner](../skills/art-skill/scripts/plan_pack.py) inserts recipe medium and composition strings into its prompts. This establishes conflicting prompt instructions, not a measured model-output failure. Eighteen recipes also contain `real people` in their avoidance lists, creating potential conflicts for portrait requests.

The passing helper tests check planning and filesystem contracts; they do not test subject-independent recipe behavior.

## Other unresolved items

- README and catalog tables are maintained separately. The shipped tests do not check documentation synchronization.
- `DESCRIPTION.txt` is an unexplained one-line repository-description file; no runtime dependency was identified in the inspected source.
- The [photo collection documentation](../examples/photo-variants/README.md) states that authors and source licenses were not supplied. The building photo visibly carries the Redamancy. signature, but this does not establish authorship or redistribution permission for any photo.

Recommended follow-up is to separate reusable style traits from scene-specific briefs, review portrait-related avoidance rules, generate documentation from shared metadata and resolve photo provenance with the supplier. Preserve frozen example recipes and manifests as historical generation records.

The [v0.1.0 release notes](releases/v0.1.0.md) summarize these findings. Its tag, installable ZIP and checksums remain unchanged.
