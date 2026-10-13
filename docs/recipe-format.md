# Recipe format

A recipe is a JSON file under `skills/art-skill/assets/styles/<id>.json`. Its ID matches the filename. Read the selected file only, then save a copy and its source hash with each pack.

```json
{
  "schema_version": "1.0",
  "id": "my-style",
  "version": "1.0.0",
  "label": "My Style",
  "traits": {
    "medium": "A concise visual medium description",
    "palette": ["#F3EFE5", "#524D43"],
    "texture": "Material and mark-making rules",
    "composition": "Framing and empty-space rules",
    "lighting": "Light and mood rules"
  },
  "avoid": ["logos and brand marks", "copied artworks"],
  "review_checks": ["A concrete visual property to inspect"],
  "limitations": ["What this recipe must not promise"]
}
```

The palette and other traits are prompt guidance, not hard model controls. Exact matching is unverified until outputs are inspected. The file hash identifies saved art-direction instructions; it does not make generation deterministic.

To add a recipe, write original trait descriptions, document its limitations, run the planner against it, and inspect at least one live generated example before advertising it as tested. User-supplied preferences take precedence; save any adapted recipe as a separate version and record the changes.

The planner validates briefs. It assumes the bundled recipe files are maintained repository assets, not an arbitrary external recipe schema validator.
