# mcp/src/agents_remember/memory_quality/style/citations/structures.py

## Governing Overview

[overview](../../overview.md)

## Purpose

Structural identities for the construct an anchored range denotes.

## Code Commentary

### Logic

Module-level surface:

- `StructuralView` (class, lines 24-98) — One parsed source revision, reused for every anchor resolved inside it.
- `fingerprint` (function, lines 101-108) — Uncached convenience entry point for callers resolving one construct.
- `_span` (function, lines 111-114)
- `_tokens` (function, lines 117-126) — A syntax token stream with comments and layout absent but operators retained.
- `_digest` (function, lines 129-131)

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.

### Todos

None.

## Evidence

### Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

- Defines the class `StructuralView` (lines 24-98) — One parsed source revision, reused for every anchor resolved inside it.. [1]
- Defines the function `fingerprint` (lines 101-108) — Uncached convenience entry point for callers resolving one construct.. [2]
- Defines the function `_span` (lines 111-114). [3]
- Defines the function `_tokens` (lines 117-126) — A syntax token stream with comments and layout absent but operators retained.. [4]
- Defines the function `_digest` (lines 129-131). [5]
