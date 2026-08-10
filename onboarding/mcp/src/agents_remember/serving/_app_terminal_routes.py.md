# mcp/src/agents_remember/serving/_app_terminal_routes.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/serving/_app_terminal_routes.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-07T22:45:00+02:00                                            |
| lastVerifiedCommitHash | `a84add4c9422b18a26f1748dedaed16194994ded`                                        |
| lastVerifiedCommitDate | 2026-08-10T05:11:18+02:00|
| governingOverview      | `overview.md`                                          |

## Governing Overview

[None](None)

## Purpose

260731-EFA-L7 responsibility split module for `mcp/src/agents_remember/serving/_app_terminal_routes.py`; owns the behaviours named by its top-level symbols.

## Code Commentary

## 260713-TES-L6 Current Delta — Sprint Provenance Projection

Terminal session responses now project `spawnRepo` and `spawnSprint`, and opener refusals preserve
the shared sprint-binding status without creating a terminal. The HTTP layer remains an adapter:
binding decisions and write-once conflict checks live in the shared serving policy used by both
dashboard and MCP routes.

- `_detected_harnesses_payload`
- `_register_terminal_session_routes`
- `_landed_cleanup_response`
- `_terminal_entry_payload`
- `_open_terminal_response`
- `_attach_leaf_response`
- `_live_paste_target`
- `_harness_submit_response`
- `_pane_paste_response`
- `_paste_response`
- `_terminate_response`
- `_retire_response`
- `_seat_ref`
- `_rename_response`
- `_write_paste_image`
- `_register_terminal_control_routes`

## Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/agents_remember/serving/_app_terminal_routes.py`.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own top-level surface is listed in Code Commentary; no cross-file citation rows are needed for this split module. | — | — |

## Update History

- 2026-08-10T04:39+02:00 — 260713-TES-L6: documented sprint provenance in terminal responses and
  fail-before-open binding refusals. Verification metadata remains pinned until closeout stamps the
  code commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
