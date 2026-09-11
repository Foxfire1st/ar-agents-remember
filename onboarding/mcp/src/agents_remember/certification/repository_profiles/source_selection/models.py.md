# mcp/src/agents_remember/certification/repository_profiles/source_selection/models.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/certification/repository_profiles/source_selection/models.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T14:50:20+00:00 |
| lastVerifiedCommitHash | c69d5171187fa1957025e393270db9f5a864ab14 |
| lastVerifiedCommitDate | 2026-09-06T16:32:29+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Source applicability overview](overview.md)

## Purpose

Defines immutable repository declarations, exact candidate/base path observations and self-validating rail applicability decisions.

## Code Commentary

### Logic

`SourcePathApplicability` binds a selector identity/version, canonical sorted unique dependency prefixes, an evidence path and a declared non-applicability reason. `_require_relative` rejects absolute, traversal, backslash, NUL and noncanonical repository paths. `CandidateSourceSelection` binds the exact base commit/base tree and candidate tree to sorted unique changed paths and verifies the full observation digest.

`RailSourceSelection` recomputes selected paths from the declaration and source observation, checks applicability and selection identity, and verifies its complete decision digest. Full mode is always applicable; targeted mode is applicable when any declared prefix matches. A targeted empty selection must carry the repository-declared reason.

### Conventions

Use canonical repository-relative paths and ordered unique tuples; preserve the declaration, source observation and mode together.

### Invariants And Boundaries

- Prefix matching is literal `startswith`; use a trailing slash when the declaration intends a directory boundary.
- Selection is fixed before execution. It cannot be inferred from a test exit or rewritten after a failure.
- A model validates the supplied observation, not whether Git actually produced it; the Git owner supplies that proof.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies to this repository-owned selection contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation applies. | N/A | N/A |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Declarations and observations enforce canonical inputs; decisions recompute matching and both digest domains. | `SourcePathApplicability`; `CandidateSourceSelection`; `RailSourceSelection` | mcp/src/agents_remember/certification/repository_profiles/source_selection/models.py:31-114 |

## Cross-Repo References

No cross-repository implementation boundary is owned by this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository reference is required. | N/A | N/A |

## Update History

- 2026-09-06T14:50:20+00:00 — Created from actual source at c69d5171187fa1957025e393270db9f5a864ab14; documented selection ownership, refusal behavior and execution limits. Source verification does not claim test execution or CCR acceptance.
