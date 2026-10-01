# mcp/src/agents_remember/providers/watcher_service.py

## Governing Overview

[overview](../../../overview.md)

## Purpose

Configured provider-watcher lifecycle service shared by upper performers.

## Code Commentary

### Logic

Module-level surface:

- `run_configured_watchers` (function, lines 16-43) — Run one watcher action against temporary settings derived from live config.

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.

### Todos

None.

## Evidence

### Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

- Defines the function `run_configured_watchers` (lines 16-43) — Run one watcher action against temporary settings derived from live config.. [1]
