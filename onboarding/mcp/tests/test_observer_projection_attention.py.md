# mcp/tests/test_observer_projection_attention.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Attention priority and occurrence-scoped dismissal behavior.

## Code Commentary

### Logic

Provider-down alarms rank above the surviving quiet-session informational occurrence. A dismissal suppresses the current actionable-drift occurrence until a newer snapshot, and a stale-session occurrence until later heartbeat activity creates a newer quiet signal. These current assertions do not establish the removed blocked-ask/awaiting-developer/turn-end cases.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

Dismissal acknowledges one triggering occurrence, not every future event of the same kind. Durable timestamps determine resurfacing.

### Todos

No file-local implementation change is requested by this reconciliation.

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

No configured domain evidence applies to the file-local claims above.

### Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

- Provider-down ranks ahead of a quiet-session signal, whose lifecycle/time are asserted. [4]
- Dismiss suppresses actionable drift until newer snapshot. [2]
- Later heartbeat activity creates a newer stale-session occurrence after dismissal, not a turn-end/awaiting-developer assertion. [5]

### Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

Fixture repositories and protocol doubles do not establish a live external integration.
