# mcp/tests/test_compound_idle_relay.py

| Field                  | Value                                                    |
| ---------------------- | -------------------------------------------------------- |
| repository             | agents-remember                                          |
| path                   | `mcp/tests/test_compound_idle_relay.py`                  |
| doc_type               | `file-level-onboarding`                                  |
| lastUpdated            | 2026-08-09T06:48+02:00                                    |
| lastVerifiedCommitHash | `c51373425be3e3f488590ad2f444810df89b4ffb`               |
| lastVerifiedCommitDate | 2026-08-26T19:22:10+02:00|
| governingOverview      | `overview.md`                                            |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

The forcing suite for 260713-TES-L3 (compound-idle relay to orchestrators): manager + ALL
workers idle → exactly one durable `state-signal` to the owning orchestrator; partial sets,
unknown members, retired rows, and zero-worker/unbound managers never fire; flap re-arm;
busy-orchestrator boundary hold with exactly one landing; master-scoped membership on every
arm; and the manager non-reaction residue one level up. All 24 tests were red before
implementation and drive the production sweep end to end through `run_agent_notifier_sweep`.

## Code Commentary

### Logic

L6 extends the compound-idle matrix beyond builders: reviewer, curator, and a future `analyst`
directly spawned by the manager all participate in the same master-scoped set. Owner-tier roles,
cross-master descendants, dead/retired rows, missing parent edges, and unknown active state are
excluded or fail closed. Working→ended transitions re-arm one fresh episode while stable episode
signatures dedupe repeated sweeps.

`CompoundIdleRelayTests` cit:([`CompoundIdleRelayTests`], mcp/tests/test_compound_idle_relay.py:163-735) builds fake catalog/inbox seams
(`_entry`, `_orchestrator`, `_manager`, `_idle_worker`, `_ctx`, `_state_signals`) and runs
multi-tick sweeps over them:

- Positive/dedupe: `test_compound_idle_positive_exactly_one_orchestrator_signal` cit:([`test_compound_idle_positive_exactly_one_orchestrator_signal`], mcp/tests/test_compound_idle_relay.py:277-312)
  proves one row naming every set member, `state_signal_landed`, marker set, and no second row
  on re-projection.
- Fail-closed negatives: partial set with one active worker cit:([`test_partial_set_active_worker_no_signal`], mcp/tests/test_compound_idle_relay.py:314-327),
  unknown member cit:([`test_unknown_member_fail_closed_no_signal`], mcp/tests/test_compound_idle_relay.py:433-441),
  unknown manager cit:([`test_unknown_manager_fail_closed_no_signal`], mcp/tests/test_compound_idle_relay.py:443-448),
  zero-worker manager cit:([`test_zero_worker_manager_does_not_signal`], mcp/tests/test_compound_idle_relay.py:648-652),
  unbound manager cit:([`test_unbound_manager_never_forms_set`], mcp/tests/test_compound_idle_relay.py:654-661),
  unbound worker cit:([`test_unbound_worker_never_joins_or_blocks`], mcp/tests/test_compound_idle_relay.py:663-681),
  while structural ownership remains routable without spawn provenance cit:([`test_structural_owner_routes_without_spawn_provenance`], mcp/tests/test_compound_idle_relay.py:710-715).
- Boundary/idle vocabulary: `awaiting-input` counts as idle cit:([`test_awaiting_input_member_counts_as_idle`], mcp/tests/test_compound_idle_relay.py:450-465);
  retired/exited rows never count (status-first) cit:([`test_retired_rows_never_count_status_first`], mcp/tests/test_compound_idle_relay.py:683-708);
  flap re-arms after a seat returns to activity cit:([`test_flap_rearms_after_a_seat_returns_to_activity`], mcp/tests/test_compound_idle_relay.py:467-507);
  a working orchestrator holds the durable row with zero mid-turn submissions at t+301 s /
  t+901 s and the next boundary lands it exactly once, terminal on this path cit:([`test_busy_orchestrator_holds_at_boundary_then_lands_exactly_once`], mcp/tests/test_compound_idle_relay.py:509-573).
- Membership arms (L19 structural ownership): same-master membership is derived from task topology and ignores spawn provenance
  cit:([`test_same_master_membership_ignores_spawn_provenance`], mcp/tests/test_compound_idle_relay.py:575-589);
  other-master workers never join or block cit:([`test_member_identity_other_master_worker_not_in_set`], mcp/tests/test_compound_idle_relay.py:591-608);
  a foreign-master worker spawned BY the manager neither blocks (active) nor joins (idle)
  cit:([`test_foreign_master_worker_active_does_not_block`, `test_foreign_master_worker_idle_does_not_join`], mcp/tests/test_compound_idle_relay.py:610-628; mcp/tests/test_compound_idle_relay.py:630-646).
- Manager residue (L3): a manager with landed rows older than the window relays the distinct
  `non-reaction` fact to its orchestrator, deduped per episode cit:([`test_manager_non_reaction_residue_relays_to_orchestrator`], mcp/tests/test_compound_idle_relay.py:717-758),
  and routes structurally even without spawn provenance cit:([`test_manager_residue_routes_structurally_without_spawn_provenance`], mcp/tests/test_compound_idle_relay.py:760-787).
