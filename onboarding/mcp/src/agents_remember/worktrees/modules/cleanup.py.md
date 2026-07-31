# mcp/src/agents_remember/worktrees/modules/cleanup.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/worktrees/modules/cleanup.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-31T00:00+02:00     |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d` |
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

Owns post-integration cleanup of registered worktrees, merged task branches,
worktree-owned observer drift snapshots, and empty worktree folders.

## Code Commentary

`cleanup_result` takes the typed `WorktreeArgs` dataclass (imported from
`agents_remember.worktrees.modules.args`), replacing the former
`argparse.Namespace`; it reads `args.approved`, `args.dry_run`,
`args.teardown_providers`, and `args.contract_path`, asserting the latter is
non-`None` before loading the contract. Cleanup requires completed integration
and explicit approval for real mutation.

When `args.teardown_providers` is true (the default), `cleanup_result` calls
`teardown_worktree_providers` first to reclaim the worktree's isolated provider
stack (Docker containers, networks, and the `provider-runtime/` tree) before
removing worktrees and directories. The teardown result is included in the
response under `providers`. When `teardown_providers` is false, a
`{"state": "skipped"}` placeholder is returned.

`remove_registered_worktree` now accepts an optional `force` keyword (default
`False`); when true it passes `--force` to `git worktree remove`. This is used
by `abandon.py` for force discard.

`delete_branch_force` is newly added and uses `git branch -D` to delete an
unmerged branch; it is used by `abandon.py`'s force path.

Cleanup still removes registered code and memory worktrees, removes empty
directories, records cleanup completion in the contract, and reports branches Git
refused to delete (`kept_branches`). Dry-run directory reporting models the
cleanup plan: if the worktree group contains only registered worktrees and the
`provider-runtime/` tree that the same cleanup run has already scheduled for
removal, the preview reports the group as `would_remove` instead of `not-empty`.
`_cleanup_summary` derives the human-facing summary from the computed cleanup
state, so dry-runs (`would-cleanup`) use prospective wording while real cleanup
and idempotent already-clean calls still report completed/already-completed
wording. Real cleanup remains conservative and only removes directories once
they are actually empty after the worktree/provider teardown steps run.

