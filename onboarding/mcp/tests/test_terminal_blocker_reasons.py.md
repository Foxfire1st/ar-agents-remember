# mcp/tests/test_terminal_blocker_reasons.py

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

`test_terminal_blocker_reasons.py` (260913-LCA-L8) pins the terminal blocker contract: a cleanup or
finalize blockage always names the component it stopped on and carries a non-empty reason, so a
blockage an operator cannot read — and cannot tell apart from a spurious one — is impossible to emit.

The measured defect: `lifecycle_finalize_task` on an enclosure returned `state: cleanup-blocked` with
`blockers: [{"provider": "providerRuntime", "reason": null}]`, while the same payload proved the
terminal archive, reported the providers `torn-down`, and said in its own summary that enclosure
deletion may continue. Cleanup stopped anyway, preserved the citation-source index with
`terminal-operation-failed`, and left the leaf un-finalized; an immediate retry then reclaimed
everything and finalized the edge. Read from source, the first call was wrong rather than stopping
for a cause the retry re-observed as resolved: the blocker was built in
`worktrees/modules/terminal_validation.py`, where a result dict with no `reason` key became `None`
and the item still counted as blocked, and the only producer able to hand it `{"removed": False}`
with no reason at all was `application/provider_runtime.py::remove_tree`'s post-reclaim
"still present" branch.

The cases are integration-lane members (`mcp/tests/test-evidence-lanes.toml`, entry row `:219`), and
the module is registered as a declared exact consumer of nine `mcp/tests/evidence-lifecycle.toml`
artifacts and of the ambient-role runner in `dependency_ownership.py`.

## Code Commentary

The existing first-call finalization case also calls public abandon preview before integration. It verifies `would-abandon`, an empty blocker list and an intact worktree, reproducing the omitted preview flag without adding a collected test case.

### Logic

Ten cases in two groups: two drive the whole public tool, five pin the two invariant owners
directly, and three (added by `260918-TSIP-L6`) hold the drift-snapshot preview repair.

**The whole-tool boundary.** `_landed_leaf` (`:102-106`) builds a real applied landing from the shared
external-memory authority fixture with `publish_closeout_evidence=True`, `_landed_leaf_config` (`:107-120`) completes the integration through the public `worktree_integrate_tool` under
`auto_land_on_integration=True` and asserts `integrated`, and `_finalize` (`:127-133`) calls the
public `lifecycle_finalize_task_tool`.

- `test_a_torn_down_provider_runtime_finalizes_on_the_first_call` (`:134-190`) reproduces the L6
  shape. The provider-runtime tree is deleted first, so the port answers the teardown with
  `providerRuntime: {"removed": False, "reason": "already-absent"}` — a provider already reclaimed is
  not a blockage. The first and only finalize call must finalize the edge: `state: finalized`,
  `cleanup-completed`, an empty `notRemoved` inventory over all four target kinds, both worktrees and
  the enclosure root really gone, the contract cell `completed`, and the leaf document `Completed`.
  **The L6 payload is reproduced through the provider port boundary rather than by triggering the
  original physical event**: the case substitutes the port's own answer instead of re-enacting a
  prior real reclaim, so it pins the decision the tool makes given that answer, not the physical
  history that produced the reported payload.
- `test_a_provider_runtime_that_cannot_be_torn_down_blocks_with_its_own_reason` (`:191-249`) is the
  genuine counterpart. A real permission failure (`chmod 0o500`, no reclaim image configured) leaves
  the provider-runtime tree in place, and the refusal must be `cleanup-blocked` / `blocked`, must
  report `removed: False` with the reason `remove_tree` produces (`permission denied: ...`), must
  carry exactly that one blocker with that same reason, must close nothing (the leaf document is not
  `Completed`, the contract `cleanup` cell is still `pending`, the worktree and the provider tree are
  still on disk), and must refuse identically on the retry. A retry may converge only by re-observing
  the cause as resolved; this one does not become success.

