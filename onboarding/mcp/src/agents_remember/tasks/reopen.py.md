# mcp/src/agents_remember/tasks/reopen.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/tasks/reopen.py`  |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-01T10:12+02:00                     |
| lastVerifiedCommitHash | `e52edaf5b655f495580efd93306afdf922b19b51` |
| lastVerifiedCommitDate | 2026-08-01T11:01:51+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[tasks/overview.md](overview.md)

## Purpose

The `task_reopen` implementation (`reopen_task`, L45-L112): reopen a fully landed leaf task under its EXACT
same leaf id. A task-state reset, not a worktree operation — it lives in the tasks
package even though it also rewrites the leaf's enclosure contract, because the thing
being reopened is the task; recreating worktrees stays `worktree_start`'s job.

## Code Commentary

### Logic

`reopen_task(contract_path, dry_run=False)` loads the enclosure contract and first runs
`_reopen_blockers` (L137-L151): the contract must be `kind == "leaf"` with closeout, integration,
and cleanup all `completed`, and neither the code nor memory worktree may still exist
on disk — anything else returns a `blocked` payload (returncode 2) listing every
blocker.

On the happy path the contract rewrite is now **two nested calls, split by what the
type checker can see** (L63-L88):

- `dataclasses.replace(contract, ...)` clears the free-form provenance — `approved_for_commit`,
  `commit_approval_note`, the three commit hashes, `integration_strategy`, the three integrated
  hashes, `lifecycle_id`, `memory_state`.
- `amend_contract(..., ContractCells(human_review_status="pending-review",
  closeout_status="not-started", integration_status="not-started", cleanup="reopened"))` moves
  the four **vocabulary** cells (L82-L87).

The split is the fix, not a refactor. typeshed declares
`dataclasses.replace(obj, /, **changes: Any)`, so for as long as `cleanup="reopened"` was spelled
as a `replace` keyword it crossed the boundary **completely unchecked** — zero pyright
diagnostics against a `Literal`, measured. And `reopened` was one of the six values
`models.worktree.WorktreeSummary` then rejected, which is how the tool that writes it and the
packet that reports it disagreed about the contract this tool had just written.
`ContractCells` (`worktree_contract.py` L171) is the typed record that puts those fields back in
front of the checker; `amend_contract` (L188 there) performs the copy, leaving any cell it was
not handed alone. `cleanup: "reopened"` remains the tombstone marker `worktree_start`'s
existing-contract branch treats like `abandoned` (recreate fresh, never attach) — and it is now a
declared member of `CleanupStatus` (L55 there), so the packet accepts it.

`_reset_leaf_doc` (L154-L187)
resolves the leaf's task document through `tasks.leaf_doc.find_leaf_doc`, sets its
status to `planning`, clears `lifecycleId` (the next start restamps it), appends an
audit decision with the reopen timestamp, and `_reset_master_index` (L190-L208) flips the master's
`subTasks` row for the doc back to `planning`. Docs are rewritten through
`tasks.store.write_task_docs`, so the markdown re-renders from the JSON. `dry_run`
previews both resets without writing anything.

### Invariants And Boundaries

- The leaf id NEVER changes across a reopen — that is the whole point; every doc,
  chat, and dashboard binding holds by construction because the identity is stable.
- Only a fully landed leaf reopens; in-flight leaves, masters/series contracts, and
  leaves with live worktrees are refused with explicit blockers.
- **A contract's vocabulary cells are moved through `ContractCells` /
  `amend_contract`, never as `dataclasses.replace` keywords.** `replace` is
  `**changes: Any` in typeshed, so a `replace` keyword is an unchecked write to a
  `Literal` field. `test_wire_vocabulary_exhaustiveness` enforces this as a rule
  across the package (`test_no_contract_cell_is_written_through_dataclasses_replace`),
  which is what stops a later edit from routing around the typed writer. The
  `replace` call that survives here is legitimate: it carries only free-form
  string/bool provenance fields, none of them a vocabulary cell.
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
| The contract dataclass and load/write helpers the reset goes through, plus the typed write path this module now uses: `ContractCells` (L171), `amend_contract` (L188), and the six vocabulary aliases including `CleanupStatus` (L55), which declares `reopened`. | [worktree_contract.py](agents-remember/mcp/src/agents_remember/worktrees/worktree_contract.py) |
| The wire model that reports `cleanup` and had rejected `reopened` until it began importing `CleanupStatus`. | [models/worktree.py](agents-remember/mcp/src/agents_remember/models/worktree.py) |
| `test_no_contract_cell_is_written_through_dataclasses_replace` and `test_every_writable_cleanup_value_validates_at_the_wire_boundary` pin both halves of this. | [test_wire_vocabulary_exhaustiveness.py](agents-remember/mcp/tests/test_wire_vocabulary_exhaustiveness.py) |

## 260718-CHATS-L5I Current Delta

Task reopening now clears the persisted landing-final observation as part of returning a contract to active work and reports any clearing failure explicitly. A reopened task must not retain an old completed landing projection as current fact.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## Update History

- 2026-08-01T10:12+02:00 — 260731-EFA-L4 curator: body corrected. The card said the happy path
  "`dataclasses.replace`s the contract back to virgin review/closeout/integration state ... and
  marks `cleanup: "reopened"`". That single `replace` is now split in two (L63-L88): the free-form
  provenance still goes through `replace`, while the four VOCABULARY cells
  (`human_review_status`, `closeout_status`, `integration_status`, `cleanup`) go through
  `amend_contract(..., ContractCells(...))` (L82-L87). The split is the fix, not a refactor —
  typeshed types `replace` as `**changes: Any`, so `cleanup="reopened"` produced zero pyright
  diagnostics against a `Literal` field, and `reopened` was one of the six values
  `models.worktree.WorktreeSummary` then rejected: this tool wrote a contract the context packet
  could not report. `reopened` is now a declared member of `CleanupStatus`
  (`worktree_contract.py` L55). Added the no-`replace`-for-vocabulary-cells invariant, noting the
  surviving `replace` call is legitimate because it carries no vocabulary cell. Citations: the
  Purpose self-citation `reopen_task` L43-L102 → L45-L112 (the function grew with the nested
  call), and `_reopen_blockers` L137-L151, `_reset_leaf_doc` L154-L187, `_reset_master_index`
  L190-L208 pinned for the first time; the `worktree_contract.py` reference row gained
  `ContractCells` L171 / `amend_contract` L188 / `CleanupStatus` L55, and rows were added for
  `models/worktree.py` and the exhaustiveness suite. Verification metadata pinned until closeout
  stamps the L4 commit.
- 2026-07-31T19:30+02:00 — 260731-EFA-L2 curator: re-derived 1 stale self-citation. Purpose cited
  the `task_reopen` implementation at L11, which is now a line inside the module docstring; the
  entry point is `reopen_task` at L43-L102 (the module docstring grew to L1-L22 and the
  landing-freeze imports/helper landed after it). Named the function explicitly so the anchor is
  self-checking. Claim unchanged.

- 2026-07-24T13:18:47Z — 260718-CHATS-L5I curator: corrected the source-side behavior record for the current backend/shared delta and preserved the pre-commit verification stamp.

- 2026-07-03T00:30+02:00 — Created for L11 (leaf reopen semantics): `reopen_task` resets a completed
  leaf's contract and doc back to planning under its original leaf id, replacing the suffixed `-rN`
  reopen workaround. Verification metadata pinned until closeout stamps the code commit.
