# mcp/tests/test_configured_contract_admission_l2.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_configured_contract_admission_l2.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-30T07:35+02:00 |
| lastVerifiedCommitHash |  `346507af24396ab7b491e02511c4af006ccd3dc5`|
| lastVerifiedCommitDate |  2026-08-30T07:51:57+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Proves all configured-contract consumers share one closed semantic admission API.

## Code Commentary

### Logic

The cases check the total accepted/refused result family and consistent translation across public
tools. Their legacy below-queue fixture now publishes the shared typed synthetic waiting door
before exercising closeout apply. This supplies the scheduling input production requires without
weakening or mocking away the production door-generation invariant.

A focused candidate-identity case drives both strict external-leaf sides through the public
authority function: a foreign code checkout is named `code/candidate`, and a foreign memory
checkout is named `memory/candidate`. The test stubs only already-proven configured repository
identity so it isolates the candidate comparison without duplicating repository discovery.

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
| No external domain source is required for this repository-owned test contract. | `_byte_tree` | mcp/tests/test_configured_contract_admission_l2.py:1-671 |

## Repo-Internal References

The test file is direct evidence for the production boundary named above.

| Finding | Anchor | Source |
| --- | --- | --- |
| The selected scenarios and assertions implement this test unit's forcing proof. | `_byte_tree` | mcp/tests/test_configured_contract_admission_l2.py:1-671 |

## Cross-Repo References

No cross-repository source is allowed by the resolved settings.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repository reference applies. | `_byte_tree` | mcp/tests/test_configured_contract_admission_l2.py:1-671 |

## Update History

- 2026-08-30T07:35+02:00 — MCAR-L03 A009: forced both strict candidate-repository mismatch
  branches after generation 9 left them as the only uncovered changed units.

- 2026-08-30T07:05+02:00 — MCAR-L03 A008: made below-queue configured-admission scenarios own
  an explicit typed fixture door so closeout tests reach the authority transition they intend to
  exercise.

- 2026-08-25T15:44+02:00 — Created during PDLS whole-system reconciliation after source and
  requirement review. Verification remains closeout-owned.
