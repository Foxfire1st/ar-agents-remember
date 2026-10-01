# mcp/src/agents_remember/worktrees/sync_transaction_recovery.py

## Governing Overview

[worktrees overview](overview.md)

## Purpose

This file owns sync finalization, exact cancellation, terminal residue cleanup, and escape from
malformed, missing, or identity-invalid journals. It reports what can be proven and never claims
heads were restored when deterministic authority is absent or incomplete.

## Code Commentary

### Logic

`finalize_sync` re-reads and validates the contract and completed work branches, writes the new base
pair plus sync log, publishes the terminal journal first, then removes temporary worktrees and refs, and
finally (since MIK-R08) returns the completed result through `with_recomputed_worklist`.
`_require_completed_branches` proves each final branch head is the exact operation-created head, and
performs no ledger re-judgement: a completed memory side is proved as Git history, and the derived
`memory.md` it carries is left to the projection that rebuilds it.
`completed_sync_result` reconstructs success and distinguishes a current pair from moved-again or
explicit memory-skipped outcomes. `cancel_sync` publishes cancelling, rolls back only participating
operation-owned sides, returns every parked candidate, proves contract bases stayed original,
publishes cancelled, then deletes
authority.

**A completed sync recomputes the leaf's worklist (MIK-R08 rule 8, architect ruling 1).** The sync moved
the base pair, so B and K_B moved with it. `with_recomputed_worklist(result, contract)` calls
`recompute_knowledge_worklist(contract)` and, when it returns a summary, sets
`result.payload["knowledgeWorklist"]`; otherwise the result is untouched. `recompute_knowledge_worklist`
looks up the bound `WorktreeServices.knowledge_worklist` port, reloads the contract (which now holds the new
base pair) and calls `port.recompute`. The port lookup, the reload and the recompute sit inside one guard:
an unbound bundle or port, or **any** exception, returns `None`. Both `finalize_sync` and the `continue`
replay of a completed generation (`sync_transaction_results.terminal_resolution_replay`) use it, so both
report the worklist of the base pair the sync wrote.

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
- **The worklist recompute never fails a completed sync.** It runs after the terminal journal is
  published; nothing it does may change the completed result except adding the optional summary. With no
  port bound, or no worklist applicable (every unconverted leaf), the result is byte-for-byte unchanged.

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

## Evidence

### Docs References

No Domain Documentation source is configured for this memory root.

### Repo-Internal References

- The stable store archives raw or opaque journal evidence and projects quarantine. [1]
- Ref reconstruction and contract/base constraints come from the sync authority module. [2]
- Exact merge attribution and rollback proof are centralized in the Git module. [3]
- Finalization refuses while a side still parks its candidate, and cancellation clears a conflicted reapply, rolls back, and returns the parked candidate or reports a typed manual repair. [4]
- The completed result gains the recomputed worklist summary; every failure leaves it unchanged. [5]
- The completed-branch proof addresses only operation-created heads and reads no ledger rows. [6]

### Cross-Repo References

No cross-repository source is configured for this memory root.