**The two invariant owners directly.** These cases need no tool call.

- `test_a_reasonless_provider_result_is_named_instead_of_becoming_a_null_reason` (`:250-272`) is the
  exact L6 input — `{"state": "torn-down", "providerRuntime": {"removed": False}}` — and asserts the
  one blocker names `no reason reported by the terminal result`.
- `test_an_unnameable_blocker_reason_is_refused_at_its_own_source` (`:273-288`) asserts `_blocker`
  raises `RuntimeError` naming the component for `None`, `""`, `"   "` and `17`.
- `test_an_empty_provider_reason_is_replaced_by_a_named_statement` (`:289-314`) pins that a blank
  producer reason — which `_blocked` correctly still reads as a blockage — cannot reach an operator
  as `reason: ""`.
- `test_remove_tree_answers_with_a_reason_whenever_it_reclaimed_nothing` (`:315-340`) pins the sole
  producer of that field: `already-absent` for a path that is not there, and a plain
  `{"removed": True}` with no reason for a real removal.
- `test_a_reclaimed_but_surviving_provider_runtime_reports_why_it_survived` (`:341-381`) drives the
  branch that could answer silently: the first `rmtree` raises `PermissionError`, the ownership
  reclaim succeeds, the retry fails again, and the surviving tree must report
  `still present after docker ownership reclaim` alongside `reclaimedViaDocker: True`.

### Conventions

The `bound_worktree_services` fixture (`:91-101`) rebinds the worktree services with a
`citation_guard` double (`_NoManagedCitationCache`, `:77-90`) whose `guard` returns production's own
authority-free `TerminalNamespaceGuard(None, None, None)`; only the cache reservation is a double, and
it is the value production yields for a fixture leaf with no managed cache namespace. The module is
marked `pytest.mark.integration` and drives real disposable repositories and real worktrees under
`tmp_path`.

Assertions are made on the operator-visible payload and on the filesystem, not on internal call
counts: the empty `notRemoved` inventory, the closed task edge, the surviving files, and the exact
blocker list are each measured. The L6 case substitutes only the teardown answer the provider port
would have returned; every other step is the production route.

### Invariants And Boundaries

- The cases pin what the change makes **impossible**, not a new capability. A reasonless blocker can
  no longer be constructed, and a surviving non-removal now names its cause; `remove_tree`'s ability
  to reclaim a tree, and cleanup's ability to reclaim an enclosure, are unchanged.
- A genuinely blocked teardown still blocks, with its own reason and its own partial inventory. The
  permission-failure case exists so the stricter builder cannot be read as turning every refusal into
  a success, and its retry assertion exists so a blockage cannot be retried into success.
- The retry-converges behaviour is explained rather than relied on: the first call was wrong, so the
  L6 shape is asserted to finalize on the first call, and the case that never reclaims is asserted to
  refuse twice.
- These are focused development cases over disposable coordination state. They are behaviour evidence
  for one contract, not full-suite certification or independent review, and this card records source
  inspection, not a test run.

### Todos

None recorded.

## Evidence

### Docs References

No Domain Documentation source is configured for this repository; the proving evidence is this
repository's own source, its own blocker vocabulary, and the operator payload it emits.

No external source is required for this repository-owned blocker contract.

### Repo-Internal References

