# dashboard/src/data/submitRetention.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/submitRetention.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-18T07:22+02:00 |
| lastVerifiedCommitHash | `f8196d98982f834d68152d307ff8025ea69440d5` |
| lastVerifiedCommitDate | 2026-07-17T22:08:10+02:00|
| governingOverview | `overview.md` |

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

## Docs References

No Domain Documentation source is configured for this repository.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live domain-documentation source was available. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The cockpit store invokes these compactors for per-session history and queue state. | `enqueueSubmit`, `upsertSubmitRecord` | dashboard/src/data/sessionCockpitStore.ts:254-254; dashboard/src/data/sessionCockpitStore.ts:256-256 |
| Retention tests protect active rows and cap only settled tails. | "reliable-submit retention policy (F4)" | dashboard/src/data/submitRetention.test.ts:25-78 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| Retention is internal to the dashboard projection. | — | — |

## Update History

- 2026-08-02T20:47+02:00 — 260731-EFA-L6 W2-B01 curator: anchored 2 citation rows; scoped citation fixing regenerated the source ranges.

- 2026-07-18T07:22+02:00 — FEUI-L8 manual route refactor: retargeted this direct data file card
  from the packed dashboard/src parent to the new nearest data authority overview. Source behavior
  is unchanged by this memory-only governance move; verification hash/date remain pinned.

- 2026-07-17T21:39+02:00 — Created for 260715-FEUI-L5; recorded the 64-row settled-history and
  queue bounds and the non-eviction boundary for live/unresolved submissions. Verification metadata
  remains pinned to the leaf base until closeout.
