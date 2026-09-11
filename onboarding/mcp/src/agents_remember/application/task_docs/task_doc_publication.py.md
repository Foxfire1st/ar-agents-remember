# mcp/src/agents_remember/application/task_docs/task_doc_publication.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/task_docs/task_doc_publication.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | `3e276f2b2052b641afbee180a472259f21b500df` |
| lastVerifiedCommitDate | 2026-09-02T14:46:34+02:00|
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

## Docs References

No configured Domain Documentation source applies to this repository-internal lifecycle seam.

## Repo-Internal References

The source file itself is the current evidence for this file-specific contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module defines the exact task publication request, transaction, and result models. | `TaskDocPublicationConflict`; `TaskDocPublication`; `TaskDocPublicationTransaction`; `TaskDocPublicationResult` | mcp/src/agents_remember/application/task_docs/task_doc_publication.py:35-50; mcp/src/agents_remember/application/task_docs/task_doc_publication.py:53-62; mcp/src/agents_remember/application/task_docs/task_doc_publication.py:65-73; mcp/src/agents_remember/application/task_docs/task_doc_publication.py:76-79 |
| Publication delegates exact validation, task write, affected-scope invalidation, and independent rebuild to the task-first owner. | `publish_task_doc_set`; `publish_task_doc_transaction_and_refresh`; `preview_task_doc_projection_effects`; `preview_task_doc_transaction_projection_effects` | mcp/src/agents_remember/application/task_docs/task_doc_publication.py:82-86; mcp/src/agents_remember/application/task_docs/task_doc_publication.py:131-147; mcp/src/agents_remember/application/task_docs/task_doc_publication.py:150-157; mcp/src/agents_remember/application/task_docs/task_doc_publication.py:160-175 |
| Graph cardinality is checked before transaction construction while disk title reads remain inside the publisher callback. | `task_doc_publication_transaction` | mcp/src/agents_remember/application/task_docs/task_doc_publication.py:178-208 |
| Scope changes bind each candidate to its exact accepted original bytes. | `task_doc_scope_changes` | mcp/src/agents_remember/application/task_docs/task_doc_publication.py:211-247 |
| Dry-run preflight validates source currentness and the classifier-scoped union through the same closure as publication. | `validate_task_doc_transaction`; `require_task_doc_sources_current` | mcp/src/agents_remember/application/task_docs/task_doc_publication.py:250-265; mcp/src/agents_remember/application/task_docs/task_doc_publication.py:268-285 |
| Focused proof refuses two graph documents before publisher/projection mutation and preserves sentinel bytes. | `TaskDocGraphPublicationTests` | mcp/tests/test_task_doc_graph_publication.py:93-140 |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

## Update History
- 2026-09-06T22:41:21+00:00: Generated citation repair: `TaskDocGraphPublicationTests` repointed to mcp/tests/test_task_doc_graph_publication.py:93-140. No content impact: mechanical anchor-range projection bound to citation source snapshot 250eac92295fa399589ccf1c9726bfb4cd28a1a0b20dca126769403fba09b52d; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for
  3e276f2b2052b641afbee180a472259f21b500df (CCR-R04@v1/L04): recorded the L04 dry-run change —
  `validate_task_doc_transaction` now folds source-currentness and
  `resolve_projection_scope_union` into one closure so preflight exercises the exact
  source-pair transaction including mutation-classified scope selection. Verification is pinned
  to the owning commit.

- 2026-08-26T10:44:52+02:00 — Documented `publish_prepared_task_documents` as the single public path for already-prepared document batches, removing repeated transaction assembly from callers.

- 2026-08-24T13:43+02:00 — DAGQC L1: ordinary publication now delegates graph-batch
  cardinality to the central zero/one owner before transaction construction while retaining
  on-disk title reads inside the protected publisher callback. The card was reconciled with the
  already-landed task-first invalidation/rebuild transaction. Verification metadata remains pinned
  until closeout.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: created from the accepted full L2 candidate. Verification fields remain blank until the architect-owned closeout has a real code commit to stamp.
