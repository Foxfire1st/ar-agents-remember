# mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_recovery_state.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_recovery_state.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-28T07:20+02:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
| governingOverview | `../overview.md` |

## Governing Overview

[worktree integration overview](../overview.md)

## Purpose

Pure live-evidence classifier for one retained direct-landing generation.

## Code Commentary

### Logic

The public surface is `DirectLandingRecoveryClassification`, `classify_direct_landing_recovery`. Direct landing is one journaled task/contract-addressed generation. Accepted code and repository state are immutable, intent precedes each memory or ledger mutation, produced commits are journaled before the next leg, and restart resumes the same generation instead of repeating raw Git from scratch.

Ledger classification distinguishes an exact current mapping from `historical`: a different
newest mapping for the same code commit can be valid prior memory history, so recovery continues
the admitted memory/ledger legs instead of declaring a conflict.

Every clean-repository branch consumes `integration.mutation_evidence.snapshot_is_clean`. The
predicate was moved without changing its exact tuple comparison, eliminating a second definition
inside this already-large classifier while preserving every recovery state transition.

### Conventions

Pure classifiers return typed observations; mutation owners publish write-ahead intent and exact evidence before advancing. Public projections carry bounded expected/observed facts and executable task-addressed next actions without leaking private operation identity.

### Invariants And Boundaries

- The canonical root journal, located through the address-only locator and immutable enclosure manifest, owns normal lifecycle state.
- Accepted input and proven commits are immutable; retry and recovery stay on the same generation until evidence admits a successor.
- Queue rows and mutable task documents are not lifecycle evidence or fallback location authorities.
- Clean-snapshot classification comes from the shared mutation-evidence owner; this classifier does
  not redefine Git cleanliness.
- A `historical` same-code mapping is recoverable pending work. An externally completed ledger
  leg may also carry additional canonical newest-first history, but it is accepted only when the
  operation mapping is newest and every accepted pre-operation row remains an exact suffix.
  Malformed bytes, reordered or dropped accepted history, broken lineage, or a mismatch against
  already-published mutation intent remain conflicts.

### Todos

None recorded beyond the explicit terminal-archive boundary recorded by the governing overview.

## Docs References

No configured Domain Documentation source applies to this repository-internal lifecycle seam.

## Repo-Internal References

The source file is the direct evidence for this file-specific ownership boundary.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module defines `DirectLandingRecoveryClassification`; `classify_direct_landing_recovery` as its public seam. | `DirectLandingRecoveryClassification`; `classify_direct_landing_recovery` | mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_recovery_state.py:53-77; mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_recovery_state.py:107-156 |
| The module consumes the shared mutation snapshot and exact-clean predicate rather than defining recovery-local copies. | `ephemeral_git_mutation_snapshot`; `snapshot_is_clean` | mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_recovery_state.py:29-32 |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

## 260821-CLIVE Exact Output Reconstruction

The pure classifier may reconstruct a missing memory commit only from the accepted parent/tree
lineage. A completed ledger leg must be clean, directly parent the accepted memory commit, change
only the ledger path, and preserve the memory-commit ledger blob as the exact accepted pre-operation
bytes. Its live ledger must parse and render canonically, preserve repository, base, and sort
metadata, place the operation code-to-memory mapping first, and retain every accepted row as an
immutable suffix. Additional canonical newest-first rows between that current mapping and the
accepted suffix are valid history; uniqueness across historical rows is not required. HEAD shape
or a matching row alone is never sufficient, and dropped or reordered accepted history remains a
developer-decision conflict.

## Update History

- 2026-08-27T18:33+02:00 — Removed the private clean-snapshot duplicate and consumed the shared
  mutation-evidence predicate; recovery semantics are unchanged.
- 2026-08-26T17:49+02:00 — Replaced single-prepend byte equality with the complete newest-first
  recovery proof: the current operation mapping must be first, accepted history must remain an exact
  suffix, canonical metadata and rendering must hold, and commit lineage/path evidence remains
  exact. This admits legitimate intervening history without weakening corruption detection.

- 2026-08-26T14:32+02:00 — Added the explicit `historical` ledger state so valid same-code memory
  history remains recoverable while unreadable or intent-conflicting evidence still fails closed.
  Verification remains closeout-owned.

- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: documented the exact lineage and byte predicates for direct-landing recovery. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.
- 2026-08-24T00:27+02:00 — 260821-CLIVE-L2 committed-route reconciliation: moved this preserved sidecar to mirror `mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_recovery_state.py`, repointed current source evidence and governing context, and verified the source at code commit `1d446724d099517f6f52d596b47827ae2391a2a4`.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: created from the accepted full L2 candidate. Verification fields remain blank until the architect-owned closeout has a real code commit to stamp.
