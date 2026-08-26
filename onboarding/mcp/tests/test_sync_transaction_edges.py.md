# mcp/tests/test_sync_transaction_edges.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_sync_transaction_edges.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-26T08:10+02:00 |
| lastVerifiedCommitHash |  `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d`|
| lastVerifiedCommitDate |  2026-08-26T08:10:26+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Focused state-machine and authority-edge coverage for contract-addressed resumable sync outside
the real-Git happy-path integration suite.

## Code Commentary

### Logic

Authority tests reject missing source branches, unsupported contract kinds, malformed official
ledger pairs, pinned-ref mismatch, partial recovery authority, contract identity drift, and moved
bases. Result tests cover complete and incomplete resolution previews, terminal/quarantine replay,
input refusal, internal exception containment, and typed absence of an active resolution.

The driver matrix then forces admission preflight, already-current memory validation, active
preview routing, every live phase transition, automatic and continued proof failures, reconciliation
of already-created operation heads, missing-journal recovery, and the immutable admitted memory
choice. Each case asserts the typed public result produced by the owning boundary.

### Invariants And Boundaries

- Canonical contract kind, identity, source pair, and pinned refs are prerequisites, not hints.
- Quarantine, missing journal, and terminal replay use explicit typed routes; none silently starts a new operation.
- Continue/cancel address the current canonical contract and cannot replace admitted choices.
- Focused lower-level failures remain visible as controlled refusal detail at the driver boundary.
- Queue rows and task prose never repair or reconstruct transaction authority.

## Docs References

No Domain Documentation source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Source-pair and pinned-authority guards reject every unproven admission shape. | `test_official_pair_preflight_reports_each_ledger_failure`; `test_recovery_side_refs_distinguish_absent_partial_and_complete`; `test_record_contract_and_base_guards_reject_identity_drift` | mcp/tests/test_sync_transaction_edges.py:152-182; mcp/tests/test_sync_transaction_edges.py:196-216; mcp/tests/test_sync_transaction_edges.py:219-260 |
| Public replay and driver routing preserve typed recovery/refusal outcomes. | `test_terminal_and_quarantine_replays_preserve_typed_outcomes`; `test_sync_boundary_returns_input_and_internal_refusals`; `test_resume_live_routes_each_active_transition` | mcp/tests/test_sync_transaction_edges.py:286-317; mcp/tests/test_sync_transaction_edges.py:320-331; mcp/tests/test_sync_transaction_edges.py:448-476 |
| Missing-journal recovery and immutable memory choice remain contract-addressed. | `test_missing_journal_and_admitted_memory_choice_route_to_typed_recovery` | mcp/tests/test_sync_transaction_edges.py:548-570 |
| The driver owns public phase routing while focused modules own authority, Git, state, results, and recovery. | `sync_contract_under_authority` | mcp/src/agents_remember/worktrees/sync_transaction.py:72-100 |

## Cross-Repo References

No cross-repository implementation source governs this focused suite.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History

- 2026-08-26T08:10+02:00 — Created strict onboarding for the frozen sync transaction edge suite.
  Verification metadata remains empty until closeout can stamp a real code commit.
