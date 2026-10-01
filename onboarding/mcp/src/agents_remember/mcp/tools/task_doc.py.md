# mcp/src/agents_remember/mcp/tools/task_doc.py

## Governing Overview

[mcp/tools/overview.md](overview.md)

## Purpose

Transport-thin payload builders for the task-domain tools: `task_doc` authoring and,
since L11, `task_reopen` (reopen a completed leaf task under its exact leaf id).

## Code Commentary

### Logic

`task_doc_payload(config, target: TaskDocTarget, *, operation, edit: TaskDocEdit = NO_EDIT,
call: TaskDocCall = DEFAULT_TASK_DOC_CALL)` calls `task_doc_tool(config, target, operation=...,
edit=..., call=...)` and
wraps the result through `base._tool_payload("task_doc", ...)`, so the response is validated against
`TaskDocResponse` and (like every tool) attributed to the active lifecycle at the `_tool_payload`
choke point.

Since 260731-EFA-L2 the arguments arrive in two objects that answer two different questions:
`TaskDocTarget(repo_id, task_name, contract_path, slug)` — which document — and
`TaskDocEdit(fields, step, decision, subtask, section)` — what the edit is. `NO_EDIT` is the
shared empty edit a read (`operation='get'`) passes. The `subtask`/`section` slots still carry the
master `set_subtask`/`set_section`/`remove_subtask` edits; `dry_run` still threads the R5 preview
flag (the application entry point renders + diffs the would-be doc and returns it **without** writing).

The published MCP signature is still the flat argument list; `mcp/registration/tasks.py` builds the
two objects, because a model-typed tool parameter would republish `task_doc` as a nested object.

### Invariants And Boundaries

- Stays transport-thin: all behavior (resolution, mutation, render) lives in the
  application entry point and the `tasks/` package.
- Must route through `base._tool_payload`, like every other builder.

## Evidence

### Repo-Internal References

- The application entry point this builder forwards to. [1]
- The shared validation/emission choke point. [2]
- The response model the payload validates against. [3]
