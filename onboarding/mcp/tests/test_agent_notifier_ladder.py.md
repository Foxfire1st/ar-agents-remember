# mcp/tests/test_agent_notifier_ladder.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_agent_notifier_ladder.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-09T06:48+02:00                                            |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`                                        |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `overview.md`                                          |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Regression suite for notifier escalation, replacement, expiry, and bounded sweep behavior under plane-owned seat identity.

## Code Commentary

### Logic

The tests prove dead-upstream detection from structural provenance; durable dispatch rows do not rebind; manager replacement preserves the worker through canonical task-document/role routing; grace expiry reaches the architect mailbox; landed seats remain terminal; repeated sweeps, cooldowns, budgets, and restart reconciliation reach bounded fixed points.

### Conventions

Test-only evidence uses deterministic fakes/fixtures and exercises the public or owning internal seam directly.

### Invariants And Boundaries

Notifier actions must use durable task/role evidence, never a guessed occupant address; duplicate findings cannot duplicate rebind, delivery, or expiry effects.

## Docs References

No Domain Documentation source is configured for this repository-local regression contract.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Current suite declaration anchoring this card. | `DeadUpstreamPredicateTests` | mcp/tests/test_agent_notifier_ladder.py:121-121 |

## Cross-Repo References

No cross-repository implementation source governs this test module.

## Update History

- 2026-08-11T19:58+02:00 — Reconciled `test_agent_notifier_ladder.py` with its current structural task/seat, tool-vocabulary, or quality-boundary regression contract and removed stale exact-id/leaf implications where present.
- 2026-08-10T13:00+02:00 — 260731-EFA-L9 curator: No content impact: re-read the current staged ladder-demolition and agent-notifier assertions; the existing test card remains accurate. Verification metadata remains pinned until closeout.
- 2026-08-09T12:08+02:00 — 260713-TES-L5 curator: recorded the escalation-predicate
  demolition, the grace-path fixed-point conversion, and the new `escalationBudget`
  load-shed/expectation-compaction scaling tests. Verification metadata pinned until
  closeout stamps the 260713-TES-L5 commit.
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
