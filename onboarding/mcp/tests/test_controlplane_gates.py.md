# test_controlplane_gates.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_controlplane_gates.py`           |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-07T22:45:00+02:00               |
| lastVerifiedCommitHash | `100b40d6be4a7d03eedbb1164ce54e2e8a314038`       |
| lastVerifiedCommitDate | 2026-08-14T08:23:37+02:00|
| governingOverview      | `overview.md`                                    |

## Purpose

Unit tests for the gate control plane: the `GateRecord` / `GateStore`
records-and-store layer and the `gate_*` payload builders (slice 6a), plus the
closeout-gate enforcement policy and its wiring (slice 6b).

## Code Commentary

The record and payload entry points are addressed through parameter objects: `create_gate` takes the
kind positionally plus `anchor=GateAnchor(lifecycle_id=…, enclosure=…)` and
`request=GateRequest(packet=…, evidence_refs=…)`; `decide_gate` and every `gate_decide*` builder take
`GateVerdict(decision=…, by=…, via=…, note=…, deciding_role=…)`; `lifecycle_gate_payload` takes a
`GateRaise(kind=…, anchor=…, request=…, ask=…)`; and every waiting builder takes
`GateWait(block=…, timeout_seconds=…, poll_seconds=…, sleep=…, monotonic=…)`, whose `block=False` is
the raise-and-continue mode this card calls `wait=false`. The supporting fixtures moved the same way:
inbox rows are seeded with `create_operator_inbox_entry(InboxMessage(…),
routing=InboxRouting(address=InboxAddress(…)), poster=InboxPoster(…))`, the ambient lifecycle is
installed as `AmbientLifecycle(events, timing=AmbientTiming(heartbeat_seconds=3600))`, and the
projection assertion calls `project_workspace(logs, structure=WorkspaceStructure(enclosures=[],
providers=[]), now=…, given=AnalyticalInputs(gates=…))`.

`GateRecordTests` covers `create_gate` / `decide_gate` purity (same id, new ts,
original snapshot untouched) and the `schema`-alias wire round-trip
(`model_validate_json` of a `by_alias` dump). `GateStoreTests` covers
append/read history plus `current()` last-wins fold, the missing-log empty read,
and `log_path` routing (lifecycle vs workspace). `GateToolTests` patches
`gates._store` over a temp `GateStore` and drives create → decide (attribution
recorded), omitted-lifecycle gate creation binding to the active ambient lifecycle, omitted-lifecycle
creation failing when no ambient lifecycle is active, unknown-decision `ValueError`, missing-gate
`KeyError`, `gate_wait`
returning on a decision and timing out while `open` (injected `sleep` /
`monotonic`), and `gate_list` folding. Task 25 adds `lifecycle_gate_payload`
coverage proving one public call expires an older open gate, creates the durable
gate, blocks the lifecycle with the ask, waits by default until a developer
decision, ignores unrelated lifecycle-scoped inbox rows, rejects an explicit lifecycle-id
mismatch, and projects both the blocked ask and current gate row from the
resulting event/gate stores.

Slice 6b adds: `GateToolTests` also covers `gate_decide_for_lifecycle` (decides
the newest open gate; `KeyError` with no open gate; unknown-decision
`ValueError`). Task 19 extends this with single-current-gate semantics
(`gate_create_payload` expires older open gates), targeted lifecycle decisions
with notes, stale expected gate rejection, `gate_wait_payload` returning
decision notes, and `gate_response_wait_payload` returning matching pending
operator-inbox entries without consuming them. Task 23/24 extends this coverage so cancel physically
deletes a gate and associated inbox entries, waiting on a deleted gate returns `state="cancelled"`, and
non-enforcement gates are deleted after `gate_response_wait` returns their terminal decision. `ApplyGateTests` covers `apply_gate` (state → `applied`,
attribution preserved, source snapshot untouched). `EvaluateCloseoutGateTests`
exercises every branch of the pure `evaluate_closeout_gate` policy (gateless
permits, non-closeout kinds ignored, open/rejected/applied block,
developer-approved permits, **model-approved blocks**, latest gate governs). Its
`_closeout_gate` fixture now takes one `decision: Decider` instead of loose
`by`/`via`/`deciding_role`/`note`/`evidence_refs` keywords: `Decider` is a test-local frozen
dataclass holding who decides and what they attach, with `verdict(verb)` assembling the production
`GateVerdict` around the verb under test. The named deciders keep the policy's actor/surface/role
triple from being respelled per case — `BY_DEVELOPER`, `BY_MODEL`, `BY_MANAGER` (orchestration
surface + manager role + a non-owning actor) and `BY_OWNING_MANAGER` (the gate's own
`OWNER_LIFECYCLE` claiming the manager role, i.e. self-approval) — and `dataclasses.replace` varies
one field for the reviewer-verdict and rejection-note cases.
cit:([`CloseoutEnforcementHelperTests`], mcp/tests/test_controlplane_gates_closeout.py:191-262) drives `closeout.py`'s closeout-gate helpers over a
temp `GateStore` rooted at a stub contract's `coordination_root`. **Since 260731-EFA-L5 R2 the
helper under test is `_claim_closeout_gate` (cit:([`_claim_closeout_gate`], mcp/src/agents_remember/worktrees/modules/closeout.py:510-560)), and
`_mark_closeout_gate_applied` no longer exists — it was deleted rather than deprecated**, so there
is no second, later step for a test to call and no arrangement of two lines that leaves the
approval spendable in between. `test_gateless_lifecycle_returns_none`,
`test_open_gate_blocks_closeout`, `test_model_approved_blocks_closeout` and
`test_developer_approved_permits_and_marks_applied` all target the claim now; the last one asserts
the gate reads `applied` immediately after the single permitting call.

