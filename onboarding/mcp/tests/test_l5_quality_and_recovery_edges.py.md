# mcp/tests/test_l5_quality_and_recovery_edges.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_l5_quality_and_recovery_edges.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-21T00:45+02:00 |
| lastVerifiedCommitHash | `e5cb139f66abbd6502d4dcc4be883eb5f49770fe` |
| lastVerifiedCommitDate | 2026-08-21T00:28:23+02:00 |
| governingOverview | `../overview.md` |

## Governing Overview

[governing overview](../overview.md)

## Purpose

Forces the residual report, certificate, public ledger-kind, series-prefix, and integration-only lifecycle boundaries around organizational completion.

## Code Commentary

The suite pins the narrow seams where the completion quality and recovery paths touch the surrounding lifecycle: residual report publication, certification revalidation, ledger-kind and series-prefix constraints on the external-memory mapping, and the integration-only boundary that ordinary leaves never cross.

## Invariants And Boundaries

- Exercises production owners rather than copied guards.
- Refusal cases assert the boundary is enforced without ref or ledger mutation.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The focused suite owns the quality-and-recovery boundary surface. | `L5QualityAndRecoveryEdgeTests` | mcp/tests/test_l5_quality_and_recovery_edges.py:23-122 |

## Documentation References

No configured domain-documentation or cross-repository source applies to this file.

## Update History

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-17T12:09+02:00 — 260815-DAG-L5: created onboarding for the L5 quality-and-recovery boundary suite.
