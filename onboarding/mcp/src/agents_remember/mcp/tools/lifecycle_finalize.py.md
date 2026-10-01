# mcp/src/agents_remember/mcp/tools/lifecycle_finalize.py

## Governing Overview

[overview.md](overview.md)

## Purpose

Payload builder for the public `lifecycle_finalize_task` MCP tool.

## Code Commentary

`lifecycle_finalize_task_payload(config, contract_path, *, docs: FinalizeTaskDocs = NO_TASK_DOCS,
dry_run=False, teardown_providers=True)` is intentionally transport-thin. It forwards the runtime
config and contract path positionally, the three task-document inputs as one `FinalizeTaskDocs`
(`task_doc_path`, `master_doc_path`, `subtask_number` — 260731-EFA-L2; `NO_TASK_DOCS` is the shared
"finalize without touching documents" value), and the dry-run and provider-teardown flags, to
`application.worktree_tools.lifecycle_finalize_task_tool`, then validates the returned payload
through `base._tool_payload` under the `lifecycle_finalize_task` public tool name.

The published MCP tool still takes the three document arguments flat; `mcp/registration/tasks.py`
builds the `FinalizeTaskDocs`.

This module owns no lifecycle or Git behavior. The application entry point owns path
containment, and the worktree finalizer owns readiness, cleanup, and
task-document reconciliation.

## Evidence

### Docs References

No external Domain Documentation source is configured for this memory repo.

### Repo-Internal References

- Application entry point validates coordination-contained paths, delegates to the worktree finalizer, and then performs configured completion cleanup. [1]
- The shared payload helper is `_tool_payload`. [2]
- The response boundary is `complete_tool_response`. [3]
- The response model is registered in the public tool registry. [4]
