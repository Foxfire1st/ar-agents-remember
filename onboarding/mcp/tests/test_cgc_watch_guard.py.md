# mcp/tests/test_cgc_watch_guard.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

CGC watcher guard behavior through a stub Redis module.

## Code Commentary

### Logic

The host loader injects Redis exception stubs before importing the runner asset. Retained cases bound readiness waiting, preserve an already indexed graph, and verify main reaches the cgc watch exec boundary after graph checks.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

No live Redis or CGC backend is started. The retained graph case proves preservation, not every historical poisoned-graph deletion path.

### Todos

No file-local implementation change is requested by this reconciliation.

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

No configured domain evidence applies to the file-local claims above.

### Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

- Wait for ready gives up after deadline. [1]
- Clear poisoned graph keeps indexed graph. [2]
- Main checks graph then execs cgc. [3]

### Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

Fixture repositories and protocol doubles do not establish a live external integration.
