# mcp/src/agents_remember/tasks/reopen.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/tasks/reopen.py`  |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-03T00:30+02:00                     |
| lastVerifiedCommitHash | `842b487b854503d95c9c2d9dce1841198ba93c7d` |
| lastVerifiedCommitDate | 2026-07-24T17:08:25+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[tasks/overview.md](overview.md)

## Purpose

The `task_reopen` implementation (`reopen_task`, L43-L102): reopen a fully landed leaf task under its EXACT
same leaf id. A task-state reset, not a worktree operation — it lives in the tasks
package even though it also rewrites the leaf's enclosure contract, because the thing
being reopened is the task; recreating worktrees stays `worktree_start`'s job.

## Code Commentary

### Logic

`reopen_task(contract_path, dry_run=False)` loads the enclosure contract and first runs
`_reopen_blockers`: the contract must be `kind == "leaf"` with closeout, integration,
and cleanup all `completed`, and neither the code nor memory worktree may still exist
on disk — anything else returns a `blocked` payload (returncode 2) listing every
blocker. On the happy path it `dataclasses.replace`s the contract back to virgin
review/closeout/integration state (`human_review pending-review`/unapproved, both
statuses `not-started`, all commit fields cleared), clears `lifecycle_id`, and marks
`cleanup: "reopened"` — the tombstone marker `worktree_start`'s existing-contract
branch treats like `abandoned` (recreate fresh, never attach). `_reset_leaf_doc`
resolves the leaf's task document through `tasks.leaf_doc.find_leaf_doc`, sets its
status to `planning`, clears `lifecycleId` (the next start restamps it), appends an
audit decision with the reopen timestamp, and `_reset_master_index` flips the master's
`subTasks` row for the doc back to `planning`. Docs are rewritten through
`tasks.store.write_task_docs`, so the markdown re-renders from the JSON. `dry_run`
previews both resets without writing anything.

### Invariants And Boundaries

- The leaf id NEVER changes across a reopen — that is the whole point; every doc,
  chat, and dashboard binding holds by construction because the identity is stable.
- Only a fully landed leaf reopens; in-flight leaves, masters/series contracts, and
  leaves with live worktrees are refused with explicit blockers.
- The tool mutates only coordination state (contract + task docs); it has no git
  effects. The response keeps the worktree-command payload shape (contract state),
  which is why `TaskReopenResponse` subclasses `WorktreeCommandResponse`.
- `nextOperation` is always `worktree_start`: edit steps via `task_doc`, then start
  the same leaf id.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The doc lookup and lifecycle restamp helpers this module shares with worktree start. | [leaf_doc.py](agents-remember/mcp/src/agents_remember/tasks/leaf_doc.py) |
| The recreate-fresh branch that admits `cleanup: reopened` and restamps the doc after the contract write. | [start.py](agents-remember/mcp/src/agents_remember/worktrees/modules/start.py) |
| The controller exposing this as the `task_reopen` MCP tool beside `task_doc`. | [task_doc_tools.py](agents-remember/mcp/src/agents_remember/controllers/task_doc_tools.py) |
| The contract dataclass and load/write helpers the reset goes through. | [worktree_contract.py](agents-remember/mcp/src/agents_remember/worktrees/worktree_contract.py) |

## 260718-CHATS-L5I Current Delta

Task reopening now clears the persisted landing-final observation as part of returning a contract to active work and reports any clearing failure explicitly. A reopened task must not retain an old completed landing projection as current fact.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## Update History

- 2026-07-31T19:30+02:00 — 260731-EFA-L2 curator: re-derived 1 stale self-citation. Purpose cited
  the `task_reopen` implementation at L11, which is now a line inside the module docstring; the
  entry point is `reopen_task` at L43-L102 (the module docstring grew to L1-L22 and the
  landing-freeze imports/helper landed after it). Named the function explicitly so the anchor is
  self-checking. Claim unchanged.

- 2026-07-24T13:18:47Z — 260718-CHATS-L5I curator: corrected the source-side behavior record for the current backend/shared delta and preserved the pre-commit verification stamp.

- 2026-07-03T00:30+02:00 — Created for L11 (leaf reopen semantics): `reopen_task` resets a completed
  leaf's contract and doc back to planning under its original leaf id, replacing the suffixed `-rN`
  reopen workaround. Verification metadata pinned until closeout stamps the code commit.
