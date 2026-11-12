# dashboard/src/panels/engine-room/stage.styles.ts

## Governing Overview

[panels/engine-room overview](overview.md)

## Purpose

The pod-stage scene style domain of the Engine Room, split from `engineRoomStyles.ts`
by the 260731-EFA-L8 R6 ruling. Owns the scene SVG/world labels, enclosure border,
SVG node boxes, pruned-node register, canopy stroke, lane flags, and warp-coupler
geometry.

## Code Commentary

### Logic

`sceneSvg` carries layout only (no global transition substrate — motion is
GSAP/Motion).
`prunedNode` is the dormant/desaturated stale-base register.

### Conventions

CSS is static; property-split law: a class opacity must never shadow a Motion-owned
value.

### Invariants And Boundaries

This domain contains no animations and no dynamic per-beat styles.

### Todos

None recorded.

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

No relevant domain documentation was found.

### Repo-Internal References

- The static scene, node, canopy, lane-flag and warp-coupler recipes. [1]

- The pruned-node recipe retains the dormant/desaturated stale-base register. [2]

### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.
