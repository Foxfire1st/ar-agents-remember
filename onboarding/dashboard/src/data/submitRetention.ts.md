# dashboard/src/data/submitRetention.ts

## Governing Overview

[data overview](overview.md)

## Purpose

Bounds FEUI-L5 submission history and queue projections without evicting live or unresolved work.

## Code Commentary

### Logic

The compactors retain every active phase and trim only the settled tail. Both the history and queue
windows are currently 64 rows. The module is deliberately pure so the same retention decision is
used after hydration, polling, response handling, and local mutation instead of leaving unbounded
full-text request records in a long-running dashboard.

### Invariants And Boundaries

- Active, ambiguous, reconciling, queued, dispatching, and withdrawal-pending work is protected from
  count-based eviction.
- Bounds apply to settled display history, not to server authority or adapter correlation.
- Retention cannot change lifecycle truth; it only removes older settled projections.

## Evidence

### Docs References

No Domain Documentation source is configured for this repository.

No configured live domain-documentation source was available.

### Repo-Internal References

- The cockpit store invokes these compactors for per-session history and queue state. [1]
- Retention tests protect active rows and cap only settled tails. [2]

### Cross-Repo References

No meaningful cross-repo references found.

Retention is internal to the dashboard projection.
