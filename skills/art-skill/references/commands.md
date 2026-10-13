# Command contract

The skill has one entry point, `art-skill`, and eight action arguments. The host loads the skill; the agent interprets the action and runs the workflow. These actions are not shell commands.

Examples on a host with a native `/art-skill` skill command:

```text
/art-skill styles
/art-skill brief a rainy reading-room pack in digital impressionism
/art-skill make a sunlit desk in sketch-scribble, no people or text
/art-skill pack @examples/rainy-reading-room.brief.json
/art-skill remix this image into lo-fi film imagery; preserve the mug and window
/art-skill inspect output/art-skill/rainy-reading-room
/art-skill export output/art-skill/rainy-reading-room as a ZIP
```

Codex fallback: replace `/art-skill` with `$art-skill`, or run `/skills` and select Art Skill. In the desktop app, select the enabled skill in the `/` menu; verify the exact displayed command locally. Do not assert a bare `/art-skill` is registered in every Codex surface.

Natural language works too: “Use Art Skill to make a four-image digital impressionist pack.” A plain request defaults to one image; a pack with no specified count defaults to four total. Show missing input choices only when they affect the result.

Read paths mentioned by the user as input data. Never interpolate prompt text into a shell command. For structured batches, write a brief file and pass its filename to the planner.
