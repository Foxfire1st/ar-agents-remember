# mcp/tests/test_lifecycle_enclosure_adoption_l2.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_lifecycle_enclosure_adoption_l2.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-23T16:08+02:00 |
| lastVerifiedCommitHash | `1d446724d099517f6f52d596b47827ae2391a2a4` |
| lastVerifiedCommitDate | 2026-08-24T00:21:10+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

Forces lifecycle enclosure adoption l2 behavior at the public and durable-state boundaries.

## Code Commentary

### Logic

The principal forcing seams are `test_adoption_and_schema_migration_execute_in_either_order`, `test_adoption_binds_exact_preview_and_refuses_changed_bytes_without_publication`, `test_lost_response_and_idempotent_replay_converge_to_one_receipt`, `test_adoption_conflict_refuses_before_locator_or_manifest_publication`. The suite forces locator and immutable root-manifest publication, confinement and digest contradictions, idempotent pre-adoption enclosure adoption, and exact root-journal recovery after task-contract loss.

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
| The file defines `test_adoption_and_schema_migration_execute_in_either_order`, `test_adoption_binds_exact_preview_and_refuses_changed_bytes_without_publication`, `test_lost_response_and_idempotent_replay_converge_to_one_receipt`, `test_adoption_conflict_refuses_before_locator_or_manifest_publication` as its principal forcing seams. | L103-L174; L177-L194; L197-L224; L227-L242 | `mcp/tests/test_lifecycle_enclosure_adoption_l2.py` |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this test file.

## Update History

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: created from the accepted full L2 candidate. Verification fields remain blank until the architect-owned closeout has a real code commit to stamp.

