# mcp/tests/test_closeout_execution_input_guards.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_closeout_execution_input_guards.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-22T10:39+02:00 |
| lastVerifiedCommitHash |  `eb7ea60ab9919f009fef58f81afe5861aa1709da`|
| lastVerifiedCommitDate |  2026-08-22T11:44:33+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

Forces every executable worktree-closeout entry to require normalized typed intent and, for non-preview mutation, journal authority before candidate work or Git.

## Code Commentary

### Logic

Separate tests call apply, preview, and the legacy CLI surface with missing normalized input or missing journal authority. The assertions pin typed refusal at the public boundary and compare refs/evidence before and after so a guard cannot merely raise after doing work. Preview-only CLI use is also task-addressed; an ambient synchronous apply cannot become an unjournaled fallback.

### Invariants And Boundaries

- Missing `EffectiveCloseoutInput` refuses before candidate materialization.
- Non-preview closeout requires the canonical durable operation.
- Dry-run remains non-mutating but still requires task/contract addressing and normalized input.
- No compatibility path reconstructs raw messages inside execution.

## Docs References

See task `260821-CLIVE-L1` L1-R1, L1-R2, L1-R4, and L1-R5.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Apply and preview refuse missing normalized intent before candidate work. | `test_closeout_apply_refuses_missing_normalized_input_before_candidate_work`; `test_preview_refuses_missing_normalized_input` | `mcp/tests/test_closeout_execution_input_guards.py:20-44` |
| Journal authority is required with zero ref/evidence change. | `test_closeout_apply_requires_journaled_explicit_approval` | `mcp/tests/test_closeout_execution_input_guards.py:47-62` |
| The legacy CLI is preview-only and task-addressed. | `test_preview_only_cli_requires_task_addressing` | `mcp/tests/test_closeout_execution_input_guards.py:65-67` |

## Cross-Repo References

No cross-repository boundary applies.

## Update History

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: created from accepted candidate tree `4241908c`; first verification stamp remains governed-closeout-owned.
