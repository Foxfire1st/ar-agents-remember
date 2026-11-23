# mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_record_cache.py

## Governing Overview

[Lifecycle overview](overview.md)

## Purpose

Reuses parsed lifecycle journal records against the journal store's file observation.

## Code Commentary

The cache keys by journal path and matches the supplied nanosecond modification time, byte size and nanosecond change time. It holds up to 4,096 paths per owner and evicts the oldest insertion when a new path would exceed that count. Native calls share a request owner and the dashboard can reuse the process owner.

## Relationships

The journal store owns the file observation, validation and the copies at the cache boundary.

## Evidence

- Cache reads compare the saved journal observation. [1]
- Owner selection uses the current request scope when present. [2]
