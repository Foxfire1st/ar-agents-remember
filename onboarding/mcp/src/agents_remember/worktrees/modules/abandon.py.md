# mcp/src/agents_remember/worktrees/modules/abandon.py

## Purpose

`abandon.py` is the discard-without-integration lifecycle operation for
worktree-backed tasks. Unlike `cleanup.py` (which requires a completed integration), abandon runs at any lifecycle stage and reclaims the isolated provider stack, removes code and memory worktrees, deletes task branches, removes the worktree group directory, and removes the enclosure generation's outside scratch root.

Successful series abandonment and exact already-abandoned terminal replay pass through
`with_terminal_atomic_series_release` after lifecycle locks are gone. Release is conditional on the
selector still naming this exact contract: a paused old series cannot clear a newer master, and
missing/unreadable/different evidence is preserved and reported rather than reconstructed from task
or queue state. Leaves, dry-runs, and blocked abandon results do not mutate the selector.

## Code Commentary

### Current Contract

Abandon evaluates provider liveness and terminal blockers for dry run as well as apply. A blocked preview returns abandon-blocked/blocked with the original coded blockers rather than would-abandon where the real call refuses. Force keeps its existing discard override; explicit approval, check order and unrecognized fail-closed exceptions retain their owners. Recognized terminal-state failures are answered before mutation, not generalized to every RuntimeError.

Abandon now publishes the admitted contract cleanup result, canonical task stage `abandoned` and mirrored master row through `publish_abandoned_task`. That shared helper plans/validates exact task candidates, publishes stage then contract under `guard.complete`, and restores both if its publication fails; returned projection effects are included in the result. The no-remains route checks `plan_task_stage` before provider teardown and reports the typed task-stage refusal rather than beginning destructive work with invalid task authority. This is an ownership/publication boundary, not permission to call abandon from documentation.

`_abandon_outputs_result` now passes `preview=args.dry_run` into terminal result validation, matching cleanup. A planned worktree or directory removal therefore stays a preview result. Shared preflight and removal owners treat only the external-memory root ledger as disposable; real uncommitted content and unmerged branch commits remain protected unless explicitly forced.

### Logic

`_abandon_result(args: WorktreeArgs)` requires explicit approval (or dry-run), then delegates to four sub-operations: `teardown_worktree_providers` reclaims Docker containers, networks, and the `provider-runtime/` tree; `_abandon_worktrees` calls `remove_registered_worktree` with the `force` flag passed through; `_abandon_branches` calls `_abandon_branch` for the code work branch, memory work branch, and memory integration branch; `_abandon_directories` removes the worktree group dir (force-removes with `remove_tree` when `force=True`, otherwise `remove_empty_dir`) and the recorded outside scratch root, while `abandon_result` wraps that answer with the outside-scratch reconcile. `_abandon_terminal_outputs` collects group reports before provider teardown, recording a collection failure instead of removing; `_abandon_directories` removes the group's role folders and merges them into the planned-removal set. Non-force leaf removal also removes reserved `logs/`, exposes its result under `directories.logs`, and includes removed/would-remove logs in the empty-group plan. Series removal removes its reserved `logs/` before returning, retains the `reports` and `lifecycle` response keys, and merges the optional `outside_scratch` removal entry when a root is recorded. Both pass `dry_run` through; preview leaves log bytes in place. Force leaf removal reclaims logs as part of the whole group.

`_abandon_branch` checks for unmerged commits via `git log --oneline
<base>..<branch>`. Without `force` it refuses to delete a branch that has
unmerged commits, recording them in the result under `unmergedCommits` with a
`hint`. With `force` it calls `delete_branch_force` (which uses `git branch
-D`). An already-absent branch is always a no-op.

> **Retained historical source account — superseded by the current contract:**
> `_abandon_blockers` collects worktrees and branches that are neither removed
> nor would-remove — i.e. kept because of a real blocking reason. If any blockers
> exist, the contract is not marked `cleanup="abandoned"` and the state is
> `"abandon-blocked"`. On a clean run the contract is stamped and state is
> `"abandoned"`. Dry-run yields `"would-abandon"`.

> **Retained historical source account — superseded by the current contract:**
> **Terminal result validation (260913-LCA-L8).** `_abandon_outputs_result` and each staged step of
> `_abandon_terminal_outputs` pass their outputs to the terminal validator as a `TerminalResult`
> rather than as loose keyword collections. Every blockage it can report names its component and a
> non-empty reason, and a result item that reports no usable reason is answered in operator language
> instead of reaching an operator as `reason: null`. Abandon's own contract is unchanged: a
> genuinely blocked abandon still blocks with its own reason, and the dry run still reports
> `would-abandon` where the apply reports `abandon-blocked`.

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



> Retained earlier citation wording: - Successful abandon and exact terminal replay are wrapped with exact source-pair release. [1]


- The terminal bridge preserves missing, unreadable, or different selection and never clears a newer owner. [2]
No relevant external documentation found.

### Repo-Internal References


