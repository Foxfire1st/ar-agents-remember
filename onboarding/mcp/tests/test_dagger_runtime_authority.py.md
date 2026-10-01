# mcp/tests/test_dagger_runtime_authority.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Shared Dagger authority snapshot and exact-owner release tests.

## Code Commentary

### Logic

Repeated admission of one declared shared engine/store yields the same snapshot digest and bound environment. A changed inspected source changes identity. Release rejects missing, foreign or stale owners while preserving the valid active owner census.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

No Dagger commands run in these unit fixtures. Historical declaration, transition and crash-reconciliation matrices are not all retained in this file.

### Todos

No file-local implementation change is requested by this reconciliation.

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

No configured domain evidence applies to the file-local claims above.

### Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

- Admits one shared authority and binds a deterministic snapshot. [1]
- Release only the exact owner and reject stale or foreign owners. [2]

### Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

Fixture repositories and protocol doubles do not establish a live external integration.
