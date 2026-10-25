# mcp/src/agents_remember/worktrees/sync_transaction_results.py

## Governing Overview

[Nearest governing route overview](overview.md)

## Purpose

Typed public projections for resumable sync results.

## Code Commentary

### Logic

Results distinguish policy choice, previews, retained merge, parked reapply, terminal replay and quarantine; retained conflict results include any journaled validationRefusal without changing continue/cancel addresses. Retained conflicts name side, worktree/files, owner and contract-addressed continue/cancel. [1]

_resolution_guidance uses supported continue for both retained forms. A structural report adds item summary and crossing-conflict marker guidance, distinguishing crossing from all-converted structural merge. No row-decision placeholder or reconcile action remains. [2] [3]

Previews mutate no index/stash/commit. Completed continuation recomputes worklist through its owner; quarantine proves no unrecorded restoration. [8] [9] [11]


**A structural memory-merge resolution names its report (MIK-R24 rule 8).** When the side record
journals a nonempty `crossingReport`, `resolution_required` adds `resolution.crossing`, the output
of `knowledge_crossing.crossing_summary`: the report path, conflicted-item count, first 100
`(path, item, reason)` entries with a truncation flag, cards taken from each side, moved marker
rows, record-conflict history owner and `howToResolve`. Its summary describes a structural merge
of knowledge files, switching to crossing-sync wording only when the report's `converted` field
is nonempty; both forms name the report and the validator-refused `crossing-conflict` markers.
All-converted merges may journal reports for conflicts or nonzero alignment diagnostics. When
`crossingReport` is empty, no report-derived resolution block or sentence is added.

**The `continue` replay of a completed sync recomputes the worklist (MIK-R08 rule 8).**
`terminal_resolution_replay` with `resolution_action='continue'` on a completed generation now returns
`with_recomputed_worklist(completed_sync_result(...), contract)`, so the replay carries the same optional
`knowledgeWorklist` summary as the original finalization (review R1 F2). A worklist failure leaves the
replayed result unchanged.

Resolution previews read `content_conflicts(side)`: memory-side root memory.md is excluded while code-side files and genuine memory content remain visible. `resolution_validation_preview` delegates the exact staged-content/MERGE_HEAD proof. `parked_wip_validation_preview` reports whether the real reapply conflicts are settled; it does not mutate an index, drop a stash, or create a commit.

### Invariants And Boundaries

- Continue and cancel travel together.
- A completed generation cannot be cancelled retroactively.
- Public resolution preserves file/report facts, not retired canonical rows.

- Memory cache-only index state cannot become a manual resolution requirement.
- Quarantine replay does not claim branch restoration without authority refs.


### Todos

No new file-local follow-up is identified by this source reconciliation.


## Evidence

### Docs References

No domain-documentation source is configured for this slice. The behavior described here is established by current repository source and the authorized LCA L9 change, rather than an invented external reference.


### Repo-Internal References



- Retained conflict shapes. [1]




- Structural/crossing report guidance. [2]



- Current continuation guidance. [3]


- Parked preview. [8]


- Staged preview. [9]


- Terminal replay/worklist. [11]



> Retained earlier citation wording: - Current file-based resolution model. [13]





- A nonempty structural memory-merge report adds resolution.crossing and a named report summary, including all-converted diagnostics; converted selects crossing wording. With no report, no report-derived block or sentence is added. [19]

- Parked-candidate reapply preview. [20]
- Policy choice and non-mutating initial/active/cancel previews. [21]
- Terminal and no-authority replay results remain distinct; the `continue` replay of a completed generation recomputes the worklist. [22]

- Content-domain conflict and staged-resolution proof is delegated to the Git owner. [23]


### Cross-Repo References

The operation and fixture boundaries described here are defined by same-repository contracts and Git helpers. No separate cross-repository document is used as evidence for this card.


No cross-repository contract is established by this file.

- Current file-based resolution model.  Anchor: `SyncResolutionProjection` [13]
