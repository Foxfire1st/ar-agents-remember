# mcp/tests/test_organizational_completion_repair_branches.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_organizational_completion_repair_branches.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-21T00:45+02:00 |
| lastVerifiedCommitHash | `e5cb139f66abbd6502d4dcc4be883eb5f49770fe` |
| lastVerifiedCommitDate | 2026-08-21T00:28:23+02:00 |
| governingOverview | `../overview.md` |

## Governing Overview

[governing overview](../overview.md)

## Purpose

Covers the remaining error-path branches of the organizational-completion repair transition so the targeted diff-coverage floor is met.

## Code Commentary

The suite drives the queue-owned repair module's refusal branches: operation identity, operation-state fingerprint, evidence commits and binding, candidate identity, code/memory authority, repair evidence, binding/master resolution, and commit mismatch. It also pins the integration-quality repair record branch and the cancellation evidence requirement.

## Invariants And Boundaries

- Exercises production repair guards rather than copied ones.
- Refusal cases assert the boundary is enforced without ref or contract mutation.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The focused suite owns the repair-branch boundary surface. | `OrganizationalCompletionRepairBranchTests` | mcp/tests/test_organizational_completion_repair_branches.py:22-296 |

## Documentation References

No configured domain-documentation or cross-repository source applies to this file.

## Update History

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-18T01:12+02:00 — 260815-DAG-L5: created onboarding for the organizational-completion repair branch suite.
