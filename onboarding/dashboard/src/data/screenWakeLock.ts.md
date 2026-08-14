# dashboard/src/data/screenWakeLock.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/screenWakeLock.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-24T13:17:50Z |
| lastVerifiedCommitHash |  `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`|
| lastVerifiedCommitDate |  2026-08-14T14:36:50+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation is configured. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Visibility, release, and overlapping-acquire handling. | `startScreenWakeLock` | dashboard/src/data/screenWakeLock.ts:34-94 |
| Cockpit startup owns the returned lifecycle. | "} from \"react\";"; "import { startScreenWakeLock } from " | dashboard/src/cockpit/Cockpit.tsx:20-20; dashboard/src/cockpit/Cockpit.tsx:9-9 |

## Cross-Repo References

No meaningful cross-repository references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| The optional browser API is wrapped locally. | `wakeLockOf` | dashboard/src/data/screenWakeLock.ts:25-28 |

## Update History

- 2026-08-04T17:52+02:00 — 260731-EFA-L6 S18-B15 curator: resolved 6 citation findings. Re-anchored and
  re-ranged the three reference rows: `startScreenWakeLock` for visibility/release handling, its
  `Cockpit.tsx:393` mount, and `wakeLockOf` for the local wrapper of the optional API. Scoped recheck
  clean.

- 2026-07-24T13:17:50Z — Created for visible-tab screen wake-lock ownership. Verification hash/date
  remain pinned to the pre-commit source stamp.
