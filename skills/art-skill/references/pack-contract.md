# Pack contract, version 1.0

## Brief

See the repository's `examples/rainy-reading-room.brief.json` for a complete brief. Required fields: `schema_version`, `id`, `style`, `subject`, `purpose`, `max_calls`, `assets`. Optional `constraints` contains strings. Each asset has `id`, `role`, `size`, `background`, `format`, and `direction`.

The first asset is the sole anchor and has no `reference`. Every later asset refers directly to that first asset. `size` is a requested target. The v0.1 planner accepts the three conservative API sizes, not all possible model dimensions. Transparent requests require PNG or WebP.

`max_calls` includes all assets and repairs, must be at least the asset count, and cannot exceed the proposed weekend limit of 12. That limit is a product decision, not a model limit. IDs contain lowercase letters, digits and hyphens. The planner validates structure, not rights or moderation.

## Plan

The planner returns the selected recipe, its SHA-256, per-asset prompts, roles, target format/size/background, anchor dependencies, planned status, base call count, repair allowance, and `actual_cost_usd: null`. It never creates images or invents a per-image price.

## Runtime manifest

Extend the plan after execution with pack `status`, `backend`, `model` (null if unknown), `calls_used`, `actual_cost_usd` (null if unknown), and per-asset results:

```json
{
  "id": "anchor",
  "status": "reviewed",
  "path": "images/anchor.png",
  "sha256": "<actual file hash>",
  "native_size": [1536, 1024],
  "transparent_pixels_verified": false,
  "review_notes": ["Palette and medium checked visually"]
}
```

This fragment illustrates the format; it is not a recorded generation. Fill values from actual files/tool results. Use `null` where unknown. Pack statuses: `planned`, `requires_backend`, `partial`, `complete`. Asset statuses: `planned`, `generated`, `reviewed`, `needs_revision`, `blocked`, `missing`. `complete` means all requested assets were saved and reviewed.

Export reviewed native originals first. Delivery-specific crops, typography, bleed, color profiles and print proofs belong to a later explicitly requested workflow.
