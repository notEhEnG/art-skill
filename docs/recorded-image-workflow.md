# Recorded image workflow, 2026-10-13

During authoring, the local Codex environment exposed an installed image-generation skill and built-in image tool. Their instructions covered text-to-image, edits, image references, transparent backgrounds, one built-in call per distinct asset, visual inspection, and copying project assets into the workspace.

The built-in tool did not expose explicit model, quality, size, or dollar-cost selectors in its available schema. Its exact backend model was not verified. API model documentation does not prove that a given Codex surface uses that same model or exposes the same controls.

This is a capability snapshot of the authoring environment, not a bundled image service or a promise of backend availability in another installation. The starter makes no image API requests. No live generations were submitted during the original draft validation.

Official references for independently checking the selected backend:

- [OpenAI image generation guide](https://developers.openai.com/api/docs/guides/image-generation)
- [OpenAI skills](https://learn.chatgpt.com/docs/build-skills)
- [GPT Image 2.5 Sunburst](https://developers.openai.com/api/docs/models/gpt-image-2.5-sunburst)
