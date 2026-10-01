# mcp/tests/test_controlplane_store_durability.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Control-plane append/compaction durability and gate torn-line policy.

## Code Commentary

### Logic

A deterministic multi-process race runs each retained store case and requires one attempted append, zero lost records and no stragglers. Gate enforcement reads reject a torn JSONL row; dashboard projection still returns the intact gate beside it.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

The measurement helper owns the mechanism and this suite asserts its outcome. The reduced source does not retain sustained stress, unlink races or historical-baseline failure demonstrations.

### Todos

No file-local implementation change is requested by this reconciliation.

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

No configured domain evidence applies to the file-local claims above.

### Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

- No record is lost when an append races a compaction. [1]
- Gate enforcement fold refuses a torn line. [2]
- Gate projection fold degrades instead of crashing. [3]

### Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

Fixture repositories and protocol doubles do not establish a live external integration.
