# mcp/src/agents_remember/worktrees/integration/closeout/door_source.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/closeout/door_source.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-25T08:16+02:00 |
| lastVerifiedCommitHash | `cb6623775a04cbdeb0509dc26f08a8268189c3f6` |
| lastVerifiedCommitDate | `2026-08-25T08:12:56+02:00` |
| governingOverview | `../overview.md` |

## Governing Overview

[Worktree-integration overview](../overview.md)

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
| The source resolver derives exact generation identity from task and contract authority. | `door_task_context`; `updated_door_generation`; `_declare_generation` | mcp/src/agents_remember/worktrees/integration/closeout/door_source.py:57-73; mcp/src/agents_remember/worktrees/integration/closeout/door_source.py:192-203; mcp/src/agents_remember/worktrees/integration/closeout/door_source.py:336-435 |

## Update History

- 2026-08-25T08:16+02:00 — 260824-PDLS wave 004: moved this preserved sidecar with its behavior-preserving package split, repointed source evidence, and verified the emergency-landed source path at code commit `cb6623775a04cbdeb0509dc26f08a8268189c3f6`; this is onboarding provenance, not Dagger certification.

- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: created from the final canonical source resolver. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.
