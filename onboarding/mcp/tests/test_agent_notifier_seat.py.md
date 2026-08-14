# mcp/tests/test_agent_notifier_seat.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_agent_notifier_seat.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-09T06:48+02:00                                            |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`                                        |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `overview.md`                                          |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Regression suite for seat-liveness findings and one notifier sweep over canonical task-document/role seats.

## Code Commentary

### Logic

The suite covers stale/degraded/unbound predicates, heartbeat progress, routable-owner refusal, backlog budgets, redelivery floors, coalescing, expiry, and restart behavior. Coalescing distinguishes roles on the same task document and routes unresolved dead seats to the architect boundary.

### Conventions

Test-only evidence uses deterministic fakes/fixtures and exercises the public or owning internal seam directly.

### Invariants And Boundaries

Diagnostics are not actionable findings; live or declared replacement evidence suppresses false inactivity; one sweep remains bounded and idempotent.

## Docs References

No Domain Documentation source is configured for this repository-local regression contract.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Current suite declaration anchoring this card. | `SeatLivenessPredicateTests` | mcp/tests/test_agent_notifier_seat.py:38-38 |

## Cross-Repo References

No cross-repository implementation source governs this test module.

## Update History

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
