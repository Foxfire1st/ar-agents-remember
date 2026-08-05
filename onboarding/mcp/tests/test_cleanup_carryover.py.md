# test_cleanup_carryover.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_cleanup_carryover.py`            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-01T09:10+02:00                           |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060`                                               |
| lastVerifiedCommitDate |2026-08-05T12:41:24+02:00|
| governingOverview      | `../overview.md`                                    |

## Governing Overview

[mcp Overview](../overview.md)

## Purpose

`test_cleanup_carryover.py` pins cleanup's post-integration safety rules. It
started as the slice-05m lifecycle-ordering suite for carryover-before-cleanup:
the lifecycle must carry the parked memory home (via the existing
`memory_carryover_apply`) **before** `worktree_cleanup` deletes the worktree that
carryover reads from. It also pins task 13's source-branch correctness and task
14's nested-task cleanup correction: task work branches are deleted only after
Git proves they are reachable from the contract's recorded source branch, while
parent/source branches survive for their own lifecycle edge. Dry-run directory
previews account for worktrees/provider-runtime paths scheduled for removal by
the same cleanup run, and dry-run summaries must speak prospectively rather than
claiming cleanup already completed. The "carryover done" signal remains the
OFFICIAL ledger itself (a row mapping the landed code commit), never a contract
stamp. Task 32 adds exact observer drift-snapshot cleanup coverage so worktree
cleanup does not leave memory-mirror rows behind after the worktree is removed.

## Code Commentary

### Logic

A `_contract(tmp, **over)` helper builds an `external`-memory `WorktreeContract`
with `integration_status == "completed"`, an `integrated_code_commit`
(`"LANDED1234"`), and a separate closeout `code_commit` (`"CLOSE1234"`), so the
tests exercise the "landed commit = `integrated_code_commit`, else `code_commit`"
rule in `guidance.carryover_done`.

