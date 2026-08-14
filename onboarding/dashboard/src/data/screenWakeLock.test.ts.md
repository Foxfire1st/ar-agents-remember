# dashboard/src/data/screenWakeLock.test.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/screenWakeLock.test.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-24T13:17:50Z |
| lastVerifiedCommitHash |  `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`|
| lastVerifiedCommitDate |  2026-08-14T14:36:50+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation is configured. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Deferred sentinel tests cover acquisition coalescing and release. | "acquires while visible and releases on stop" | dashboard/src/data/screenWakeLock.test.ts:108-116 |
| The production owner holds one sentinel at a time. | "export function startScreenWakeLock" | dashboard/src/data/screenWakeLock.ts:34-34 |

## Cross-Repo References

No meaningful cross-repository references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| This is local browser-API test coverage. | "reacquires after a UA-initiated release while still visible" | dashboard/src/data/screenWakeLock.test.ts:118-126 |

## Update History

- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B23 curator: replaced the `n/a` rows with exact
  anchors and fixer-generated ranges; exact non-fixing check returns zero findings.

- 2026-07-24T13:17:50Z — Created for wake-lock lifecycle and overlap regression coverage.
  Verification hash/date remain pinned to the pre-commit source stamp.