- Emitter guards (fix round 1, F4/F5): the marker re-record is a no-op cit:([`test_compound_idle_marker_guard_suppresses_repeat_record`], mcp/tests/test_compound_idle_relay.py:789-805);
  the action skips no-seat-row (both `session_id=None` and unknown id) cit:([`test_emit_skips_no_seat_row`, `test_emit_skips_finding_without_session_id`], mcp/tests/test_compound_idle_relay.py:823-827; mcp/tests/test_compound_idle_relay.py:829-839),
  already-emitted-on-fresh-signature cit:([`test_emit_skips_already_emitted`], mcp/tests/test_compound_idle_relay.py:841-862),
  and no-longer-idle-at-action-time cit:([`test_emit_skips_no_longer_idle_at_action_time`], mcp/tests/test_compound_idle_relay.py:864-883);
  the action-time signature replaces a stale evaluation-time signature in both the ask and the
  marker cit:([`test_action_time_signature_replaces_stale_evaluation_signature`], mcp/tests/test_compound_idle_relay.py:885-919).

### 260713-TES-L4 Landed-State Fixture Alignment

The landed-row fixtures (non-reaction episode seeds) now carry the formal `state="landed"`
alongside `deliveryState="delivered"`/`adapterDeliveryState="accepted"` — the by-rule pending
landing folded into the schema with the N13/N16 migration (260713-TES-L4). The suite's
boundary-hold/land assertions and `state_signal_landed` checks are unchanged in intent.

### Conventions

Simulation-harness style shared with `test_state_signal_relay.py`: one `_ctx()` per test,
injected clocks, accepted-paster fake for adapter acceptance at boundaries, and
`sweep.remember` folds consistent with the store. The suite uses `_state_signals()` to filter
the inbox by `messageKind == "state-signal"`.

### Invariants And Boundaries

- Exactly one durable `state-signal` per compound set; re-projection never mints a second row,
  and a flap (idle→active→idle) re-arms via the signature and mints a NEW row for the new
  episode.
- Membership is master-scoped on every arm and status-first; `turn_state=None` fails the set
  closed; zero-worker and unbound managers never signal.
- Boundary-held rows never climb the ladder or hit the wire mid-turn; correlated acceptance at
  a turn boundary is terminal on this path (`state_signal_landed`).
- The manager non-reaction residue is a distinct fact routed one hop up; compound-idle stays a
  pure seat-state signal.

### Todos

None.

## Docs References

No Domain Documentation entries are configured in the resolved `system/sources.md`; the
compound-idle semantics are same-repository runtime behavior proven by source and tests.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external/domain document defines this relay; the suite is the forcing proof. | `CompoundIdleRelayTests` | mcp/tests/test_compound_idle_relay.py:163-735 |

## Repo-Internal References

The suite exercises `serving/state_signals.py` (predicates), `serving/_agent_notifier_actions.py`
(emitter), `serving/_agent_notifier_evaluation.py` (composition), `serving/seat_turn_truth.py`
(marker write), `controlplane/signal_routing.py` (`master_key`/`derive_signal_owner`), and the
landed-terminality predicate.

| Finding | Anchor | Source |
| --- | --- | --- |
| The predicates under test (set assembly, signature, findings). | `compound_idle_sets`; `compound_idle_signature`; `evaluate_compound_idle_findings` | mcp/src/agents_remember/serving/state_signals.py:119-133; mcp/src/agents_remember/serving/state_signals.py:136-144; mcp/src/agents_remember/serving/state_signals.py:222-242 |
| The emitter under test (action-time signature, skip branches, boundary-gated post). | `_emit_compound_idle` | mcp/src/agents_remember/serving/_agent_notifier_actions.py:483-539 |
| The marker write seam with its no-op guard. | `record_compound_idle_emitted` | mcp/src/agents_remember/serving/seat_turn_truth.py:155-166 |
| Landed terminality the suite asserts stays unreachable mid-turn. | `state_signal_landed` | mcp/src/agents_remember/controlplane/operator_inbox_records.py:28-36 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary participates in this suite. | — | — |

## 260713-TES-L5 Current Delta — Context Without Nudge Store

The compound-idle relay harness drops `OrchestrationNudgeStore` from
`AgentNotifierContext` (the sweep no longer nudges); relay behavior and landed-row fixtures
are unchanged.

## Update History

- 2026-08-26T12:30+02:00 — 260821-ARSPAWN-L2 semantic re-read: retained the compound-idle set/signature/
  finding claim after verifying the current selector still requires a manager plus task-owned
  running subordinates all at a turn boundary; regenerated its source ranges.

- 2026-08-11T19:58+02:00 — Aligned the regression card for `test_compound_idle_relay.py` with the source's current task-document, seat-routing, inbox, or lifecycle assertions.
- 2026-08-10T13:00+02:00 — 260731-EFA-L9 curator: recorded the current compound-idle relay assertions
  and re-read them against the staged source; verification metadata remains pinned until closeout.

- 2026-08-10T04:39+02:00 — 260713-TES-L6: recorded all-subordinate compound-idle membership,
  topology exclusions, and re-arm/dedupe coverage. Verification metadata remains pinned until
  closeout stamps the code commit.

- 2026-08-09T12:08+02:00 — 260713-TES-L5 curator: recorded the nudge-store removal from the
  relay harness context. Verification metadata pinned until closeout stamps the
  260713-TES-L5 commit.
- 2026-08-09T06:48+02:00 — 260713-TES-L4 curator: recorded the landed-row fixture alignment to
  the formal `state="landed"` (N13/N16 migration). Verification metadata pinned until closeout
  stamps the 260713-TES-L4 commit.
- 2026-08-09T03:51+02:00 — 260713-TES-L3 curator: created this sidecar for the new
  compound-idle forcing suite (24 tests: positive/dedupe, fail-closed negatives, boundary
  hold/land, membership-arm pins, manager residue, emitter guards, action-time signature).
  Verification metadata pinned to the leaf base `7af76249` until closeout stamps the
  260713-TES-L3 commit.
