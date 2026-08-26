# mcp/src/agents_remember/worktrees/integration/legacy/legacy_operation_authority.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/legacy/legacy_operation_authority.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T00:27+02:00 |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d` |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[worktree integration overview](../overview.md)

## Purpose

Location and serialization authority for the explicit legacy bridge.

## Code Commentary

### Logic

The public surface is `LegacyOperationTarget`, `legacy_pre_adoption`, `revalidated_legacy_target`, `legacy_lifecycle_lease`, `require_explicit_bridge_compatible`. This file belongs only to the explicit bounded schema-1 bridge. It preserves original bytes/digest and evidence under a dedicated lease, migrates once or archives terminal proof, and must disappear when its measurable removal guard is satisfied; the normal current-schema reader never falls back here.

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

| Finding | Anchor | Source |
| --- | --- | --- |
| The module defines `LegacyOperationTarget`; `legacy_pre_adoption`; `revalidated_legacy_target` as its public seam. | `LegacyOperationTarget`; `legacy_pre_adoption`; `revalidated_legacy_target` | mcp/src/agents_remember/worktrees/integration/legacy/legacy_operation_authority.py:30-33; mcp/src/agents_remember/worktrees/integration/legacy/legacy_operation_authority.py:36-43; mcp/src/agents_remember/worktrees/integration/legacy/legacy_operation_authority.py:46-71 |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

## Update History

- 2026-08-24T00:27+02:00 — 260821-CLIVE-L2 committed-route reconciliation: moved this preserved sidecar to mirror `mcp/src/agents_remember/worktrees/integration/legacy/legacy_operation_authority.py`, repointed current source evidence and governing context, and verified the source at code commit `1d446724d099517f6f52d596b47827ae2391a2a4`.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: created from the accepted full L2 candidate. Verification fields remain blank until the architect-owned closeout has a real code commit to stamp.
