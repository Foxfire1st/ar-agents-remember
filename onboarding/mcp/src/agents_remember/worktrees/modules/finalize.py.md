# mcp/src/agents_remember/worktrees/modules/finalize.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/worktrees/modules/finalize.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-30T15:25:16+02:00 |
| lastVerifiedCommitHash | `904e804b07a598d5d6c66f06b7e67ddab64d9b8e` |
| lastVerifiedCommitDate | 2026-09-30T15:46:42+02:00|
| governingOverview      | `overview.md`                              |

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

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Final result releases exact terminal selection before root task archival, reports retryable release failure, and carries the review-artifact archive hook's report on an archived (or would-archive) root task (MIK-R25). | "def _finalized_result("; "archive = _with_review_artifact_cleanup(contract, archive, dry_run=args.dry_run)" | mcp/src/agents_remember/worktrees/modules/finalize.py:153-230 |
| The archive hook is carried for an archived task only; unbound is `not-bound`, and an exception is a `failed` report, never raised. | `_with_review_artifact_cleanup` | mcp/src/agents_remember/worktrees/modules/finalize.py:233-271 |
| Exact terminal release is independent of queue/task scheduling state. | `with_terminal_atomic_series_release` | mcp/src/agents_remember/worktrees/activation/atomic_series_activation_terminal.py:17-65 |
| Cleanup behavior and branch/worktree removal are delegated here. | "def cleanup_result" | mcp/src/agents_remember/worktrees/modules/cleanup.py:645-645 |
| The cleanup seam that runs reclamation, short-circuits an already-completed cell, and shapes a real successful reclamation through the report shaper — deliberately not on a dry run or a nonzero return code. | `_run_or_verify_cleanup`; "cleanup_report(contract, result.payload)" | mcp/src/agents_remember/worktrees/modules/finalize.py:328-362; mcp/src/agents_remember/worktrees/modules/finalize.py:361-361 |
| The operator-facing report shape this module restores for a completed reclamation, and its `already-clean` rule. | `cleanup_report`; "ALREADY_CLEAN = \"already-clean\"" | mcp/src/agents_remember/worktrees/modules/cleanup_report.py:23-23; mcp/src/agents_remember/worktrees/modules/cleanup_report.py:28-53 |
| Carryover completion is proven against the official memory ledger here. | "def carryover_done" | mcp/src/agents_remember/worktrees/modules/guidance.py:193-193 |
| Git ancestry proof uses the worktree module Git adapter. | "def is_ancestor" | mcp/src/agents_remember/worktrees/modules/git.py:139-139 |
| Task document JSON/markdown reconciliation uses the task document service. | "def write_task_doc(task_root: Path" | mcp/src/agents_remember/tasks/store.py:108-108 |
| Focused tests pin a named master's row completion and two-document rollback and the misplaced-master refusal, and (MIK-R38) the folder master's row under the demotion rule, the dry run, the standalone cases and every refusal before any write. | "class LifecycleFinalizeTests(_FinalizeFixtures):"; "class FolderMasterFinalizeTests(_FinalizeFixtures):" | mcp/tests/test_lifecycle_finalize.py:155-244; mcp/tests/test_lifecycle_finalize.py:247-409 |

## Cross-Repo References

No meaningful cross-repository reference applies to this repository-owned terminal operation.

| Finding | Anchor | Source |
| --- | --- | --- |

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

| Finding | Anchor | Source |
| --- | --- | --- |
| Parent resolution dispatches on the leaf's `master`; with no target the leaf finalizes standalone, and an asserted parent is refused. | "def _resolve_parent_target("; "target = _named_parent(contract.task_root, args, leaf.master, leaf.id)"; "target = _folder_parent(contract.task_root, args, leaf)"; "standalone leaf has no immediate parent reference to assert" | mcp/src/agents_remember/worktrees/modules/finalize.py:397-437 |
| A named master: expected path, assertions, read, exactly one row. | "def _named_parent(" | mcp/src/agents_remember/worktrees/modules/finalize.py:450-456 |
| A leaf naming none: the master sync's helper, the named-master checks, standalone without a row, and the named cause when a parent was asserted. | "folder_master = folder_master_json_path(task_root, leaf)"; "lists no row {leaf.id!r}; the leaf finalizes"; "_assert_parent_arguments(args, expected_parent, leaf.id)" | mcp/src/agents_remember/worktrees/modules/finalize.py:459-481 |
| Every master read refuses a non-master and a document the store would write elsewhere; the leaf gets the same check before its parent is resolved. | "require_task_document_in_place(parent_path, parent, FinalizeTaskDocumentError)"; "require_task_document_in_place(leaf_path, leaf, FinalizeTaskDocumentError)" | mcp/src/agents_remember/worktrees/modules/finalize.py:507-519; mcp/src/agents_remember/worktrees/modules/finalize.py:393-393 |
| The completed row goes through the master demotion rule. | `_parent_completion_candidate`; "return demote_completed_master_if_unresolved(updated)" | mcp/src/agents_remember/worktrees/modules/finalize.py:632-646 |
| The one rule for a leaf naming no master, shared with the master sync and reopen. | "def folder_master_json_path(task_root: Path, leaf: TaskDocument)" | mcp/src/agents_remember/tasks/master_sync.py:165-183 |

