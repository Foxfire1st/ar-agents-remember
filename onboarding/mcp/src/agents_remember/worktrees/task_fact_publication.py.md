# mcp/src/agents_remember/worktrees/task_fact_publication.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/task_fact_publication.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash |  `3e276f2b2052b641afbee180a472259f21b500df`|
| lastVerifiedCommitDate |  2026-09-02T14:46:34+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[governing route overview](../../../overview.md)

## Purpose

Provide the one task-first publication boundary shared by task-truth writers, now including the
mutation-classified scope gate: a task batch that changes no semantically invalidating field
publishes truth without touching any disposable projection.

## Code Commentary

### Logic

The service validates and publishes authoritative task bytes under the short task-publication lock, derives the before/after sprint-scope union, invalidates every affected projection to invalid-empty, and rebuilds each scope independently from current task and waiting-door sources.

L04 reordered the transaction: scope resolution now happens before publication inside the lock
(validate, resolve scopes, then write), so an unclassified or scope-refusing delta can refuse
before any task bytes are written. `contract_projection_scopes` additionally early-returns an
empty tuple when `classify_task_document_mutation` reports no override invalidates a projection,
so lifecycle-owned contract writes that only restamp lifecycle/audit fields cause zero queue churn.

### Invariants And Boundaries

- Task truth publishes before projection effects and is never rolled back for a queue failure.
- Queue rows are disposable output and are never rebuild input.
- Every affected scope receives a typed effect and executable rebuild action.
- Contract-owned task publication uses the same service; there is no compatibility wrapper.
- Scope resolution precedes publication; a scope refusal prevents task truth from being written.
- A change classified as evidence/audit-only selects no projection scope.

### Todos

None recorded.

## Docs References

No configured domain-documentation source applies to this repository-internal route.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Publication and validation return the committed value plus per-scope effects; scope resolution precedes publication. | `TaskFactPublicationResult`; `publish_task_fact_mutation`; `validate_task_fact_mutation` | mcp/src/agents_remember/worktrees/task_fact_publication.py:34-37; mcp/src/agents_remember/worktrees/task_fact_publication.py:40-72; mcp/src/agents_remember/worktrees/task_fact_publication.py:75-81 |
| Contract scope and task-fact adapters share the task-first owner; contract scope short-circuits when no override invalidates a projection. | `contract_projection_scopes`; `publish_contract_task_facts`; `preview_contract_task_facts` | mcp/src/agents_remember/worktrees/task_fact_publication.py:84-113; mcp/src/agents_remember/worktrees/task_fact_publication.py:116-129; mcp/src/agents_remember/worktrees/task_fact_publication.py:132-147 |
| Invalidation and rebuild failures become bounded per-scope effects. | `_invalidate_scope`; `_invalidation_failure_effect`; `_rebuild_failure_effect` | mcp/src/agents_remember/worktrees/task_fact_publication.py:164-194; mcp/src/agents_remember/worktrees/task_fact_publication.py:211-224; mcp/src/agents_remember/worktrees/task_fact_publication.py:227-248 |
| The schema-owned classifier decides whether an override invalidates projections. | `classify_task_document_mutation` | mcp/src/agents_remember/tasks/document_field_effects.py:317-330 |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

## Update History

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for
  3e276f2b2052b641afbee180a472259f21b500df (CCR-R04@v1/L04): recorded the L04 transaction
  reorder (scope resolution precedes publication) and the mutation-class short-circuit in
  `contract_projection_scopes`. Verification is pinned to the owning commit.

- 2026-08-29T17:23+02:00 — No content impact: reviewed the Python 3.13 generic-class and local type-parameter migration and confirmed that authoritative task publication plus disposable projection effects remain as documented. Verification remains closeout-owned.

- 2026-08-26T10:44:52+02:00 — No content impact: reviewed the closeout-projection model package relocation; task-first mutation publication and projection effects are unchanged.

- 2026-08-24T14:48+02:00 — DAGQC cumulative CLIVE final-gap curation: created the strict source-mirroring card from current code. Verification hash/date remain blank for architect-owned final stamping.
