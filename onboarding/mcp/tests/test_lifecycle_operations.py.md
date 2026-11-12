# mcp/tests/test_lifecycle_operations.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Asynchronous lifecycle operation launch and cancellation authority.

## Code Commentary

### Logic

Starting returns queued immediately and an exact duplicate observes one launch. The cross-kind/terminal contract lease was removed with the door-operation-journal lock plane, so no lease exclusion remains. Before the boundary, cancellation proves worker exit before releasing its authority. After commit proof, cancellation refuses with immutable-output recovery required and keeps approval claimed.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

Public projection omits worker internals. An irreversible result cannot make spent approval reusable or turn cancellation into rollback.

### Todos

No file-local implementation change is requested by this reconciliation.

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

No configured domain evidence applies to the file-local claims above.

### Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

- Start returns immediately and duplicate observes one launch. [1]
- The cross-kind/terminal contract-lifecycle lease was removed with the door-operation-journal lock plane, so no lease exclusion is asserted here any more; the retained behaviour is start/observe dedup and the two cancellation boundaries. [2]
- Cancel before boundary proves exit before releasing worker authority. [3]
- Cancel after boundary refuses without making approval reusable. [4]

### Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

Fixture repositories and protocol doubles do not establish a live external integration.
