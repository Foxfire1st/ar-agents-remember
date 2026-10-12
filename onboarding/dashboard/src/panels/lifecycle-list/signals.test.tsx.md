# dashboard/src/panels/lifecycle-list/signals.test.tsx

## Governing Overview

[panels/ overview](../overview.md)

## Purpose

The independent Operations-signals suite split from `LifecycleList.test.tsx` by the
260731-EFA-L8 test split. Pins the independent signal rendering on rows
(state marks, attention, gate hints) without coupling to the detail panel.

## Code Commentary

### Logic

Seeds rows with varied lifecycle states and asserts the per-row signal marks
(including the `awaiting-developer` live-state mark rule).

### Invariants And Boundaries

Signal meaning remains independent of task progress and detail selection. Current assertions locate one priority word and full row hover; inbox dismissal must still be reachable beside a gate, name its inbox target and not select the row. Qualified chat identity and lifecycle/document state remain distinct.

### Todos

None recorded.

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

No relevant domain documentation was found.

### Repo-Internal References

- The Operations-signals suite. [1]

### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.
