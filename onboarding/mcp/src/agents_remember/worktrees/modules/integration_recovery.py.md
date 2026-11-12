# mcp/src/agents_remember/worktrees/modules/integration_recovery.py

## Governing Overview

[Governing route overview](overview.md)

## Purpose

Proves exact ref convergence and external-memory output identity before integration finalization resumes.

## Code Commentary

### Logic

Recovery proves the actual memory-content commit. A standalone memory worktree must be clean outside root `memory.md`; series recovery reads its named memory branch directly. The cache is neither read nor matched against a pairing before finalization.

`classify_convergent_recovery_refs` delegates to the canonical integration-ref classifier and escalates conflicts as typed decision errors. `prove_external_memory_recovery` reads the task memory branch for a series, or requires a standalone memory worktree clean outside the cache and reads its HEAD, then requires that exact commit to equal the journaled memory-content commit.

### Conventions

Recovery classifies current Git facts; it does not repair refs or infer equivalence.

#### Invariants And Boundaries

- Conflicting refs require a decision rather than a silent fallback.
- Standalone memory recovery requires a worktree clean outside root `memory.md`.
- The recovered memory head must exactly name the recorded memory-content commit.

### Todos

None recorded.

## Evidence

### Docs References

No external Domain Documentation source is configured for this slice. The current behavior is repository-owned and is supported by the source references below.

No configured external source applies.

### Repo-Internal References

The following current source boundaries establish the ledger-retirement behavior.

- `prove_external_memory_recovery` requires exact accepted memory HEAD/ref and ignores only root cache dirtiness. [1]
- `classify_convergent_recovery_refs` delegates exact ref classification and preserves typed conflicts. [2]

- Convergent refs are classified by the canonical authority classifier and conflicts stay typed. (`classify_convergent_recovery_refs`) [3]
- External-memory proof requires the exact task-memory head to equal the journaled memory-content commit. (`prove_external_memory_recovery`) [4]

### Cross-Repo References

No cross-repository boundary is owned here; the external memory repository is contract-addressed runtime data.

No additional cross-repository evidence applies.
