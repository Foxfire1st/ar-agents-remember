# dashboard/src/data/stream.test.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/stream.test.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-02T01:42+02:00|
| lastVerifiedCommitHash |  `842b487b854503d95c9c2d9dce1841198ba93c7d`|
| lastVerifiedCommitDate |  2026-07-24T17:08:25+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[data overview](overview.md)

## Purpose

Verify state-stream sleep/wake recovery and the open-deadline honesty boundary.

## Code Commentary

### Logic

A controlled EventSource proves that an open channel quietly cycles after a sleep-sized clock jump,
hidden tabs are exempt from watchdog cycling, ordinary transport errors still signal loss, and a replacement
that neither opens nor errors is eventually marked signal-lost and retried.

### Conventions

Fake timers model the post-wake wall-clock discontinuity.

### Invariants And Boundaries

Quiet recovery avoids unnecessary visual churn; never opening is not quiet health and cannot retain live
connection state.

### Todos

None.

## Docs References

No Domain Documentation entries are configured in this memory worktree's source registry.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation is configured. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Controlled state-stream cases cover wake, hidden, error, and never-open paths. | "connectState liveness (260723 sleep/wake)" | dashboard/src/data/stream.test.ts:36-120 |
| Production state-stream transport owns the deadline. | `connectState` | dashboard/src/data/stream.ts:30-114 |

## Cross-Repo References

No meaningful cross-repository references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| The test covers dashboard-local state transport. | "connectState liveness (260723 sleep/wake)" | dashboard/src/data/stream.test.ts:36-120 |

## Update History

- 2026-08-02T16:44:03+02:00 — W1-B07 curator: repaired 3 repository-reference citations (3/3 anchored and sourced; scoped citation check clean).

- 2026-08-02T01:42+02:00 — No content impact: re-derived line range(s) that ended past the end of the file the row names (`memory_quality/style/citations`, `citation_range_out_of_bounds`). Each range was rewritten by reading the cited construct at its current location; no claim was changed to fit a range, and no range was interpolated. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-24T13:17:50Z — Created for state-stream half-open and open-deadline regression coverage.
  Verification hash/date remain pinned to the pre-commit source stamp.
