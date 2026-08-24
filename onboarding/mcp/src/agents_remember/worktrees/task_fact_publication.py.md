# mcp/src/agents_remember/worktrees/task_fact_publication.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/task_fact_publication.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T14:48+02:00 |
| lastVerifiedCommitHash |  `f95487ec993b58d34911bba0206a7fa6ef9684eb`|
| lastVerifiedCommitDate |  2026-08-24T15:28:18+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[governing route overview](../../../overview.md)

## Purpose

Provide the one task-first publication boundary shared by task-truth writers.

## Code Commentary

### Logic

The service validates and publishes authoritative task bytes under the short task-publication lock, derives the before/after sprint-scope union, invalidates every affected projection to invalid-empty, and rebuilds each scope independently from current task and waiting-door sources.

### Invariants And Boundaries

- Task truth publishes before projection effects and is never rolled back for a queue failure.
- Queue rows are disposable output and are never rebuild input.
- Every affected scope receives a typed effect and executable rebuild action.
- Contract-owned task publication uses the same service; there is no compatibility wrapper.

### Todos

None recorded.

## Docs References

No configured domain-documentation source applies to this repository-internal route.

## Repo-Internal References

| Finding | Source Range | Source Path |
| --- | --- | --- |
| Publication and validation return the committed value plus per-scope effects. | L37-L85 | [source](mcp/src/agents_remember/worktrees/task_fact_publication.py) |
| Contract scope and task-fact adapters share the task-first owner. | L86-L157 | [source](mcp/src/agents_remember/worktrees/task_fact_publication.py) |
| Invalidation and rebuild failures become bounded per-scope effects. | L158-L243 | [source](mcp/src/agents_remember/worktrees/task_fact_publication.py) |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

## Update History

- 2026-08-24T14:48+02:00 — DAGQC cumulative CLIVE final-gap curation: created the strict source-mirroring card from current code. Verification hash/date remain blank for architect-owned final stamping.
