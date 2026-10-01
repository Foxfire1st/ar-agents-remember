# mcp/src/agents_remember/worktrees/modules/startup/start_memory.py

| Field | Value |
| --- | --- |
| verificationStatus | working-candidate |

The body describes the uncommitted LCA L9 working candidate. The commit fields identify the latest real commit touching this source file; they do not claim that the candidate is committed or accepted.

## Governing Overview

[Nearest governing route overview](../overview.md)

## Purpose

Own external-memory admission and preparation during worktree start.

## Code Commentary

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

### Docs References

No domain-documentation source is configured for this slice. The behavior described here is established by current repository source and the authorized LCA L9 change, rather than an invented external reference.

### Repo-Internal References

These current source spans identify the implementation owners and the specific assertions supporting the file's behavior. A test definition is evidence of its assertions, not an execution or certification receipt.

- Source state, named-branch admission, and informational Git-derived metadata. [1]
- Mtime reuse and divergence handling preserve the current indexing behavior. [2]
- Missing external repository and explicit disabled-memory outcomes. [3]
- The informational ledger is reconstructed from commit attribution without a cache read. [4]

### Cross-Repo References

The operation and fixture boundaries described here are defined by same-repository contracts and Git helpers. No separate cross-repository document is used as evidence for this card.
