# mcp/tests/test_organizational_completion_repair_branches.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_organizational_completion_repair_branches.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-23T16:08+02:00 |
| lastVerifiedCommitHash | `1d446724d099517f6f52d596b47827ae2391a2a4` |
| lastVerifiedCommitDate | 2026-08-24T00:21:10+02:00 |
| governingOverview | `../overview.md` |

## Governing Overview

[governing overview](../overview.md)

## Purpose

Covers the remaining error-path branches of the organizational-completion repair transition so the targeted diff-coverage floor is met.

## Code Commentary

The suite drives the integration-journal repair module's refusal branches: operation identity,
operation-state fingerprint, evidence commits and binding, candidate identity, code/memory
authority, repair evidence, binding/master resolution, and commit mismatch. It also pins the
integration-quality repair record branch, queue-candidate disposition, and cancellation evidence.

## Invariants And Boundaries

- Exercises production repair guards rather than copied ones.
- Refusal cases assert the boundary is enforced without ref or contract mutation.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The focused suite owns the repair-branch boundary surface. | `OrganizationalCompletionRepairBranchTests` | mcp/tests/test_organizational_completion_repair_branches.py:24-274 |

## Documentation References

No configured domain-documentation or cross-repository source applies to this file.

## 260821-CLIVE-L2 Current Regression Contract

The current forcing seams include `test_record_repair_refuses_mismatched_operation_identity`, `test_repair_evidence_refuses_operation_state_mismatch`, `test_prepare_refuses_non_gate_failed_result`, `test_prepare_refuses_missing_repair_evidence`. The L2 additions force journal-owned claim transfer, exact protected-ref decisions, source-movement reconciliation, and organizational disposition/repair without queue-owned lifecycle evidence.

### Reconciled Source Evidence

| Finding | Citations | Source Path |
| --- | --- | --- |
| The current test source exercises `test_record_repair_refuses_mismatched_operation_identity`, `test_repair_evidence_refuses_operation_state_mismatch`, `test_prepare_refuses_non_gate_failed_result`, `test_prepare_refuses_missing_repair_evidence`. | L87-L96; L99-L104; L107-L111; L113-L117 | `mcp/tests/test_organizational_completion_repair_branches.py` |

## Update History

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this test card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-18T01:12+02:00 — 260815-DAG-L5: created onboarding for the organizational-completion repair branch suite.
