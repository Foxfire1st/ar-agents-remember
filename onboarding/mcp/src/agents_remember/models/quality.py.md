# mcp/src/agents_remember/models/quality.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/quality.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T20:55+02:00 |
| lastVerifiedCommitHash | `77bc614506b8b50937aed6846523547d36045947` |
| lastVerifiedCommitDate | 2026-08-24T20:41:34+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[models/overview.md](overview.md)

## Purpose

Defines the strict shared public response model for lifecycle-owned quality-gate results, including
stable developer-facing and immutable published-result paths plus typed Dagger memory policy.

## Code Commentary

### Logic

`QualityGateResult` names every quality field permitted in closeout and integration responses.
`reportPath` is the stable enclosure wrapper report; `publishedResultPath` is the optional immutable
artifact used only when recovery accepted an already published generation. `QualityMemoryPolicy`
and `QualityMemoryCap` replace open mappings with exact literals and a positive byte cap.

### Invariants And Boundaries

- Extra quality fields are rejected by `StrictResponseModel`; callers cannot leak private paths or
  silently invent response vocabulary.
- The two report paths have different meanings and must not overwrite one another.
- Memory-cap policy and mechanism are exact public literals rather than `dict[str, unknown]`.
- The model is shared by closeout and integration response owners.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies; this is a repository-owned public wire model.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Memory policy and explicit cap have closed, typed vocabulary. | `QualityMemoryPolicy`; `QualityMemoryCap` | mcp/src/agents_remember/models/quality.py:13-26 |
| The quality response retains both stable wrapper and optional immutable publication paths. | `QualityGateResult` | mcp/src/agents_remember/models/quality.py:29-49 |

## Cross-Repo References

No meaningful cross-repository implementation reference applies.

## 260824-PDLS — Quality Carries Certifying Capability

`CheckConfig` now carries the opaque Dagger admission required by pytest and retry-proof planning,
plus an optional route-neutral pytest phase-report destination. `QualityGateResult` carries the
certifying evidence minted from the verified Dagger publication path. These are typed fields, not
`dict[str, unknown]` flags that a direct caller can elevate.

## Update History

- 2026-08-24T20:55+02:00 — 260824-PDLS added typed admission, phase reporting, and certifying
  evidence fields.

- 2026-08-24T14:19+02:00 — 260821-DAGQC-L2: created for the strict shared quality-result wire model. Verification remains blank until architect-owned closeout stamps the code commit.