The two blocking cases **additionally** assert that the early refusal
`_refuse_unsatisfied_closeout_gate` (cit:([`_refuse_unsatisfied_closeout_gate`], mcp/src/agents_remember/worktrees/modules/closeout.py:518-540)) raises for the same seeded gate. That
is a second rung, not a duplicate: the claim sits one statement above the first irreversible act
(`closeout_result`, cit:([`closeout_result`], mcp/src/agents_remember/worktrees/modules/closeout.py:1037-1131)), while the early read sits before staging and the strict code-quality gate
(`gate_staged_code`, cit:([`gate_staged_code`], mcp/src/agents_remember/worktrees/modules/closeout_staged_quality.py:77-129)), so without it an unapproved closeout would only be refused after a full quality run over a
staged worktree. The early rung is safe precisely because it can only DENY — its read is unlocked
and therefore already stale when it returns, but a stale refusal costs a rerun and consumes
nothing, and a stale permit is re-evaluated under the lock by the claim.

**What the claim changed underneath these tests.** `GateStore.claim_approval` (cit:([`claim_approval`], mcp/src/agents_remember/controlplane/store.py:190-234)) folds the log, evaluates the policy and appends the `applied` snapshot inside **one**
held `exclusive_access`, so `approved -> applied` is a compare-and-swap against every other writer
and exactly one caller can both see the gate approved and be the one that marks it consumed. The
consequence is a deliberate semantic change worth stating plainly: **an approval now authorises one
attempt, not one success.** A closeout that dies after the claim — crashed process, failed memory
quality gate, git error, ENOSPC — leaves the approval consumed and the next closeout needs a fresh
gate. That is the fail-closed side of a trade whose alternative is not milder: marking applied at
the end means every way that late write can fail to land leaves a live approval sitting on top of
completed, irreversible work.
260703-L4 extends the suite with gate policy and evidence coverage: record
helpers append reviewer-verdict refs and orchestration attribution,
`gate_decide_payload` records active-lifecycle deciding identity, rejects owner
self-approval and missing required verdicts before append, projections surface
evidence refs, and the pure resolver blocks/permits manager delegated closeout
approvals according to `GatePolicy`.

## Invariants And Boundaries

- Pure units + a patched store; no live config / observer is needed. The
  dev-time conformance suite separately exercises the real config-rooted builders
  against a fixture workspace.
- The two rungs must stay distinguishable. `_refuse_unsatisfied_closeout_gate` decides nothing and
  writes nothing; `_claim_closeout_gate` is the only thing that spends an approval. A test that
  asserted only one of them would pass while the other was deleted, and deleting the claim is the
  check-then-act defect this leaf was called in to remove.
- Nothing outside `GateStore.claim_approval` may append an `applied` snapshot for an enforcement
  path. That is what makes "one approval" a property of the store rather than of a
  call ordering in `closeout.py`.
