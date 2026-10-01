# dashboard/src/panels/session-cockpit/SetOutcomeToasts.test.tsx

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

Regression contract for background set-outcome persistence, acknowledgment, and collapse.

## Code Commentary

### Logic

Proves that no toast appears without attention or for the focused seat, that focus and `mark seen`
are separate actions, that only mark seen acknowledges the ledger, and that several affected
sessions share one stack.

### Conventions

The real cockpit store supplies attention state while callbacks make focus intent observable.

### Invariants And Boundaries

Changing focus does not silently acknowledge an outcome, and dismissal is an explicit mark-seen
operation.

### Todos

None recorded.

## Evidence

### Docs References

No Domain Documentation source is configured.

No external domain citation applies.

### Repo-Internal References

- Visibility, persistence, mark-seen, focus, and collapse cases. [1]
- Component under test. [2]

### Cross-Repo References

No meaningful cross-repo boundary is owned here.

No cross-repo evidence applies.
