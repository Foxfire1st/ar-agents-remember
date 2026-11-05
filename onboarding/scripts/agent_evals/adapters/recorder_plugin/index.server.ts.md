# scripts/agent_evals/adapters/recorder_plugin/index.server.ts

## Governing Overview

[governing overview](../../overview.md)

## Purpose

Records exact-owner native helper updates and turn-end events for a fixture host.

## Code Commentary

### Invariants And Boundaries

Readiness and recording-window markers distinguish subscription snapshots from actual events. Restarts and errors invalidate the window; plugin code alone proves no loaded recorder or captured event.

## Evidence

- The source defines this file's responsibility and the boundaries described here. [1]
