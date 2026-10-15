# mcp/src/agents_remember/serving/served_state.py

## Governing Overview

[serving overview](overview.md)

## Purpose

The served workspace state extends the observer projection with servingBuild and the optional L81 watcherHealth reading. No notifier heartbeat, supervisor alias or terminal observer-health tail remains.

## Code Commentary

ServedWorkspaceProjection declares optional servingBuild and watcherHealth; SERVED_TAIL_FIELDS names exactly those two extensions. served_state_tail omits missing build facts and dumps a present build with exclude_none. Routes merge the tail onto a copy of the per-instance projection memo; persisted observer state stays in its own schema, and only SSE snapshots receive the tail. Content-revision/304 gating is distinct from response assembly. Removed matrix/health tests are not current conformance or execution evidence.

Watcher health is typed and omissive: an unconfigured watcher omits the entire field, a running watcher omits downSince, and an outage carries its recorded downSince. The assembly validates the supplied watcher reading and omits an invalid one. Notifier heartbeat, supervisor aliases and terminal-observer health remain removed.

## Evidence boundary

Current source interpretation only; no fresh execution or grade.

## Source-bound reference inputs

- Optional servingBuild and watcherHealth extend the observer projection; notifier, supervisor and terminal-health tails remain removed. [1]
- Absent build or watcher facts are omitted; a supplied watcher reading is validated and an invalid reading is omitted. [2]
- The current tail vocabulary is exactly servingBuild and watcherHealth. [3]
