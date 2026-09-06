# mcp/tests/test_lifecycle_preparation_selection.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_lifecycle_preparation_selection.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T17:13:06+00:00 |
| lastVerifiedCommitHash | |
| lastVerifiedCommitDate | |
| governingOverview | `overview.md` |

## Governing Overview

[Owning overview](overview.md)

## Purpose

Selected private preparation and truthful recovery phase fixtures.

## Code Commentary

### Logic

Actual selected profile/door/Git fixtures and the canonical operation store exercise command-at-most-once selection, cancellation retention, logical ref and intent drift, forbidden private/published state combinations and private recovery through requeue, launch and projection. The inherited code executor is injected and command-start-only fixtures do not claim a real command ran. These are scoped production-owner regressions, not completed Gate-5 certification.

### Conventions

Use the named source owners directly. This card describes the current uncommitted implementation; commit-based verification remains pending.

### Invariants And Boundaries

The documented types and paths do not themselves establish execution, certification, delivery or acceptance. Those claims require the corresponding owning runtime evidence.

### Todos

No source-local TODO is asserted here.

## Docs References

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation applies. | N/A | N/A |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| `_stamp` owns the corresponding behavior described above. | `_stamp` | `mcp/tests/test_lifecycle_preparation_selection.py:90-91` |
| `_fixture` owns the corresponding behavior described above. | `_fixture` | `mcp/tests/test_lifecycle_preparation_selection.py:94-115` |
| `test_changed_logical_ref_and_corrupt_selected_intent_refuse_cancellation` owns the corresponding behavior described above. | `test_changed_logical_ref_and_corrupt_selected_intent_refuse_cancellation` | `mcp/tests/test_lifecycle_preparation_selection.py:301-325` |
| `test_private_state_cannot_arrive_completed_or_combine_with_publication` owns the corresponding behavior described above. | `test_private_state_cannot_arrive_completed_or_combine_with_publication` | `mcp/tests/test_lifecycle_preparation_selection.py:328-362` |
| `test_preparation_wire_refuses_duplicate_command_order_and_wrong_owner` owns the corresponding behavior described above. | `test_preparation_wire_refuses_duplicate_command_order_and_wrong_owner` | `mcp/tests/test_lifecycle_preparation_selection.py:365-382` |
| `test_private_recovery_phase_survives_failure_requeue_launch_and_public_projection` owns the corresponding behavior described above. | `test_private_recovery_phase_survives_failure_requeue_launch_and_public_projection` | `mcp/tests/test_lifecycle_preparation_selection.py:385-442` |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository source is needed for this card. | N/A | N/A |

## Update History

### 2026-09-06T17:13:06+00:00 — Initial L34 implementation card

Created from the current source. Verification metadata is intentionally unset until a genuine commit-based verification occurs; no test or acceptance result is asserted.
