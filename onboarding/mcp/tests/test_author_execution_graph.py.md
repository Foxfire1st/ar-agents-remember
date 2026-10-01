# mcp/tests/test_author_execution_graph.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Incremental execution-graph authoring through the public task-document operation.

## Code Commentary

### Logic

The retained successful batch replaces a master node with two segments and adds a provenance-bearing edge. Dry run preserves the entire document snapshot; apply persists typed nodes, derived waves and rendered navigation. A duplicate-node batch refuses atomically without changing any document.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

Disposable coordination roots isolate publication. Do not attribute the removed graph-bootstrap, role-validation or edge-error matrix to these two cases.

### Todos

No file-local implementation change is requested by this reconciliation.

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

No configured domain evidence applies to the file-local claims above.

### Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

- Dry run previews and writes nothing then apply publishes. [1]
- Batch atomicity leaves everything untouched on failure. [2]

### Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

Fixture repositories and protocol doubles do not establish a live external integration.
