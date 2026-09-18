# mcp/src/agents_remember/worktrees/modules/finalize.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/worktrees/modules/finalize.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-14T19:00+02:00 |
| lastVerifiedCommitHash | `ea9cf0abeab4fe88961bda10b4f54d30266a9634` |
| lastVerifiedCommitDate | 2026-09-17T23:56:19+02:00|
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
cit:([`_run_or_verify_cleanup`], mcp/src/agents_remember/worktrees/modules/finalize.py:277-311):

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
cit:(["cleanup_report(contract, result.payload)"], mcp/src/agents_remember/worktrees/modules/finalize.py:310-310)
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

Task document reconciliation is optional and edge-scoped. `task_doc_path` is
set to `Completed` unless it points at a master document. `master_doc_path` plus
`subtask_number` sets only that immediate parent row to `Completed`. The parent
task status itself is left unchanged, and ancestors are not completed
recursively; callers repeat finalization for the next parent-child branch edge.
Dry-run returns `would-update` task-document states without writing files.

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Final result releases exact terminal selection before root task archival and reports retryable release failure. | `_finalized_result` | mcp/src/agents_remember/worktrees/modules/finalize.py:144-220 |
| Exact terminal release is independent of queue/task scheduling state. | `with_terminal_atomic_series_release` | mcp/src/agents_remember/worktrees/activation/atomic_series_activation_terminal.py:17-65 |
| Cleanup behavior and branch/worktree removal are delegated here. | "def cleanup_result" | mcp/src/agents_remember/worktrees/modules/cleanup.py:645-645 |
| The cleanup seam that runs reclamation, short-circuits an already-completed cell, and shapes a real successful reclamation through the report shaper — deliberately not on a dry run or a nonzero return code. | `_run_or_verify_cleanup`; "cleanup_report(contract, result.payload)" | mcp/src/agents_remember/worktrees/modules/finalize.py:277-311; mcp/src/agents_remember/worktrees/modules/finalize.py:310-310 |
| The operator-facing report shape this module restores for a completed reclamation, and its `already-clean` rule. | `cleanup_report`; "ALREADY_CLEAN = \"already-clean\"" | mcp/src/agents_remember/worktrees/modules/cleanup_report.py:23-23; mcp/src/agents_remember/worktrees/modules/cleanup_report.py:28-53 |
| Carryover completion is proven against the official memory ledger here. | "def carryover_done" | mcp/src/agents_remember/worktrees/modules/guidance.py:189-189 |
| Git ancestry proof uses the worktree module Git adapter. | "def is_ancestor" | mcp/src/agents_remember/worktrees/modules/git.py:139-139 |
| Task document JSON/markdown reconciliation uses the task document service. | "def write_task_doc(task_root: Path" | mcp/src/agents_remember/tasks/store.py:108-108 |
| Focused tests pin readiness, dry-run, cleanup-blocked, and task-doc update behavior. | `LifecycleFinalizeTests` | mcp/tests/test_lifecycle_finalize.py:28-176 |

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

## Update History
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