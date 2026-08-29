# mcp/tests/test_lifecycle_operation_controls_l2.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_lifecycle_operation_controls_l2.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-29T10:09+02:00 |
| lastVerifiedCommitHash |  `60e429d17e9fcbca3ab1c02563afcaa5761b8c5a`|
| lastVerifiedCommitDate |  2026-08-29T20:33:10+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Forces task-addressed lifecycle controls and dispositions.

## Code Commentary

### Logic

The suite covers start, observe, resume, retry, cancel, cleanup, completed direct/closeout, and unreadable journal states. Its cancellation cases distinguish preserved staged/repaired candidates from unattributed protected-ref changes.

### Conventions

Tests execute production owners and use shared builders only for canonical setup. Scenario-specific
differences remain in the test so fixtures do not become a parallel implementation.

### Invariants And Boundaries

- The suite preserves loud negative cases and exact identity/refusal assertions; it does not obtain
  green through a fallback, allowlist, or weakened production threshold.
- Dagger owns certifying execution. Any direct execution remains bounded diagnostic evidence only.

### Todos

None recorded.

## Docs References

The configured Domain Documentation registry is empty. No external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain source is required for this repository-owned test contract. | `_command` | mcp/tests/test_lifecycle_operation_controls_l2.py:1-983 |

## Repo-Internal References

The test file is direct evidence for the production boundary named above.

| Finding | Anchor | Source |
| --- | --- | --- |
| The selected scenarios and assertions implement this test unit's forcing proof. | `_command` | mcp/tests/test_lifecycle_operation_controls_l2.py:1-983 |

## Cross-Repo References

No cross-repository source is allowed by the resolved settings.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repository reference applies. | `_command` | mcp/tests/test_lifecycle_operation_controls_l2.py:1-983 |

## Update History

- 2026-08-29T10:09+02:00 — Added the failed-gate successor boundary: cancellation preserves
  uncommitted repair bytes but refuses an unattributed HEAD change as a developer decision.
- 2026-08-25T15:44+02:00 — Created during PDLS whole-system reconciliation after source and
  requirement review. Verification remains closeout-owned.
