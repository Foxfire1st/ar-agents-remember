# mcp/src/agents_remember/worktrees/sync_transaction_authority.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/sync_transaction_authority.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T01:15+00:00 |
| lastVerifiedCommitHash | `14582854955223f75588c23c9f29f9d51bde9675` |
| lastVerifiedCommitDate | 2026-09-18T09:05:03+02:00|
| verificationStatus | working-candidate |
| governingOverview | `overview.md` |

The body describes the uncommitted LCA L9 working candidate. The commit fields identify the latest real commit touching this source file; they do not claim that the candidate is committed or accepted.

## Governing Overview

[Nearest governing route overview](overview.md)

## Purpose

Own the side plans, pinned refs, contract identity, base transitions, and parked-candidate completion facts for resumable source synchronization.

## Code Commentary

### Logic

`side_record` binds a code or memory side to its repository, source/work branches, pre-sync head, recorded base, deterministic base/pre-sync/source backup refs, and merge or fast-forward plan. Series sync uses temporary enclosure worktrees; leaves use their ordinary worktrees. `source_pair` resolves the named local source tips without consulting a ledger file or requiring a code-to-memory row.

Pinned refs are created, checked, reconstructed, and deleted by exact object identity. Journal-to-contract validation binds paths, task identity, kind, repositories, branches, and allowed base transitions. Finalization permits only the recorded old or admitted new bases; cancellation retains the original-base requirement.

The shared parked-WIP helpers restore the candidate before dropping its exact stash. Genuine reapply conflicts retain the stash and resolution state. Settling a manually resolved reapply checks content conflicts, discards only memory-side cache changes, and leaves the real candidate uncommitted for its owning closeout.

### Conventions

The base/pre-sync/source ref triple is recovery authority, not a third delivered commit. Shared side payloads expose WIP details only for sides that actually parked content.

### Invariants And Boundaries

- Journal identity cannot be rebound to another contract or repository.
- All participating authority refs remain exact; partial ref triples are errors.
- Missing memory attribution is informational and does not make source sync mid-cycle.
- Cache-only conflict/index state is excluded from parked-content completion; real unresolved content remains a blocker.

### Todos

No new file-local follow-up is identified by this source reconciliation.

## Docs References

No domain-documentation source is configured for this slice. The behavior described here is established by current repository source and the authorized LCA L9 change, rather than an invented external reference.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

These current source spans identify the implementation owners and the specific assertions supporting the file's behavior. A test definition is evidence of its assertions, not an execution or certification receipt.

| Finding | Anchor | Source |
| --- | --- | --- |
| Side planning and exact source-pair reads. | `side_record`; `source_pair` | mcp/src/agents_remember/worktrees/sync_transaction_authority.py:39-75; mcp/src/agents_remember/worktrees/sync_transaction_authority.py:110-118 |
| Pinned ref authority and reconstruction require exact identities. | `pin_authority`; `require_pinned_authority` | mcp/src/agents_remember/worktrees/sync_transaction_authority.py:121-126; mcp/src/agents_remember/worktrees/sync_transaction_authority.py:129-143 |
| Contract identity and base-transition constraints. | `require_record_contract`; `require_contract_bases_unchanged` | mcp/src/agents_remember/worktrees/sync_transaction_authority.py:206-220; mcp/src/agents_remember/worktrees/sync_transaction_authority.py:245-252 |
| Parked-content restoration and settlement retain the exact stash until safe. | `restore_parked_wip`; `settle_resolved_parked_wip` | mcp/src/agents_remember/worktrees/sync_transaction_authority.py:316-356; mcp/src/agents_remember/worktrees/sync_transaction_authority.py:380-401 |

## Cross-Repo References

The operation and fixture boundaries described here are defined by same-repository contracts and Git helpers. No separate cross-repository document is used as evidence for this card.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History
2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.

- 2026-09-15T01:15+00:00 — 260913-LCA-L9 working candidate: Removed official-pair ledger admission and connected parked-candidate settlement to memory-domain content conflict handling while retaining pinned-ref and contract/base proof. Current source and citation targets were checked; the metadata records the last real file commit, and candidate changes remain uncommitted.

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
