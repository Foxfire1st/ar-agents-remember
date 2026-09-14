# mcp/src/agents_remember/worktrees/sync_transaction_authority.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/sync_transaction_authority.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-14T19:00+02:00 |
| lastVerifiedCommitHash |  `bb65a2073228c5e143b055a470f39c6c9e2f4d9d`|
| lastVerifiedCommitDate |  2026-09-14T19:36:04+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[worktrees overview](overview.md)

## Purpose

This file owns admission and identity authority for resumable source synchronization: exact side
locations/plans, official code-memory pair validation, pinned refs, journal-to-contract identity,
finalization/cancellation preconditions, and common response evidence.

## Code Commentary

### Logic

`side_record` binds one code or memory side to repository, operation worktree, source/work branch,
admitted source commit, pre-sync head, recorded base, three deterministic backup refs, and a plan.
Series sync uses temporary enclosure `.sync` worktrees; leaves use their ordinary worktrees.
`preflight_official_pair` reads `memory.md` at the admitted official memory tip and requires a
newest current mapping for the admitted code tip before mutation. Older same-code rows remain valid
history.

`pin_authority`, `require_pinned_authority`, and `delete_authority` manage exact base/pre-sync/source
refs. Recovery reconstructs a side only when all three exist. Contract validation binds journal
path, task id, kind, repositories, worktrees, and branches; finalization additionally constrains
base transitions, while cancellation requires original bases. Shared helpers update the journal and
shape side/result payloads without changing authority.

### Conventions

Git authority uses full commit ids and compare-exact refs. Source pair means local protected branch
tips; upstream fetch evidence lives elsewhere. Missing one member of a recovery-ref triple is an
error, not partial success.

### Invariants And Boundaries

- External-memory admission requires the newest valid ledger mapping for the exact code tip; global
  code-key uniqueness is not an admission rule.
- Journal identity cannot be rebound to another contract, repository, branch, or worktree.
- All participating refs are pinned before the journaled mutation proceeds.
- Cleanup deletes refs only when they still equal the admitted commits.
- This module does not infer authority from queue state or ambient checkout position.

## Parked-Candidate Restore Authority

The shared restore helpers live here so the driver, the recovery owner, and the read-only previews
never re-implement the proof. `restore_parked_wip` returns one side's parked candidate to its
worktree and journals the outcome: a clean reapply is proven restored before the stash entry is
dropped and `wipState` becomes `restored`; a conflicted one becomes the retained
`*-resolution-required` state with `wipState="restore-conflict"`, the exact `conflictFiles`, and the
stash kept — and its third return value tells the caller not to advance that side.
`restore_cancelled_wip` reapplies every still-parked candidate after the rollback restored the
pinned pre-sync heads. `settle_resolved_parked_wip` closes a conflict the agent resolved in the
worktree: it refuses while any unmerged path remains, then retires the stash entry without
committing, so the resolved candidate stays uncommitted for the closeout that owns it.
`require_parked_wip_settled` is the finalization safety net.

`side_payload` gained one conditional `wip` block (`state`, `paths`, `pathCount`) for any side that
parked something; sides that parked nothing emit no `wip` key, so an ordinary side's payload is
unchanged. `resolution_phase` centralises the `code-resolution-required` /
`memory-resolution-required` phase name both restore and merge callers use.

### Todos

Authority and result-state claims are reconciled to the frozen source; verification metadata awaits
the real code commit.

## Docs References

No Domain Documentation source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The journal models store every side identity and deterministic ref used here. | `SyncSideRecord`; `SyncOperationRecord`; `sync_side_refs` | mcp/src/agents_remember/worktrees/sync_transaction_state.py:41-67; mcp/src/agents_remember/worktrees/sync_transaction_state.py:70-87; mcp/src/agents_remember/worktrees/sync_transaction_state.py:159-161 |
| Exact ref, checkout, merge, and rollback proof is centralized in the Git module. | `create_pinned_ref`; `require_side_checkout`; `start_side_merge`; `rollback_side` | mcp/src/agents_remember/worktrees/sync_transaction_git.py:52-61; mcp/src/agents_remember/worktrees/sync_transaction_git.py:93-99; mcp/src/agents_remember/worktrees/sync_transaction_git.py:264-301; mcp/src/agents_remember/worktrees/sync_transaction_git.py:375-403 |
| The driver admits and advances only after this authority preflight succeeds. | `sync_contract_under_authority` | mcp/src/agents_remember/worktrees/sync_transaction.py:82-110 |
| The shared parked-candidate restore helpers prove a clean reapply, retain a conflicted one, return the candidate after cancellation, and refuse finalization while one is parked. | `restore_parked_wip`; `restore_cancelled_wip`; `settle_resolved_parked_wip`; `require_parked_wip_settled` | mcp/src/agents_remember/worktrees/sync_transaction_authority.py:356-395; mcp/src/agents_remember/worktrees/sync_transaction_authority.py:398-417; mcp/src/agents_remember/worktrees/sync_transaction_authority.py:420-440; mcp/src/agents_remember/worktrees/sync_transaction_authority.py:443-450 |
| The shared side payload emits the parked-candidate projection only for a side that parked one, and the resolution phase names are centralised. | `side_payload`; `resolution_phase` | mcp/src/agents_remember/worktrees/sync_transaction_authority.py:329-349; mcp/src/agents_remember/worktrees/sync_transaction_authority.py:352-353 |

## Cross-Repo References

No cross-repository source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History

- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (citation pass): re-derived the source ranges of 2
  claim(s) whose anchor no longer sat in its cited range and normalised 0 further range(s) in this
  card from their anchors against the frozen source snapshot (`agents-remember memory-citations
  --fix --document`, snapshot 188b8ecd). No claim wording changed; every rewritten range was read
  back at its current position. Verification metadata remains closeout-owned.
- 2026-09-11T23:05:00+00:00: Curator citation reconciliation: `SyncOperationRecord`, `SyncSideRecord`, `sync_side_refs` repointed to mcp/src/agents_remember/worktrees/sync_transaction_state.py:159-161, mcp/src/agents_remember/worktrees/sync_transaction_state.py:41-67, mcp/src/agents_remember/worktrees/sync_transaction_state.py:70-87. No content impact: mechanical anchor-range projection against citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged.

- 2026-09-10T15:06+02:00 — Parked-candidate restore authority: recorded the four shared restore helpers, the conditional `wip` side projection, and the centralised resolution phase names; re-derived every cited range against the current working tree. Verification remains closeout-owned.

- 2026-08-26T14:32+02:00 — Corrected official source-pair admission to use newest-first current
  mapping authority while accepting retained same-code memory history. Verification remains
  closeout-owned.

- 2026-08-26T08:20+02:00 — Final frozen reconciliation of source-pair, ledger, contract, and
  pinned-ref admission authority.

- 2026-08-26T02:55+02:00 — Drafted strict sync-authority onboarding; final source freeze and
  verification remain open.