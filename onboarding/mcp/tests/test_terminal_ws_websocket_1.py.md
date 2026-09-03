# mcp/tests/test_terminal_ws_websocket_1.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_terminal_ws_websocket_1.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | `6f10c24d72db6171c0d434b307e6806996e2f11d`                                        |
| lastVerifiedCommitDate | 2026-09-02T18:10:52+02:00|
| governingOverview      | `overview.md`                                          |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Terminal HTTP/WebSocket suite for session I/O, lifecycle cleanup, catalog projection, and task-aware open. L21 added the agent-notifier-disabled settings fixture so stale-session reconciliation runs without notification side effects.

## Code Commentary

### Logic

Cases prove PTY forwarding and teardown, catalog reconciliation, termination/landing cleanup, and terminal open with canonical task-document persistence. The cleanup fixture marks its nominal running row live in the fake host, so the assertion distinguishes status-based cleanup from background liveness reconciliation. Required task identity failures are explicit, while an intentionally unbound raw terminal remains supported where the endpoint contract allows it.

L21's `test_get_terminal_sessions_marks_stale_tmux_rows_exited` now writes a
`settings.json` with `{"orchestration": {"agentNotifier": {"enabled": false}}}` into the
coordination root before hitting the sessions endpoint, keeping the enumeration assertion free of
agent-notifier publication.

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
| Stale tmux rows are marked exited with agent notifications disabled. | `test_get_terminal_sessions_marks_stale_tmux_rows_exited` | mcp/tests/test_terminal_ws_websocket_1.py:196-210 |

## Cross-Repo References

No cross-repository implementation source governs this test module.

## Update History

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for
  6f10c24d72db6171c0d434b307e6806996e2f11d (CCR-R21@v2/L21): recorded the L21 settings fixture in
  `test_get_terminal_sessions_marks_stale_tmux_rows_exited` that disables the agent notifier
  before the stale-session enumeration assertion. Verification is pinned to the owning commit.

- 2026-08-31T12:00+02:00 — A005 made the landed-cleanup fixture's running row actually live so
  the background liveness sweep cannot rewrite the condition being tested. Verification remains
  closeout-owned.

- 2026-08-11T19:58+02:00 — Reconciled `test_terminal_ws_websocket_1.py` with its current structural task/seat, tool-vocabulary, or quality-boundary regression contract and removed stale exact-id/leaf implications where present.
- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
