# mcp/tests/test_pi_rpc_process.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Actual Pi subprocess transport correlation and cancellation.

## Code Commentary

### Logic

A deterministic child replies to a correlated request, streams an event and exposes stderr before clean stop. EOF during an outstanding request is ambiguous with its original correlation ID. Cancellation discards a late response so the next request/reader can complete normally.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

The process boundary is real but the child is a fixture, not an installed Pi model session. Ambiguous receipt must not be reclassified as never sent.

### Todos

No file-local implementation change is requested by this reconciliation.

The cancellation-correlation test waits for the exact first request ID to enter the transport's pending set before cancellation. This establishes request admission directly while preserving late-response and successor-correlation assertions.

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

No configured domain evidence applies to the file-local claims above.

### Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

- Correlates response streams event and stops cleanly. [1]
- Eof during correlated request is ambiguous. [2]
- Cancelled request ignores late response and next reader survives. [3]

### Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

Fixture repositories and protocol doubles do not establish a live external integration.

- The operation opportunity precedes the retained assertion. [4]
