# mcp/src/agents_remember/worktrees/integration/closeout/recovery_projection.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/closeout/recovery_projection.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-25T08:16+02:00 |
| lastVerifiedCommitHash | `cb6623775a04cbdeb0509dc26f08a8268189c3f6` |
| lastVerifiedCommitDate | `2026-08-25T08:12:56+02:00` |
| governingOverview | `../overview.md` |

## Governing Overview

[worktree integration overview](../overview.md)

## Purpose

Derives the legacy closeout recovery-commit projection and generation-retention decision from authoritative mutation evidence and exact contract finalization proof.

## Code Commentary

### Logic

Commit-proven evidence is reduced into the code, memory-content, and ledger commit tuple. The evidence model already guarantees that `commit-proven` carries a commit, so projection narrows that typed fact instead of duplicating an impossible-state guard. Reported recovery cells may agree with the projection but cannot contradict or replace it. `closeout_generation_retained` returns true only when durable mutation evidence exists or an exact canonical finalization publication proves the completed closeout edge.

Finalization proof is deliberately narrow: the contract hash must be present with closeout and approval claimed, complete recovery commits where external memory requires them, and a legal terminal status/phase/result. This preserves a no-op or verified-existing generation through publication without inventing a Git mutation.

### Invariants And Boundaries

- Recovery cells are derived compatibility projection, never primary lifecycle evidence.
- Commit-proven evidence owns mutation recovery.
- Exact `closeout_finalized_contract_sha256` owns publication recovery.
- Phase, approval, or irreversible booleans alone never retain a generation.
- Queue rows never carry or decide this evidence.

### Todos

L2 owns public recovery and revision behavior; L1 only establishes the evidence boundary.

## Docs References

See task `260821-CLIVE-L1` L1-R4 and L1-R6.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Recovery commits are projected from proven mutations. | `derive_closeout_recovery_commits` | mcp/src/agents_remember/worktrees/integration/closeout/recovery_projection.py:28-49 |
| Reported cells must match the projection. | `require_closeout_recovery_projection` | mcp/src/agents_remember/worktrees/integration/closeout/recovery_projection.py:83-91 |
| Retention requires mutation or exact finalization evidence. | `closeout_generation_retained` | mcp/src/agents_remember/worktrees/integration/closeout/recovery_projection.py:94-105 |

## Cross-Repo References

No meaningful cross-repository reference applies.

## 260821-CLIVE-L2 Current Contract

The current source seams include `derive_closeout_recovery_commits`, `require_closeout_recovery_projection`, `closeout_generation_retained`. Recovery projection is derived from exact journaled mutation/finalization evidence and live repository state. Ambiguity retains the same generation and yields an executable control; it is not inferred from queue phase or a broad completion flag.

### Reconciled Source Evidence

| Finding | Anchor | Source |
| --- | --- | --- |
| The current module exposes `derive_closeout_recovery_commits`, `require_closeout_recovery_projection`, `closeout_generation_retained` at this ownership boundary. | `derive_closeout_recovery_commits`; `require_closeout_recovery_projection`; `closeout_generation_retained` | mcp/src/agents_remember/worktrees/integration/closeout/recovery_projection.py:28-49; mcp/src/agents_remember/worktrees/integration/closeout/recovery_projection.py:83-91; mcp/src/agents_remember/worktrees/integration/closeout/recovery_projection.py:94-105 |

## Update History

- 2026-08-25T08:16+02:00 — 260824-PDLS wave 004: moved this preserved sidecar with its behavior-preserving package split, repointed source evidence, and verified the emergency-landed source path at code commit `cb6623775a04cbdeb0509dc26f08a8268189c3f6`; this is onboarding provenance, not Dagger certification.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: created from candidate tree `4241908c`; first commit verification remains closeout-owned.
