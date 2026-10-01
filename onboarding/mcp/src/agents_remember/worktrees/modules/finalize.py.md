# mcp/src/agents_remember/worktrees/modules/finalize.py

## Governing Overview

[Worktree operation modules overview](overview.md)

## Purpose

Owns the terminal `lifecycle_finalize_task` worktree operation: prove that a
closed task's landed commit is present on the recorded parent source branch,
run (or verify) reclamation, and reconcile task documents to `Completed`.

Since 260831-LOCR-L31 this module is the **only** landing-side route that reclaims. Integration
publishes the landed refs and stops; the terminal reclamation of the enclosure belongs here, which
is what makes the task edge finalization actually reachable.

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

Cleanup is handled as part of the finalization operation, and it is the **only** route that reclaims
an integrated enclosure: `worktree_integrate` lands the refs and stops, so a landed-but-unfinalized
leaf still owns its worktrees, its merged local branches, its reports directory and its enclosure
root. `_run_or_verify_cleanup` is the whole seam
cit:([`_run_or_verify_cleanup`], mcp/src/agents_remember/worktrees/modules/finalize.py:328-362):

- If the contract is already cleaned, the response records `already-completed` without calling
  cleanup at all.
- Otherwise it delegates to `cleanup_result` with `approved=not dry_run` and `teardown_providers`
  carried through.
- The `except RuntimeError` branch is unchanged: a raised cleanup refusal becomes
  `returncode 2` with `state: "blocked"`, which the caller reports as `cleanup-blocked` and which
  leaves task documents untouched. A failed cleanup therefore refuses **before** the task edge closes
  rather than marking a leaf and its master row `Completed` over an enclosure that is still on disk.

**The report is shaped here, and only for a real reclamation (260831-LOCR-L31).** A real,
completed reclamation is passed through
`cleanup_report(contract, result.payload)`
cit:(["cleanup_report(contract, result.payload)"], mcp/src/agents_remember/worktrees/modules/finalize.py:361-361)
— the operator-facing sentence and inventory documented on its own card. The gate in front of that
call is load-bearing in both directions: when `args.dry_run` or `result.returncode != 0`, the cleanup
payload is returned **unchanged**, because a preview lists what cleanup *would* remove (so shaping it
would assert a reclamation that never happened) and a refusal must stay readable in cleanup's own
words, its `blockers` and partial inventory intact. The run-and-catch half that used to own this
reporting (`automatic_cleanup.run_automatic_cleanup`, deleted by this same change) had no caller left
once reclamation moved here.
cit:([`cleanup_report`], mcp/src/agents_remember/worktrees/modules/cleanup_report.py:28-53)

After cleanup and task-truth reconciliation converge, `_finalized_result` performs an idempotent
exact terminal activation release before archiving a root series task. A release failure returns
`activation-release-blocked` with the completed cleanup/task updates so the caller can retry the
same canonical contract. A missing, vacant, unreadable, or different selection is preserved and
reported; a paused old master cannot clear the currently selected one. Successful results carry the
activation observation/release evidence and only then archive a root series task.

**The review-artifact archive hook (MIK-R25 rule 5, D17).** Right after `archive_completed_root_task`,
`_finalized_result` passes the archive result through `_with_review_artifact_cleanup`. For a task that was
`archived` (or `would-archive` on a dry run) it takes the composition-bound `review_artifact_cleanup` port from
`worktree_services()` and calls it with a `ReviewArtifactCleanupRequest`: the task root as it is now (the archive
path once archived), `task_name` = the contract's `task_root.name` (the review-ref namespace, ruling
2026-09-30T02:32:42 (a)), the contract's code and memory repositories, and `dry_run`. Its report is carried as
`taskArchive.reviewArtifacts`. An unbound port reports `state: "not-bound"` rather than "nothing to delete", and
any exception becomes `{state: "failed", detail}`: the task is already archived, so the hook never fails finalize
(review F2, ruling 2026-09-29T23:15:34). The hook itself is `application/review_artifact_cleanup.py`.

Task document reconciliation is edge-scoped. The contract identity resolves the one leaf document
(`task_doc_path` only asserts it) and completes it. The leaf's immediate parent row is derived, never
supplied: the master the leaf names or, for a leaf naming none, its folder's `task.json` by the task-document
master sync's rule (MIK-R38, below). `master_doc_path` plus `subtask_number` are identity assertions that
must match that edge. Only that row becomes `Completed`; the parent task's own status is left unchanged
except that a `Completed` master with an open row is demoted to `inProgress`, and ancestors are not
completed recursively; callers repeat finalization for the next parent-child branch edge. Dry-run returns
`would-update` task-document states without writing files.

## Evidence

### Docs References

No external Domain Documentation source is configured for this memory repo.

### Repo-Internal References

- Final result releases exact terminal selection before root task archival, reports retryable release failure, and carries the review-artifact archive hook's report on an archived (or would-archive) root task (MIK-R25). [1]
- The archive hook is carried for an archived task only; unbound is `not-bound`, and an exception is a `failed` report, never raised. [2]
- Exact terminal release is independent of queue/task scheduling state. [3]
- Cleanup behavior and branch/worktree removal are delegated here. [4]
- The cleanup seam that runs reclamation, short-circuits an already-completed cell, and shapes a real successful reclamation through the report shaper — deliberately not on a dry run or a nonzero return code. [5]
- The operator-facing report shape this module restores for a completed reclamation, and its `already-clean` rule. [6]
- Carryover completion is proven against the official memory ledger here. [7]
- Git ancestry proof uses the worktree module Git adapter. [8]
- Task document JSON/markdown reconciliation uses the task document service. [9]
- Focused tests pin a named master's row completion and two-document rollback and the misplaced-master refusal, and (MIK-R38) the folder master's row under the demotion rule, the dry run, the standalone cases and every refusal before any write. [10]

