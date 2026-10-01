# mcp/src/agents_remember/observer/store.py

## Governing Overview

[observer overview](overview.md)

## Purpose

`store.py` is the append-only event store: it resolves a given event's log path
and appends it as one JSONL line.

## Code Commentary

### 260707-HFX2-L13 Workspace Cursor And Heartbeat Storage

Workspace appends now take a POSIX `flock` on `workspace/events.lock`, the same cross-process lock
used by physical compaction and live reads. `events.cursor.json` stores the non-negative virtual
`baseOffset`, written atomically, and `workspace_logical_size` exposes virtual EOF. This lock is
necessary rather than generic defensive code: serving and MCP processes both append while the live
compactor replaces the file, so an unlocked rewrite can lose writes or tear cursor state.

Lifecycle heartbeats no longer append to `events.jsonl`. They atomically overwrite one
`heartbeat.json` sidecar per lifecycle; `read()` merges the newest sidecar event into the validated
log, while `read_log()` and `read_heartbeat()` expose the two storage layers to the projection cache.
Real lifecycle and workspace events retain their prior JSONL routing.

### 260707-HFX2-L12 CS-6 Update

`EventStore.read()` now skips corrupt, legacy, or torn JSONL lines. That keeps one bad lifecycle event row from freezing the projection tick fleet-wide while preserving append-only write semantics for valid rows.

`EventStore(observer_root)` holds the `logs/observer/` root. `log_path(lifecycle_id)`
routes to `lifecycles/<id>/events.jsonl` when a lifecycle id is present, else the
shared `workspace/events.jsonl`. `append(event)` creates parent dirs on first
write and appends `event.model_dump_json(by_alias=True, exclude_none=True)`.
`read(lifecycle_id)` validates a log back into `Event` objects — the minimal,
validated read that proves the write format round-trips (the projection layer
will read more richly).

## Invariants And Boundaries

- **Single writer per lifecycle file.** Exclusive adoption (one live session per
  lifecycle) means appends need no cross-process lock. The only events written to
  a lifecycle file are written by its live owner; a dormant fleeting lifecycle
  past TTL is *pruned* (directory deletion), never terminated by a non-owner
  append — so the single-writer invariant holds without coordination.
- Append-only: history is never rewritten in place (corrections are later
  events, by design).

## Evidence

### Repo-Internal References

- The event envelope serialized and validated by the observer model. [1]
- The store layout, retention tiers, and TTL prune rule. [2]
