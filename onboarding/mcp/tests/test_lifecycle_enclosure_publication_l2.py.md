# mcp/tests/test_lifecycle_enclosure_publication_l2.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_lifecycle_enclosure_publication_l2.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-23T16:08+02:00 |
| lastVerifiedCommitHash | `1d446724d099517f6f52d596b47827ae2391a2a4` |
| lastVerifiedCommitDate | 2026-08-24T00:21:10+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

Forces lifecycle enclosure publication l2 behavior at the public and durable-state boundaries.

## Code Commentary

### Logic

The principal forcing seams are `test_leaf_and_series_publication_resumes_every_ordered_cut`, `test_concurrent_locator_reservation_converges_or_types_exact_conflict`, `test_present_nonregular_and_unreadable_locator_are_not_adoption_absence`, `test_locator_manifest_contract_and_root_contradictions_remain_distinct`. The suite forces locator and immutable root-manifest publication, confinement and digest contradictions, idempotent pre-adoption enclosure adoption, and exact root-journal recovery after task-contract loss.

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
| The file defines `test_leaf_and_series_publication_resumes_every_ordered_cut`, `test_concurrent_locator_reservation_converges_or_types_exact_conflict`, `test_present_nonregular_and_unreadable_locator_are_not_adoption_absence`, `test_locator_manifest_contract_and_root_contradictions_remain_distinct` as its principal forcing seams. | L51-L128; L132-L174; L177-L203; L206-L234 | `mcp/tests/test_lifecycle_enclosure_publication_l2.py` |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this test file.

## Update History

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: created from the accepted full L2 candidate. Verification fields remain blank until the architect-owned closeout has a real code commit to stamp.

