# mcp/src/agents_remember/worktrees/task_fact_publication.py

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

## Evidence

### Docs References

No configured domain-documentation source applies to this repository-internal route.

### Repo-Internal References

- Publication returns the committed value plus per-scope effects; the injected `validate` callable and scope resolution both run before the publication write, and the former `validate_task_fact_mutation` seam no longer exists. [1]
- Contract scope and task-fact adapters share the task-first owner; contract scope short-circuits when no override invalidates a projection. [2]
- Invalidation and rebuild failures become bounded per-scope effects. [3]
- The schema-owned classifier decides whether an override invalidates projections. [4]

### Cross-Repo References

No meaningful cross-repository boundary is owned by this file.
