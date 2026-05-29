# mcp/src/agents_remember/mcp/tools/memory.py

| Field                  | Value                                          |
| ---------------------- | ---------------------------------------------- |
| repository             | agents-remember-md                             |
| path                   | `mcp/src/agents_remember/mcp/tools/memory.py`  |
| doc_type               | `file-level-onboarding`                        |
| lastUpdated            | 2026-05-29T18:35+02:00|
| lastVerifiedCommitHash | `23f4d7681f7fcd729049c5f27878c84bbb8f8e58`                                      |
| lastVerifiedCommitDate | 2026-05-29T20:24:00+02:00|
| governingOverview      | `overview.md`                                  |

## Purpose

Memory, drift, route-index, baseline, and carryover payload builders.

## Code Commentary

### Logic

Holds `drift_check_payload`, `memory_quality_check_payload`,
`route_index_refresh_payload`, `memory_init_payload`,
`memory_baseline_status_payload`, `memory_baseline_adopt_payload`,
`memory_carryover_plan_payload`, and `memory_carryover_apply_payload`. Each
forwards typed arguments to the matching `controllers.memory_tools` function and
returns through `base._tool_payload`.

### Invariants And Boundaries

- Transport-thin: all memory/drift behavior lives in `controllers.memory_tools`
  and the memory/onboarding-drift packages.
- The effectful builders (`route_index_refresh_payload`, `memory_init_payload`,
  `memory_baseline_adopt_payload`) default `dry_run=False` (act-by-default),
  matching the server registration; `dry_run=true` previews.

## Update History

- 2026-05-29T20:20+02:00: Recorded the act-by-default `dry_run` default on the effectful memory payload builders.
- 2026-05-29T18:35+02:00: Created from the `mcp/tools.py` domain split (commit `01f503d`).
