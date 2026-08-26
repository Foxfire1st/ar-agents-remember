# mcp/tests/test_lifecycle_operation_request_validation_l2.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_lifecycle_operation_request_validation_l2.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-23T16:08+02:00 |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d` |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

Forces lifecycle operation request validation l2 behavior at the public and durable-state boundaries.

## Code Commentary

### Logic

The principal forcing seams are `test_public_operation_control_payload_refuses_invalid_request_before_authority`. The suite forces task-addressed legal controls, immutable same-generation retry/recovery, evidence-safe cancellation, write-ahead successor revision, door publication, concurrency, and executable refusal paths.

### Conventions

Tests address operations by task/contract plus kind and generation, assert durable evidence and public legal controls, and compare state across failure cuts. Helpers remain test-only and invoke the same public/domain seams as production.

### Invariants And Boundaries

- A passing assertion must prove the advertised action executes or terminates safely; payload shape alone is insufficient.
- Queue projection is never accepted as lifecycle evidence, and private operation identifiers do not cross the public test boundary.
- Failure-path assertions check non-mutation or exact same-generation recovery, not merely an exception string.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies to these repository-internal forcing tests.

## Repo-Internal References

The test source is the direct evidence for the regression contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| The file defines `test_public_operation_control_payload_refuses_invalid_request_before_authority` as its principal forcing seams. | `test_public_operation_control_payload_refuses_invalid_request_before_authority` | mcp/tests/test_lifecycle_operation_request_validation_l2.py:23-90 |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this test file.

## 2026-08-26 Common Response Envelope

Invalid lifecycle-control requests still refuse before authority and omit private operation
coordinates, but the public payload is now checked as a superset of the domain refusal. It must
also carry `developerDecisionRequired=false` plus exact tokenizer/token-count metadata emitted by
the common response finalizer.

## Update History

- 2026-08-26T10:44:52+02:00 — Reconciled invalid-request assertions with the common finalized response envelope and token metadata.
- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: created from the accepted full L2 candidate. Verification fields remain blank until the architect-owned closeout has a real code commit to stamp.

