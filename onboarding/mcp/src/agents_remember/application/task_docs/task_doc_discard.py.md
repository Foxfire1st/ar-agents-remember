# mcp/src/agents_remember/application/task_docs/task_doc_discard.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/task_docs/task_doc_discard.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T14:48+02:00 |
| lastVerifiedCommitHash |  `f95487ec993b58d34911bba0206a7fa6ef9684eb`|
| lastVerifiedCommitDate |  2026-08-24T15:28:18+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[governing route overview](overview.md)

## Purpose

Implement audited discard of a planning leaf proven never to have started.

## Code Commentary

### Logic

The module validates a nonblank discard request, resolves the exact parent/child binding, obtains the centralized unstarted-evidence proof, publishes a versioned parent audit, and removes the exact child JSON/Markdown bytes in one rollback-safe task transaction. Lost-response retries resume only against the recorded source digests and modes.

### Invariants And Boundaries

- Discard never marks the leaf or its steps Completed.
- Any enclosure, door, operation, worker, review, commit, progress, or unreadable execution evidence refuses the mutation.
- Changed or non-regular child bytes are preserved; replay removes only the exact audited sources.
- The ordinary task-first projection invalidation/rebuild effect follows successful publication.

### Todos

None recorded.

## Docs References

No configured domain-documentation source applies to this repository-internal route.

## Repo-Internal References

| Finding | Source Range | Source Path |
| --- | --- | --- |
| The request and candidate models bind discard input to exact source evidence. | L43-L73 | [source](mcp/src/agents_remember/application/task_docs/task_doc_discard.py) |
| The apply and resume paths publish the parent audit and exact child removals. | L74-L328 | [source](mcp/src/agents_remember/application/task_docs/task_doc_discard.py) |
| Replay removal is guarded by recorded digest, size, and regular-file mode. | L360-L409 | [source](mcp/src/agents_remember/application/task_docs/task_doc_discard.py) |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

## Update History

- 2026-08-24T14:48+02:00 — DAGQC cumulative CLIVE final-gap curation: created the strict source-mirroring card from current code. Verification hash/date remain blank for architect-owned final stamping.
