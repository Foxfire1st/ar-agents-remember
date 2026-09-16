# mcp/src/agents_remember/worktrees/task_fact_publication.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/task_fact_publication.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash |  `3b552f5a215648274dc5e6e4d5f0a01c2ee80be2`|
| lastVerifiedCommitDate |  2026-09-12T01:54:48+02:00|
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
| Publication returns the committed value plus per-scope effects; the injected `validate` callable and scope resolution both run before the publication write, and the former `validate_task_fact_mutation` seam no longer exists. | `TaskFactPublicationResult`; `publish_task_fact_mutation` | mcp/src/agents_remember/worktrees/task_fact_publication.py:33-36; mcp/src/agents_remember/worktrees/task_fact_publication.py:39-69 |
| Contract scope and task-fact adapters share the task-first owner; contract scope short-circuits when no override invalidates a projection. | `contract_projection_scopes`; `publish_contract_task_facts`; `preview_contract_task_facts` | mcp/src/agents_remember/worktrees/task_fact_publication.py:104-116; mcp/src/agents_remember/worktrees/task_fact_publication.py:119-134; mcp/src/agents_remember/worktrees/task_fact_publication.py:72-101 |
| Invalidation and rebuild failures become bounded per-scope effects. | `_invalidate_scope`; `_invalidation_failure_effect`; `_rebuild_failure_effect` | mcp/src/agents_remember/worktrees/task_fact_publication.py:151-181; mcp/src/agents_remember/worktrees/task_fact_publication.py:198-211; mcp/src/agents_remember/worktrees/task_fact_publication.py:214-236 |
| The schema-owned classifier decides whether an override invalidates projections. | `classify_task_document_mutation` | mcp/src/agents_remember/tasks/document_field_effects.py:345-358 |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

## Update History
- 2026-09-11T23:05:00+00:00: Repaired one claim. It named a `validate_task_fact_mutation` seam and cited lines 34-37/40-72/75-81; that function exists nowhere in the tree, validation is now the caller-supplied `validate` callable invoked inside `publish_task_fact_mutation`, and the claim now names `TaskFactPublicationResult` (class at 33-36) and `publish_task_fact_mutation` (def at 39-69) at their exact current extents.
- 2026-09-11T23:05:00+00:00: Curator citation reconciliation: `_invalidate_scope`, `_invalidation_failure_effect`, `_rebuild_failure_effect` repointed to mcp/src/agents_remember/worktrees/task_fact_publication.py:151-181, mcp/src/agents_remember/worktrees/task_fact_publication.py:198-211, mcp/src/agents_remember/worktrees/task_fact_publication.py:214-236. No content impact: mechanical anchor-range projection against citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged.
- 2026-09-09T12:22:46+00:00: Generated citation repair: `classify_task_document_mutation` repointed to mcp/src/agents_remember/tasks/document_field_effects.py:345-358. No content impact: mechanical anchor-range projection bound to citation source snapshot 06f99a0e57ce8b514dd7ed6685874da5285e3ec2e8c4a3f6a5d768b622094451; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for
  3e276f2b2052b641afbee180a472259f21b500df (CCR-R04@v1/L04): recorded the L04 transaction
  reorder (scope resolution precedes publication) and the mutation-class short-circuit in
  `contract_projection_scopes`. Verification is pinned to the owning commit.

- 2026-08-29T17:23+02:00 — No content impact: reviewed the Python 3.13 generic-class and local type-parameter migration and confirmed that authoritative task publication plus disposable projection effects remain as documented. Verification remains closeout-owned.

- 2026-08-26T10:44:52+02:00 — No content impact: reviewed the closeout-projection model package relocation; task-first mutation publication and projection effects are unchanged.

- 2026-08-24T14:48+02:00 — DAGQC cumulative CLIVE final-gap curation: created the strict source-mirroring card from current code. Verification hash/date remain blank for architect-owned final stamping.
