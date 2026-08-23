# mcp/tests/test_integration_ref_controls_l2.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_integration_ref_controls_l2.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-23T16:08+02:00 |
| lastVerifiedCommitHash | `1d446724d099517f6f52d596b47827ae2391a2a4` |
| lastVerifiedCommitDate | 2026-08-24T00:21:10+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

Forces integration ref controls l2 behavior at the public and durable-state boundaries.

## Code Commentary

### Logic

The principal forcing seams are `test_integrate_ref_movement_requires_same_generation_recover`, `test_third_protected_ref_status_and_public_handler_require_developer_decision`, `test_missing_or_unreadable_protected_ref_is_one_public_decision`. The suite forces claim transfer, door authority, exact protected-ref classification, publication recovery, and same-generation reconciliation without moving lifecycle evidence into the queue.

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

| Finding | Citations | Source Path |
| --- | --- | --- |
| The file defines `test_integrate_ref_movement_requires_same_generation_recover`, `test_third_protected_ref_status_and_public_handler_require_developer_decision`, `test_missing_or_unreadable_protected_ref_is_one_public_decision` as its principal forcing seams. | L70-L91; L94-L198; L210-L318 | `mcp/tests/test_integration_ref_controls_l2.py` |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this test file.

## Update History

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: created from the accepted full L2 candidate. Verification fields remain blank until the architect-owned closeout has a real code commit to stamp.

