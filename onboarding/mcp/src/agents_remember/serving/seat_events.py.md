# mcp/src/agents_remember/serving/seat_events.py

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

## Evidence

### Docs References

No relevant external documentation found after checking the repo Domain Documentation for
observer-event-specific behavior; this file follows an existing internal event-logging convention,
not an external standard.

- No external/domain document defines this event shape; the existing `orchestration_nudge_manager` precedent and the `ar-observer-event/v1` schema are the source of truth. [1]

### Repo-Internal References

`seat_events.py` reuses the `observer/` event infrastructure and mirrors an existing event-logging
pattern; it is called by every retire/rename/turn-state mutation path.

- `Event`/`now_iso` define the record shape and timestamp helper this module builds every event from. [2]
- `observer_root`/`EventStore` are the append-only durable log this module writes to. [3]
- `new_ulid` generates the event `id`. [4]
- `orchestration_nudge_manager` is the existing event-logging pattern this module mirrors (same `EventStore(observer_root(config)).append(Event(...))` shape). [5]
- `session_retire_payload`/`session_rename_payload` call `log_retire_event`/`log_rename_event` after a successful mutation. [6]
- `api_terminal_retire`/`api_terminal_rename` call the same functions from the serving endpoints; `api_terminal_landed_cleanup` logs each cleanup retirement; `create_app` wires `on_turn_state_change=lambda observation: log_turn_state_change_event(config, observation.entry)` into the liveness sweeper. [7]
- `auto_complete_seats` calls `log_retire_event` for default automatic closes and `log_landed_event` for the settings opt-out; both remain subordinate to edge success. [8]

### Cross-Repo References

No meaningful cross-repo references found.

The observer event feed is consumed by the local dashboard/watcher surface, not a cross-repo boundary.
