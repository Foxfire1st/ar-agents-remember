# mcp/src/agents_remember/application/task_docs

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | `mcp/src/agents_remember/application/task_docs` |
| doc_type | `route-local-overview` |
| lastUpdated | 2026-08-21T00:45+02:00 |
| lastVerifiedCommitHash | `e5cb139f66abbd6502d4dcc4be883eb5f49770fe` |
| lastVerifiedCommitDate | 2026-08-21T00:28:23+02:00 |
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
- The served-build preflight and the route-review/queue-scope gates still run before any write
  (unchanged from the flat-application era).
- Nothing here touches memory repos or the coordination ledger directly.

## Update History

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: created the `application/task_docs`
  route — seven modules moved from `application/` (flat); `task_doc_tools` gained
  `_sprint_doc_identity`. Verified at code commit e5cb139f.
