# mcp/src/agents_remember/worktrees/task_fact_publication.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/task_fact_publication.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T14:48+02:00 |
| lastVerifiedCommitHash |  `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d`|
| lastVerifiedCommitDate |  2026-08-26T08:10:26+02:00|
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
| Publication and validation return the committed value plus per-scope effects. | `TaskFactPublicationResult`; `publish_task_fact_mutation`; `validate_task_fact_mutation` | mcp/src/agents_remember/worktrees/task_fact_publication.py:36-39; mcp/src/agents_remember/worktrees/task_fact_publication.py:42-74; mcp/src/agents_remember/worktrees/task_fact_publication.py:77-83 |
| Contract scope and task-fact adapters share the task-first owner. | `contract_projection_scopes`; `publish_contract_task_facts`; `preview_contract_task_facts` | mcp/src/agents_remember/worktrees/task_fact_publication.py:86-107; mcp/src/agents_remember/worktrees/task_fact_publication.py:110-123; mcp/src/agents_remember/worktrees/task_fact_publication.py:126-141 |
| Invalidation and rebuild failures become bounded per-scope effects. | `_invalidate_scope`; `_invalidation_failure_effect`; `_rebuild_failure_effect` | mcp/src/agents_remember/worktrees/task_fact_publication.py:158-188; mcp/src/agents_remember/worktrees/task_fact_publication.py:205-218; mcp/src/agents_remember/worktrees/task_fact_publication.py:221-243 |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

## Update History

- 2026-08-26T10:44:52+02:00 — No content impact: reviewed the closeout-projection model package relocation; task-first mutation publication and projection effects are unchanged.

- 2026-08-24T14:48+02:00 — DAGQC cumulative CLIVE final-gap curation: created the strict source-mirroring card from current code. Verification hash/date remain blank for architect-owned final stamping.