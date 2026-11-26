# mcp/src/agents_remember/worktrees/modules/cleanup.py

## Purpose

Owns post-integration cleanup of registered worktrees, merged task branches,
worktree-owned observer drift snapshots, the task folder (`worktree_group`), and the enclosure generation's outside scratch root. Before deleting a modern task folder in full through `terminal_group.py`, cleanup moves out role reports, any real `messages` directory, and a leaf's own tool-call lines (copied to the master's notes without `detail` links); a keep failure records `tool-calls-not-kept` and blocks before deletion. The cleanup call's own line goes to the coordination root.

## Code Commentary

### Current Contract

Cleanup preserves its check order and no-remains handling. Dry and real calls both return blocked/coded answers for live provider setup or terminal blockers. Incomplete integration returns integration-incomplete with worktree_record_landing guidance for a series and worktree_integrate guidance for a leaf; a recognized missing carryover returns carryover-required. Cleanup gains no force override from shared blocker wording. The archive-ready kept_line=None/no-rejudgment/no-invented-landedTips policy is now owned by _cleanup_terminal_branch and returned to cleanup_result; its earlier failure narrative is historical. Unrecognized exceptions remain named failures.

The contract-derived terminal mutation authority identifies the external-memory checkout separately. `remove_registered_worktree` discards changes to its root ledger cache through the shared cache owner before ordinary Git removal. No force flag is added for cache handling. Code files named `memory.md`, other memory paths and branch-ancestry safeguards retain their normal protection.

`_cleanup_result` takes the typed `WorktreeArgs` dataclass (imported from `agents_remember.worktrees.modules.args`), replacing the former `argparse.Namespace`; it reads `args.approved`, `args.dry_run`, `args.teardown_providers` and `args.contract_path`, asserting the latter is non-`None` before loading the contract, while `cleanup_result` is the wrapper that adds the outside-scratch reconcile around it. Cleanup requires completed integration
and explicit approval for real mutation.

Successful series cleanup, including an exact already-completed retry reconstructed from the
terminal archive, is wrapped by `with_terminal_atomic_series_release` after terminal lifecycle
locks are gone. The bridge releases this contract's own activation record only when it still names
that exact series contract. Vacant/missing or a newer different activation is preserved; malformed
selector evidence is reported rather than replaced by queue/task inference. A durable release failure turns
the result into a retryable nonzero response so the canonical terminal contract/receipt remains the
address for another exact attempt. Leaves and dry-runs do not mutate activation.

When `args.teardown_providers` is true (the default), cleanup calls
`teardown_terminal_providers` first to reclaim the isolated provider
stack (skipping symlinked provider state outside the task folder) before
removing worktrees and the task folder, reporting the outcome under `providers`.
When `teardown_providers` is false, a
`{"state": "skipped", "reason": "teardown_providers disabled"}` entry is returned,
and any `provider-runtime/` directory that still holds provider state blocks
cleanup before deletion.

`remove_registered_worktree` now accepts an optional `force` keyword (default
`False`); when true it passes `--force` to `git worktree remove`. This is used
by `abandon.py` for force discard.

`delete_branch_force` is newly added and uses `git branch -D` to delete an
unmerged branch; it is used by `abandon.py`'s force path.

> **Retained historical source account — superseded by the current contract:**
> Cleanup still removes registered code and memory worktrees, removes empty
> directories, records cleanup completion in the contract, and reports branches Git
> refused to delete (`kept_branches`). Since 260731-EFA-L4 that completion stamp is
> `amend_contract(contract, ContractCells(cleanup="completed"))` on a real run (dry-run leaves the
> contract untouched, as before) — `dataclasses.replace` is no longer imported for it. `cleanup` is
> one of the six persisted vocabulary cells, and typeshed declares `replace` as `**changes: Any`, so
> `replace(contract, cleanup=<anything>)` was checked by nothing, including against the wire model
> that reports the value. The written contract is unchanged. Dry-run directory reporting models the
> cleanup plan: if the worktree group contains only registered worktrees and the
> `provider-runtime/` tree that the same cleanup run has already scheduled for
> removal, the preview reports the group as `would_remove` instead of `not-empty`.
> `_cleanup_summary` derives the human-facing summary from the computed cleanup
> state, so dry-runs (`would-cleanup`) use prospective wording while real cleanup
> and idempotent already-clean calls still report completed/already-completed
> wording. Real cleanup remains conservative and only removes directories once
> they are actually empty after the worktree/provider teardown steps run.

`cleanup_result` blocks (exit 2) while
`provider_async.provider_setup_running(contract)` reports a live background
setup — teardown must not race the setup thread; a dead thread surfaces as a
stale heartbeat and does not block (GitHub #53).

> **Retained historical source account — superseded by the current contract:**
> **Terminal result validation (260913-LCA-L8).** `_cleanup_outputs_result` builds a `TerminalResult`
> from the operation's five output collections and passes `preview=args.dry_run`; that flag is what
> keeps a dry run's `would_remove` entries from being read as blockages, because a preview states what
> cleanup would reclaim rather than what it did. `_cleanup_terminal_outputs` stages each successive
> step's outputs through the same bundle without the flag, since each of those checks runs only on a
> real cleanup. Every blockage the builder emits now names its component and carries a non-empty
> reason, and a result item that reports no usable reason is answered in operator language instead of
> reaching an operator as `reason: null`. The cleanup contract itself is unchanged: a genuinely
> blocked cleanup still blocks with its own reason, and a dry run still reports `would-cleanup` where
> the apply reports `cleanup-blocked`.

### Slice 05m + Task 14: carryover-before-cleanup hard guard + child-edge work-branch cleanup

> **Retained historical source account — superseded by the current contract:**
> **Carryover hard-guard.** `cleanup_result` now refuses (raises `RuntimeError`,
> message mentions "carryover") when integration is `completed` but
> `guidance.carryover_done(contract)` is false — because cleanup deletes the parked
> memory branch before its exact landed mapping has been proven on the named source.
> Current `carryover_done` proves the actual memory commit against named source history. The computed ledger file has no admission role; a disabled-memory contract has no memory worktree to carry and passes vacuously. (The source comment was reworded by `CAPS-R12@v1` from the removed "internal/disabled" pairing to the supported set; the behaviour is unchanged, and the removed `internal` mode is no longer named here.)

**Branch cleanup** operates on the just-finalized child edge only. It removes task
work branches after proving they are reachable from the contract's corresponding
source branches; parent/source branches are the next node up the task tree and are
finalized/cleaned by their own lifecycle edge. Helpers:

- `_repo_default_branch(repo)` — the repo's default branch (e.g. `main`) from the local
  `origin/HEAD` symref (`git symbolic-ref --short refs/remotes/origin/HEAD`), falling
  back to `"main"`; used only to refuse ever deleting the default branch if a contract
  accidentally names it as a work branch.
- `delete_remote_branch_if_present(repo, branch, dry_run)` — clears `origin/<branch>`
  when the code work branch still has a remote ref: `git ls-remote --heads origin
  <branch>` probe → `git push origin --delete` (the push is split out into
  `_push_branch_deletion`). Honest reasons:
  `empty` / `remote-unreachable` / `already-absent`; `would_delete` on dry-run.

**Both remote calls are bounded (260731-EFA-L3).** They are the only two network-talking
git commands on the terminal path, owned since the extraction by `terminal_branch_retirement.py`,
and they run inside an MCP tool call the client cannot
cancel; the module-local runner they used to go through set no timeout at all, so an
unreachable or wedged remote held the tool call open indefinitely. `_remote_git(repo,
args)` now wraps both:

```python
def _remote_git(repo: Path, args: list[str]) -> subprocess.CompletedProcess[str] | None:
    try:
        return run_git(repo, args, GitRunnerOptions(timeout=GIT_REMOTE_TIMEOUT_SECONDS))
    except subprocess.TimeoutExpired:
        return None
```

`GIT_REMOTE_TIMEOUT_SECONDS` (120s, from `kernel.git_command`) is the remote band —
deliberately tighter than the 300s local default the remaining `run_git` call in this file
takes, because bytes either move or the connection is wedged. A stall returns `None`,
and both call sites fold that into the reason the caller already handles:
`probe is None or probe.returncode != 0` → `remote-unreachable` in
`delete_remote_branch_if_present`, and `res is None` → `remote-unreachable` in
`_push_branch_deletion`. So a hung remote reads exactly like an unreachable one and
never escapes as an exception; the payload shape and every reason string are unchanged.

The remaining local call in this module is `worktree remove`, which calls the shared
`kernel.git_command.run_git` with no options object, i.e. the 300-second local class, and
with the `GIT_DIR`-family environment scrub the module-local runner never had. The
`branch -d`/`-D`, `symbolic-ref`, `branch --show-current` and `checkout` shapes the module
once issued locally no longer run here: `branch --show-current` now runs in
`terminal_branch_retirement.py`, and the remote pair above runs through the extracted
`_remote_git` owner.

**Task 13 correction.** Work-branch cleanup no longer relies on Git's ambient
merge target (`HEAD` / upstream) and no longer force-drops task work branches
just because carryover is done. `delete_branch_if_merged_into(repo, branch,
target_ref, dry_run)` first proves `merge-base --is-ancestor <work_branch>
<contract source_branch>`, then deletes with `git branch -D`; the force delete is
safe by construction because the explicit source-branch proof already succeeded.
If the proof fails, cleanup keeps the branch with reason
`not-merged-into-source` and `kept_branches` reports it. `_retire_work_branch(target, dry_run, *,
remote)` uses this rule for `code_work`, `memory_work`, and the scratch memory integration
branch.

Since 260731-EFA-L2 `target` is the frozen **`RetiringBranch(repo, branch, source_branch,
default_branch)`** — one task work branch on its way out: the repo it lives in, the branch itself,
the source branch it must be proven merged into before deletion, and that repo's default branch
(the one to check out when the branch being deleted is currently checked out). Retirement never
consults any of these without the others, and each call site in `_deleted_branches` derives the
whole set from one contract side, so a code-side repo can no longer be paired with a memory-side
source branch by argument order.

**Task 14 correction.** The older source-branch retirement path was removed because
nested dashboard tasks use parent/source branches as their own lifecycle edges. In
that tree, cleaning up a leaf must remove only the leaf's work branch; deleting the
parent/source branch would prematurely remove the next edge up. `_deleted_branches`
therefore returns only `code`, `memory`, and optional `memory_integration` entries.
The old `code_source`/`memory_source` payload entries and `_retire_branch(...)`
helper are gone.

`_cleanup_state` and `_kept_branches` treat the intentional `default-or-empty` skip as
clean: a retire result whose `reason` is `default-or-empty` (the default branch was
deliberately not deleted) counts toward `already-clean` and is excluded from
`kept_branches` (it is not a branch Git refused — it is one we declined to touch).

**Task 32 drift snapshot cleanup.** `cleanup_result` also calls
`remove_drift_snapshot(contract.coordination_root, repository=contract.code_worktree.name,
branch=contract.code_work_branch, dry_run=args.dry_run)` and includes the result under
`drift_snapshots["code"]`. Dry-runs report the exact snapshot that would be removed.
Real cleanup deletes only that contract-owned code-worktree snapshot; unrelated snapshots
remain for their own cleanup or projection-time orphan pruning. The deletion boundary is
exact to the contract's code worktree name and work branch; cleanup must not broadly prune
other snapshots from this path.

**Task-folder move-out and whole-folder removal.** Directory preview and removal are owned by `terminal_group.py` (`prepare_terminal_group`, `preview_group_removal`, `remove_terminal_group`); `_removed_directories` and the empty-directory check are gone. Before destructive work begins, `prepare_terminal_group` previews directory and move-out blockers (including symlink/writability checks and `provider-runtime/` when `teardown_providers=False`), closes recorded task seats, and moves out role reports, any real `messages` directory, and leaf tool-call lines. After worktrees, branches, and drift snapshots clear, `remove_terminal_group` re-runs report and tool-call collection, removes outside scratch and request locators, and removes the entire `worktree_group` folder in full for both leaf and modern series contracts (preserving the `reports`/`logs` summary rows). Only a legacy series whose `worktree_group` equals `<task_root>/enclosures` keeps subfolder removal via `legacy_series_directories` and preserves a colliding child `reports` enclosure through `legacy_series_reports_is_child_enclosure`.

## Admitted cleanup with agent archive (MIK-R76)

`_cleanup_reserved` delegates to `terminal_cleanup._cleanup_with_guard`, which calls `prepare_terminal_group` after terminal admission and before destructive outputs to preview folder removal, close recorded leaf or series seats through `archive_terminal_agents`, block if any seat or move-out/directory blocker remains, and complete move-out before deletion. `_already_completed_cleanup` delegates to `retry_terminal_group` (`terminal_retry.py`), which re-checks generation, remaining checkouts, seats, and move-out/directory blockers before retrying removal; any non-empty `agentArchive` report is merged into the result payload.

## 260928-MIK-L129 — a repeated cleanup carries no rejudged record on the archived contract

> **Retained historical source account — superseded by the current contract:**
> `cleanup_result` set `kept_line` only on the branch without a terminal archive, but passed it to
> `_cleanup_reserved` on every path. A repeat admitted by an archive-ready terminal authority (the
> archived contract, the same operation and arguments, a state other than `cleanup-completed`) reached
> the shared tail with `kept_line` unbound and raised `UnboundLocalError`, unless the provider or the
> preflight check returned first. That state is what an interrupted cleanup leaves behind, and the
> repeat is the only supported way out of it.

> **Retained historical source account — superseded by the current contract:**
> The R1 repair superseded the first recompute attempt per the Parent ruling
> L129-THE-GATE-IS-NOT-JUDGED-AGAIN: on the archive branch the gate is not judged again.
> `TerminalEnclosureArchive` declares no kept-line record of that judgement and forbids extra fields,
> so the repeat carries `kept_line = None`; its answer may lack `landedTips` but invents none.
> `kept_line` flows only to the optional `landedTips` attach, which nothing else consumes, so the
> repeat needs no record. Re-evaluating live carryover evidence on replay would strand cleanups whose
> branches the accepted first run already retired, contrary to rule 2. The completed-cleanup and
> argument-mismatch early returns, the first-run gate, the check and refusal order and texts, the
> no-remains path and closed-agent archiving are unchanged.

## Evidence

### Docs References

No external Domain Documentation source is configured for this memory repo.

### Repo-Internal References

- The authorized memory target clears its disposable cache before ordinary Git removal. [1]

- The bridge releases only an exact selected series and reports durable release failure. [3]


- Defines the `WorktreeArgs` dataclass that types the `cleanup_result` input. [4]


- **Retained historical source account — superseded by the current contract:** `cleanup_result` hard-guards on `carryover_done` (imported from here) and reuses `status_payload`. [5]
- **Retained historical source account — superseded by the current contract:** Series reports-tree preservation is decided by the legacy child-enclosure guard imported from terminal validation. [6]

> Retained earlier citation wording: - **Retained historical source account — superseded by the current contract:** Terminal mutation capability binds every removable worktree and local/remote branch to the validated contract before cleanup delegates to the lowest writers. [7]

- **Retained historical source account — superseded by the current contract:** Provider teardown is delegated to this module. [8]


> Retained earlier citation wording: - `delete_branch_force` and `remove_registered_worktree(force=...)` are reused by abandon. [9]


- Shared drift snapshot removal helper used by cleanup. [10]

- `_remote_git` runs both remote-talking calls with `run_git` plus `GIT_REMOTE_TIMEOUT_SECONDS`, passed as `GitRunnerOptions(timeout=...)`. [11]




- `CleanupStatus`, `ContractCells` and `amend_contract` — the vocabulary the `completed` stamp belongs to and the typed write it takes. [12]





> Retained earlier citation wording: - `CleanupStatus`, `ContractCells` and `amend_contract` — the vocabulary the `completed` stamp belongs to and the typed write it takes. [17]



- The bundle the cleanup outputs are validated through, and the builder that refuses a blockage with no reason. [13]


- The forced L6-shape case: an already torn-down provider runtime finalizes on the first call, and a provider runtime that cannot be removed blocks with its own reason. [14]

- Worktree tests cover cleanup preconditions and completed cleanup state. [15]

### Cross-Repo References

This file owns no ambient cross-repository authority. Any external-memory repository it reaches remains explicitly contract-addressed.


> Retained earlier citation wording: - **Retained historical source account — superseded by the current contract:** A cleanup repeated after its terminal archive was written carries no rejudged record: the archive-ready branch binds `kept_line = None` and invents no `landedTips`.

- **Retained historical source account — superseded by the current contract:** The dry-run repeat of an archive-ready cleanup finishes with no invented `landedTips`. [23]
- **Retained historical source account — superseded by the current contract:** The real-run and branch-gone repeats complete the contract and the terminal authority re-reads `cleanup-completed`. [24]

> Retained earlier citation wording: - **Retained historical source account — superseded by the current contract:** Successful cleanup and exact terminal replay pass through the terminal activation-release bridge.


## 260815-DAG-L4 Authority History, Reconciled By CLIVE

Task-derived integration refs remain mechanically non-ordinary, but final terminal admission is not
a queue-release transaction. For an atomic series, `cleanup_result` proves current child retirement,
operation compatibility, and the exact archived terminal predecessor, then receives an ephemeral
operation-, contract-, thread-, and context-bound terminal permit. The permit expires with the
publication; no mutable queue blocker supplies cleanup authority. Leaf deletion targets remain
strictly contract-derived.

## 260821-CLIVE-L1 Lease API Migration

Cleanup now treats the contract lease as serialization only and invokes `require_lifecycle_operation_compatible` explicitly while held before terminal publication. Cleanup semantics are otherwise unchanged; active-operation compatibility no longer hides inside lease acquisition.

## 260821-CLIVE-L2 Current Contract

The current source seams include `remove_registered_worktree`. Branch deletion (`delete_branch_if_merged`, `delete_branch_if_merged_into`) now lives in `terminal_branch_retirement.py` and is called through the terminal owner. The public module consumes closed configured-contract admission and performs its authoritative reread at the existing mutation seam. Destructive terminal cleanup/abandon remains fail closed until external archive proof exists; no inferred locator, raw scan, or compatibility reader is permitted.

### Reconciled Source Evidence


- The current module exposes `remove_registered_worktree` at this ownership boundary; branch deletion is exposed by `terminal_branch_retirement.py`. [16]


- The current module exposes `remove_registered_worktree` at this ownership boundary; branch deletion is exposed by `terminal_branch_retirement.py`. [18]


## 260821-CLIVE Archive-Before-Cleanup

Cleanup requires completed integration and any required landed-memory carryover before deleting the
parked branch. It proves terminal/no-ambiguous-operation state, publishes and reads back the exact
external archive/receipt, then performs the destructive tail under terminal authority. The archive
binds `teardown_providers`; only identical retries converge after root deletion. Atomic series use
the ephemeral terminal permit/release seam. Already-completed status returns the retained archive
proof and never reconstructs deleted live state.

Rule 5 terminal cases: branch retirement primitives moved whole into `terminal_branch_retirement.py`, including the kept-line proof that deletes a work branch whose tip sits on the landing or default line; the no-remains probe moved into `terminal_inventory.py`, shared by cleanup and abandon; a leaf whose contract says completed while its folder or branches still exist is finished by the repeated cleanup, which the citation-cache guard does not refuse for a missing state. `cleanup.py` keeps the terminal authority and delegates task-folder preview and whole-folder removal to `terminal_group.py`.

## Governing Overview

[governing overview](overview.md)

> Retained earlier citation wording: - Cleanup preserves its check order and no-remains handling. Dry and real calls both return blocked/coded answers for live provider setup or terminal blockers. Incomplete integration returns integration-incomplete with worktree_record_landing guidance for a series and worktree_integrate guidance for a leaf; a recognized missing carryover returns carryover-required. Cleanup gains no force override from shared blocker wording. The archive-ready kept_line=None/no-rejudgment/no-invented-landedTips policy is now owned by _cleanup_terminal_branch and returned to cleanup_result; its earlier failure narrative is historical. Unrecognized exceptions remain named failures. [25]

## 260928-MIK-L198 — Cleanup removes the root and sweeps the ended ones

`cleanup_result` is now a thin wrapper that returns `with_outside_scratch_reconcile(_cleanup_result(args), dry_run=args.dry_run)`, so every run also sweeps the product parent and carries `outsideScratchReconcile` on the payload when the sweep removed or reported a root. `terminal_group.py` includes `outside_scratch.removal_entry_for(contract, dry_run=dry_run)` under the `outside_scratch` key on both leaf and series paths, removing the recorded root and reporting `would_remove` on preview. `_already_completed_cleanup` takes `dry_run` and delegates residue reclamation to `retry_terminal_group`; any remaining blocker (task folder, live seat, checkout, or outside scratch root) returns return code 2 with state `blocked`, summary "Cleanup is already recorded but its task resources could not be removed.", `directories`, `blockers`, and optional `agentArchive` or `outsideScratch`. After the completed contract is published and read back, `_publish_cleanup` calls `write_completion_record(contract, updated, operation="worktree_cleanup")`, the completion evidence a successor's sweep reads in place of the contract the group takes away.



- `CleanupStatus`, `ContractCells` and `amend_contract` — the vocabulary the `completed` stamp belongs to and the typed write it takes. [17]







- **Retained historical source account — superseded by the current contract:** Successful cleanup and exact terminal replay pass through the terminal activation-release bridge. Anchor: `cleanup_result` [2]








- **Retained historical source account — superseded by the current contract:** A cleanup repeated after its terminal archive was written carries no rejudged record: the archive-ready branch binds `kept_line = None` and invents no `landedTips`. Anchor: `cleanup_result` [22]







- Cleanup preserves its check order and no-remains handling. Dry and real calls both return blocked/coded answers for live provider setup or terminal blockers. Incomplete integration returns integration-incomplete with worktree_record_landing guidance for a series and worktree_integrate guidance for a leaf; a recognized missing carryover returns carryover-required. Cleanup gains no force override from shared blocker wording. The archive-ready kept_line=None/no-rejudgment/no-invented-landedTips policy is now owned by _cleanup_terminal_branch and returned to cleanup_result; its earlier failure narrative is historical. Unrecognized exceptions remain named failures. [25]




- **Retained historical source account — superseded by the current contract:** Terminal mutation capability binds every removable worktree and local/remote branch to the validated contract before cleanup delegates to the lowest writers.  Anchor: `_terminal_mutation_authority` [7]


- `delete_branch_force` and `remove_registered_worktree(force=...)` are reused by abandon. [9]


- Cleanup keeps leaf call lines through `terminal_group.py` before removing the task folder and carries the keep outcome on `directories.logs`. [27]