- Abandon passes its dry-run flag into terminal result validation. [3]

- Provider teardown is delegated to the provider-runtime teardown function. [4]

- `remove_registered_worktree` (from cleanup), `delete_branch_if_merged`, `delete_branch_force` (from `terminal_branch_retirement`), and `remove_empty_dir` are reused through the terminal owners. [5]


- `remove_registered_worktree` (from cleanup), `delete_branch_if_merged`, `delete_branch_force` (from `terminal_branch_retirement`), and `remove_empty_dir` are reused through the terminal owners. [13]



> Retained earlier citation wording: - `remove_registered_worktree` (from cleanup), `delete_branch_if_merged`, `delete_branch_force` (from `terminal_branch_retirement`), and `remove_empty_dir` are reused through the terminal owners. [14]



- `WorktreeArgs` types the abandon input. [6]


- `WorktreeArgs` types the abandon input. [15]

- The closeout registrar exposes `worktree_abandon` with `force` forwarded from the MCP layer. [7]
- Series reports-tree preservation is decided by the legacy child-enclosure guard imported from terminal validation. [8]


> Retained earlier citation wording: - The cleanup vocabulary includes abandoned and reopened as declared terminal/reopen states. [9]


- The typed contract amendment record holds the six optional vocabulary cells. [10]


> Retained earlier citation wording: - The typed amendment helper preserves unspecified cells and applies supplied vocabulary values. [11]



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



> Retained earlier citation wording: - The current module exposes `abandon_result` at this ownership boundary. [12]



## 260821-CLIVE Archive-Before-Abandon

Abandon now proves terminal/no-ambiguous-operation authority, publishes and reads back the external
archive/receipt, and only then removes providers, worktrees, branches, reports, and the enclosure
root. The archive binds the accepted `force` argument; retry with different input refuses, while an
exact terminal retry/status works after the live root is gone. Atomic series require the ephemeral
terminal release capability, never a persistent queue blocker. Already-abandoned results retain and
surface terminal archive proof.

Rule 5 no-remains exception: with no locator, no worktree folder, no work branches and no recorded outside scratch root still on disk, abandon finishes directly with nothing to archive and nothing to delete, persisting its reason in the surviving contract with a readback. A leaf with uncommitted changes or unlanded branch commits is given up only with `force` and the explicit approval, without a sync of its master.

## Governing Overview

[governing overview](overview.md)


> Retained earlier citation wording: - Abandon evaluates provider liveness and terminal blockers for dry run as well as apply. A blocked preview returns abandon-blocked/blocked with the original coded blockers rather than would-abandon where the real call refuses. Force keeps its existing discard override; explicit approval, check order and unrecognized fail-closed exceptions retain their owners. Recognized terminal-state failures are answered before mutation, not generalized to every RuntimeError. [16]


- No-remains abandon validates task-stage authority before teardown. [17]
> Retained earlier citation wording: - The normal publication returns shared task/contract projection effects. [18]

- One shared owner publishes/restores task stage and contract under the terminal guard. [19]

## 260928-MIK-L198 — Abandon removes the root and records its completion

`abandon_result` is now a wrapper that returns `with_outside_scratch_reconcile(_abandon_result(args), dry_run=args.dry_run)`, so an abandon run also sweeps the product parent and carries `outsideScratchReconcile` when the sweep removed or reported a root. `_abandon_directories` publishes the root's entry under the `outside_scratch` key through `outside_scratch.removal_entry_for(contract, dry_run=dry_run)` on the series path, the leaf path and the `force` path. `_already_abandoned` now takes `dry_run` and asks `outside_scratch.terminal_blocker`; a root it could not remove returns return code 2 with state `abandon-blocked`, the summary "The worktree is already recorded as abandoned but its outside scratch root could not be removed." and the failure under `blockers`, while a removed or already-absent root is carried as `outsideScratch`. After the abandoned contract and task row are published and read back, `_publish_abandon` calls `write_completion_record(contract, updated, operation="worktree_abandon")`.

- Successful abandon and exact terminal replay are wrapped with exact source-pair release.  Anchor: `abandon_result` [1]


- The typed amendment helper preserves unspecified cells and applies supplied vocabulary values. [11]


- The current module exposes `abandon_result` at this ownership boundary.  Anchor: `abandon_result` [12]


- `remove_registered_worktree` (from cleanup), `delete_branch_if_merged`, `delete_branch_force` (from `terminal_branch_retirement`), and `remove_empty_dir` are reused through the terminal owners. [14]


- Abandon evaluates provider liveness and terminal blockers for dry run as well as apply. A blocked preview returns abandon-blocked/blocked with the original coded blockers rather than would-abandon where the real call refuses. Force keeps its existing discard override; explicit approval, check order and unrecognized fail-closed exceptions retain their owners. Recognized terminal-state failures are answered before mutation, not generalized to every RuntimeError. [16]


- The normal publication returns shared task/contract projection effects. [18]


- The cleanup vocabulary includes abandoned and reopened as declared terminal/reopen states. [9]
