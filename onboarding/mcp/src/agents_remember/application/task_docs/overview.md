# mcp/src/agents_remember/application/task_docs

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | `mcp/src/agents_remember/application/task_docs` |
| doc_type | `route-local-overview` |
| lastUpdated | 2026-08-24T13:43+02:00 |
| lastVerifiedCommitHash | `f95487ec993b58d34911bba0206a7fa6ef9684eb` |
| lastVerifiedCommitDate | 2026-08-24T15:28:18+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[application overview](../overview.md)

## Purpose

The task-document authoring package (260815-DAG master full-gate repair): the operation-dispatched
`task_doc_tool` application entry point and its sibling modules — `task_ref` (the typed task
reference), `task_reopen` (leaf reopen), `task_doc_route_review` (candidate-bound route-review
authority), `task_doc_publication` (task-first exact publication plus projection refresh),
`task_doc_graph_titles` (zero-or-one graph-bearing batch authority),
`task_doc_section_scaffolding` (atomic raw-section shape boundary),
`task_execution_topology` (graph authoring/edits), and `task_sprint_linkage`
(sprint↔master attach/detach/linkage facts). The modules moved here from `application/` (flat) so
the task-document authoring seam owns one package.

## Hot Path Summary

Task-document authoring is the source-of-truth publication plane. An otherwise-valid mutation is
never subordinate to queue state. The exact transaction rechecks accepted source bytes, writes task
truth and invalidates every affected waiting projection under the task-publication lock, then
rebuilds each disposable projection independently from current closeout-door facts. A planning
change therefore yields a clear invalidation/rebuild signal without freezing unrelated task-doc
authoring or claiming lifecycle evidence for an operation already underway.

`task_doc` MCP calls dispatch through `task_doc_tool` to one operation (create/replace/edits/special
ops); the special ops (sprint linkage + execution graph authoring) publish inside their own
functions and return raw operation payloads merged with the standard identity via
`_sprint_doc_identity`. Route review, topology enforcement, and master-row completion
checks run before any publication; everything validates against the strict `TaskDocResponse` wire
shape (the special-op fields declared in `models/task_doc.py`).

Graph-bearing writers share `task_doc_graph_titles`: pure batch cardinality is checked early and a
batch with more than one graph-bearing document refuses, while on-disk title reads remain inside the
locked publisher callback. Create/replace share `task_doc_section_scaffolding`: raw `sections` must
be a list of mappings before any missing canonical register scaffolds are appended.

## Conventions

- The package uses relative imports between its own modules (`from . import task_sprint_linkage`).
- The strict task-document writer authorities in `code_quality/single_owner.py` name these files.
- Shared contracts are explicit owners, not copied private helpers: graph cardinality/title context
  lives in `task_doc_graph_titles.py`, raw-section scaffolding in
  `task_doc_section_scaffolding.py`, and publication ordering in `task_doc_publication.py`.

## Invariants And Boundaries

- Only these modules may author/render task documents; the application layer is the only writer.
- Task truth owns authoring; the waiting queue is a disposable scheduling projection and cannot
  freeze `task_doc` operations.
- Queue invalidation cannot erase claimed/running/commit lifecycle evidence; that durable evidence
  belongs outside the projection plane.
- Publication admits at most one graph-bearing document. Preview and apply use the same owner; no
  first-graph selector, catch-and-split retry, or silent title fallback is introduced.
- Raw section scaffolding validates the entire container/member shape before mutation and preserves
  typed errors; it does not coerce malformed input.
- Nothing here touches memory repos or the coordination ledger directly.

## Current Architecture After CLIVE And DAGQC L1

Task publication validates the complete accepted source set and current integration authority, then
writes task truth plus projection invalidation atomically or reports the exact conflict. Rebuild is
independent and derived from current task/door facts. DAGQC L1 centralizes graph-bearing batch
cardinality/title context and raw-section pre-model validation so all authoring routes share one
contract per concern.

### Reconciled Source Evidence

| Finding | Citations | Source Path |
| --- | --- | --- |
| Task-first transactional publication and independent projection refresh. | L82-L166 | `mcp/src/agents_remember/application/task_docs/task_doc_publication.py` |
| Zero-or-one graph-bearing publication batch and in-memory title context. | L17-L51 | `mcp/src/agents_remember/application/task_docs/task_doc_graph_titles.py` |
| Atomic raw-section shape validation and missing-register scaffolding. | L17-L55 | `mcp/src/agents_remember/application/task_docs/task_doc_section_scaffolding.py` |

## Update History

- 2026-08-24T13:43+02:00 — 260821-DAGQC-L1: made the task-first publication ownership current,
  added the shared graph-cardinality/title and raw-section-scaffolding route owners, and removed the
  stale queue-subordinate transitional account. Verification metadata remains pinned until
  architect-owned closeout stamps the real code commit.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: refreshed current route intent and source evidence for the accepted full L2 candidate; verification provenance and contract-scoped quality enforcement remain architect-closeout-owned.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: created the `application/task_docs`
  route — seven modules moved from `application/` (flat); `task_doc_tools` gained
  `_sprint_doc_identity`. Verified at code commit e5cb139f.
