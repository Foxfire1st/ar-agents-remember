# mcp/src/agents_remember/worktrees/modules/abandon.py

## Purpose

`abandon.py` is the discard-without-integration lifecycle operation for
worktree-backed tasks. Unlike `cleanup.py` (which requires a completed
integration), abandon runs at any lifecycle stage and reclaims the isolated
provider stack, removes code and memory worktrees, deletes task branches, and
removes the worktree group directory.

Successful series abandonment and exact already-abandoned terminal replay pass through
`with_terminal_atomic_series_release` after lifecycle locks are gone. Release is conditional on the
selector still naming this exact contract: a paused old series cannot clear a newer master, and
missing/unreadable/different evidence is preserved and reported rather than reconstructed from task
or queue state. Leaves, dry-runs, and blocked abandon results do not mutate the selector.

## Code Commentary

`_abandon_outputs_result` now passes `preview=args.dry_run` into terminal result validation, matching cleanup. A planned worktree or directory removal therefore stays a preview result. Shared preflight and removal owners treat only the external-memory root ledger as disposable; real uncommitted content and unmerged branch commits remain protected unless explicitly forced.

### Logic

`abandon_result(args: WorktreeArgs)` requires explicit approval (or dry-run),
then delegates to four sub-operations: `teardown_worktree_providers` reclaims
Docker containers, networks, and the `provider-runtime/` tree; `_abandon_worktrees`
calls `remove_registered_worktree` with the `force` flag passed through;
`_abandon_branches` calls `_abandon_branch` for the code work branch, memory
work branch, and memory integration branch; `_abandon_directories` removes the
worktree group dir (force-removes with `remove_tree` when `force=True`,
otherwise `remove_empty_dir`).

`_abandon_branch` checks for unmerged commits via `git log --oneline
<base>..<branch>`. Without `force` it refuses to delete a branch that has
unmerged commits, recording them in the result under `unmergedCommits` with a
`hint`. With `force` it calls `delete_branch_force` (which uses `git branch
-D`). An already-absent branch is always a no-op.

`_abandon_blockers` collects worktrees and branches that are neither removed
nor would-remove — i.e. kept because of a real blocking reason. If any blockers
exist, the contract is not marked `cleanup="abandoned"` and the state is
`"abandon-blocked"`. On a clean run the contract is stamped and state is
`"abandoned"`. Dry-run yields `"would-abandon"`.

**Terminal result validation (260913-LCA-L8).** `_abandon_outputs_result` and each staged step of
`_abandon_terminal_outputs` pass their outputs to the terminal validator as a `TerminalResult`
rather than as loose keyword collections. Every blockage it can report names its component and a
non-empty reason, and a result item that reports no usable reason is answered in operator language
instead of reaching an operator as `reason: null`. Abandon's own contract is unchanged: a
genuinely blocked abandon still blocks with its own reason, and the dry run still reports
`would-abandon` where the apply reports `abandon-blocked`.

Non-force abandon removes the reserved `<worktree_group>/reports` tree before its empty-group check, so
the operational curator checklist cannot keep an otherwise reclaimable enclosure alive. Since
260815-DAG-L10 a series contract's reports tree is the master worktree group's `reports/`
(holding the series operation record/log, citation source-index cache, and Dagger test sandbox),
preserved only when `legacy_series_reports_is_child_enclosure` proves a legacy series contract
(group still recorded as the task enclosure root) shares that path with a child leaf named
`reports`. Force
abandon already removes the complete worktree group and therefore reclaims the same report without
a second deletion path.

Since 260731-EFA-L4 that stamp is
`amend_contract(contract, ContractCells(cleanup="abandoned"))`, not `dataclasses.replace`; the
module no longer imports `replace` at all. `cleanup` is one of the six persisted vocabulary cells,
and typeshed declares `replace` as `**changes: Any`, so `replace(contract, cleanup=<anything>)` was
checked by nothing — including against the wire model that reports the value. The written contract
is unchanged.

### Invariants And Boundaries

- Requires explicit `--approved` or `dry_run`; refuses silently-destructive
  real runs.
- Without `force`, dirty worktrees and unmerged branches are blockers; commits
  are surfaced so the caller can decide whether to lose them.
- With `force`, `git worktree remove --force` and `git branch -D` are used;
  the contract is stamped as abandoned only when no blockers remain.
