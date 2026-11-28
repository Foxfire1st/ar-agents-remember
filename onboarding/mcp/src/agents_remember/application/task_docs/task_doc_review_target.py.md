# mcp/src/agents_remember/application/task_docs/task_doc_review_target.py

## Governing Overview

[task_docs overview](overview.md)

## Purpose

This module guards `task_doc` `begin_review` and `record_review` calls against silently targeting master `task.json` when a caller omits `slug` or supplies `slug="task"` from a leaf context. It runs before `task.json` is read or mutated.

## Code Commentary

`_GUARDED_REVIEW_OPS` restricts enforcement to `begin_review` and `record_review`; `record_route_review` is intentionally exempt so atomic-master route reviews continue to use their canonical series binding without a leaf `slug`.

`enforce_review_target` inspects the optional active `WorktreeContract`, the seat's `AgentBinding` (via `_safe_agent_binding`, treating malformed bindings as `None`), and sibling leaf `.json` files under `task_root` (excluding `task.json`). When `slug` is omitted or blank, it raises `TaskDocError` with code `review-target-slug-required` if a leaf contract is active, if the caller is a leaf-bound seat (binding `task_ref` path does not end in `task.json`), or if sibling leaf `.json` files exist in `task_root`. When `slug` is explicitly `"task"`, it raises `TaskDocError` with code `review-target-mismatch` if either a leaf contract is active or the caller is a leaf-bound seat.

A genuine master-level review on a directory with sibling leaf files still succeeds when called without a leaf contract or leaf-bound seat by passing explicit `slug="task"`.

## Relationships

`task_doc_tools.py::_resolve_task_doc_target` calls `enforce_review_target` during target resolution before loading or modifying `task.json`. At the MCP boundary (`mcp/tools/task_doc.py::task_doc_payload`), raised `TaskDocError` instances are converted into structured `{ok: False, code: ...}` refusals while direct domain callers continue to observe `TaskDocError`.

## Evidence

- `_GUARDED_REVIEW_OPS` limits the guard to `begin_review` and `record_review`, keeping atomic-master `record_route_review` exempt. [1]
- `enforce_review_target` refuses omitted `slug` with `review-target-slug-required` on leaf contracts, leaf-bound seats, or task folders holding sibling leaf documents, and refuses `slug="task"` with `review-target-mismatch` on leaf contracts or leaf-bound seats. [2]
