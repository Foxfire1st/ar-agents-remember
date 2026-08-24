# mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_operation.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_operation.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T14:43+02:00 |
| lastVerifiedCommitHash | `f95487ec993b58d34911bba0206a7fa6ef9684eb` |
| lastVerifiedCommitDate | 2026-08-24T15:28:18+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[worktree integration overview](../overview.md)

## Purpose

Durable synchronous coordinator for one direct-landing generation.

## Code Commentary

### Logic

The public surface is `DirectLandingRuntime`, `direct_landing_store`, `direct_landing_record`, `reconcile_direct_landing`, `reset_reconciled_attempt`. Direct landing is one journaled task/contract-addressed generation. Accepted code and repository state are immutable, intent precedes each memory or ledger mutation, produced commits are journaled before the next leg, and restart resumes the same generation instead of repeating raw Git from scratch.

### Conventions

Pure classifiers return typed observations; mutation owners publish write-ahead intent and exact evidence before advancing. Public projections carry bounded expected/observed facts and executable task-addressed next actions without leaking private operation identity.

### Invariants And Boundaries

- The canonical root journal, located through the address-only locator and immutable enclosure manifest, owns normal lifecycle state.
- Accepted input and proven commits are immutable; retry and recovery stay on the same generation until evidence admits a successor.
- Queue rows and mutable task documents are not lifecycle evidence or fallback location authorities.

### Todos

None recorded beyond the explicit terminal-archive boundary recorded by the governing overview.

## Docs References

No configured Domain Documentation source applies to this repository-internal lifecycle seam.

## Repo-Internal References

The source file is the direct evidence for this file-specific ownership boundary.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The module defines `DirectLandingRuntime`; `direct_landing_store`; `direct_landing_record` as its public seam. | L39-L155; L158-L159; L162-L198 | `mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_operation.py` |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

## 260821-CLIVE Door Intent And Convergent Recovery

The initial direct-landing record accepts its door publication and journals claim intent before
persistence. Reconciliation may record missing memory or ledger output commits only when the pure
recovery classifier proves them from accepted mutation lineage and deterministic bytes. The same
operation generation is resumed; ambiguous output remains a developer decision.

## Update History

- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: recorded door-bound direct landing and classifier-authorized crash convergence. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.

- 2026-08-24T00:27+02:00 — 260821-CLIVE-L2 committed-route reconciliation: moved this preserved sidecar to mirror `mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_operation.py`, repointed current source evidence and governing context, and verified the source at code commit `1d446724d099517f6f52d596b47827ae2391a2a4`.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: created from the accepted full L2 candidate. Verification fields remain blank until the architect-owned closeout has a real code commit to stamp.
