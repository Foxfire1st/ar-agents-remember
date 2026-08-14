# mcp/tests/test_terminal_ws_websocket_1.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_terminal_ws_websocket_1.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-07T22:45:00+02:00                                            |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`                                        |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `overview.md`                                          |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Terminal HTTP/WebSocket suite for session I/O, lifecycle cleanup, catalog projection, and task-aware open.

## Code Commentary

### Logic

Cases prove PTY forwarding and teardown, catalog reconciliation, termination/landing cleanup, and terminal open with canonical task-document persistence. Required task identity failures are explicit, while an intentionally unbound raw terminal remains supported where the endpoint contract allows it.

### Conventions

Test-only evidence uses deterministic fakes/fixtures and exercises the owning seam directly.

### Invariants And Boundaries

The server owns the catalog row returned to clients; task claims use structured references and never accept a leaf-key attachment payload.

## Docs References

No Domain Documentation source is configured for this repository-local regression contract.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Current suite declaration anchoring this card. | `TerminalWebSocketTests1` | mcp/tests/test_terminal_ws_websocket_1.py:14-14 |

## Cross-Repo References

No cross-repository implementation source governs this test module.

## Update History

- 2026-08-11T19:58+02:00 — Reconciled `test_terminal_ws_websocket_1.py` with its current structural task/seat, tool-vocabulary, or quality-boundary regression contract and removed stale exact-id/leaf implications where present.
- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
