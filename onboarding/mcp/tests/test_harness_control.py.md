# mcp/tests/test_harness_control.py

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Reusable deterministic fake adapters and private IPC server seams for harness-control checks.

## Code Commentary

### Logic

The fake records launches, submissions, setters, responses and reconciliation requests. It advertises an intentionally empty capability snapshot, can emit snapshots/events, and settles an answered multiplexed interaction from the pending tuple. Completion events carry the original submission operation.

Blocking submit and setter adapters use explicit asyncio events to hold and release work. The observed server exposes connection completion through a finally-set event. The dropped-response server dispatches the first actual submit, closes its socket before returning the receipt, and delegates subsequent connections normally. Fixed identity, launch and catalog builders keep exact-session inputs consistent.

### Invariants And Boundaries

This retained module defines support objects and builders; it contains no collected test functions. Its former family-wide coverage narrative is historical. Helper availability is not evidence that a removed scenario still runs.

## Evidence

### Repo-Internal References

- The fake supplies cached state, recording and deterministic events. [1]
- Explicit submission hold/release and injected error. [2]
- Explicit setter hold/release returns queued acceptance. [3]
- Connection completion is observable even when dispatch fails. [4]
- A real first dispatch loses only its outer response. [5]
- The catalog builder derives identity fields from the supplied control identity. [6]

### Docs References

No external documentation is needed for these source-owned helper facts.

### Cross-Repo References

No separate cross-repository authority is established by this helper module.
