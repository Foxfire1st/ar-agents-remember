# mcp/tests/test_integration_branch_authority_bootstrap_edges.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_integration_branch_authority_bootstrap_edges.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-23T16:08+02:00 |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d` |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[governing overview](../overview.md)

## Purpose

Forces journaled atomic-series bootstrap to reject changed sprint branch authority, source-tip or
topology drift, malformed WAL, mismatched published contracts, partial-ref rollback failure, ref
transaction races, and code/external-memory identity changes.

## Code Commentary

The focused suite reuses the real configured repository and task-topology builders from
`integration_branch_authority_test_support.py`. Each test drives
`ensure_master_series_contract` through its production journal and publication seams, injects
exactly one crash or concurrent authority change, and proves refs, contracts, and bootstrap WAL
state remain recoverable or absent as required.
Direct helper cases retain the real journal capability and exact expected-old values, so they cover
the lowest writer without inventing a test-only bypass.

## Invariants And Boundaries

- Bootstrap journal recovery is bound to the exact task-derived sprint source branch.
- Code source tips and master execution nature are revalidated immediately before first ref creation.
- Failure leaves no unjournaled atomic branch, contract, or stale bootstrap record.
- External-memory bootstrap records remain paired with their exact repository and source branch.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The suite owns bootstrap journal, recovery, rollback, ref-transaction, and external-memory authority edge cases. | `IntegrationBranchAuthorityBootstrapEdgeTests` | mcp/tests/test_integration_branch_authority_bootstrap_edges.py:23-284 |

## Documentation References

No configured domain-documentation or cross-repository source applies to this file.

## 260821-CLIVE-L2 Current Regression Contract

The current forcing seams include `test_bootstrap_record_revalidates_repository_path_and_memory_edge`, `test_bootstrap_journal_refuses_changed_sprint_branch_without_mutation`, `test_bootstrap_revalidates_source_tip_before_first_ref_creation`, `test_bootstrap_revalidates_atomic_topology_before_first_ref_creation`. The L2 additions force journal-owned claim transfer, exact protected-ref decisions, source-movement reconciliation, and organizational disposition/repair without queue-owned lifecycle evidence.

### Reconciled Source Evidence

| Finding | Anchor | Source |
| --- | --- | --- |
| The current test source exercises `test_bootstrap_record_revalidates_repository_path_and_memory_edge`, `test_bootstrap_journal_refuses_changed_sprint_branch_without_mutation`, `test_bootstrap_revalidates_source_tip_before_first_ref_creation`, `test_bootstrap_revalidates_atomic_topology_before_first_ref_creation`. | `test_bootstrap_record_revalidates_repository_path_and_memory_edge`; `test_bootstrap_journal_refuses_changed_sprint_branch_without_mutation`; `test_bootstrap_revalidates_source_tip_before_first_ref_creation`; `test_bootstrap_revalidates_atomic_topology_before_first_ref_creation` | mcp/tests/test_integration_branch_authority_bootstrap_edges.py:24-48; mcp/tests/test_integration_branch_authority_bootstrap_edges.py:50-90; mcp/tests/test_integration_branch_authority_bootstrap_edges.py:92-116; mcp/tests/test_integration_branch_authority_bootstrap_edges.py:118-146 |

## Update History

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this test card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-19T22:32+02:00 — No content impact: 260815-DAG-L13 reworded the expected bootstrap refusal to "effective atomic master nature"; the documented refusal boundary is unchanged. Verification remains closeout-owned.

- 2026-08-16T09:45+02:00 — Added production-owner forcing for malformed/mismatched recovery records, partial rollback failure, exact-ref transaction refusal, and external-memory journal drift after the targeted Dagger coverage report.
- 2026-08-16T04:43+02:00 — 260815-DAG-L4: created by moving the three contiguous bootstrap edge tests from `test_integration_branch_authority_edges.py` to keep both discovered modules below the enforced file-size limit without duplicating helpers or compatibility imports. Verification remains closeout-owned.
