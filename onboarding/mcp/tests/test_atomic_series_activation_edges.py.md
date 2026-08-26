# mcp/tests/test_atomic_series_activation_edges.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_atomic_series_activation_edges.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-26T08:10+02:00 |
| lastVerifiedCommitHash |  `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d`|
| lastVerifiedCommitDate |  2026-08-26T08:10:26+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Focused validation, observation, archive, release, and selecting-transaction edge coverage for the
single disposable atomic-series activation authority.

## Code Commentary

### Logic

Identity cases reject blank or unprovable repositories, incomplete external pairs, absent
coordination authority, terminal contracts, noncanonical contract/master refs, and any loaded
contract that no longer matches its recorded pair and master. Store cases translate observation
failures, distinguish malformed bytes from opaque/absent entries, and refuse an archive that cannot
be preserved safely.

Release cases require exact selected/cancellation ownership and distinguish unreadable, missing,
recordless, failed, and truly vacant outcomes. Transaction cases cover preview, typed input/fetch
refusal, selected continue/cancel replay, release after cancellation, code-only versus incomplete
external pairs, and preservation of typed retry arguments.

### Invariants And Boundaries

- Selection authority is canonical source pair plus canonical master contract, never mere file presence.
- Only selecting or exact cancellation/terminal operations may repair or release the snapshot.
- Nonregular selector entries are quarantined without following them; unpreservable evidence blocks replacement.
- `skip-memory` or an otherwise incomplete external pair cannot advance selection to active.
- Retry guidance retains the exact memory choice and resolution action already supplied.

## Docs References

No Domain Documentation source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Pair/master/contract authority rejects noncanonical or mismatched identity. | `test_selected_and_cancel_owner_guards_require_exact_observation`; `test_record_identity_and_contract_authority_mismatches_fail_closed`; `test_loaded_contract_must_retain_pair_and_master_identity` | mcp/tests/test_atomic_series_activation_edges.py:161-179; mcp/tests/test_atomic_series_activation_edges.py:190-205; mcp/tests/test_atomic_series_activation_edges.py:208-228 |
| Archive and release edges distinguish preserved absence, opaque failure, unreadable state, and exact vacancy. | `test_archive_records_absence_and_refuses_unpreservable_entries`; `test_release_refuses_unreadable_missing_and_recordless_internal_calls`; `test_terminal_release_reports_failure_and_true_absence` | mcp/tests/test_atomic_series_activation_edges.py:240-273; mcp/tests/test_atomic_series_activation_edges.py:276-300; mcp/tests/test_atomic_series_activation_edges.py:303-324 |
| Selecting sync retains continue/cancel and incomplete-pair semantics. | `test_selected_sync_continue_cancel_replay_and_code_only_incomplete_pair`; `test_admission_refusal_preserves_typed_retry_arguments` | mcp/tests/test_atomic_series_activation_edges.py:346-406; mcp/tests/test_atomic_series_activation_edges.py:409-419 |
| Focused production owners separate selector storage, selection/release, terminal release, and sync-before-exposure. | `observe_atomic_series`; `release_atomic_series_selection`; `with_terminal_atomic_series_release`; `sync_selected_atomic_series_under_authority` | mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:170-187; mcp/src/agents_remember/worktrees/activation/atomic_series_activation_release.py:24-55; mcp/src/agents_remember/worktrees/activation/atomic_series_activation_terminal.py:17-65; mcp/src/agents_remember/worktrees/activation/atomic_series_activation_transaction.py:113-136 |

## Cross-Repo References

No cross-repository implementation source governs this focused suite.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History

- 2026-08-26T08:10+02:00 — Created strict onboarding for the frozen activation edge suite.
  Verification metadata remains empty until closeout can stamp a real code commit.