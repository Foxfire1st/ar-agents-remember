# mcp/tests/test_wave1a_tool_inspections.py

## Governing Overview

[MCP Tests](overview.md)

## Purpose

This unit-regression test module verifies compact inline tool projections, removal of generic `outputSchema` and duplicate `structuredContent`, registration-time `ToolAnnotations` merging, `stdio_probe` text-JSON parsing, the omitted-slug review target guard, `task_doc.create` slug/repo injection, and MCP-boundary typed refusal conversion.

## Code Commentary

The tests are grouped into three areas:

- **Compact projections and early refusals:** Exercises `server_info_payload` with 128 running servers (checking summary counts, 5-entry `recent` list, and full 128-server daily log), `_integrity_answer` with 115 family routes and 50 worklist items (checking summary counts, omitted `items`, and full daily log), `project_landing_answer("worktree_sync", ...)` with 60 conflict files on a deep worktree root (verifying `>400` tokens overflows at bound 400 and fits cleanly under the 550-token bound with 5-entry capped `files` and `fileCount`), `compact_write_answer` with 20 violations/written/removed entries (5-entry caps and total counts), `build_early_refusal_result` single-line UTF-8 compact JSON with `structured_content is None`, and the unchanged 5,000-token `knowledge_read` exception bound.
- **Schemas, annotations, and `stdio_probe`:** Exercises `create_server` to confirm all 44 generic `dict`-returning public tools omit `outputSchema` while a custom `BaseModel`-returning tool retains `outputSchema` and `structured_content`; exercises `read_only_annotations` to confirm site-declared hints merge while central `read_only_hint` wins (`context_packet` and `knowledge_diff` remain `False`) and unclassified tools raise `UnknownReadOnlyMark`; and exercises `stdio_probe.probe_tool_server` with `structured_content=None`.
- **Review target guard, `task_doc.create`, and MCP-boundary refusals:** Exercises `task_doc` over a live `Client` to verify `begin_review` and `record_review` without `slug` refuse with `review-target-slug-required` leaving master `task.json` byte-identical, `task_doc.create` injects top-level `repo` and `slug`, accepts `kind="master"` with `slug="task"` as the canonical `task.json` file stem, and refuses all other mismatched values (including `kind="subTask"` with `slug="task"`) with `task-doc-slug-mismatch` or `task-doc-repo-mismatch`, a leaf-bound reviewer passing `slug="task"` gets `review-target-mismatch`, and atomic-master `record_route_review` without `slug` still succeeds without modifying the leaf document. Also verifies `task_doc_payload`, `worktree_status_payload`, `worktree_closeout_preview_payload`, `worktree_closeout_apply_payload`, and `worktree_checkpoint_landing_payload` convert their narrow typed domain errors into `{ok: False, code: ...}` refusals while re-raising unexpected `ImportError`/`RuntimeError`.

## Relationships

Declared in `mcp/tests/test-evidence-lanes.toml` under `unit-regression` and listed as an exact consumer in `mcp/tests/evidence-lifecycle.toml` for `_user_settings_guard.py`, `dashboard/package-lock.json`, `test_closeout_queue.py`, and `tool_answer_l111_test_support.py`. These are source-declared test assertions, not a fresh execution or certification receipt.

## Evidence

- Compact projection tests cover `server_info` (128 servers), `knowledge_integrity_check` (115 routes and 50 worklist items), `worktree_sync` (60 conflict files, 400-token overflow vs 550-token bound), `knowledge_write` (5-entry caps and counts), compact early refusals, and the 5,000-token `knowledge_read` bound. [1]
- Schema, annotation, and probe tests verify generic dict tools omit `outputSchema` while `BaseModel` tools keep it, `read_only_annotations` merges hints with central `read_only_hint` precedence, and `stdio_probe` parses text JSON when `structured_content` is `None`. [2]
- Target-guard and boundary-refusal tests verify omitted-slug and leaf-bound `slug="task"` refusals with zero `task.json` writes, atomic-master `record_route_review` preservation, `task_doc.create` slug/repo injection and mismatch refusals, and typed-error refusal conversion with unexpected exceptions re-raised. [3]