### Cross-Repo References

No meaningful cross-repository reference applies to this repository-owned terminal operation.

## Series-Contract Notes

Finalization reports `enclosurePath` for the leaf being finalized and only archives completed root tasks when the finalized contract is a root `kind="series"` contract.

## 260815-DAG-L3 Finalization Publication, Replaced By Task CAS

Leaf/master task-document reconciliation no longer publishes through a bound sprint queue.
Finalization validates and writes the exact leaf/parent batch under task CAS; only task-source conflict
can refuse that canonical publication. Projection invalidation/rebuild is a reported downstream
effect and cannot partially govern or roll back task status.

## 260821-CLIVE Finalization Task Publication

Finalization captures exact leaf and parent task-source snapshots during preflight, then validates
them again under the task-publication CAS before publishing the task batch. Accepted task truth is
independent of projection state; the result reports per-sprint `projectionEffects`, and dry-run
previews the same scope without writing. A changed or unreadable source blocks task publication
before bytes move. Projection refresh failure is reported separately and never rolls back an
accepted finalization write.

## 260928-MIK-L38 The Leaf's Master Is Resolved By The Master Sync's Rule

Developer direction D32: a completed leaf must show `Completed` on the master that lists it. Before MIK-R38 this
module called a leaf that names no `master` standalone and skipped its parent (`parent: skipped, leaf has no
immediate parent`), while the task-document master sync (`tasks/master_sync.py`) resolved the same leaf to its
folder's `task.json` and kept that row current. Every 260928-MIK leaf names no master, so 15 finished leaves read
`inProgress` on the master until resync writes repaired them.

- **One rule.** `_resolve_parent_target` dispatches on `leaf.master`. A named master takes `_named_parent`, the old
  sequence unchanged (expected path, the caller's assertions, the read, exactly one row). A leaf naming none takes
  `_folder_parent`, which asks `master_sync.folder_master_json_path`: the folder's `task.json` when the leaf is a
  `subTask` and the file exists, else nothing. Reopen resolves an unnamed leaf through the same helper (ruling
  2026-09-30T12:33:07 Q2), so the three writers of a leaf's master row share one rule.
- **The checks of a named master.** The folder master is read through `_read_parent` (readable, a master, in
  place), must list the leaf exactly once (`_exact_parent_row`), and its row must point at this leaf's file
  (`_check_parent_row_path`); the completed row goes through `demote_completed_master_if_unresolved`. The caller's
  `master_doc_path` and `subtask_number` assertions are checked exactly as for a named master.
- **Standalone as before.** No folder master, or one listing no row for the leaf, leaves the leaf standalone: the
  leaf completes and the parent update reads `skipped` with the reason. A caller that asserts a parent in that
  case is refused with the cause, "folder master … lists no row …; the leaf finalizes standalone" (review R1 note
  4). Finalize never creates a row; the master sync adds one on the leaf's next task-document write. A `light`
  document is itself the folder's `task.json`, so it has no folder master.
- **Refused before cleanup and before any write** (`task-document-resolution-blocked`, return code 2): a folder
  `task.json` that is unreadable (review R1 note 2; base crashed in publication) or not a master (so a `subTask`
  naming none in such a folder is refused, as the master sync refuses its writes; ruling Q4), a master listing the
  leaf twice, a row pointing at another file, and a mismatched assertion.
- **A document the store would write elsewhere is refused** (review R1 finding 1, ruling 2026-09-30T13:11:32; the
  parent side by ruling 13:35:32). The store writes a document by kind and slug (`json_path_for`), never back to
  the path it was read from, so a hand-made `light` leaf `14_x.json` or a hand-made master `other.json` would be
  written over the series `task.json`. `_resolve_task_targets` checks the leaf and `_read_parent` checks every
  master, named or folder, through `tasks/leaf_doc.require_task_document_in_place`. Correctly placed documents
  finalize exactly as before; review R2's read-only sweep of the real task folders (557 sub-tasks, 39 masters)
  refused none. For a named master this is the only behaviour change: a refusal instead of a silent overwrite.
- **A dry run** reports the parent update it would make (`would-update`, the resolved `task.json`, the row
  number), as for a named master.
- `_expected_parent_path` now takes the named reference; its dead `task.md` default, a second copy of the fallback
  that could never run, is gone.

The change is not gated on the memory conversion: once this build is installed, finalize resolves every task
folder this way. Tests: `FolderMasterFinalizeTests` and one `LifecycleFinalizeTests` case, in the integration lane
with the existing finalize cases (ruling Q1). Review R1 passed with notes, R2 passed; the leaf was synced onto L32
(`59daf505`) with a clean 3-way apply, and its finalize, reopen and dependency-ownership tests pass on the synced
tree.

- Parent resolution dispatches on the leaf's `master`; with no target the leaf finalizes standalone, and an asserted parent is refused. [11]
- A named master: expected path, assertions, read, exactly one row. [12]
- A leaf naming none: the master sync's helper, the named-master checks, standalone without a row, and the named cause when a parent was asserted. [13]
- Every master read refuses a non-master and a document the store would write elsewhere; the leaf gets the same check before its parent is resolved. [14]
- The completed row goes through the master demotion rule. [15]
- The one rule for a leaf naming no master, shared with the master sync and reopen. [16]
