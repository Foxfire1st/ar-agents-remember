# mcp/src/agents_remember/controlplane/stamps.py

## Governing Overview

[overview](overview.md)

## Purpose

Aging an ISO-8601 stamp against a clock -- the primitive the record stores share.

## Code Commentary

### Logic

Module-level surface:

- `age_seconds` (function, lines 22-35) — Seconds between an ISO-8601 ``stamp`` and ``now``; ``None`` when unparseable.

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.

### Todos

None.

## Evidence

### Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

- Defines the function `age_seconds` (lines 22-35) — Seconds between an ISO-8601 ``stamp`` and ``now``; ``None`` when unparseable.. [1]
