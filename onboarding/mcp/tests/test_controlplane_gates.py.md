# test_controlplane_gates.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Gate-record snapshot purity, durable folding and shared tool fixture.

## Code Commentary

### Logic

create_gate returns an open snapshot; decide_gate preserves its ID and attributes the new decision without mutating the original. Appending both snapshots retains history while current folds last-wins. GateToolTests supplies temporary stores and a creation helper to the retained tool suites.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

This file no longer contains the historical closeout-enforcement matrix. Store snapshots and fixture gate creation do not grant closeout authority.

### Todos

No file-local implementation change is requested by this reconciliation.

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

No configured domain evidence applies to the file-local claims above.

### Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

- Create and decide are pure snapshots. [1]
- Append keeps history and current folds last wins. [2]

### Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

Fixture repositories and protocol doubles do not establish a live external integration.
