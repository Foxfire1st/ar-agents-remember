# mcp/tests/checkpoint_landing_test_support.py

| Field | Value |
| --- | --- |
| verificationStatus | working-candidate |

The body describes the uncommitted LCA L9 working candidate. The commit fields identify the latest real commit touching this source file; they do not claim that the candidate is committed or accepted.

## Governing Overview

[Nearest governing route overview](overview.md)

## Purpose

Provide shared real-Git builders and readers for checkpoint and ordinary series/leaf integration scenarios.

## Code Commentary

### Logic

`close_out_leaf` authors code and one attributed memory-content commit in the leaf's own worktrees, refreshes an untracked cache, and records only the accepted pair. `accumulate_master_line` combines a real code commit with a memory-content commit whose trailer names it; the returned LedgerRow is a convenient value for that actual pair, not a row read from cached history.

`branch_checkout` creates and removes an exact disposable branch worktree. Source advancement and absorption use real content commits and a native merge; no helper creates ledger-only commits, rewrites cached rows to authorize a landing, or manually records a reconciled pair. The remaining readers expose exact revisions, memory repository, payload strings, and master task status.

`checkpoint` calls the public worktree_checkpoint_landing tool with ff-only strategy. Its consumers are the checkpoint end-to-end, cross-master concurrency, and lifecycle playthrough modules.

### Conventions

A flat support module owns shared construction steps; scenario-specific assertions stay in the consumers. A support function's existence does not establish that a scenario ran.

### Invariants And Boundaries

- Real commits and branches back every accepted pair.
- Memory cache preparation is part of ordinary memory content; refreshing the cache is not a Git commit.
- Checkpoint scenarios retain the public tool boundary.
- Disposed scratch worktrees do not become authority for a later scenario.

### Todos

No new file-local follow-up is identified by this source reconciliation.

## Evidence

### Docs References

No domain-documentation source is configured for this slice. The behavior described here is established by current repository source and the authorized LCA L9 change, rather than an invented external reference.

### Repo-Internal References

These current source spans identify the implementation owners and the specific assertions supporting the file's behavior. A test definition is evidence of its assertions, not an execution or certification receipt.

- Leaf and accumulated-master pairs are built from real code/memory commits. [1]
- Temporary branch ownership and real source-content reconciliation. [2]
- Public checkpoint and canonical master status helpers. [3]
- The public boundary scenarios consume the shared builders. [4]

### Cross-Repo References

The operation and fixture boundaries described here are defined by same-repository contracts and Git helpers. No separate cross-repository document is used as evidence for this card.
