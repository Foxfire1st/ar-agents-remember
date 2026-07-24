# dashboard/src/data/taskHierarchy.test.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/taskHierarchy.test.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-24T13:17:50Z |
| lastVerifiedCommitHash |  `842b487b854503d95c9c2d9dce1841198ba93c7d`|
| lastVerifiedCommitDate |  2026-07-24T17:08:25+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[data overview](overview.md)

## Purpose

Cover normalized parent-task matching and the per-series-list identity cache used by task hierarchy
rendering.

## Code Commentary

### Logic

Fixtures exercise relative path normalization, deterministic first-series and creation-order matches,
document-id override, master/unknown exclusion, and the intentional behavior that a fresh series-list
array observes changed refs while the same array retains its cached index.

### Conventions

The tests build only the projection fields required by the pure lookup helpers.

### Invariants And Boundaries

The cache follows immutable projection-list identity; callers that mutate a list in place cannot expect
its already-built lookup index to change.

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
| Tests define normalization, precedence, and identity-cache expectations. | L28-L118 | [taskHierarchy.test.ts](taskHierarchy.test.ts) |
| The production lookup owns the WeakMap index. | L13-L56 | [taskHierarchy.ts](taskHierarchy.ts) |

## Cross-Repo References

No meaningful cross-repository references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The hierarchy helper is repository-local projection logic. | L1-L118 | [taskHierarchy.test.ts](taskHierarchy.test.ts) |

## Update History

- 2026-07-24T13:17:50Z — Created for cached parent-task lookup regression coverage. Verification
  hash/date remain pinned to the pre-commit source stamp.
