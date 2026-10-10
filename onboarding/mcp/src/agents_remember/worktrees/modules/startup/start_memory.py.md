# mcp/src/agents_remember/worktrees/modules/startup/start_memory.py

## Governing Overview

[Nearest governing route overview](../overview.md)

## Purpose

Own external-memory admission/preparation and truthful named-ref facts during worktree start.

## Code Commentary

`prepare_memory_for_start` first settles disabled/external repository availability. Ordinary apply/default use calls `_ensure_memory_source_branch`, requiring the exact task-derived protected source ref; this owner creates no source branch.

Only explicit dry run carrying an admitted unpublished, non-symlink parent may report the exact source ref `would-create`, and only when that named ref is actually absent. A partial bootstrap journal may already own the ref while its parent contract is unpublished: then the original named-ref helper returns `existing`. Contract absence and ref absence are distinct facts. The planned base commit remains the owner's validated readable input; no fallback or guessed source is selected.

Ledger response metadata comes from `derive_memory_ledger` at that recorded base and remains informational. The existing worktree/mTime preparation keeps its dry-run boundary: no worktree creation or mTime synchronization. Divergent/missing source paths retain existing explicit indexing/mTime behavior. Generic ambient tool-completion logging is outside this startup-owned no-materialization claim.

### Logic

`prepare_memory_for_start` settles internal, disabled, or external memory, requires the exact configured memory source branch, and creates or reuses the memory worktree. Its `lastVerifiedCodeCommit` and `lastMemoryContentCommit` response data come from `derive_memory_ledger` at the recorded memory base. An unattributed history produces empty informational values; a missing, stale, or malformed cached `memory.md` is not an admission condition.

Mtime reuse skips `.git`, non-files, missing source files, and known divergent paths. Missing source files are counted. A computable source/worktree diff leaves changed paths fresh for indexing; an uncomputable diff is explicitly reported. Dry-run does not create a worktree or synchronize mtimes.

### Conventions

Named branch and repository facts establish the memory source. The existing disabled-memory choice remains explicit; this module does not create a substitute protected source branch.

### Invariants And Boundaries

- The memory repository and exact source branch must exist for an external-memory start.
- Cache rows never select the code base or establish compatibility.
- Derived metadata reports only committed attribution; it does not invent a mapping for the selected code base.
- Worktree creation and mtime handling retain their existing dry-run boundary.

### Todos

No new file-local follow-up is identified by this source reconciliation.

## Evidence

No Domain Documentation source is configured in system/sources.md. These are current source/assertion anchors; the approved requirement and bound public receipts remain task artifacts.


- Preview facts distinguish absent exact refs from existing journal-owned refs. [5]
- Ordinary default/apply requires the exact named ref and writes none. [6]
- Dry run skips mTime mutation; divergence remains explicit. [7]

### Docs References

No domain-documentation source is configured for this slice. The behavior described here is established by current repository source and the authorized LCA L9 change, rather than an invented external reference.

### Repo-Internal References

These current source spans identify the implementation owners and the specific assertions supporting the file's behavior. A test definition is evidence of its assertions, not an execution or certification receipt.

- Source state, named-branch admission, and informational Git-derived metadata. [8]
- Mtime reuse and divergence handling preserve the current indexing behavior. [9]
- Missing external repository and explicit disabled-memory outcomes. [10]
- The informational ledger is reconstructed from commit attribution without a cache read. [11]

### Cross-Repo References

The operation and fixture boundaries described here are defined by same-repository contracts and Git helpers. No separate cross-repository document is used as evidence for this card.
