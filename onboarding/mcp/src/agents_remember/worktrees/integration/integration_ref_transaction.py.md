# mcp/src/agents_remember/worktrees/integration/integration_ref_transaction.py

| Field | Value |
| --- | --- |
| verificationStatus | working-candidate |

The body describes the uncommitted LCA L9 working candidate. The commit fields identify the latest real commit touching this source file; they do not claim that the candidate is committed or accepted.

## Governing Overview

[Nearest governing route overview](overview.md)

## Purpose

Prepare and publish exact code/memory ref moves with expected-old compare-and-swap and safe refresh of owned checkouts.

## Code Commentary

### Logic

`IntegratedCommits` contains code and memory-content commits only. `LandingAdmission` optionally carries the checkpoint's captured candidate; ordinary integration instead matches the recorded closeout pair. Preparation verifies output authority, current named source tips, source-to-candidate ancestry, and substantive checkout cleanliness before returning its private prepared-move capability.

`require_integrated_memory_ancestry` checks the accepted code object exists and the accepted memory output descends from the exact memory source. It does not parse a ledger, inspect rows, compare headers, or require a trailer mapping for the selected code commit.

Publication CASes code first and memory second. If memory loses a race, code may already be landed; the error retains expected before/intended pair facts and preserves the competing memory ref. There is no hard-reset rollback that can clobber it. Owned checkout refresh requires the named ref at the accepted new tip and permits only old or already-new substantive trees/indexes. On the memory side it excludes root `memory.md`, discarding only that derived path's local state when native checkout needs it.

### Conventions

The lowest ref writer requires the private preparation capability. `CheckoutRefresh` carries side, old, and new identities; code-side files retain ordinary semantics even if named memory.md.

### Invariants And Boundaries

- A compare-and-swap always includes the expected old object id.
- A torn pair remains visible; concurrent memory work is never reset to make the result look atomic.
- Cache state is excluded only for the memory domain and cannot select a delivered commit.
- Unrelated untracked files, substantive content changes, missing objects, or moved refs still refuse.
- Checkpoint and final integration share one transaction with route-specific candidate data.

### Todos

No new file-local follow-up is identified by this source reconciliation.

## Evidence

### Docs References

No domain-documentation source is configured for this slice. The behavior described here is established by current repository source and the authorized LCA L9 change, rather than an invented external reference.

### Repo-Internal References

These current source spans identify the implementation owners and the specific assertions supporting the file's behavior. A test definition is evidence of its assertions, not an execution or certification receipt.

- Two-output and route-specific candidate data. [1]
- Preparation validates accepted output and source/checkout state. [2]
- Ordered expected-old CAS retains a torn pair on a memory race. [3]
- Owned checkout refresh excludes only memory cache state. [4]
- Real Git regression for cache independence and competing memory CAS. [5]

### Cross-Repo References

The operation and fixture boundaries described here are defined by same-repository contracts and Git helpers. No separate cross-repository document is used as evidence for this card.
