# dashboard/src/data/inflight.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/inflight.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-11T15:20+02:00 |
| lastVerifiedCommitHash |  `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`|
| lastVerifiedCommitDate |  2026-08-14T14:36:50+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation is configured. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The map shares a pending promise and releases it by identity on settle. | `shareInflight` | dashboard/src/data/inflight.ts:21-30 |
| Repository and terminal catalogs use the helper for boot contention. | "export const fetchRepos = (base"; "export async function fetchTerminalSessionsOrNull(base" | dashboard/src/data/files.ts:108-111; dashboard/src/data/terminal.ts:413-430 |

## Cross-Repo References

No meaningful cross-repository references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| This is repository-local browser state coordination. | `shareInflight` | dashboard/src/data/inflight.ts:21-30 |

## Update History

- 2026-08-11T15:20+02:00 — Re-anchored both catalog consumers to their unique keyed
  `shareInflight` calls and refreshed the terminal consumer's moved range.
- 2026-08-04T18:40+02:00 — 260731-EFA-L6 S18-B18 curator: normalized the 3 citation rows to plain
  sources with `shareInflight` anchors (inflight.ts 15-30) and added the terminal catalog range
  (terminal.ts 368-387) beside files.ts 108-111 so the repository+terminal claim carries both
  consumers. Zero findings remain.

- 2026-07-24T13:17:50Z — Created for bounded boot-read single-flight ownership. Verification hash/date
  remain pinned to the pre-commit source stamp.
