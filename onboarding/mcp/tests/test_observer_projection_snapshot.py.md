# mcp/tests/test_observer_projection_snapshot.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Observer snapshot projection and persisted current-state smoke test.

## Code Commentary

### Logic

The fixture builds temporary runtime inputs and drives project-and-write end to end. The retained case requires one lifecycle in the projection and a persisted latest-state.json under the configured observer root.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

This single smoke case does not prove every historical reader/refusal or root-journal addressing edge. A written projection is derived state rather than mutation authority.

### Todos

No file-local implementation change is requested by this reconciliation.

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

No configured domain evidence applies to the file-local claims above.

### Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

- Project and write end to end. [1]

### Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

Fixture repositories and protocol doubles do not establish a live external integration.
