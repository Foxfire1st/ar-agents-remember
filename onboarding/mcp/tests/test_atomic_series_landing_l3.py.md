# mcp/tests/test_atomic_series_landing_l3.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Atomic landing exclusion at the declared-parent boundary.

## Code Commentary

### Logic

A leaf with its exact declared atomic parent may land at the same target. Removing that parent relationship leaves a live unrelated same-target contract and requires AtomicLandingBlocked with live-nonterminal state.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

The fixture uses contract/ref authority; absence of a relationship cannot be treated as permission to share the target.

### Todos

No file-local implementation change is requested by this reconciliation.

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

No configured domain evidence applies to the file-local claims above.

### Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

- Exact declared parent same target permits leaf landing. [1]
- Live nonterminal unrelated same target contract blocks landing. [2]

### Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

Fixture repositories and protocol doubles do not establish a live external integration.
