# mcp/src/agents_remember/models/quality.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/quality.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T14:19+02:00 |
| lastVerifiedCommitHash |  `f95487ec993b58d34911bba0206a7fa6ef9684eb`|
| lastVerifiedCommitDate |  2026-08-24T15:28:18+02:00|
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

## Update History

- 2026-08-24T14:19+02:00 — 260821-DAGQC-L2: created for the strict shared quality-result wire model. Verification remains blank until architect-owned closeout stamps the code commit.
