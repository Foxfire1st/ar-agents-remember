# mcp/src/agents_remember/worktrees/sync_transaction_recovery.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/sync_transaction_recovery.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-14T13:20+02:00 |
| lastVerifiedCommitHash |  `3b552f5a215648274dc5e6e4d5f0a01c2ee80be2`|
| lastVerifiedCommitDate |  2026-09-12T01:54:48+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[worktrees overview](overview.md)

## Purpose

This file owns sync finalization, exact cancellation, terminal residue cleanup, and escape from
malformed, missing, or identity-invalid journals. It reports what can be proven and never claims
heads were restored when deterministic authority is absent or incomplete.

## Code Commentary

### Logic

`finalize_sync` re-reads and validates the contract and completed work branches, writes the new base
pair plus sync log, publishes the terminal journal first, then removes temporary worktrees and refs.
`_require_completed_branches` proves each final branch head is the exact operation-created head, and
performs no ledger re-judgement: a completed memory side is proved as Git history, and the derived
`memory.md` it carries is left to the projection that rebuilds it.
`completed_sync_result` reconstructs success and distinguishes a current pair from moved-again or
explicit memory-skipped outcomes. `cancel_sync` publishes cancelling, rolls back only participating
operation-owned sides, returns every parked candidate, proves contract bases stayed original,
publishes cancelled, then deletes
authority.

Unreadable or identity-invalid journals fail closed until explicit cancel. Cancellation first
archives exact raw bytes or an opaque nonregular entry. With no refs it writes terminal quarantine
and explicitly makes no heads-restored claim. With refs it reconstructs complete sides, proves
rollback, and cancels; partial authority restores only complete provable sides and returns bounded
manual-repair evidence for what remains. Missing journals follow the same ref-proof path. Terminal
cleanup is idempotent and republishes strict bytes after residue removal.

### Conventions

Archive evidence is preserved before repair. Manual repair payloads expose contract bases, observed
worktree/branch/MERGE_HEAD/ref facts, required proof checks, and the exact retry call, but no private
ambient inference.

### Invariants And Boundaries

- Terminal journal publication precedes deletion of recovery authority.
- The completed-branch proof is a Git proof: it never re-reads, or requires rows from, the ledger a
  completed memory side carries.
- Cancellation restores only the exact pinned pre-sync state and refuses changed contract bases.
- Corrupt evidence is archived before quarantine or ref-based rollback.
- No-refs quarantine means usable terminal sync state, not a false rollback-success claim.
- Partial authority is preserved for manual repair; incomplete refs are not deleted wholesale.

## Parked-Candidate Recovery Ownership

`finalize_sync` calls `require_parked_wip_settled(record)` after the completed-branch proof: it
refuses to finalize while any participating side still parks the candidate it carries, so a carry
cannot terminate with the WIP stranded in the stash. `cancel_sync` gains the mirror duty. For a side
in `restore-conflict` it first calls `discard_conflicted_wip_reapply` to clear the conflicted
reapply (the candidate itself is still safe in its stash), then runs the existing pinned-ref
rollback, then `restore_cancelled_wip` reapplies the candidate onto the restored pre-sync head and
drops the stash. If that reapply cannot be proven, cancellation returns
`sync-cancel-wip-restore-failed` as a manual repair with the stash kept and the pinned refs not
deleted.

### Todos

Nonregular-entry, cancellation, and recovery claims are reconciled to the frozen source;
commit-derived verification remains closeout-owned.

## Docs References

No Domain Documentation source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The stable store archives raw or opaque journal evidence and projects quarantine. | `SyncOperationStore`; `_quarantined_sync_projection` | mcp/src/agents_remember/worktrees/sync_transaction_state.py:172-366; mcp/src/agents_remember/worktrees/sync_transaction_state.py:410-430 |
| Ref reconstruction and contract/base constraints come from the sync authority module. | `side_record`; `require_record_contract` | mcp/src/agents_remember/worktrees/sync_transaction_authority.py:44-79; mcp/src/agents_remember/worktrees/sync_transaction_authority.py:246-260 |
| Exact merge attribution and rollback proof are centralized in the Git module. | `exact_created_head`; `rollback_side` | mcp/src/agents_remember/worktrees/sync_transaction_git.py:406-414; mcp/src/agents_remember/worktrees/sync_transaction_git.py:375-403 |
| Finalization refuses while a side still parks its candidate, and cancellation clears a conflicted reapply, rolls back, and returns the parked candidate or reports a typed manual repair. | `finalize_sync`; `cancel_sync`; "require_parked_wip_settled(record)"; "restore_cancelled_wip(store, record)" | mcp/src/agents_remember/worktrees/sync_transaction_recovery.py:56-92; mcp/src/agents_remember/worktrees/sync_transaction_recovery.py:159-190; mcp/src/agents_remember/worktrees/sync_transaction_authority.py:443-450; mcp/src/agents_remember/worktrees/sync_transaction_authority.py:398-417 |
| The completed-branch proof addresses only operation-created heads and reads no ledger rows. | `_require_completed_branches` | mcp/src/agents_remember/worktrees/sync_transaction_recovery.py:516-536 |

## Cross-Repo References

No cross-repository source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History
- 2026-09-14T13:20+02:00 — The ledger ruling reaches the completed-branch proof:
  `_require_completed_branches` no longer calls `validate_completed_side`, so finalization proves each
  final head is the exact operation-created head and reads no ledger rows from the memory side it
  completes. Recorded that in Logic and as a local invariant, added its reference row, and re-derived
  the `finalize_sync`/`cancel_sync` and Git-module anchors against the current source. Verification
  remains closeout-owned.
- 2026-09-11T23:05:00+00:00: The recovery row anchored `require_parked_wip_settled` and `restore_cancelled_wip` as bare symbols; each now resolves three times across the cited files (import and call in `sync_transaction_recovery.py`, definition in `sync_transaction_authority.py`), so the claim could not be compared with its provenance. Those two anchors are now the exact call texts `require_parked_wip_settled(record)` and `restore_cancelled_wip(store, record)`, each occurring once in the cited recovery extents; `finalize_sync`, `cancel_sync`, both cited extents, and the claim's wording are unchanged.
- 2026-09-11T23:05:00+00:00: Curator citation reconciliation: `SyncOperationStore`, `_quarantined_sync_projection` repointed to mcp/src/agents_remember/worktrees/sync_transaction_state.py:172-366, mcp/src/agents_remember/worktrees/sync_transaction_state.py:410-430. No content impact: mechanical anchor-range projection against citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged.

- 2026-09-10T15:06+02:00 — Parked-candidate recovery ownership: recorded `require_parked_wip_settled` in `finalize_sync` and the cancel path that clears a conflicted reapply, rolls back, and returns the parked candidate (or reports `sync-cancel-wip-restore-failed`). Re-derived the store/authority/Git anchors against the current working tree. Verification remains closeout-owned.

- 2026-08-26T08:20+02:00 — Final frozen reconciliation of cancellation, finalization,
  malformed/nonregular journal recovery, and partial-authority manual repair.

- 2026-08-26T02:55+02:00 — Drafted finalization, cancellation, quarantine, and manual-repair
  onboarding; post-Dagger reconciliation and verification remain open.