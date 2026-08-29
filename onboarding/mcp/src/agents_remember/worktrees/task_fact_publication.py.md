# mcp/src/agents_remember/worktrees/task_fact_publication.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/task_fact_publication.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-29T17:23+02:00 |
| lastVerifiedCommitHash |  `60e429d17e9fcbca3ab1c02563afcaa5761b8c5a`|
| lastVerifiedCommitDate |  2026-08-29T20:33:10+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| Publication and validation return the committed value plus per-scope effects. | `TaskFactPublicationResult`; `publish_task_fact_mutation`; `validate_task_fact_mutation` | mcp/src/agents_remember/worktrees/task_fact_publication.py:33-36; mcp/src/agents_remember/worktrees/task_fact_publication.py:39-71; mcp/src/agents_remember/worktrees/task_fact_publication.py:74-80 |
| Contract scope and task-fact adapters share the task-first owner. | `contract_projection_scopes`; `publish_contract_task_facts`; `preview_contract_task_facts` | mcp/src/agents_remember/worktrees/task_fact_publication.py:83-104; mcp/src/agents_remember/worktrees/task_fact_publication.py:107-120; mcp/src/agents_remember/worktrees/task_fact_publication.py:123-138 |
| Invalidation and rebuild failures become bounded per-scope effects. | `_invalidate_scope`; `_invalidation_failure_effect`; `_rebuild_failure_effect` | mcp/src/agents_remember/worktrees/task_fact_publication.py:155-185; mcp/src/agents_remember/worktrees/task_fact_publication.py:202-215; mcp/src/agents_remember/worktrees/task_fact_publication.py:218-240 |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

## Update History

- 2026-08-29T17:23+02:00 — No content impact: reviewed the Python 3.13 generic-class and local type-parameter migration and confirmed that authoritative task publication plus disposable projection effects remain as documented. Verification remains closeout-owned.

- 2026-08-26T10:44:52+02:00 — No content impact: reviewed the closeout-projection model package relocation; task-first mutation publication and projection effects are unchanged.

- 2026-08-24T14:48+02:00 — DAGQC cumulative CLIVE final-gap curation: created the strict source-mirroring card from current code. Verification hash/date remain blank for architect-owned final stamping.
