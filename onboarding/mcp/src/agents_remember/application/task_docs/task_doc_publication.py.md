# mcp/src/agents_remember/application/task_docs/task_doc_publication.py

## Governing Overview

[governing route overview](overview.md)

## Purpose

Own exact task-document source-CAS and task-first publication. One mutation publishes canonical
task bytes and invalidates the complete affected sprint-projection union under the task-publication
lock, then rebuilds each disposable projection independently.

## Code Commentary

### Logic

`TaskDocPublication` carries the original/candidate documents, complete accepted JSON/Markdown
source snapshots, and optional publisher. `task_doc_publication_transaction` first invokes the
central zero/one graph-document assertion, derives exact before/after projection scope changes, and
builds a `TaskDocPublicationTransaction`. `publish_task_doc_transaction_and_refresh` delegates that
transaction to `publish_task_fact_mutation`: accepted bytes are rechecked, task truth is written,
and every affected projection scope is invalidated under one task-publication lock; each invalidated
projection then rebuilds independently. Dry-run validates the same source pair and previews the
same projection effects without writing. A mismatch raises `TaskDocPublicationConflict` with
bounded expected/observed evidence.

L04 narrowed the dry-run preflight: `validate_task_doc_transaction` now collects source-currentness
and scope-union resolution into one closure so the read-only path exercises the identical exact
source-pair transaction as protected publication, including the mutation-classified scope selection
performed by `resolve_projection_scope_union` over `TaskDocScopeChange` entries.

Ordinary disk-backed graph-title reads deliberately remain inside the publisher callback, after
the task lock is held, so the title snapshot used for rendering is read under the same
serialization boundary as the document write.
Only pure submitted-batch graph cardinality is checked earlier.

`publish_prepared_task_documents` is the public application seam for callers that have already
captured candidate documents and exact source snapshots. It routes those bytes through the same
transaction, rather than making registration and other prepared-document callers reconstruct
scope-union or publisher behavior. This keeps accepted-source CAS, task-first publication,
invalidation, and rebuild behind one API.

### Conventions

Callers prepare all selected/affected source snapshots before entering the transaction and must not
re-read a weaker subset inside their own publisher. Pure validation may precede locking; disk state
that participates in a read-modify-write invariant is read only inside the publisher callback.

### Invariants And Boundaries

- Exact JSON and Markdown bytes for every selected/affected document are one CAS precondition.
- Task truth is authoritative. Queue/projection state is disposable: task publication invalidates
  the full affected scope and projection rebuild happens after the lock, per scope.
- A publication batch has at most one graph-bearing document. Unsupported cardinality refuses
  before transaction construction; there is no first-document selection or split retry.
- Existing on-disk title reads stay inside the protected publisher callback to avoid rendering
  from a stale pre-lock title snapshot.
- Dry-run preflight runs the same source-pair validation and classifier-scoped union as the real
  transaction; it never writes task or projection bytes.

### Todos

None recorded.

## Evidence

### Docs References

No configured Domain Documentation source applies to this repository-internal lifecycle seam.

### Repo-Internal References

The source file itself is the current evidence for this file-specific contract.

- The module defines the exact task publication request, transaction, and result models. [1]
- Publication delegates exact validation, task write, affected-scope invalidation, and independent rebuild to the task-first owner. [2]
- Graph cardinality is checked before transaction construction while disk title reads remain inside the publisher callback. [3]
- Scope changes bind each candidate to its exact accepted original bytes. [4]
- Dry-run preflight validates source currentness and the classifier-scoped union through the same closure as publication. [5]
- Focused proof refuses two graph documents before publisher/projection mutation and preserves sentinel bytes. [6]

### Cross-Repo References

No meaningful cross-repository boundary is owned by this file.
