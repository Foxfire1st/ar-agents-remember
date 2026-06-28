# mcp/src/agents_remember/worktrees/modules/finalize.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/worktrees/modules/finalize.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-23T22:50+02:00                     |
| lastVerifiedCommitHash |                                            `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`|
| lastVerifiedCommitDate |                                            2026-06-28T18:49:06+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

Owns the terminal `lifecycle_finalize_task` worktree operation: prove that a
closed task's landed commit is present on the recorded parent source branch,
verify or run cleanup, and reconcile task documents to `Completed`.

## Code Commentary

`FinalizeArgs` carries the contract path, optional leaf task document path,
optional parent/master task document path plus subtask number, `dry_run`, and
provider-teardown behavior. `finalize_result` loads the contract and refuses to
finalize until closeout is completed, a code commit is recorded, integration is
completed, the landed commit (`integrated_code_commit` when present, otherwise
`code_commit`) is an ancestor of the local `code_source_branch`, and
`guidance.carryover_done` reports external-memory carryover complete.

The readiness check treats PR-gated and direct branch edges the same after the
PR process is done and the parent branch has been pulled locally: it checks Git
ancestry on the local recorded source branch. It intentionally does not infer
squash-merge equivalence; squash recovery is a manual/emergency path because it
breaks commit-lineage based memory lookup.

Cleanup is handled as part of the finalization operation. If the contract is
already cleaned, the response records `already-completed`; otherwise the module
delegates to `cleanup_result` with `approved=not dry_run` and
`teardown_providers` carried through. Cleanup failures return
`cleanup-blocked` and leave task documents unchanged.

Task document reconciliation is optional and edge-scoped. `task_doc_path` is
set to `Completed` unless it points at a master document. `master_doc_path` plus
`subtask_number` sets only that immediate parent row to `Completed`. The parent
task status itself is left unchanged, and ancestors are not completed
recursively; callers repeat finalization for the next parent-child branch edge.
Dry-run returns `would-update` task-document states without writing files.

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Cleanup behavior and branch/worktree removal are delegated here. | [cleanup.py](agents-remember/mcp/src/agents_remember/worktrees/modules/cleanup.py) |
| Carryover completion is proven against the official memory ledger here. | [guidance.py](agents-remember/mcp/src/agents_remember/worktrees/modules/guidance.py) |
| Git ancestry proof uses the worktree module Git adapter. | [git.py](agents-remember/mcp/src/agents_remember/worktrees/modules/git.py) |
| Task document JSON/markdown reconciliation uses the task document service. | [document.py](agents-remember/mcp/src/agents_remember/tasks/document.py) |
| Focused tests pin readiness, dry-run, cleanup-blocked, and task-doc update behavior. | [test_lifecycle_finalize.py](agents-remember/mcp/tests/test_lifecycle_finalize.py) |

## Series-Contract Notes

Finalization reports `enclosurePath` for the leaf being finalized and only archives completed root tasks when the finalized contract is a root `kind="series"` contract.

## Update History

- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: finalization now returns `enclosurePath`, skips root archive work for leaf contracts, and archives completed root series tasks into `0_archive` once a series contract is finalized. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-23T22:50+02:00 — Created for dashboard task 14. The module adds the terminal lifecycle finalizer that proves one parent-child branch edge, runs or verifies cleanup, and marks the current task plus immediate parent row complete. Verification metadata is pending until closeout stamps the source commit.
