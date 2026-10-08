# mcp/src/agents_remember/worktrees/sync_transaction_git.py

## Governing Overview

[Nearest governing route overview](overview.md)

## Purpose

Exact Git mutations and proofs for resumable code and memory-content sync.

## Code Commentary

### Logic

WIP is parked/restored under recorded ownership; only memory-side root memory.md is disposable cache. Code files with that name retain ordinary semantics. [1] [2]

Before Git mutates a divergent memory merge, _knowledge_merge plans structural knowledge/onboarding merge for any converted side: all-converted trees merge directly, crossings convert legacy sides first, and only all-unconverted sides use plain Git. _apply_knowledge_merge installs clean/conflicted items and writes a report only for conflicts or conversion. [9]

Remaining real conflicts go to the agent. Staged continuation closes crossing history and validates the exact staged tree against both parents/paired code before the admitted ordinary merge commit. Refusal leaves the merge staged; no dataset stage or row-decision route remains. Rollback retains exact ownership and restores tracked cache before abort. [8] [12] [14]

### Invariants And Boundaries

- Only exact admitted fast-forward/two-parent output is accepted.
- Structural validity is not semantic approval.
- Every converted memory merge is validated before commit.

## Evidence

### Repo-Internal References


- Pinned refs/checkouts. [1]


- Exact WIP park/restore proof. [2]


- Supported staged continuation. [8]


- Structural merge for every converted side. [9]


- Exact staged validator before commit. [12]


- Attributable rollback. [14]


- Current public content-conflict scenario. [15]


### Cross-Repo References

No cross-repository contract is established by this file.
