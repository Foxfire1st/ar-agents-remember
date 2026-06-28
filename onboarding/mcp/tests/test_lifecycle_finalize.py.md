# mcp/tests/test_lifecycle_finalize.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_lifecycle_finalize.py`     |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-23T22:50+02:00                     |
| lastVerifiedCommitHash |                                            `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`|
| lastVerifiedCommitDate |                                            2026-06-28T18:49:06+02:00|
| governingOverview      | `../overview.md`                              |

## Purpose

Focused regression tests for the `lifecycle_finalize_task` worktree operation
and response-model registration.

## Code Commentary

The fixture creates temporary Git repositories and disabled-memory worktree
contracts so the finalizer's Git ancestry proof runs against real commits. It
also creates JSON-primary task documents through `write_task_doc`, allowing the
tests to assert that finalization writes both JSON and rendered markdown through
the production task document service.

Covered behavior:

- a finalized task updates the leaf document to `Completed`, updates only the
  immediate parent subtask row to `Completed`, and leaves the parent/master task
  status unchanged
- missing closeout/integration data or a landed commit absent from the target
  branch returns `not-finalizable-yet` blockers
- cleanup failures return `cleanup-blocked` and do not mutate task documents
- dry-run returns `would-finalize` and `would-update` without mutating documents
- `PUBLIC_TOOL_RESPONSE_MODELS` registers `lifecycle_finalize_task` to
  `LifecycleFinalizeTaskResponse`

The local `_payload` helper casts `WorktreeCommandResult.payload` for test
assertions only; runtime payloads remain typed as `dict[str, object]`.

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Finalizer behavior under test lives here. | [finalize.py](agents-remember/mcp/src/agents_remember/worktrees/modules/finalize.py) |
| Task document read/write behavior used by the fixture lives here. | [document.py](agents-remember/mcp/src/agents_remember/tasks/document.py) |
| Git fixture helpers come from the existing worktree support tests. | [test_worktree_support.py](agents-remember/mcp/tests/test_worktree_support.py) |
| Public response model registry is checked for the finalizer entry. | [tool_registry.py](agents-remember/mcp/src/agents_remember/models/tool_registry.py) |

## Update History

- 2026-06-23T22:50+02:00 — Created focused lifecycle finalizer regression coverage. Verification metadata is pending until closeout stamps the source commit.
