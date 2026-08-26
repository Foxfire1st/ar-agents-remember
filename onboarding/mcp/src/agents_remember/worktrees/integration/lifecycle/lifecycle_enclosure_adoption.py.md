# mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_enclosure_adoption.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_enclosure_adoption.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T14:43+02:00 |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d` |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[worktree integration overview](../overview.md)

## Purpose

Explicit audited adoption of pre-locator readable worktree enclosures.

## Code Commentary

### Logic

The public surface is `AdoptedLifecycleArtifact`, `LifecycleEnclosureAdoptionReceipt`, `LifecycleEnclosureAdoptionPreview`, `preview_lifecycle_enclosure_adoption`, `apply_lifecycle_enclosure_adoption`. Adoption is an explicit audited dry-run/apply path for a readable pre-locator enclosure. It binds exact bytes, publishes one locator/manifest/journal location, and records an idempotent receipt; it is distinct from schema migration and never runs as an implicit fallback.

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
| The module defines `AdoptedLifecycleArtifact`; `LifecycleEnclosureAdoptionReceipt`; `LifecycleEnclosureAdoptionPreview` as its public seam. | `AdoptedLifecycleArtifact`; `LifecycleEnclosureAdoptionReceipt`; `LifecycleEnclosureAdoptionPreview` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_enclosure_adoption.py:32-37; mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_enclosure_adoption.py:40-53; mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_enclosure_adoption.py:56-79 |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

## 260821-CLIVE Successor-WAL Retirement

Enclosure adoption no longer recognizes `.successor-intent` as a legacy artifact. That standalone
WAL is not recoverable authority under the final design; successor publication is proven by the
terminal archive/receipt/locator and exact predecessor transaction instead.

## Update History

- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: removed obsolete successor-intent WAL recognition from the documented adoption surface. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.

- 2026-08-24T00:27+02:00 — 260821-CLIVE-L2 committed-route reconciliation: moved this preserved sidecar to mirror `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_enclosure_adoption.py`, repointed current source evidence and governing context, and verified the source at code commit `1d446724d099517f6f52d596b47827ae2391a2a4`.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: created from the accepted full L2 candidate. Verification fields remain blank until the architect-owned closeout has a real code commit to stamp.
