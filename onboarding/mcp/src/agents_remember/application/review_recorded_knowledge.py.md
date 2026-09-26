# review_recorded_knowledge.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/review_recorded_knowledge.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-26T19:49:05Z |
| lastVerifiedCommitHash | `43b247d5bf30d4191f8fd5eb4dea9cfd72e4258d`|
| lastVerifiedCommitDate | 2026-09-27T00:14:33+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[overview.md](overview.md)

## Purpose

Read a closed leaf knowledge state from its exact recorded memory commit endpoints when no frozen review generation exists.

## Code Commentary

### Logic

read_recorded_knowledge delegates endpoint selection to recorded_committed_range. read_memory_knowledge reads only the knowledge.sqlite Git blob at each endpoint, checks that it is a regular file, and asks the dataset identity owner to read it. Each side retains available, not-recorded, missing or corrupt state. Mismatched repository namespaces make the after side corrupt. The RecordedKnowledge instance holds temporary read files until the composed resolution is released, then its finalizer cleans them.

### Conventions

Use the existing owner interfaces and exact recorded identities; keep transient task evidence outside durable onboarding.

### Invariants And Boundaries

No current worktree, branch tip or sibling generation supplies a missing operand. Temporary paths never enter comparison or cursor identity. The result is explicitly reconstructed history, not a new retained comparison generation or knowledge publication.

### Todos

No additional work is asserted by this card.

## Docs References

No Domain Documentation source is configured. The implementation-specific account is grounded in the repository source below.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain source could be checked. | — | — |

## Repo-Internal References

The named constructs own this behavior; reads and validation use their existing callers and models.

| Finding | Anchor | Source |
| --- | --- | --- |
| `RecordedKnowledge` owns the behavior described above. | `RecordedKnowledge` | mcp/src/agents_remember/application/review_recorded_knowledge.py:28-49 |
| `read_recorded_knowledge` owns the behavior described above. | `read_recorded_knowledge` | mcp/src/agents_remember/application/review_recorded_knowledge.py:52-82 |
| `read_memory_knowledge` owns the behavior described above. | `read_memory_knowledge` | mcp/src/agents_remember/application/review_recorded_knowledge.py:85-131 |

## Cross-Repo References

No independent cross-repository interface is introduced by this source.

| Finding | Anchor | Source |
| --- | --- | --- |
| No additional cross-repository evidence is required. | — | — |

## Update History

- 2026-09-26T19:49:05Z — Created the exact historical knowledge-operand reader card.
