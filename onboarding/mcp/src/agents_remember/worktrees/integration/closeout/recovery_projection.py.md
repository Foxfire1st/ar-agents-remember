# mcp/src/agents_remember/worktrees/integration/closeout/recovery_projection.py

## Governing Overview

[Governing route overview](overview.md)

## Purpose

Derives the closeout recovery-commit projection and generation-retention decision from authoritative mutation evidence and exact contract finalization proof.

## Code Commentary

### Conventions

Accepted input, exact Git facts, and typed owner results stay distinct from disposable projections.

### Logic

The recovery projection contains only `codeCommit` and `memoryContentCommit`. Exact external-memory finalization requires those real output cells; internal or disabled memory requires no external-memory cell. No cache receipt or third commit can retain or block a generation.

Commit-proven evidence is reduced into the code and memory-content commit pair. The evidence model already guarantees that `commit-proven` carries a commit, so projection narrows that typed fact instead of duplicating an impossible-state guard. Reported recovery cells may agree with the projection but cannot contradict or replace it. `closeout_generation_retained` retains private preparation, legacy migration, mutation recovery or exact canonical finalization evidence; none of those categories can be inferred from arbitrary recovery cells.

Finalization proof is deliberately narrow: the contract hash must be present with closeout and approval claimed, complete recovery commits where external memory requires them, and a legal terminal status/phase/result. This preserves a no-op or verified-existing generation through publication without inventing a Git mutation.

#### Invariants And Boundaries

- Recovery cells are a derived journal projection, never primary lifecycle evidence.
- Commit-proven evidence owns mutation recovery.
- Exact `closeout_finalized_contract_sha256` owns publication recovery.
- Phase, approval, or irreversible booleans alone never retain a generation.
- Queue rows never carry or decide this evidence.

### Todos

L2 owns public recovery and revision behavior; L1 only establishes the evidence boundary.

### CCR private preparation boundary

`closeout_recovery_phase` returns `recovering-private-preparation` for a retained preparation with no claimed approval, irreversible boundary, mutation-recovery requirement, legacy migration or finalized contract proof. Claimed recovery uses `recovering-after-claim`, or `contract-finalization` while waiting. Preparation retains the current generation without manufacturing a consumed approval.

- The current `closeout_generation_retained` boundary implements the preparation contract above. [1]
- The current `closeout_recovery_phase` boundary implements the preparation contract above. [2]

## Evidence

### Docs References

No external Domain Documentation source is configured for this slice. The current behavior is repository-owned and is supported by the source references below.

No configured external source applies.

### Repo-Internal References

The following current source boundaries establish the ledger-retirement behavior.

- `derive_closeout_recovery_commits` projects only code and memory-content commits from proven evidence. [3]
- `_has_exact_finalization_evidence` requires exact publication proof and the actual output cells for the memory mode. [4]

- Recovery commits are projected from proven mutations. (`derive_closeout_recovery_commits`) [5]
- Reported cells must match the projection. (`require_closeout_recovery_projection`) [6]
- Retention requires mutation or exact finalization evidence. (`closeout_generation_retained`) [7]

### Cross-Repo References

No meaningful cross-repository reference applies.

No additional cross-repository evidence applies.

## 260821-CLIVE-L2 Current Contract

The current source seams include `derive_closeout_recovery_commits`, `require_closeout_recovery_projection`, `closeout_generation_retained`. Recovery projection is derived from exact journaled mutation/finalization evidence and live repository state. Ambiguity retains the same generation and yields an executable control; it is not inferred from queue phase or a broad completion flag.

### Reconciled Source Evidence

- The current module exposes `derive_closeout_recovery_commits`, `require_closeout_recovery_projection`, `closeout_generation_retained` at this ownership boundary. [8]
