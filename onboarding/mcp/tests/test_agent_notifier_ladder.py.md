# mcp/tests/test_agent_notifier_ladder.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_agent_notifier_ladder.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-09T06:48+02:00                                            |
| lastVerifiedCommitHash | `cdca11264fb4d27ee08f5e8b37ac5496e67c0840`                                        |
| lastVerifiedCommitDate | 2026-08-09T07:36:31+02:00|
| governingOverview      | `overview.md`                                          |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Part of the 260731-EFA-L7 in-place split family for `test_agent_notifier_ladder.py`'s source module; covers the behaviours named by its test classes.

## Code Commentary

- `EscalationPredicateTests`
- `DeadUpstreamPredicateTests`
- `LadderWalkIntegrationTests`
- `Cs6SweepScalingTests`

### 260713-TES-L2 Fixture Kind Swap

`Cs6SweepScalingTests` now seeds an overdue `ack-by` expectation row instead of `briefed-by`.
The swap keeps the scaling fixture on a kind that still drives expectation findings after the
worker→manager predicate retirement (260713-TES-L2): `briefed-by` rows remain dashboard
provenance but no longer fire `expectation-overdue`, while `ack-by` still exercises the
overdue→nudge→ladder path the CS-6 ceiling asserts. The bounded fixed-point ceiling semantics
the class pins are unchanged.

### 260713-TES-L4 Ladder Retirement And Terminal-Honesty Tests

`LadderWalkIntegrationTests` converted the rung-climb fixtures to the N3/N16 terminal truth:
`test_silent_live_seat_reaches_unresolved_after_attempt_ceiling` drives
`PERSISTENT_FAILURE_ATTEMPTS` sweeps and asserts `state="unresolved"`/`terminalReason=
"attempt-limit"` with delivery evidence intact and NO `orchestration.escalation.rung` event;
`test_landed_row_produces_no_retry_nudge_or_escalation_ever` pins the N16 regression across
repeated sweeps; `test_relay_restart_reconciles_by_request_id_without_duplicate_submission`
proves the same correlated request is never resubmitted and lands at the next boundary;
`test_delivered_dispatch_never_rebinds` pins dispatch-brief exact-pinning even against a dead
addressee; `test_dead_manager_row_rebinds_to_replacement_within_grace` and
`test_dead_manager_without_replacement_expires_to_architect_mailbox` pin the N14/N2/N3 rebind
and grace-expiry paths (rebind clears correlation and resets attempts; expiry readdresses the
marker to the role-only architect mailbox). `Cs6SweepScalingTests` swaps its overdue fixture to
`verdict-by` and replaces the escalation-budget cap test with
`test_dead_seat_expiry_emission_is_exactly_one_per_row_per_sweep` (linear, level-triggered, and
terminal on the next sweep).

## Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/tests/test_agent_notifier_ladder.py`.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own top-level surface is listed in Code Commentary; no cross-file citation rows are needed for this split module. | — | — |

## Update History

- 2026-08-09T06:48+02:00 — 260713-TES-L4 curator: recorded the ladder-retirement conversions
  (attempt-ceiling `unresolved`, landed-never-retried, relay-restart reconcile-by-request_id,
  dispatch exact-pinning, rebind/grace-expiry to the architect mailbox) and the
  `Cs6SweepScalingTests` verdict-by fixture + one-per-row-per-sweep expiry emission test.
  Verification metadata pinned until closeout stamps the 260713-TES-L4 commit.
- 2026-08-09T01:21+02:00 — 260713-TES-L2 curator: recorded the `Cs6SweepScalingTests` fixture
  kind swap from `briefed-by` to `ack-by` (the scaling fixture now exercises an expectation kind
  that still drives findings). Verification metadata pinned until closeout stamps the
  260713-TES-L2 commit.
- 2026-08-08T22:10+02:00 — 260713-TES-L1 completion round (curator): refreshed this sidecar body for the supervisor -> agent-notifier rename (module paths, identifiers, settings keys, wire keys, prose) and the compat seams; verification metadata pinned until closeout stamps the 260713-TES-L1 commit.
- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
