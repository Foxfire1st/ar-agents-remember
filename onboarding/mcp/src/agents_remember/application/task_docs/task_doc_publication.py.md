# mcp/src/agents_remember/application/task_docs/task_doc_publication.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/task_docs/task_doc_publication.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T13:43+02:00 |
| lastVerifiedCommitHash | `f95487ec993b58d34911bba0206a7fa6ef9684eb` |
| lastVerifiedCommitDate | 2026-08-24T15:28:18+02:00|
| governingOverview | `overview.md` |

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

Ordinary disk-backed graph-title reads deliberately remain inside the publisher callback, after
the task lock is held, so the title snapshot used for rendering is read under the same
serialization boundary as the document write.
Only pure submitted-batch graph cardinality is checked earlier.

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

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies to this repository-internal lifecycle seam.

## Repo-Internal References

The source file itself is the current evidence for this file-specific contract.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The module defines the exact task publication request, transaction, and result models. | L35-L80 | [task_doc_publication.py](mcp/src/agents_remember/application/task_docs/task_doc_publication.py) |
| Publication delegates exact validation, task write, affected-scope invalidation, and independent rebuild to the task-first owner. | L82-L133 | [task_doc_publication.py](mcp/src/agents_remember/application/task_docs/task_doc_publication.py) |
| Graph cardinality is checked before transaction construction while disk title reads remain inside the publisher callback. | L136-L166 | [task_doc_publication.py](mcp/src/agents_remember/application/task_docs/task_doc_publication.py) |
| Focused proof refuses two graph documents before publisher/projection mutation and preserves sentinel bytes. | L112-L160 | [test_task_doc_graph_publication.py](mcp/tests/test_task_doc_graph_publication.py) |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

## Update History

- 2026-08-24T13:43+02:00 — DAGQC L1: ordinary publication now delegates graph-batch
  cardinality to the central zero/one owner before transaction construction while retaining
  on-disk title reads inside the protected publisher callback. The card was reconciled with the
  already-landed task-first invalidation/rebuild transaction. Verification metadata remains pinned
  until closeout.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: created from the accepted full L2 candidate. Verification fields remain blank until the architect-owned closeout has a real code commit to stamp.
