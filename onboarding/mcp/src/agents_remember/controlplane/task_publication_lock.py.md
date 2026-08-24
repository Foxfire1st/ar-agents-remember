# mcp/src/agents_remember/controlplane/task_publication_lock.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/controlplane/task_publication_lock.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T14:43+02:00 |
| lastVerifiedCommitHash | `f95487ec993b58d34911bba0206a7fa6ef9684eb`|
| lastVerifiedCommitDate | 2026-08-24T15:28:18+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Control-plane overview](overview.md)

## Purpose

Provides the short repository-scoped mutex used to publish exact task-document and closeout-door
bytes without a lost update. It is a compare-and-swap serialization seam, not a task, queue, lane,
or lifecycle lock.

## Code Commentary

The lock path is derived from the repository identity under the coordination root. `create=False`
supports a non-writing preview, while the mutation path takes the filesystem lock only around the
bounded reread-and-publication transaction. Callers must still re-read canonical authority while
holding it; possession of this mutex never supplies semantic authority.

## Invariants And Boundaries

- The critical section is short and repository-scoped; worker execution and review never run under it.
- Task authoring is never subordinate to queue state.
- The lock stores no lifecycle, scheduling, or commit evidence.
- There is no shadow lock, compatibility route, or unlocked fallback.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Repository-scoped lock construction and acquisition live in this module. | `task_publication_lock` | `mcp/src/agents_remember/controlplane/task_publication_lock.py` |

## Update History

- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: created the exact 1:1 card from the final code snapshot. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.
