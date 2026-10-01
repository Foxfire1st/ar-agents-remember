# dashboard/src/panels/engine-room/geometry.ts

## Governing Overview

[panels/engine-room overview](overview.md)

## Purpose

The pure geometry and derivation layer of the Engine Room scene, extracted from
`EnclosureCanvas.tsx` by the 260731-EFA-L8 responsibility split. It owns the canvas
coordinate constants, conduit path math, state vocabulary narrowing, and the small
formatting/derivation helpers the scene layers render.

## Code Commentary

### Logic

The column layout is fixed by `COL_MAIN_CX` / `COL_FEAT_CX` / `COL_WT_CX`, and all
node, coupler, and wire positions derive from `POS` / `ENGINE` / `COUPLER_X` /
`OFFICIAL_COUPLER_X` / `EDGE_GEOM`. `conduitState` and `runtimeState` narrow
untrusted server strings to the render vocabulary. `conduitPathD` builds SVG paths
per edge, `refusedPolarityOf` derives the flash polarity from edge state alone
(failed → red, stale → amber), and `branchEnter` computes the build-up materialisation
opacity/dx. `isBlocked`, `truncate`, `alertProps`, and `CLOSEOUT_BEATS` are the shared
render helpers.

### Conventions

Everything here is pure: no DOM, no React, no animation state. Motion properties are
owned by GSAP/Motion in the layer components, never by these constants.

### Invariants And Boundaries

This module must stay free of component imports. `RuntimeState` includes `missing`
(an expected-but-unobserved provider slot) and `unknown`; both render as drained,
not faulting.

### Todos

None recorded.

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

No relevant domain documentation was found.

### Repo-Internal References

- The scene-wide coordinate constants and conduit-path builder consumed by the layers. [1]
- The runtime/state vocabulary narrowing shared by gauges and conduits. [2]
- The materialisation/block derivations this module feeds. [3]

### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.
