# mcp/src/agents_remember/worktrees/candidate_identity.py

## Governing Overview

[Worktree services](overview.md)

## Purpose

Resolve an authority-selected candidate root to the `candidate-v1:` digest consumed by same-round review recording. This module reads Git and candidate files; it neither publishes task documents nor authenticates a Reviewer.

## Code Commentary

`resolve_candidate_identity` combines the successful HEAD-tree lookup, staged and unstaged tracked diff output, and the representations of nonignored untracked entries reported by Git status. `_fold_untracked_entry` selects kind using `lstat`: links contribute kind and `readlink` target without opening the referent; regular files contribute kind, executable-bit flag and content; directory/FIFO/socket/other entries contribute their own tags. Every failed component read makes the whole result `None`, rather than a matchable unreadable marker. `_git` uses read-only subprocesses with a bounded timeout and accepts output only on successful return. `_head_tree` never infers a state from diagnostic text; an unborn or otherwise unprovable HEAD remains unproven.

### Invariants And Boundaries

- The review transition treats `None` as unproven, never as evidence that the candidate is unchanged.
- Callers resolve the root through task/contract authority; caller-provided candidate strings do not replace this read.
- Link representation is not dereferenced. A missing link target is still a readable link entry, not a failed regular-content read. Failed `lstat`, `readlink` or regular-content reads propagate unproven; no fallback classifies diagnostic text.
- The ruled property is Git-tree representation equality; these defined inputs and retained native tests support the construction. Concurrent mutation and every possible Git configuration are not exhaustively proved by those tests.
- Ignored environments are outside Git's reported untracked population. No Git index, ref or working file is written here.

## Evidence

- Successful HEAD lookup is used; failed lookup remains unproven without an error-text classifier. [1]
- Candidate input construction and fail-unproven propagation over actual untracked entry representations. [2]

- Untracked entries preserve link kind/target, regular kind/executable bit/content and other-kind tags without following a link; failed reads stay unproven. [3]
