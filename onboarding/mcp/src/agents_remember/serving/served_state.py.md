# mcp/src/agents_remember/serving/served_state.py

## Governing Overview

[serving overview](overview.md)

## Purpose

The served workspace state extends the observer projection with servingBuild only. No notifier heartbeat, supervisor alias or terminal observer-health tail remains.

## Code Commentary

ServedWorkspaceProjection makes servingBuild optional; SERVED_TAIL_FIELDS names exactly that extension. served_state_tail omits missing build facts and dumps a present build with exclude_none. Routes merge the tail onto a copy of the per-instance projection memo; persisted observer state stays in its own schema, and only SSE snapshots receive the tail. Content-revision/304 gating is distinct from response assembly. Removed matrix/health tests are not current conformance or execution evidence.

## Evidence boundary

Current source interpretation only; no fresh execution or grade.

## Source-bound reference inputs

- [1]
- [2]
- [3]
