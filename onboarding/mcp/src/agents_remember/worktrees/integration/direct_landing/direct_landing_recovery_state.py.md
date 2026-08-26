# mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_recovery_state.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_recovery_state.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T14:43+02:00 |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d` |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[worktree integration overview](../overview.md)

## Purpose

Pure live-evidence classifier for one retained direct-landing generation.

## Code Commentary

### Logic

The public surface is `DirectLandingRecoveryClassification`, `classify_direct_landing_recovery`. Direct landing is one journaled task/contract-addressed generation. Accepted code and repository state are immutable, intent precedes each memory or ledger mutation, produced commits are journaled before the next leg, and restart resumes the same generation instead of repeating raw Git from scratch.

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
| The module defines `DirectLandingRecoveryClassification`; `classify_direct_landing_recovery` as its public seam. | `DirectLandingRecoveryClassification`; `classify_direct_landing_recovery` | mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_recovery_state.py:46-70; mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_recovery_state.py:101-150 |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

## 260821-CLIVE Exact Output Reconstruction

The pure classifier may reconstruct a missing memory commit only from the accepted parent/tree
lineage. A ledger commit must be clean, parent the accepted memory commit, change only the ledger
path, and contain the exact deterministic `prepend_mapping` bytes. HEAD shape or a ledger mapping
alone is never sufficient; conflicts and ambiguous lineage remain developer decisions.

## Update History

- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: documented the exact lineage and byte predicates for direct-landing recovery. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.

- 2026-08-24T00:27+02:00 — 260821-CLIVE-L2 committed-route reconciliation: moved this preserved sidecar to mirror `mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_recovery_state.py`, repointed current source evidence and governing context, and verified the source at code commit `1d446724d099517f6f52d596b47827ae2391a2a4`.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: created from the accepted full L2 candidate. Verification fields remain blank until the architect-owned closeout has a real code commit to stamp.