- Provider teardown runs before worktree/branch removal so the provider stack
  is reclaimed even when Git operations subsequently fail.
- The only report tree this module removes independently is the contract's
  `<worktree_group>/reports` tree — for a series contract since 260815-DAG-L10 that is the master
  worktree group's reports (`worktrees/<repo>/<master>-ar/reports`), not a task-enclosure child;
  force mode removes it only as part of that same group.
- The contract `cleanup` field is set to `"abandoned"` on success; this value
  causes a subsequent `start` call to recreate rather than reattach. `"abandoned"` is a member of
  `worktree_contract.CleanupStatus`, and the write must go through `ContractCells` /
  `amend_contract` — no `replace` call here may carry a `cleanup=` keyword, because typeshed's
  `**changes: Any` means pyright would check nothing.
- The docstring points at the `l-01-agent-lifecycles` skill's
  read-only/abandon exit as the lifecycle entry that drives this operation.

## Admitted abandon with agent archive (MIK-R76)

`_abandon_reserved` delegates to `terminal_abandon._abandon_with_guard`, which archives the leaf's
recorded agents through `archive_terminal_agents` after terminal admission and before the
destructive outputs. The already-abandoned terminal path also archives before returning, and a
non-empty `agentArchive` report is merged into the result payload. The module keeps its own result,
blocker and contract-stamp behavior.

## Evidence

### Docs References

No external Domain Documentation source is configured for this memory repo.

- Successful abandon and exact terminal replay are wrapped with exact source-pair release. [1]
- The terminal bridge preserves missing, unreadable, or different selection and never clears a newer owner. [2]
No relevant external documentation found.

### Repo-Internal References

- Abandon passes its dry-run flag into terminal result validation. [3]
- Provider teardown is delegated to the provider-runtime teardown function. [4]
- `remove_registered_worktree`, `delete_branch_if_merged`, `delete_branch_force`, and `remove_empty_dir` are reused from cleanup. [5]
- `WorktreeArgs` types the abandon input. [6]
- The closeout registrar exposes `worktree_abandon` with `force` forwarded from the MCP layer. [7]
- Series reports-tree preservation is decided by the legacy child-enclosure guard imported from terminal validation. [8]
- The cleanup vocabulary includes abandoned and reopened as declared terminal/reopen states. [9]
- The typed contract amendment record holds the six optional vocabulary cells. [10]
- The typed amendment helper preserves unspecified cells and applies supplied vocabulary values. [11]

### Cross-Repo References

This file owns no ambient cross-repository authority. Any external-memory repository it reaches remains explicitly contract-addressed.
## 260815-DAG-L4 Authority History, Reconciled By CLIVE

Task-derived integration refs remain mechanically non-ordinary, but final terminal admission is not
a queue-release transaction. For an atomic series, `abandon_result` proves the current child/operation
census and exact archived terminal predecessor, then receives an ephemeral operation-, contract-,
thread-, and context-bound terminal permit. That permit is consumed inside the publication and cannot
be stored or reused. No mutable queue blocker is acquired, released, or consulted as terminal evidence.

## 260821-CLIVE-L1 Lease API Migration

Abandon now acquires the pure contract lifecycle lease and separately calls `require_lifecycle_operation_compatible` while held before terminal publication. Its abandonment behavior is otherwise unchanged; the migration removes reliance on the lease performing an active-operation census.

## 260821-CLIVE-L2 Current Contract

The current source seams include `abandon_result`. The public module consumes closed configured-contract admission and performs its authoritative reread at the existing mutation seam. Destructive terminal cleanup/abandon remains fail closed until external archive proof exists; no inferred locator, raw scan, or compatibility reader is permitted.

### Reconciled Source Evidence

- The current module exposes `abandon_result` at this ownership boundary. [12]

## 260821-CLIVE Archive-Before-Abandon

Abandon now proves terminal/no-ambiguous-operation authority, publishes and reads back the external
archive/receipt, and only then removes providers, worktrees, branches, reports, and the enclosure
root. The archive binds the accepted `force` argument; retry with different input refuses, while an
exact terminal retry/status works after the live root is gone. Atomic series require the ephemeral
terminal release capability, never a persistent queue blocker. Already-abandoned results retain and
surface terminal archive proof.

## Governing Overview

[governing overview](overview.md)
