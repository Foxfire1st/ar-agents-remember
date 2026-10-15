# mcp/src/agents_remember/serving/projections/snapshots_impl/_lifecycle_logs.py

## Governing Overview

[governing overview](../overview.md)

## Purpose

Share stat-gated parsed lifecycle-event logs between full and path-directed projection reads without a module cycle. Unchanged identities reuse parsed events; enumerating reads prune to the live set, while directed reads touch only named logs.

## Code Commentary

Share stat-gated parsed lifecycle-event logs between full and path-directed projection reads without a module cycle. Unchanged identities reuse parsed events; enumerating reads prune to the live set, while directed reads touch only named logs.

## Boundaries

Local implementation and executable evidence do not replace requirement authority or the owning transaction. Retained source semantics and explicit unavailable/failure states remain binding.

## Evidence

- Share stat-gated parsed lifecycle-event logs between full and path-directed projection reads without a module cycle. Unchanged identities reuse parsed events; enumerating reads prune to the live set, while directed reads touch only named logs. [1]
