# mcp/tests/test_configured_contract_admission_l2.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_configured_contract_admission_l2.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-23T16:08+02:00 |
| lastVerifiedCommitHash | `1d446724d099517f6f52d596b47827ae2391a2a4` |
| lastVerifiedCommitDate | 2026-08-24T00:21:10+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

Forces configured contract admission l2 behavior at the public and durable-state boundaries.

## Code Commentary

### Logic

The principal forcing seams are `test_every_public_consumer_exhaustively_refuses_each_semantic_category`, `test_real_admission_classifies_expected_failures_and_leaves_unexpected_faults_loud`, `test_mutation_time_configured_authority_change_uses_the_same_public_projector`, `test_real_post_admission_lower_failures_share_the_public_projector`. The suite exhaustively proves the one closed admission result and projector across every public current-contract consumer, exact admitted-object reuse, mutation-time authoritative reread, and loud unexpected faults.

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
| The file defines `test_every_public_consumer_exhaustively_refuses_each_semantic_category`, `test_real_admission_classifies_expected_failures_and_leaves_unexpected_faults_loud`, `test_mutation_time_configured_authority_change_uses_the_same_public_projector`, `test_real_post_admission_lower_failures_share_the_public_projector` as its principal forcing seams. | L197-L272; L275-L322; L334-L387; L400-L476 | `mcp/tests/test_configured_contract_admission_l2.py` |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this test file.

## Update History

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: created from the accepted full L2 candidate. Verification fields remain blank until the architect-owned closeout has a real code commit to stamp.

