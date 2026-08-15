# mcp/src/agents_remember/application/closeout_queue.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/closeout_queue.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-15T09:10+02:00 |
| lastVerifiedCommitHash | `17987fa66a642306eb8d20fa9a4bff2b881550d2` |
| lastVerifiedCommitDate | 2026-08-15T14:36:30+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[application overview](overview.md)

## Purpose

This module is the ambient-authorized application boundary for the sprint closeout queue. It turns
the hosted caller's canonical seat and task-document binding into the structural `QueueActor` used
by the queue service; actor identity is never accepted from public request data.

## Code Commentary

### Logic

`closeout_queue_tool` resolves the ambient seat from the terminal catalog, refuses an unbound seat,
and delegates the validated request with the resolved role and task-document reference.

### Conventions

The application layer owns ambient identity resolution; scheduling mechanics stay in
`worktrees/closeout_queue.py`.

### Invariants And Boundaries

- Public callers cannot self-assert a role or task identity.
- Ambient-seat failures retain their typed status through `CloseoutQueueError`.
- This module does not mutate task documents or Git refs directly.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies; this is an internal authority boundary.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Ambient seat resolution precedes construction of the structural queue actor. | `closeout_queue_tool` | mcp/src/agents_remember/application/closeout_queue.py:18-38 |

## Cross-Repo References

No meaningful cross-repository reference applies.

## Update History

- 2026-08-15T09:10+02:00 — Created for L3's ambient-authorized closeout-queue application boundary; verification remains pinned to the leaf base until closeout stamps the candidate commit.
