# dashboard/src/panels/engine-room/remote.tsx

## Governing Overview

[panels/engine-room overview](overview.md)

## Purpose

The remote/PR strip renderers of the Engine Room scene, extracted from
`EnclosureCanvas.tsx` by the 260731-EFA-L8 responsibility split. `RemoteChip` renders
one origin ref as a colour-as-state chip, `PrBadge` the open/merged PR pill, and
`RemoteStrip` the band that orders refs code-first (`origin-feat → PR → origin-main →
origin-mem-main`).

## Code Commentary

### Logic

Chip tone derives from `LandingRefNode` state (planned dashed/muted · live amber
outline · done mint fill). `RemoteStrip` renders the strip only while an enclosure is
landing and drops missing probe refs; the connector wires come from the remote styles.

### Conventions

Refs are coloured by their actual state only; a planned ref is never shown in the live
register. Labels stay readable at the 0.76× canvas scale.

### Invariants And Boundaries

The strip is render-only: it never probes refs itself; refs arrive from the projection.

### Todos

None recorded.

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

No relevant domain documentation was found.

### Repo-Internal References

- The strip/band composition and its chip/badge primitives. [1]

### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.
