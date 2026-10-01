# mcp/src/agents_remember/certification/repository_profiles/models.py

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

### Current source-selection contract

Repository rails carry optional sourceApplicability and canonical conditionalPrerequisites. GeneratedCandidateInput binds a unique source/generated scope census to a declared Gate-1 check rail. EnvironmentReconstructionDefinition declares producer, consuming gates, dependency directories, artifact/proof paths, reconstruction command and bounded time/entry/byte limits; directories must be unique and non-overlapping. Profile normalization orders environments, generated inputs and conditional prerequisites before digesting. The plan retains optional CandidateSourceSelection. Dagger executor transport declares optional retainedReportsArgument; the removed diffBaseArgument is not part of this schema.

- `RepositoryRailDefinition` carries the current contract described above. [1]
- `GeneratedCandidateInput` carries the current contract described above. [2]
- `EnvironmentReconstructionDefinition` carries the current contract described above. [3]
- `_normalize_repository_profile` carries the current contract described above. [4]
- `RepositoryProfilePlan` carries the current contract described above. [5]

## Evidence

### Docs References

No configured Domain Documentation source applies; this is the repository-neutral R22 contract.

### Repo-Internal References

- The selector authority pins v2 schema and declares external inputs. [6]
- Canonical profile normalization determines the repository profile digest. [7]
- Selector normalization canonicalizes its declared collections. [8]
- The canonical profile revalidates its content digest. [9]
- A repository gate plan binds exact semantic inputs and execution declarations. [10]
- A repository profile plan binds its selected gates and content identity. [11]
- Gate plan digests exclude only the aggregate profile digest for stable per-gate identity. [12]

### Cross-Repo References

None; this is the repository-neutral profile schema authority.
