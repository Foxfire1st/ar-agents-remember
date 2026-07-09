# mcp/src/agents_remember/serving/seat_events.py

| Field                  | Value                                            |
| ---------------------- | ---------------------------------------------------- |
| repository             | agents-remember                                        |
| path                   | `mcp/src/agents_remember/serving/seat_events.py`        |
| doc_type               | `file-level-onboarding`                                 |
| lastUpdated            | 2026-07-09T14:05+02:00                                  |
| lastVerifiedCommitHash | `c392985424896e9f392507295a23c4902d0c0696`              |
| lastVerifiedCommitDate | 2026-07-09T14:31:11+02:00|
| governingOverview      | `overview.md`                                           |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

`seat_events.py` emits the observer events that feed the watcher/architect
NEEDS-ATTENTION feed for seat landing, retirement, rename, and turn-state transitions. It exists so
the completion-edge landing hooks, the `session_retire`/`session_rename` MCP tools, and the L5
liveness-sweep turn-state wiring
(`serving/app.py`'s `on_turn_state_change` callback) log identically-shaped `ar-observer-event/v1`
records, rather than each caller hand-rolling its own event shape.

## Code Commentary

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

| Finding | Citations | Source Path |
| --- | --- | --- |
| No external/domain document defines this event shape; the existing `orchestration_nudge_manager` precedent and the `ar-observer-event/v1` schema are the source of truth. | L1-L85 | [seat_events.py](seat_events.py) |

## Repo-Internal References

`seat_events.py` reuses the `observer/` event infrastructure and mirrors an existing event-logging
pattern; it is called by every retire/rename/turn-state mutation path.

| Finding | Citations | Source Path |
| --- | --- | --- |
| `Event`/`now_iso` define the record shape and timestamp helper this module builds every event from. | `Event`; `now_iso` | [../observer/events.py](../observer/events.py) |
| `observer_root`/`EventStore` are the append-only durable log this module writes to. | `observer_root`; `EventStore.append` | [../observer/paths.py](../observer/paths.py); [../observer/store.py](../observer/store.py) |
| `new_ulid` generates the event `id`. | `new_ulid` | [../observer/ulid.py](../observer/ulid.py) |
| `orchestration_nudge_manager` is the existing event-logging pattern this module mirrors (same `EventStore(observer_root(config)).append(Event(...))` shape). | `orchestration_nudge_manager` | [../mcp/tools/orchestration.py](../mcp/tools/orchestration.py) |
| `session_retire_payload`/`session_rename_payload` call `log_retire_event`/`log_rename_event` after a successful mutation. | `session_retire_payload`; `session_rename_payload` | [../mcp/tools/terminal.py](../mcp/tools/terminal.py) |
| `api_terminal_retire`/`api_terminal_rename` call the same functions from the serving endpoints; `api_terminal_landed_cleanup` logs each cleanup retirement; `create_app` wires `on_turn_state_change=lambda observation: log_turn_state_change_event(config, observation.entry)` into the liveness sweeper. | `api_terminal_retire`; `api_terminal_landed_cleanup`; `api_terminal_rename`; `create_app` | [app.py](app.py) |
| `_auto_land_completed_seats` calls `log_landed_event` for every completion-edge landed seat, inside the same best-effort `try/except Exception` guard that wraps the landing body. | `_auto_land_completed_seats` | [../controllers/worktree_tools.py](../controllers/worktree_tools.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The observer event feed is consumed by the local dashboard/watcher surface, not a cross-repo boundary. | — | — |

## Update History

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
