# dashboard/src/panels/session-cockpit/sessions-view/stopResiduals.test.tsx

## Governing Overview

[panels/session-cockpit overview](../overview.md)

## Purpose

The stop-residual suite split from `SessionsView.test.tsx` by the 260731-EFA-L8 test
split. Pins the L6 stage InteractionBar and stop-residual behavior (informational
stop residuals outlive tombstoned rows).

## Code Commentary

### Logic

Seeds terminal sessions and covers two independent boundaries: a focused lifecycle-free pending
answer posts once to the exact session interaction-response route without using `/submit`, while a
stopped seat retains its informational residual after the row is tombstoned.

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

- The focused composer proves lifecycle-free exact-session routing and duplicate-send locking. [1]
- The stop-residual suite. [2]

### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.
