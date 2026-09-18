# mcp/tests/test_terminal_blocker_reasons.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_terminal_blocker_reasons.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-14T20:00+02:00 |
| lastVerifiedCommitHash | `a135150459f8499ba309faf0373cc3b4bf7ff852`|
| lastVerifiedCommitDate | 2026-09-18T19:58:12+02:00|
| governingOverview | `overview.md` |

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

The cases are integration-lane members (`mcp/tests/test-evidence-lanes.toml`, entry row `:177`), and
the module is registered as a declared exact consumer of nine `mcp/tests/evidence-lifecycle.toml`
artifacts and of the ambient-role runner in `dependency_ownership.py`.

## Code Commentary

The existing first-call finalization case also calls public abandon preview before integration. It verifies `would-abandon`, an empty blocker list and an intact worktree, reproducing the omitted preview flag without adding a collected test case.

### Logic

Seven cases in two groups: two drive the whole public tool, five pin the two invariant owners
directly.

**The whole-tool boundary.** `_landed_leaf` (`:84-86`) builds a real applied landing from the shared
external-memory authority fixture with `publish_closeout_evidence=True`, `_landed_leaf_config`
(`:89-100`) completes the integration through the public `worktree_integrate_tool` under
`auto_land_on_integration=True` and asserts `integrated`, and `_finalize` (`:109-113`) calls the
public `lifecycle_finalize_task_tool`.

- `test_a_torn_down_provider_runtime_finalizes_on_the_first_call` (`:116-170`) reproduces the L6
  shape. The provider-runtime tree is deleted first, so the port answers the teardown with
  `providerRuntime: {"removed": False, "reason": "already-absent"}` — a provider already reclaimed is
  not a blockage. The first and only finalize call must finalize the edge: `state: finalized`,
  `cleanup-completed`, an empty `notRemoved` inventory over all four target kinds, both worktrees and
  the enclosure root really gone, the contract cell `completed`, and the leaf document `Completed`.
  **The L6 payload is reproduced through the provider port boundary rather than by triggering the
  original physical event**: the case substitutes the port's own answer instead of re-enacting a
  prior real reclaim, so it pins the decision the tool makes given that answer, not the physical
  history that produced the reported payload.
- `test_a_provider_runtime_that_cannot_be_torn_down_blocks_with_its_own_reason` (`:173-229`) is the
  genuine counterpart. A real permission failure (`chmod 0o500`, no reclaim image configured) leaves
  the provider-runtime tree in place, and the refusal must be `cleanup-blocked` / `blocked`, must
  report `removed: False` with the reason `remove_tree` produces (`permission denied: ...`), must
  carry exactly that one blocker with that same reason, must close nothing (the leaf document is not
  `Completed`, the contract `cleanup` cell is still `pending`, the worktree and the provider tree are
  still on disk), and must refuse identically on the retry. A retry may converge only by re-observing
  the cause as resolved; this one does not become success.

**The two invariant owners directly.** These cases need no tool call.

- `test_a_reasonless_provider_result_is_named_instead_of_becoming_a_null_reason` (`:232-252`) is the
  exact L6 input — `{"state": "torn-down", "providerRuntime": {"removed": False}}` — and asserts the
  one blocker names `no reason reported by the terminal result`.
- `test_an_unnameable_blocker_reason_is_refused_at_its_own_source` (`:255-268`) asserts `_blocker`
  raises `RuntimeError` naming the component for `None`, `""`, `"   "` and `17`.
- `test_an_empty_provider_reason_is_replaced_by_a_named_statement` (`:271-294`) pins that a blank
  producer reason — which `_blocked` correctly still reads as a blockage — cannot reach an operator
  as `reason: ""`.
- `test_remove_tree_answers_with_a_reason_whenever_it_reclaimed_nothing` (`:297-320`) pins the sole
  producer of that field: `already-absent` for a path that is not there, and a plain
  `{"removed": True}` with no reason for a real removal.
- `test_a_reclaimed_but_surviving_provider_runtime_reports_why_it_survived` (`:323-361`) drives the
  branch that could answer silently: the first `rmtree` raises `PermissionError`, the ownership
  reclaim succeeds, the retry fails again, and the surviving tree must report
  `still present after docker ownership reclaim` alongside `reclaimedViaDocker: True`.

