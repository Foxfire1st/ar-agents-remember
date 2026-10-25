# mcp/src/agents_remember/worktrees/sync_transaction_authority.py

## Governing Overview

[Nearest governing route overview](overview.md)

## Purpose

Own the side plans, pinned refs, contract identity, base transitions, and parked-candidate completion facts for resumable source synchronization.

## Code Commentary

### Logic

`side_record` binds a code or memory side to its repository, source/work branches, pre-sync head, recorded base, deterministic base/pre-sync/source backup refs, and merge or fast-forward plan. Series sync uses temporary enclosure worktrees; leaves use their ordinary worktrees. `source_pair` resolves the named local source tips without consulting a ledger file or requiring a code-to-memory row.

Pinned refs are created, checked, reconstructed, and deleted by exact object identity. Journal-to-contract validation binds paths, task identity, kind, repositories, branches, and allowed base transitions. Finalization permits only the recorded old or admitted new bases; cancellation retains the original-base requirement.

The shared parked-WIP helpers prove restoration and retain the exact stash until the transaction is terminal. Genuine reapply conflicts retain the stash and resolution state. Settling a manually resolved reapply checks content conflicts, discards only memory-side cache changes, and leaves the real candidate uncommitted for its owning closeout.

A side can already hold the exact reapply after an interrupted restore or an edit the carried head already holds. `_skip_apply_proven` requires a live recorded stash and a complete successful proof before `_mark_restored` changes the journal; it does not reapply twice. Failed inventory remains failed even if the diagnostic sample is empty. `_unproven_restore_error` names at most ten failed paths inline, the remainder count, retained stash, cancel action and do-not-edit instruction; full named failures are logged and inventory incompleteness is disclosed. Each readable non-default carried-head merge rule appears beside its failed path. The refusal reconstructs Git's command/exit/reason only from its first ten named failures: `reapply_merge_fault` must need the lazy native merge on that sample and capture a fault. If those named paths use equality/base/simple-content cases, the refusal has no native-reason note even if a later failed path needed failed native acquisition. The full failed-name log does not make this inline diagnostic exhaustive. Cancellation instead carries faults actually captured by its own ownership assessments; neither path permits a plain-file fallback. This module presents the shared Git owner's result; it does not compute a second expectation.

A genuine conflict retains its stash and resolution phase. Fresh same-call reapply output is fingerprinted, while crash-window output earns capture only after exact scratch verification; an empty map preserves uncertainty rather than blessing owner edits. Stashes survive restore and manual settlement until terminal transaction publication. Cancellation proves the full stash inventory and restores stash^2 as the exact parked index before journaling restored, including retry and already-restored sides., so a crash after restoring one side cannot remove that side's only recoverable copy.

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

No external Domain Documentation entries are configured. Source and test assertions are distinguished from execution and acceptance evidence.

### Repo-Internal References

- Side planning and exact source-pair reads. [1]

- Pinned ref authority and reconstruction require exact identities. [2]

- Contract identity and base-transition constraints. [3]

- Parked-content restoration and settlement retain the exact stash until safe. [4]

- Restoration accepts only complete proven reapply and retains live stash authority. [5]

- Failed proof retains ten-inline/full-name-log, readable-rule, stash/cancel/no-edit boundaries; native command/exit/reason appears only when recomputing the named sample requires a native merge and captures a fault. [6]


- Cancellation restores already-restored sides and supports pre-sync reapply retry. [7]


### Cross-Repo References

No additional configured cross-repository contract is asserted.
