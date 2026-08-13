# mcp/src/agents_remember/serving/seat_events.py

| Field                  | Value                                            |
| ---------------------- | ---------------------------------------------------- |
| repository             | agents-remember                                        |
| path                   | `mcp/src/agents_remember/serving/seat_events.py`        |
| doc_type               | `file-level-onboarding`                                 |
| lastUpdated            | 2026-08-02T01:05+02:00 |
| lastVerifiedCommitHash | `1580f92715ff93c988f9a15439ad9bec60ef4c5d`              |
| lastVerifiedCommitDate | 2026-08-13T00:18:59+02:00|
| governingOverview      | `overview.md`                                           |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

`seat_events.py` emits the observer events that feed the watcher/architect
NEEDS-ATTENTION feed for seat landing, retirement, rename, and turn-state transitions. It exists so
the completion-edge close-or-land hooks, the `session_retire`/`session_rename` MCP tools, and the L5
liveness-sweep turn-state wiring
(`serving/app.py`'s `on_turn_state_change` callback) log identically-shaped `ar-observer-event/v1`
records, rather than each caller hand-rolling its own event shape.

## Code Commentary

### 260707-HFX2-L17 Event Identity

Seat observer events now include current `seatRole` beside historical `spawnRole`, allowing event
consumers to distinguish origin provenance from the leaf-role binding that rename/retire/turn-state
operations currently affect.

### Logic

Four functions, each building one `Event` and appending it via `EventStore(observer_root(config))`:

- `log_retire_event(config, entry)` — kind `"seat.retired"`, `ts=entry.retired_at or now_iso()`,
  `trust="observed"`, `actor="system" if entry.retired_by_session is None else "model"`.
  Dashboard landed-group cleanup and other system-driven cleanup can pass `by_session=None`; manual
  retire is attributed to `"model"`. Data payload carries `session`, `label`, `spawnRole`,
  `leafKey`, `retiredBySession`, `retiredReason`, `retiredEdge`.
- `log_landed_event(config, entry)` — kind `"seat.landed"`, `ts=entry.landed_at or now_iso()`,
  `trust="observed"`, `actor="system"`. Data payload carries `session`, `label`, `spawnRole`,
  `leafKey`, `landedReason`, `landedEdge`.
- `log_rename_event(config, entry)` — kind `"seat.renamed"`, `ts=now_iso()` (rename has no dedicated
  provenance timestamp field on the entry, unlike retire), `trust="observed"`, `actor="model"`
  (rename is always a self-declared/actor-driven action, never automated). Data payload carries
  `session`, `label`, `spawnedLabel`, `spawnRole`.
- `log_turn_state_change_event(config, entry)` — kind `"seat.turn-state-changed"`,
  `ts=entry.turn_state_changed_at or now_iso()`, `trust="inferred"` (distinct from the other two's
  `"observed"` — a turn-state classification is a best-effort marker-regex INFERENCE, not a directly
  observed fact like a retire/rename action), `actor="system"`. Data payload carries `session`,
  `label`, `turnState`, `spawnRole`.

All four mirror the existing `orchestration_nudge_manager` event-logging pattern
(`new_ulid()` for `id`, `EventStore(observer_root(config)).append(Event(...))`) rather than
inventing a new logging shape.

### Conventions

Every function takes `(config: McpRuntimeConfig, entry: TerminalCatalogEntry)` and returns `None` —
fire-and-forget logging, called by the caller AFTER a successful catalog mutation, never before.

### Invariants And Boundaries

- `log_turn_state_change_event` is called ONLY on an actual state transition
  (`TerminalLivenessObservation.turn_state_changed`), never once per sweep tick — that gating lives
  in the CALLER (`terminal_liveness.py`'s `on_turn_state_change` wiring in `serving/app.py`), not in
  this module; this module has no opinion on when it is called, only how the event is shaped.
- `McpRuntimeConfig` is imported only under `TYPE_CHECKING` — a type-only import to avoid pulling
  the full config module at runtime for a file that only needs the type for its signature.

### Todos

No known follow-up in this file.

## Docs References

No relevant external documentation found after checking the repo Domain Documentation for
observer-event-specific behavior; this file follows an existing internal event-logging convention,
not an external standard.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external/domain document defines this event shape; the existing `orchestration_nudge_manager` precedent and the `ar-observer-event/v1` schema are the source of truth. | "def log_retire_event" | mcp/src/agents_remember/serving/seat_events.py:28-28 |

## Repo-Internal References

`seat_events.py` reuses the `observer/` event infrastructure and mirrors an existing event-logging
pattern; it is called by every retire/rename/turn-state mutation path.

| Finding | Anchor | Source |
| --- | --- | --- |
| `Event`/`now_iso` define the record shape and timestamp helper this module builds every event from. | `Event`; `now_iso` | mcp/src/agents_remember/observer/events.py:34-36; mcp/src/agents_remember/observer/events.py:39-64 |
| `observer_root`/`EventStore` are the append-only durable log this module writes to. | `observer_root` | mcp/src/agents_remember/observer/store.py:106-107 |
| `new_ulid` generates the event `id`. | `new_ulid` | mcp/src/agents_remember/observer/ulid.py:30-41 |
| `orchestration_nudge_manager` is the existing event-logging pattern this module mirrors (same `EventStore(observer_root(config)).append(Event(...))` shape). | "def orchestration_nudge_manager_payload" | mcp/src/agents_remember/mcp/tools/orchestration.py:19-19 |
| `session_retire_payload`/`session_rename_payload` call `log_retire_event`/`log_rename_event` after a successful mutation. | `session_retire_payload`; `session_rename_payload` | mcp/src/agents_remember/mcp/tools/terminal.py:66-83; mcp/src/agents_remember/mcp/tools/terminal.py:86-95 |
| `api_terminal_retire`/`api_terminal_rename` call the same functions from the serving endpoints; `api_terminal_landed_cleanup` logs each cleanup retirement; `create_app` wires `on_turn_state_change=lambda observation: log_turn_state_change_event(config, observation.entry)` into the liveness sweeper. | `api_terminal_retire`; `api_terminal_landed_cleanup`; `api_terminal_rename`; `create_app` | mcp/src/agents_remember/serving/_app_terminal_routes.py:707-709; mcp/src/agents_remember/serving/_app_terminal_routes.py:769-781; mcp/src/agents_remember/serving/_app_terminal_routes.py:783-789; mcp/src/agents_remember/serving/app.py:230-290 |
| `auto_complete_seats` calls `log_retire_event` for default automatic closes and `log_landed_event` for the settings opt-out; both remain subordinate to edge success. | `auto_complete_seats` | mcp/src/agents_remember/application/completion_cleanup.py:27-108 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| The observer event feed is consumed by the local dashboard/watcher surface, not a cross-repo boundary. | — | — |

## Update History

- 2026-08-11T19:58+02:00 — Aligned the current serving card for `seat_events.py` with seat ownership, delivery, lifecycle, and terminal boundaries represented by this source.
- 2026-08-10T10:35+02:00 — 260731-EFA-L9 curator repair: refreshed this staged card from the current onboarding body and re-resolved moved/deleted citations; verification metadata remains pinned until L9 closeout.\n
- 2026-08-10T05:45+02:00 — 260805-ARG-L1 relationship update: default completion emits
  system-attributed `seat.retired`; the explicit landed opt-out still emits `seat.landed`.

- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B24 curator: replaced the `n/a` rows with exact
  anchors and removed duplicated ranges; exact non-fixing check returns zero findings.

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-10T15:07+02:00 — 260707-HFX2-L17: added current binding-role provenance to seat events
  while retaining immutable spawn-role history.

- 2026-07-09T14:05+02:00 — 260707-HFX2-L11 curator correction: documented `log_landed_event`
  (`seat.landed`) and corrected the completion-edge reference from auto-retire to auto-land; retire
  events now describe explicit/manual or landed-cleanup termination paths, while successful
  integration/finalize edges emit landing events. Verification metadata pinned until closeout stamps
  the HFX2-L11 commit.
- 2026-07-08T02:43+02:00 — Created for 260707-HFX-L8 (seat retirement + live identity + turn-state):
  `log_retire_event`/`log_rename_event`/`log_turn_state_change_event`, mirroring the existing
  `orchestration_nudge_manager` event-logging pattern to feed the watcher/architect NEEDS-ATTENTION
  feed with `ar-observer-event/v1` records (`seat.retired`/`seat.renamed`/
  `seat.turn-state-changed`). Turn-state events fire only on an actual transition, gated by the
  caller. Verification metadata pinned until closeout stamps the HFX-L8 commit.
