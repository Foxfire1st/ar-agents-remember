# mcp/src/agents_remember/models/tools/tool_response.py

## Governing Overview

[overview](../overview.md)

## Purpose

Pure wire-model validation and token finalization for tool-shaped responses.

## Code Commentary

### Logic

Module-level surface:

- `finalize_tool_response` (function, lines 15-26) — Validate one declared response, apply optional caller enrichment, and count tokens.

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.

### Todos

None.

## Evidence

### Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

- Defines the function `finalize_tool_response` (lines 15-26) — Validate one declared response, apply optional caller enrichment, and count tokens.. [1]