## Update History
- 2026-09-30T15:25:16+02:00 — 260928-MIK-L38 curator (staged change set on `ar/260928-mik-l38`, code base `59daf5055eb1ceffba89170be64ac85cabf860f4`; review R1 pass-with-notes, fixes, R2 pass): **body updated for MIK-R38.** New section "260928-MIK-L38 The Leaf's Master Is Resolved By The Master Sync's Rule" (D32; rulings 12:33:07 Q1, Q2, Q4, 13:11:32 finding 1 and notes 2 and 4, 13:35:32 parent guard; R2 pass; the L32 sync) with six rows. The Code Commentary paragraph on task-document reconciliation was corrected: it said `master_doc_path` plus `subtask_number` set the parent row, but the row has been derived from the leaf (the arguments only assert it), and it now names the folder-master rule and the demotion. **Reopened claim re-read, reworded and re-anchored:** the `LifecycleFinalizeTests` row no longer claimed readiness, dry-run and cleanup-blocked cases the class does not hold; it now names both test classes on their line-exact class lines, so the committed generated bullet (2026-09-06T22:41:21+00:00) is left intact. The `_finalized_result` row was re-pointed by the exact +4 import shift (`149-226` → `153-230`); the `_run_or_verify_cleanup` rows by the installed fixer (one generated bullet, kept) and the exact +4 shift. No verification stamp was advanced.
- 2026-09-30T13:22:40+00:00: Generated citation repair: "cleanup_report(contract, result.payload)" repointed to mcp/src/agents_remember/worktrees/modules/finalize.py:361-361. No content impact: mechanical anchor-range projection bound to citation source snapshot 7bf4b32298650854529d8e6c804df2de7f6bf2ad388d219d6f1439bc23af3bf3; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T04:01:40+02:00 — 260928-MIK-L25 curator (uncommitted change set on `ar/260928-mik-l25`, code base `3eb034a6ab0493a51da5dcd6d013aa6f27f39496` plus the staged delta): **body updated for MIK-R25.** Added the Code Commentary paragraph on the review-artifact archive hook (`_with_review_artifact_cleanup`, rule 5, review F2 and ruling 02:32:42 (a)) and its row. **Reopened claim re-read, reworded and re-anchored:** the `_finalized_result` row now also names the hook's report; its committed generated-repair bullet (2026-09-11T22:39:01+00:00) is left intact, so the row is re-anchored on the line-exact quotes "def _finalized_result(" and the hook call. The other rows were projected by the installed fixer. No verification stamp was advanced.
- 2026-09-30T01:49:28+00:00: Generated citation repair: `_run_or_verify_cleanup` repointed to mcp/src/agents_remember/worktrees/modules/finalize.py:324-358. No content impact: mechanical anchor-range projection bound to citation source snapshot a85c638de10bc300eb93d4b69fedcbaf6e141873de546e8335d0f51f59402273; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T01:49:28+00:00: Generated citation repair: "cleanup_report(contract, result.payload)" repointed to mcp/src/agents_remember/worktrees/modules/finalize.py:357-357. No content impact: mechanical anchor-range projection bound to citation source snapshot a85c638de10bc300eb93d4b69fedcbaf6e141873de546e8335d0f51f59402273; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "def carryover_done" repointed to mcp/src/agents_remember/worktrees/modules/guidance.py:193-193. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: "def cleanup_result" repointed to mcp/src/agents_remember/worktrees/modules/cleanup.py:645-645. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: "def carryover_done" repointed to mcp/src/agents_remember/worktrees/modules/guidance.py:189-189. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: "def is_ancestor" repointed to mcp/src/agents_remember/worktrees/modules/git.py:139-139. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T06:49:47+00:00: Generated citation repair: "def cleanup_result" repointed to mcp/src/agents_remember/worktrees/modules/cleanup.py:645-645. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T06:49:47+00:00: Generated citation repair: "def carryover_done" repointed to mcp/src/agents_remember/worktrees/modules/guidance.py:189-189. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T06:49:47+00:00: Generated citation repair: "def is_ancestor" repointed to mcp/src/agents_remember/worktrees/modules/git.py:139-139. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (citation pass): re-derived the source ranges of 1
  claim(s) whose anchor no longer sat in its cited range and normalised 2 further range(s) in this
  card from their anchors against the frozen source snapshot (`agents-remember memory-citations
  --fix --document`, snapshot 188b8ecd). No claim wording changed; every rewritten range was read
  back at its current position. Verification metadata remains closeout-owned.
