# mcp/src/agents_remember/serving/projections/snapshots_impl/_task_documents.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/serving/projections/snapshots_impl/_task_documents.py` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | `99dc249bd507c20b09ece1169c2b1fa2af8e8c1b` |
| lastVerifiedCommitDate | 2026-09-02T05:53:10+02:00|
| governingOverview      | `../overview.md`                                       |

## Governing Overview

[serving projections overview](../overview.md)

## Purpose

Task-document and series readers: summaries, full bodies, lifecycle binding. Task JSON is the source of truth (never the rendered markdown). These readers project task documents and the series checklist, resolve cross-folder lifecycle links, and hash full bodies for the on-demand body endpoint.

## Code Commentary

- `read_task_documents`
- `read_task_document_body`
- `_task_document_lifecycle_maps`
- `_task_doc_lifecycle_id`
- `_doc_enclosure_lifecycle`
- `read_series_documents`
- `_series_subtask_nodes`
- `_series_subtask_created_at`
- `_ref_lifecycle`
- `_task_step_nodes`
- `_task_doc_node`
- `_task_doc_body_revision` (since 260815-DAG-L14 the revision covers `subTasks` + `seats` so
  an open reader refetches when sprint linkage/seat edits land)
- `_task_doc_node` since 260815-DAG-L14 passes `SubTaskRef.masterRef` through to
  `TaskSubTaskRefNode.masterRef` and projects `doc.seats` as `TaskSeatNode` rows

Since 260831-CCR (commit `99dc249b`) the readers canonicalize the typed requirement and open-question
slots into stable reader strings: `_requirement_reader_text` (line 494) renders an
`ApprovedRequirementPacketRef` as `{stableId}@{version} — {path}`, `_question_reader_text`
(line 500) renders an `AcceptanceObligationQuestion` as `Acceptance obligation {id}: {question}`,
and `_task_doc_body_revision` (line 606) hashes typed intent slots through a stable by-alias dump
(`_task_intent_body_value`, line 631) so a change to a packet version or an obligation question
text alters the body revision and open readers refetch.

## Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/agents_remember/serving/projections/snapshots_impl/_task_documents.py`.
- Type-preserving intent slots must keep their canonicalized text stable: the reader surface is a
  string projection, while the digest path uses the typed by-alias dump.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own top-level surface is listed in Code Commentary; no cross-file citation rows are needed for this split module. | — | — |
| Canonicalized requirement text reader for typed packet refs. | `_requirement_reader_text` | mcp/src/agents_remember/serving/projections/snapshots_impl/_task_documents.py:494-498 |
| Canonicalized open-question reader for typed acceptance obligations. | `_question_reader_text` | mcp/src/agents_remember/serving/projections/snapshots_impl/_task_documents.py:500-504 |
| Body revision hashing of typed intent slots. | `_task_doc_body_revision`; `_task_intent_body_value` | mcp/src/agents_remember/serving/projections/snapshots_impl/_task_documents.py:606-623; mcp/src/agents_remember/serving/projections/snapshots_impl/_task_documents.py:631-637 |


## 260815-DAG-L12 Render-Ready Graph View Wiring

Both snapshot readers now project `TaskDocNode.executionGraphView` (L12-R4): `_task_doc_node` was split into the include-body-gated `_reader_fields` and the sprint-only `_execution_graph_fields` behind a bundled `_TaskDocProjectionOptions` (`include_body` + `master_docs`), and `_master_docs_by_ref` builds the title/status/nature join table from the bounded payload window (root `task.json` documents are never evicted, so a sprint's commanded masters are always present). `_execution_graph_view` does the tasks-domain walk — derived waves, resolved edge endpoints, joined titles, per-master facts — and feeds the primitives-only `build_execution_graph_view` builder (the observer package must not import tasks). Docs without a graph project `None`; `_task_doc_body_revision` is unchanged.


## 260821-CLIVE Discarded-Unstarted Projection

Master task and series nodes now project `discardedCount` plus typed `discardedSubTasks`, including
the audited reason, timestamp, disposition, and exact unstarted proof. The discarded history also
participates in task-body revision identity so an open reader refetches after a valid discard.
Discarded entries are historical task truth and never disappear merely because they are absent from
the active subtask list.

## CCR-R02@v2 Typed Slot Canonicalization

Per `requirements/CCR-R02-v2-normative-task-intent-identity.md`, the reader surface accounts for
typed `ApprovedRequirementPacketRef` and `AcceptanceObligationQuestion` slots (never raw model
reprs) and includes them in body-revision identity, so served bodies and revision tokens reflect
normative intent content exactly.

## Update History

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for 99dc249bd507 (CCR-R02@v2/L25):
  the serving task-document readers now canonicalize typed requirement/accepted-obligation slots and
  include them in `_task_doc_body_revision`; documented the stable reader-string and digest path.
  Verified at code commit 99dc249bd507c20b09ece1169c2b1fa2af8e8c1b.

- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: documented projection of audited discarded-unstarted task history. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.


- 2026-08-20T10:45+02:00 — 260815-DAG-L12:   both readers project the render-ready `executionGraphView`; `_task_doc_node` split into `_reader_fields` + `_execution_graph_fields` with `_TaskDocProjectionOptions`, `_master_docs_by_ref` join table, and the `_execution_graph_view` serving seam (L12-R4). Verified at code commit b7f2c8e2.

- 2026-08-20T04:26+02:00 — 260815-DAG-L14: `_task_doc_node` passes the typed `masterRef` through
  and projects first-class `seats` (`TaskSeatNode`); `_task_doc_body_revision` now covers
  `subTasks` + `seats` so an open sprint reader refetches on linkage/seat edits. Verified at code
  commit 9c3180c1.

- 2026-08-19T08:55+02:00 — 260815-DAG-L11: `_task_doc_node` now projects `executionWaves` as
  `TaskExecutionNode` rows (each persisted `SprintExecutionNode` re-validated into the served
  segment-aware projection type). Verification remains closeout-owned.

- 2026-08-15T02:16:50+02:00 — 260815-DAG-L1: task snapshot hydration now carries explicit master
  nature and sprint graph, derives deterministic waves, and includes both fields in body revision identity.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
