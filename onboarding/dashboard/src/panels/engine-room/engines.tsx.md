# dashboard/src/panels/engine-room/engines.tsx

## Governing Overview

[panels/engine-room overview](overview.md)

## Purpose

The branch-node and engine-gauge renderers of the Engine Room scene, extracted from
`EnclosureCanvas.tsx` by the 260731-EFA-L8 responsibility split. `BranchNode` draws a
repository branch node (including the pruned/stale-base register); `EngineGauge` draws
the provider engine podracer gauge with its charge, petals, and runtime-state palette.

## Code Commentary

### Logic

`BranchNode` composes label, flags, detach slide, and materialisation opacity from a
`CommitRefNode` plus the landing/detaching/pruned flags. `EngineGauge` maps
`RuntimeState` to the gauge frame/charge/petal treatments (nominal mint, indexing
cyan, down alarm, configured/unknown/missing drained or dashed). Branch-label
truncation and detach delays are computed here as pure helpers.

### Conventions

Colour-as-state: the gauge body carries runtime state; the frame is a constant gold
bezel except `down`, which re-colours red.

### Invariants And Boundaries

These components render only projection data and must never fake a state. Motion
transitions (charge, fault breathe) are driven by GSAP/Motion in the layers, not by
CSS animation in these components.

### Todos

None recorded.

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

No relevant domain documentation was found.

### Repo-Internal References

- The branch-node renderer with landing/pruned registers. [1]
- The runtime-state gauge renderer. [2]

### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.
