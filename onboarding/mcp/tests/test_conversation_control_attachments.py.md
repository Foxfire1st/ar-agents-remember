# mcp/tests/test_conversation_control_attachments.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Attachment limits, one-use identity, recovery and unknown-outcome retention.

## Code Commentary

### Logic

Actual control composition rejects invalid MIME/count/bytes/kind, binds the receipt to one submitted request, and rejects tampering before dispatch. Exact replay writes once; changed content conflicts. Withdrawal returns a recoverable asset whose rebind is idempotent for one new request and cannot be exchanged twice; native resubmission carries the rebound identity.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

Unknown outcomes preserve spool bytes and remain unknown after reconcile. The reduced source does not retain cleanup-on-expiry or policy/telemetry matrices.

### Todos

No file-local implementation change is requested by this reconciliation.

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

No configured domain evidence applies to the file-local claims above.

### Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

- Mime count byte and kind limits are typed. [1]
- Submit carries refs and consumes one use. [2]
- Tampered asset block is rejected before dispatch. [3]
- Double use of one asset is typed. [4]
- Withdraw marks recoverable and rebind exchanges one use. [5]
- Unknown outcome is retained and never cleaned. [6]

### Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

Fixture repositories and protocol doubles do not establish a live external integration.
