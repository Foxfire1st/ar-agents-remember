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
pair plus sync log including actual `codeHeadTo`/`memoryHeadTo` produced heads for landing-chain merge admission, publishes the terminal journal first, then removes temporary worktrees and refs, and
finally (since MIK-R08) returns the completed result through `with_recomputed_worklist`.
`_require_completed_branches` proves each final branch head is the exact operation-created head, and
performs no ledger re-judgement: a completed memory side is proved as Git history, and the derived
`memory.md` it carries is left to the projection that rebuilds it.
`completed_sync_result` reconstructs success and distinguishes a current pair from moved-again or
explicit memory-skipped outcomes. `cancel_sync` first proves all-side ownership, then publishes cancelling, rolls back operation-owned output, returns every parked candidate, proves original contract bases, publishes cancelled and retires its stashes and authority.

**A completed sync recomputes the leaf's worklist (MIK-R08 rule 8, architect ruling 1).** The sync moved
the base pair, so B and K_B moved with it. `with_recomputed_worklist(result, contract)` calls
`recompute_knowledge_worklist(contract)` and, when it returns a summary, sets
`result.payload["knowledgeWorklist"]`; otherwise the result is untouched. `recompute_knowledge_worklist`
looks up the bound `WorktreeServices.knowledge_worklist` port, reloads the contract (which now holds the new
base pair) and calls `port.recompute`. The port lookup, the reload and the recompute sit inside one guard:
an unbound bundle or port, or **any** exception, returns `None`. Both `finalize_sync` and the `continue`
replay of a completed generation (`sync_transaction_results.terminal_resolution_replay`) use it, so both
report the worklist of the base pair the sync wrote. Since MIK-R66 the completed result also carries the
journaled crossing summaries (`successful_crossings`): the same `crossing_summary` view the resolution
response carries, so a successful sync reports its report identity and alignment counts too.

Unreadable or identity-invalid journals fail closed until explicit cancel. Cancellation first
archives exact raw bytes or an opaque nonregular entry. With no refs it writes terminal quarantine
and explicitly makes no heads-restored claim. With refs it reconstructs complete sides, proves
rollback, and cancels; partial authority restores only complete provable sides and returns bounded
manual-repair evidence for what remains. Missing journals follow the same ref-proof path. Terminal
cleanup is idempotent and republishes strict bytes after residue removal.

Cancellation prechecks every participating side before journal mutation, including pinned heads, live stash ownership and retained worktree/index fingerprints. Both assessment paths use the Git owner's one native reapply expectation; recovery adds no alternate merge result. Later and unproved work is saved in verified binary patches, paths and untracked mirrors before discard and cancelling. Successful cancellation names saved files/digests and deduplicates the assessments' native merge faults in its cancelled summary; unknown attribution is not adopted as transaction output. A save/readback failure returns sync-cancel-save-failed with the unchanged phase and cancel retry. A failure after saving but during discard returns sync-cancel-saved-discard-failed, retains the saved artifacts and directs cancel retry; it is not a promise that no earlier discard occurred. Neither later work nor a native merge fault alone imposes the retired refusal/resolve-and-continue route.

After all sides are proven, cancellation publishes cancelling, discards only attributable output, rolls heads back and restores every parked candidate, including already-restored sides. Terminal cancelled publication precedes `_retire_restored_stashes` and authority deletion. Completed-sync finalization has the same terminal-before-retirement boundary; terminal residue cleanup retries only exact owned resources. An interrupted cancellation keeps its stash authority for the next same action.

### Conventions

Archive evidence is preserved before repair. Manual repair payloads expose contract bases, observed
worktree/branch/MERGE_HEAD/ref facts, required proof checks, and the exact retry call, but no private
ambient inference.

### Invariants And Boundaries

- Terminal journal publication precedes deletion of recovery authority.
- The completed-branch proof is a Git proof: it never re-reads, or requires rows from, the ledger a
  completed memory side carries.
- Cancellation restores pinned pre-sync state; it may undo only the unfinished generation's proven finalized pair and exact trailing sync-log heads. Unrelated contract changes still refuse.
- Corrupt evidence is archived before quarantine or ref-based rollback.
- No-refs quarantine means usable terminal sync state, not a false rollback-success claim.
- Partial authority is preserved for manual repair; incomplete refs are not deleted wholesale.
- **The worklist recompute never fails a completed sync.** It runs after the terminal journal is
  published; nothing it does may change the completed result except adding the optional summary. With no
  port bound, or no worklist applicable (every unconverted leaf), the result is byte-for-byte unchanged.

## Parked-Candidate Recovery Ownership

`finalize_sync` refuses while parked work is unsettled. Cancel assesses both sides before touching either, then discards only operation-owned reapply output while its candidate remains in the kept stash. After rollback, every participating parked candidate is returned, including one already restored before the stop. A failed cancellation reapply reports `sync-cancel-wip-restore-failed` with stash and authority retained for recovery. No ordinary restore drops the stash before terminal publication.

### Todos

Nonregular-entry, cancellation, and recovery claims are reconciled to the frozen source;
commit-derived verification remains closeout-owned.

## Evidence

### Docs References

No external Domain Documentation entries are configured. Source and test assertions are distinguished from execution and acceptance evidence.

### Repo-Internal References

- The stable store archives raw or opaque journal evidence and projects quarantine. [1]

- Only terminal transactions retire their exact restored stashes. [10]

- Ref reconstruction and contract/base constraints come from the sync authority module. [2]


- Rollback proof is centralized in the Git module. [3]

- Finalization refuses while a side still parks its candidate, and cancellation clears a conflicted reapply, rolls back, and returns the parked candidate or reports a typed manual repair. [4]

- The completed result gains the recomputed worklist summary; every failure leaves it unchanged. [5]

- The completed-branch proof addresses only operation-created heads and reads no ledger rows. [6]

- A completed sync carries the journaled crossing summaries with their alignment counts. [7]

- All-side ownership prechecks precede cancelling journal mutation. [8]

- Save-first cancellation names actual saved files and digests; native merge faults explain failed attribution in the cancelled summary rather than forcing a later-work refusal. [9]

### Cross-Repo References

No additional configured cross-repository contract is asserted.
