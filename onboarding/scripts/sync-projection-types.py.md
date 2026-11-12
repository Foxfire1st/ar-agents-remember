# scripts/sync-projection-types.py

## Governing Overview

[overview](../overview.md)

## Purpose

Generate or check the dashboard projection schema and TypeScript contract.

## Code Commentary

### Logic

Module-level surface:

- `parse_args` (function, lines 20-40)
- `check` (function, lines 43-51)
- `main` (function, lines 54-65)

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.

### Todos

None.

## Evidence

### Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

- Defines the function `parse_args` (lines 20-40). [1]
- Defines the function `check` (lines 43-51). [2]
- Defines the function `main` (lines 54-65). [3]

## PDLS Wave 005 Current Delta

The script now adds both `mcp/src` and `mcp/test_support` to its explicit import path, then imports
the projection generator from its verification owner. This preserves the repository script entry
point without shipping test-evidence machinery as product runtime code.
