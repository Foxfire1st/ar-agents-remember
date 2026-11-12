# mcp/src/agents_remember/memory_quality/style/document_shape/diff_markers.py

## Governing Overview

[overview](../../overview.md)

## Purpose

Report diff prefixes left at column zero in memory Markdown.

## Code Commentary

### Logic

Module-level surface:

- `check_onboarding_root` (function, lines 30-38)
- `check_file` (function, lines 41-48)
- `line_finding` (function, lines 51-80)
- `marker_finding` (function, lines 83-98)

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.

### Todos

None.

## Evidence

### Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

- Defines the function `check_onboarding_root` (lines 30-38). [1]
- Defines the function `check_file` (lines 41-48). [2]
- Defines the function `line_finding` (lines 51-80). [3]
- Defines the function `marker_finding` (lines 83-98). [4]
