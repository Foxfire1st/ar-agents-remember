# mcp/src/agents_remember/controlplane/inbox_backoff.py

| Field                  | Value                                                             |
| ---------------------- | ------------------------------------------------------------------ |
| repository             | agents-remember                                                    |
| path                   | `mcp/src/agents_remember/controlplane/inbox_backoff.py`            |
| doc_type               | `file-level-onboarding`                                            |
| lastUpdated            | 2026-07-08T23:59+02:00                                             |
| lastVerifiedCommitHash | `5f9163882857114319552d303e2e301082b588ba`|
| lastVerifiedCommitDate | 2026-07-08T18:21:20+02:00|
| governingOverview      | `overview.md`                                                      |

## Governing Overview

[overview.md](overview.md)

## Purpose

R3 (260707-HFX2-L1): pure backoff-schedule math + per-target rate limiting for redelivering a
pending/unacked operator inbox entry — the math `OperatorInboxStore.record_delivery`/
`list_redeliverable` call; L2 (the supervisor sweep, a sibling leaf) is the actual driver.

## Code Commentary

### Logic

`BACKOFF_SCHEDULE_SECONDS` is a fixed ladder (30s, 60s, 5m, 15m, 1h, 6h) — `attemptCount` indexes
into it, clamped to the last entry as a steady-state ceiling so a long-pending row never floods
redelivery. `backoff_seconds_for_attempt(attempt_count)` returns the wait before the NEXT attempt;
`next_attempt_at(now=, attempt_count=)` stamps the durable `nextAttemptAt` ISO timestamp
`record_delivery` writes onto the entry — a row, never an in-memory timer.

`is_ladder_resolved(entry)` is the explicit terminal predicate for rows that reached the terminal
escalation rung against a non-live target seat. `is_due(entry, now=)` is true only for a `pending`
entry that is not ladder-resolved, whose `deliveryState` is one of the redeliverable states, and
whose `nextAttemptAt` has elapsed (or is unset, i.e. never attempted).
`is_rate_limited(entry, now=, rate_limit_seconds=)`
mirrors the `OrchestrationNudgeStore.record` rate-limit pattern
(`orchestration_nudges.py:81-99`): compare elapsed time since `lastAttemptAt` against a per-target
floor, independent of the backoff schedule, so a burst of posts to the same target cannot become a
burst of redeliveries. `redeliverable(entries, now=, rate_limit_seconds=)` composes both: due AND
not ladder-resolved AND not rate-limited.

### Conventions

`_REDELIVERABLE_DELIVERY_STATES` includes `delivered` deliberately — R1's central claim is that
`delivered` is never terminal (pasted != perceived), so a delivered-but-unacked row still
schedules and remains redeliverable; only `consume` (an inbox `state` transition, not a
`deliveryState` one) stops it.

### Invariants And Boundaries

- Pure functions only — no store reads/writes, no clock calls (`now` is always a caller-supplied
  parameter, so tests are deterministic).
- This module computes WHETHER to redeliver; it never redelivers itself — `OperatorInboxStore.
  list_redeliverable` selects candidates, and the actual re-push through `deliver_inbox_entry` is
  L2's job.
- Ladder-resolved rows are terminal and never redeliverable even though they are not consumed/acked.

### Todos

None.

## Docs References

The A2A push-then-poll semantics (push = at-least-one-attempt, MAY-retry; durable task state is
the only guaranteed path) and Temporal/Restate/Inngest persisted-timeout patterns (research
`wf_5782a3a5-6a1`, cited in the leaf spec) motivate a durable backoff schedule over an in-memory
retry loop.

| Finding | Citations | Source Path |
| --- | --- | --- |
| None (research citation, no local doc). | N/A | N/A |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The backoff ladder + rate-limit gate mirror `OrchestrationNudgeStore.record`'s elapsed-time check. | L81-L99 | [orchestration_nudges.py](agents-remember/mcp/src/agents_remember/controlplane/orchestration_nudges.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| None. | N/A | N/A |

## Update History

- 2026-07-08T23:59+02:00 — 260707-HFX2-L8: added `is_ladder_resolved` and made due/redeliverable
  selection explicitly exclude ladder-resolved terminal rows. Verification metadata pinned until
  closeout stamps the HFX2-L8 commit.
- 2026-07-08T14:20+02:00 — 260707-HFX2-L1: created for R3 redelivery backoff math + per-target
  rate limiting. Verification metadata pinned until closeout stamps the 260707-HFX2-L1 commit.
