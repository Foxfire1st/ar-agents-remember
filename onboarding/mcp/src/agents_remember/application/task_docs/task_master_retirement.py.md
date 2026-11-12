# mcp/src/agents_remember/application/task_docs/task_master_retirement.py

## Governing Overview

[task_docs overview](overview.md)

## Purpose

Implements the one `task_doc.retire_master` state machine for a master, through its commanding sprint or on its own when no sprint commands it. Finalization never archives a master.

## Code Commentary

`Observed` captures the record, folder and source state; `_admit` produces a `RetirementPlan`. The states are `not-recorded`, `sprint-edited`, `proof-written`, `folder-archived`, `hook-failed` and `hook-finished`. Exactly one owner records retirement: a commanding sprint retains a retirement row, or the master retains `notes/reports/master-retirement.json`. A conflicting second record refuses. The call addresses that owner and a repeated request must match its retained proof.

Sprint retirement accepts a typed row, a correlated legacy seat row or commanded membership with no row. The sprint-edit owner removes affirmed edges, calls `_detached_data` and installs an abandoned retirement row. A legacy seat keeps its file, number, name and scope; without a row, an unused number is appended. The retired row has no live `masterRef`. An unfinished outgoing successor edge must be explicitly affirmed; the last node of a nonempty graph cannot be removed.

Publication rechecks sources and readiness evidence. A completing `sprint-edited` request rewrites the sprint JSON and Markdown pair before moving the folder, repairing an interrupted render without adding another row. A failure before archival restores the exact sprint sources and the folder. After archival, `_archived` checks sources, refreshes a stale projection when necessary, and cleans what remains. `_clean_up` owns the real hook outcome: failure preserves retirement and returns `ok=false`, `retired-with-hook-failures`, `hook-failed` and the identical-request retry action. Deleted artifacts are never recreated.

A changed reason, edge selection or namespace refuses. Only root task folders can be retired. Answers carry the restart notice once a record exists or the request would write one; a refusal before recording carries none.

## Evidence

- The one route observes and admits the exact retained state and recording owner. [9]
- Sprint publication rechecks evidence and repairs the source pair before moving the folder. [10]
- Legacy seat files are retained, while an unrepresented commanded master receives a free-number retirement row. [11]
- The cleanup transition owns the real hook result and preserves a failed retirement. [12]
- The shared edge owner requires affirmation of unfinished outgoing successors. [13]
