# mcp/src/agents_remember/controlplane/inbox_backoff.py

| Field                  | Value                                                             |
| ---------------------- | ------------------------------------------------------------------ |
| repository             | agents-remember                                                    |
| path                   | `mcp/src/agents_remember/controlplane/inbox_backoff.py`            |
| doc_type               | `file-level-onboarding`                                            |
| lastUpdated            | 2026-07-09T11:19+02:00                                             |
| lastVerifiedCommitHash | `e400ed0ce98752d1b65d00de97c9b84c7ea20814`|
| lastVerifiedCommitDate | 2026-07-10T20:04:45+02:00|
| governingOverview      | `overview.md`                                                      |

## Governing Overview

[overview.md](overview.md)

## Purpose

R3 (260707-HFX2-L1): pure backoff-schedule math + per-target rate limiting for redelivering a
pending/unacked operator inbox entry — the math `OperatorInboxStore.record_delivery`/
`list_redeliverable` call; L2 (the supervisor sweep, a sibling leaf) is the actual driver. HFX2-L9
turns the old short rate limit into the shared 900-second production floor for every retry path.

## Code Commentary

### Logic

`BACKOFF_SCHEDULE_SECONDS` is a fixed ladder (30s, 60s, 5m, 15m, 1h, 6h) — `attemptCount` indexes
into it, clamped to the last entry as a steady-state ceiling so a long-pending row never floods
redelivery. `MIN_REDELIVERY_INTERVAL_SECONDS` and `DEFAULT_RATE_LIMIT_SECONDS` are both 900 seconds
since HFX2-L9. `require_redelivery_floor_seconds(rate_limit_seconds, owner=...)` returns that floor
when the caller passes `None` and refuses any explicit sub-900 value with a loud `ValueError`.
`backoff_seconds_for_attempt(attempt_count)` returns the wait before the NEXT attempt;
`next_attempt_at(now=, attempt_count=, redelivery_floor_seconds=...)` stamps the durable
`nextAttemptAt` ISO timestamp as the max of the ladder rung and the required floor — a row, never an
in-memory timer.

`is_ladder_resolved(entry)` is the explicit terminal predicate for rows that reached the terminal
escalation rung against a non-live target seat. `is_due(entry, now=)` is true only for a `pending`
entry that is not ladder-resolved, whose `deliveryState` is one of the redeliverable states, and
whose `nextAttemptAt` has elapsed (or is unset, i.e. never attempted).
`is_rate_limited(entry, now=, rate_limit_seconds=)`
mirrors the `OrchestrationNudgeStore.record` rate-limit pattern, but now validates the supplied
rate-limit value through the same 900-second floor helper
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
- No delivered, queued, unconfirmed, or no-hosted-session row may be retried sooner than 900 seconds;
  below-floor caller settings are refused rather than silently clamped.

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
| The redelivery floor helper defaults to 900 seconds and refuses explicit sub-floor values; `next_attempt_at` applies the floor over the early ladder rungs. | L24-L72 | [inbox_backoff.py](agents-remember/mcp/src/agents_remember/controlplane/inbox_backoff.py) |
| The rate-limit predicate reuses the same floor helper before comparing elapsed time since `lastAttemptAt`. | L92-L108 | [inbox_backoff.py](agents-remember/mcp/src/agents_remember/controlplane/inbox_backoff.py) |
| The backoff ladder + rate-limit gate mirror `OrchestrationNudgeStore.record`'s elapsed-time check. | L81-L99 | [orchestration_nudges.py](agents-remember/mcp/src/agents_remember/controlplane/orchestration_nudges.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| None. | N/A | N/A |

## Update History

- 2026-07-09T11:19+02:00 — 260707-HFX2-L9: replaced the 30-second effective retry limit with the
  shared 900-second `MIN_REDELIVERY_INTERVAL_SECONDS` floor, added fail-loud below-floor validation,
  and made `next_attempt_at`/`is_rate_limited` apply that floor. Verification metadata pinned until
  closeout stamps the 260707-HFX2-L9 commit.
- 2026-07-08T23:59+02:00 — 260707-HFX2-L8: added `is_ladder_resolved` and made due/redeliverable
  selection explicitly exclude ladder-resolved terminal rows. Verification metadata pinned until
  closeout stamps the HFX2-L8 commit.
- 2026-07-08T14:20+02:00 — 260707-HFX2-L1: created for R3 redelivery backoff math + per-target
  rate limiting. Verification metadata pinned until closeout stamps the 260707-HFX2-L1 commit.
