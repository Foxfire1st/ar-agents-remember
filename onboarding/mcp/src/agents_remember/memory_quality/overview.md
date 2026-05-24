# mcp/src/agents_remember/memory_quality/ — Memory Quality Overview

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| sourceRoute            | `mcp/src/agents_remember/memory_quality/`  |
| doc_type               | `route-overview`                           |
| lastUpdated            | 2026-05-24T03:09+02:00                     |
| lastVerifiedCommitHash | `0360e6fd7ab582075f11a2a6a50dfc0566f273e9` |
| lastVerifiedCommitDate | 2026-05-24T03:09:23+02:00                 |
| governingOverview      | `../../../overview.md`                     |

## Governing Overview

[mcp/overview.md](../../../overview.md)

## Purpose

`memory_quality/` owns memory-layer quality control for the MCP package. It
groups integrity checks that compare onboarding to source state and style
checks that enforce repository memory conventions.

## Hot Path Summary

`check.py` is the public package-level runner. It can execute style-only checks
without repository context, or combine drift integrity and style checks when an
MCP controller supplies `DriftCheckContext`. Drift logic lives under
`integrity/onboarding_drift_check/`; update-history ordering lives under
`style/update_history/`. The history-order checker is diagnostic; the matching
`history_order_fix.py` module is the explicit mutating script for timestamped
history-order fixes.

## Route Model

- `check.py` normalizes check names, dispatches quality runners, and returns one
  combined payload.
- `integrity/onboarding_drift_check/` contains the moved C-02 drift classifier
  and bounded summary helper.
- `style/update_history/` checks that onboarding `## Update History` bullets
  are newest-first and timestamped, and contains the dedicated history-order
  fix script.
- `integrity/ledger_consistency.py` is reserved for a future ledger-vs-memory
  consistency check.

## Invariants And Boundaries

- Task-start work should use `drift_check` to build the onboarding worklist.
- Closeout should run `memory_quality_check` after onboarding refresh and before
  the memory content commit.
- Style checks should not block the beginning of normal implementation work.
- `memory_quality_check` should stay diagnostic; mechanical style rewrites
  belong in focused fix scripts.
- New memory-quality checks should be placed under `style/` or `integrity/`
  according to what they validate.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The MCP controller builds drift context and calls the package runner for `memory_quality_check`. | [skill_tools.py](agents-remember-md/mcp/src/agents_remember/controllers/skill_tools.py) |
| Tool metadata and server registration expose `memory_quality_check` to agents. | [tools.py](agents-remember-md/mcp/src/agents_remember/mcp/tools.py); [server.py](agents-remember-md/mcp/src/agents_remember/mcp/server.py) |
| The update-history fixer is a dedicated mutating module rather than a `memory_quality_check` option. | [history_order_fix.py](agents-remember-md/mcp/src/agents_remember/memory_quality/style/update_history/history_order_fix.py) |

## Update History

- 2026-05-24T03:09+02:00: Updated after adding the dedicated `history_order_fix.py` script and keeping `memory_quality_check` report-only.
- 2026-05-24T02:47+02:00: Created after memory quality became a first-class package route with integrity and style subdomains.
