# mcp/tests/test_pytest_bootstrap_boundaries.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_pytest_bootstrap_boundaries.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-28T07:20+02:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Proves Dagger admission and hermetic bootstrap remain separate after Candidate A retirement and
the verification package move out of product `src`.

## Code Commentary

### Logic

The cases force opaque certifying authority, candidate/Git/global isolation, Candidate A artifact
absence, service deferral, and the no-eager-import boundary. The hermetic child path contains both
`mcp/test_support` and `mcp/src`, while importing the shared plugin remains free of Dagger/service
side effects.

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
| No external domain source is required for this repository-owned test contract. | `VALID_NONCE` | mcp/tests/test_pytest_bootstrap_boundaries.py:43-43 |

## Repo-Internal References

The test file is direct evidence for the production boundary named above.

| Finding | Anchor | Source |
| --- | --- | --- |
| The selected scenarios and assertions implement this test unit's forcing proof. | `VALID_NONCE` | mcp/tests/test_pytest_bootstrap_boundaries.py:43-43 |

## Cross-Repo References

No cross-repository source is allowed by the resolved settings.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repository reference applies. | `VALID_NONCE` | mcp/tests/test_pytest_bootstrap_boundaries.py:43-43 |

## Update History

- 2026-08-28T06:28+02:00 — PDLS wave 005 curator: replaced the obsolete four-state/direct-runner
  account with Candidate A retirement, opaque certification, dual product/verification import
  roots, and shared-plugin service deferral.

- 2026-08-25T15:44+02:00 — Created during PDLS whole-system reconciliation after source and
  requirement review. Verification remains closeout-owned.
