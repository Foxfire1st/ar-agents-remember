# scripts/agent_evals/adapters/recorder_plugin/index.server.ts

## Governing Overview

[governing overview](../../overview.md)

## Purpose

Records exact-owner native helper updates and turn-end events for a fixture host.

## Code Commentary

The recorder registers through `server.addHook` (`agent.open.before` and `agent.turn.after`). Because the turn-end hook carries an empty timeline from Paseo 0.13, it records the agent's held timeline read through `agents.ref(id).timeline.refetch` in the hook's place, each item with its row's turn id.

### Invariants And Boundaries

Readiness and recording-window markers distinguish subscription snapshots from actual events. Restarts and errors invalidate the window; plugin code alone proves no loaded recorder or captured event.

## Evidence

- The source defines this file's responsibility and the boundaries described here. [1]
