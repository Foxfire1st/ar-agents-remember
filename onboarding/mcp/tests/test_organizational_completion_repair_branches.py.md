# mcp/tests/test_organizational_completion_repair_branches.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_organizational_completion_repair_branches.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-18T01:12+02:00 |
| lastVerifiedCommitHash | `cdcdc566fc6bee44b371a9d15c2048ceb1a49b8b` |
| lastVerifiedCommitDate | 2026-08-18T03:31:59+02:00|
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

- 2026-08-18T01:12+02:00 — 260815-DAG-L5: created onboarding for the organizational-completion repair branch suite.