### Conventions

The `bound_worktree_services` fixture (`:73-81`) rebinds the worktree services with a
`citation_guard` double (`_NoManagedCitationCache`, `:59-69`) whose `guard` returns production's own
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

## Docs References

No Domain Documentation source is configured for this repository; the proving evidence is this
repository's own source, its own blocker vocabulary, and the operator payload it emits.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external source is required for this repository-owned blocker contract. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Public abandon preview is non-mutating and does not invent a removal failure. | `test_a_torn_down_provider_runtime_finalizes_on_the_first_call` | mcp/tests/test_terminal_blocker_reasons.py:116-170 |
| The L6 shape finalizes on the first call: the terminal archive is proven, the provider runtime is already gone, and an empty `notRemoved` inventory is reported. | `test_a_torn_down_provider_runtime_finalizes_on_the_first_call` | mcp/tests/test_terminal_blocker_reasons.py:116-170 |
| The genuine counterpart: a provider runtime that cannot be removed blocks with its own reason, closes nothing, and refuses identically on retry. | `test_a_provider_runtime_that_cannot_be_torn_down_blocks_with_its_own_reason` | mcp/tests/test_terminal_blocker_reasons.py:173-229 |
| The exact L6 input — `{"removed": False}` with no reason — is answered in operator language instead of becoming a null reason. | `test_a_reasonless_provider_result_is_named_instead_of_becoming_a_null_reason` | mcp/tests/test_terminal_blocker_reasons.py:232-252 |
| An unnameable blocker reason raises at the call site that detected it. | `test_an_unnameable_blocker_reason_is_refused_at_its_own_source` | mcp/tests/test_terminal_blocker_reasons.py:255-268 |
| A blank producer reason cannot reach an operator as `reason: ""`. | `test_an_empty_provider_reason_is_replaced_by_a_named_statement` | mcp/tests/test_terminal_blocker_reasons.py:271-294 |
| The sole provider-runtime producer answers with a reason whenever it reclaimed nothing. | `test_remove_tree_answers_with_a_reason_whenever_it_reclaimed_nothing` | mcp/tests/test_terminal_blocker_reasons.py:297-320 |
| The post-reclaim branch that could answer silently now names its own cause. | `test_a_reclaimed_but_surviving_provider_runtime_reports_why_it_survived` | mcp/tests/test_terminal_blocker_reasons.py:323-361 |
| The landed fixture and the public calls the whole-tool cases drive. | `_landed_leaf`; `_landed_leaf_config`; `_landed_leaf_document`; `_finalize` | mcp/tests/test_terminal_blocker_reasons.py:84-86; mcp/tests/test_terminal_blocker_reasons.py:89-100; mcp/tests/test_terminal_blocker_reasons.py:103-106; mcp/tests/test_terminal_blocker_reasons.py:109-113 |
| The service rebinding and the citation-guard double the whole-tool cases run against. | `bound_worktree_services`; `_NoManagedCitationCache` | mcp/tests/test_terminal_blocker_reasons.py:59-69; mcp/tests/test_terminal_blocker_reasons.py:72-81 |
| The only construction path for a terminal blockage; it refuses a missing, blank or non-string reason. | `_blocker` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:640-656 |
| The operator-language answer for a reasonless or malformed result item. | `_blocked_reason` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:625-637 |
| The bundle and the builder the invariant-owner cases drive directly. | `TerminalResult`; `terminal_result_blockers` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:229-243; mcp/src/agents_remember/worktrees/modules/terminal_validation.py:246-288 |
| The producer whose reason the refusal carries, including the post-reclaim branch this module forces. | `remove_tree` | mcp/src/agents_remember/application/provider_runtime.py:289-326 |
| The port the L6 teardown answer is substituted on, and the services builder the fixture rebinds. | `ProviderLifecyclePort`; `build_default_worktree_services` | mcp/src/agents_remember/worktrees/services.py:54-96; mcp/src/agents_remember/application/worktree_services.py:203-211 |
| The public terminal route the whole-tool cases call. | `lifecycle_finalize_task_tool` | mcp/src/agents_remember/application/worktree_tools.py:855-886 |
| The landing fixture and the public configuration the whole-tool cases build on. | `_authority_fixture`; `_closed_external_leaf_worktrees`; `_public_config` | mcp/tests/integration_branch_authority_test_support.py:48-91; mcp/tests/integration_branch_authority_test_support.py:129-296; mcp/tests/test_transaction_only_worktree_delivery.py:59-83 |
| The integration lane row the fail-closed manifest requires. | "integration = [" | mcp/tests/test-evidence-lanes.toml:128-200 |
| The exact-consumer declaration that gives this module ownership for targeted selection: this module's entry inside the ownership catalog's repository-test-input mapping. | "REPOSITORY_TEST_INPUT_CONSUMERS: dict[Path, frozenset[Path]]" | mcp/test_support/agents_remember_test_support/code_quality/dependency_ownership.py:56-184 |

