# mcp/tests/test_harness_control_claude_stream_2.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Claude model/effort echo and ambiguous-delivery recovery.

## Code Commentary

### Logic

Model and effort setters require correlated terminal echoes and respect the selected model menu. Timed-out setter replay is neutralized before a clean retry. Disconnect stays unknown without resend; later structured history may reconcile accepted delivery. Nonzero exit fails control, and forced stop reclaims a reader blocked by a full event queue.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

Queued or unknown is not effective selection. Late transport evidence must reconcile the original operation rather than submit it again.

### Todos

No file-local implementation change is requested by this reconciliation.

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

No configured domain evidence applies to the file-local claims above.

### Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

- Model and effort set require terminal echo and update model gate. [1]
- Set timeout neutralizes late replay before a clean retry. [2]
- Disconnect reconciliation stays unknown and never resends. [3]
- Late replay reconciles unknown from structured history without resend. [4]
- Nonzero process exit maps to failed. [5]
- Forced stop reclaims a reader blocked by full event queue. [6]

### Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

Fixture repositories and protocol doubles do not establish a live external integration.
