# mcp/tests/test_state_signal_relay.py

| Field                  | Value                                                    |
| ---------------------- | -------------------------------------------------------- |
| repository             | agents-remember                                          |
| path                   | `mcp/tests/test_state_signal_relay.py`                   |
| doc_type               | `file-level-onboarding`                                  |
| lastUpdated            | 2026-08-09T06:48+02:00|
| lastVerifiedCommitHash | `a84add4c9422b18a26f1748dedaed16194994ded`                                    |
| lastVerifiedCommitDate | 2026-08-10T05:11:18+02:00|
| governingOverview      | `overview.md`                                            |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

The multi-tick relay simulation suite for 260713-TES-L2: incident-#1 proof (a worker finishes
without posting an inbox row and its manager still receives the done signal), busy-manager
boundary hold with exactly one landing (including past the escalation SLA and backoff floor),
origin attribution, owner rebinding, idle-flap re-arm, non-reaction residue, dedupe, and
boundary drain.

## Code Commentary

### Logic

L6 makes the completed/interrupted and non-reaction matrices role-neutral across manager-owned
subordinates and adds evaluate→mutate→act races. Reparent, leaf/master movement, working re-entry,
termination, terminal-evidence replacement, retargeted/consumed landed rows, malformed values, and
missing truth must all return `skipped` with no row or marker. The final residual regression mutates
`adapterAcceptedAt` to a valid ISO string without timezone; it proves the action rejects it without
raising or aborting the sweep.

`StateSignalRelayTests` cit:([`StateSignalRelayTests`], mcp/tests/test_state_signal_relay.py:127-742) drives `run_agent_notifier_sweep` over fake catalog/inbox
seams across simulated ticks:

- `test_incident_1_finished_worker_without_inbox_row_still_signals_manager` cit:([`test_incident_1_finished_worker_without_inbox_row_still_signals_manager`], mcp/tests/test_state_signal_relay.py:197-218):
  catalog row only (`turn-ended`/`completed`/`terminal_evidence_id=turn-9`), one sweep emits
  exactly one durable `state-signal` to the owning manager; re-projection emits none.
- `test_busy_manager_holds_at_boundary_then_lands_exactly_once` cit:([`test_busy_manager_holds_at_boundary_then_lands_exactly_once`], mcp/tests/test_state_signal_relay.py:501-567): a working manager
  holds on the durable schedule; t+301s and t+901s (the F1 regression ticks) still produce zero
  adapter submissions and rung 0; the boundary then drains and lands exactly once.
- Origin cases cit:([`test_interrupted_signal_carries_developer_origin`, `test_interrupted_signal_with_unknown_origin`], mcp/tests/test_state_signal_relay.py:569-583; mcp/tests/test_state_signal_relay.py:585-597): developer-stamped vs unknown; dedupe per seat+turn cit:([`test_dedupe_keys_per_seat_and_turn`], mcp/tests/test_state_signal_relay.py:220-232);
  owner rebinding after manager replacement cit:([`test_owner_rebinding_after_manager_replacement`], mcp/tests/test_state_signal_relay.py:599-616) — the fixture keeps the
  replacement manager `turn_state="working"` since 260713-TES-L3 so the test isolates the L2
  rebinding behavior it owns (a turn-ended manager + idle worker would additionally fire the
  new compound-idle fact); idle flap re-arm cit:([`test_idle_flap_rearms_for_a_new_turn`], mcp/tests/test_state_signal_relay.py:618-657);
  non-reaction residue + dedupe cit:([`test_non_reaction_residue_relays_distinct_fact`, `test_non_reaction_dedupe_marker_suppresses_repeat`], mcp/tests/test_state_signal_relay.py:659-700; mcp/tests/test_state_signal_relay.py:702-737) — the landed-row
  fixtures now carry the formal `state="landed"` (N13/N16); no done signal for killed/hung/failed/unknown cit:([`test_no_done_signal_for_killed_or_hung_seats`], mcp/tests/test_state_signal_relay.py:739-757); re-fire renews the same row cit:([`test_repeat_fire_renews_the_same_row`], mcp/tests/test_state_signal_relay.py:773-792); scope exclusions cit:([`test_non_reaction_ignores_non_worker_young_and_malformed_rows`], mcp/tests/test_state_signal_relay.py:794-859); boundary drain skip/fresh-boundary rules and ordinary-row drain cit:([`test_boundary_drain_skips_rows_without_a_fresh_boundary`, `test_boundary_drain_pushes_other_pending_rows_for_the_seat`], mcp/tests/test_state_signal_relay.py:861-954; mcp/tests/test_state_signal_relay.py:956-1012); no-sweep store-fold post cit:([`test_post_owner_signal_without_sweep_reads_the_store_fold`], mcp/tests/test_state_signal_relay.py:1014-1033).

