# mcp/tests/test_agent_notifier_seat.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_agent_notifier_seat.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-09T06:48+02:00                                            |
| lastVerifiedCommitHash | `cdca11264fb4d27ee08f5e8b37ac5496e67c0840`                                        |
| lastVerifiedCommitDate | 2026-08-09T07:36:31+02:00|
| governingOverview      | `overview.md`                                          |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Part of the 260731-EFA-L7 in-place split family for `test_agent_notifier_seat.py`'s source module; covers the behaviours named by its test classes.

## Code Commentary

- `SeatLivenessPredicateTests`
- `SweepIntegrationTests`

### 260713-TES-L2 Fixture Kind Swap

`SweepIntegrationTests` now writes overdue `ack-by` expectation rows for the worker/orphan
fixtures instead of `briefed-by`. The seeded drift still drives the full
expectation-overdue → auto-nudge → escalation chain through `run_agent_notifier_sweep`, but on
the expectation kind that remains active after the worker→manager predicate retirement
(260713-TES-L2): `briefed-by`/`turn-report-by` no longer produce notifier findings, so the
integration fixtures had to move to `ack-by` to keep exercising the SLA path end to end.

### 260713-TES-L4 Dead-Seat Expiry And Fixture-Kind Update

`SweepIntegrationTests` now writes overdue `verdict-by` rows for the worker/orphan fixtures
(ack-by retired with the N16 consume demotion; verdict-by remains active) and
`test_dead_seat_row_expires_to_the_architect_mailbox_not_redelivered` replaces the ladder
terminal fixture: a pending row to a dead seat with no replacement past the 5-minute grace
resolves `expired`/`rebind-grace-expired`, readdresses to `recipientRole="architect"`, emits
`orchestration.agent-notifier.rebind-expired`, and is never redelivered (N2/N3).

## Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/tests/test_agent_notifier_seat.py`.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own top-level surface is listed in Code Commentary; no cross-file citation rows are needed for this split module. | — | — |

## Update History

- 2026-08-09T06:48+02:00 — 260713-TES-L4 curator: recorded the verdict-by fixture swap (N16
  ack-by retirement) and the dead-seat expiry-to-architect-mailbox integration test (N2/N3).
  Verification metadata pinned until closeout stamps the 260713-TES-L4 commit.
- 2026-08-09T01:21+02:00 — 260713-TES-L2 curator: recorded the `SweepIntegrationTests` fixture
  kind swap from `briefed-by` to `ack-by` (dispatch-time SLA findings now cover ack-by only).
  Verification metadata pinned until closeout stamps the 260713-TES-L2 commit.
- 2026-08-08T22:10+02:00 — 260713-TES-L1 completion round (curator): refreshed this sidecar body for the supervisor -> agent-notifier rename (module paths, identifiers, settings keys, wire keys, prose) and the compat seams; verification metadata pinned until closeout stamps the 260713-TES-L1 commit.
- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
