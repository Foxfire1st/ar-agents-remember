# mcp/src/agents_remember/models/lifecycles/memory_census.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/lifecycles/memory_census.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-09 |
| lastVerifiedCommitHash | `602143bd1d48226f4d53b83ff7c5002a695dcdff` |
| lastVerifiedCommitDate | 2026-09-09T00:26:24+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Lifecycle models overview](overview.md)

## Purpose

Defines the strict identities, rows, blockers, and result model for the governed-memory structural census. These models validate exact Git-relative artifact paths and keep the census explicitly noncertifying.

## Code Commentary

### Logic

`require_git_relative_path` rejects empty, escaped, NUL-containing, backslash, drive-prefixed, or non-UTF-8 paths. `GovernedArtifactIdentity` distinguishes file, inline, route, and entity artifacts; `MemoryCensusRow` records expected presence and source reasons; `MemoryCensusResult` enforces unique UTF-8 ordered rows.

### Invariants And Boundaries

- Extra model fields are forbidden and records are frozen.
- Entity rows require `entities.md` plus a nonempty subidentity; whole-document artifacts cannot carry one.
- Absence is legal only for a pre-existing artifact and remains a disposition input, not acceptance.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies.

| Finding | Anchor | Source |
| --- | --- | --- |
| The strict census vocabulary is repository-owned. | `MemoryCensusResult` | mcp/src/agents_remember/models/lifecycles/memory_census.py:104-118 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Exact relative path spelling is validated without normalization. | `require_git_relative_path` | mcp/src/agents_remember/models/lifecycles/memory_census.py:16-30 |
| Artifact identity and entity subidentity rules are enforced together. | `GovernedArtifactIdentity` | mcp/src/agents_remember/models/lifecycles/memory_census.py:33-66 |
| Presence, source reasons, and structural ordering are validated in the census result models. | `MemoryCensusRow`; `MemoryCensusResult` | mcp/src/agents_remember/models/lifecycles/memory_census.py:69-118 |

## Cross-Repo References

None; the model is local to the governed-memory census.

## Update History

- 2026-09-09T02:42:21+02:00 — CCR-L24 inherited-source reconciliation: created the previously absent governed sidecar from source bytes matching code commit `8133b6a9de2f787cb6c4527621a70123357aff31` (candidate-tree source SHA-256 `66719d12eb277fb3f6394e366491f8a08eceb3da86cc483abdf1f6f837573b14`). No future candidate verification stamp was used.
