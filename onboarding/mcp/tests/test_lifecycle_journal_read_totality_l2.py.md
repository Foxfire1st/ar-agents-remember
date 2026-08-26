# mcp/tests/test_lifecycle_journal_read_totality_l2.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_lifecycle_journal_read_totality_l2.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T14:48+02:00 |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d` |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

Forces lifecycle journal read totality l2 behavior at the public and durable-state boundaries.

## Code Commentary

### Logic

The principal forcing seams are `test_registered_public_reader_refuses_empty_proven_claim_timestamp`, `test_strict_journal_failure_status_stale_control_and_context_are_total`, `test_unreadable_contract_public_start_status_and_real_context_use_locator_journal`, `test_deleted_contract_real_context_retains_exact_root_journal_operation`. The suite proves public status, controls, and context remain total for expected journal/location failures while preserving exact typed decisions and leaving unexpected faults loud.

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
| The file defines `test_registered_public_reader_refuses_empty_proven_claim_timestamp`, `test_strict_journal_failure_status_stale_control_and_context_are_total`, `test_unreadable_contract_public_start_status_and_real_context_use_locator_journal`, `test_deleted_contract_real_context_retains_exact_root_journal_operation` as its principal forcing seams. | `test_registered_public_reader_refuses_empty_proven_claim_timestamp`; `test_strict_journal_failure_status_stale_control_and_context_are_total`; `test_unreadable_contract_public_start_status_and_real_context_use_locator_journal`; `test_deleted_contract_real_context_retains_exact_root_journal_operation` | mcp/tests/test_lifecycle_journal_read_totality_l2.py:190-243; mcp/tests/test_lifecycle_journal_read_totality_l2.py:246-301; mcp/tests/test_lifecycle_journal_read_totality_l2.py:304-370; mcp/tests/test_lifecycle_journal_read_totality_l2.py:373-416 |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this test file.

## Current Contract — 260821 CLIVE Final

This is the current source-backed contract for this test card. It supersedes any earlier
queue-lifecycle, blocker-row, replan/drain, or compatibility-reader wording where present.

Forces total public behavior for malformed current journals, successor journals, locator/manifest failures, and missing or unreadable live contracts.

### Current Invariants

- Locator-to-manifest-to-journal addressability survives task-side contract loss.
- Expected failures become one typed public decision; present-unreadable evidence is never absence.

## Update History

- 2026-08-24T14:48+02:00 — DAGQC cumulative CLIVE final-gap curation: reconciled this test card to current source while preserving prior history and verification provenance.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: created from the accepted full L2 candidate. Verification fields remain blank until the architect-owned closeout has a real code commit to stamp.
