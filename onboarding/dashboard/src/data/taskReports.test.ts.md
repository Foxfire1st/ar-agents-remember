# dashboard/src/data/taskReports.test.ts

## Governing Overview

[data overview](overview.md)

## Purpose

Unit tests for the per-task reports client: the reports URL carries the recorded task reference, and the dashboard `/tasks/<repo>/` prefix is stripped before the request so the report resolves to this task's recorded start.

## Code Commentary

Two cases cover `listTaskReports` URL building and `docRefPath` prefix stripping against a mocked transport. No product surface is rendered; the suite pins the client contract the task page's reports section depends on.

## Evidence

- The reports request names the recorded task reference. [1]
- The dashboard prefix is stripped to the recorded form. [2]
