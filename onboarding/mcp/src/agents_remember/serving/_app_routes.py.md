# mcp/src/agents_remember/serving/_app_routes.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/serving/_app_routes.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-09-15T20:42+02:00 |
| lastVerifiedCommitHash | `e9678c56e7f441371584ad8a18e2b9380cb38cf0` |
| lastVerifiedCommitDate | 2026-09-15T20:50:53+02:00|
| governingOverview      | `overview.md`                                          |

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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The state response merges the serve-time tail onto a copy of the memoized body. | `_state_response` | mcp/src/agents_remember/serving/_app_routes.py:77-108 |
| The SSE route hands the same readers to the projection stream. | `_register_projection_routes` | mcp/src/agents_remember/serving/_app_routes.py:124-177 |
| The observer-health reader whose `None` makes the key absent. | `_terminal_observer_health_payload` | mcp/src/agents_remember/serving/_app_lifespan.py:376-394 |

## Update History

- 2026-09-15T20:42+02:00 — 260831-LOCR-L17 curator (uncommitted change set on `ar/260831-locr-l17`,
  base `99534dc5`, `_app_routes.py` +12/−2): both state routes now pass the observer-health reader
  into the tail, so the card records the current read-only wiring: `_state_response` merges the three
  readers onto a copy of the memoized dump and the SSE generator receives the same three, with
  `_terminal_observer_health_payload` returning `None` when no valid row exists for the current
  serving lifetime — which is what makes the key absent rather than null. Recorded that these routes
  only read: no GET/SSE rewrites, repairs, creates or deletes the health row, and the projection
  revision, ETag, 304 path and delta shape are untouched. Also repaired this card's governing
  overview link, which read `[None](None)`, to the serving route overview. Verification metadata
  remains closeout-owned; no stamp advanced.

- 2026-08-24T00:51+02:00 — No content impact: 260821-CLIVE-L2 the route module only repoints `finalize_tool_response` to its moved `models.tools` package. Verified at code commit `1d446724`.

- 2026-08-11T19:58+02:00 — Distinguished internal dashboard gate-decision finalization from the
  agent-facing structural `gate_decide` tool name.
- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
