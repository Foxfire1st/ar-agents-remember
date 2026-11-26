# mcp/src/agents_remember/worktrees/modules/abandon.py

## Purpose

`abandon.py` is the discard-without-integration lifecycle operation for
worktree-backed tasks. Unlike `cleanup.py` (which requires a completed integration), abandon does not require completed integration, retains terminal-worktree admission, and removes any leftover `provider-runtime` directory, removes code and memory worktrees, deletes task branches, removes the worktree group directory, and removes the enclosure generation's outside scratch root.

Successful series abandonment and exact already-abandoned terminal replay pass through
`with_terminal_atomic_series_release` after lifecycle locks are gone. Release is conditional on the
selector still naming this exact contract: a paused old series cannot clear a newer master, and
missing/unreadable/different evidence is preserved and reported rather than reconstructed from task
or queue state. Leaves, dry-runs, and blocked abandon results do not mutate the selector.

## Code Commentary

When abandoning a leaf, both force and ordinary paths keep its own tool-call lines in the master notes before the removal that would delete the enclosure log. A failed keep blocks that removal and reports the reason for retry.

`abandon_result` measures `_landed_work_fact` before its removal path runs. When the recorded code work branch exists, differs from the source branch and is its ancestor, the fact names `on-source-line`, the branch and the line. `_with_landed_work_answer` adds `landedWork` and its sentence only to a successful result; missing branches and refused abandonment gain no such claim. This observation does not bypass terminal admission or dirty/unmerged-work checks.

### Current Contract

Abandon evaluates terminal blockers for dry run as well as apply. A blocked preview returns abandon-blocked/blocked with the original coded blockers rather than would-abandon where the real call refuses. Force keeps its existing discard override; explicit approval, check order and unrecognized fail-closed exceptions retain their owners. Recognized terminal-state failures are answered before mutation, not generalized to every RuntimeError.

Abandon now publishes the admitted contract cleanup result, canonical task stage `abandoned` and mirrored master row through `publish_abandoned_task`. That shared helper plans/validates exact task candidates, publishes stage then contract under `guard.complete`, and restores both if its publication fails; returned projection effects are included in the result. The no-remains route checks `plan_task_stage` before directory teardown and reports the typed task-stage refusal rather than beginning destructive work with invalid task authority. This is an ownership/publication boundary, not permission to call abandon from documentation.

`_abandon_outputs_result` now passes `preview=args.dry_run` into terminal result validation, matching cleanup. A planned worktree or directory removal therefore stays a preview result. Shared preflight and removal owners treat only the external-memory root ledger as disposable; real uncommitted content and unmerged branch commits remain protected unless explicitly forced.

### Logic

`_abandon_result(args: WorktreeArgs)` requires explicit approval (or dry-run), then runs admitted outputs through `terminal_abandon._abandon_with_guard` and `_abandon_terminal_outputs`: `prepare_terminal_group` previews folder and move-out blockers, closes recorded task seats, and runs move-out (role reports, any real `messages` directory, and leaf tool-call lines); `_abandon_worktrees` calls `remove_registered_worktree` with `force`; `_abandon_branches` calls `_abandon_branch` for code and carried memory work branches; and `remove_terminal_group` removes the entire `worktree_group` folder (including any leftover `provider-runtime/` directory without a provider teardown step) and recorded outside scratch root on both leaf (forced or not) and modern series paths (keeping `legacy_series_directories` only for a legacy series whose `worktree_group` equals `<task_root>/enclosures`), while `abandon_result` wraps the answer with `with_outside_scratch_reconcile`. `_abandon_directories` is retained only for the directory-only sprint-archive hook (`task_sprint_archive.py`).

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
> genuinely blocked abandon still blocks with its own reason, and the dry run reports
> a terminal-preflight blockage rather than promising `would-abandon` where the apply refuses.

Both forced and non-forced leaf abandon, as well as modern series abandon, remove the entire `worktree_group` folder in full through `terminal_group.remove_terminal_group` after move-out, with no empty-directory check. Only a legacy series contract whose `worktree_group` equals `<task_root>/enclosures` uses `legacy_series_directories` and preserves a colliding child leaf enclosure named `reports` through `legacy_series_reports_is_child_enclosure`.

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
- Folder removal stays contract-addressed: leaf (forced or not) and modern series abandon move out
  reports, real `messages`, and leaf tool calls before removing the whole `worktree_group`; only a
  legacy series preserves a colliding child enclosure named `reports`.
- The contract `cleanup` field is set to `"abandoned"` on success; this value
  causes a subsequent `start` call to recreate rather than reattach. `"abandoned"` is a member of
  `worktree_contract.CleanupStatus`, and the write must go through `ContractCells` /
  `amend_contract` — no `replace` call here may carry a `cleanup=` keyword, because typeshed's
  `**changes: Any` means pyright would check nothing.
