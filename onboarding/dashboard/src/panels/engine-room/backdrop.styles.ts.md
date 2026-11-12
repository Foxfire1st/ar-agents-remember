# dashboard/src/panels/engine-room/backdrop.styles.ts

## Governing Overview

[panels/engine-room overview](overview.md)

## Purpose

The atmospheric backdrop style domain of the Engine Room, split from
`engineRoomStyles.ts` by the 260731-EFA-L8 R6 ruling. Owns the absolutely-positioned
`backdrop` layer, the faint amber-tinted `backdropVideo` (with the radial vignette
mask), and `stageContent`, the scene layer stacked above it.

## Code Commentary

### Logic

`backdrop` pins the layer to the stage (`inset:0`, `pointerEvents:none`,
`overflow:hidden`). `backdropVideo` uses `mixBlendMode:screen` + low opacity and a
radial `maskImage` so faded edges fall back to the dark stage; `stageContent` sits
above it.

### Conventions

Atmosphere only: `aria-hidden` is the component's duty; effects gating is the
caller's (`useShouldAnimate` / effects toggle).

### Invariants And Boundaries

The layer must never intercept pointer events or sit above the scene content.

### Todos

None recorded.

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

No relevant domain documentation was found.

### Repo-Internal References

- The backdrop layer recipes. [1]

### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.