- **An `applied` `closeout-approval` record is no longer reclaimable garbage, so it cannot be used
  as fixture filler.** Since R1, `applied` snapshots of a `CONSUMED_APPROVAL_GATE_KINDS` kind are
  retained at any age — they are the authority record that stops one approval being spent twice.
  Three fixtures across the suite had been seeding exactly such a record purely as something for a
  reclaim pass to drop, and retaining them would have quietly turned those harnesses into no-ops:
  a compaction with nothing prunable does not rewrite, so the concurrency they exist to exercise
  would never happen and both halves of the affected tests would pass for the wrong reason. All
  three moved to `expired` (which is in `PRUNE_IMMEDIATE_GATE_STATES`): `_store_durability.py`'s
  `GateAdapter.write_decoy` (cit:([`GateAdapter`], mcp/tests/_store_durability.py:191-218)), `test_durable_store_contract.py`'s
  `GateReclaimOwnershipTests.setUp` (cit:([`GateReclaimOwnershipTests`], mcp/tests/test_durable_store_contract.py:854-918)), and `test_gate_replay_window.py`'s `_prunable_gate`
  (cit:([`_prunable_gate`], mcp/tests/test_gate_replay_window.py:116-130)) — the last of which also moved off `closeout-approval` onto `alarm-ack`, a kind
  nothing decides on. Each carries the reasoning in a comment at the fixture rather than in a
  commit message.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The records under test. | `GateRecord`; `create_gate`; `decide_gate`; `apply_gate` | mcp/src/agents_remember/controlplane/records.py:45-77; mcp/src/agents_remember/controlplane/records.py:127-149; mcp/src/agents_remember/controlplane/records.py:152-177; mcp/src/agents_remember/controlplane/records.py:185-194 |
| The store under test, and since 260731-EFA-L5 the only way to spend an approval: `claim_approval` folds, evaluates policy and appends the `applied` snapshot inside one held lock. | `claim_approval` | mcp/src/agents_remember/controlplane/store.py:190-234 |
| The payload builders under test. | `gate_create_payload`; `lifecycle_gate_payload`; `gate_decide_payload`; `gate_wait_payload`; `gate_response_wait_payload`; `gate_list_payload` | mcp/src/agents_remember/mcp/tools/gates.py:44-54; mcp/src/agents_remember/mcp/tools/gates.py:57-63; mcp/src/agents_remember/mcp/tools/gates.py:92-109; mcp/src/agents_remember/mcp/tools/gates.py:158-168; mcp/src/agents_remember/mcp/tools/gates.py:171-188; mcp/src/agents_remember/mcp/tools/gates.py:191-196 |
| The operator inbox store polled by `gate_response_wait_payload`. | `gate_response_wait_payload` | mcp/src/agents_remember/mcp/tools/gates.py:171-188 |
| The enforcement policy under test (slice 6b): `evaluate_gate`, whose `applied` branch is the refusal a second consume meets and the reason the `applied` snapshot is an authority record. | `evaluate_gate` | mcp/src/agents_remember/controlplane/enforcement.py:52-94 |
| Gate delegation policy under test. | `make_gate_policy`; `named_gate_policy`; `apply_seam_verdict_requirement`; `delegated_decision_failure_reason`; `approval_failure_reason` | mcp/src/agents_remember/controlplane/gate_policy.py:52-64; mcp/src/agents_remember/controlplane/gate_policy.py:67-83; mcp/src/agents_remember/kernel/primitives/gate_policy.py:75-107; mcp/src/agents_remember/kernel/primitives/gate_policy.py:110-127; mcp/src/agents_remember/kernel/primitives/gate_policy.py:130-149 |
| The closeout helpers under test: the early deny-only read `_refuse_unsatisfied_closeout_gate` (called before staging and the strict gate) and the claim `_claim_closeout_gate` (one statement above the first irreversible act). `_mark_closeout_gate_applied` was deleted, not deprecated. | `_refuse_unsatisfied_closeout_gate`; `_claim_closeout_gate`; `closeout_result` | mcp/src/agents_remember/worktrees/modules/closeout.py:529-605; mcp/src/agents_remember/worktrees/modules/closeout.py:1031-1163 |
| The staged-quality owner called between those boundaries binds and certifies the accepted candidate. | "def gate_staged_code(" | mcp/src/agents_remember/worktrees/modules/closeout_staged_quality.py:77-129 |
| Why an `applied` `closeout-approval` record can no longer be used as reclaimable fixture filler: `CONSUMED_APPROVAL_GATE_KINDS` retains it at any age, and `PRUNE_IMMEDIATE_GATE_STATES` is what the three relocated decoys now use instead. | `CONSUMED_APPROVAL_GATE_KINDS`; `PRUNE_IMMEDIATE_GATE_STATES` | mcp/src/agents_remember/controlplane/interaction_retention.py:52-54; mcp/src/agents_remember/controlplane/interaction_retention.py:85-85 |
| The suite that pins the claim's position rather than its policy: the gate is already `applied` by the time `commit_if_dirty` runs, a failure upstream leaves it `approved`, and `_prunable_gate` is one of the three fixtures moved to `expired`. | `test_the_approval_is_already_consumed_when_the_first_commit_runs`; `_prunable_gate` | mcp/tests/test_gate_replay_window.py:116-130; mcp/tests/test_gate_replay_window.py:582-615 |
| The second and third relocated decoys, beside the ownership and durability assertions they keep honest: `GateAdapter.write_decoy` and its enclosing adapter. | `GateAdapter` | mcp/tests/_store_durability.py:191-218 |
| The durable-store ownership fixture that also carries the relocated decoy. | `GateReclaimOwnershipTests` | mcp/tests/test_durable_store_contract.py:854-918 |
| The conformance suite that also covers the gate tools. | `ToolResponseConformanceTests` | mcp/tests/test_tool_response_conformance.py:639-734 |

