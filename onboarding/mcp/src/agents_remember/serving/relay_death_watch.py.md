# mcp/src/agents_remember/serving/relay_death_watch.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/relay_death_watch.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-09T06:48+02:00 |
| lastVerifiedCommitHash | `c51373425be3e3f488590ad2f444810df89b4ffb` |
| lastVerifiedCommitDate | 2026-08-26T19:22:10+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[serving overview](overview.md)

## Purpose

Independent relay-death surfacing (N5): the agent-notifier relay never relays its own death.
This dashboard-side watcher runs on its own cadence, reads the notifier heartbeat row, and —
when the tick goes stale past the configured cutoff — posts one durable `degradation-alert`
row to the architect mailbox. It is deliberately NOT part of the notifier loop, bounded by an
append-only marker file (one post per stale heartbeat identity) and by the inbox store's D4
cap, and fail-safe on settings-read failure (default cutoff).

## Code Commentary

### Logic

- `RELAY_DEATH_WATCH_INTERVAL_SECONDS = 30.0` cit:([`RELAY_DEATH_WATCH_INTERVAL_SECONDS`], mcp/src/agents_remember/serving/relay_death_watch.py:44-44) — the watcher's
  independent cadence, decoupled from the notifier sweep interval.
- `RELAY_DEATH_MARKER_FILENAME = "agent-notifier-death-watch.json"` cit:([`RELAY_DEATH_MARKER_FILENAME`], mcp/src/agents_remember/serving/relay_death_watch.py:47-47) —
  the durable dedupe marker lives under `observer_root/workspace/`.
- `RelayDeathMarker` cit:([`RelayDeathMarker`], mcp/src/agents_remember/serving/relay_death_watch.py:51-56) — one post-per-stale-heartbeat identity:
  which tick was reported, and when/where.
- `RelayDeathMarkerStore` cit:([`RelayDeathMarkerStore`], mcp/src/agents_remember/serving/relay_death_watch.py:58-89) — tiny durable marker preventing a
  stale-heartbeat post storm across watcher restarts; `read()` returns `None` on
  missing/corrupt content, `write()` uses `atomic_write_text`.
- `_stale_cutoff_seconds` cit:([`_stale_cutoff_seconds`], mcp/src/agents_remember/serving/relay_death_watch.py:91-98) — the configured stale cutoff with a
  default fallback (`DEFAULT_AGENT_NOTIFIER_STALE_CUTOFF_SECONDS`) when settings are
  unreadable.
- `post_relay_death_signal` cit:([`post_relay_death_signal`], mcp/src/agents_remember/serving/relay_death_watch.py:100-152) — returns `False` when there is no
  heartbeat at all (the relay is opt-in, so absence is not evidence of death), when the tick is
  fresh, or when the marker already names this `lastTickAt`. Otherwise it derives the scoped
  architect owner, appends a `degradation-alert` row (reason text carries the heartbeat age and
  cutoff), writes the marker, and best-effort pushes the row to a live architect seat.
- `_try_deliver` cit:([`_try_deliver`], mcp/src/agents_remember/serving/relay_death_watch.py:155-164) — best-effort push; the durable row is the surface
  regardless, so delivery failure is swallowed.
- `relay_death_watch_loop` cit:([`relay_death_watch_loop`], mcp/src/agents_remember/serving/relay_death_watch.py:167-174) — the `asyncio` loop spawned from
  `_app_lifespan._serving_lifespan`; sleeps the independent cadence, runs the check in a
  worker thread, logs-and-continues on failure.

### Conventions

The watcher writes through the same durable inbox row shape as every other poster
(`create_operator_inbox_entry` with routing/owner/poster), so its alert is indistinguishable in
mechanism from an ordinary row. It never mutates the heartbeat store and never writes the
notifier's own logs.

### Invariants And Boundaries

- The relay never relays its own death: this module is the observer/dashboard-side path (N5),
  never a notifier-loop action.
- One durable alert per stale heartbeat identity; the marker re-arms only when the heartbeat
  ticks again (a fresh `lastTickAt`).
- A heartbeat that never ticked is silent — opt-in posture, same as the staleness banner.
- Settings-read failure falls back to the default cutoff; the loop itself logs and retries next
  interval.
- Boundedness: marker file is one tiny JSON document; the alert row is bounded by the inbox
  store's D4 cap.

### Todos

None.

## Docs References

No Domain Documentation entries are configured in the resolved `system/sources.md`; the
heartbeat-staleness and degradation-alert semantics are same-repository runtime behavior proven
by source and tests.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external/domain document defines this watcher; N5 ruling and the tests are the authority. | `post_relay_death_signal` | mcp/src/agents_remember/serving/relay_death_watch.py:100-152 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The heartbeat row and age helper the watcher reads. | `AgentNotifierHeartbeatStore`; `heartbeat_age_seconds` | mcp/src/agents_remember/serving/agent_notifier_heartbeat.py:63-125; mcp/src/agents_remember/serving/agent_notifier_heartbeat.py:128-138 |
| The scoped architect mailbox the alert is addressed to (role-only fallback when no scoped seat). | `derive_architect_owner` | mcp/src/agents_remember/controlplane/signal_routing.py:111-120 |
| The durable push path for the alert row. | `deliver_inbox_entry` | mcp/src/agents_remember/serving/inbox_delivery.py:165-223 |
| The loop task is spawned by the serving lifespan beside the notifier loop. | `_serving_lifespan` | mcp/src/agents_remember/serving/_app_lifespan.py:168-213 |


## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary owns or consumes this watcher. | — | — |

## Update History

- 2026-08-11T19:58+02:00 — Aligned the current serving card for `relay_death_watch.py` with seat ownership, delivery, lifecycle, and terminal boundaries represented by this source.
- 2026-08-09T06:48+02:00 — 260713-TES-L4 curator: created this file-level onboarding card for
  the new relay-death watcher module (N5): independent 30s cadence, heartbeat-staleness →
  architect-mailbox `degradation-alert`, per-tick-identity marker dedupe, default-cutoff
  settings fallback, best-effort delivery, loop wiring from `_serving_lifespan`. Verification
  metadata pinned until closeout stamps the 260713-TES-L4 commit.
