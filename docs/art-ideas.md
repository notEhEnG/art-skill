# Additional styles and workflow ideas

Art Skill includes **34 recipes** across core, additional, optical/material and dream/glow collections. This page covers the twelve additional styles and four ways to build asset packs. Each style listed here has a visually reviewed example. Use the exact ID with `remix`, `make` or `pack`; the IDs are style arguments, not new slash commands. [Browse all twelve generated examples](../examples/expanded-styles/README.md).

## Twelve additional styles

| Style ID | Visual direction | Live example | Review priority |
| --- | --- | --- | --- |
| `watercolor-wash` | Translucent washes, visible paper and soft pigment edges; leave small highlights unpainted. | [Watercolor Wash example](../examples/expanded-styles/watercolor-wash/README.md) | Keep the low horizon and separate cloud layers readable. |
| `gouache-poster` | Opaque matte color, simplified shapes and bold light/dark separation. | [Gouache Poster example](../examples/expanded-styles/gouache-poster/README.md) | Preserve tree rhythm without flattening every depth layer. |
| `linocut` | Two-tone carved-looking shapes, strong silhouettes and directional hatch marks. | [Linocut example](../examples/expanded-styles/linocut/README.md) | Distinguish trunks, foliage and the path with clear negative space. |
| `risograph` | Two or three spot-color-like layers, grain and slight offset edges. | [Risograph example](../examples/expanded-styles/risograph/README.md) | Preserve the roofline and windows; treat the print effect as an aesthetic. |
| `stained-glass` | Translucent jewel-colored panes separated by dark structural lines. | [Stained Glass example](../examples/expanded-styles/stained-glass/README.md) | Keep the cloud silhouette recognizable instead of random pane subdivision. |
| `cyanotype` | Deep blue ground, pale silhouettes and a quiet paper-print texture. | [Cyanotype example](../examples/expanded-styles/cyanotype/README.md) | Retain a coherent tonal hierarchy in dense foliage. |
| `clay-diorama` | Rounded hand-formed shapes, small material imperfections and gentle miniature lighting. | [Clay Diorama example](../examples/expanded-styles/clay-diorama/README.md) | Keep windows and railing readable without inventing extra objects. |
| `felt-collage` | Colored textile shapes, soft fiber edges and shallow layered shadows. | [Felt Collage example](../examples/expanded-styles/felt-collage/README.md) | Simplify foliage while retaining the slope and central conifers. |
| `embroidery` | Thread-like strokes, stitched contours and a fabric background. | [Embroidery example](../examples/expanded-styles/embroidery/README.md) | Thread directions should describe cloud volume, with no invented lettering. |
| `ink-wash` | Restrained grayscale washes, expressive contours and deliberate blank paper. | [Ink Wash example](../examples/expanded-styles/ink-wash/README.md) | Preserve bright lobes and cool shadow masses. |
| `geometric-facets` | Flat polygon-like color planes and a limited palette. | [Geometric Facets example](../examples/expanded-styles/geometric-facets/README.md) | Keep the horizon and sky/water separation; this is raster art. |
| `ceramic-mosaic` | Small irregular tile-like shapes with visible grout and selective color variation. | [Ceramic Mosaic example](../examples/expanded-styles/ceramic-mosaic/README.md) | Maintain large cloud and reflection patterns before adding tile detail. |

These describe raster aesthetics. Exact spot separations, physically accurate materials, repeatable tile/stitch geometry and production-ready print files have not been verified.

## Suggested first styles to try

1. **Watercolor wash:** a softer treatment for the sunset and cloud photographs, with a clear contrast to the existing pixel and film examples.
2. **Risograph:** a compact graphic direction for postcard sets and covers, using a shared small palette across all four scenes.
3. **Clay diorama:** a playful material treatment of the building and garden, useful for exploring a recognizable scene series.

All twelve recipes use the [existing recipe format](recipe-format.md) and were exercised through the offline planner before generation. Every example records actual dimensions, source/recipe/image hashes and review notes. Unknown model and cost fields remain `null`. One example per recipe does not establish same-style multi-image consistency.

## Four workflow ideas beyond style transfer

| Workflow | Inputs | Output pack | What to check |
| --- | --- | --- | --- |
| Trip postcard set | A small photo collection, trip notes and one selected recipe | One cohesive image per stop, with a separate caption file | No invented location facts; reserve clear space for captions added during layout. |
| Seasonal scene series | One reference scene, a selected recipe and four seasonal briefs | Four intentional seasonal interpretations | Preserve the viewpoint and major landmarks; label the scenes as imagined variations. |
| Wallpaper pair | One scene, a recipe and chosen portrait/landscape compositions | A phone-oriented image and desktop-oriented image | Inspect each composition separately; record actual dimensions and keep subject details away from interface areas. |
| Place-inspired texture pack | A photograph and a small palette | A cover, two abstract textures and an illustrated accent | Review motifs and crop safety; do not claim seamless tiling or transparency without checking. |

Each workflow has structured inputs, a bounded output set, visual review and a manifest. It should use the host's configured image tool; no new backend or paid API integration is implied.

[Current recipes and gallery](../README.md) · [Reference photographs](../examples/photo-variants/README.md)
