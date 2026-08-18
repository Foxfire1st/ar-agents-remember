# mcp/tests/test_integration_branch_authority_series_drift.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_integration_branch_authority_series_drift.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-16T07:46+02:00 |
| lastVerifiedCommitHash | `25841d0ddc2d93c4950abf097168fa24b220c5ad` |
| lastVerifiedCommitDate | 2026-08-18T11:30:22+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[governing overview](../overview.md)

## Purpose

Forces an atomic series whose sprint source advanced after closeout to refuse the leaf-owned
replay/conflict path instead of treating the ambient repository checkout as a writable leaf.

## Code Commentary

The focused regression uses the real configured atomic blocker, series contract, named atomic
candidate ref, and lifecycle operation owner. It advances the sprint super after series closeout,
requests replay, and proves operation creation refuses before a durable journal is written.

## Invariants And Boundaries

- Atomic-series source drift cannot be resolved through an ambient leaf worktree.
- A refused replay attempt creates no integration operation record.
- The test is moved from the broader edge suite without duplicated behavior or compatibility code.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The focused suite owns the atomic-series source-drift replay refusal. | `IntegrationBranchAuthoritySeriesDriftTests` | mcp/tests/test_integration_branch_authority_series_drift.py:22-51 |

## Documentation References

No configured domain-documentation or cross-repository source applies to this file.

## Update History

- 2026-08-18T09:05+02:00 — Renamed the atomic 'barrier' concept to 'blocker' throughout (terminology unification; no behavioral change). Verification remains closeout-owned.

- 2026-08-16T07:46+02:00 — 260815-DAG-L4: created by moving the atomic source-drift/replay refusal from `test_integration_branch_authority_edges.py` to keep both discovered modules below the enforced file-size limit without duplication. Verification remains closeout-owned.
