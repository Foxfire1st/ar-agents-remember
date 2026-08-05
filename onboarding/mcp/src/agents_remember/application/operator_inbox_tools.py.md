# mcp/src/agents_remember/application/operator_inbox_tools.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/operator_inbox_tools.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
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
- `operator_inbox_poll_tool` (function, lines 101-124)
- `operator_inbox_consume_tool` (function, lines 127-158)

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
| Defines the function `_result` (lines 31-33) — Return the raw use-case result for the MCP adapter to finalize.. | `_result` | mcp/src/agents_remember/application/operator_inbox_tools.py:31-33 |
| Defines the function `_store` (lines 40-41). | `_store` | mcp/src/agents_remember/application/operator_inbox_tools.py:40-41 |
| Defines the function `_entry_payload` (lines 44-45). | `_entry_payload` | mcp/src/agents_remember/application/operator_inbox_tools.py:44-45 |
| Defines the function `operator_inbox_post_tool` (lines 48-68). | `operator_inbox_post_tool` | mcp/src/agents_remember/application/operator_inbox_tools.py:48-68 |
| Defines the function `post_operator_inbox` (lines 71-98) — Compose flat transport fields into one operator-inbox post use case.. | `post_operator_inbox` | mcp/src/agents_remember/application/operator_inbox_tools.py:71-98 |
| Defines the function `operator_inbox_poll_tool` (lines 101-124). | `operator_inbox_poll_tool` | mcp/src/agents_remember/application/operator_inbox_tools.py:101-124 |
| Defines the function `operator_inbox_consume_tool` (lines 127-158). | `operator_inbox_consume_tool` | mcp/src/agents_remember/application/operator_inbox_tools.py:127-158 |

## Update History

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
