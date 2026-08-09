# mcp/tests/test_codex_app_server_adapter_reconnect.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_codex_app_server_adapter_reconnect.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-09T20:03+02:00                                            |
| lastVerifiedCommitHash | `fb0296562ceb29929a3675a1b0195700d23bc56a`                                        |
| lastVerifiedCommitDate | 2026-08-09T20:35:49+02:00|
| governingOverview      | `overview.md`                                          |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Reconnect and correlated-response coverage for the native Codex adapter. It proves command
approvals, structured content-bearing MCP elicitation, and Codex's exact empty-form MCP tool
approval loop. The latter covers all three scalar actions: accept maps to an empty content object,
while decline and cancel remain action-only.

## Code Commentary

- `test_correlated_server_approval_and_elicitation_responses` starts one adapter, correlates each
  response to its exact server RPC, preserves the existing structured form response, then emits
  empty `requestedSchema.properties` tool approvals and proves `accept`, `decline`, and `cancel`
  produce the native result shapes expected by Codex.
- `test_mcp_elicitation_response_edges_remain_typed_and_fail_closed` pins the complementary
  boundaries: scalar accept is refused for a content-bearing form, malformed structured actions
  fail closed, accepted structured forms require content, non-form and malformed-form requests do
  not gain action buttons, and the adjacent permissions response path remains unchanged.


## Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/tests/test_codex_app_server_adapter_reconnect.py`.
- Content-bearing forms must continue using structured JSON; the action-button cases are limited to
  the exact empty-form schema.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Correlated structured and empty-form elicitation response coverage. | `test_correlated_server_approval_and_elicitation_responses` | mcp/tests/test_codex_app_server_adapter_reconnect.py:44-124 |
| Typed/fail-closed response-shape and action-button boundary coverage. | `test_mcp_elicitation_response_edges_remain_typed_and_fail_closed` | mcp/tests/test_codex_app_server_adapter_reconnect.py:127-161 |

## Update History

- 2026-08-09T20:03+02:00 — 260713-TES-L5F2: added direct negative-edge coverage for non-empty
  scalar acceptance, malformed structured results, and non-actionable form shapes.

- 2026-08-09T19:36+02:00 — 260713-TES-L5F2: added protocol-faithful empty-form MCP tool approval
  coverage for accept, decline, and cancel while retaining the non-empty structured form case.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
