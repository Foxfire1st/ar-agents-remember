# mcp/src/agents_remember/application/task_docs

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | `mcp/src/agents_remember/application/task_docs` |
| doc_type | `route-local-overview` |
| lastUpdated | 2026-08-23T16:08+02:00 |
| lastVerifiedCommitHash | `1d446724d099517f6f52d596b47827ae2391a2a4` |
| lastVerifiedCommitDate | 2026-08-24T00:21:10+02:00 |
| governingOverview | `../overview.md` |

## Governing Overview

[application overview](../overview.md)

## Purpose

The task-document authoring package (260815-DAG master full-gate repair): the operation-dispatched
`task_doc_tool` application entry point and its sibling modules — `task_ref` (the typed task
reference), `task_reopen` (leaf reopen), `task_doc_route_review` (candidate-bound route-review
authority), `task_doc_queue_scope` (governing queue scope), `task_execution_topology` (graph
authoring/edits), and `task_sprint_linkage` (sprint↔master attach/detach/linkage facts). The
modules moved here from `application/` (flat) so the task-document authoring seam owns one package.

## Hot Path Summary

Task-document authoring remains the source-of-truth publication plane. L2 adds exact source snapshots and short integration serialization where task structure intersects landing. The pre-L3 queue-governed publisher and its sprint-wide refusal behavior are still present; L3 owns removing that authoring dependency and replacing it with affected-candidate invalidation/rebuild.

`task_doc` MCP calls dispatch through `task_doc_tool` to one operation (create/replace/edits/special
ops); the special ops (sprint linkage + execution graph authoring) publish inside their own
functions and return raw operation payloads merged with the standard identity via
`_sprint_doc_identity`. Route review, queue scope, topology enforcement, and master-row completion
checks run before any publication; everything validates against the strict `TaskDocResponse` wire
shape (the special-op fields declared in `models/task_doc.py`).

## Conventions

- The package uses relative imports between its own modules (`from . import task_sprint_linkage`).
- The strict task-document writer authorities in `code_quality/single_owner.py` name these files.

## Invariants And Boundaries

- Only these modules may author/render task documents; the application layer is the only writer.
- The served-build preflight, route-review gate, and transitional pre-L3 queue-scope gate still run
  before a governed write.
- Nothing here touches memory repos or the coordination ledger directly.

## 260821-CLIVE-L2 Current Architecture

Task publication now validates the complete accepted source set and current integration authority, then writes one transaction or reports the exact conflict. L2 centralizes this transaction but still wraps governed publication in the pre-L3 queue store. Removing queue refusal from task authoring and adding affected-candidate invalidation/rebuild remain L3 scope.

### Reconciled Source Evidence

| Finding | Citations | Source Path |
| --- | --- | --- |
| Transactional task publication. | L36-L74; L77-L197 | `mcp/src/agents_remember/application/task_docs/task_doc_publication.py` |

## Update History

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: refreshed current route intent and source evidence for the accepted full L2 candidate; verification provenance and contract-scoped quality enforcement remain architect-closeout-owned.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: created the `application/task_docs`
  route — seven modules moved from `application/` (flat); `task_doc_tools` gained
  `_sprint_doc_identity`. Verified at code commit e5cb139f.
