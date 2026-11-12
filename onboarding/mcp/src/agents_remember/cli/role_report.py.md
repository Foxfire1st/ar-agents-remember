# mcp/src/agents_remember/cli/role_report.py

## Governing Overview

[Route overview](../overview.md)

## Purpose

The module owns the read-only routes that serve the report files role launches recorded:
the one report addressed by the launcher's execution selection, and the per-task listing of
a task's recorded starts (newest first, at most twenty) that the task page shows beside its
Notes link.

## Code Commentary

`RoleReportRequest` extends the result selection with the recorded request ID and has no path input. `read_role_report` resolves the launch context, computes the launch-derived file name (task-bound: `<document-id>-<role>-<request-id>.md` under the task's report root; taskless: `<request-id>.md` under the workspace's role report root), reads the saved receipt and serves only the recorded canonical file directly below that root. `_recorded_report_path` refuses a sibling, handover, nested or retargeted recorded path; `_report_access_refusal` serves the canonical file when the task's access alias is absent and refuses an actually retargeted alias distinctly; `_read_report_file` checks the regular-file mode and reads within the shared bound. `register_role_report_route` adds the POST route `/api/role-launch/report` beside the existing role-launch routes.

## 260928-MIK-L126 Current Delta — Per-Task Report Listing

`list_task_reports` reads the recorded starts from receipt current-plus-history files, filters
by the recorded task reference (`_complete_task_selection` completes the page's exact task-only
target to the canonical chain, `_find_recorded_receipt` locating the current receipt), and caps
the answer at `_TASK_REPORT_ROWS` (20) however many starts a task accumulates. `read_role_report`
opens live and archived receipts through the confined report path with all refusals intact, so a
task-report target opens the exact recorded report (L126-CODE-10). Reports are found by what the
product recorded at each start, never by a walk of the tree.

## Invariants And Boundaries

Every refusal is named: report-selection-invalid, report-receipt-invalid, report-execution-missing, report-execution-mismatch, report-not-written, report-path-mismatch, report-outside-root, report-access-retargeted/invalid and report-unreadable. The single-report route serves nothing else — no other file of the reports folder, no write — and a non-regular file is refused before it is read. The listing route serves recorded starts only, capped at twenty. It does not author, move or delete a report and does not decide acceptance (MIK-R75 rule 4a).

## Evidence

The current source and test assertions below establish the documented ownership; test citations do not claim a rerun in this pass.

- The listing reads recorded starts filtered by task, capped at twenty. [7]
- The page target completes to the canonical task chain. [8]
- Live and archived receipts open through the confined path. [9]
- The row cap bounds the reports answer. [10]

The current source and test assertions below establish the documented ownership; test citations do not claim a rerun in this pass.



- The request body carries the selection and request ID only; there is no path input. [3]


## Investigator scope and request identity

Task-bound Investigator report lookup requires its exact request UUID and follows the task-owned recorded report. Earlier role spellings and report paths remain read addresses; no role-wide latest result is substituted. Existing product-root confinement, size bound and read-only serving remain unchanged.


## Refreshed current evidence

- The route resolves the execution and requires the recorded canonical report. [1]
- The recorded file must be the launch-derived name directly under the root. [2]
- The read-only regular-file read with bounded size. [4]
- The canonical file serves when the access alias is absent. [5]

- The file's Investigator boundary and request identity. [6]
