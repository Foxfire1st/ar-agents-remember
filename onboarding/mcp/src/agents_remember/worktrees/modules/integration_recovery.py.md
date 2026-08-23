# mcp/src/agents_remember/worktrees/modules/integration_recovery.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/modules/integration_recovery.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T00:27+02:00 |
| lastVerifiedCommitHash | `1d446724d099517f6f52d596b47827ae2391a2a4` |
| lastVerifiedCommitDate | 2026-08-24T00:21:10+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[worktree modules overview](overview.md)

## Purpose

Proves exact ref convergence and external-memory ledger state before integration finalization resumes.

## Code Commentary

### Logic

`classify_convergent_recovery_refs` delegates to the canonical integration-ref classifier and escalates conflicts as typed decision errors. `prove_external_memory_recovery` reads the task memory branch for a series, or requires a clean standalone memory worktree and reads its HEAD, then requires that exact commit to equal the journaled ledger commit.

### Conventions

Recovery classifies current Git facts; it does not repair refs or infer equivalence.

### Invariants And Boundaries

- Conflicting refs require a decision rather than a silent fallback.
- Standalone memory recovery requires a clean worktree.
- The recovered memory head must exactly name the recorded ledger commit.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies to this Git recovery boundary.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Convergent refs are classified by the canonical authority classifier and conflicts stay typed. | L18-L25 | `mcp/src/agents_remember/worktrees/modules/integration_recovery.py` |
| External-memory proof requires the exact task-memory head to equal the journaled ledger commit. | L28-L45 | `mcp/src/agents_remember/worktrees/modules/integration_recovery.py` |

## Cross-Repo References

No cross-repository boundary is owned here; the external memory repository is contract-addressed runtime data.

## Update History

- 2026-08-24T00:27+02:00 — 260821-CLIVE-L2 committed-route reconciliation: created the missing strict sidecar and verified it at code commit `1d446724d099517f6f52d596b47827ae2391a2a4`.
