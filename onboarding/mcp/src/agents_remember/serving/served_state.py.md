# mcp/src/agents_remember/serving/served_state.py

## Governing Overview

[overview](overview.md)

## Purpose

The served workspace state extends the observer projection with servingBuild, the serving process id, the optional watcherHealth reading, the checkout binding and the build-currentness reading. It carries no notifier heartbeat, supervisor alias or terminal observer-health tail.

## Code Commentary

ServedWorkspaceProjection declares optional servingBuild, watcherHealth, checkoutBinding, buildCurrentness and servingProcessId; SERVED_TAIL_FIELDS names exactly those five extensions. served_state_tail omits missing build facts, dumps a present build with exclude_none together with the answering process's own id, and adds a supplied build-currentness reading. Routes merge the tail onto a copy of the per-instance projection memo; persisted observer state stays in its own schema, and only `/api/state` responses and SSE snapshots receive the tail. Content-revision/304 gating is distinct from response assembly. The process id is what the dashboard supervisor compares with the socket owner, so a state answer binds its build to the listening process.

Watcher health is typed and omissive: an unconfigured watcher omits the entire field, a running watcher omits downSince, and an outage carries its recorded downSince. The assembly validates the supplied watcher reading and omits an invalid one.

## Evidence boundary

Current source interpretation only; no fresh execution or grade.

## Source-bound reference inputs

- Optional servingBuild, watcherHealth, checkoutBinding, buildCurrentness and servingProcessId extend the observer projection. [1]

- Absent build or watcher facts are omitted; a supplied watcher reading is validated and an invalid reading is omitted. [2]

- The current tail vocabulary is exactly servingBuild, watcherHealth, checkoutBinding, buildCurrentness and servingProcessId. [3]
- A present build adds the answering process id, and a supplied currentness reading is dumped into the tail. [4]
- The dashboard supervisor refuses an answer whose process id differs from the socket owner. [5]
