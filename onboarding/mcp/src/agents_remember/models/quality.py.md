# mcp/src/agents_remember/models/quality.py

## Governing Overview

[models/overview.md](overview.md)

## Purpose

Defines the strict shared public response model for lifecycle-owned quality-gate results, including
stable developer-facing and immutable published-result paths plus typed memory policy. Since
CCR-R22@v1 (L22, commit `685f83c44055`) the model is profile-aware: `QualityGateResult` gained
`executorAdapterId`, `profileDigest` (64-hex), `profilePlanDigest` (64-hex),
`profileSelectionId`, and `resultArtifact`, and `QualityMemoryPolicy.processPolicy` replaces
the old `pytestProcesses: Literal["auto"]` literal with `profile-adapter-owned` -- process
policy now belongs to the repository profile adapter, not pytest.
CCR-R12@v4 (260831-CCR-L12, commit `cfd09381`) adds the optional `runtimeAuthorityDigest` field (64-hex) to `QualityGateResult`: the frozen host-level shared Dagger
authority snapshot digest admitted for the run, surfaced by the strict gate report and the published quality
manifest schema-v3.1. It stays optional so ownerless/preview and no-authority fixture paths still validate.

## Code Commentary

### Logic

`QualityGateResult` names every quality field permitted in closeout and integration responses: the legacy executor/mode/diffBase fields plus the new profile identity fields (`executorAdapterId`, `profileDigest`, `profilePlanDigest`, `profileSelectionId`, `resultArtifact`).
`reportPath` is the stable enclosure wrapper report; `publishedResultPath` is the optional immutable
artifact used only when recovery accepted an already published generation. `QualityMemoryPolicy`
and `QualityMemoryCap` replace open mappings with exact literals and a positive byte cap.

### Invariants And Boundaries

- Extra quality fields are rejected by `StrictResponseModel`; callers cannot leak private paths or
  silently invent response vocabulary.
- The two report paths have different meanings and must not overwrite one another.
- Memory-cap policy and mechanism are exact public literals rather than `dict[str, unknown]`.
- Profile identity fields are strictly typed: the two digest fields must match `^[0-9a-f]{64}$`; `processPolicy` is the literal `profile-adapter-owned` (no `pytestProcesses` auto literal remains).

### Todos

None recorded.

## Evidence

### Docs References

No configured Domain Documentation source applies; this is a repository-owned public wire model.

### Repo-Internal References

- Memory policy and explicit cap have closed, typed vocabulary. [1]
- The quality response retains both stable wrapper and optional immutable publication paths. [2]

### Cross-Repo References

No meaningful cross-repository implementation reference applies.

## 260824-PDLS — Quality Carries Certifying Capability

`CheckConfig` now carries the opaque Dagger admission required by pytest and retry-proof planning,
plus an optional route-neutral pytest phase-report destination. `QualityGateResult` carries the
certifying evidence minted from the verified Dagger publication path. These are typed fields, not
`dict[str, unknown]` flags that a direct caller can elevate.
