# mcp/tests/test_agent_notifier_seat.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_agent_notifier_seat.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-09-06T21:38+00:00 |
| lastVerifiedCommitHash | `d36109038b3f2b500c138f9dc1ea9c9f9a247489`                                        |
| lastVerifiedCommitDate | 2026-09-06T22:21:49+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Notifier sweep integration for durable signals, redelivery and heartbeat state.

## Code Commentary

### Logic

Four retained scenarios seed inbox and stale-seat facts, constrain one-attempt redelivery budgeting, renew one signal row after cooldown, and keep a restarted sweep from retrying before the 900-second floor. The seeded legacy seats have no protocol endpoint, so both delivery actions remain unconfirmed while heartbeat and observer facts persist.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

Use temporary stores and real cooldown persistence. Signal renewal preserves row identity; unconfirmed delivery must not be described as successful paste or full predicate-family coverage.

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
| Seeded drift produces expected actions and ticks heartbeat. | `test_seeded_drift_produces_expected_actions_and_ticks_heartbeat` | mcp/tests/test_agent_notifier_seat.py:71-140 |
| Redeliver budget limits attempts and heartbeat reports backlog. | `test_redeliver_budget_limits_attempts_and_heartbeat_reports_backlog` | mcp/tests/test_agent_notifier_seat.py:142-168 |
| Repeated seat liveness sweeps coalesce into one signal row. | `test_repeated_seat_liveness_sweeps_coalesce_into_one_signal_row` | mcp/tests/test_agent_notifier_seat.py:170-207 |
| Pending backlog does not burst redeliver before floor after restart. | `test_pending_backlog_does_not_burst_redeliver_before_floor_after_restart` | mcp/tests/test_agent_notifier_seat.py:209-233 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## Update History

- 2026-09-06T21:38+00:00 — Reconciled the actual retained source after IAS test simplification at d3610903: corrected fixture/test roles, removed obsolete current-coverage claims and refreshed existing-source citations. Earlier entries remain historical; verification stamps remain closeout-owned.


- 2026-08-11T19:58+02:00 — Reconciled `test_agent_notifier_seat.py` with its current structural task/seat, tool-vocabulary, or quality-boundary regression contract and removed stale exact-id/leaf implications where present.
- 2026-08-09T12:08+02:00 — 260713-TES-L5 curator: recorded the nudge-store removal and the
  expectation-overdue/auto-nudge assertion deletions in the sweep integration suite.
  Verification metadata pinned until closeout stamps the 260713-TES-L5 commit.
- 2026-08-09T06:48+02:00 — 260713-TES-L4 curator: recorded the verdict-by fixture swap (N16
  ack-by retirement) and the dead-seat expiry-to-architect-mailbox integration test (N2/N3).
  Verification metadata pinned until closeout stamps the 260713-TES-L4 commit.
- 2026-08-09T01:21+02:00 — 260713-TES-L2 curator: recorded the `SweepIntegrationTests` fixture
  kind swap from `briefed-by` to `ack-by` (dispatch-time SLA findings now cover ack-by only).
  Verification metadata pinned until closeout stamps the 260713-TES-L2 commit.
- 2026-08-08T22:10+02:00 — 260713-TES-L1 completion round (curator): refreshed this sidecar body for the supervisor -> agent-notifier rename (module paths, identifiers, settings keys, wire keys, prose) and the compat seams; verification metadata pinned until closeout stamps the 260713-TES-L1 commit.
- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
