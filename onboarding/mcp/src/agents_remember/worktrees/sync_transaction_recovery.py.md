# mcp/src/agents_remember/worktrees/sync_transaction_recovery.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/sync_transaction_recovery.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-14T20:00+02:00 |
| lastVerifiedCommitHash |  `0da444b3b2b61f6a86fa4076b283c305db025d22`|
| lastVerifiedCommitDate |  2026-09-20T02:38:15+02:00|
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
| Ref reconstruction and contract/base constraints come from the sync authority module. | `side_record`; `require_record_contract` | mcp/src/agents_remember/worktrees/sync_transaction_authority.py:39-74; mcp/src/agents_remember/worktrees/sync_transaction_authority.py:206-220 |
| Exact merge attribution and rollback proof are centralized in the Git module. | `exact_created_head`; `rollback_side` | mcp/src/agents_remember/worktrees/sync_transaction_git.py:477-506; mcp/src/agents_remember/worktrees/sync_transaction_git.py:509-517 |
| Finalization refuses while a side still parks its candidate, and cancellation clears a conflicted reapply, rolls back, and returns the parked candidate or reports a typed manual repair. | `finalize_sync`; `cancel_sync`; "require_parked_wip_settled(record)"; "restore_cancelled_wip(store, record)" | mcp/src/agents_remember/worktrees/sync_transaction_recovery.py:56-92; mcp/src/agents_remember/worktrees/sync_transaction_recovery.py:159-190 |
| The completed-branch proof addresses only operation-created heads and reads no ledger rows. | `_require_completed_branches` | mcp/src/agents_remember/worktrees/sync_transaction_recovery.py:516-536 |

## Cross-Repo References

No cross-repository source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History
- 2026-09-20T00:16:01+00:00: Generated citation repair: `exact_created_head`; `rollback_side` repointed to mcp/src/agents_remember/worktrees/sync_transaction_git.py:509-517; mcp/src/agents_remember/worktrees/sync_transaction_git.py:477-506. No content impact: mechanical anchor-range projection bound to citation source snapshot b8fe5b3589f1357e836aaad1587e69ed38bbda0d58221eaa2150e96eb0561e93; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-17T08:11:27+00:00 — 260915-KS-L9 curator (memory-quality closure): re-read every reopened claim in this card against code commit `c22beb0121946c0637e113ec4cf29da29fd4aec7` and advanced the verification stamp to that commit, which closeout re-stamps. A generated citation repair had already rewritten these ranges mechanically, so each was re-read rather than trusted: the range was checked against the current definition of the construct the claim is about, and the wording still holds. Extents chosen: `exact_created_head`; `rollback_side` at mcp/src/agents_remember/worktrees/sync_transaction_git.py:459-488; mcp/src/agents_remember/worktrees/sync_transaction_git.py:491-499.
- 2026-09-17T07:33:51+00:00: Generated citation repair: `side_record`; `require_record_contract` repointed to mcp/src/agents_remember/worktrees/sync_transaction_authority.py:39-74; mcp/src/agents_remember/worktrees/sync_transaction_authority.py:206-220. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T07:33:51+00:00: Generated citation repair: `exact_created_head`; `rollback_side` repointed to mcp/src/agents_remember/worktrees/sync_transaction_git.py:491-499; mcp/src/agents_remember/worktrees/sync_transaction_git.py:459-488. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-17T03:31:11+02:00 — 260915-KS-L9 curator (re-scoped repair): added mcp/src/agents_remember/worktrees/sync_transaction_git.py:459 to the row 91 of this card as the citation for `rollback_side`: no cited file carried the construct, and the checker named line(s) [459] in this file as its live location; added mcp/src/agents_remember/worktrees/sync_transaction_authority.py:39 to the row 90 of this card as the citation for `side_record`: no cited file carried the construct, and the checker named line(s) [39] in this file as its live location
- 2026-09-17T03:31:11+02:00 — 260915-KS-L9 curator (re-scoped repair): re-pointed `rollback_side` in the row 91 of this card from mcp/src/agents_remember/worktrees/sync_transaction_git.py:491-492 to mcp/src/agents_remember/worktrees/sync_transaction_git.py:459-460, the extent of the construct the claim is about (the checker named line(s) [459] as its live location); re-pointed `side_record` in the row 90 of this card from mcp/src/agents_remember/worktrees/sync_transaction_authority.py:206-207 to mcp/src/agents_remember/worktrees/sync_transaction_authority.py:39-43, the extent of the construct the claim is about (the checker named line(s) [39] as its live location)
- 2026-09-17T03:31:11+02:00 — 260915-KS-L9 curator (re-scoped repair): re-pointed `exact_created_head` in the row 91 of this card from mcp/src/agents_remember/worktrees/sync_transaction_git.py:459-460 to mcp/src/agents_remember/worktrees/sync_transaction_git.py:491-492, the extent of the construct the claim is about (the checker named line(s) [278, 385, 408] as its live location); re-pointed `require_record_contract` in the row 90 of this card from mcp/src/agents_remember/worktrees/sync_transaction_authority.py:39-43 to mcp/src/agents_remember/worktrees/sync_transaction_authority.py:206-207, the extent of the construct the claim is about (the checker named line(s) [206, 237] as its live location)
- 2026-09-17T03:31:11+02:00 — 260915-KS-L9 curator (re-scoped repair): re-read the reopened claim in the row 91 of this card against the current code: its anchor still resolves inside the cited range, so the wording holds and the stamp advances
- 2026-09-17T03:31:11+02:00 — 260915-KS-L9 curator (re-scoped repair): clamped mcp/src/agents_remember/worktrees/sync_transaction_authority.py:425 to mcp/src/agents_remember/worktrees/sync_transaction_authority.py:424, the range the cited construct now occupies; kept one copy of the repeated citation mcp/src/agents_remember/worktrees/sync_transaction_authority.py:206-207 in the row 90 of this card; the repetition added no pooled evidence; kept one copy of the repeated citation mcp/src/agents_remember/worktrees/sync_transaction_git.py:491-492 in the row 91 of this card; the repetition added no pooled evidence
- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator (drift re-verification): the removed
  `validate_completed_side` call is the frozen change and the earlier entries record it. Re-checked
  `_require_completed_branches` `:516-536`: it holds. No wording changed. Verification metadata
  remains closeout-owned.
- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator (drift re-verification):
  `mcp/src/agents_remember/worktrees/sync_transaction_recovery.py` changed since the recorded
  verification commit. Re-read the card against the frozen on-disk source and re-checked its claims
  and cited ranges: nothing this card asserts is falsified by the change, so no wording changed.
  Verification metadata remains closeout-owned; no verification stamp advanced.
- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (drift re-verification): the source moved since
  the recorded verification commit (the `validate_completed_side` call and import were removed).
  Re-read the card against the current source: the card already records that removal, and the cited
  `_require_completed_branches` range (516-536) still holds. No wording changed; verification
  metadata remains closeout-owned.
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