- The docstring points at the `l-01-agent-lifecycles` skill's
  read-only/abandon exit as the lifecycle entry that drives this operation.

## Admitted abandon with agent archive (MIK-R76)

`_abandon_reserved` delegates to `terminal_abandon._abandon_with_guard`, which runs `prepare_terminal_group` after terminal admission and before destructive outputs to preview folder removal, close recorded leaf or series seats through `archive_terminal_agents`, block abandon (`abandon-blocked`) if any seat or move-out/directory blocker remains, and move out preserved files. `_already_abandoned` delegates residue reclamation and seat checks to `retry_terminal_group` (`terminal_retry.py`), merging any non-empty `agentArchive` report into the result payload.

## Evidence

### Docs References

No external Domain Documentation source is configured for this memory repo.


> Retained earlier citation wording: - Successful abandon and exact terminal replay are wrapped with exact source-pair release.

- The terminal bridge preserves missing, unreadable, or different selection and never clears a newer owner. [2]
No relevant external documentation found.

### Repo-Internal References



- Abandon passes its dry-run flag into terminal result validation. [3]

- `remove_registered_worktree` (from cleanup), `delete_branch_if_merged`, `delete_branch_force` (from `terminal_branch_retirement`), and `remove_empty_dir` are reused through the terminal owners. [5]

- `remove_registered_worktree` (from cleanup), `delete_branch_if_merged`, `delete_branch_force` (from `terminal_branch_retirement`), and `remove_empty_dir` are reused through the terminal owners. [13]


> Retained earlier citation wording: - `remove_registered_worktree` (from cleanup), `delete_branch_if_merged`, `delete_branch_force` (from `terminal_branch_retirement`), and `remove_empty_dir` are reused through the terminal owners.


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

> Retained earlier citation wording: - Abandon evaluates terminal blockers for dry run as well as apply. A blocked preview returns abandon-blocked/blocked with the original coded blockers rather than would-abandon where the real call refuses. Force keeps its existing discard override; explicit approval, check order and unrecognized fail-closed exceptions retain their owners. Recognized terminal-state failures are answered before mutation, not generalized to every RuntimeError. [16]



- No-remains abandon validates task-stage authority before teardown. [17]


> Retained earlier citation wording: - The normal publication returns shared task/contract projection effects. [18]

- One shared owner publishes/restores task stage and contract under the terminal guard. [19]

## 260928-MIK-L198 — Abandon removes the root and records its completion

`abandon_result` is now a wrapper that returns `with_outside_scratch_reconcile(_abandon_result(args), dry_run=args.dry_run)`, so an abandon run also sweeps the product parent and carries `outsideScratchReconcile` when the sweep removed or reported a root. `terminal_group.py` publishes `outside_scratch.removal_entry_for(contract, dry_run=dry_run)` under the `outside_scratch` key for both leaf and series abandon paths (`_abandon_directories` keeps it for the directory-only sprint-archive helper). `_already_abandoned` takes `dry_run` and delegates residue reclamation to `retry_terminal_group`; any remaining blocker returns return code 2 with state `abandon-blocked`, summary "Abandon is already recorded but its task resources could not be removed.", `directories`, `blockers`, and optional `agentArchive` or `outsideScratch`. After the abandoned contract and task row are published and read back, `_publish_abandon` calls `write_completion_record(contract, updated, operation="worktree_abandon")`.


- Successful abandon and exact terminal replay retain terminal atomic-series release in their admitted paths. The outer wrapper reconciles outside scratch and attaches a successful ancestry-based landed-work observation. Anchor: `abandon_result` [1]

- The typed amendment helper preserves unspecified cells and applies supplied vocabulary values. [11]

- The current module exposes `abandon_result` at this ownership boundary.  Anchor: `abandon_result` [12]



- `remove_registered_worktree` (from cleanup), `delete_branch_if_merged` and `delete_branch_force` (from `terminal_branch_retirement`), and `remove_terminal_group` (from `terminal_group`) are reused through the terminal owners; `remove_empty_dir` remains only for `_abandon_directories`. [14]



- Abandon evaluates terminal blockers for dry run as well as apply. A blocked preview returns abandon-blocked/blocked with the original coded blockers rather than would-abandon where the real call refuses. Force keeps its existing discard override; explicit approval, check order and unrecognized fail-closed exceptions retain their owners. Recognized terminal-state failures are answered before mutation, not generalized to every RuntimeError. [16]



- The normal publication returns shared task/contract projection effects. [18]


- The cleanup vocabulary includes abandoned and reopened as declared terminal/reopen states. [9]



- Both leaf abandon paths preserve the leaf call lines before deleting the folder that contains the log. [21]
