# dashboard/src/panels/engine-room/layout.styles.ts

## Governing Overview

[panels/engine-room overview](overview.md)

## Purpose

The room-layout and health/fact style domain of the Engine Room, split from
`engineRoomStyles.ts` by the 260731-EFA-L8 R6 ruling. Owns the full-bleed room
shell/grid/stage/zones/header, the left enclosure stack (with `stackList` top-aligned
so single rows keep intrinsic height), health dots, phase/fact chips, node boxes, and
the official strip labels.

## Code Commentary

### Logic

Static atoms are `css({...})`; stateful treatments are `cva` keyed on one semantic
axis (`stackItem`, `healthDot`, `phaseChip`, `factChip`, `nodeBox`, `roomCaution`).
All colours go through `token(colors.*)`.

### Conventions

Colour-as-state; no animation in this domain (motion lives in GSAP/Motion).

### Invariants And Boundaries

`stackList` keeps `overflowX:hidden` + `minWidth:0` so the repo label ellipsizes and
the phase pill never clips.

### Todos

None recorded.

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

No relevant domain documentation was found.

### Repo-Internal References

- The room layout recipes. [1]
- The stack/health/fact recipes. [2]

### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.
