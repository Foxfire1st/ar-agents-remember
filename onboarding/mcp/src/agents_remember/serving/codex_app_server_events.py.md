# mcp/src/agents_remember/serving/codex_app_server_events.py

## Governing Overview

[overview](overview.md)

## Purpose

The Codex adapter's bounded event fan-out and its load-shedding policy.

## Code Commentary

### Logic

Module-level surface:

- `CodexEventQueue` (class, lines 24-118) — Bounded queue with honest load-shedding: never raises, never silently drops.

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.

### Todos

None.

## Evidence

### Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

- Defines the class `CodexEventQueue` (lines 24-118) — Bounded queue with honest load-shedding: never raises, never silently drops.. [1]
