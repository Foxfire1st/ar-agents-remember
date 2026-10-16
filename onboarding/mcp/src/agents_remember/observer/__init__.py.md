# mcp/src/agents_remember/observer/__init__.py

## Governing Overview

[overview.md](overview.md)

## Purpose

The observer facade exports workspace events, schema and pure assembly, not ambient/session state or served-onboarding dedup.

## Code Commentary

The explicit `__all__` exports Event/envelope/actor/trust/time, EventStore, new_ulid, workspace/provider/enclosure/task/analytical schemas, project_workspace, enclosure_actions, build_analytics, staleness_histogram and observer_root. Heavy I/O readers stay direct imports. No ambient state, heartbeat/TTL constants or served ledger is exported; landing operation models retain their independent meaning.

## Evidence

- Explicit facade exports workspace schema, event storage and pure assembly only. [9]
