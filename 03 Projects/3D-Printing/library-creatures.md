---
date: 2026-03-06
tags: [3d-printing, library-creatures, wizard-study]
---

# Library Creatures Series

Original creature designs by Corey, created via AI image generation → MakerWorld image-to-3D pipeline.

## Design Philosophy
- Creatures that look like they could exist on Earth — realistic anatomy, not cartoon
- Each creature has an ecological reason to inhabit a wizard's study/library
- FDM printable: bold forms, no elements thinner than ~3mm, solid fins > separate fingers
- Grounded in real animal base + one library-specific adaptation

## Published Creatures

| Creature | Base Animal | Niche | MakerWorld Stats |
|---|---|---|---|
| Book Mouse | Mouse | Nests in books, collects knowledge | 29 likes, 78 collections, 6 comments, 2 Boosts |
| Spider Imp | Spider | Web-spinner, inhabits dark corners | — |
| Libramite | Mite/insect | Tiny, lives in the microecosystem of tomes | — |

## In Development

### Inkfin
- **Base:** Axolotl/salamander
- **Color:** Deep blue-black (old ink), pale parchment underside, iridescent sheen
- **Signature feature:** Solid fan-shaped crest rising from back of skull — one piece, with feather-quill ridges carved into surface. Glows faintly blue-white at edges.
- **Eyes:** Large, forward-facing, glowing amber-gold
- **Markings:** Faint luminous script-like traces along spine and sides
- **Niche:** Eats silverfish and bookworms (library guardian). Drawn to smell of aged ink and vellum. Sits motionless on book covers — appears to be reading. Nocturnal.
- **Print pose:** Standing on four sturdy legs, head raised, crest fanned
- **Status:** Gemini iteration in progress — needs solid crest (not separate feather fingers), no accessories, no beak

#### Iteration Log

| # | Image | Result | Problem |
|---|---|---|---|
| 1 | unnamed.jpg (dropped 2026-03-06) | Dark axolotl, right colors, blob-style gill stalks | Gills are thick rounded tubes (axolotl-realistic), not a fan/crest — wrong silhouette |
| 2 | unnamed (1).jpg (dropped 2026-03-06) | Dark axolotl, feather-fingers, beak, monocle | Classic Gemini overreach — separate feather fingers + accessories added unprompted |
| Ref | 2025-12-21 webp (inspiration) | White 3D printed lizard/dragon creature leaning against books on a shelf | Excellent style reference — bold FDM forms, right scale, looks at home in a library |

**Current blocker:** Gemini defaults to natural axolotl gill stalks OR separate feather fingers. Need to force the single-piece solid fan crest with language that makes clear it's one unified structure.

#### Gemini Prompt (current best):
```
A fantastical amphibian creature with an axolotl body shape. Dark blue-black smooth skin, pale underside with faint luminous script-like markings.

Head crest: a single solid fan-shaped crest rising from the back of the skull, like a wide fish fin, with deep ridges carved along its surface suggesting feather quills. One solid piece, not separate fingers. The crest glows faintly blue-white at the edges.

Amphibian face — no beak, no accessories, no glasses, no jewelry. Large glowing amber eyes. Soft rounded snout.

Standing on four sturdy legs. Plain white background. No props. Bold, printable forms only — no fine details thinner than 3mm. Fantastical but anatomically grounded.
```

## Candidate Concepts (not yet developed)

| Concept | Base | Hook |
|---|---|---|
| Tome Crab | Hermit crab | Uses a small book as its shell |
| Spine Serpent | Snake | Lives between books, scales like leather binding |
| Scroll Gecko | Gecko | Clings to scroll cases, skin like aged vellum |
| Parchment Moth | Moth | Wings patterned like faded script (fragile to print — caution) |
| Index Beetle | Beetle | Wing cases like illuminated manuscript pages |

## Do Not Revisit
- Anything with separate thin "finger" elements (unprintable on FDM)
- Props/accessories added by Gemini (monocle, chains, etc.) — always negate explicitly
- Pure cartoon/fantasy art style — prompt must specify "nature documentary realism"
