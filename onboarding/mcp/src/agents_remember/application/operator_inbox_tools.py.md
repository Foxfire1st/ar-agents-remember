# mcp/src/agents_remember/application/operator_inbox_tools.py

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

## Evidence

### Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

- Defines the function `_result` (lines 31-33) — Return the raw use-case result for the MCP adapter to finalize.. [1]
- Defines the function `_store` (lines 40-41). [2]
- Defines the function `_entry_payload` (lines 44-45). [3]
- Defines the function `operator_inbox_post_tool` (lines 48-68). [4]
- Defines the function `post_operator_inbox` (lines 71-98) — Compose flat transport fields into one operator-inbox post use case.. [5]
- Defines the function `operator_inbox_poll_tool` (lines 101-124). [6]
- Defines the function `operator_inbox_consume_tool` (lines 127-158). [7]