- 2026-09-14T15:05+02:00 — No content impact: mechanical citation re-derivation after the
  260913-LCA-L8 change set added one import line to `worktrees/modules/cleanup.py`, shifting
  `def cleanup_result` from line 632 to 633. The anchor was re-read at `cleanup.py:633-633`, where the
  definition still sits; the cited symbol and its meaning are unchanged.
- 2026-09-12T19:50+02:00 — 260831-LOCR-L31 root integration to `lifecycle_finalize_task`: this
  module is now the **only** landing-side route that reclaims, because `worktree_integrate` stopped
  running cleanup inside itself. Recorded the two-part `_run_or_verify_cleanup` seam: the unchanged
  `already-completed` short-circuit and `except RuntimeError` → `returncode 2` / `state: "blocked"`
  refusal (which still leaves task documents untouched), plus the new report shaping through
  `cleanup_report(contract, result.payload)` and its load-bearing gate — the cleanup payload is
  returned unchanged when `args.dry_run` or `result.returncode != 0`, so a preview never asserts a
  reclamation that did not happen and a refusal keeps its own `blockers` and partial inventory.
  Noted that the run-and-catch half which used to own this reporting
  (`automatic_cleanup.run_automatic_cleanup`) was deleted with zero callers once reclamation moved
  here. Verification metadata remains closeout-owned; no acceptance claim.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `_finalized_result` repointed to mcp/src/agents_remember/worktrees/modules/finalize.py:143-219. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: "def cleanup_result" repointed to mcp/src/agents_remember/worktrees/modules/cleanup.py:632-632. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-06T22:41:21+00:00: Generated citation repair: `LifecycleFinalizeTests` repointed to mcp/tests/test_lifecycle_finalize.py:28-176. No content impact: mechanical anchor-range projection bound to citation source snapshot 250eac92295fa399589ccf1c9726bfb4cd28a1a0b20dca126769403fba09b52d; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-08-26T08:45+02:00 — Restored the canonical Cross-Repo reference section for this changed
  finalization card.

- 2026-08-26T08:30+02:00 — Restored the required governing-overview link while reconciling exact
  terminal selection release behavior.

- 2026-08-26T03:37+02:00 — Added finalization's exact terminal activation-release/readback seam
  before root archival, including explicit release-blocked retry evidence and preservation of a
  different current selection. Verification remains post-Dagger/closeout-owned.

- 2026-08-24T15:04+02:00 — Cumulative CLIVE curation: merged exact source CAS and independent projection effects into finalization task publication. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.



- 2026-08-20T10:45+02:00 — 260815-DAG-L12 curator: re-anchored citation range(s) to current source after the L12 line movement (cited files changed, card source unchanged); verification metadata unchanged.

- 2026-08-18T09:05+02:00 — Renamed the atomic 'barrier' concept to 'blocker' throughout (terminology unification; no behavioral change). Verification remains closeout-owned.

- 2026-08-15T09:53+02:00 — No content impact: L3's Pyright repair narrows the already-required
  leaf task root before the queue-bound publication callback; finalization ordering and task writes
  remain unchanged.
- 2026-08-15T09:10+02:00 — L3 content update: documented queue-governed finalization task writes
  and explicit refusal projection; verification remains closeout-owned.
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B22 curator: rebound the cleanup-delegation
  citation to the actual `def cleanup_result` definition via the scoped fixer; exact non-fixing
  check returns zero findings.

- 2026-08-02T17:36:56+02:00 — 260731-EFA-L6 curator W1-B09: repaired 10 citation finding(s); scoped recheck clean.

- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: finalization now returns `enclosurePath`, skips root archive work for leaf contracts, and archives completed root series tasks into `0_archive` once a series contract is finalized. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-23T22:50+02:00 — Created for dashboard task 14. The module adds the terminal lifecycle finalizer that proves one parent-child branch edge, runs or verifies cleanup, and marks the current task plus immediate parent row complete. Verification metadata is pending until closeout stamps the source commit.