# mcp/src/agents_remember/application/task_docs/task_doc_publication.py

## Governing Overview

[governing route overview](overview.md)

## Purpose

Own exact task-document source-CAS, task-first publication and the repository task-root file-lock boundary. Task-document preparation and central publication share that one re-entrant file lock; a call-scoped marker refuses a publication nested inside an active publication. Disposable projection invalidation and per-scope rebuild do not replace this source/copy rollback boundary.

## Code Commentary

### Logic

`TaskDocPublication` carries original/candidate documents, exact JSON/Markdown source snapshots and an optional publisher. The transaction builder checks zero-or-one graph cardinality and derives the complete before/after projection-scope union. `run_task_doc_call` takes `kernel.file_lock.exclusive_file_lock` on `coordination_root/tasks/<repository>` before the task-doc dispatcher reads the authoritative edit source or prepares its candidate. `lock_path_for` names the sibling `<repository>.lock`; the central `publish_task_doc_transaction_and_refresh` re-enters that same lock, with no second task-root lock/order.

The central wrapper sets the call-scoped `_publication_active` marker and resets its token in `finally`. A nested task-doc entry answers `task-document-publication-in-progress` before its callback runs; a direct nested central call raises the named `TaskDocError` before its publisher runs. Re-entrant locking therefore does not admit a second successful publication inside the active interval.

Under that lock the private central body delegates exact CAS, task publication, copy refresh and projection work to their existing owners. A copy-refresh exception restores the pre-batch source snapshots before the lock is released; rollback failure is named and chained, not hidden. Another thread/process waits, then its task-doc call reads and prepares after rollback so its keyed question stands. The top-level independently prepared topology/retirement/linkage callers keep exact CAS and clean conflict refusal, without retries. Whole-source rollback remains the admitted design; there is no per-key inverse. Dry-run validates the same source pair and previews effects without publication. A source mismatch raises `TaskDocPublicationConflict` with bounded expected/observed evidence.

L04 narrowed the dry-run preflight: `validate_task_doc_transaction` now collects source-currentness
and scope-union resolution into one closure so the read-only path exercises the identical exact
source-pair transaction as protected publication, including the mutation-classified scope selection
performed by `resolve_projection_scope_union` over `TaskDocScopeChange` entries.

`validate_task_doc_transaction` also checks every candidate `subTask` that does not name an explicit `master`. Its folder master must exist and resolve to kind `master`, with a `subTasks` row whose number equals the candidate leaf ID. Resolution uses the prepared candidate overrides from the same transaction, so a prepared master/row is read consistently with its leaf. Missing folder-master authority or the matching row raises `Sub-task publication requires a master.` This conditional guard is exercised by dry preflight and protected publication; it does not claim to validate explicitly named-master paths through this branch.

Ordinary disk-backed graph-title reads deliberately remain inside the publisher callback, after
the task lock is held, so the title snapshot used for rendering is read under the same
serialization boundary as the document write.
Only pure submitted-batch graph cardinality is checked earlier.

`publish_prepared_task_documents` is the public application seam for callers that have already
captured candidate documents and exact source snapshots. It routes those bytes through the same
transaction, rather than making registration and other prepared-document callers reconstruct
scope-union or publisher behavior. This keeps accepted-source CAS, task-first publication,
invalidation, and rebuild behind one API.

Publication refreshes rendered task-document copies inside the same publisher: after the accepted write, `refresh_task_document_copies` rewrites the changed leaf in every existing enclosure atomically per file, and a copy failure rolls back the accepted sources before re-raising, so a failed copy refresh never leaves task truth ahead of its reads.

### Conventions

The ordinary task-doc entry holds the task-root file lock from authoritative source read through preparation and central publication. Independently prepared callers still carry the complete exact source pair into the central CAS; they cannot weaken it to a subset or retry automatically. Disk graph-title reads remain inside the publisher callback. Pure submitted-batch graph cardinality may be checked before central publication.

### Invariants And Boundaries

- Exact JSON and Markdown bytes for every selected/affected document are one CAS precondition.
- Task truth is authoritative. Queue/projection state is disposable: the owner invalidates the full affected scope and rebuilds per scope. The outer task-root file lock remains held until the central call returns, including its refresh/rollback and projection work.
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
- One task-root file lock and the call-scoped active marker surround central publication; the private body performs exact validation, source publication, copy refresh/rollback and per-scope projection work. [2]
- The outer task-doc call holds the same repository lock before reading/preparing the edit and refuses a nested publication before invoking the callback. [7]
- The kernel primitive uses a sibling lock file, a per-resource thread mutex and flock, with same-thread re-entry sharing the outer hold. [8]
- Native nested-refusal fixtures cover append and replacement and require task-source and memory bytes to equal their pre-batch values after failed refresh. [9]
- Graph cardinality is checked before transaction construction while disk title reads remain inside the publisher callback. [3]
- Scope changes bind each candidate to its exact accepted original bytes. [4]
- Dry-run and protected publication share exact source-currentness, conditional folder-master/matching-row validation with prepared overrides, and classifier-scoped union resolution. [5]
- Focused proof refuses two graph documents before publisher/projection mutation and preserves sentinel bytes. [6]

### Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

- The waiting second-thread writer prepares after failed-batch rollback and its question remains, for append and replacement cases. [10]