### Conventions

Simulation harness style: one `_ctx()` per test, injected clocks, `sweep.remember` folds kept
consistent with the store so re-projection behaves like production.

### Invariants And Boundaries

- Exactly one durable row per seat+turn; re-fire renews, never duplicates.
- A boundary-held signal must not climb the ladder or hit the wire while its manager is
  running (F1).
- Non-reaction facts cover worker→manager and, since 260713-TES-L3, manager→orchestrator —
  one per landed-row episode (this suite's residue cases are worker-scope; the manager-scope
  cases live in `test_compound_idle_relay.py`).

### Todos

None.

## Docs References

No Domain Documentation entries are configured in the resolved `system/sources.md`.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external/domain document defines these relays; the suite is the incident-#1 proof. | `StateSignalRelayTests` | mcp/tests/test_state_signal_relay.py:127-742 |

## Repo-Internal References

The suite exercises `serving/state_signals.py`, `serving/_agent_notifier_actions.py`,
`serving/_agent_notifier_evaluation.py`, and `controlplane/operator_inbox_records.py`.

| Finding | Anchor | Source |
| --- | --- | --- |
| The predicates under test. | `evaluate_state_signal_findings`; `evaluate_non_reaction_findings`; `evaluate_boundary_drain_findings` | mcp/src/agents_remember/serving/state_signals.py:136-144; mcp/src/agents_remember/serving/state_signals.py:211-225; mcp/src/agents_remember/serving/state_signals.py:304-350 |
| The actions under test. | `_emit_state_signal`; `_emit_non_reaction`; `_drain_boundary` | mcp/src/agents_remember/serving/_agent_notifier_actions.py:421-480; mcp/src/agents_remember/serving/_agent_notifier_actions.py:542-599; mcp/src/agents_remember/serving/_agent_notifier_actions.py:602-611 |
| Landed terminality the suite asserts stays unreachable mid-turn. | `state_signal_landed` | mcp/src/agents_remember/controlplane/operator_inbox_records.py:66-74 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary participates in this suite. | — | — |

## 260713-TES-L5 Current Delta — Nudge Store Gone From Harness

`StateSignalRelayTests` drops `OrchestrationNudgeStore` from the sweep context; the relay
fixtures and formal `state="landed"` assertions are unchanged.

## Update History

- 2026-08-10T04:39+02:00 — 260713-TES-L6: documented all-subordinate relay, action-time mutation,
  fresh-owner metadata, and timezone-naive evidence regressions. Verification metadata remains
  pinned until closeout stamps the code commit.

- 2026-08-09T12:08+02:00 — 260713-TES-L5 curator: recorded the nudge-store removal from the
  state-signal relay harness. Verification metadata pinned until closeout stamps the
  260713-TES-L5 commit.
- 2026-08-09T06:48+02:00 — 260713-TES-L4 curator: recorded the landed-row fixtures' formal
  `state="landed"` alignment (N13/N16 migration; the by-rule pending landing no longer exists).
  Verification metadata pinned until closeout stamps the 260713-TES-L4 commit.
- 2026-08-09T03:51+02:00 — 260713-TES-L3 curator: recorded the working-manager fixture change
  in `test_owner_rebinding_after_manager_replacement` (isolates the L2 rebinding behavior from
  the new compound-idle fact), corrected the governing-overview link, and widened the
  non-reaction invariant to include the manager→orchestrator arm. Verification metadata pinned
  until closeout stamps the 260713-TES-L3 commit.
- 2026-08-09T01:21+02:00 — 260713-TES-L2 curator: created this sidecar for the new relay
  simulation suite (incident-#1, boundary hold past SLA/backoff, origin, rebinding, idle flap,
  non-reaction, drain). Verification metadata pinned to the leaf base `1c1629fc` until closeout
  stamps the 260713-TES-L2 commit.
