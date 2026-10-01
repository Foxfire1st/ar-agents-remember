# mcp/tests/test_dispatch_brief.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Durable initial dispatch-brief delivery and exact-target retry.

## Code Commentary

### Logic

Ready delivery creates one inbox-rooted landed row and meets the briefed-by expectation through the adapter. Rejected or not-ready delivery preserves one pending row. Ambiguous retry reconciles retained adapter truth without another submit; an exact missing agent target never redirects to a matching lifecycle.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

No raw paste fallback is allowed. A durable row ID is not embedded as prompt content, and unresolved acceptance must remain unconfirmed.

### Todos

No file-local implementation change is requested by this reconciliation.

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

No configured domain evidence applies to the file-local claims above.

### Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

- Ready dispatch is inbox rooted lands and starts expectation clocks. [1]
- Rejected adapter receipt keeps same row pending. [2]
- Ambiguous redelivery reconciles without resubmitting. [3]
- Not ready queues one durable dispatch row for plane retry. [4]
- Exact agent target never falls back to matching lifecycle. [5]

### Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

Fixture repositories and protocol doubles do not establish a live external integration.
