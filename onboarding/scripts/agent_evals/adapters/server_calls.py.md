# scripts/agent_evals/adapters/server_calls.py

## Governing Overview

[governing overview](../overview.md)

## Purpose

Cross-checks fixture server logs against native actions and uniquely placed opaque intervals.

## Code Commentary

### Invariants And Boundaries

Dropped or unplaceable calls remain unknown. Shortened arguments and log identifiers are not expanded into invented provider calls.

Retained placement replay reads the fixtureServerCall rows already present in the frozen raw export, not the original logs. It discards derived placements and prior log-recovery events before recomputing native matches or uniquely placed opaque-interval recoveries. Raw records, their historical placement, source bindings and export digest remain unchanged; still-unplaceable calls are reported again and unrelated recording failures remain unknown.

## Evidence

- The source defines this file's responsibility and the boundaries described here. [1]
