# Validation, 2026-10-13

Completed:

- Nine helper contract tests passed with Python 3.14 on Windows. They cover the total call cap, six recipe plans, shared-anchor dependencies, format/alpha compatibility, IDs, existing-file preservation and full project-local installation copies.
- The installed skill creator's `quick_validate.py` reported `Skill is valid!` using a workspace-local PyYAML dependency. PyYAML is needed only for that validator, not for the shipped helpers.
- The example brief produced `examples/rainy-reading-room.plan.json`: four assets, six maximum calls, two repair slots, zero executed calls and unknown monetary cost.
- The source video was visually inspected at exact 0–7 second samples; six style captions were recorded. Audio was not transcribed.

- 24 live built-in image calls produced four separate six-style source-photo sets in `examples/photo-variants/`, with zero repairs. Every native PNG has verified SHA-256, CRCs and decodable image data. Actual dimensions and source orientation are recorded; none were inferred from the requested planner sizes.
- README gallery links, per-style prompt/recipe/manifest links and manifest file hashes were checked. Four unchanged original photographs are included under descriptive filenames, with source hashes and gallery paths recorded.

Pending release checks:

- A four-asset Codex demo, including reference consistency and actual cutout transparency.
- Interactive skill discovery and slash-menu routing in each intended host/version.
- An agent-invoked ZIP/export workflow across intended hosts.

This 24-image run used the Codex built-in image tool. No moderation blocks were observed in its 24 calls. The tool did not expose a model identifier or monetary cost, so neither is inferred. Cross-host backend access is not implied by the installation tests.

These checks make the starter reviewable; they do not establish model quality or production readiness.
