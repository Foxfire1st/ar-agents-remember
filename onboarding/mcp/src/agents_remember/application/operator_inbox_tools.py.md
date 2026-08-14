# mcp/src/agents_remember/application/operator_inbox_tools.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/operator_inbox_tools.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
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
| Defines the function `_result` (lines 31-33) — Return the raw use-case result for the MCP adapter to finalize.. | `_result` | mcp/src/agents_remember/application/operator_inbox_tools.py:28-30 |
| Defines the function `_store` (lines 40-41). | `_store` | mcp/src/agents_remember/application/operator_inbox_tools.py:39-40 |
| Defines the function `_entry_payload` (lines 44-45). | `_entry_payload` | mcp/src/agents_remember/application/operator_inbox_tools.py:43-44 |
| Defines the function `operator_inbox_post_tool` (lines 48-68). | `operator_inbox_post_tool` | mcp/src/agents_remember/application/operator_inbox_tools.py:47-67 |
| Defines the function `post_operator_inbox` (lines 71-98) — Compose flat transport fields into one operator-inbox post use case.. | `post_operator_inbox` | mcp/src/agents_remember/application/operator_inbox_tools.py:70-97 |
| Defines the function `operator_inbox_poll_tool` (lines 101-124). | `operator_inbox_poll_tool` | mcp/src/agents_remember/application/operator_inbox_tools.py:100-125 |
| Defines the function `operator_inbox_consume_tool` (lines 127-158). | `operator_inbox_consume_tool` | mcp/src/agents_remember/application/operator_inbox_tools.py:127-158 |

## Update History

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
