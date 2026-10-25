# mcp/tests/test_paseo_role_agents.py

## Governing Overview

[Tests route overview](overview.md)

## Purpose

Proves the per-agent facts a role start publishes for the dashboard plug-in: one record per agent,
merged into the published file without dropping another agent's facts, skipped when incomplete or
missing, and written only when the launch actually carries a runtime and a report. Registration also
has to reclaim a registration only when the host ended it explicitly.

## Code Commentary

### Logic

`RoleAgentPublishTests` covers the file itself: `test_publish_then_read_round_trips_one_record` proves
publish then read returns the same record and an unchanged republish leaves the file's mtime alone,
`test_publish_merges_without_dropping_other_agents` proves a second agent is added beside the first,
and `test_read_skips_incomplete_records_and_missing_files` keeps a malformed record and an absent file
from being read as facts.

`RoleStartPublishesForPluginTests` drives the start hook: `test_a_start_publishes_role_task_and_report`
checks the published role, task and report, `test_a_repeat_start_publishes_nothing_new` checks a repeat
leaves the published file unchanged, and `test_no_runtime_or_no_report_publishes_nothing` checks the
hook stays silent when either prerequisite is missing.

- **Reclaim needs an explicit end.** `test_registration_reclaims_only_explicitly_ended_roles` reclaims a
  registration only from an authoritative ended occurrence, and a revival supersedes an older end.
- **Concurrency keeps facts.** `test_concurrent_role_registrations_preserve_each_others_facts` runs
  registrations against one published file and requires every agent's facts to survive.

### Conventions

Cases build their own `McpRuntimeConfig` in a temporary root, write the runtime block through
`write_runtime_block`, and drive a `dispatch_request()` carrying the role, task and report facts.

### Invariants And Boundaries

- The published file is merged, never replaced wholesale.
- An incomplete record is skipped rather than interpreted, and a missing file is not an error.

## Evidence

- Publish/read round trip, unchanged republish and cross-agent merging. [1]

- The start hooks publish only when the runtime and the report facts exist. [2]

- Only an authoritative ended occurrence reclaims a registration; a revival supersedes an older end. [3]
- Concurrent registrations retain every published agent's facts. [4]
