# mcp/src/agents_remember/serving/_app_routes.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/serving/_app_routes.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-08-24T00:51+02:00 |
| lastVerifiedCommitHash | `1d446724d099517f6f52d596b47827ae2391a2a4` |
| lastVerifiedCommitDate | 2026-08-24T00:21:10+02:00 |
| governingOverview      | `overview.md`                                          |

## Governing Overview

[None](None)

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

## Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/agents_remember/serving/_app_routes.py`.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own top-level surface is listed in Code Commentary; no cross-file citation rows are needed for this split module. | — | — |

## Update History

- 2026-08-24T00:51+02:00 — No content impact: 260821-CLIVE-L2 the route module only repoints `finalize_tool_response` to its moved `models.tools` package. Verified at code commit `1d446724`.

- 2026-08-11T19:58+02:00 — Distinguished internal dashboard gate-decision finalization from the
  agent-facing structural `gate_decide` tool name.
- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
