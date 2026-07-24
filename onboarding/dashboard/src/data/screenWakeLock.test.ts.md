# dashboard/src/data/screenWakeLock.test.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/screenWakeLock.test.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-24T13:17:50Z |
| lastVerifiedCommitHash |  `842b487b854503d95c9c2d9dce1841198ba93c7d`|
| lastVerifiedCommitDate |  2026-07-24T17:08:25+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[data overview](overview.md)

## Purpose

Verify visible-tab wake-lock acquisition, release, reacquisition, graceful API absence, and overlapping
request coalescing.

## Code Commentary

### Logic

Fake documents, navigators, and sentinels expose visibility events and deferred `request` resolution.
The overlap case proves only one held sentinel exists and that `stop()` releases every issued sentinel.

### Conventions

The suite injects the DOM and Navigator dependencies rather than mutating browser globals.

### Invariants And Boundaries

No test treats unsupported or denied wake lock as an application failure.

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
| Deferred sentinel tests cover acquisition coalescing and release. | L64-L179 | [screenWakeLock.test.ts](screenWakeLock.test.ts) |
| The production owner holds one sentinel at a time. | L34-L94 | [screenWakeLock.ts](screenWakeLock.ts) |

## Cross-Repo References

No meaningful cross-repository references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| This is local browser-API test coverage. | L1-L179 | [screenWakeLock.test.ts](screenWakeLock.test.ts) |

## Update History

- 2026-07-24T13:17:50Z — Created for wake-lock lifecycle and overlap regression coverage.
  Verification hash/date remain pinned to the pre-commit source stamp.
