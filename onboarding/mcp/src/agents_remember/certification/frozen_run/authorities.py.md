# mcp/src/agents_remember/certification/frozen_run/authorities.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/certification/frozen_run/authorities.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T14:47:06+00:00 |
| lastVerifiedCommitHash | c69d5171187fa1957025e393270db9f5a864ab14 |
| lastVerifiedCommitDate | 2026-09-06T16:32:29+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Frozen certification run overview](overview.md)

## Purpose

Defines closed retained observations for mutation, source lineage, staged-worktree rules, and generated-input declarations used by lifecycle admission.

## Code Commentary

### Logic

`AuthorityInputSnapshot` binds an identified owner and address to exact UTF-8 bytes and their SHA-256. Mutation authority records the addressed task, roots, work refs and normalized commit intent; optional memory root/ref must appear together. Source authority records bounded lineage edges with explicit tips and relation kinds. Worktree rules retain physical Git identity, HEAD, staged/add-all trees, conflicts and hook observation. Generated-input records bind profile declarations to the candidate but retain status `unknown`; Gate 1 still owns freshness checking.

`CandidateAuthorityEnvelope` combines the four semantic projections. `CandidateAuthorityRecords` binds the envelope digest while separately retaining original input snapshots and creation evidence. Input snapshot identities must be unique and sorted by owner/address. The real observation caller assembles these from task, contract, source-lineage and effective-input owners.

### Conventions

Use the existing observation owner to populate these records from actual task, contract, Git and profile inputs.

### Invariants And Boundaries

- Authority models describe observations; constructing one does not acquire a lock, run a hook, stage files or authorize a write.
- `authorityDigest` covers semantic projections. Top-level `inputSnapshots` and provenance remain separately retained derivation evidence. The generated-input `declarations` snapshot is inside the semantic envelope and is included in that digest.
- The byte snapshot hash must match its exact UTF-8 serialization. Memory mutation roots and refs are an inseparable pair.
- Generated-input status remains unknown until its gate owner checks it.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies to this repository-owned contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation applies. | N/A | N/A |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Snapshots verify exact bytes and mutation authority requires a complete memory pair. | `AuthorityInputSnapshot`; `MutationAuthorityRecord` | mcp/src/agents_remember/certification/frozen_run/authorities.py:19-50 |
| Source and worktree contracts retain explicit tips, physical identities and preparation observations. | `SourceAuthorityEdge`; `WorktreeRuleRecord` | mcp/src/agents_remember/certification/frozen_run/authorities.py:53-86 |
| Generated-input declarations do not claim freshness; the aggregate validates its semantic digest and snapshot order. | `GeneratedInputRecord`; `CandidateAuthorityRecords` | mcp/src/agents_remember/certification/frozen_run/authorities.py:89-128 |
| The production observer derives records from current task, door, worktree, lineage and contract owners. | `observe_certification_candidate` | mcp/src/agents_remember/worktrees/integration/closeout/certification/observation.py:97-189 |

## Cross-Repo References

No cross-repository implementation boundary is owned by this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository reference is required. | N/A | N/A |

## Update History

- 2026-09-06T14:47:06+00:00 — Created from the actual source at c69d5171187fa1957025e393270db9f5a864ab14; documented retained authority and its validation boundaries. This source verification does not assert gate execution or CCR acceptance.
