# dashboard/src/data/taskReports.ts

## Governing Overview

[data overview](overview.md)

## Purpose

Same-origin browser client for a task's recorded role starts (`GET /api/role-launch/reports`). The rows come from what the product recorded at each start — newest first, at most twenty — never from a walk of the notes tree, so a task page with any number of starts costs one bounded request. An unreadable record rejects so the page can say the reports could not be listed while keeping its Notes link.

## Code Commentary

`listTaskReports(repo, master, doc)` builds the per-task reports URL and delegates to the shared `getJson` transport. `docRefPath(repo, docPath)` strips the dashboard `/tasks/<repo>/` prefix down to the recorded task reference, because the reader scope must name the recorded form for the report to resolve to this task's recorded start. `TaskReportRow` carries the recorded `path`/`canonicalPath` plus `available`; `TaskReports.explorer` names the notes-relative folder of the report files only when more reports exist than the twenty shown.

## Evidence

- The per-task reports URL is built from repo, master and doc. [1]
- The dashboard doc prefix is stripped to the recorded task reference. [2]
- Report rows come from recorded starts, newest first, at most twenty. [3]


