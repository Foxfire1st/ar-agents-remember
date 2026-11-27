# mcp/tests/test_terminal_blocker_reasons.py

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

`test_terminal_blocker_reasons.py` (260913-LCA-L8) pins the terminal blocker contract: a cleanup or
finalize blockage always names the component it stopped on and carries a non-empty reason, so a
blockage an operator cannot read — and cannot tell apart from a spurious one — is impossible to emit.



The cases are integration-lane members (`mcp/tests/test-evidence-lanes.toml:795`).
The complete lifecycle catalog declares this module as an exact consumer on **12**
artifact rows. That dependency ownership and the ambient-role runner declaration
are selection metadata, not execution evidence.

## Code Commentary

Abandon preview and real abandon now live in dedicated `test_abandon_removes_leftover_provider_runtime_directory_directly` (`:163-200`), verifying `would-abandon`, `directories.provider_runtime.would_remove=True`, intact leftover directory on preview, and direct removal on apply.

### Logic

Eight cases: three drive the whole public tools over leftover provider-runtime directories, two pin the blocker validator and `worktrees/modules/filesystem.py::remove_tree` directly, and three hold the drift-snapshot preview contract.

**The whole-tool boundary.** `_landed_leaf` (`:100-102`) uses the shared external-memory fixture to create real code and memory worktrees and commits
and, with `publish_closeout_evidence=True`, write and reread a completed-closeout contract recording both commit IDs. `_landed_leaf_config` (`:105-116`) calls the integration application entry point with `strategy="ff-only"` and `dry_run=False` and asserts `integrated`. `_finalize` (`:125-129`) calls the finalization application entry point.

- `test_cleanup_removes_leftover_provider_runtime_directory_directly` (`:132-160`): creates `<group>/provider-runtime`, runs `worktree_cleanup_tool(dry_run=True)` asserting `would-cleanup` and `directories.provider_runtime.would_remove=True` while leaving the directory on disk, then calls `_finalize` asserting `finalized`, `cleanup-completed`, directory and worktree group removed, contract `cleanup == "completed"`, and leaf document `Completed`.
- `test_abandon_removes_leftover_provider_runtime_directory_directly` (`:163-200`): resets worktrees to source branches, creates `<group>/provider-runtime`, runs `worktree_abandon_tool(dry_run=True)` (`would-abandon`, `would_remove=True`, directory retained) and `worktree_abandon_tool(dry_run=False)` (`abandoned`, `removed=True`, directory and worktree group removed, contract `cleanup == "abandoned"`).
- `test_an_unremovable_provider_runtime_directory_blocks_cleanup_with_its_reason` (`:203-234`): sets `chmod 0o500` on `<group>/provider-runtime`, calls `_finalize` asserting `cleanup-blocked`/`blocked`, `directories.provider_runtime.removed=False`, `reason` starting with `"permission denied"`, a blocker with `directory == "provider_runtime"` and permission-denied reason, leaf document not `Completed`, contract `cleanup == "pending"`, and directory still present.

**The two invariant owners directly.** These cases need no tool call.

- `test_an_unnameable_blocker_reason_is_refused_at_its_own_source` (`:237-245`) asserts `_blocker({"directory": "provider_runtime"}, unnameable)` raises `RuntimeError` naming `provider_runtime` for `None`, `""`, `"   "` and `17`.
- `test_remove_tree_answers_with_a_reason_whenever_it_reclaimed_nothing` (`:248-283`) exercises `worktrees/modules/filesystem.py::remove_tree` for `already-absent`, `dry_run=True` (`would_remove: True`), real removal (`removed: True`), and `chmod 0o500` (`removed: False`, reason starting with `"permission denied"`).

### Conventions

The `bound_worktree_services` fixture (`:88-97`) rebinds the worktree services with a
`citation_guard` double (`_NoManagedCitationCache`, `:69-85`) whose `guard` returns production's own
authority-free `TerminalNamespaceGuard(None, None, None)`; only the cache reservation is a double, and
it is the value production yields for a fixture leaf with no managed cache namespace. The module is
marked `pytest.mark.integration` and drives real disposable repositories and real worktrees under
`tmp_path`.

Assertions are made on the operator-visible payload and on the filesystem, not on internal call
counts: the closed task edge, removed/surviving files, and exact blocker list are each measured using the shared worktree service fixture and its citation-guard double.

### Invariants And Boundaries

- The cases pin what the change makes **impossible**, not a new capability. A reasonless blocker can
  no longer be constructed; `remove_tree`'s ability
  to reclaim a tree, and cleanup's ability to reclaim an enclosure, are unchanged.
- A genuinely blocked teardown still blocks, with its own reason and its own partial inventory. The
  permission-failure case exists so the stricter builder cannot be read as turning every refusal into
  a success.
- A leftover provider-runtime directory is reclaimed directly on cleanup or abandon, and an unremovable directory blocks finalization with its permission-denied reason.
- These are focused development cases over disposable coordination state. They are behaviour evidence
  for one contract, not full-suite certification or independent review, and this card records source
  inspection, not a test run.

