# mcp/src/agents_remember/memory_quality/ — Memory Quality Overview

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| sourceRoute            | `mcp/src/agents_remember/memory_quality/`  |
| doc_type               | `route-local-overview`                     |
| lastUpdated            | 2026-06-06T12:15                           |
| lastVerifiedCommitHash | `610b8568b6517a78a80d35583101b32ed396e2a7` |
| lastVerifiedCommitDate | 2026-06-11T15:49:54+02:00|
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
`integrity/onboarding_drift_check/`; the pre-code-commit missing-onboarding
check lives at `integrity/check_missing_onboarding.py`; update-history ordering lives under
`style/update_history/`. The history-order checker is diagnostic; the matching
`history_order_fix.py` module is the explicit mutating script for timestamped
history-order fixes.

## Route Model

- `check.py` normalizes check names, dispatches quality runners, and returns one
  combined payload.
- `integrity/onboarding_drift_check/` contains the moved `c-02-memory-quality-control` skill drift classifier
  and bounded summary helper.
- `integrity/check_missing_onboarding.py` checks only current worktree
  additions so newly added eligible files get sidecars before the code commit.
- `style/update_history/` checks that onboarding `## Update History` bullets
  are newest-first and timestamped, and contains the dedicated history-order
  fix script.

## Invariants And Boundaries

- Task-start work should use `drift_check` to build the onboarding worklist.
- Closeout should run `memory_quality_check` after onboarding refresh and before
  the memory content commit.
- Closeout should run `check_missing_onboarding` before the code commit when
  the task added source files; this is local worktree responsibility, not a
  whole-repository adoption scan.
- Style checks should not block the beginning of normal implementation work.
- `memory_quality_check` should stay diagnostic; mechanical style rewrites
  belong in focused fix scripts.
- New memory-quality checks should be placed under `style/` or `integrity/`
  according to what they validate.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The MCP controller builds drift context and calls the package runner for `memory_quality_check`. | [memory_tools.py](agents-remember/mcp/src/agents_remember/controllers/memory_tools.py) |
| Tool metadata and server registration expose `memory_quality_check` to agents. | [mcp/tools/memory.py](agents-remember/mcp/src/agents_remember/mcp/tools/memory.py); [server.py](agents-remember/mcp/src/agents_remember/mcp/server.py) |
| The update-history fixer is a dedicated mutating module rather than a `memory_quality_check` option. | [history_order_fix.py](agents-remember/mcp/src/agents_remember/memory_quality/style/update_history/history_order_fix.py) |
| The missing-onboarding checker catches newly added worktree files before code commit. | [check_missing_onboarding.py](agents-remember/mcp/src/agents_remember/memory_quality/integrity/check_missing_onboarding.py) |

## Update History

- 2026-06-11T15:20+02:00 — No route impact: onboarding_drift_check/git_ops.py fingerprint helpers gained a keyword-only ref parameter for carryover entity-catalog validation; route structure and check responsibilities are unchanged.
- 2026-06-06T12:15: Re-verified against the current memory-quality package; corrected controller and MCP payload-builder references after memory tools moved out of the former `skill_tools.py`/`mcp/tools.py` surfaces.
- 2026-05-31T12:40+02:00: Removed the `integrity/ledger_consistency.py` reserved-stub bullet after the empty stub source and its sidecar were deleted in the 1.0.0 remediation.
- 2026-05-24T03:24+02:00: Updated after adding `check_missing_onboarding` as the pre-code-commit integrity pass for newly added files.
- 2026-05-24T03:09+02:00: Updated after adding the dedicated `history_order_fix.py` script and keeping `memory_quality_check` report-only.
- 2026-05-24T02:47+02:00: Created after memory quality became a first-class package route with integrity and style subdomains.
