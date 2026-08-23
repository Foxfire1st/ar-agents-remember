# mcp/tests/test_organizational_completion_branches.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_organizational_completion_branches.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-23T16:08+02:00 |
| lastVerifiedCommitHash | `1d446724d099517f6f52d596b47827ae2391a2a4` |
| lastVerifiedCommitDate | 2026-08-24T00:21:10+02:00 |
| governingOverview | `../overview.md` |

## Governing Overview

[governing overview](../overview.md)

## Purpose

Forces the canonical completion/sibling matrix, exact master-generation drift, and both directions of finality-scope change with unchanged refs, contract, and queue candidate.

## Code Commentary

The suite exercises the production completion and publication owners across branch-shaped scenarios: a non-final leaf reuses its targeted closeout certification, a final leaf runs one full gate, exact master-generation drift is refused, and final-to-nonfinal / nonfinal-to-final scope changes return the structured pre-boundary result without moving refs.

## Invariants And Boundaries

- Exercises production owners rather than a parallel policy implementation.
- Every refusal asserts refs, contract bytes, and the queue candidate remain unchanged.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The focused suite owns the completion-branch forcing surface. | `OrganizationalCompletionBranchTests` | mcp/tests/test_organizational_completion_branches.py:28-482 |

## Documentation References

No configured domain-documentation or cross-repository source applies to this file.

## 260821-CLIVE-L2 Current Regression Contract

The current forcing seams include `test_completion_scope_and_completed_marker_guard_matrix`, `test_sibling_loading_and_master_publication_guards`, `test_candidate_identity_guard_matrix`, `test_landed_sibling_identity_target_ancestry_and_memory_guards`. The L2 additions force journal-owned claim transfer, exact protected-ref decisions, source-movement reconciliation, and organizational disposition/repair without queue-owned lifecycle evidence.

### Reconciled Source Evidence

| Finding | Citations | Source Path |
| --- | --- | --- |
| The current test source exercises `test_completion_scope_and_completed_marker_guard_matrix`, `test_sibling_loading_and_master_publication_guards`, `test_candidate_identity_guard_matrix`, `test_landed_sibling_identity_target_ancestry_and_memory_guards`. | L75-L154; L156-L219; L221-L251; L253-L322 | `mcp/tests/test_organizational_completion_branches.py` |

## Update History

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this test card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-17T12:09+02:00 — 260815-DAG-L5: created onboarding for the organizational completion branch forcing suite.
