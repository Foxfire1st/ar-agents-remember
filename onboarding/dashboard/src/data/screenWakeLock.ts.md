# dashboard/src/data/screenWakeLock.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/screenWakeLock.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-24T13:17:50Z |
| lastVerifiedCommitHash |  `842b487b854503d95c9c2d9dce1841198ba93c7d`|
| lastVerifiedCommitDate |  2026-07-24T17:08:25+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[data overview](overview.md)

## Purpose

Keep the monitoring cockpit's screen awake while its document is visible, without pinning a backgrounded
tab or creating an operator alarm for an unavailable platform API.

## Code Commentary

### Logic

`startScreenWakeLock` requests a screen sentinel when visible, reacquires after a UA release or visible
return, and returns a stop function that removes the listener and releases its owned sentinel.

### Conventions

The narrow local `WakeLockLike` shapes avoid making optional platform APIs global dashboard state.

### Invariants And Boundaries

The `acquiring` guard coalesces overlapping requests so only one sentinel is owned. Unsupported or denied
APIs log one informational note and remain a no-op; the feature never implies that a wake lock is held.

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
| Visibility, release, and overlapping-acquire handling. | L30-L94 | [screenWakeLock.ts](screenWakeLock.ts) |
| Cockpit startup owns the returned lifecycle. | L1-L760 | [../cockpit/Cockpit.tsx](../cockpit/Cockpit.tsx) |

## Cross-Repo References

No meaningful cross-repository references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The optional browser API is wrapped locally. | L15-L94 | [screenWakeLock.ts](screenWakeLock.ts) |

## Update History

- 2026-07-24T13:17:50Z — Created for visible-tab screen wake-lock ownership. Verification hash/date
  remain pinned to the pre-commit source stamp.
