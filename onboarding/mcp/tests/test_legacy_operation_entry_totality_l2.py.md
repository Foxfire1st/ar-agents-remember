# mcp/tests/test_legacy_operation_entry_totality_l2.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_legacy_operation_entry_totality_l2.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-23T16:08+02:00 |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d` |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

Forces legacy operation entry totality l2 behavior at the public and durable-state boundaries.

## Code Commentary

### Logic

The principal forcing seams are `test_legacy_public_entry_refuses_unconfined_contract_before_any_read`, `test_preadoption_unreadable_initial_contract_never_inferrs_report_target`, `test_addressable_unreadable_initial_contract_uses_locator_publication_authority`, `test_legacy_reload_failure_refuses_before_raw_record_access`. The suite bounds schema-1 inspect/migrate/archive and proves confinement, original-byte evidence, dedicated serialization, idempotence, removal guards, and separation from normal current-schema admission.

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
| The file defines `test_legacy_public_entry_refuses_unconfined_contract_before_any_read`, `test_preadoption_unreadable_initial_contract_never_inferrs_report_target`, `test_addressable_unreadable_initial_contract_uses_locator_publication_authority`, `test_legacy_reload_failure_refuses_before_raw_record_access` as its principal forcing seams. | `test_legacy_public_entry_refuses_unconfined_contract_before_any_read`; `test_preadoption_unreadable_initial_contract_never_inferrs_report_target`; `test_addressable_unreadable_initial_contract_uses_locator_publication_authority`; `test_legacy_reload_failure_refuses_before_raw_record_access` | mcp/tests/test_legacy_operation_entry_totality_l2.py:43-63; mcp/tests/test_legacy_operation_entry_totality_l2.py:66-95; mcp/tests/test_legacy_operation_entry_totality_l2.py:98-122; mcp/tests/test_legacy_operation_entry_totality_l2.py:125-164 |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this test file.

## Update History

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: created from the accepted full L2 candidate. Verification fields remain blank until the architect-owned closeout has a real code commit to stamp.

