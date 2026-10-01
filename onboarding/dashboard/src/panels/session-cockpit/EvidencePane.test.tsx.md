# dashboard/src/panels/session-cockpit/EvidencePane.test.tsx

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

Pins the Evidence pane's proof completeness, missing-evidence honesty, both lifecycle stop-residual
classes, and exact dismissal behavior before and after a seat leaves the catalog.

## Code Commentary

### Logic

- Covers launch, set receipt, submit receipt/reconciliation, bridge error, pane, liveness, and
  explicit mark-seen rendering.
- Proves absent receipt fields remain absent rather than being inferred.
- Covers terminate and retire residuals, exact `(sessionId, at)` dismissal, no-focus visibility,
  and a successful terminate residual revealed after the terminated seat disappears.

### Invariants And Boundaries

- Both stop classes are informational and share the same authoritative notice store.
- Catalog removal must not erase the latest confirmed control-stop detail.

### Todos

None recorded.

## Evidence

### Docs References

No Domain Documentation source is configured.

No external domain citation applies.

### Repo-Internal References

- Focused-seat case covers launch, receipt/reconciliation, bridge, pane, retire-stop residual, and liveness evidence. [1]
- Missing-receipt honesty case. [2]
- Terminate and retire residuals remain inspectable without focus and share dismissal across surfaces. [3]
- A successful terminate residual remains visible after the terminated seat is removed. [4]
- Component under test. [5]

### Cross-Repo References

No meaningful cross-repo boundary is owned here.

No cross-repo evidence applies.

## FEUI-L8 Reviewed Candidate Delta

Updates lifecycle notice fixtures for the new `cleanupFailure` state so evidence tests exercise the complete notice-store shape.

The reviewed candidate is still uncommitted. Existing verification hash/date remain pinned to the
leaf base; closeout owns commit stamping.
