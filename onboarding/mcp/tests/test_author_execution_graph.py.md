# mcp/tests/test_author_execution_graph.py

## Governing Overview

[overview](overview.md)

## Purpose

Incremental execution-graph authoring through the public task-document operation.

## Code Commentary

### Logic

The retained successful batch replaces a master node with two segments and adds a provenance-bearing edge. Dry run preserves the entire document snapshot; apply persists typed nodes, derived waves and rendered navigation. A duplicate-node batch refuses atomically without changing any document. The fixture's judgment row is authored by the Architect by default; a row authored by the Orchestrator authors the graph the same way, and any other or retired author (`worker`, `manager`, `reviewer`, `curator`, `investigator`, `bootstrap`, `designer`, `strategist`) is refused with `task-execution-graph-judgment-author-refused` on dry run and apply alike, leaving the snapshot unchanged.

### Conventions

Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

Disposable coordination roots isolate publication. Do not attribute graph bootstrap or an edge-error matrix to these cases; their only role check is the judgment-author admission.

### Todos

No file-local implementation change is requested by this reconciliation.

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

No configured domain evidence applies to the file-local claims above.

### Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

- Dry run preserves the task-document snapshot; apply publishes the graph changes. This assertion is not a universal no-I/O claim about enclosing registered-call log/river records. [1]

- Batch atomicity leaves everything untouched on failure. [2]

- An Orchestrator-authored ruling still authors the graph. [3]
- Every other or retired ruling author is refused without writes, on dry run and apply. [4]


### Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

Fixture repositories and protocol doubles do not establish a live external integration.
