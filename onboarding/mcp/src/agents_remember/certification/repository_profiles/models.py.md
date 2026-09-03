# mcp/src/agents_remember/certification/repository_profiles/models.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/certification/repository_profiles/models.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | db57101a9001ede8c681ff9de4eb0147d8b636bc |
| lastVerifiedCommitDate | 2026-09-02T16:49:50+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[Certification contract overview](../overview.md)

## Purpose

Strict repository-owned inputs for the configurable Gate 1-4 contribution: the
`RepositoryCertificationProfile` schema and its normalized content-addressed digests. It fixes
the profile/selection/rail/selector/executor/decoder/artifact declarations a repository contributes
to the generic certification registry.

## Code Commentary

### Logic

Frozen contract models declare `RepositoryProfileSelection` (purpose/mode/executor/decoder plus
exactly four gate selections), `RepositoryGateSelection` (applicable requires rails and
population, not-applicable requires only a reason), `RepositoryRailDefinition`/`RepositoryRailExecution`,
`RepositorySelectorAuthority`, `DaggerModuleExecutorDefinition`,
`JsonExitStatusDecoderDefinition`, `PublishedArtifactDefinition`, and the aggregate
`RepositoryCertificationProfile`.

L19 pinned `RepositorySelectorAuthority.schemaVersion` to the literal
`repository-selector-result/v2` and added the declared `externalInputs` tuple, which
participates in the normalized profile digest via `_normalize_selector`.
`repository_profile_digest` normalizes every ordered/deduplicated collection before
content-addressing, and `CanonicalRepositoryCertificationProfile` verifies the profileDigest
at validation. `RepositoryGatePlan`/`RepositoryProfilePlan` freeze per-gate semantic
identity, with `repository_gate_plan_digest` deliberately excluding the aggregate
profileDigest so an unchanged earlier gate plan keeps its identity when a later gate's repository
configuration changes. `RepositorySemanticInputNode` binds one canonical input to its exact
consuming gates and validates canonical JSON plus content digest.

### Invariants And Boundaries

- Profile mode is `targeted` or `full` only; gate selections are always exactly Gates 1-4.
- Applicable selections require rails and population and forbid a reason; not-applicable requires a
  reason and forbids the rest.
- Every digest is a canonical content digest over normalized JSON; the canonical profile re-verifies
  it.
- Gate plans require the complete earlier-gate prerequisite prefix and canonical execution waves.
- Repository selector schema version is fixed to v2; legacy v1 selector results are not admitted.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies; this is the repository-neutral R22 contract.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The selector authority pins v2 schema and declares external inputs. | `RepositorySelectorAuthority` | mcp/src/agents_remember/certification/repository_profiles/models.py:151-161 |
| Normalization digests ordered/deduplicated collections, including external inputs. | `repository_profile_digest`; `_normalize_selector` | mcp/src/agents_remember/certification/repository_profiles/models.py:308-311; mcp/src/agents_remember/certification/repository_profiles/models.py:357-366 |
| The canonical profile re-verifies its digest; gate plans bind exact semantic identity. | `CanonicalRepositoryCertificationProfile`; `RepositoryGatePlan`; `RepositoryProfilePlan` | mcp/src/agents_remember/certification/repository_profiles/models.py:407-419; mcp/src/agents_remember/certification/repository_profiles/models.py:466-511; mcp/src/agents_remember/certification/repository_profiles/models.py:514-550 |
| Gate plan digests exclude only the aggregate profile digest for stable per-gate identity. | `repository_gate_plan_digest` | mcp/src/agents_remember/certification/repository_profiles/models.py:553-564 |

## Cross-Repo References

None; this is the repository-neutral profile schema authority.

## Update History

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for
  db57101a9001ede8c681ff9de4eb0147d8b636bc (CCR-R19@v2/L19): created the card and recorded the
  L19 changes — `RepositorySelectorAuthority.schemaVersion` pinned to
  `repository-selector-result/v2` and the declared `externalInputs` tuple that now
  participates in the normalized profile digest. Verification is pinned to the owning commit.
