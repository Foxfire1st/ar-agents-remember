# mcp/src/agents_remember/serving/codex_app_server_threads.py

## Governing Overview

[overview](overview.md)

## Purpose

Multiplexed thread demux for one Codex app-server connection.

## Code Commentary

### Logic

Module-level surface:

- `CodexThreadState` (class, lines 32-66) — Per-thread demux state on one multiplexed app-server connection.
- `CodexThreadRegistry` (class, lines 69-300) — The threads on one connection, their agent identities, and the item->thread index.

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.

### Todos

None.

## Evidence

### Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

- Defines the class `CodexThreadState` (lines 32-66) — Per-thread demux state on one multiplexed app-server connection.. [1]
- Defines the class `CodexThreadRegistry` (lines 69-300) — The threads on one connection, their agent identities, and the item->thread index.. [2]