As of the 260703-L8 seam ruling the suite carries MasterHandoverSeamTests: delegability to the orchestrator, the named-policy routing, human-pinned kinds staying pinned, apply_seam_verdict_requirement binding only delegated seam rules, verdict-evidence refusal/acceptance on a delegated handover decision, and owner-never-self-approves on the handover kind.

As of cycle 5 SeamChannelTests exercises the seam end-to-end at the payload layer: wait=false raise (and its refusal for undelegated kinds), cross-lifecycle decide by packet-carried gate id with orchestration attribution, verdict-evidence requirement, cli refusal on delegated kinds, raiser cancel, and evaluate_gate over the handover kind. Cycle 6 tightens the refusal coverage (an all-human refusal now also asserts no orphan gate persists and no sibling is expired — validate-then-mutate; a delegated-but-non-seam kind like plan-approval is refused too) and adds `HandoverEnforcementHelperTests`: the integrate-side `handover_gate_guard` over a cross-lifecycle `GateStore.all_current()` fold — open-on-foreign-lifecycle blocks, policy-valid approval permits, the CONFIGURED policy (not `DEFAULT_GATE_POLICY`) governs, gateless/unaddressed permits, `parent_task_name` addressing works, and `worktree_integrate_tool` is inspected to construct `WorktreeArgs` with `config.orchestration.gate_policy`. `GateToolTests` also covers the ambient-defaulting `gate_list_payload` (ambient → that lifecycle's gates; no ambient → workspace). Since 260707-HFX2-L11 the bare `SimpleNamespace` fake config
this test constructs also carries a `retirement=SimpleNamespace(auto_land_on_integration=False)`
attribute: `worktree_integrate_tool` reads `config.retirement.auto_land_on_integration`
unconditionally on a successful non-dry-run integrate, so without this the fake would raise
`AttributeError` the moment the new auto-land branch is reached; setting it `False` keeps the
landing hook orthogonal to this test's gate-policy-plumbing focus and disabled against the
fake's unattached contract. Cycle 7 adds three layers on the enclosure address: SeamChannelTests proves an enclosure-less/blank wait=false raise refuses BEFORE mutation (no orphan gate, sibling not expired) and that a raised gate carries its address; HandoverEnforcementHelperTests covers the pure `unmatched_handover_gate_warning` (foreign-enclosure open gate warns with gateId+enclosure, no-handover-gates and matched/decided cases stay silent); and `IntegrateDryRunGuardTests` drives `integrate_result(dry_run=true)` with the git steps mocked over a REAL cross-lifecycle store, asserting the preview carries `handover_gate` (permitted/gateId/reason), names `handover-gate-blocked` in the summary when the real run would refuse, carries the unmatched-gate warning, and never calls `write_contract`; its mocked `_integration_replay_requirements` now returns an `IntegrationSources(current_code_source=…, current_memory_source=…, code_replay_required=…, memory_replay_required=…)` object rather than a bare four-tuple.

## Update History
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: this test module was split in place into a family under 1,200 lines (L7-R5); the card remains the family entry point and the name set was reconciled item for item. Verification metadata stays pinned until closeout stamps the 260731-EFA-L7 commit.
- 2026-08-03T02:57+02:00 — W3-B03 curator: curated 12 table citations and 14 prose citation repairs for gate records, policy, closeout ordering, retention fixtures, and conformance coverage; fixer-generated ranges verified.

- 2026-08-01T16:30+02:00 — 260731-EFA-L5 curator: cit:([`CloseoutEnforcementHelperTests`], mcp/tests/test_controlplane_gates_closeout.py:191-262) now
  exercises `_claim_closeout_gate` (cit:([`_claim_closeout_gate`], mcp/src/agents_remember/worktrees/modules/closeout.py:510-560)) wherever it used to call
  `_enforce_closeout_gate`, and the two blocking cases **additionally** assert that
  `_refuse_unsatisfied_closeout_gate` (cit:([`_refuse_unsatisfied_closeout_gate`], mcp/src/agents_remember/worktrees/modules/closeout.py:518-540)) raises for the same seeded gate.
  `_mark_closeout_gate_applied` was **deleted rather than deprecated**, so
  `test_developer_approved_permits_and_marks_applied` no longer calls a second step — it asserts the
  gate reads `applied` straight after the single permitting call, which is the point: permitting and
  marking applied are one step and there is no arrangement of two lines that leaves the approval
  spendable in between. Recorded the two rungs as distinct rather than redundant — the claim sits
  one statement above the first irreversible act (cit:([`closeout_result`], mcp/src/agents_remember/worktrees/modules/closeout.py:1037-1131)) while the early read sits
  before staging and the strict code-quality gate (cit:([`gate_staged_code`], mcp/src/agents_remember/worktrees/modules/closeout_staged_quality.py:77-129)), and the early rung is safe only because it
  can exclusively DENY: its unlocked read is stale on return, but a stale refusal costs a rerun and
  consumes nothing while a stale permit is re-evaluated under the lock. Recorded the mechanism
  underneath: `GateStore.claim_approval` (cit:([`claim_approval`], mcp/src/agents_remember/controlplane/store.py:190-234)) folds, evaluates policy
  and appends the `applied` snapshot inside **one** held `exclusive_access`, making
  `approved -> applied` a compare-and-swap, and with it the deliberate semantic change — **an
  approval now authorises one attempt, not one success** — together with why the fail-closed side is
  the correct trade rather than the harsher one. **Also recorded where the fixture churn fits:**
  three fixtures across the suite had been seeding an `applied` `closeout-approval` record purely as
  something for a reclaim pass to drop, and since R1 such a record is retained at any age
  (`CONSUMED_APPROVAL_GATE_KINDS`), so leaving them would have made a compaction with nothing
  prunable skip its rewrite and quietly turn those harnesses into no-ops. All three moved to
  `expired`: `_store_durability.py::GateAdapter.write_decoy` (cit:([`GateAdapter`], mcp/tests/_store_durability.py:191-218)),
  `test_durable_store_contract.py::GateReclaimOwnershipTests.setUp` (cit:([`GateReclaimOwnershipTests`], mcp/tests/test_durable_store_contract.py:854-918)) and
  `test_gate_replay_window.py::_prunable_gate` (cit:([`_prunable_gate`], mcp/tests/test_gate_replay_window.py:116-130)), the last also moving off
  `closeout-approval` onto `alarm-ack`. **Citations:** every range added here was opened and checked
  against each symbol the claim names, ends included — cit:([`evaluate_gate`], mcp/src/agents_remember/controlplane/enforcement.py:52-94) with its `applied`
  branch, both closeout helpers with their call sites, and each of the three fixtures.
  The reference table is two-column by construction, so citations are carried inline in the Finding
  cells rather than by widening it. Verification metadata untouched.
- 2026-07-31T16:50+02:00 — 260731-EFA-L2 code-quality gate: the whole gate substrate moved its
  loose arguments into parameter objects, so this suite now calls `create_gate` with `GateAnchor`
  + `GateRequest`, `decide_gate` and every `gate_decide*` builder with `GateVerdict`,
  `lifecycle_gate_payload` with `GateRaise`, and every waiting builder with `GateWait` — whose
  `block=False` is the raise-and-continue mode this card had been calling `wait=false` as a
  keyword. Added a Code Commentary paragraph naming those shapes plus the moved fixture calls
  (`create_operator_inbox_entry` through
  `InboxMessage`/`InboxRouting`/`InboxAddress`/`InboxPoster`, `AmbientLifecycle` through
  `AmbientTiming`, `project_workspace` through `WorkspaceStructure` and `AnalyticalInputs`).
  Documented the new test-local `Decider` frozen dataclass and its `BY_DEVELOPER` / `BY_MODEL` /
  `BY_MANAGER` / `BY_OWNING_MANAGER` constants, which replaced `_closeout_gate`'s loose
  `by`/`via`/`deciding_role`/`note`/`evidence_refs` keywords, and recorded that
  `IntegrateDryRunGuardTests` now mocks `_integration_replay_requirements` to an
  `IntegrationSources` object instead of a four-tuple. No test case was added, removed, or
  renamed, and the closeout-policy branches, the seam refusals, and the handover-guard assertions
  are unchanged.
- 2026-07-09T14:05+02:00 — 260707-HFX2-L11 curator correction: updated the handover fake-config
  note from `auto_retire_on_integration` to `auto_land_on_integration`; the hook remains disabled
  so gate-policy plumbing tests stay focused. Verification metadata pinned until closeout stamps
  the HFX2-L11 commit.
- 2026-07-08T02:43+02:00 — 260707-HFX-L8 (seat lifecycle: retirement + live identity +
  turn-state): updated the pre-existing `HandoverEnforcementHelperTests` fake `SimpleNamespace`
  config to add a `retirement=SimpleNamespace(auto_retire_on_integration=False)` attribute, needed
  now that `worktree_integrate_tool` reads `config.retirement.auto_retire_on_integration`
  unconditionally on success; without it the fake would raise `AttributeError` once the new
  auto-retire branch is reached. Not a new test — a required update to an existing one. Verification
  metadata pinned until closeout stamps the HFX-L8 commit.
- 2026-07-05T19:55+02:00 - L8 builder cycle 7: enclosure-required raise refusal (AR4-1a), unmatched-open-gate warning helper tests (AR4-1b), and IntegrateDryRunGuardTests for the guard-reporting, non-persisting dry run (AR4-2). Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T19:10+02:00 - L8 builder cycle 6: HandoverEnforcementHelperTests (7 tests), wait=false refusal hygiene + seam-kind restriction coverage, ambient gate_list tests. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T18:20+02:00 - L8 seam channel (cycle 5): SeamChannelTests added (7 tests). Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T16:30+02:00 - L8 seam-ruling remediation (cycle 4): MasterHandoverSeamTests added (6 tests). Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-04T12:32+02:00 — 260703-L4: added coverage for delegated
  orchestration attribution, no owner self-approval, reviewer-verdict evidence
  requirements, projection evidence refs, and policy-aware closeout enforcement.
  Verification metadata pinned until closeout stamps the L4 commit.
- 2026-06-26T18:43+02:00 — Regression coverage: `lifecycle_gate_payload`
  tests now prove the public default waits through unrelated lifecycle inbox
  rows and returns only after the newly opened gate is decided.
- 2026-06-26T17:05+02:00 — Regression coverage: `lifecycle_gate_payload`
  tests now prove the public junction waits internally, including a timeout path
  and a developer-decision path, instead of merely returning initialized wait
  metadata.
- 2026-06-26T14:16+02:00 — Task 25: added unified `lifecycle_gate_payload` coverage while retaining split-builder tests as lower-level compatibility coverage.
- 2026-06-25T14:02+02:00 — Task 24 reopened: added tests that `gate_create_payload(lifecycle_id=None)` binds to active ambient lifecycle and rejects creation without an active lifecycle.
- 2026-06-25T13:20+02:00 — Task 23/24: added tests for cancel/delete semantics, deleted-gate waits returning cancelled, and post-wait deletion of non-enforcement gates.
- 2026-06-25T07:17+02:00 — Task 19: added tests for expiring superseded open lifecycle gates, targeted lifecycle decisions with notes and stale expected gate ids, `gate_wait` decision-note payloads, and `gate_response_wait` returning matching inbox entries without consuming them. Verification metadata pinned until closeout stamps the task-19 code commit.
- 2026-06-18T12:10+02:00 — Task 6 slice 6b: added tests for `gate_decide_for_lifecycle`, `apply_gate`, the pure `evaluate_closeout_gate` policy (all branches, incl. model-approved-blocks), and the `closeout.py` enforcement helpers. Verification metadata pinned until closeout stamps the 6b code commit.
- 2026-06-18T01:05+02:00 — Created for task 6 slice 6a: gate substrate + tool unit tests. Verification metadata pinned until closeout stamps the 6a code commit.
