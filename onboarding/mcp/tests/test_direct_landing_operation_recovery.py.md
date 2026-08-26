# mcp/tests/test_direct_landing_operation_recovery.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_direct_landing_operation_recovery.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-26T14:32+02:00 |
| lastVerifiedCommitHash |  `7833df0b219bba560f67f6e1158c3f4f155e1ce6`|
| lastVerifiedCommitDate |  2026-08-26T15:02:28+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Exercises production-shaped crash and drift cuts for durable direct landing.

## Code Commentary

### Logic

The suite proves retry convergence across journal, Git, quality, publication, and external-memory boundaries.

The same-generation recovery matrix includes a newest exact mapping with older history and a
settings-only memory change that supersedes a historical same-code row while preserving it in the
new ledger commit.

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
| No external domain source is required for this repository-owned test contract. | `_RETRY_LEGS` | mcp/tests/test_direct_landing_operation_recovery.py:59-59 |

## Repo-Internal References

The test file is direct evidence for the production boundary named above.

| Finding | Anchor | Source |
| --- | --- | --- |
| The selected scenarios and assertions implement this test unit's forcing proof. | `_RETRY_LEGS` | mcp/tests/test_direct_landing_operation_recovery.py:59-59 |

## Cross-Repo References

No cross-repository source is allowed by the resolved settings.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repository reference applies. | `_RETRY_LEGS` | mcp/tests/test_direct_landing_operation_recovery.py:59-59 |

## Update History

- 2026-08-26T14:32+02:00 — Added direct-landing recovery proof for current-versus-historical
  same-code mappings and memory-only supersession without history loss. Verification remains
  closeout-owned.
- 2026-08-25T15:44+02:00 — Created during PDLS whole-system reconciliation after source and
  requirement review. Verification remains closeout-owned.
