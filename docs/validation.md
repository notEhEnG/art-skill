# Validation, 2026-10-13

Completed:

- Nine helper contract tests passed with Python 3.14 on Windows. They cover the total call cap, all 18 recipe plans, shared-anchor dependencies, format/alpha compatibility, IDs, existing-file preservation and full project-local installation copies.
- The installed skill creator's `quick_validate.py` reported `Skill is valid!` using a workspace-local PyYAML dependency. PyYAML is needed only for that validator, not for the shipped helpers.
- The example brief produced `examples/rainy-reading-room.plan.json`: four assets, six maximum calls, two repair slots, zero executed calls and unknown monetary cost.
- The source video was visually inspected at exact 0–7 second samples; six style captions were recorded. Audio was not transcribed.

- 24 live built-in image calls produced four separate six-style source-photo sets in `examples/photo-variants/`, with zero repairs. Every native PNG has verified SHA-256, CRCs and decodable image data. Actual dimensions and source orientation are recorded; none were inferred from the requested planner sizes.
- README gallery links, per-style prompt/recipe/manifest links and manifest file hashes were checked. Four unchanged original photographs are included under descriptive filenames, with source hashes and gallery paths recorded.

- Twelve additional recipes each have one live visually reviewed example in `examples/expanded-styles/`: 12 built-in calls, zero repairs and zero observed moderation blocks. This brings the public gallery to 36 generated images. Their native PNG integrity, dimensions, hashes, prompts, recipe locks and original-source links were checked. Same-style multi-image consistency is still pending.
- The expanded SKILL.md passed the skill frontmatter validator; the nine helper contract tests passed with all 18 recipes and installation copies.

Pending release checks:

- A four-asset Codex demo, including reference consistency and actual cutout transparency.
- Interactive skill discovery and slash-menu routing in each intended host/version.
- An agent-invoked ZIP/export workflow across intended hosts.

Both example runs (24 original-style images and 12 added-style images) used the Codex built-in image tool. No moderation blocks were observed in their 36 calls. The tool did not expose a model identifier or monetary cost, so neither is inferred. Cross-host backend access is not implied by the installation tests.

These checks make the starter reviewable; they do not establish model quality or production readiness.
