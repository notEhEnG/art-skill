# More directions for Art Skill

The six bundled recipes have a 24-image reference gallery. The twelve directions below are **proposals**, not installed recipes or tested image examples. Their names are candidate recipe IDs, not extra slash commands. Each would follow the existing remix/pack workflow: preserve the original subject, freeze a recipe, generate one anchor, inspect it, then reference that anchor for a bounded series.

## Twelve additional styles

| Proposed ID | Visual direction | First photo to try | Review priority |
| --- | --- | --- | --- |
| `watercolor-wash` | Translucent washes, visible paper and soft pigment edges; leave small highlights unpainted. | [Sunset bay](../examples/photo-variants/sunset-bay/README.md) | Keep the low horizon and separate cloud layers readable. |
| `gouache-poster` | Opaque matte color, simplified shapes and bold light/dark separation. | [Hillside garden](../examples/photo-variants/hillside-garden/README.md) | Preserve tree rhythm without flattening every depth layer. |
| `linocut` | Two-tone carved-looking shapes, strong silhouettes and directional hatch marks. | [Hillside garden](../examples/photo-variants/hillside-garden/README.md) | Distinguish trunks, foliage and the path with clear negative space. |
| `risograph` | Two or three spot-color-like layers, grain and slight offset edges. | [Building and rainbow](../examples/photo-variants/building-rainbow/README.md) | Preserve the roofline and windows; treat the print effect as an aesthetic. |
| `stained-glass` | Translucent jewel-colored panes separated by dark structural lines. | [Towering cumulus](../examples/photo-variants/cumulus-clouds/README.md) | Keep the cloud silhouette recognizable instead of random pane subdivision. |
| `cyanotype` | Deep blue ground, pale silhouettes and a quiet paper-print texture. | [Hillside garden](../examples/photo-variants/hillside-garden/README.md) | Retain a coherent tonal hierarchy in dense foliage. |
| `clay-diorama` | Rounded hand-formed shapes, small material imperfections and gentle miniature lighting. | [Building and rainbow](../examples/photo-variants/building-rainbow/README.md) | Keep windows and railing readable without inventing extra objects. |
| `felt-collage` | Colored textile shapes, soft fiber edges and shallow layered shadows. | [Hillside garden](../examples/photo-variants/hillside-garden/README.md) | Simplify foliage while retaining the slope and central conifers. |
| `embroidery` | Thread-like strokes, stitched contours and a fabric background. | [Towering cumulus](../examples/photo-variants/cumulus-clouds/README.md) | Thread directions should describe cloud volume, with no invented lettering. |
| `ink-wash` | Restrained grayscale washes, expressive contours and deliberate blank paper. | [Towering cumulus](../examples/photo-variants/cumulus-clouds/README.md) | Preserve bright lobes and cool shadow masses. |
| `geometric-facets` | Flat polygon-like color planes and a limited palette. | [Sunset bay](../examples/photo-variants/sunset-bay/README.md) | Keep the horizon and sky/water separation; this is raster art. |
| `ceramic-mosaic` | Small irregular tile-like shapes with visible grout and selective color variation. | [Sunset bay](../examples/photo-variants/sunset-bay/README.md) | Maintain large cloud and reflection patterns before adding tile detail. |

These describe raster aesthetics. Exact spot separations, physically accurate materials, repeatable tile/stitch geometry and production-ready print files have not been verified.

## Best first additions

1. **Watercolor wash:** a softer treatment for the sunset and cloud photographs, with a clear contrast to the existing pixel and film examples.
2. **Risograph:** a compact graphic direction for postcard sets and covers, using a shared small palette across all four scenes.
3. **Clay diorama:** a playful material treatment of the building and garden, useful for exploring a recognizable scene series.

For any selected direction, add one recipe using the [existing recipe format](recipe-format.md), run the offline planner, and generate one reviewed example before describing that recipe as supported. Keep unknown model and cost fields `null`.

## Four workflow ideas beyond style transfer

| Workflow | Inputs | Output pack | What to check |
| --- | --- | --- | --- |
| Trip postcard set | A small photo collection, trip notes and one selected recipe | One cohesive image per stop, with a separate caption file | No invented location facts; reserve clear space for captions added during layout. |
| Seasonal scene series | One reference scene, a selected recipe and four seasonal briefs | Four intentional seasonal interpretations | Preserve the viewpoint and major landmarks; label the scenes as imagined variations. |
| Wallpaper pair | One scene, a recipe and chosen portrait/landscape compositions | A phone-oriented image and desktop-oriented image | Inspect each composition separately; record actual dimensions and keep subject details away from interface areas. |
| Place-inspired texture pack | A photograph and a small palette | A cover, two abstract textures and an illustrated accent | Review motifs and crop safety; do not claim seamless tiling or transparency without checking. |

Each workflow has structured inputs, a bounded output set, visual review and a manifest. It should use the host's configured image tool; no new backend or paid API integration is implied.

[Current recipes and gallery](../README.md) · [Reference photographs](../examples/photo-variants/README.md)
