# mcp/src/agents_remember/worktrees/sync_transaction_recovery.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/sync_transaction_recovery.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-10T15:06+02:00 |
| lastVerifiedCommitHash |  `7833df0b219bba560f67f6e1158c3f4f155e1ce6`|
| lastVerifiedCommitDate |  2026-08-26T15:02:28+02:00|
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
| The stable store archives raw or opaque journal evidence and projects quarantine. | `SyncOperationStore`; `_quarantined_sync_projection` | mcp/src/agents_remember/worktrees/sync_transaction_state.py:155-305; mcp/src/agents_remember/worktrees/sync_transaction_state.py:349-369 |
| Ref reconstruction and contract/base constraints come from the sync authority module. | `side_record`; `require_record_contract` | mcp/src/agents_remember/worktrees/sync_transaction_authority.py:44-79; mcp/src/agents_remember/worktrees/sync_transaction_authority.py:246-260 |
| Exact merge attribution and rollback proof are centralized in the Git module. | `exact_created_head`; `rollback_side` | mcp/src/agents_remember/worktrees/sync_transaction_git.py:369-397; mcp/src/agents_remember/worktrees/sync_transaction_git.py:400-408 |
| Finalization refuses while a side still parks its candidate, and cancellation clears a conflicted reapply, rolls back, and returns the parked candidate or reports a typed manual repair. | `finalize_sync`; `cancel_sync`; `require_parked_wip_settled`; `restore_cancelled_wip` | mcp/src/agents_remember/worktrees/sync_transaction_recovery.py:57-93; mcp/src/agents_remember/worktrees/sync_transaction_recovery.py:160-191; mcp/src/agents_remember/worktrees/sync_transaction_authority.py:443-450; mcp/src/agents_remember/worktrees/sync_transaction_authority.py:398-417 |

## Cross-Repo References

No cross-repository source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History

- 2026-09-10T15:06+02:00 — Parked-candidate recovery ownership: recorded `require_parked_wip_settled` in `finalize_sync` and the cancel path that clears a conflicted reapply, rolls back, and returns the parked candidate (or reports `sync-cancel-wip-restore-failed`). Re-derived the store/authority/Git anchors against the current working tree. Verification remains closeout-owned.

- 2026-08-26T08:20+02:00 — Final frozen reconciliation of cancellation, finalization,
  malformed/nonregular journal recovery, and partial-authority manual repair.

- 2026-08-26T02:55+02:00 — Drafted finalization, cancellation, quarantine, and manual-repair
  onboarding; post-Dagger reconciliation and verification remain open.