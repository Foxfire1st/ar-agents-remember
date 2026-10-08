# mcp/src/agents_remember/worktrees/sync_transaction_results.py

## Governing Overview

[Nearest governing route overview](overview.md)

## Purpose

Typed public projections for resumable sync results.

## Code Commentary

### Logic

Results distinguish policy choice, previews, retained merge, parked reapply, terminal replay and quarantine. Retained conflicts name side, worktree/files, owner and contract-addressed continue/cancel. [1]

_resolution_guidance uses supported continue for both retained forms. A structural report adds item summary and crossing-conflict marker guidance, distinguishing crossing from all-converted structural merge. No row-decision placeholder or reconcile action remains. [2] [3]

Previews mutate no index/stash/commit. Completed continuation recomputes worklist through its owner; quarantine proves no unrecorded restoration. [8] [9] [11]

### Invariants And Boundaries

- Continue and cancel travel together.
- A completed generation cannot be cancelled retroactively.
- Public resolution preserves file/report facts, not retired canonical rows.

## Evidence

### Repo-Internal References


- Retained conflict shapes. [1]


- Structural/crossing report guidance. [2]


- Current continuation guidance. [3]


- Parked preview. [8]


- Staged preview. [9]


- Terminal replay/worklist. [11]


- Current file-based resolution model. [13]


### Cross-Repo References

No cross-repository contract is established by this file.
