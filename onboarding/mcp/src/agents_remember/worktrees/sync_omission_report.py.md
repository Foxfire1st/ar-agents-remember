# mcp/src/agents_remember/worktrees/sync_omission_report.py

## Governing Overview

[worktrees overview](overview.md)

## Purpose

Own the omission report file of a parked-candidate continue: where it lives, how the owner's recorded reconciliations are read back, and the full write.

## Code Commentary

`report_path` places the report in the enclosure's own scratch, `scratch/sync-omissions-<generation>/<side>.json`, never in a synced worktree.

`read_reconciliations` returns each entry's recorded reconciliations by parked path. Only a missing file means no records. A file that cannot be read, is not JSON, or lacks the report shape (an `entries` list whose entries carry a string `path` and a `reconciliations` list) raises `OmissionReportUnreadableError` naming the file and the way on, and the file is left as the owner left it; a continue that rewrites the report therefore never replaces recorded reconciliations with an empty list.

`write_report` writes the full document (`ar-sync-omissions/v1`: the transaction identity, totals, and each entry's omitted and remaining items with the owner's reconciliations) as canonical JSON; an `OSError` raises `OmissionReportWriteError` naming the location.

## Relationships

`sync_parked_omissions.measure` calls `report_path` and `read_reconciliations`. `sync_transaction._continue_parked_wip_restore` writes the measured report with `write_report` and answers any `OmissionReportError` as `sync-resolution-incomplete`. `sync_transaction_results.parked_wip_validation_preview` reads the report through `measure` and never writes it.

## Evidence

- The report lives in the enclosure's scratch, per generation and side. [1]
- Only a missing report means no records; any other read failure refuses. [2]
- The refusal names the file and says it was left untouched. [3]
- A failed write raises its own error naming the location. [4]
- The continue writes the measured report and answers a report error as an incomplete resolution. [5]
