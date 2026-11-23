# mcp/tests/test_paseo_role_agents.py

## Governing Overview

[Tests route overview](overview.md)

## Purpose

Proves the per-agent facts a role start publishes for the dashboard plug-in: one record per agent,
merged into the published file without dropping another agent's facts, skipped when incomplete or
missing, and written only when the launch actually carries a runtime and a report. Registration also
preserves closed and omitted records and distinguishes a later confirmed archive from a newer registration.

## Code Commentary

### Logic

`RoleAgentPublishTests` covers the file itself: `test_publish_then_read_round_trips_one_record` proves
publish then read returns the supplied identity,
`test_publish_merges_without_dropping_other_agents` proves a second agent is added beside the first,
and `test_read_skips_incomplete_records_and_missing_files` keeps a malformed record and an absent file
from being read as facts.

`RoleStartPublishesForPluginTests` drives the start hook: `test_a_start_publishes_role_task_and_report`
checks the published role, task and report, `test_a_repeat_start_preserves_one_identity_and_refreshes_its_registration` checks a repeat refreshes the timestamp on one row, and `test_no_runtime_or_no_report_publishes_nothing` checks the
hook stays silent when either prerequisite is missing.

- **Recovery uses positive evidence.** The archive, exact absence and concurrent-registration cases check registration order, receipt status, and that incomplete observations leave records in place.
- **Concurrency keeps facts.** `test_concurrent_role_registrations_preserve_each_others_facts` runs
  registrations against one published file and requires every agent's facts to survive.

### Conventions

Cases build their own `McpRuntimeConfig` in a temporary root, write the runtime block through
`write_runtime_block`, and drive a `dispatch_request()` carrying the role, task and report facts.

### Invariants And Boundaries

- The published file is merged, never replaced wholesale.
- An incomplete record is skipped rather than interpreted, and a missing file is not an error.

## Evidence


- Published facts round-trip. Same-identity republish refreshes registration time, and merging preserves other agents. [1]



- The start hooks publish only when the runtime and the report facts exist. [2]



- A positive archive reclaims a valid registration only when it is newer. An older archive, a close and listing omission preserve the row. [3]


- Concurrent registrations retain every published agent's facts. [4]