- `CarryoverDoneTests` build a REAL official memory git repo via `_official_memory(*codes)`
  (`init_repo` + a base `create_initial_ledger`, then one commit per mapped code so
  each carried memory commit's `%cI` resolves). They assert `carryover_done` is
  `(True, <iso>)` when the ledger maps the landed commit, `(False, "")` when it maps
  something else, and `(True, "")` vacuously for `internal` memory (nothing to carry).
- `GuidanceCarryoverRoutingTests` patch `guidance.carryover_done` to drive
  `lifecycle_guidance` on the `integration_status == "completed"` branch: a `(False, "")`
  return routes phase `carryover-pending` with `nextTool == "memory_carryover_apply"`;
  a `(True, "<iso>")` return routes `cleanup-pending` with `nextTool == "worktree_cleanup"`
  and surfaces `carryoverDoneAt`. Note the asymmetry in how those keys are read: `phase`
  with `guidance["phase"]`, but `nextTool` and `carryoverDoneAt` with `guidance.get(...)`.
  That is the return type, not a style choice — `lifecycle_guidance` now returns a
  `LifecycleGuidance` TypedDict (cit:([`LifecycleGuidance`], mcp/src/agents_remember/worktrees/modules/guidance.py:86-96)) on which
  `phase`/`summary`/`nextOperation` are required and `nextTool`/`nextArgs`/`nextRequiredArgs`/
  `carryoverDoneAt` are `NotRequired`, and `next_guidance` sets `nextTool` only `if tool`.
  An absent next-move is an **omitted key**, never `""`, so subscripting it is a type error
  even in the two phases that always carry one.
- `CleanupCarryoverGuardTests` patch `cleanup.carryover_done` to `(False, "")`, write
  the contract, and assert `cleanup_result` RAISES `RuntimeError` (message mentions
  "carryover") — the hard guard that refuses to delete the parked memory branch before
  it was carried home.
- `SourceBranchProofTests` build a real `main` + `feat/dashboard` + `ar/task` graph.
  They prove `delete_branch_if_merged_into` deletes the task work branch while
  `main` is checked out when `ar/task` is contained in the recorded
  `feat/dashboard` source branch, and keeps an `ar/unmerged` branch with reason
  `not-merged-into-source` when that proof fails.
- `CleanupChildEdgeTests` build real code and memory repos with a landed
  `feat/dashboard` parent branch and `ar/task` child branch, run full
  `cleanup_result(..., dry_run=False)` with provider teardown disabled, and assert
  cleanup deletes only the child task branches. The parent/source branches remain
  present in both repos, and the branch payload contains only `code` and `memory`.
- `CleanupDryRunDirectoryTests` patch carryover/provider teardown, create a standard
  worktree group containing only the code worktree, memory worktree, and
  `provider-runtime/`, then assert `cleanup_result(..., dry_run=True)` reports the
  group directory as `would_remove` rather than `not-empty`, returns state
  `would-cleanup`, and uses prospective "Cleanup would reclaim..." wording in the
  summary.
- `RemoteBranchDeleteTests` mock `cleanup.run_git` to cover `delete_remote_branch_if_present`:
  an absent `origin/<branch>` (empty `ls-remote`) is not pushed, a present one is deleted.
- `CleanupDriftSnapshotTests` writes real observer drift snapshots and proves dry-run cleanup
  reports the contract-owned code snapshot as `would_remove`, while real cleanup deletes only
  that exact snapshot and preserves an unrelated one.

47 test methods across 11 test classes; this residual-only curation does not assert a fresh runtime test result.

### Conventions

Imports the shared `git` / `init_repo` helpers from `test_worktree_support` (the
worktree suite idiom). `unittest.mock.patch` targets the name in the module under
test (`...guidance.carryover_done`, `...cleanup.carryover_done`, `...cleanup.run_git`)
so the production call site is the one swapped. The carryover signal is always the
official ledger, so the ledger-backed tests construct a real git repo rather than
faking the row.

### Invariants And Boundaries

- The carryover-done signal under test is the OFFICIAL ledger (no contract stamp);
  the guard and the guidance route both read it through `carryover_done`.
- Work-branch deletion is source-branch-specific: the recorded source branch is the
  proof target, not the checkout's ambient `HEAD` or upstream.
- Cleanup is a child-edge operation: it removes finalized task work branches but
  does not retire parent/source branches. Parent/source branches are finalized by
  their own lifecycle edge.
- Dry-run directory reporting models cleanup's scheduled removals, but real cleanup
  remains conservative and removes directories only after they are empty.
- External-only: the carryover route + cleanup guard are no-ops for `internal`/`disabled`
  memory (vacuously done), which `test_internal_memory_is_vacuously_done` asserts.
- Cleanup drift snapshot removal is exact to the contract's code worktree name and branch;
  unrelated snapshots must remain untouched.

### Todos

None.

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| `carryover_done` reads the official ledger mapping used as the carryover-complete signal. | `carryover_done` | mcp/src/agents_remember/worktrees/modules/guidance.py:204-227 |
| `_post_integration_phase` routes completed integrations through `carryover-pending` or `cleanup-pending` and selects the corresponding carryover or cleanup tool. | `_post_integration_phase` | mcp/src/agents_remember/worktrees/modules/guidance.py:260-306 |
| `GuidanceCarryoverRoutingTests` proves both carryover-pending and cleanup-pending routes. | `GuidanceCarryoverRoutingTests` | mcp/tests/test_cleanup_carryover.py:155-178 |
| The cleanup carryover guard and result contract under test. | `cleanup_result` | mcp/src/agents_remember/worktrees/modules/cleanup.py:422-465 |
| Source-branch work-branch deletion is proved by the cleanup helper. | `delete_branch_if_merged_into` | mcp/src/agents_remember/worktrees/modules/cleanup.py:82-112 |
| Child-edge source preservation is tracked by the cleanup deletion set. | `_deleted_branches` | mcp/src/agents_remember/worktrees/modules/cleanup.py:302-342 |
| Dry-run directory planning and empty-directory removal are owned by the cleanup state helpers. | `remove_empty_dir`; `_scheduled_removal_paths`; `_cleanup_state` | mcp/src/agents_remember/worktrees/modules/cleanup.py:267-282; mcp/src/agents_remember/worktrees/modules/cleanup.py:345-357; mcp/src/agents_remember/worktrees/modules/cleanup.py:373-392 |
| Remote branch deletion is handled by the cleanup helper. | `delete_remote_branch_if_present` | mcp/src/agents_remember/worktrees/modules/cleanup.py:174-190 |
| Shared drift snapshot path/removal helper used by cleanup and the drift snapshot cleanup tests. | `remove_drift_snapshot` | mcp/src/agents_remember/observer/drift_snapshots.py:25-33 |
| The official ledger reader and mapping lookup the carryover-done signal is built on. | `load_ledger`; `find_mapping` | mcp/src/agents_remember/kernel/memory_ledger.py:187-190; mcp/src/agents_remember/kernel/memory_ledger.py:232-234 |
| The shared `git` and `init_repo` helper definitions reused here. | `git`; `init_repo` | mcp/tests/test_worktree_support.py:90-100; mcp/tests/test_worktree_support.py:103-120 |
| This cleanup suite's `_official_memory` helper exercises the shared `git` and `init_repo` helpers. | `_official_memory` | mcp/tests/test_cleanup_carryover.py:120-133 |
| The typed `WorktreeArgs` DTO `cleanup_result` consumes. | `WorktreeArgs`; `cleanup_result` | mcp/src/agents_remember/worktrees/modules/args.py:20-82; mcp/src/agents_remember/worktrees/modules/cleanup.py:422-465 |

## Cross-Repo References

No meaningful cross-repo references found.

## Series-Contract Notes

Cleanup/carryover tests keep the carryover-before-cleanup invariant while updating contract fixtures to the new series-contract schema.

## Update History

- 2026-08-04T16:40:00+02:00 — 260731-EFA-L6 S18-B12 curator correction (reviewer-BLOCK repair): replaced the stale 14-test claim with the actual 47 test methods across 11 classes without asserting green runtime status; routing is bound to `_post_integration_phase` (260-306) and its focused tests; the ledger claim is narrowed to the `load_ledger`/`find_mapping` reads with no writer in `carryover_done`; the shared `git`/`init_repo` helpers and their `_official_memory` use are bound by source owner; the scoped fixer generated the final routing range.
- 2026-08-02T16:44:57+02:00 — L6 W1-B02 curator: repaired 4 repository-internal reference rows for drift snapshots, the memory ledger, shared worktree test helpers, and `WorktreeArgs`; scoped citation verification follows.

- 2026-08-01T09:10+02:00 — 260731-EFA-L4 curator: `GuidanceCarryoverRoutingTests` moved three
  assertions from `guidance["nextTool"]` / `guidance["carryoverDoneAt"]` to `.get(...)`, and the
  card described the reads closely enough that leaving that unexplained would mislead. Recorded
  why: `lifecycle_guidance` now returns the `LifecycleGuidance` TypedDict, whose next-move and
  `carryoverDoneAt` keys are `NotRequired` — verified at `worktrees/modules/guidance.py` L85-L96
  (the TypedDict), L141-L157 (`next_guidance`, which sets `nextTool` only `if tool`) and L229
  (`lifecycle_guidance`'s return annotation). Both routing verdicts, the expected tool names and
  the `carryoverDoneAt` value are unchanged. Re-read the rest against the current 440-line file:
  still 14 tests across 8 classes, `CarryoverDoneTests` / `CleanupCarryoverGuardTests` /
  `SourceBranchProofTests` / `CleanupChildEdgeTests` / `CleanupDryRunDirectoryTests` /
  `CleanupDriftSnapshotTests` / `RemoteBranchDeleteTests` all present and unrenamed, and all six
  Repo-Internal reference paths resolve.

- 2026-06-27T23:09+02:00 — Task 32 memory-mirror pruning: added `CleanupDriftSnapshotTests` and a drift snapshot fixture helper to prove cleanup dry-runs/removes the exact contract-owned code-worktree drift snapshot while preserving unrelated snapshots. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: cleanup/carryover tests now exercise the series-contract contract shape while preserving the code-first, memory-after cleanup expectations. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-24T00:27+02:00 — Added dry-run cleanup wording coverage: `CleanupDryRunDirectoryTests` now asserts the `would-cleanup` state and prospective "Cleanup would reclaim..." summary, preventing dry-run payloads from claiming cleanup completed.
- 2026-06-24T00:16+02:00 — Task 14 cleanup correction: removed the obsolete `_retire_branch` source-retirement test coverage and added `CleanupChildEdgeTests`, which run real cleanup against code and memory repos to prove only the child task branches are removed while the parent/source branches survive. Updated the purpose, logic, invariants, references, and test count for the child-edge cleanup contract.
- 2026-06-23T15:09+02:00 — Task 13 cleanup correctness: added `SourceBranchProofTests` for `delete_branch_if_merged_into` (delete a task work branch merged into the recorded dashboard/source branch even while `main` is checked out; keep an unmerged work branch with `not-merged-into-source`) and `CleanupDryRunDirectoryTests` for the dry-run worktree-group directory preview after scheduled code/memory worktree plus provider-runtime removals. Corrected this touched sidecar's governing overview link to `../overview.md`.
- 2026-06-21T06:40+02:00 — Created for slice 05m (carryover-before-cleanup ordering + work/source branch retirement): covers `carryover_done` (ledger maps the landed commit / doesn't / internal-vacuous), the guidance routing (`carryover-pending` vs `cleanup-pending` + `carryoverDoneAt`), the cleanup carryover-guard (refuses before carryover), `_retire_branch` (force-delete when landed / keep when not / never the default / switch off a checked-out branch), and `delete_remote_branch_if_present` (absent vs present, mocked). 12 tests. Verification metadata left empty until closeout stamps the 05m code commit.
