# mcp/tests/test_l5_quality_and_recovery_edges.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_l5_quality_and_recovery_edges.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T21:23+02:00 |
| lastVerifiedCommitHash | `b99501852bcfa5f499a25e7183063751f6133a28` |
| lastVerifiedCommitDate | 2026-08-24T21:21:58+02:00 |
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

## 260821-DAGQC-L2 Quality Recovery Edges

The quality edge cases now reject hostile/non-object/extra-root manifest shapes through the shared
error, verify declared artifact integrity from one snapshot, and assert recovered responses retain
the stable wrapper report separately from the immutable published result.

## 260824-PDLS Recovery Evidence Proof

Recovery fixtures now publish schema-2 generations with candidate trees and require typed
certifying evidence in fresh success payloads. Invalid/unreadable result exports refuse publication,
and recovered evidence must match the current Git tree. Schema `1.0` remains a deliberate public
reader refusal, not a compatibility route.

## Update History

- 2026-08-24T21:23+02:00 — Updated quality recovery for candidate-bound certifying evidence.

- 2026-08-24T14:19+02:00 — 260821-DAGQC-L2: extended focused recovery edges for strict manifest authority and distinct stable/published result paths. Verification metadata remains pinned until architect-owned closeout.


- 2026-08-24T00:51+02:00 — No content impact: 260821-CLIVE-L2 the test only repoints `LifecycleOperationStore` to its moved integration lifecycle package. Verified at code commit `1d446724`.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-17T12:09+02:00 — 260815-DAG-L5: created onboarding for the L5 quality-and-recovery boundary suite.
