# dashboard/src/data/stream.test.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/stream.test.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-24T13:17:50Z |
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

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation is configured. | Source discovery checked | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Controlled state-stream cases cover wake, hidden, error, and never-open paths. | L6-L120 | [stream.test.ts](stream.test.ts) |
| Production state-stream transport owns the deadline. | L1-L240 | [stream.ts](stream.ts) |

## Cross-Repo References

No meaningful cross-repository references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The test covers dashboard-local state transport. | L1-L120 | [stream.test.ts](stream.test.ts) |

## Update History

- 2026-07-24T13:17:50Z — Created for state-stream half-open and open-deadline regression coverage.
  Verification hash/date remain pinned to the pre-commit source stamp.
