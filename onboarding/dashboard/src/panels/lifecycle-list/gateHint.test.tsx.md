# dashboard/src/panels/lifecycle-list/gateHint.test.tsx

## Governing Overview

[panels/ overview](../overview.md)

## Purpose

The gate-hint suite split from `LifecycleList.test.tsx` by the 260731-EFA-L8 test
split. Pins the L17 rule: a gate hint is informational and offers no bare-ask
affordance.

## Code Commentary

### Logic

Seeds a gated lifecycle row and asserts the hint renders without an unauthorized
ask/respond affordance.

### Invariants And Boundaries

Assertions preserved from the monolithic suite.

### Todos

None recorded.

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

No relevant domain documentation was found.

### Repo-Internal References

- The gate-hint suite. [1]

### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.
