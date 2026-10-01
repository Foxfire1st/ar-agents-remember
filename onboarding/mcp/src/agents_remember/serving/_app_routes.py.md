# mcp/src/agents_remember/serving/_app_routes.py

## Governing Overview

[serving overview](overview.md)

## Purpose

260731-EFA-L7 responsibility split module for `mcp/src/agents_remember/serving/_app_routes.py`; owns the behaviours named by its top-level symbols.

## Code Commentary

- `_state_response`
- `_task_document_response`
- `_register_projection_routes`
- `_recorded_gate_decision`
- `_gate_decision_response`
- `_dismissal_response`
- `_action_response`
- `_operator_inbox_response`
- `_inbox_dismiss_response`
- `_register_action_routes`

Recorded dashboard gate decisions finalize under the internal
`gate_decide_internal` vocabulary. This route is an internal projection/action seam and must not
mislabel itself as the agent-facing structural `gate_decide` tool.

The state routes assemble the serve-time tail from `_app_lifespan`'s payload readers: `_state_response`
merges `served_state_tail(build=…, heartbeat=_agent_notifier_heartbeat_payload(runtime),
observer_health=_terminal_observer_health_payload(runtime))` onto a copy of the memoized projection
dump, and the SSE generator is handed the same three readers. Since `LOCR-R17@v1` that third reader
resolves the observer stage's own persisted health row for the CURRENT serving lifetime and returns
`None` when no valid row exists, which is what makes `terminalObserverHealth` absent rather than null.
The routes only read: neither `/api/state` nor the SSE stream writes, repairs, creates or deletes the
health row, and neither can change the projection revision, the ETag, the 304 path or the delta shape.

## Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/agents_remember/serving/_app_routes.py`.

## Evidence

### Repo-Internal References

- The state response merges the serve-time tail onto a copy of the memoized body. [1]
- The SSE route hands the same readers to the projection stream. [2]
- The observer-health reader whose `None` makes the key absent. [3]
