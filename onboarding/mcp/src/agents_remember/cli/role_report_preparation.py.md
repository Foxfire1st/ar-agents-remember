# mcp/src/agents_remember/cli/role_report_preparation.py

## Governing Overview

[Route overview](../../../overview.md)

## Purpose

Names a launch request's report and settles that request's hand-over locator before any report folder, frozen detail or hand-over artifact is written.

## Code Commentary

`role_report_path` requires the durable request id and computes the request-qualified report name: `<document id>-<role>-<request id>.md` for a task-bound role, `<request id>.md` for a taskless one, under the task report access root's `role-launch` folder (or the role's own folder for a taskless launch). Before it creates the report folder, it calls `ensure_locator` with the canonical report folder, so the alias is owned, reused, rebuilt or refused at the first moment the launch knows where its report lives. A retargeted or occupied alias therefore refuses the launch before any detail or artifact is published, and a repeat of the same request finds the alias it made.

`REPORTS_DIRECTORY` lives here with the owner that uses it, so the read route and this writer share one folder name rather than importing it from the launch preparer.

## Evidence

- The report name is request-qualified and task-bound or taskless by the selected role. [1]
- The request locator is settled at the report folder before the report folder or any file is written. [2]
