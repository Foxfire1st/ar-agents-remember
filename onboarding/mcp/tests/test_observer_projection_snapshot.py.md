# mcp/tests/test_observer_projection_snapshot.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Observer snapshot projection and persisted current-state smoke test.

## Code Commentary

### Logic

The fixture builds temporary runtime inputs and drives project-and-write end to end. It requires no lifecycles root and a persisted latest-state.json under the configured observer root. Pending enclosures count as admitted/active runtime groups, while reopened enclosures do not. Changing only drift-snapshot age emits no analytics delta; changing the snapshot actionable count from zero to two emits one analytics event.

### Conventions

This card describes the current retained assertions; the earlier IAS `d3610903` source identity is historical. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

These focused cases do not prove every historical reader/refusal or root-journal addressing edge. A written projection is derived state rather than mutation authority.

### Todos

No file-local implementation change is requested by this reconciliation.

The additional predicates are source assertions over real contract files and constructed analytics projections; they do not turn a written projection into mutation authority.

## Evidence

- Pending but not reopened enclosures admit runtime worktree groups. [2]


### Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

No configured domain evidence applies to the file-local claims above.

### Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.


- Project and write end to end. [1]


### Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

Fixture repositories and protocol doubles do not establish a live external integration.

- The age-only comparison uses drift snapshots; changing actionableCount emits an analytics event. [3]
