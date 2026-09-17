# mcp/src/agents_remember/worktrees/sync_transaction_authority.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/sync_transaction_authority.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T01:15+00:00 |
| lastVerifiedCommitHash | `ea9cf0abeab4fe88961bda10b4f54d30266a9634` |
| lastVerifiedCommitDate | 2026-09-17T23:56:19+02:00|
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
| Side planning and exact source-pair reads. | n/a | [mcp/src/agents_remember/worktrees/sync_transaction_authority.py](mcp/src/agents_remember/worktrees/sync_transaction_authority.py) |
| Pinned ref authority and reconstruction require exact identities. | n/a | [mcp/src/agents_remember/worktrees/sync_transaction_authority.py](mcp/src/agents_remember/worktrees/sync_transaction_authority.py) |
| Contract identity and base-transition constraints. | n/a | [mcp/src/agents_remember/worktrees/sync_transaction_authority.py](mcp/src/agents_remember/worktrees/sync_transaction_authority.py) |
| Parked-content restoration and settlement retain the exact stash until safe. | n/a | [mcp/src/agents_remember/worktrees/sync_transaction_authority.py](mcp/src/agents_remember/worktrees/sync_transaction_authority.py) |

## Cross-Repo References

The operation and fixture boundaries described here are defined by same-repository contracts and Git helpers. No separate cross-repository document is used as evidence for this card.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History

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