## Cross-Repo References

Each case builds its own disposable code repository and external memory repository as real temporary
Git repositories under `tmp_path`, which is what lets the landing, integration and finalization
routes run at all. No production cross-repository authority is claimed by this focused module.

| Finding | Anchor | Source |
| --- | --- | --- |
| The landing world each whole-tool case builds is a real temporary repository pair. | `_authority_fixture`; `_closed_external_leaf_worktrees` | mcp/tests/integration_branch_authority_test_support.py:48-91; mcp/tests/integration_branch_authority_test_support.py:129-296 |

## Update History
2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `lifecycle_finalize_task_tool` repointed to mcp/src/agents_remember/application/worktree_tools.py:855-886. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-15T06:37:50+02:00 — LCA L9 terminal delivery: The existing first-call finalization case also calls public abandon preview before integration. It verifies `would-abandon`, an empty blocker list and an intact worktree, reproducing the omitted preview flag without adding a collected test case.


- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator (provenance repair): the gate could not compare
  this claim with its verification provenance because the anchor was a quoted path string that
  occurs many times in evidence-lifecycle.toml and twice in the ownership catalog, so no historical
  location was unique. Repaired the citations, not the claims: the lane row now anchors the lane
  block that declares this module, and the ownership row anchors the repository-test-input mapping
  that carries its entry. Verification metadata remains closeout-owned.
- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (citation pass): re-derived the source ranges of 1
  claim(s) whose anchor no longer sat in its cited range and normalised 3 further range(s) in this
  card from their anchors against the frozen source snapshot (`agents-remember memory-citations
  --fix --document`, snapshot 188b8ecd). No claim wording changed; every rewritten range was read
  back at its current position. Verification metadata remains closeout-owned.
- 2026-09-14T15:05+02:00 — 260913-LCA-L8 curator: created this one-to-one sidecar for the leaf's new
  integration module. Recorded the measured defect (a `providerRuntime` blockage with `reason: null`
  stopped a cleanup whose own payload proved the archive and an already torn-down provider runtime),
  the source diagnosis (the result-reading path turned a missing `reason` key into `None` and still
  counted the item as blocked, and `remove_tree`'s post-reclaim "still present" branch was the only
  producer able to answer `removed: False` with no reason), and the case-by-case proof: the L6 shape
  finalizes on the first call, a real permission failure blocks with its own reason and refuses
  identically on retry, and the two invariant owners are driven directly. Stated plainly that the L6
  payload is reproduced through the provider port boundary rather than by re-enacting the original
  physical event, and that the change makes a reasonless blocker unrepresentable without adding
  teardown capability. Recorded the registration the fail-closed manifest requires — the
  **integration** lane row at `mcp/tests/test-evidence-lanes.toml:177`, the nine exact-consumer rows
  in `mcp/tests/evidence-lifecycle.toml` (`:331`, `:391`, `:435`, `:565`, `:604`, `:643`, `:955`,
  `:1012`, `:1038`) and the `dependency_ownership.py:82` declaration for the ambient-role runner —
  all ownership accounting only, not execution or acceptance evidence. The metadata table records
  the branch base this card was derived against; no commit contains this file yet, closeout owns the
  real stamp, and no acceptance claim is made.
