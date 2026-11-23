# mcp/src/agents_remember/models/lifecycles/operation_kinds.py

## Governing Overview

[governing route overview](overview.md)

## Purpose

Lifecycle-operation kind vocabulary without model import cycles.

## Code Commentary

### Logic

`LifecycleOperationPhase` contains no `ledger-commit` or `direct-ledger-commit`. Code and
memory commit phases still distinguish real output publication; consumer cache refresh requires
no lifecycle commit phase. Projection matrices and generated clients consume this same literal.

The public surface is the module-level closed vocabulary. This module is strict evidence vocabulary, not an I/O or scheduling owner. Its models keep generation, publication, enclosure, termination, legacy, and direct-landing facts explicit so partial or contradictory state fails validation instead of being inferred from queue rows or task prose.

### Conventions

The file exposes typed values or one narrow operation boundary. Callers consume those values directly rather than reconstructing lower-level state from strings, mutable task documents, or queue projection.

### Invariants And Boundaries

- Preserve the module's single ownership seam; do not add a fallback reader or duplicate authority.
- Expected refusal states remain typed and bounded, while unexpected programming faults remain loud.
- The canonical root journal retains direct generations and readable older closeout and integration records. Ordinary closeout and integration execute through the synchronous worktree routes.

### Todos

None recorded.

### CCR private preparation boundary

`recovering-private-preparation` remains a distinct stored phase for historical private work before approval consumption. Historical projection preserves its distinction from `recovering-after-claim`. Fresh direct recovery uses the admitted direct lifecycle phases.

- The shared `LifecycleOperationPhase` vocabulary preserves the distinct private-preparation phase for retained evidence. [1]

## Evidence

### Docs References

No configured Domain Documentation source applies to this repository-internal lifecycle seam.

No configured external domain-documentation source applies.

### Repo-Internal References

The source file itself is the current evidence for this file-specific contract.

- The canonical phase union excludes both retired ledger-commit phases. [2]
- The module defines the closed module vocabulary as its public seam. [3]
- None [4]
- None [5]

### Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

No separate external implementation source applies to this file.

## Historical 2026-08-26 Shared Control Vocabulary

The 2026-08-26 cycle-free model owner defined both `LifecycleOperationKind` and the then-current
`LifecycleControlAction` set: retry, recover, cancel, revise, retire, and supersede.
Registration, request models and policy used that shared set. The current vocabulary is recorded below.

## CCR-R18@v1 Centralized Status And Phase Vocabulary

260831-CCR-L18 centralized the full lifecycle-operation vocabulary in this module: `LifecycleOperationKind`, the closed `LifecycleOperationStatus` (queued/running/input-required/termination-required/completed/failed/cancelled), the closed `LifecycleOperationPhase` (queued/preflight/memory-preflight/quality/approval-claim/recovering-after-claim/code-commit/memory-refresh/memory-commit/integration-replay/integration-quality/source-merge/contract-finalization/door-publication/termination-required/direct-preflight/direct-memory-commit/direct-terminal-publication/completed/failed/cancelled), and the existing `LifecycleControlAction` literal union.

The state matrix in `models/lifecycles/operation_projection.py` consumes these status/phase literals directly, and its import-time exhaustiveness check (`validate_state_matrix_is_exhaustive`) fails if either vocabulary grows without a matching matrix update. No I/O or scheduling authority lives here.

## CCR-L42 current candidate

The shared `LifecycleControlAction` vocabulary includes `retry`, `recover`, `resume`, `cancel`, `retire` and `supersede`. The public handler refuses ordinary historical generations before mutation. Use the advertised direct actions for a live direct generation.
