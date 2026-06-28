# mcp/src/agents_remember/mcp/tools/lifecycle_finalize.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/mcp/tools/lifecycle_finalize.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-23T22:50+02:00                     |
| lastVerifiedCommitHash |                                            `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`|
| lastVerifiedCommitDate |                                            2026-06-28T18:49:06+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

Payload builder for the public `lifecycle_finalize_task` MCP tool.

## Code Commentary

`lifecycle_finalize_task_payload` is intentionally transport-thin. It forwards
the runtime config, contract path, optional leaf task document, optional parent
document plus subtask number, dry-run flag, and provider-teardown flag to
`controllers.worktree_tools.lifecycle_finalize_task_tool`, then validates the
returned payload through `base._tool_payload` under the
`lifecycle_finalize_task` public tool name.

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

- 2026-06-23T22:50+02:00 — Created as the payload-builder surface for `lifecycle_finalize_task`. Verification metadata is pending until closeout stamps the source commit.