`cleanup_result` blocks (exit 2) while
`provider_async.provider_setup_running(contract)` reports a live background
setup — teardown must not race the setup thread; a dead thread surfaces as a
stale heartbeat and does not block (GitHub #53).

### Slice 05m + Task 14: carryover-before-cleanup hard guard + child-edge work-branch cleanup

**Carryover hard-guard.** `cleanup_result` now refuses (raises `RuntimeError`,
message mentions "carryover") when integration is `completed` but
`guidance.carryover_done(contract)` is false — because cleanup deletes the parked
memory branch that `memory_carryover_apply` reads from, so cleaning up before the
carry would silently discard it. The proof is the OFFICIAL ledger (`carryover_done`,
imported from `guidance`), **not** a contract stamp; `internal`/`disabled` memory has
nothing to carry and passes vacuously.

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
  <branch>` probe → `git push origin --delete`. Honest reasons:
  `empty` / `remote-unreachable` / `already-absent`; `would_delete` on dry-run.

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

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Defines the `WorktreeArgs` dataclass that types the `cleanup_result` input. | [args.py](agents-remember/mcp/src/agents_remember/worktrees/modules/args.py) |
| `cleanup_result` hard-guards on `carryover_done` (imported from here) and reuses `status_payload`. | [guidance.py](agents-remember/mcp/src/agents_remember/worktrees/modules/guidance.py) |
| Integration creates the scratch memory integration branch name that cleanup may remove. | [integrate.py](agents-remember/mcp/src/agents_remember/worktrees/modules/integrate.py) |
| Provider teardown is delegated to this module. | [provider_teardown.py](agents-remember/mcp/src/agents_remember/worktrees/modules/provider_teardown.py) |
| `delete_branch_force` and `remove_registered_worktree(force=...)` are reused by abandon. | [abandon.py](agents-remember/mcp/src/agents_remember/worktrees/modules/abandon.py) |
| The carryover guard, work-branch cleanup, source-branch preservation, remote work-branch deletion, and dry-run directory-plan reporting are pinned here. | [test_cleanup_carryover.py](agents-remember/mcp/tests/test_cleanup_carryover.py) |
| Shared drift snapshot removal helper used by cleanup. | [observer/drift_snapshots.py](agents-remember/mcp/src/agents_remember/observer/drift_snapshots.py) |
| Worktree tests cover cleanup preconditions and completed cleanup state. | [test_worktree_support.py](agents-remember/mcp/tests/test_worktree_support.py) |

## Update History

- 2026-07-31T00:00+02:00 — 260731-EFA-L2 (gate honesty, `PLR0913` armed with no exemptions):
  `_retire_work_branch` was re-signed from `(repo, branch, source_branch, default_branch, dry_run,
  *, remote)` to `(target: RetiringBranch, dry_run, *, remote)`. All three call sites in
  `_deleted_branches` build the `RetiringBranch` from one contract side. Retirement rules, the
  merged-into-source proof and the payload shape are unchanged. Verification metadata pinned until
  closeout stamps the L2 commit.
- 2026-06-27T23:09+02:00 — Task 32 memory-mirror pruning: cleanup now reports/removes the exact observer drift snapshot for the contract's code worktree branch, leaving unrelated snapshots for their own lifecycle. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-24T00:27+02:00 — Corrected cleanup's human summary wording: `would-cleanup` dry-runs now say cleanup would reclaim providers/worktrees/merged branches instead of saying cleanup completed, while real `cleanup-completed` and idempotent `already-clean` states keep completed wording.
- 2026-06-24T00:03+02:00 — Task 14 cleanup correction: cleanup is now a child-edge operation. `_deleted_branches` removes only the finalized task work branches (`code`, `memory`, optional `memory_integration`) after the source-branch ancestry proof, keeps parent/source branches for their own lifecycle edge, removes the `code_source`/`memory_source` payload entries, and deletes the obsolete `_retire_branch(...)` source-retirement helper. The code work branch remote deletion remains available via `delete_remote_branch_if_present`.
- 2026-06-23T15:09+02:00 — Task 13 cleanup correctness: work-branch deletion now uses the contract source branch as the proof target (`merge-base --is-ancestor work_branch source_branch`) before deleting with `git branch -D`, so the ambient checkout (`main` or another branch) no longer decides whether a task branch is safe to remove. Unsafe branches are kept with `not-merged-into-source`. Dry-run directory reporting now subtracts scheduled worktree and provider-runtime removals before deciding whether the worktree group would become empty. At this point, the source-branch retirement path from slice 05m still existed; Task 14 later removed it.
- 2026-06-21T06:40+02:00 — slice 05m (carryover-before-cleanup + work/source branch retirement): (a) `cleanup_result` now HARD-GUARDS — it raises/refuses when integration is completed but `guidance.carryover_done(contract)` is false (external memory), because cleanup deletes the parked memory branch carryover reads from; the "landed" proof is `carryover_done` (we are strictly past it). (b) Added `_repo_default_branch` (local `origin/HEAD` symref), `delete_remote_branch_if_present` (`ls-remote` probe → `git push origin --delete`), and `_retire_branch` (local `-d`, force `-D` when it balks AND landed; never the default branch; switches off a checked-out branch first; optional remote). (c) `_deleted_branches` now retires BOTH the worktree branch AND the (PR'd) source branch — local for code + memory, plus the remote for the code source branch (memory is local-only). (d) `_cleanup_state`/`_kept_branches` treat the intentional `default-or-empty` skip as clean. Rewrote the Code Commentary; added the `guidance.py` + `test_cleanup_carryover.py` references. Verification metadata pinned until closeout stamps the 05m code commit.
- 2026-06-10T07:30+02:00 — `cleanup_result` blocks (exit 2) while `provider_async.provider_setup_running(contract)` reports a live background setup — teardown must not race the setup thread; a dead thread surfaces as a stale heartbeat and does not block (GitHub #53).
- 2026-06-01T00:00+02:00 — `cleanup_result` now conditionally calls `teardown_worktree_providers` via the new `args.teardown_providers` flag (default true); `remove_registered_worktree` gained an optional `force` keyword; `delete_branch_force` added. Updated Code Commentary and added provider teardown + abandon cross-references.
- 2026-05-31T12:50+02:00 — `cleanup_result` arg re-typed from `argparse.Namespace` to the new `WorktreeArgs` dataclass (imported from `modules.args`) with an `args.contract_path is not None` assert; corrected Code Commentary to name the typed param and added the args.py reference (1.0.0 review remediation).
- 2026-05-25T20:41+02:00: Created during worktree manager module extraction.
