# mcp/src/agents_remember/models/lifecycle_finalize.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/models/lifecycle_finalize.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-23T22:50+02:00                     |
| lastVerifiedCommitHash |                                            `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`|
| lastVerifiedCommitDate |                                            2026-06-28T18:49:06+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

Defines the strict public response contract for `lifecycle_finalize_task`.

## Code Commentary

`LifecycleFinalizeTaskResponse` inherits from `ToolResponse`, so it uses the
strict Agents Remember response-envelope convention. It declares the finalizer
operation name plus identity fields (`taskId`, `taskName`, `lifecycleId`), the
current finalizer `state`, `dryRun`, contract path, optional landed commit and
target branch, blocker list, cleanup detail, task-update detail, and summary.

The model intentionally does not accept the full `worktree_status` payload. The
finalizer response is a separate terminal contract: it reports only the edge
proof, cleanup result, task-document reconciliation, and blockers relevant to
finalization.

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Strict tool response base class is defined here. | [base.py](agents-remember/mcp/src/agents_remember/models/base.py) |
| Public response registry maps `lifecycle_finalize_task` to this model. | [tool_registry.py](agents-remember/mcp/src/agents_remember/models/tool_registry.py) |
| Conformance tests validate representative finalizer payloads against this model. | [test_tool_response_conformance.py](agents-remember/mcp/tests/test_tool_response_conformance.py) |

## Series-Contract Notes

`LifecycleFinalizeTaskResponse` carries both the leaf `enclosurePath` and the root-level `taskArchive` result so finalization can report contract cleanup and root archival separately.

## Update History

- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: finalization responses now expose `enclosurePath` and `taskArchive` so callers can report the leaf contract path and root-task archive action. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-23T22:50+02:00 — Created the strict `LifecycleFinalizeTaskResponse` model for the lifecycle finalizer tool. Verification metadata is pending until closeout stamps the source commit.
