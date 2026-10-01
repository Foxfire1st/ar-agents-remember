# dashboard/src/panels/engine-room/remote.styles.ts

## Governing Overview

[panels/engine-room overview](overview.md)

## Purpose

The remote/PR strip style domain of the Engine Room, split from `engineRoomStyles.ts`
by the 260731-EFA-L8 R6 ruling. Owns the strip header, code-chain and carryover
connectors, and the chip/badge recipes (`remoteChip`, `remoteChipLabel`,
`remoteChipState`, `prBadge`, `prBadgeLabel`, `prBadgeSub`).

## Code Commentary

### Logic

`remoteChip` is a `cva` keyed on tone: planned dashed/muted, live amber outline,
done mint fill. `prBadge` is keyed on open/merged. Connectors are solid amber (code
chain) vs dashed muted (carryover handoff).

### Conventions

Static styles only; the sole motion is the gated fill/stroke transition on a
projection state flip.

### Invariants And Boundaries

These recipes style the strip only; state derivation stays in `remote.tsx`.

### Todos

None recorded.

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

No relevant domain documentation was found.

### Repo-Internal References

- The strip/connector recipes. [1]
- The chip and PR badge recipes. [2]

### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.
