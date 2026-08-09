# mcp/tests/test_agent_notifier_seat.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_agent_notifier_seat.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-09T01:21+02:00                                            |
| lastVerifiedCommitHash | `7af76249ff1aa728d34a6e81c5f09c8bcb797484`                                        |
| lastVerifiedCommitDate | 2026-08-09T02:17:45+02:00|
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

## Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/tests/test_agent_notifier_seat.py`.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own top-level surface is listed in Code Commentary; no cross-file citation rows are needed for this split module. | — | — |

## Update History
- 2026-08-09T01:21+02:00 — 260713-TES-L2 curator: recorded the `SweepIntegrationTests` fixture
  kind swap from `briefed-by` to `ack-by` (dispatch-time SLA findings now cover ack-by only).
  Verification metadata pinned until closeout stamps the 260713-TES-L2 commit.
- 2026-08-08T22:10+02:00 — 260713-TES-L1 completion round (curator): refreshed this sidecar body for the supervisor -> agent-notifier rename (module paths, identifiers, settings keys, wire keys, prose) and the compat seams; verification metadata pinned until closeout stamps the 260713-TES-L1 commit.
- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
