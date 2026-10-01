# mcp/tests/test_conversation_control_api.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Conversation HTTP interrupt and attachment lifecycle integration.

## Code Commentary

### Logic

A real HTTP/bridge/IPC fixture drives interrupt acceptance, pending settlement, idempotent replay and final interrupted status with one native write. Remote authorization refuses with typed 403. Attachment staging, submit, status and reconcile preserve receipt metadata and missing requests return 404.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

The adapter is a harness-edge double. No retained source-scan or complete policy/telemetry response matrix is asserted by these three cases.

### Todos

No file-local implementation change is requested by this reconciliation.

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

No configured domain evidence applies to the file-local claims above.

### Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

- Interrupt ack settle replay and single write. [1]
- Remote peer fails closed typed 403. [2]
- Attachment stage submit status reconcile. [3]

### Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

Fixture repositories and protocol doubles do not establish a live external integration.
