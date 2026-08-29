# mcp/src/agents_remember/worktrees/modules/cleanup.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/worktrees/modules/cleanup.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated | 2026-08-29T17:23+02:00 |
| lastVerifiedCommitHash | `60e429d17e9fcbca3ab1c02563afcaa5761b8c5a` |
| lastVerifiedCommitDate | 2026-08-29T20:33:10+02:00|
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

Successful series cleanup, including an exact already-completed retry reconstructed from the
terminal archive, is wrapped by `with_terminal_atomic_series_release` after terminal lifecycle
locks are gone. The bridge releases the source-pair selector only when it still names this exact
series contract. Vacant/missing or a newer different selection is preserved; malformed selector
evidence is reported rather than replaced by queue/task inference. A durable release failure turns
the result into a retryable nonzero response so the canonical terminal contract/receipt remains the
address for another exact attempt. Leaves and dry-runs do not mutate activation.

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
refused to delete (`kept_branches`). Since 260731-EFA-L4 that completion stamp is
`amend_contract(contract, ContractCells(cleanup="completed"))` on a real run (dry-run leaves the
contract untouched, as before) — `dataclasses.replace` is no longer imported for it. `cleanup` is
one of the six persisted vocabulary cells, and typeshed declares `replace` as `**changes: Any`, so
`replace(contract, cleanup=<anything>)` was checked by nothing, including against the wire model
that reports the value. The written contract is unchanged. Dry-run directory reporting models the
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
memory branch before its exact landed mapping has been proven on the named source.
The proof is the OFFICIAL ledger (`carryover_done`,
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
  <branch>` probe → `git push origin --delete` (the push is split out into
  `_push_branch_deletion`). Honest reasons:
  `empty` / `remote-unreachable` / `already-absent`; `would_delete` on dry-run.

**Both remote calls are bounded (260731-EFA-L3).** They are the only two network-talking
git commands in this module, and they run inside an MCP tool call the client cannot
cancel; the module-local runner they used to go through set no timeout at all, so an
unreachable or wedged remote held the tool call open indefinitely. `_remote_git(repo,
args)` now wraps both:

```python
def _remote_git(repo: Path, args: list[str]) -> subprocess.CompletedProcess[str] | None:
    try:
        return run_git(repo, args, timeout=GIT_REMOTE_TIMEOUT_SECONDS)
    except subprocess.TimeoutExpired:
        return None
```

`GIT_REMOTE_TIMEOUT_SECONDS` (120s, from `kernel.git_command`) is the remote band —
deliberately tighter than the 300s local default every other `run_git` call in this file
takes, because bytes either move or the connection is wedged. A stall returns `None`,
and both call sites fold that into the reason the caller already handles:
`probe is None or probe.returncode != 0` → `remote-unreachable` in
`delete_remote_branch_if_present`, and `res is None` → `remote-unreachable` in
`_push_branch_deletion`. So a hung remote reads exactly like an unreachable one and
never escapes as an exception; the payload shape and every reason string are unchanged.

Everything else in this module (`worktree remove`, `branch -d`/`-D`,
`symbolic-ref`, `branch --show-current`, `checkout`) calls the shared
`kernel.git_command.run_git` with no `timeout=`, i.e. the 300-second local class, and
with the `GIT_DIR`-family environment scrub the module-local runner never had.

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

**Enclosure report cleanup.** Before testing whether the worktree group is empty,
`_removed_directories` removes the exact reserved `<worktree_group>/reports` tree. Since
260815-DAG-L10 a series contract's group is the master worktree group
(`worktrees/<repo>/<master>-ar`), so the series sweep reclaims the operation record/log, the
citation source-index cache, and the Dagger test sandbox that land under it; the tree is
preserved only when `legacy_series_reports_is_child_enclosure` proves a legacy series contract
(group still recorded as the task enclosure root) shares that path with a child leaf enclosure
named `reports`. Dry-run adds
that prospective removal to the same planned-path model used for worktrees/provider runtime, so a
group containing only scheduled paths and the curator checklist correctly reports
`would_remove`. No other task or coordination report directory is pruned.

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Successful cleanup and exact terminal replay pass through the terminal activation-release bridge. | `cleanup_result` | mcp/src/agents_remember/worktrees/modules/cleanup.py:635-710 |
| The bridge releases only an exact selected series and reports durable release failure. | `with_terminal_atomic_series_release` | mcp/src/agents_remember/worktrees/activation/atomic_series_activation_terminal.py:17-65 |
| Defines the `WorktreeArgs` dataclass that types the `cleanup_result` input. | "class WorktreeArgs" | mcp/src/agents_remember/worktrees/modules/args.py:32-32 |
| `cleanup_result` hard-guards on `carryover_done` (imported from here) and reuses `status_payload`. | "def carryover_done" | mcp/src/agents_remember/worktrees/modules/guidance.py:191-191 |
| Series reports-tree preservation is decided by the legacy child-enclosure guard imported from terminal validation. | `legacy_series_reports_is_child_enclosure` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:73-84 |
| Terminal mutation capability binds every removable worktree and local/remote branch to the validated contract before cleanup delegates to the lowest writers. | `_terminal_mutation_authority` | mcp/src/agents_remember/worktrees/modules/cleanup.py:77-115 |
| Provider teardown is delegated to this module. | `teardown_worktree_providers` | mcp/src/agents_remember/application/provider_runtime.py:161-180 |
| `delete_branch_force` and `remove_registered_worktree(force=...)` are reused by abandon. | "def _abandon_branches" | mcp/src/agents_remember/worktrees/modules/abandon.py:489-489 |
| The carryover guard, work-branch cleanup, source-branch preservation, remote work-branch deletion, and dry-run directory-plan reporting are pinned here. | `CleanupCarryoverGuardTests` | mcp/tests/test_cleanup_carryover.py:331-346 |
| Shared drift snapshot removal helper used by cleanup. | `remove_drift_snapshot` | mcp/src/agents_remember/kernel/primitives/drift_snapshot.py:27-35 |
| `run_git` plus `GIT_REMOTE_TIMEOUT_SECONDS`, the remote timeout class `_remote_git` passes. | `GIT_REMOTE_TIMEOUT_SECONDS` | mcp/src/agents_remember/kernel/git_command.py:72-72 |
| `CleanupStatus`, `ContractCells` and `amend_contract` — the vocabulary the `completed` stamp belongs to and the typed write it takes. | `amend_contract` | mcp/src/agents_remember/worktrees/worktree_contract.py:198-226 |
| Worktree tests cover cleanup preconditions and completed cleanup state. | `WorktreeSupportTests` | mcp/tests/test_worktree_support.py:807-882 |
| Cleanup tests prove both real and dry-run removal of the enclosure's exact curator reports directory. | `test_cleanup_removes_child_branches_and_preserves_parent_sources`; `test_worktree_group_would_remove_when_only_scheduled_paths_remain` | mcp/tests/test_cleanup_carryover.py:437-518; mcp/tests/test_cleanup_carryover.py:588-614 |

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

The current source seams include `remove_registered_worktree`, `delete_branch_if_merged`, `delete_branch_if_merged_into`. The public module consumes closed configured-contract admission and performs its authoritative reread at the existing mutation seam. Destructive terminal cleanup/abandon remains fail closed until external archive proof exists; no inferred locator, raw scan, or compatibility reader is permitted.

### Reconciled Source Evidence

| Finding | Anchor | Source |
| --- | --- | --- |
| The current module exposes `remove_registered_worktree`, `delete_branch_if_merged`, `delete_branch_if_merged_into` at this ownership boundary. | `remove_registered_worktree`; `delete_branch_if_merged`; `delete_branch_if_merged_into` | mcp/src/agents_remember/worktrees/modules/cleanup.py:180-201; mcp/src/agents_remember/worktrees/modules/cleanup.py:204-226; mcp/src/agents_remember/worktrees/modules/cleanup.py:229-265 |

## 260821-CLIVE Archive-Before-Cleanup

Cleanup requires completed integration and any required landed-memory carryover before deleting the
parked branch. It proves terminal/no-ambiguous-operation state, publishes and reads back the exact
external archive/receipt, then performs the destructive tail under terminal authority. The archive
binds `teardown_providers`; only identical retries converge after root deletion. Atomic series use
the ephemeral terminal permit/release seam. Already-completed status returns the retained archive
proof and never reconstructs deleted live state.

## Update History

- 2026-08-29T17:23+02:00 — No content impact: reviewed the Python 3.13 type-alias syntax migration for terminal cleanup outputs and confirmed that the documented cleanup contract is unchanged. Verification remains closeout-owned.

- 2026-08-26T03:37+02:00 — Documented exact post-terminal atomic-series selection release for
  cleanup and idempotent archive replay. A paused series cannot clear a newer selection; queue/task
  state supplies no fallback. Verification remains post-Dagger/closeout-owned.

- 2026-08-24T15:04+02:00 — Cumulative CLIVE curation: merged terminal archival, exact teardown replay, carryover ordering, and atomic terminal authority into cleanup. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: curated against accepted candidate tree `4241908c`; verification metadata remains pinned until governed closeout stamps the landed code commit.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-20T05:12+02:00 — L13 landed-wave refresh: the series closeout-report routing
  commit (0a746c9f) touched this source; card re-verified against the current file, verification
  stamp advanced to 0a746c9f. Body unchanged — the documented contract still holds.


- 2026-08-19T04:05+02:00 — 260815-DAG-L10 curator: the series reports sweep now targets the
  master worktree group's `reports/` tree (series operation log, citation source-index cache,
  Dagger test sandbox), with preservation narrowed to legacy series contracts through the renamed
  `legacy_series_reports_is_child_enclosure` guard; leaf enclosure behavior is unchanged.
  Verification metadata stamped at the landed code commit `e41ea31d`.
- 2026-08-16T00:45+02:00 — Recorded the queue-owned atomic-series terminal permit and corrected cleanup guidance to the exact named-source ledger proof; verification remains closeout-owned.
- 2026-08-15T23:38+02:00 — Reconciled this worktree owner's role in task-derived protected-ref authority, exact named-ref movement, and crash-safe recovery. Verification metadata remains closeout-owned.
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-11T16:54+02:00 — Added exact garbage collection for the reserved enclosure `reports/`
  tree and included it in dry-run empty-directory planning.
- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B22 curator: replaced the ten `n/a`-anchor
  table citations with exact anchors and fixer-generated ranges; exact non-fixing check returns
  zero findings.

- 2026-08-01T09:54+02:00 — 260731-EFA-L4 curator: the `cleanup="completed"` stamp changed mechanism.
  `cleanup_result` now writes `amend_contract(contract, ContractCells(cleanup="completed"))` on a
  real run, the `from dataclasses import dataclass, replace` import dropped `replace`, and
  `ContractCells` / `amend_contract` joined the `worktree_contract` import block. Recorded it and
  why: `cleanup` is one of the six persisted vocabularies, and typeshed types
  `dataclasses.replace`'s `**changes` as `Any`, so the old call was checked by nothing — not by
  pyright and not against the wire model that reports the value. The dry-run branch still leaves the
  contract untouched, and the written contract is unchanged, so nothing else in this card moved: I
  re-verified the carryover hard-guard, `RetiringBranch` retirement, `_remote_git`'s 120s remote
  bound and its `remote-unreachable` folding, the `default-or-empty` clean skip, and the Task 32
  drift-snapshot boundary against the current file. Added the `worktree_contract.py` reference row.
  Verification metadata pinned until closeout stamps the L4 commit.
- 2026-07-31T20:54+02:00 — 260731-EFA-L3 curator: the module lost its import of the local `run_git`
  and now takes `run_git` + `GIT_REMOTE_TIMEOUT_SECONDS` from `kernel.git_command`. Two new symbols
  the commentary did not describe: `_remote_git` (runs a remote-talking git command at the 120s
  remote bound and returns `None` on `subprocess.TimeoutExpired`) and `_push_branch_deletion` (the
  `push origin --delete` half split out of `delete_remote_branch_if_present`). Documented both, why
  the remote band is tighter than the 300s local default the rest of the module takes, and that a
  stall folds into the existing `remote-unreachable` reason so no payload field or reason string
  changed. Verification metadata pinned until closeout stamps the L3 commit.
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

## Governing Overview

[governing overview](overview.md)

## Cross-Repo References

This file owns no ambient cross-repository authority. Any external-memory repository it reaches remains explicitly contract-addressed.
