# mcp/tests/test_direct_landing_operation_recovery.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_direct_landing_operation_recovery.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | `fbc89847233b1c5959f56475f2cb51f936d5ef0b` |
| lastVerifiedCommitDate | 2026-09-02T07:47:04+02:00|
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

Under CCR-R03@v1 the admitted-store case now rebuilds the record through `direct_landing_record`
with the stored candidate and admitted door publication, then requires the rebuilt record's
declared dependency set (`require_lifecycle_operation_dependencies`) — so the recovery matrix proves
a dependency-declared, door-bound record can be rebuilt and stays current
cit:([`DirectLandingOperationRecoveryTests.test_*`], mcp/tests/test_direct_landing_operation_recovery.py:209-230).

### Conventions

Tests execute production owners and use shared builders only for canonical setup. Scenario-specific
differences remain in the test so fixtures do not become a parallel implementation.

### Invariants And Boundaries

- The suite preserves loud negative cases and exact identity/refusal assertions; it does not obtain
  green through a fallback, allowlist, or weakened production threshold.
- Dagger owns certifying execution. Any direct execution remains bounded diagnostic evidence only.
- Door-bound direct-landing records must rebuild with a dependency declaration equal to their
  admitted inputs.

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
| R03 dependency-required rebuild of door-bound records. | `direct_landing_record`; `require_lifecycle_operation_dependencies` | mcp/tests/test_direct_landing_operation_recovery.py:209-230 |

## Cross-Repo References

No cross-repository source is allowed by the resolved settings.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repository reference applies. | `_RETRY_LEGS` | mcp/tests/test_direct_landing_operation_recovery.py:59-59 |

## Update History

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for fbc89847233b1c5959f56475f2cb51f936d5ef0b (CCR-R03@v1/L03): recorded the dependency-required direct-landing-record rebuild proof; prior recovery-matrix prose preserved.

- 2026-08-26T14:32+02:00 — Added direct-landing recovery proof for current-versus-historical
  same-code mappings and memory-only supersession without history loss. Verification remains
  closeout-owned.
- 2026-08-25T15:44+02:00 — Created during PDLS whole-system reconciliation after source and
  requirement review. Verification remains closeout-owned.