### Todos

None recorded.

## Earlier Memory-Base Context

The following accounts are retained from memory revision `81cfe4a89f5ffb222bd09640410d268d3fbef254`. They describe their earlier source epochs, observations and rationale; they are not new executions or current acceptance results. Current source corrections above remain in force.

### Earlier observed cleanup incident

Summary based on the earlier card account, base lines 13–23:

> The measured defect: `lifecycle_finalize_task` on an enclosure returned `state: cleanup-blocked` with
> `blockers: [{"provider": "providerRuntime", "reason": null}]`, while the same payload proved the
> terminal archive, reported the providers `torn-down`, and said in its own summary that enclosure
> deletion may continue. Cleanup stopped anyway, preserved the citation-source index with
> `terminal-operation-failed`, and left the leaf un-finalized; an immediate retry then reclaimed
> everything and finalized the edge. Read from source, the first call was wrong rather than stopping
> for a cause the retry re-observed as resolved: the blocker was built in
> `worktrees/modules/terminal_validation.py`, where a result dict with no `reason` key became `None`
> and the item still counted as blocked, and the only producer able to hand it `{"removed": False}`
> with no reason at all was `application/provider_runtime.py::remove_tree`'s post-reclaim
> "still present" branch.

### Earlier preview repair and retry explanation

Summary based on the earlier card account, base lines 32–105:

> The earlier account records that calling public abandon preview in the existing first-call finalization case reproduced the omitted preview flag without adding a collected test case. It explained retry convergence rather than relying on it: the first L6 call was wrong, the repaired L6 shape must finalize on its first call, and the genuinely unreclaimable case must refuse twice.

### Earlier L6 preview growth

Summary based on the earlier card account, base lines 182–186:

> At the 260918-TSIP-L6 epoch, the card recorded three added drift-snapshot preview cases and growth from 361 to 480 lines. Those growth figures and that epoch’s lane coordinates are historical measurements. The current source inventory above, including its 486 lines and ten definitions, remains separate.

## Evidence

### Docs References

No Domain Documentation source is configured for this repository; the proving evidence is this
repository's own source, its own blocker vocabulary, and the operator payload it emits.

No external source is required for this repository-owned blocker contract.

### Repo-Internal References


- Public abandon preview returns would-abandon with directories.provider_runtime.would_remove true and leaves the leftover provider-runtime directory in place; real abandon removes it directly. [1]



- Cleanup preview marks a leftover provider-runtime directory for removal and one finalize call completes cleanup directly, removing the directory and worktree group and marking the contract and leaf document completed. [2]



- An unnameable blocker reason raises at the call site that detected it. [5]



- The direct removal test exercises worktrees/modules/filesystem.py::remove_tree for absent-path reason, dry-run preview, real removal, and permission-denied failure. [12]


- The landed fixture and the public calls the whole-tool cases drive. [14]

- The service rebinding and the citation-guard double the whole-tool cases run against. [15]

- The only construction path for a terminal blockage; it refuses a missing, blank or non-string reason. [16]
- The operator-language answer for a reasonless or malformed result item. [17]


- The bundle and the builder the invariant-owner cases drive directly. [18]



- The direct directory removal helper that answers with an explicit reason whenever it reclaims nothing. [19]



- The worktree services container and default services builder the fixture rebinds. [20]



- The public terminal route the whole-tool cases call. [21]


- The landing fixture and the public configuration the whole-tool cases build on. [22]

- The landing fixture and the public configuration the whole-tool cases build on. [24]

### Cross-Repo References

The three whole-tool cases build disposable code and external memory Git repositories under `tmp_path`. The helper-level cases exercise typed results or filesystem removal fixtures directly.

### Repo-Internal References (continued)

- The landing world each whole-tool case builds is a real temporary repository pair. [27]

## Drift-Snapshot Preview Cases

The module has **362 physical lines** and **eight source test definitions**. Its preview definitions are:

`test_a_drift_snapshot_preview_is_not_read_as_an_unreclaimed_result` (`:391-427`) drives the drift-snapshot expectation directly with `preview=True` and requires the entry to be pending rather than blocked; `test_a_real_reasonless_drift_snapshot_still_refuses_rather_than_passing_as_preview` (`:430-451`) preserves the real reasonless refusal; and `test_the_cleanup_preview_of_a_task_with_a_drift_snapshot_reports_no_blocker` (`:454-489`) drives the tool-level cleanup preview. These are static source-definition locations, not a fresh execution result.

- The integration lane selects mcp/tests/test_terminal_blocker_reasons.py. Execution evidence is recorded separately. [23]

- The lane manifest declares test_terminal_blocker_reasons.py in integration. Membership selects evidence and establishes no invocation. [25]



- Twelve exact artifact consumer lists in the lifecycle catalog name this module. The dependency-ownership reader consumes the catalog for selection. [30]



- Twelve exact artifact consumer lists in the lifecycle catalog name this module. The dependency-ownership reader consumes the catalog for selection. [28]
