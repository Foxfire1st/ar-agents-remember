# mcp/src/agents_remember/worktrees/sync_transaction_state.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/sync_transaction_state.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-26T08:30+02:00 |
| lastVerifiedCommitHash |  `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d`|
| lastVerifiedCommitDate |  2026-08-26T08:10:26+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[worktrees overview](overview.md)

## Purpose

This file defines and stores the strict stable state for one resumable worktree-sync generation.
The journal lives below the enclosure root so status, continuation, cancellation, and damage
recovery do not depend on a readable task document or queue projection.

## Code Commentary

### Logic

`SyncSideRecord` binds each participating side to exact repositories/worktrees/branches, admitted
source/pre-sync/base commits, three authority refs, plan, progress, result head, and conflicts.
`SyncOperationRecord` records one generation, canonical contract/task/kind, original bases, phase,
memory policy, both sides, and timestamps. `SyncQuarantineRecord` is terminal proof that corrupt
evidence was archived without rollback authority. The store path is always
`.lifecycle/sync-operation.json`; authority refs derive from a hash of the contract path.

`SyncOperationStore` strictly lstat/opens without following nonregular entries, parses only operation
or quarantine records, writes atomically, preserves raw malformed bytes, and can atomically archive
opaque directory/symlink/other entries with bounded metadata. `observe_sync_operation` projects
malformed, quarantined, identity-mismatched, conflict, cancelling, terminal, or resumable state with
contract-addressed next/cancel arguments and without parsing task truth.

### Conventions

Models are frozen and reject extra fields. The store is single-record; repository integration
authority serializes writers. Observation is total and read-only, while archival happens only in
explicit recovery.

### Invariants And Boundaries

- Stable lifecycle state is at the enclosure root, not in task or queue files.
- Nonregular or malformed journal entries never become normal operation records.
- Raw/opaque evidence is preserved before replacement; quarantine is explicit terminal vocabulary.
- Identity mismatch points cancellation at the locator-proven requested contract and exposes the
  journal path separately.
- The public projection omits private authority refs and commit-detail internals.

### Todos

Final nonregular handling and public model fields are reconciled to the frozen source;
commit-derived verification remains closeout-owned.

## Docs References

No Domain Documentation source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The driver treats this store as the sole current generation and routes recovery from its strict outcomes. | `_read_sync_record`; `_route_sync_record` | mcp/src/agents_remember/worktrees/sync_transaction.py:103-141; mcp/src/agents_remember/worktrees/sync_transaction.py:144-164 |
| Recovery archives damaged entries, writes quarantine, or reconstructs cancellation from refs. | `cancel_sync`; `recover_unreadable_journal`; `recover_missing_journal` | mcp/src/agents_remember/worktrees/sync_transaction_recovery.py:156-181; mcp/src/agents_remember/worktrees/sync_transaction_recovery.py:184-254; mcp/src/agents_remember/worktrees/sync_transaction_recovery.py:257-274 |
| Public status embeds this journal projection without moving its authority into task/queue state. | `worktree_status_packet` | mcp/src/agents_remember/application/worktree_status.py:46-128 |

## Cross-Repo References

No cross-repository source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History

- 2026-08-26T08:30+02:00 — Rebounded the public status citation to the frozen status projection
  implementation after final structural consolidation.

- 2026-08-26T08:20+02:00 — Final frozen reconciliation of stable journal storage,
  nonregular/raw archive evidence, quarantine, and public phase projection.

- 2026-08-26T02:55+02:00 — Drafted stable journal/store/status onboarding against the pre-Dagger
  candidate; final fields, citations, and verification remain open.