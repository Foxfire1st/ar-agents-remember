# candidate_progression.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/candidate_progression.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-26T20:13:29Z |
| lastVerifiedCommitHash | `43b247d5bf30d4191f8fd5eb4dea9cfd72e4258d`|
| lastVerifiedCommitDate | 2026-09-27T00:14:33+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[overview.md](../overview.md)

## Purpose

Advance a draft candidate code-tree binding only from an explicitly observed predecessor while preserving its knowledge and all other admission scope.

## Code Commentary

### Logic

read_candidate_predecessor reads the exact receipt and logical dataset identity. plan_candidate_code runs the same binding checks without a lockfile or receipt write. progress_candidate_code takes the existing candidate exclusive lock, rechecks the predecessor receipt and dataset, validates the unchanged repository/lane/task/memory scope and code base, and runs the source-currentness check before the ordinary receipt writer publishes the successor.

### Conventions

Use existing capture, candidate locking, receipt and dataset identity owners. Refusals retain their explicit cause.

### Invariants And Boundaries

Normal candidate open remains strict. Only the code tree may progress; knowledge rows, allocation state and the original before half are not changed. A stale predecessor, moved dataset, foreign scope or moved source refuses without a replacement receipt.

### Todos

No additional work is asserted by this card.

## Docs References

No Domain Documentation source is configured. This account concerns the repository's own admission contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain source could be checked. | — | — |

## Repo-Internal References

These constructs bind the code capture and candidate progression to the existing authority.

| Finding | Anchor | Source |
| --- | --- | --- |
| `read_candidate_predecessor` implements the described admission boundary. | `read_candidate_predecessor` | mcp/src/agents_remember/memory/knowledge/candidate_progression.py:47-55 |
| `plan_candidate_code` implements the described admission boundary. | `plan_candidate_code` | mcp/src/agents_remember/memory/knowledge/candidate_progression.py:88-99 |
| `progress_candidate_code` implements the described admission boundary. | `progress_candidate_code` | mcp/src/agents_remember/memory/knowledge/candidate_progression.py:58-85 |
| `_validate_progression` implements the described admission boundary. | `_validate_progression` | mcp/src/agents_remember/memory/knowledge/candidate_progression.py:117-143 |
| `_same_scope` implements the described admission boundary. | `_same_scope` | mcp/src/agents_remember/memory/knowledge/candidate_progression.py:146-153 |

## Cross-Repo References

The leaf contract supplies code and memory roots; this module introduces no independent repository-selection authority.

| Finding | Anchor | Source |
| --- | --- | --- |
| No separate cross-repository authority is introduced. | — | — |

## Update History

- 2026-09-26T20:13:29Z — Created the exact-source admission boundary card.
