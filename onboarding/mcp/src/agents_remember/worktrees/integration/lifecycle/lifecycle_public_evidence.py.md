# mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_public_evidence.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_public_evidence.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T00:27+02:00 |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d` |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[worktree integration overview](../overview.md)

## Purpose

Bound private lifecycle identity before developer-facing serialization.

## Code Commentary

### Logic

The public surface is `PublicEvidencePair`, `MigratedLifecycleClassification`, `public_lifecycle_evidence_pair`, `public_lifecycle_evidence`, `public_failure_evidence`, `classify_migrated_lifecycle`. This file bounds public refusal evidence and next actions. Missing, unreadable, mismatched, or ambiguous artifacts remain typed decisions with expected/observed facts; they are never downgraded to absence and private operation keys never cross the public boundary.

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
| The module defines `PublicEvidencePair`; `MigratedLifecycleClassification`; `public_lifecycle_evidence_pair` as its public seam. | `PublicEvidencePair`; `MigratedLifecycleClassification`; `public_lifecycle_evidence_pair` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_public_evidence.py:15-18; mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_public_evidence.py:24-58; mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_public_evidence.py:61-79 |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

## Update History

- 2026-08-24T00:27+02:00 — 260821-CLIVE-L2 committed-route reconciliation: moved this preserved sidecar to mirror `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_public_evidence.py`, repointed current source evidence and governing context, and verified the source at code commit `1d446724d099517f6f52d596b47827ae2391a2a4`.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: created from the accepted full L2 candidate. Verification fields remain blank until the architect-owned closeout has a real code commit to stamp.
