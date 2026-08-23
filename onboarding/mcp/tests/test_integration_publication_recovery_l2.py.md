# mcp/tests/test_integration_publication_recovery_l2.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_integration_publication_recovery_l2.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-23T16:08+02:00 |
| lastVerifiedCommitHash | `1d446724d099517f6f52d596b47827ae2391a2a4` |
| lastVerifiedCommitDate | 2026-08-24T00:21:10+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

Forces integration publication recovery l2 behavior at the public and durable-state boundaries.

## Code Commentary

### Logic

The principal forcing seams are `test_queue_deleted_after_claim_before_refs_recovers_same_generation`, `test_surviving_queue_receipt_contains_projection_identity_only`, `test_journal_claim_intent_survives_queue_invalidation_and_governed_task_edit`, `test_queue_deleted_between_code_and_memory_refs_retains_torn_pair_and_recovers`. The suite forces claim transfer, door authority, exact protected-ref classification, publication recovery, and same-generation reconciliation without moving lifecycle evidence into the queue.

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
| The file defines `test_queue_deleted_after_claim_before_refs_recovers_same_generation`, `test_surviving_queue_receipt_contains_projection_identity_only`, `test_journal_claim_intent_survives_queue_invalidation_and_governed_task_edit`, `test_queue_deleted_between_code_and_memory_refs_retains_torn_pair_and_recovers` as its principal forcing seams. | L51-L101; L103-L160; L162-L243; L245-L299 | `mcp/tests/test_integration_publication_recovery_l2.py` |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this test file.

## Update History

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: created from the accepted full L2 candidate. Verification fields remain blank until the architect-owned closeout has a real code commit to stamp.

