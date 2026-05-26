# mcp/src/agents_remember/providers/cgc/lifecycle/refresh.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/cgc/lifecycle/refresh.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-25T21:14+02:00                     |
| lastVerifiedCommitHash | `c310611a6678051c9e37b912c522b367530c0686` |
| lastVerifiedCommitDate | 2026-05-26T02:17:03+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[CGC Lifecycle Overview](overview.md)

## Purpose

`refresh.py` owns CodeGraphContext index refresh lifecycle for one configured
root or every settings-backed root.

## Code Commentary

### Logic

The module builds `cgc index <repo> --force` commands, returns dry-run refresh
payloads, starts the managed backend when required, runs CGC doctor before live
refreshes, records refresh state, and aggregates all-root refresh results.

### Invariants And Boundaries

- Refresh requires a healthy CGC install and backend when settings-backed roots
  use managed backend mode.
- All-root result aggregation is reused from `process_control.py`.
- Bounded `cgc run` and visualizer behavior live in `query.py`.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Backend startup is delegated to the CGC backend lifecycle module. | [backend.py](agents-remember-md/mcp/src/agents_remember/providers/cgc/lifecycle/backend.py) |
| All-root aggregation helpers are shared with process control. | [process_control.py](agents-remember-md/mcp/src/agents_remember/providers/cgc/lifecycle/process_control.py) |

## Update History

- 2026-05-25T21:14+02:00: Split from `process.py` so refresh orchestration is separate from watcher process control and bounded queries.
