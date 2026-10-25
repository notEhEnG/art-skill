# Validation record

## v0.2.0 release packaging — 2026-10-25

- The v0.2.0 installable ZIP contains 44 files, including all 34 canonical recipes and `VERSION` set to `0.2.0`.
- ZIP integrity and every archived file were checked against their source bytes. After extraction, the packaged planner successfully planned the sample brief with each of the 34 recipes without generating images.
- A SHA-256 checksum file accompanies the ZIP. README release links and local documentation links were checked, and all 14 helper contract tests passed locally on Windows.
- Recipe prompts and runtime behavior are unchanged from v0.1.0. The source review below remains applicable; its unresolved issues are listed in the [v0.2.0 release notes](releases/v0.2.0.md#known-issues).

## Latest source verification — 2026-10-25

The [post-release review](verification-2026-10-25.md) inspected published commit `ec9f2296b9a1a9b9664347864419a155e60174b0` and ran the helper tests, isolated Codex installer, project dry-run and repeated planner command. All 14 helper tests passed; installation destinations and saved-plan overwrite protection behaved as documented.

The review also confirmed unresolved scene-specific recipe instructions and portrait-avoidance conflicts. README/catalog synchronization and original-photo rights remain unverified. No new images were generated, and these issues were not fixed during verification. See the [release's known issues](releases/v0.1.0.md#known-issues).

## Release packaging verification — 2026-10-25

- The `v0.1.0` installable ZIP contains 44 files, including all 34 canonical recipes, references, planner, UI metadata, license and version.
- ZIP integrity and every archived file were checked against their source bytes. After extraction, the packaged planner successfully planned the sample brief with each of the 34 recipes without generating images.
- A SHA-256 checksum file accompanies the installable ZIP. The smaller ZIP excludes the example gallery; full repository source archives retain it.
- All 14 helper contract tests passed locally with Python 3.14 on Windows. The release uses the existing four-configuration CI workflow for Windows/Linux and Python 3.10/3.14.
- README local links and navigation anchors were checked, including the versioned release notes. No new images were generated.

See [v0.1.0 release notes](releases/v0.1.0.md) for installation and known gaps.

## Previous verification — 2026-10-24

Current inventory: **34 recipes, 52 reviewed artwork files and four original photographs**. Older dated sections below describe the catalog and tests that existed during those runs.

- All **14 helper contract tests** passed locally with Python 3.14 on Windows. They exercise every current recipe and installation for all three hosts.
- New installer regression cases cover first/later copy failures, partial-copy removal, rollback of completed copies, preservation of existing content and a target appearing after preflight, interrupted copies, cleanup-failure reporting and dry runs that create nothing.
- Installation success messages are emitted only after every requested host succeeds. Rollback applies to handled errors and interruptions; forced process termination or power loss can still leave partial files. Cleanup failures are explicitly reported.
- All 52 artwork SHA-256 values and native PNG dimensions match their manifests. Referenced source-photo hashes match the four unchanged originals. No artwork was regenerated in this verification.
- README recipe rows, the four collapsed galleries, original-image references, local document links and navigation anchors were checked. The build prompt now describes the full 34-recipe, 52-example catalog.
- [GitHub Actions](../.github/workflows/tests.yml) runs the helper tests on Windows and Linux with Python 3.10 and 3.14. See the [live workflow results](https://github.com/notEhEnG/art-skill/actions/workflows/tests.yml) for commit-specific outcomes.

Live image generation, same-style multi-image consistency, cutout transparency and interactive host discovery were not exercised by this verification. Current outstanding checks are tracked in the [README roadmap](../README.md#known-gaps-and-roadmap).

## Historical validation — 2026-10-13

This run covered the then-current **18 recipes and 36 generated examples**, with nine helper tests. These figures are historical, not the latest inventory.

Completed:

- Nine helper contract tests passed with Python 3.14 on Windows. They cover the total call cap, all 18 recipe plans, shared-anchor dependencies, format/alpha compatibility, IDs, existing-file preservation and full project-local installation copies.
- The installed skill creator's `quick_validate.py` reported `Skill is valid!` using a workspace-local PyYAML dependency. PyYAML is needed only for that validator, not for the shipped helpers.
- The example brief produced `examples/rainy-reading-room.plan.json`: four assets, six maximum calls, two repair slots, zero executed calls and unknown monetary cost.
- The source video was visually inspected at exact 0–7 second samples; six style captions were recorded. Audio was not transcribed.

- 24 live built-in image calls produced four separate six-style source-photo sets in `examples/photo-variants/`, with zero repairs. Every native PNG has verified SHA-256, CRCs and decodable image data. Actual dimensions and source orientation are recorded; none were inferred from the requested planner sizes.
- README gallery links, per-style prompt/recipe/manifest links and manifest file hashes were checked. Four unchanged original photographs are included under descriptive filenames, with source hashes and gallery paths recorded.

- Twelve additional recipes each have one live visually reviewed example in `examples/expanded-styles/`: 12 built-in calls, zero repairs and zero observed moderation blocks. This brings the public gallery to 36 generated images. Their native PNG integrity, dimensions, hashes, prompts, recipe locks and original-source links were checked. Same-style multi-image consistency is still pending.
- The expanded SKILL.md passed the skill frontmatter validator; the nine helper contract tests passed with all 18 recipes and installation copies.

### Checks left pending in that run

- A four-asset Codex demo, including reference consistency and actual cutout transparency.
- Interactive skill discovery and slash-menu routing in each intended host/version.
- An agent-invoked ZIP/export workflow across intended hosts.

Both example runs (24 original-style images and 12 added-style images) used the Codex built-in image tool. No moderation blocks were observed in their 36 calls. The tool did not expose a model identifier or monetary cost, so neither is inferred. Cross-host backend access is not implied by the installation tests.

These checks make the starter reviewable; they do not establish model quality or production readiness.

## Recorded artwork runs — 2026-10-24

- Optical and material styles: 9 live examples, 10 built-in calls and 1 repair. Each native output was visually inspected against its source photo and recipe.
- Dream and glow styles: 7 live examples, 8 built-in calls and 1 repair. Each native output was visually inspected against its source photo and recipe.
- Source and output SHA-256, PNG chunk CRCs, decoded image data, native dimensions, frozen recipes, planner results and relative gallery links were checked. The repository originals remain byte-for-byte unchanged.
- The then-current nine helper contract tests and the skill frontmatter validator were rerun against all 34 recipes. Same-style multi-image consistency and cross-host generation remained pending.
- Model identity and monetary cost were not exposed by the image tool.
