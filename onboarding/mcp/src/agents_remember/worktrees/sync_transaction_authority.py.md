# mcp/src/agents_remember/worktrees/sync_transaction_authority.py

| Field | Value |
| --- | --- |
| verificationStatus | working-candidate |

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

## Evidence

### Docs References

No domain-documentation source is configured for this slice. The behavior described here is established by current repository source and the authorized LCA L9 change, rather than an invented external reference.

### Repo-Internal References

These current source spans identify the implementation owners and the specific assertions supporting the file's behavior. A test definition is evidence of its assertions, not an execution or certification receipt.

- Side planning and exact source-pair reads. [1]
- Pinned ref authority and reconstruction require exact identities. [2]
- Contract identity and base-transition constraints. [3]
- Parked-content restoration and settlement retain the exact stash until safe. [4]

### Cross-Repo References

The operation and fixture boundaries described here are defined by same-repository contracts and Git helpers. No separate cross-repository document is used as evidence for this card.
