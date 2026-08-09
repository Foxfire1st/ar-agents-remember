# mcp/src/agents_remember/serving/_app_lifespan.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/serving/_app_lifespan.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-09T06:48+02:00                                            |
| lastVerifiedCommitHash | `2dea095cd68454a7a68893e37c07dbd8daa86d32`                                        |
| lastVerifiedCommitDate | 2026-08-09T18:00:39+02:00|
| governingOverview      | `overview.md`                                          |

## Governing Overview

[None](None)

## Purpose

260731-EFA-L7 responsibility split module for `mcp/src/agents_remember/serving/_app_lifespan.py`; owns the behaviours named by its top-level symbols.
Since 260713-TES-L4 it also owns the notifier loop's last-good settings resilience (R7/N5) and
the dashboard-side relay-death watcher task (N5 — the relay never relays its own death).

## Code Commentary

- `_agent_notifier_context`
- `_agent_notifier_loop`
- `_serving_lifespan`
- `_agent_notifier_heartbeat_payload`

### 260713-TES-L4 Settings Last-Good Loop And Relay-Death Task

`load_agentic_settings` moved INSIDE `_agent_notifier_loop`'s try: a failed read keeps the
previous good configuration for that sweep (fails loud per tick, never kills the loop); with
no last-good snapshot at all the loop skips the sweep and retries after the default interval.
`_agent_notifier_context(runtime, settings=...)` receives the same resolved (possibly
last-good) settings snapshot the enabled-check and interval used. `_serving_lifespan` now also
spawns `relay_death_watch_loop(runtime)` (independent 30s cadence, heartbeat-staleness →
durable `degradation-alert` row to the architect mailbox, marker-file dedupe per tick
identity).

## Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/agents_remember/serving/_app_lifespan.py`.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own top-level surface is listed in Code Commentary; no cross-file citation rows are needed for this split module. | — | — |

## Update History

- 2026-08-09T12:08+02:00 — 260713-TES-L5 curator: recorded the context cleanup —
## 260713-TES-L5 Current Delta — Context Without Nudge Or Escalation Knobs

`_agent_notifier_context` no longer constructs an `OrchestrationNudgeStore` and no longer reads
`settings.escalation` (the family is deleted). It wires `redeliver_budget` and
`escalation_budget` from `settings.agent_notifier` as the per-sweep load-shed caps.

## Update History

- 2026-08-09T12:08+02:00 — 260713-TES-L5 curator: recorded the context cleanup —
  `_agent_notifier_context` no longer wires a `nudge_store` or the escalation SLA/rung/
  respawn knobs (`settings.escalation` no longer exists); `escalation_budget` is read from
  `settings.agent_notifier.escalation_budget` beside `redeliver_budget`. Verification metadata
  pinned until closeout stamps the 260713-TES-L5 commit.
- 2026-08-09T06:48+02:00 — 260713-TES-L4 curator: recorded the last-good settings loop
  (R7/N5 — settings load inside the sweep try, per-tick loud failure, no-last-good skip) and
  the independent relay-death watcher task spawned from `_serving_lifespan` (N5). Verification
  metadata pinned until closeout stamps the 260713-TES-L4 commit.
- 2026-08-08T22:10+02:00 — 260713-TES-L1 completion round (curator): refreshed this sidecar body for the supervisor -> agent-notifier rename (module paths, identifiers, settings keys, wire keys, prose) and the compat seams; verification metadata pinned until closeout stamps the 260713-TES-L1 commit.
- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
