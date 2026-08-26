# mcp/src/agents_remember/worktrees/sync_transaction_recovery.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/sync_transaction_recovery.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-26T08:20+02:00 |
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
operation-owned sides, proves contract bases stayed original, publishes cancelled, then deletes
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
| The stable store archives raw or opaque journal evidence and projects quarantine. | `SyncOperationStore`; `_quarantined_sync_projection` | mcp/src/agents_remember/worktrees/sync_transaction_state.py:145-295; mcp/src/agents_remember/worktrees/sync_transaction_state.py:339-359 |
| Ref reconstruction and contract/base constraints come from the sync authority module. | `side_record`; `require_record_contract` | mcp/src/agents_remember/worktrees/sync_transaction_authority.py:39-74; mcp/src/agents_remember/worktrees/sync_transaction_authority.py:241-255 |
| Exact merge attribution and rollback proof are centralized in the Git module. | `exact_created_head`; `rollback_side` | mcp/src/agents_remember/worktrees/sync_transaction_git.py:251-279; mcp/src/agents_remember/worktrees/sync_transaction_git.py:282-290 |

## Cross-Repo References

No cross-repository source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History

- 2026-08-26T08:20+02:00 — Final frozen reconciliation of cancellation, finalization,
  malformed/nonregular journal recovery, and partial-authority manual repair.

- 2026-08-26T02:55+02:00 — Drafted finalization, cancellation, quarantine, and manual-repair
  onboarding; post-Dagger reconciliation and verification remain open.