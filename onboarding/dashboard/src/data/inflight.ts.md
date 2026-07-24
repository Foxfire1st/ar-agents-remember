# dashboard/src/data/inflight.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/inflight.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-24T13:17:50Z |
| lastVerifiedCommitHash |  `842b487b854503d95c9c2d9dce1841198ba93c7d`|
| lastVerifiedCommitDate |  2026-07-24T17:08:25+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[data overview](overview.md)

## Purpose

Provide per-key single-flight ownership for idempotent dashboard boot reads without becoming a cache.

## Code Commentary

### Logic

Concurrent callers receive the first pending promise for a key. The promise's identity-guarded `finally`
removes only its own slot after success or rejection, allowing later reads to issue a fresh request.

### Conventions

Callers supply the async read and are responsible for an abort-capable transport bound.

### Invariants And Boundaries

Sharing a promise shares both result and rejection. This module has no timeout and no value cache; adding
one would blur its ownership with a caller's cache policy.

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
| The map shares a pending promise and releases it by identity on settle. | L15-L30 | [inflight.ts](inflight.ts) |
| Repository and terminal catalogs use the helper for boot contention. | L94-L108 | [files.ts](files.ts) |

## Cross-Repo References

No meaningful cross-repository references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| This is repository-local browser state coordination. | L1-L30 | [inflight.ts](inflight.ts) |

## Update History

- 2026-07-24T13:17:50Z — Created for bounded boot-read single-flight ownership. Verification hash/date
  remain pinned to the pre-commit source stamp.
