# mcp/tests/test_terminal_blocker_reasons.py

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

`test_terminal_blocker_reasons.py` (260913-LCA-L8) pins the terminal blocker contract: a cleanup or
finalize blockage always names the component it stopped on and carries a non-empty reason, so a
blockage an operator cannot read — and cannot tell apart from a spurious one — is impossible to emit.



The cases are integration-lane members (`mcp/tests/test-evidence-lanes.toml:792`).
The complete lifecycle catalog declares this module as an exact consumer on **12**
artifact rows. That dependency ownership and the ambient-role runner declaration
are selection metadata, not execution evidence.

## Code Commentary

The existing first-call finalization case also calls public abandon preview before integration. It verifies `would-abandon`, an empty blocker list and an intact worktree, using the existing test definition.

### Logic

Ten cases: two drive the whole public tool, five pin the two invariant owners
directly, and three hold the drift-snapshot preview contract.

**The whole-tool boundary.** `_landed_leaf` (`:108-110`) uses the shared external-memory fixture to create real code and memory worktrees and commits
and, with `publish_closeout_evidence=True`, write and reread a completed-closeout contract recording both commit IDs. `_landed_leaf_config` (`:113-124`) calls the integration application entry point with `strategy="ff-only"` and `dry_run=False` and asserts `integrated`. `_finalize` (`:133-137`) calls the finalization application entry point.

- `test_a_torn_down_provider_runtime_finalizes_on_the_first_call` (`:140-197`) reproduces the L6
  shape. The fixture ensures the provider-runtime tree is absent, then supplies the teardown double with
  `providerRuntime: {"removed": False, "reason": "already-absent"}`. The first and only finalize call must complete the edge with `state: finalized`,
  `cleanup-completed`, an empty `notRemoved` inventory over all four target kinds, the code worktree and
  enclosure root absent, the contract cell `completed`, and the leaf document `Completed`.
  **The L6 payload is reproduced through the provider port boundary rather than by triggering the
  original physical event**: the case substitutes the port's own answer instead of re-enacting a
  prior real reclaim, so it pins the decision the tool makes given that answer, not the physical
  history that produced the reported payload.
- `test_a_provider_runtime_that_cannot_be_torn_down_blocks_with_its_own_reason` (`:200-256`) is the
  genuine counterpart. A real permission failure (`chmod 0o500`, no reclaim image configured) leaves
  the provider-runtime tree in place, and the refusal must be `cleanup-blocked` / `blocked`, must
  report `removed: False` with the reason `remove_tree` produces (beginning with `permission denied`), must
  carry exactly that one blocker with that same reason, must close nothing (the leaf document is not
  `Completed`, the contract `cleanup` cell is still `pending`, the worktree and the provider tree are
  still on disk). The retry repeats the blocked state and the blocker list, and the document still lacks Completed status.

**The two invariant owners directly.** These cases need no tool call.

- `test_a_reasonless_provider_result_is_named_instead_of_becoming_a_null_reason` (`:259-279`) is the
  exact L6 input — `{"state": "torn-down", "providerRuntime": {"removed": False}}` — and asserts the
  one blocker names `no reason reported by the terminal result`.
- `test_an_unnameable_blocker_reason_is_refused_at_its_own_source` (`:282-295`) asserts `_blocker`
  raises `RuntimeError` naming the component for `None`, `""`, `"   "` and `17`.
- `test_an_empty_provider_reason_is_replaced_by_a_named_statement` (`:298-321`) pins that a blank
  producer reason — which `_blocked` correctly still reads as a blockage — cannot reach an operator
  as `reason: ""`.
- `test_remove_tree_answers_with_a_reason_whenever_it_reclaimed_nothing` (`:324-347`) exercises the removal producer: `already-absent` for a path that is not there, and a plain
  `{"removed": True}` with no reason for a real removal.
- `test_a_reclaimed_but_surviving_provider_runtime_reports_why_it_survived` (`:350-388`) drives the
  branch that could answer silently: the first `rmtree` raises `PermissionError`, the ownership
  reclaim double reports success, the second removal returns without removing the tree, and the surviving tree must report
  `still present after docker ownership reclaim` alongside `reclaimedViaDocker: True`.

### Conventions

The `bound_worktree_services` fixture (`:97-105`) rebinds the worktree services with a
`citation_guard` double (`_NoManagedCitationCache`, `:77-93`) whose `guard` returns production's own
authority-free `TerminalNamespaceGuard(None, None, None)`; only the cache reservation is a double, and
it is the value production yields for a fixture leaf with no managed cache namespace. The module is
marked `pytest.mark.integration` and drives real disposable repositories and real worktrees under
`tmp_path`.

