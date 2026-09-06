# mcp/src/agents_remember/models/lifecycles/operation_kinds.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/lifecycles/operation_kinds.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-04T10:05+02:00|
| lastVerifiedCommitHash | `f93ac631ca161e5880db3a937728cb256686b13b` |
| lastVerifiedCommitDate | 2026-09-04T09:56:23+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[governing route overview](overview.md)

## Purpose

Lifecycle-operation kind vocabulary without model import cycles.

## Code Commentary

### Logic

The public surface is the module-level closed vocabulary. This module is strict evidence vocabulary, not an I/O or scheduling owner. Its models keep generation, publication, enclosure, termination, legacy, and direct-landing facts explicit so partial or contradictory state fails validation instead of being inferred from queue rows or task prose.

### Conventions

The file exposes typed values or one narrow operation boundary. Callers consume those values directly rather than reconstructing lower-level state from strings, mutable task documents, or queue projection.

### Invariants And Boundaries

- Preserve the module's single ownership seam; do not add a fallback reader or duplicate authority.
- Expected refusal states remain typed and bounded, while unexpected programming faults remain loud.
- Durable lifecycle facts live in the canonical root journal; scheduling projections may only consume them.

### Todos

None recorded.

### CCR private preparation boundary

`recovering-private-preparation` is a distinct lifecycle operation phase for retained private work before approval consumption. Callers must not translate it into `recovering-after-claim`.

| Finding | Anchor | Source |
| --- | --- | --- |
| The current `LifecycleOperationPhase` boundary implements the preparation contract above. | "LifecycleOperationPhase = Literal[" | mcp/src/agents_remember/models/lifecycles/operation_kinds.py:15-40 |

## Docs References

No configured Domain Documentation source applies to this repository-internal lifecycle seam.

## Repo-Internal References

The source file itself is the current evidence for this file-specific contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module defines the closed module vocabulary as its public seam. | `LifecycleOperationKind` | mcp/src/agents_remember/models/lifecycles/operation_kinds.py:5-5 |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

## 2026-08-26 Shared Control Vocabulary

This cycle-free model owner now defines both `LifecycleOperationKind` and the closed
`LifecycleControlAction` vocabulary: retry, recover, cancel, revise, retire, and supersede.
Registration, request models, and lifecycle-control policy import the same literal set instead of
redeclaring it across layers.

## CCR-R18@v1 Centralized Status And Phase Vocabulary

260831-CCR-L18 centralized the full lifecycle-operation vocabulary in this module: `LifecycleOperationKind`, the closed `LifecycleOperationStatus` (queued/running/input-required/termination-required/completed/failed/cancelled), the closed `LifecycleOperationPhase` (queued/preflight/memory-preflight/quality/approval-claim/recovering-after-claim/code-commit/memory-refresh/memory-commit/ledger-commit/integration-replay/integration-quality/source-merge/contract-finalization/door-publication/termination-required/direct-preflight/direct-memory-commit/direct-ledger-commit/direct-terminal-publication/completed/failed/cancelled), and the existing `LifecycleControlAction` literal union.

The state matrix in `models/lifecycles/operation_projection.py` consumes these status/phase literals directly, and its import-time exhaustiveness check (`validate_state_matrix_is_exhaustive`) fails if either vocabulary grows without a matching matrix update. No I/O or scheduling authority lives here.

## Update History

- 2026-09-07 — Reconciled the preparation contract introduced by 245057 against surviving d361 source; retained prior history and verification pins.


- 2026-09-04T10:05+02:00 — 260831-CCR-L18 Gate-5 memory pass: recorded the move of `LifecycleOperationStatus` / `LifecycleOperationPhase` into this centralized vocabulary module and their consumption by the new projection state matrix. Verified at code commit f93ac631ca161e5880db3a937728cb256686b13b.

- 2026-08-26T10:44:52+02:00 — Documented the newly centralized closed lifecycle-control action vocabulary alongside operation kinds.
- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: created from the accepted full L2 candidate. Verification fields remain blank until the architect-owned closeout has a real code commit to stamp.

