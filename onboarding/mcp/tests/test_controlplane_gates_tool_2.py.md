# mcp/tests/test_controlplane_gates_tool_2.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Gate cancellation, bounded waiting and stale-decision tests.

## Code Commentary

### Logic

Cancel removes the gate and associated inbox entries. Waiting on an open gate times out; response waiting returns a matching pending inbox entry without consuming it. An expected-gate mismatch refuses instead of deciding another lifecycle gate.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

Receiving a response and consuming it are separate operations. Stale identity cannot be substituted with the newest available gate.

### Todos

No file-local implementation change is requested by this reconciliation.

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

No configured domain evidence applies to the file-local claims above.

### Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

- Cancel deletes gate and pending inbox entries. [1]
- Wait times out while open. [2]
- Response wait returns matching inbox entry without consuming. [3]
- Decide for lifecycle rejects stale expected gate. [4]

### Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

Fixture repositories and protocol doubles do not establish a live external integration.
