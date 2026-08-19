# mcp/tests/test_integration_branch_authority_bootstrap_edges.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_integration_branch_authority_bootstrap_edges.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-19T22:32+02:00 |
| lastVerifiedCommitHash | `b523f53b193e9783e7c7e6410c772e7d64d8df17` |
| lastVerifiedCommitDate | 2026-08-19T21:54:50+02:00|
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
| The suite owns bootstrap journal, recovery, rollback, ref-transaction, and external-memory authority edge cases. | `IntegrationBranchAuthorityBootstrapEdgeTests` | mcp/tests/test_integration_branch_authority_bootstrap_edges.py:21-284 |

## Documentation References

No configured domain-documentation or cross-repository source applies to this file.

## Update History

- 2026-08-19T22:32+02:00 — No content impact: 260815-DAG-L13 reworded the expected bootstrap refusal to "effective atomic master nature"; the documented refusal boundary is unchanged. Verification remains closeout-owned.

- 2026-08-16T09:45+02:00 — Added production-owner forcing for malformed/mismatched recovery records, partial rollback failure, exact-ref transaction refusal, and external-memory journal drift after the targeted Dagger coverage report.
- 2026-08-16T04:43+02:00 — 260815-DAG-L4: created by moving the three contiguous bootstrap edge tests from `test_integration_branch_authority_edges.py` to keep both discovered modules below the enforced file-size limit without duplicating helpers or compatibility imports. Verification remains closeout-owned.