- Public abandon preview is non-mutating and does not invent a removal failure. [1]
- The L6 shape finalizes on the first call: the terminal archive is proven, the provider runtime is already gone, and an empty `notRemoved` inventory is reported. [2]
- The genuine counterpart: a provider runtime that cannot be removed blocks with its own reason, closes nothing, and refuses identically on retry. [3]
- The exact L6 input — `{"removed": False}` with no reason — is answered in operator language instead of becoming a null reason. [4]
- An unnameable blocker reason raises at the call site that detected it. [5]
- Public abandon preview is non-mutating and does not invent a removal failure. [6]
- The L6 shape finalizes on the first call: the terminal archive is proven, the provider runtime is already gone, and an empty `notRemoved` inventory is reported. [7]
- The genuine counterpart: a provider runtime that cannot be removed blocks with its own reason, closes nothing, and refuses identically on retry. [8]
- The exact L6 input — `{"removed": False}` with no reason — is answered in operator language instead of becoming a null reason. [9]
- An unnameable blocker reason raises at the call site that detected it. [10]
- A blank producer reason cannot reach an operator as `reason: ""`. [11]
- The sole provider-runtime producer answers with a reason whenever it reclaimed nothing. [12]
- The post-reclaim branch that could answer silently now names its own cause. [13]
- The landed fixture and the public calls the whole-tool cases drive. [14]
- The service rebinding and the citation-guard double the whole-tool cases run against. [15]
- The only construction path for a terminal blockage; it refuses a missing, blank or non-string reason. [16]
- The operator-language answer for a reasonless or malformed result item. [17]
- The bundle and the builder the invariant-owner cases drive directly. [18]
- The producer whose reason the refusal carries, including the post-reclaim branch this module forces. [19]
- The port the L6 teardown answer is substituted on, and the services builder the fixture rebinds. [20]
- The public terminal route the whole-tool cases call. [21]
- The landing fixture and the public configuration the whole-tool cases build on. [22]
- The integration lane row the fail-closed manifest requires. [23]
- The landing fixture and the public configuration the whole-tool cases build on. [24]
- The integration lane row the fail-closed manifest requires. [25]
- The exact-consumer declaration that gives this module ownership for targeted selection: this module's entry inside the ownership catalog's repository-test-input mapping. [26]

### Cross-Repo References

Each case builds its own disposable code repository and external memory repository as real temporary
Git repositories under `tmp_path`, which is what lets the landing, integration and finalization
routes run at all. No production cross-repository authority is claimed by this focused module.

- The landing world each whole-tool case builds is a real temporary repository pair. [27]

## 260918-TSIP-L6 The Drift-Snapshot Preview Cases

This leaf added three cases (`:382-480`) to the module, and the module grew **361 → 480 lines**:
`test_a_drift_snapshot_preview_is_not_read_as_an_unreclaimed_result` (`:382-420`) drives the
drift-snapshot expectation directly with `preview=True` and requires the entry to be pending
rather than blocked; `test_a_real_reasonless_drift_snapshot_still_refuses_rather_than_passing_as_preview`
(`:421-444`) is the counterpart that keeps the repair from becoming a blanket success; and
`test_the_cleanup_preview_of_a_task_with_a_drift_snapshot_reports_no_blocker` (`:445-480`) drives
the *tool-level* cleanup preview, which is the route the defect was found on (`T62`/`D49`).

**Every line figure in this card's body and reference table is re-derived at this candidate**,
not shifted: the module's definitions moved because the new cases are appended at the end and the
`preview=result.preview` repair sits at `terminal_validation.py:285-292`. The case figures are
`_landed_leaf` `:102-106`, `_landed_leaf_config` `:107-120`, `_landed_leaf_document` `:121-126`,
`_finalize` `:127-133`, `test_a_torn_down_provider_runtime_finalizes_on_the_first_call`
`:134-190`, `test_a_provider_runtime_that_cannot_be_torn_down_blocks_with_its_own_reason`
`:191-249`, `test_a_reasonless_provider_result_is_named_instead_of_becoming_a_null_reason`
`:250-272`, `test_an_unnameable_blocker_reason_is_refused_at_its_own_source` `:273-288`,
`test_an_empty_provider_reason_is_replaced_by_a_named_statement` `:289-314`,
`test_remove_tree_answers_with_a_reason_whenever_it_reclaimed_nothing` `:315-340` and
`test_a_reclaimed_but_surviving_provider_runtime_reports_why_it_survived` `:341-381`. The module
now has **ten** cases, not seven, and its lane row is
`mcp/tests/test-evidence-lanes.toml:220` (it read `:177` when this card was written).
