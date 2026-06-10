# mcp/src/agents_remember/mcp/tools/memory.py

| Field                  | Value                                          |
| ---------------------- | ---------------------------------------------- |
| repository             | agents-remember-md                             |
| path                   | `mcp/src/agents_remember/mcp/tools/memory.py`  |
| doc_type               | `file-level-onboarding`                        |
| lastUpdated            | 2026-06-10T09:00+02:00|
| lastVerifiedCommitHash | `cca911fcb6417ecf56de00c17d05aa304daa51c5`                                      |
| lastVerifiedCommitDate | 2026-06-10T02:35:22+02:00|
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

The two carryover builders additionally file the full controller result under
`temp/tool-reports/memory_carryover_plan/` / `.../memory_carryover_apply/` via
`write_tool_report`, then return `compact_carryover_payload(full, reportPath)`:
per-decision `source_path` lists in `decisions` (each list capped at
`MAX_INLINE_CARRYOVER_PATHS` = 25 with a `... (+N more in report)` marker),
`carriedPaths` for apply, and `reportPath` inline. The `candidates` array — and
`carried`, which apply duplicated verbatim — never reach the wire; before this,
a 28-file apply response cost 7.7k tokens (GitHub #52).

### Invariants And Boundaries

- Transport-thin: all memory/drift behavior lives in `controllers.memory_tools`
  and the memory/onboarding-drift packages. Wire-shape compaction is the one
  exception that belongs here (mirroring `tools/providers.py` and
  `tools/core.py`): the controller keeps returning the full result, and the
  report is written BEFORE compaction so forensic detail is never lost.
- Decision facts stay inline (per-decision path lists, commits, intent note);
  only derivable per-record verbosity (onboarding paths, repeated
  evidence/reason strings) moves to the report.
- The effectful builders (`route_index_refresh_payload`, `memory_init_payload`,
  `memory_baseline_adopt_payload`) default `dry_run=False` (act-by-default),
  matching the server registration; `dry_run=true` previews.

## Update History

- 2026-06-10T09:00+02:00 — Carryover plan/apply responses compacted for 2.5.2 (GitHub #52): full result filed via `write_tool_report`, wire keeps per-decision capped path lists + `carriedPaths` + `reportPath`, drops `candidates`/`carried` (apply previously repeated every record twice; 7.7k tokens for a 28-file carryover).
- 2026-05-29T20:20+02:00: Recorded the act-by-default `dry_run` default on the effectful memory payload builders.
- 2026-05-29T18:35+02:00: Created from the `mcp/tools.py` domain split (commit `01f503d`).
