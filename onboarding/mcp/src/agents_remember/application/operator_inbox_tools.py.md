# mcp/src/agents_remember/application/operator_inbox_tools.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/operator_inbox_tools.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-09T06:48+02:00 |
| lastVerifiedCommitHash | `cdca11264fb4d27ee08f5e8b37ac5496e67c0840` |
| lastVerifiedCommitDate | 2026-08-09T07:36:31+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[overview](overview.md)

## Purpose

Application operations for the ``operator_inbox_*`` return channel.

## Code Commentary

### Logic

Module-level surface:

- `_result` (function, lines 31-33) — Return the raw use-case result for the MCP adapter to finalize.
- `_store` (function, lines 40-41)
- `_entry_payload` (function, lines 44-45)
- `operator_inbox_post_tool` (function, lines 48-68)
- `post_operator_inbox` (function, lines 71-98) — Compose flat transport fields into one operator-inbox post use case.
- `operator_inbox_poll_tool` (function, lines 101-127) — lists pending rows, plus terminal
  markers when `include_terminal=True` (N11), via `list_for_mailbox`.
- `operator_inbox_consume_tool` (function, lines 130-151) — optional attribution marker only
  (N16): stamps `consumedAt`/`By`/`Via`, never changes state, and performs no expectation
  lookup (the ack-by fulfillment block is gone).
- `operator_inbox_supersede_tool` (function, lines 154-180) — explicit supersession (R11):
  calls `mark_superseded` and returns the terminal marker (`state`, `terminalAt`,
  `terminalReason`, `supersededBy`); never inferred from artifacts/branches/task state.

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.

### Todos

None.

## Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| Defines the function `_result` (lines 31-33) — Return the raw use-case result for the MCP adapter to finalize.. | `_result` | mcp/src/agents_remember/application/operator_inbox_tools.py:28-30 |
| Defines the function `_store` (lines 40-41). | `_store` | mcp/src/agents_remember/application/operator_inbox_tools.py:37-38 |
| Defines the function `_entry_payload` (lines 44-45). | `_entry_payload` | mcp/src/agents_remember/application/operator_inbox_tools.py:41-42 |
| Defines the function `operator_inbox_post_tool` (lines 48-68). | `operator_inbox_post_tool` | mcp/src/agents_remember/application/operator_inbox_tools.py:45-65 |
| Defines the function `post_operator_inbox` (lines 71-98) — Compose flat transport fields into one operator-inbox post use case.. | `post_operator_inbox` | mcp/src/agents_remember/application/operator_inbox_tools.py:68-95 |
| Defines the function `operator_inbox_poll_tool` (lines 101-124). | `operator_inbox_poll_tool` | mcp/src/agents_remember/application/operator_inbox_tools.py:98-123 |
| Defines the function `operator_inbox_consume_tool` (lines 127-158). | `operator_inbox_consume_tool` | mcp/src/agents_remember/application/operator_inbox_tools.py:126-150 |

## Update History

- 2026-08-09T06:48+02:00 — 260713-TES-L4 curator: recorded the `include_terminal` poll
  surface (N11), the attribution-only consume (N16 — no ack-by expectation fulfillment, state
  unchanged), and the new `operator_inbox_supersede_tool` (R11 explicit supersession).
  Verification metadata pinned until closeout stamps the 260713-TES-L4 commit.
- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
