# Validation, 2026-10-13

Completed:

- Nine helper contract tests passed with Python 3.14 on Windows. They cover the total call cap, six recipe plans, shared-anchor dependencies, format/alpha compatibility, IDs, existing-file preservation and full project-local installation copies.
- The installed skill creator's `quick_validate.py` reported `Skill is valid!` using a workspace-local PyYAML dependency. PyYAML is needed only for that validator, not for the shipped helpers.
- The example brief produced `examples/rainy-reading-room.plan.json`: four assets, six maximum calls, two repair slots, zero executed calls and unknown monetary cost.
- The source video was visually inspected at exact 0–7 second samples; six style captions were recorded. Audio was not transcribed.

Pending release checks:

- Live generation and visual acceptance for any of the six recipes.
- A four-asset Codex demo, including reference consistency and actual cutout transparency.
- Interactive skill discovery and slash-menu routing in each intended host/version.
- Actual generated-image export and manifest validation.

No image-generation requests were submitted, so there is no measured per-image price, live latency, or generation moderation outcome to report. Cross-host backend access is not implied by the installation tests.

These checks make the starter reviewable; they do not establish model quality or production readiness.
