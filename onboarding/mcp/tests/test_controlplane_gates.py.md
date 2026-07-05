# test_controlplane_gates.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_controlplane_gates.py`           |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-05T18:20+02:00 |
| lastVerifiedCommitHash | `e3b11ab9e2f3f89d45c6de01c21040600f2b3c7a`       |
| lastVerifiedCommitDate | 2026-07-05T17:03:17+02:00|
| governingOverview      | `overview.md`                                    |

## Purpose

Unit tests for the gate control plane: the `GateRecord` / `GateStore`
records-and-store layer and the `gate_*` payload builders (slice 6a), plus the
closeout-gate enforcement policy and its wiring (slice 6b).

## Code Commentary

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
developer-approved permits, **model-approved blocks**, latest gate governs).
`CloseoutEnforcementHelperTests` drives `closeout.py`'s `_enforce_closeout_gate` /
`_mark_closeout_gate_applied` / `_closeout_gate_payload` over a temp `GateStore`
rooted at a stub contract's `coordination_root`.
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

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The records under test. | [controlplane/records.py](agents-remember/mcp/src/agents_remember/controlplane/records.py) |
| The store under test. | [controlplane/store.py](agents-remember/mcp/src/agents_remember/controlplane/store.py) |
| The payload builders under test. | [mcp/tools/gates.py](agents-remember/mcp/src/agents_remember/mcp/tools/gates.py) |
| The operator inbox store polled by `gate_response_wait_payload`. | [controlplane/operator_inbox_store.py](agents-remember/mcp/src/agents_remember/controlplane/operator_inbox_store.py) |
| The enforcement policy under test (slice 6b). | [controlplane/enforcement.py](agents-remember/mcp/src/agents_remember/controlplane/enforcement.py) |
| Gate delegation policy under test. | [controlplane/gate_policy.py](agents-remember/mcp/src/agents_remember/controlplane/gate_policy.py) |
| The closeout enforcement helpers under test (slice 6b). | [worktrees/modules/closeout.py](agents-remember/mcp/src/agents_remember/worktrees/modules/closeout.py) |
| The conformance suite that also covers the gate tools. | [test_tool_response_conformance.py](agents-remember/mcp/tests/test_tool_response_conformance.py) |

As of the 260703-L8 seam ruling the suite carries MasterHandoverSeamTests: delegability to the orchestrator, the named-policy routing, human-pinned kinds staying pinned, apply_seam_verdict_requirement binding only delegated seam rules, verdict-evidence refusal/acceptance on a delegated handover decision, and owner-never-self-approves on the handover kind.

As of cycle 5 SeamChannelTests exercises the seam end-to-end at the payload layer: wait=false raise (and its refusal for undelegated kinds), cross-lifecycle decide by packet-carried gate id with orchestration attribution, verdict-evidence requirement, cli refusal on delegated kinds, raiser cancel, and evaluate_gate over the handover kind.

## Update History

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
