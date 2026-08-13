# mcp/src/agents_remember/serving/_app_terminal_routes.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/serving/_app_terminal_routes.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-08-11T10:28+02:00 |
| lastVerifiedCommitHash | `1580f92715ff93c988f9a15439ad9bec60ef4c5d`                                        |
| lastVerifiedCommitDate | 2026-08-13T00:18:59+02:00|
| governingOverview      | `overview.md`                                          |

## Governing Overview

[Serving overview](overview.md)

## Purpose

Owns terminal catalog, open, structural task-assignment, paste/submit, terminate, retire, rename, and
cleanup HTTP route behavior.

## Code Commentary

### Logic

Session-route registration exposes current catalog/open/assignment endpoints. Catalog/open payloads
serialize task-document binding and staged replacement. `_attach_task_response` validates the real
document against topology, applies the generalized assignment primitive, and maps strict success or
refusal models.

### Conventions

HTTP routes may use a runtime session id to select the occupant being operated on; the binding itself
is task document plus role.

### Invariants And Boundaries

- No attach-leaf endpoint or leaf-ref compatibility response remains.
- Assignment refuses invalid altitude and occupied singular seats without mutation.
- Open and catalog payloads return server-owned current facts.

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
- 2026-08-12T20:10+02:00 — L23 curator: documented HTTP transport of lineage admission failures; verification remains closeout-owned.

- 2026-08-11T19:58+02:00 — Aligned the current serving card for `_app_terminal_routes.py` with seat ownership, delivery, lifecycle, and terminal boundaries represented by this source.
- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
