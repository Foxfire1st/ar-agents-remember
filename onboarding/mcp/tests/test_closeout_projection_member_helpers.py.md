# mcp/tests/test_closeout_projection_member_helpers.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Candidate-document and semantic-topology fixtures for closeout consumers.

## Code Commentary

### Logic

Builders create a segmented predecessor/master/successor graph, a richly populated leaf document, resolved document tuples and a semantic graph index. Observational fields and task intent coexist in the candidate fixture so consumers can vary them independently.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

No test methods remain here. Building an index or sample routeReview is fixture setup, not proof of current readiness or an independent review.

### Todos

No file-local implementation change is requested by this reconciliation.

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

No configured domain evidence applies to the file-local claims above.

### Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

- Ref. [1]
- Graph. [2]
- Candidate document. [3]
- Documents. [4]
- Semantic index. [5]
- Bound sprint. [6]

### Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

Fixture repositories and protocol doubles do not establish a live external integration.
