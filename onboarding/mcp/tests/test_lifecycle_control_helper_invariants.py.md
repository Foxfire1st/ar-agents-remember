# mcp/tests/test_lifecycle_control_helper_invariants.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_lifecycle_control_helper_invariants.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-26T16:57+02:00 |
| lastVerifiedCommitHash | `8dcf0645fdbc3aa490132d5947b22227d45ff302` |
| lastVerifiedCommitDate | 2026-08-26T16:57:26+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Proves lifecycle cancellation, generation replacement, and completed-disposition helpers.

## Code Commentary

### Logic

The cases cover worker termination, door/queue ownership, repair failure, retry convergence, exact
completed owners, and cancelled closeout replacement from a current waiting door whose provenance
may have advanced after cancellation.

### Conventions

Tests execute production owners and use shared builders only for canonical setup. Scenario-specific
differences remain in the test so fixtures do not become a parallel implementation.

### Invariants And Boundaries

- The suite preserves loud negative cases and exact identity/refusal assertions; it does not obtain
  green through a fallback, allowlist, or weakened production threshold.
- Cancelled replacement accepts a current waiting door only with worker-exit proof and still rejects
  a deferred door or unproven exit.
- Dagger owns certifying execution. Any direct execution remains bounded diagnostic evidence only.

### Todos

None recorded.

## Docs References

The configured Domain Documentation registry is empty. No external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain source is required for this repository-owned test contract. | `test_cancelled_closeout_and_completed_replacement_bind_release_proof` | mcp/tests/test_lifecycle_control_helper_invariants.py:1-343 |

## Repo-Internal References

The test file is direct evidence for the production boundary named above.

| Finding | Anchor | Source |
| --- | --- | --- |
| The selected scenarios and assertions implement this test unit's forcing proof. | `test_cancelled_closeout_and_completed_replacement_bind_release_proof` | mcp/tests/test_lifecycle_control_helper_invariants.py:1-343 |

## Cross-Repo References

No cross-repository source is allowed by the resolved settings.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repository reference applies. | `test_cancelled_closeout_and_completed_replacement_bind_release_proof` | mcp/tests/test_lifecycle_control_helper_invariants.py:1-343 |

## Update History

- 2026-08-26T16:57+02:00 — Replaced mocked claimed-predecessor proof with the production
  cancelled-closeout boundary: current waiting provenance plus proven worker exit advances, while
  deferred disposition and unproven exit refuse.
- 2026-08-25T15:44+02:00 — Created during PDLS whole-system reconciliation after source and
  requirement review. Verification remains closeout-owned.
