# mcp/src/agents_remember/worktrees/integration/closeout_door_source.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/closeout_door_source.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T14:43+02:00 |
| lastVerifiedCommitHash | `f95487ec993b58d34911bba0206a7fa6ef9684eb`|
| lastVerifiedCommitDate | 2026-08-24T15:28:18+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Worktree-integration overview](overview.md)

## Purpose

Resolves the canonical candidate, master, sprint, caller, grade, admission, scheduling, and
provenance facts that determine a closeout-door generation.

## Code Commentary

The candidate address is derived from the configured contract and current task topology. Managers
declare a leaf door; subsequent controls may also be exercised by the authorized sprint architect
or orchestrator. Completion, grade, review, memory, ledger, admission, scheduling, source bases,
and the task-topology fingerprint all enter the deterministic generation identity.

## Invariants And Boundaries

- Callers cannot inject a leaf candidate address or substitute a queue row for canonical truth.
- Series declaration requires sanctioned direct execution and an asserted candidate.
- Incomplete work or noncanonical grade/admission/provenance refuses generation construction.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The source resolver derives exact generation identity from task and contract authority. | `resolve_closeout_door_source` | `mcp/src/agents_remember/worktrees/integration/closeout_door_source.py` |

## Update History

- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: created from the final canonical source resolver. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.
