# mcp/src/agents_remember/worktrees/sync_parked_omissions.py

## Governing Overview

[worktrees overview](overview.md)

## Purpose

Measure the parked authoring a resolved parked-candidate reapply no longer holds, and verify the owner's recorded reconciliation evidence, before a continue may call the sync resolved. The measurement writes nothing; `sync_omission_report` owns the report file.

## Code Commentary

`measure(side, contract, record)` reads back the reconciliations already recorded in the report, then reads each stashed parked path once (its pre-sync blob, its parked blob and its resolved worktree entry, following a rename the carried line made) and lists what the resolved tree lacks: a line the parked change added that the resolved file holds fewer times (`missing-addition`), a line it removed that the resolved file still holds (`retained-removal`), a parked deletion the resolution undid (`missing-deletion`), or a whole-content difference where lines cannot be counted, for binary or non-blob content (`changed-content`). Blank lines are not counted.

`ParkedOmissions` keeps every path with omitted items, reconciled ones included, so the report keeps the owner's records, and its totals count only what remains. `projection` is the answer block (totals and the report path, never the list); `summary` is the refusal naming the items, paths and classes, the stash as potentially the only saved copy, the report and the continue/cancel way on.

`_EvidenceReader` counts a recorded item as reconciled only with evidence it re-measures. A `replacement` holds when its target, confined to the worktree, holds the named line or the item's own fact now; a target that escapes the worktree is no evidence. A `mergedFact` holds when its commit is on the carried line's history and that commit's file holds the fact. A bare label is no evidence. Each cited target is read once per path.

`journal_omissions` records the report path and the outstanding count on the side record and keeps the phase.

## Relationships

`sync_transaction._continue_parked_wip_restore` measures after the unmerged-path check, writes the report and journals the omissions; `sync_transaction_results.parked_wip_validation_preview` measures for a preview without writing. Reads go through `sync_transaction_git` (stash inventory, parked and worktree content, renames, carried head) and `sync_transaction_git._read.revision_content`; replacement paths are confined by `kernel.sidecar_pairing.confine_rel`. The answer block type is `models.worktree.SyncOmissionsProjection`, and `application/review_sync_rebinding.py` gives omissions their own advice state.

## Evidence

- Every parked path is read once and judged against the resolved tree; nothing is written. [1]
- Added lines missing and removed lines retained are counted per line. [2]
- The refusal names the stash as potentially the only saved copy and the way on. [3]
- Recorded evidence is re-measured; an escaping replacement path or an off-line commit is no evidence. [4]
- The report path and outstanding count are journaled on the side. [5]
