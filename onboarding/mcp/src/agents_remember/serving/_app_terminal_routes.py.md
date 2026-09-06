# mcp/src/agents_remember/serving/_app_terminal_routes.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/serving/_app_terminal_routes.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-09-06T22:06:54+00:00 |
| lastVerifiedCommitHash | `f2b7c648f540efb9d64ceea22e11e651cb5cc914`                                        |
| lastVerifiedCommitDate | 2026-08-31T15:32:32+02:00|
| governingOverview      | `overview.md`                                          |

## Governing Overview

[Serving overview](overview.md)

## Purpose

Owns terminal catalog, open, structural task-assignment, paste/submit, terminate, retire, rename, and
cleanup HTTP route behavior.

## Code Commentary

The WebSocket endpoint attaches only to an already live session. An unavailable attachment closes with 4404; it never creates a replacement process. The bridge carries raw terminal I/O, independently of reliable whole-message adapter submission. On exit it marks a dead process exited, otherwise closes only the attached client, then closes the WebSocket. HTTP callers receive catalog-owned launch/binding facts. cit:([`_serve_terminal_websocket`], mcp/src/agents_remember/serving/_app_terminal_routes.py:86-112).

### Logic

Session-route registration exposes current catalog/open/assignment endpoints. Catalog/open payloads
serialize task-document binding and staged replacement. `_attach_task_response` validates the real
document against topology, applies the generalized assignment primitive, and maps strict success or
refusal models.
The HTTP retirement path now projects both actor and target reviewer parent stamps into `SeatRef`
before calling the same central retirement policy as the MCP path. Thus a sprint architect cannot
retire an orchestrator-owned super reviewer merely because both generations share the sprint
reviewer address.

### Conventions

HTTP routes may use a runtime session id to select the occupant being operated on; the binding itself
is task document plus role.

### Invariants And Boundaries

- No attach-leaf endpoint or leaf-ref compatibility response remains.
- Assignment refuses invalid altitude and occupied singular seats without mutation.
- Open and catalog payloads return server-owned current facts.
- HTTP retirement carries the generation-bound reviewer parent pair into the single authority
  policy; the route does not reimplement ownership.

### Todos

None.

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Session route registration owns terminal open/catalog/assignment endpoints. | `_register_terminal_session_routes` | mcp/src/agents_remember/serving/_app_terminal_routes.py:130-205 |
| Catalog/open payloads use current structural binding. | `_terminal_entry_payload` | mcp/src/agents_remember/serving/_app_terminal_routes.py:207-333 |
| Task assignment delegates validation and generalized mutation. | `_attach_task_response` | mcp/src/agents_remember/serving/_app_terminal_routes.py:335-388 |

## Cross-Repo References

No cross-repository implementation dependency governs this file.

## L23 Dashboard Refusal Transport

Terminal open and task-attach routes map source-lineage refusals to HTTP 409 and
preserve status, detail, and the strict projection. The dashboard receives
operator-actionable evidence while the catalog remains unchanged.

## Update History

- 2026-09-06T22:06:54+00:00 — Preserved source-verified runtime semantics from retired test onboarding; no removed coverage is claimed and verification pins are unchanged.
- 2026-08-31T04:59+02:00 — 260821-ARSPAWN-L5 independent-review repair: recorded HTTP retirement
  propagation of reviewer parent provenance into the shared plane-specific authority policy.
  Verification remains closeout-owned.

- 2026-08-12T20:10+02:00 — L23 curator: documented HTTP transport of lineage admission failures; verification remains closeout-owned.

- 2026-08-11T19:58+02:00 — Aligned the current serving card for `_app_terminal_routes.py` with seat ownership, delivery, lifecycle, and terminal boundaries represented by this source.
- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
