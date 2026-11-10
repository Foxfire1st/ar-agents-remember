# mcp/src/agents_remember/models/tools/tool_response.py

## Governing Overview

[overview](../overview.md)

## Purpose

Pure wire-model validation and token finalization for tool-shaped responses.

## Code Commentary

### Logic

Module-level surface:

- `finalize_tool_response` (function, lines 15-31) — Validate one declared response, apply optional caller enrichment, and count tokens. It validates through the tool's `TOOL_RESPONSE_MODELS` entry, except that a payload whose `code` is `server-build-stale` validates through `models.base.StaleBuildRefusalResponse`, so the shared stale-build refusal needs no writer-specific success fields.

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.

### Todos

None.

## Evidence

### Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

- Defines the function `finalize_tool_response`, which validates a declared response (or the stale-build refusal), applies optional caller enrichment and counts tokens. [1]
