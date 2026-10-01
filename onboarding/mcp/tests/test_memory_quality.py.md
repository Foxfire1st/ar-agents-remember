# mcp/tests/test_memory_quality.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Memory-census metadata authority, historical-row and moved-card handling, and entity-catalog alignment tests.

## Code Commentary

### Logic

The first four tests exercise the census repair boundary: a valid current sidecar mapping is accepted despite absent or stale historical metadata, a repaired current mapping is not vetoed by an old association, a removed historical sidecar remains an absent census row without a removal blocker, and a move retains both the old absent row and the new present row. The two retained tests reject a fingerprint without an inventory entity and accept exactly one fingerprint per inventory member. Alignment remains first in the before-metadata-refresh check ordering. Helpers write exact onboarding/entity fixtures and initialize clean memory repositories.

### Conventions

The retained entity assertions were present at IAS `d3610903`; the current candidate carries four census regression cases covering current metadata, historical rows, and moved old/new cards. Historical entries below record earlier test populations and do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

Current census cases distinguish current candidate metadata from historical metadata: current missing or conflicting mappings remain blockers, while historical-only associations provide removal context, remain enumerable as absent rows, and do not veto a valid current mapping or require an extra removal declaration. The ordering assertion establishes check registration, not a prohibition on authorized pre-gate memory preparation.

### Todos

No file-local implementation change is requested by this reconciliation.

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

No configured domain evidence applies to the file-local claims above.

### Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

- Current repaired metadata and historical removal behavior are covered by the census regression helper. [1]
- A repaired current mapping is accepted even when the historical card named an old source. [2]
- A removed historical card remains an absent row without a removal blocker. [3]
- A moved card retains old and new census rows with absent and present final states. [4]
- Entity catalog alignment rejects orphaned fingerprint before code rails. [5]
- Entity catalog alignment accepts one fingerprint per inventory entry. [6]

### Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

Fixture repositories and protocol doubles do not establish a live external integration.
