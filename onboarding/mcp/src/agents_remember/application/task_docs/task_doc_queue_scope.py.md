# mcp/src/agents_remember/application/task_docs/task_doc_queue_scope.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/task_docs/task_doc_queue_scope.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | `3e276f2b2052b641afbee180a472259f21b500df` |
| lastVerifiedCommitDate | 2026-09-02T14:46:34+02:00|
| governingOverview | `overview.md` |

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

## Docs References

No configured Domain Documentation source applies; this is repository-internal task authority.
The governing CCR-R04@v1 packet supplies the invalidation-classification semantics the scope
union consumes.

| Finding | Anchor | Source |
| --- | --- | --- |
| R04 requires optimistic refresh only for semantic topology/intent/completion changes and zero task-driven queue refresh for evidence/audit-only edits. | "Required Behavior"; "Examples" | ar-coordination/tasks/agents-remember/260831_closeout-certification-reform/requirements/CCR-R04-v1-mutation-classified-projection-invalidation.md:25-86 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The public resolver classifies each change and returns a deterministic old/new sprint union. | `TaskDocScopeChange`; `resolve_projection_scope_union` | mcp/src/agents_remember/application/task_docs/task_doc_queue_scope.py:21-35; mcp/src/agents_remember/application/task_docs/task_doc_queue_scope.py:38-86 |
| Leaf scope is derived through the canonical parent master with the full batch override set. | `_leaf_projection_scopes` | mcp/src/agents_remember/application/task_docs/task_doc_queue_scope.py:93-121 |
| The schema-owned classifier decides whether a delta invalidates projections. | `classify_task_document_mutation`; `TaskDocumentMutationClassification.invalidates_projection` | mcp/src/agents_remember/tasks/document_field_effects.py:317-330; mcp/src/agents_remember/tasks/document_field_effects.py:86-95 |

## Cross-Repo References

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

## Update History

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for
  3e276f2b2052b641afbee180a472259f21b500df (CCR-R04@v1/L04): recorded the L04 classifier gate —
  `TaskDocScopeChange` now carries a derived `TaskDocumentMutationClassification` and
  `resolve_projection_scope_union` skips changes that do not invalidate projections.
  Verification is pinned to the owning commit.

- 2026-08-24T15:04+02:00 — Cumulative CLIVE curation: replaced pre-publication queue scope with the final post-publication before/after projection union. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.

- 2026-08-24T00:51+02:00 — 260821-CLIVE-L2: reconciled accepted-source-generation queue-scope preparation and the current-L2 versus L3 boundary. Verified at code commit `1d446724`.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: source moved to `mcp/src/agents_remember/application/task_docs/task_doc_queue_scope.py` (new package route); the citation fixer repointed in-body references; import paths updated inside the module. Verified at code commit e5cb139f.

- 2026-08-15T11:25+02:00 — Created for the L3 static-gate repair that extracted queue-scope
  resolution from the task-doc dispatcher without duplicating or changing its policy.
