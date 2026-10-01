# mcp/tests/test_harness_submission_authority.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Bridge-owned submission ordering, withdrawal and idempotency races.

## Code Commentary

### Logic

A slow operation leaves status and queued withdrawal responsive. Dispatch claim and withdrawal have an explicit winner; withdrawal during preflight prevents a native write. Early completion is buffered until the exact head can release. Same IDs replay but changed source/payload conflict. Certified pre-send busy requeues locally; epoch/source scope refuse and a pinned full ledger declines new room.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

No vendor queue or resend substitutes for bridge authority. Capacity refusal preserves records that cannot safely be dropped.

### Todos

No file-local implementation change is requested by this reconciliation.

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

No configured domain evidence applies to the file-local claims above.

### Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

- Slow active operation does not block status or queued withdrawal. [1]
- Dispatch claim wins atomic withdrawal race. [2]
- Withdrawal during preflight wins before dispatch claim. [3]
- Completion before receipt is buffered and releases exact head. [4]
- Same id is idempotent but source or payload change conflicts. [5]
- Certified pre send busy requeues without vendor queue or resend. [6]
- Epoch and public source scope fail closed. [7]
- A ledger with nothing droppable refuses room rather than forgetting a row. [8]

### Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

Fixture repositories and protocol doubles do not establish a live external integration.
