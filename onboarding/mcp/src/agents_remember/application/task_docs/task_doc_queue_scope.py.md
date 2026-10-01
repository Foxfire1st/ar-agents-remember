# mcp/src/agents_remember/application/task_docs/task_doc_queue_scope.py

## Governing Overview

[application/overview.md](overview.md)

## Purpose

Computes the complete old/new union of sprint projections affected by an already-accepted task
document batch, gated by the schema-owned mutation classification. This is post-publication refresh
scope only: task truth publishes independently, then each affected disposable projection is
invalidated/rebuilt.

## Code Commentary

### Logic

`TaskDocScopeChange` binds one accepted before/candidate pair to its canonical `TaskDocumentRef`
and, in `__post_init__`, derives the exact `TaskDocumentMutationClassification` through
`classify_task_document_mutation`.

`resolve_projection_scope_union()` accepts exact before/candidate pairs keyed by canonical
`TaskDocumentRef`. It rejects cross-repository or conflicting entries, constructs one candidate
override map for the whole batch, and unions every affected sprint only from changes whose
`invalidates_projection` is true: a sprint includes itself, a commanded master resolves every
canonical sprint consumer, and a leaf resolves through its parent master. A change whose classified
delta carries only acceptance-evidence or operational-audit classes contributes no scope. Sorting by
canonical key makes the refresh plan deterministic.

### Conventions

Projection scope is derived from canonical task topology plus the accepted batch overrides; callers
cannot inject an unrelated sprint identity. The mutation classifier is schema-owned; this module
never maintains a private classification table.

### Invariants And Boundaries

- A task batch may affect zero, one, or multiple sprint projections; every canonical old/new
  consumer is included.
- Only classified topology, intent, or completion-readiness changes select scopes; evidence/audit
  deltas select none.
- The accepted candidate override set is evaluated as one generation, so a multi-document edit is
  not split into contradictory intermediate topology.
- An unrelated unreadable document cannot veto the task mutation; a directly addressed invalid
  relationship still fails closed at the authoritative task boundary.
- Projection reads are never task-document CAS inputs. This module neither publishes task files nor
  grants queue/lifecycle authority.

### Todos

None recorded.

## Evidence

### Docs References

No configured Domain Documentation source applies; this is repository-internal task authority.
The governing CCR-R04@v1 packet is the task authority for the invalidation-classification
semantics here:
`ar-coordination/tasks/agents-remember/260831_closeout-certification-reform/requirements/CCR-R04-v1-mutation-classified-projection-invalidation.md`.
It is an authority link, not a resolved dependency-version source; current behavior is
evidenced by the repository-owned references below.

- R04's semantic invalidation and evidence/audit exclusion are implemented by the schema-owned classifier and deterministic scope union. [1]

### Repo-Internal References

- The public resolver classifies each change and returns a deterministic old/new sprint union. [2]
- Leaf scope is derived through the canonical parent master with the full batch override set. [3]
- The schema-owned classifier decides whether a delta invalidates projections. [4]

### Cross-Repo References

No meaningful cross-repository reference applies.

## Historical 260821-CLIVE-L2 Boundary (Superseded)

The intermediate L2 design prepared one governing queue scope before task publication. CLIVE final
removed that ownership inversion. The surviving invariant is only that projection computation uses
an accepted canonical task generation and never feeds projection state back into task CAS. The live
owner is the post-publication union described above.

## 260821-CLIVE Final Projection Blast Radius

This module no longer resolves one governing queue before task publication. It receives accepted
before/candidate document pairs and computes the complete old/new union of affected sprint
projections after the authoritative task batch publishes. Sprint changes include themselves;
master and leaf changes resolve every canonical projection consumer with the full override set.
Unrelated unreadable documents cannot veto the task write, while a directly addressed invalid
relationship still fails closed. The result is refresh scope only, never task mutation authority.

This section supersedes the earlier accepted-generation queue-lock preparation description.

## L04 Mutation-Classified Scope

Only a change whose classified delta invalidates projections (topology, intent, or
completion-readiness) enters the union. Acceptance-evidence and operational-audit edits publish
task truth with no task-driven queue refresh, matching CCR-R04@v1.
