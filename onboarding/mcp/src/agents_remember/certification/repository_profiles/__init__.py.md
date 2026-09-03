# mcp/src/agents_remember/certification/repository_profiles/__init__.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/certification/repository_profiles/__init__.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | db57101a9001ede8c681ff9de4eb0147d8b636bc |
| lastVerifiedCommitDate | 2026-09-02T16:49:50+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[Certification contract overview](../overview.md)

## Purpose

The package facade for the explicit repository-owned Gate 1-4 profile authority. It re-exports the
profile admission, canonicalization, execution, planning, selection-result, and validation surface
so certification consumers depend on one stable import seam. L19 added the typed
`repository-selector-result/v2` result contract to the facade.

## Code Commentary

### Logic

The module re-exports `AdmittedRepositoryProfile`, `load_repository_profile`,
`canonicalize_repository_profile`/`repository_profile_digest`,
`admit_repository_profile_execution`, `compile_repository_profile_plan`/`admit_repository_profile_plan`,
`validate_repository_profile`, and the L19 selection-result surface
(`RepositorySelectionDraft`, `RepositorySelectionOutput`, `RepositorySelectionReason`,
`RepositorySelectionResult`, `build_repository_selection_result`,
`repository_selection_result_digest`). `__all__` is the complete public vocabulary.

### Conventions

- The facade is import-only; no behavior is implemented here.
- Every exported name is declared in `__all__`.

### Invariants And Boundaries

- The package owns only repository-neutral profile/selections contracts; it never imports
  repository-specific rail implementations.
- Profile and selector-result schema versions are pinned literals enforced by the exported models.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies; the profiles are repository-owned contracts.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The facade exports the full selection-result surface added by L19. | `RepositorySelectionResult`; `build_repository_selection_result`; `__all__` | mcp/src/agents_remember/certification/repository_profiles/__init__.py:26-33; mcp/src/agents_remember/certification/repository_profiles/__init__.py:38-59 |

## Cross-Repo References

None; this package is the repository-neutral authority inside agents-remember.

## Update History

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for
  db57101a9001ede8c681ff9de4eb0147d8b636bc (CCR-R19@v2/L19): created the card for the package
  facade and recorded the L19 re-export of the selection-result contract.
  Verification is pinned to the owning commit.
