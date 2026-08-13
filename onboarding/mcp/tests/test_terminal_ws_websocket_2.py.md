# mcp/tests/test_terminal_ws_websocket_2.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_terminal_ws_websocket_2.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-07T22:45:00+02:00                                            |
| lastVerifiedCommitHash | `1580f92715ff93c988f9a15439ad9bec60ef4c5d`                                        |
| lastVerifiedCommitDate | 2026-08-13T00:18:59+02:00|
| governingOverview      | `overview.md`                                          |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Terminal route suite for structural task attachment, seat collision, harness launch, and reopen behavior.

## Code Commentary

### Logic

`attach-task` binds a current session by canonical task document and role, refuses unknown/unmatchable/terminated/landed targets, and enforces role-scoped uniqueness. Reopen preserves live truth and replaces only dead ownership; settings-owned harness selections remain complete and validated.

### Conventions

Test-only evidence uses deterministic fakes/fixtures and exercises the owning seam directly.

### Invariants And Boundaries

Document sharing across distinct roles is valid; a second live occupant of the same document+role fails; attachment never depends on a caller-supplied occupant for another agent seat.

## Docs References

No Domain Documentation source is configured for this repository-local regression contract.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Current suite declaration anchoring this card. | `TerminalWebSocketTests2` | mcp/tests/test_terminal_ws_websocket_2.py:13-373 |

## Cross-Repo References

No cross-repository implementation source governs this test module.

## L23 HTTP 409 Lineage Refusals

The extension suite advances super and proves both terminal open and task attach
return HTTP 409 with `source-lineage-stale` evidence. Neither a host process nor
an existing catalog binding is mutated on refusal.

## Update History
- 2026-08-12T20:10+02:00 — L23 curator: documented dashboard-route fail-closed lineage responses; verification remains closeout-owned.

- 2026-08-11T19:58+02:00 — Reconciled `test_terminal_ws_websocket_2.py` with its current structural task/seat, tool-vocabulary, or quality-boundary regression contract and removed stale exact-id/leaf implications where present.
- 2026-08-10T13:00+02:00 — 260731-EFA-L9 curator: No content impact: re-read the split terminal-WebSocket test card against its current staged source; the documented coverage remains accurate. Verification metadata remains pinned until closeout.
- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
