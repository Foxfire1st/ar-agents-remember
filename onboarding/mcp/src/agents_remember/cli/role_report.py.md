# mcp/src/agents_remember/cli/role_report.py

## Governing Overview

[Route overview](../overview.md)

## Purpose

The module owns the one read-only route that serves the report file a role launch recorded, addressed by the launcher's execution selection.

## Code Commentary

`RoleReportRequest` extends the result selection with the recorded request ID and has no path input. `read_role_report` resolves the launch context, computes the launch-derived file name (task-bound: `<document-id>-<role>-<request-id>.md` under the task's report root; taskless: `<request-id>.md` under the workspace's role report root), reads the saved receipt and serves only the recorded canonical file directly below that root. `_recorded_report_path` refuses a sibling, handover, nested or retargeted recorded path; `_report_access_refusal` serves the canonical file when the task's access alias is absent and refuses an actually retargeted alias distinctly; `_read_report_file` checks the regular-file mode and reads within the shared bound. `register_role_report_route` adds the POST route `/api/role-launch/report` beside the existing role-launch routes.

## Invariants And Boundaries

Every refusal is named: report-selection-invalid, report-receipt-invalid, report-execution-missing, report-execution-mismatch, report-not-written, report-path-mismatch, report-outside-root, report-access-retargeted/invalid and report-unreadable. The route serves nothing else — no listing, no other file of the reports folder, no write — and a non-regular file is refused before it is read. It does not author, move or delete a report and does not decide acceptance (MIK-R75 rule 4a).

## Evidence

The current source and test assertions below establish the documented ownership; test citations do not claim a rerun in this pass.

- The route's one function: resolves the execution from the launcher's own selection, requires the recorded canonical report and answers every refusal by name. [1]
- Requires the recorded file to be the launch-derived name directly under the exact report root, and refuses a sibling, handover or nested replacement. [2]
- The request body carries the selection and request ID only; there is no path input. [3]
- The read-only regular-file read with the bounded size and truncation contract. [4]
- Serves the canonical file when the task's report-access alias is absent and refuses an actually retargeted alias distinctly. [5]
