# mcp/tests/test_lifecycle_operation_controls_l2.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_lifecycle_operation_controls_l2.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | `99dc249bd507c20b09ece1169c2b1fa2af8e8c1b` |
| lastVerifiedCommitDate | 2026-09-02T05:53:10+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Forces task-addressed lifecycle controls and dispositions.

## Code Commentary

### Logic

The suite covers start, observe, resume, retry, cancel, cleanup, completed direct/closeout, and unreadable journal states. Its cancellation cases distinguish preserved staged/repaired candidates from unattributed protected-ref changes.

Since 260831-CCR (commit `99dc249b`) the suite adds
`test_public_control_refuses_stale_recover_for_legacy_missing_intent` (line 169-208): it takes a
dirty closeout record whose door/journal carry a `MissingTaskIntent`, rewrites the store bytes,
and proves that the previously advertised `recover` row is refused by the public control handler
(`_public_control`) with `status=lifecycle-control-not-legal`, no worker launch, and the exact
store bytes unchanged — the L25 repair's stale-recover refusal without reuse of the legacy
generation.

### Conventions

Tests execute production owners and use shared builders only for canonical setup. Scenario-specific
differences remain in the test so fixtures do not become a parallel implementation.

### Invariants And Boundaries

- The suite preserves loud negative cases and exact identity/refusal assertions; it does not obtain
  green through a fallback, allowlist, or weakened production threshold.
- Dagger owns certifying execution. Any direct execution remains bounded diagnostic evidence only.
- A stale recover or retry row advertised before a missing-intent rewrite is rejected by the
  public handler on revalidation, with no worker launch and no journal bytes changed.

### Todos

None recorded.

## Docs References

The configured Domain Documentation registry is empty. No external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain source is required for this repository-owned test contract. | `_command` | mcp/tests/test_lifecycle_operation_controls_l2.py:1-1030 |

## Repo-Internal References

The test file is direct evidence for the production boundary named above.

| Finding | Anchor | Source |
| --- | --- | --- |
| The selected scenarios and assertions implement this test unit's forcing proof. | `_command` | mcp/tests/test_lifecycle_operation_controls_l2.py:1-1030 |
| The stale-recover missing-intent refusal regression. | `test_public_control_refuses_stale_recover_for_legacy_missing_intent` | mcp/tests/test_lifecycle_operation_controls_l2.py:169-208 |
| The typed sentinel used to rewrite the legacy generation. | `MissingTaskIntent` | mcp/tests/test_lifecycle_operation_controls_l2.py:180-184 |

## Cross-Repo References

No cross-repository source is allowed by the resolved settings.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repository reference applies. | `_command` | mcp/tests/test_lifecycle_operation_controls_l2.py:1-1030 |

## CCR-R02@v2 Public-Control Missing-Intent Refusal

Per `requirements/CCR-R02-v2-normative-task-intent-identity.md` and the L25 repair, a stale
previously advertised recover/retry action is rejected when the public handler revalidates
current evidence against a missing-intent generation; this regression pins that refusal with no
worker launch. Part of the landed L25 candidate `99dc249b`.

## Update History

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for 99dc249bd507 (CCR-R02@v2/L25):
  added the public-control stale-recover refusal regression for legacy missing-intent generations;
  documented the no-worker-launch, byte-preserving failure proof. Verified at code commit
  99dc249bd507c20b09ece1169c2b1fa2af8e8c1b.

- 2026-08-29T10:09+02:00 — Added the failed-gate successor boundary: cancellation preserves
  uncommitted repair bytes but refuses an unattributed HEAD change as a developer decision.
- 2026-08-25T15:44+02:00 — Created during PDLS whole-system reconciliation after source and
  requirement review. Verification remains closeout-owned.
