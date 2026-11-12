# mcp/tests/test_sync_parked_omissions.py

## Governing Overview

[MCP test overview](overview.md)

## Purpose

Prove that a parked-candidate continue whose resolution drops parked authoring stops with an omission report and keeps the parked stash, settling only when each omission is restored or reconciled with evidence the sync re-measures.

## Code Commentary

`ParkedOmissionCustodyTests` drives the real sync over `SyncFixture` repositories. A resolution that drops a parked line and file answers `sync-resolution-incomplete` with the report path and keeps the stash; restoring the content lets the next continue answer `synced`, empty the stash and move the code base to the source tip. Replacement evidence naming lines the resolved file holds settles; a bare `reconciled: true` label counts as no evidence (`reconciledItems` 0). A dry-run continue reports the omissions without writing the report, the journal or the stash. Memory-side omissions are reported and settle the same way.

`OmissionReportBoundaryTests` treats the owner-edited report as evidence input. A report broken into invalid JSON refuses on preview and on continue with a summary naming the file and the way on, carries no `omissions` block, and leaves the report bytes, the journal and the stash unchanged. A replacement path that escapes the worktree is no evidence, and the owner's reconciliations stay in the rewritten report. Blob reads by `measure` stay constant as the omitted items of one path grow from 3 to 12.

`ReviewAdviceResolutionTests` checks that review advice names the resolution kind: parked reapplication, retained merge and omissions awaiting reconciliation each get their own state, and a resumed reapply with a recorded report answers the `omissions` block (side, report, item count) through `WorktreeSyncResponse` and advice naming the item count and report.

## Relationships

It exercises `worktrees/sync_parked_omissions.py`, `worktrees/sync_omission_report.py` and the continue path of `worktrees/sync_transaction.py`, plus `application/review_sync_rebinding.rebinding_result_block`. Fixtures come from `test_worktree_sync.py` (`SyncFixture`), `test_sync_reapply_merge.py` (`sync_record`) and `test_worktree_sync_knowledge_merge.py`; the blob-read count patches `sync_transaction_git._read`. It sits beside `test_sync_parked_candidate.py`, which covers the parked candidate's return.

## Evidence

- A dropping resolution stops with a report and keeps the stash; restoring it settles. [1]
- Recorded replacement evidence is re-measured before a settle. [2]
- A bare reconciled label is no evidence. [3]
- A preview reports omissions without writing or moving anything. [4]
- A malformed report refuses and keeps every byte. [5]
- A replacement outside the worktree is no evidence. [6]
- Blob reads do not grow with the items one path omits. [7]
- A resumed reapply with a recorded report answers the omissions block and its own advice. [8]
