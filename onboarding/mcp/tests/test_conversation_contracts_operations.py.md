# mcp/tests/test_conversation_contracts_operations.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_conversation_contracts_operations.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-07T22:45:00+02:00                                            |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb`                                        |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
| governingOverview      | `overview.md`                                          |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Part of the 260731-EFA-L7 in-place split family for `test_conversation_contracts_operations.py`'s source module; covers the behaviours named by its test classes.

## Code Commentary

- `test_turn_status_rejects_every_irrelevant_waiting_and_terminal_product`
- `test_unknown_status_evidence_can_never_establish_ready`
- `test_capability_has_no_version_demotion_predicate`
- `test_capability_state_tier_and_evidence_matrix_fails_closed`
- `test_supported_attachment_capability_requires_nonzero_exact_limits`
- `test_operation_fingerprint_is_order_stable_and_payload_sensitive`
- `test_open_and_attachment_operations_carry_semantic_revision_and_fingerprint`
- `test_open_operation_requires_one_exact_catalog_proven_identity`
- `test_open_failure_identity_rollback_and_catalog_products_are_bidirectional`
- `test_interrupt_operation_enforces_acknowledgement_settlement_products`
- `test_withdrawal_operation_enforces_phase_outcome_recovery_products`
- `test_attachment_operation_enforces_phase_outcome_recovery_products`
- `test_public_withdrawal_request_cannot_claim_server_fingerprint`
- `test_queue_projection_exposes_withdrawal_identity_only_for_queued_cockpit_work`
- `test_withdrawal_raw_recovery_exists_only_on_authoritative_withdrawn_response`

## Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/tests/test_conversation_contracts_operations.py`.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own top-level surface is listed in Code Commentary; no cross-file citation rows are needed for this split module. | — | — |

## Update History

- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
