# mcp/tests/test_organizational_completion_branches.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_organizational_completion_branches.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-21T00:45+02:00 |
| lastVerifiedCommitHash | `e5cb139f66abbd6502d4dcc4be883eb5f49770fe` |
| lastVerifiedCommitDate | 2026-08-21T00:28:23+02:00 |
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
| The focused suite owns the completion-branch forcing surface. | `OrganizationalCompletionBranchTests` | mcp/tests/test_organizational_completion_branches.py:24-476 |

## Documentation References

No configured domain-documentation or cross-repository source applies to this file.

## Update History

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-17T12:09+02:00 — 260815-DAG-L5: created onboarding for the organizational completion branch forcing suite.
