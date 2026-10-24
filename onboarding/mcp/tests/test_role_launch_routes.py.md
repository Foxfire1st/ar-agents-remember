# mcp/tests/test_role_launch_routes.py

## Governing Overview

[Tests route overview](overview.md)

## Purpose

Covers the HTTP routes behind the dashboard's role launch: the task-report link, the message-binding
projection a launch reuses, the public execution result the dashboard reads, the projects architect
dispatch, and the identity a taskless execution keeps across a revive.

## Code Commentary

### Logic

- **Task reports.** `TaskReportAccessTests.test_report_link_writes_to_canonical_task_reports` keeps the
  report link writing into the canonical task reports.
- **Binding projection.** `MessageBindingProjectionTests` reuses identical request content for a
  projection and refuses a replacement, and proves a launch receipt references the projection before the
  native launch.
- **The public result.** `RoleExecutionResultTests` admits the manual role operations by the shipped
  capsule manifest, keeps the selected capsule operation on a public execution, and whitelists the host
  fields while keeping the saved call private. It also proves `canStart` means a fresh request while a
  bound live seat stays a singleton, and that report availability is projected independently of session
  status.
- **Dispatch.** `RoleProjectDispatchTests.test_projects_architect_dispatch_remains_available` keeps the
  projects architect dispatch reachable through the routes.
- **Taskless identity.** `TasklessExecutionIdentityTests` keeps a taskless request address exact and a
  bound revive unchanged, replays a same request while a second intent gets its own receipt and report,
  and confines the one-time history-id migration to matching taskless ids.

### Conventions

`_runtime_config()` builds the configuration a route reads, and the routes are registered against a test
app so each case observes the answer the dashboard receives.

### Invariants And Boundaries

- The public execution result is a whitelist: host fields travel, the saved call does not.
- A request's identity does not drift between a taskless revive and a bound one.

## Evidence

- Report links, projection reuse, the public execution result, dispatch and taskless identity are asserted through the routes. [1]
