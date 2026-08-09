# mcp/tests/test_compound_idle_relay.py

| Field                  | Value                                                    |
| ---------------------- | -------------------------------------------------------- |
| repository             | agents-remember                                          |
| path                   | `mcp/tests/test_compound_idle_relay.py`                  |
| doc_type               | `file-level-onboarding`                                  |
| lastUpdated            | 2026-08-09T03:51+02:00                                    |
| lastVerifiedCommitHash | `7463b97a560e39367b9e31a687f09ea3f4f6b9f6`               |
| lastVerifiedCommitDate | 2026-08-09T04:22:51+02:00|
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

`CompoundIdleRelayTests` cit:([`CompoundIdleRelayTests`], mcp/tests/test_compound_idle_relay.py:164-741) builds fake catalog/inbox seams
(`_entry`, `_orchestrator`, `_manager`, `_idle_worker`, `_ctx`, `_state_signals`) and runs
multi-tick sweeps over them:

- Positive/dedupe: `test_compound_idle_positive_exactly_one_orchestrator_signal` cit:([`test_compound_idle_positive_exactly_one_orchestrator_signal`], mcp/tests/test_compound_idle_relay.py:212-247)
  proves one row naming every set member, `state_signal_landed`, marker set, and no second row
  on re-projection.
- Fail-closed negatives: partial set with one active worker cit:([`test_partial_set_active_worker_no_signal`], mcp/tests/test_compound_idle_relay.py:248-262),
  unknown member cit:([`test_unknown_member_fail_closed_no_signal`], mcp/tests/test_compound_idle_relay.py:263-270),
  unknown manager cit:([`test_unknown_manager_fail_closed_no_signal`], mcp/tests/test_compound_idle_relay.py:271-277),
  zero-worker manager cit:([`test_zero_worker_manager_does_not_signal`], mcp/tests/test_compound_idle_relay.py:472-477),
  unbound manager cit:([`test_unbound_manager_never_forms_set`], mcp/tests/test_compound_idle_relay.py:478-484),
  unbound worker cit:([`test_unbound_worker_never_joins_or_blocks`], mcp/tests/test_compound_idle_relay.py:485-504),
  and no-spawn-provenance owner cit:([`test_no_signal_without_spawn_provenance_owner`], mcp/tests/test_compound_idle_relay.py:533-539).
- Boundary/idle vocabulary: `awaiting-input` counts as idle cit:([`test_awaiting_input_member_counts_as_idle`], mcp/tests/test_compound_idle_relay.py:278-294);
  retired/exited rows never count (status-first) cit:([`test_retired_rows_never_count_status_first`], mcp/tests/test_compound_idle_relay.py:505-532);
  flap re-arms after a seat returns to activity cit:([`test_flap_rearms_after_a_seat_returns_to_activity`], mcp/tests/test_compound_idle_relay.py:295-336);
  a working orchestrator holds the durable row with zero mid-turn submissions at t+301 s /
  t+901 s and the next boundary lands it exactly once, terminal on this path cit:([`test_busy_orchestrator_holds_at_boundary_then_lands_exactly_once`], mcp/tests/test_compound_idle_relay.py:337-402).
- Membership arms (fix round 1, F1): same-master binding counts even when spawned by another
  manager cit:([`test_member_identity_same_master_binding_counts`], mcp/tests/test_compound_idle_relay.py:403-414);
  other-master workers never join or block cit:([`test_member_identity_other_master_worker_not_in_set`], mcp/tests/test_compound_idle_relay.py:415-433);
  a foreign-master worker spawned BY the manager neither blocks (active) nor joins (idle)
  cit:([`test_foreign_master_worker_active_does_not_block`, `test_foreign_master_worker_idle_does_not_join`], mcp/tests/test_compound_idle_relay.py:434-453; mcp/tests/test_compound_idle_relay.py:454-471).
- Manager residue (L3): a manager with landed rows older than the window relays the distinct
  `non-reaction` fact to its orchestrator, deduped per episode cit:([`test_manager_non_reaction_residue_relays_to_orchestrator`], mcp/tests/test_compound_idle_relay.py:540-581),
  and skips when no spawn-provenance owner exists cit:([`test_manager_residue_skips_without_spawn_provenance_owner`], mcp/tests/test_compound_idle_relay.py:582-608).
- Emitter guards (fix round 1, F4/F5): the marker re-record is a no-op cit:([`test_compound_idle_marker_guard_suppresses_repeat_record`], mcp/tests/test_compound_idle_relay.py:609-642);
  the action skips no-seat-row (both `session_id=None` and unknown id) cit:([`test_emit_skips_no_seat_row`, `test_emit_skips_finding_without_session_id`], mcp/tests/test_compound_idle_relay.py:643-648; mcp/tests/test_compound_idle_relay.py:649-660),
  already-emitted-on-fresh-signature cit:([`test_emit_skips_already_emitted`], mcp/tests/test_compound_idle_relay.py:661-683),
  and no-longer-idle-at-action-time cit:([`test_emit_skips_no_longer_idle_at_action_time`], mcp/tests/test_compound_idle_relay.py:684-704);
  the action-time signature replaces a stale evaluation-time signature in both the ask and the
  marker cit:([`test_action_time_signature_replaces_stale_evaluation_signature`], mcp/tests/test_compound_idle_relay.py:705-741).

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
| No external/domain document defines this relay; the suite is the forcing proof. | `CompoundIdleRelayTests` | mcp/tests/test_compound_idle_relay.py:164-741 |

## Repo-Internal References

The suite exercises `serving/state_signals.py` (predicates), `serving/_agent_notifier_actions.py`
(emitter), `serving/_agent_notifier_evaluation.py` (composition), `serving/seat_turn_truth.py`
(marker write), `controlplane/signal_routing.py` (`master_key`/`derive_signal_owner`), and the
landed-terminality predicate.

| Finding | Anchor | Source |
| --- | --- | --- |
| The predicates under test (set assembly, signature, findings). | `compound_idle_sets`; `compound_idle_signature`; `evaluate_compound_idle_findings` | mcp/src/agents_remember/serving/state_signals.py:69-103; mcp/src/agents_remember/serving/state_signals.py:104-111; mcp/src/agents_remember/serving/state_signals.py:159-180 |
| The emitter under test (action-time signature, skip branches, boundary-gated post). | `_emit_compound_idle` | mcp/src/agents_remember/serving/_agent_notifier_actions.py:680-737 |
| The marker write seam with its no-op guard. | `record_compound_idle_emitted` | mcp/src/agents_remember/serving/seat_turn_truth.py:155-166 |
| Landed terminality the suite asserts stays unreachable mid-turn. | `state_signal_landed` | mcp/src/agents_remember/controlplane/operator_inbox_records.py:54-65 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary participates in this suite. | — | — |

## Update History

- 2026-08-09T03:51+02:00 — 260713-TES-L3 curator: created this sidecar for the new
  compound-idle forcing suite (24 tests: positive/dedupe, fail-closed negatives, boundary
  hold/land, membership-arm pins, manager residue, emitter guards, action-time signature).
  Verification metadata pinned to the leaf base `7af76249` until closeout stamps the
  260713-TES-L3 commit.
