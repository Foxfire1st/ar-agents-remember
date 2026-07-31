# mcp/src/agents_remember/mcp/tools/lifecycle_finalize.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/mcp/tools/lifecycle_finalize.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-31T15:31+02:00                     |
| lastVerifiedCommitHash |                                            `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d`|
| lastVerifiedCommitDate |                                            2026-07-31T19:28:50+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

Payload builder for the public `lifecycle_finalize_task` MCP tool.

## Code Commentary

`lifecycle_finalize_task_payload(config, contract_path, *, docs: FinalizeTaskDocs = NO_TASK_DOCS,
dry_run=False, teardown_providers=True)` is intentionally transport-thin. It forwards the runtime
config and contract path positionally, the three task-document inputs as one `FinalizeTaskDocs`
(`task_doc_path`, `master_doc_path`, `subtask_number` — 260731-EFA-L2; `NO_TASK_DOCS` is the shared
"finalize without touching documents" value), and the dry-run and provider-teardown flags, to
`controllers.worktree_tools.lifecycle_finalize_task_tool`, then validates the returned payload
through `base._tool_payload` under the `lifecycle_finalize_task` public tool name.

The published MCP tool still takes the three document arguments flat; `mcp/registration/tasks.py`
builds the `FinalizeTaskDocs`.

This module owns no lifecycle or Git behavior. The controller owns path
containment, and the worktree finalizer owns readiness, cleanup, and
task-document reconciliation.

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Controller function validates coordination-contained paths and delegates to the worktree finalizer. | [worktree_tools.py](agents-remember/mcp/src/agents_remember/controllers/worktree_tools.py) |
| The shared payload helper validates public response shape. | [base.py](agents-remember/mcp/src/agents_remember/mcp/tools/base.py) |
| The response model is registered in the public tool registry. | [lifecycle_finalize.py](agents-remember/mcp/src/agents_remember/models/lifecycle_finalize.py) |

## Update History

- 2026-07-31T15:31+02:00 — 260731-EFA-L2: the three task-document keyword arguments became one
  `FinalizeTaskDocs` (default `NO_TASK_DOCS`), and `contract_path` moved to a positional argument.
  Verification metadata pinned until closeout stamps the L2 code commit.
- 2026-06-23T22:50+02:00 — Created as the payload-builder surface for `lifecycle_finalize_task`. Verification metadata is pending until closeout stamps the source commit.
