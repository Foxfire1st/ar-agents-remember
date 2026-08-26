# mcp/tests/test_sync_transaction_state_edges.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_sync_transaction_state_edges.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-26T08:10+02:00 |
| lastVerifiedCommitHash |  `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d`|
| lastVerifiedCommitDate |  2026-08-26T08:10:26+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Focused fail-closed coverage for the stable enclosure-root resumable-sync journal, its preserved
damage evidence, and its read-only public projection.

## Code Commentary

### Logic

The suite constructs strict side and operation records, then drives `SyncOperationStore` through
filesystem observation failures, malformed bytes, nonregular entries, idempotent archives, and
conflicting pre-existing archive evidence. It proves that malformed and quarantined journals
remain visible without being trusted, including exact requested-contract mismatch evidence.

The phase matrix covers running, retained code/memory resolution, cancellation, completion, and
cancelled projections. Only live/recoverable phases advertise contract-addressed continue/cancel
arguments; terminal phases do not. A nonregular journal and invalid closed model values fail
through the declared journal/model boundaries rather than being coerced.

### Invariants And Boundaries

- Journal damage is evidence to preserve or quarantine, never permission to infer lifecycle state.
- Raw archive retries are idempotent only when bytes and metadata agree exactly.
- Nonregular entries are classified without following or parsing them.
- A requested contract mismatch is explicit and offers only the safe exact cancel route.
- Projection state is derived from the stable journal, not task text or queue membership.

## Docs References

No Domain Documentation source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Store and archive edges preserve failures and reject conflicting evidence. | `test_store_translates_lstat_and_open_failures`; `test_raw_archive_is_idempotent_and_rejects_conflicting_evidence`; `test_opaque_archive_does_not_overwrite_existing_destination` | mcp/tests/test_sync_transaction_state_edges.py:89-106; mcp/tests/test_sync_transaction_state_edges.py:122-134; mcp/tests/test_sync_transaction_state_edges.py:163-167 |
| Observer coverage projects damaged, quarantined, active, and identity-mismatched journals. | `test_observer_projects_malformed_and_quarantined_journals`; `test_active_projection_covers_each_durable_phase`; `test_active_projection_fails_closed_on_requested_contract_mismatch` | mcp/tests/test_sync_transaction_state_edges.py:170-199; mcp/tests/test_sync_transaction_state_edges.py:213-238; mcp/tests/test_sync_transaction_state_edges.py:241-254 |
| The owning journal/store and projection implementation is the stable enclosure-root state module. | `SyncOperationStore`; `observe_sync_operation` | mcp/src/agents_remember/worktrees/sync_transaction_state.py:145-295; mcp/src/agents_remember/worktrees/sync_transaction_state.py:298-314 |

## Cross-Repo References

No cross-repository implementation source governs this focused suite.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History

- 2026-08-26T08:10+02:00 — Created strict onboarding for the frozen journal-state edge suite.
  Verification metadata remains empty until closeout can stamp a real code commit.
