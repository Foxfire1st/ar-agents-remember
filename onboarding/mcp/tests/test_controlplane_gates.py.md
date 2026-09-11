# test_controlplane_gates.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_controlplane_gates.py`           |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-09-06T21:38+00:00 |
| lastVerifiedCommitHash | `d36109038b3f2b500c138f9dc1ea9c9f9a247489`       |
| lastVerifiedCommitDate | 2026-09-06T22:21:49+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Gate-record snapshot purity, durable folding and shared tool fixture.

## Code Commentary

### Logic

create_gate returns an open snapshot; decide_gate preserves its ID and attributes the new decision without mutating the original. Appending both snapshots retains history while current folds last-wins. GateToolTests supplies temporary stores and a creation helper to the retained tool suites.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

This file no longer contains the historical closeout-enforcement matrix. Store snapshots and fixture gate creation do not grant closeout authority.

### Todos

No file-local implementation change is requested by this reconciliation.

## Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain evidence applies to the file-local claims above. | N/A | N/A |

## Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

| Finding | Anchor | Source |
| --- | --- | --- |
| Create and decide are pure snapshots. | `test_create_and_decide_are_pure_snapshots` | mcp/tests/test_controlplane_gates.py:40-59 |
| Append keeps history and current folds last wins. | `test_append_keeps_history_and_current_folds_last_wins` | mcp/tests/test_controlplane_gates.py:68-82 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## Update History

- 2026-09-06T21:38+00:00 — Reconciled the actual retained source after IAS test simplification at d3610903: corrected fixture/test roles, removed obsolete current-coverage claims and refreshed existing-source citations. Earlier entries remain historical; verification stamps remain closeout-owned.


- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1 candidate-11 curation rebind: refreshed formatter-moved source coordinates against accepted tree `4241908c`; where applicable, replaced a deleted coordinator anchor with the sole current owner. Verification metadata remains pinned until governed closeout.
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: this test module was split in place into a family under 1,200 lines (L7-R5); the card remains the family entry point and the name set was reconciled item for item. Verification metadata stays pinned until closeout stamps the 260731-EFA-L7 commit.
- 2026-08-03T02:57+02:00 — W3-B03 curator: curated 12 table citations and 14 prose citation repairs for gate records, policy, closeout ordering, retention fixtures, and conformance coverage; fixer-generated ranges verified.

- 2026-08-01T16:30+02:00 — 260731-EFA-L5 curator: cit:([`CloseoutEnforcementHelperTests`], mcp/tests/test_controlplane_gates_closeout.py:191-262) now
  exercises `_claim_closeout_gate` (cit:([`_claim_closeout_gate`], mcp/src/agents_remember/worktrees/modules/closeout.py:474-525)) wherever it used to call
  `_enforce_closeout_gate`, and the two blocking cases **additionally** assert that
  `_refuse_unsatisfied_closeout_gate` (cit:([`_refuse_unsatisfied_closeout_gate`], mcp/src/agents_remember/worktrees/modules/closeout.py:448-471)) raises for the same seeded gate.
  `_mark_closeout_gate_applied` was **deleted rather than deprecated**, so
  `test_developer_approved_permits_and_marks_applied` no longer calls a second step — it asserts the
  gate reads `applied` straight after the single permitting call, which is the point: permitting and
  marking applied are one step and there is no arrangement of two lines that leaves the approval
  spendable in between. Recorded the two rungs as distinct rather than redundant — the claim sits
  before the first journaled mutation intent and Git act (cit:([`_closeout_commit_phase`], mcp/src/agents_remember/worktrees/modules/closeout.py:869-927)) while the early read sits
  before staging and the strict code-quality gate (cit:([`gate_staged_code`], mcp/src/agents_remember/worktrees/queue/closeout_staged_quality.py:77-129)), and the early rung is safe only because it
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
