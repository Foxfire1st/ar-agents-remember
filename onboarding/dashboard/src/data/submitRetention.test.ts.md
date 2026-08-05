# dashboard/src/data/submitRetention.test.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/submitRetention.test.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-18T07:22+02:00 |
| lastVerifiedCommitHash | `f8196d98982f834d68152d307ff8025ea69440d5` |
| lastVerifiedCommitDate | 2026-07-17T22:08:10+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[data overview](overview.md)

## Purpose

Proves that submit retention stays bounded while preserving every live or unresolved request.

## Code Commentary

### Logic

The suite creates mixed active and settled histories/queues, verifies both 64-row settled-tail
limits, and confirms that compaction never discards protected phases even when they exceed the
normal display window.

### Invariants And Boundaries

- A retention test failure is a correctness issue when an active row disappears, not merely a UI
  pagination issue.
- The suite tests pure projection compaction; server ledger bounds are covered separately.

## Docs References

No Domain Documentation source is configured for this repository.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live domain-documentation source was available. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The system under test defines protected phases and settled-tail bounds. | `SUBMIT_HISTORY_INSPECTOR_WINDOW`, `SUBMIT_QUEUE_RETENTION_WINDOW`, `PROTECTED_SUBMIT_PHASES`, `compactSubmitHistory`, `compactSubmitQueue` | dashboard/src/data/submitRetention.ts:8-9; dashboard/src/data/submitRetention.ts:11-20; dashboard/src/data/submitRetention.ts:27-40; dashboard/src/data/submitRetention.ts:43-45 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| This is a repository-local unit suite. | — | — |

## Update History

- 2026-08-03T02:39:28+02:00 — W3-B04 curator: curated 1 table citation (1 total), supplying exact anchors and path; the scoped fixer generated all final extents.

- 2026-07-18T07:22+02:00 — FEUI-L8 manual route refactor: retargeted this direct data file card
  from the packed dashboard/src parent to the new nearest data authority overview. Source behavior
  is unchanged by this memory-only governance move; verification hash/date remain pinned.

- 2026-07-17T21:39+02:00 — Created for 260715-FEUI-L5; captured bounded settled-tail and protected
  active-row behavior. Verification metadata remains pinned to the leaf base until closeout.
