# Changelog

Published versions link to their GitHub Releases. Earlier dated entries record development milestones.

## [0.1.0](https://github.com/notEhEnG/art-skill/releases/tag/v0.1.0) — 2026-10-25

First public release: 34 art-direction recipes, 52 reviewed repository examples, offline pack planning and project-local installation for Codex, Claude Code and Cursor.

### Post-release verification — 2026-10-25

- Documented [source-level review results](docs/verification-2026-10-25.md) for the published release. All 14 helper tests, the isolated Codex installer smoke test and the project installer dry-run passed.
- Confirmed that saved-plan parent directories are created automatically and a repeated write exits with code 2 while preserving the existing plan.
- Recorded unresolved recipe issues: all 12 additional recipes contain example-scene instructions, and 18 recipes include a `real people` avoidance rule that can conflict with portrait requests. These findings have not been fixed or tested through new image generation.
- Recorded remaining documentation synchronization and original-photo provenance gaps. The v0.1.0 tag and download assets are unchanged.

### Changed

- Remove the historical research snapshot and its documentation links.
- Clarify `$skill-installer` invocation and terminal clone/setup steps; refresh build-prompt counts and separate current validation from historical records.
- Roll back failed or interrupted project installations across requested hosts, preserving existing content and reporting incomplete cleanup.
- Put installation, first use, host invocation and action examples before the README gallery.
- Replace repeated before/after tables with a shared originals strip and four collapsed thumbnail grids.
- Group all 34 recipe descriptions and practical limits into matching categories.
- Standardize the Building and Rainbow photo name and refresh the workflow-ideas introduction.

### Added

- A versioned installable skill ZIP, SHA-256 checksums and [release notes](docs/releases/v0.1.0.md).
- A first-run prompt with expected output files, troubleshooting, contribution guidance and a known-gaps checklist.
- License, Python and live test-workflow badges, contents navigation and direct evidence links.
- A GitHub Actions workflow for the helper contract tests on Windows and Linux with Python 3.10 and 3.14.

## 2026-10-24

### Added

- Nine optical and material recipes with one reviewed original-photo example each.
- Seven dream and glow recipes with one reviewed original-photo example each.
- Native image dimensions, source/recipe/output hashes, exact prompts and review notes for the new examples, bringing the catalog to 34 recipes and 52 reviewed images.

## Earlier work

- Six core recipes with four source-photo variants each.
- Twelve additional recipes with one reviewed example each.
- Offline pack planning, project-local installers for Codex, Claude Code and Cursor, and nine helper contract tests.
