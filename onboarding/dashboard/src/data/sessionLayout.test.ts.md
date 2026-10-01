# dashboard/src/data/sessionLayout.test.ts

## Governing Overview

[data overview](overview.md)

## Purpose

The narrow-width/floor/rail-default unit suite (260715-FEUI-L1 S2 R3; eight cases in the current
suite): downward crossings collapse, upward crossings expand, and a user's manual choice below
the threshold is never fought.

## Code Commentary

### Logic

- **autoCollapseTransition** — collapse on a downward crossing / expand on the way back up (both
  thresholds); QUIET while staying on one side (the manual-reopen-respected rule); first-measure
  collapse only when already below.
- **The ~80-col floor** — flags `ptyFloorPx()-1`, not the floor itself, and never a 0-width
  (hidden-layer) stage.
- **railDefaultPercent** (round 2, finding 4) — pixel→percentage conversion (1280/1920/900),
  min/max clamps (2560→12, 400→40), and the unmeasured fallback (0/-5 →
  `RAIL_FALLBACK_PERCENT`).
- **hasPersistedPanelLayout** — reads the library's own `react-resizable-panels:${id}` key via an
  injectable storage and survives a throwing storage (false).

### Invariants And Boundaries

Pure suite; the component-level counterparts (chip re-measure on `onLayout`, one-shot calibration,
persisted-layout skip) live in `SessionsView.test.tsx`. Test-only.

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

- The suite exercises autoCollapseTransition across crossing, quiet, and first-measure cases. [1]
- The component-level floor-chip and calibration counterparts. [2]

### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.