Assertions are made on the operator-visible payload and on the filesystem, not on internal call
counts: the empty `notRemoved` inventory, the closed task edge, the surviving files, and the exact
blocker list are each measured. The L6 case substitutes only the teardown answer the provider port
would have returned. The case also uses the shared worktree service fixture and its citation-guard double.

### Invariants And Boundaries

- The cases pin what the change makes **impossible**, not a new capability. A reasonless blocker can
  no longer be constructed, and a surviving non-removal now names its cause; `remove_tree`'s ability
  to reclaim a tree, and cleanup's ability to reclaim an enclosure, are unchanged.
- A genuinely blocked teardown still blocks, with its own reason and its own partial inventory. The
  permission-failure case exists so the stricter builder cannot be read as turning every refusal into
  a success, and its retry assertion exists so a blockage cannot be retried into success.
- The already-absent provider shape is asserted to finalize on the first call, and the case that
  never reclaims is asserted to refuse twice.
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


- Public abandon preview returns would-abandon with no blockers and leaves the fixture’s code worktree in place. [1]


- The injected already-absent teardown response allows one finalize call to complete. The case checks four empty notRemoved lists, absence of the code worktree and enclosure root, and completion of the contract and task document. [2]

- The permission-failure fixture preserves the task document state, pending cleanup, code worktree and provider-runtime path. Its retry repeats the blocked state and exact blocker list. [3]
- The exact L6 input — `{"removed": False}` with no reason — is answered in operator language instead of becoming a null reason. [4]
- An unnameable blocker reason raises at the call site that detected it. [5]

- Public abandon preview returns would-abandon with no blockers and leaves the fixture’s code worktree in place. [6]


- The injected already-absent teardown response allows one finalize call to complete. The case checks four empty notRemoved lists, absence of the code worktree and enclosure root, and completion of the contract and task document. [7]

- The permission-failure fixture preserves the task document state, pending cleanup, code worktree and provider-runtime path. Its retry repeats the blocked state and exact blocker list. [8]
- The exact L6 input — `{"removed": False}` with no reason — is answered in operator language instead of becoming a null reason. [9]
- An unnameable blocker reason raises at the call site that detected it. [10]
- A blank producer reason cannot reach an operator as `reason: ""`. [11]
- The direct removal test checks the absent-path reason and the removed result for an existing path. [12]
- The post-reclaim branch that could answer silently now names its own cause. [13]


- The landed fixture and the public calls the whole-tool cases drive. [14]




- The service rebinding and the citation-guard double the whole-tool cases run against. [15]


- The only construction path for a terminal blockage; it refuses a missing, blank or non-string reason. [16]
- The operator-language answer for a reasonless or malformed result item. [17]
- The bundle and the builder the invariant-owner cases drive directly. [18]
- The producer whose reason the refusal carries, including the post-reclaim branch this module forces. [19]


- The port the L6 teardown answer is substituted on, and the services builder the fixture rebinds. Anchor: `ProviderLifecyclePort` `build_default_worktree_services` [20]




- The public terminal route the whole-tool cases call. [21]




- The landing fixture and the public configuration the whole-tool cases build on. [22]



- The landing fixture and the public configuration the whole-tool cases build on. [24]

### Cross-Repo References

The two finalize cases and the tool-level cleanup preview build disposable code and external memory Git repositories under `tmp_path`. The helper-level cases exercise typed results or provider-runtime fixtures directly.


### Repo-Internal References (continued)


- The landing world each whole-tool case builds is a real temporary repository pair. [27]



## Drift-Snapshot Preview Cases

The module has **489 physical lines** and **ten source test definitions**. Its preview definitions are:

`test_a_drift_snapshot_preview_is_not_read_as_an_unreclaimed_result` (`:391-427`) drives the drift-snapshot expectation directly with `preview=True` and requires the entry to be pending rather than blocked; `test_a_real_reasonless_drift_snapshot_still_refuses_rather_than_passing_as_preview` (`:430-451`) preserves the real reasonless refusal; and `test_the_cleanup_preview_of_a_task_with_a_drift_snapshot_reports_no_blocker` (`:454-489`) drives the tool-level cleanup preview. These are static source-definition locations, not a fresh execution result.


- The integration lane selects mcp/tests/test_terminal_blocker_reasons.py. Execution evidence is recorded separately. [23]

- The lane manifest declares test_terminal_blocker_reasons.py in integration. Membership selects evidence and establishes no invocation. [25]






- Twelve exact artifact consumer lists in the lifecycle catalog name this module. The dependency-ownership reader consumes the catalog for selection. [28]
