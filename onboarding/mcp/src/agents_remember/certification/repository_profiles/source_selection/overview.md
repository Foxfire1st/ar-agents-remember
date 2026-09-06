# Repository Source Applicability Overview

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | `mcp/src/agents_remember/certification/repository_profiles/source_selection` |
| doc_type | `route-local-overview` |
| lastUpdated | 2026-09-06T14:50:20+00:00 |
| lastVerifiedCommitHash | c69d5171187fa1957025e393270db9f5a864ab14 |
| lastVerifiedCommitDate | 2026-09-06T16:32:29+02:00 |
| governingOverview | `../../overview.md` |

## Governing Overview

[Certification contract overview](../../overview.md)

## What This Area Is

Repository-declared path applicability for individual rails, admitted before execution. The package
separates declaration validation, actual Git observation, pure decision compilation and retained
record reading. It does not own the Python dependency-closure selector or dashboard test commands.

## Hot Path Summary

Use `git.py` to observe exact base/candidate trees, `compilation.py` to derive rail applicability,
and `models.py` to validate the complete frozen decision. `validation.py` binds evidence publication,
command placeholders and conditional prerequisites; `reader.py` reopens the bounded decision file.

## Operating Model

Profile validation checks declarations before execution. If a selected rail declares source
applicability, the Git owner observes a complete path delta with rename detection disabled. The
compiler matches literal declared prefixes and freezes applicability with its source identity.
Full mode makes an already selected rail applicable; targeted non-applicability requires an empty match and the
repository-declared reason. The retained reader validates that decision for consumers.

## Local Invariants And Traps

- Literal prefix matching needs an explicit trailing slash for directory-only prefixes.
- Invalid or truncated Git observation refuses; there is no widening or empty-census fallback.
- Non-applicability is admitted before execution, never inferred from a skipped exit.
- Conditional prerequisites remain declared same-gate prerequisite edges.
- A path-based rail decision does not prove that other test selectors can narrow their populations.

## File-Level Onboarding Map

| Source File | Onboarding | Status |
| --- | --- | --- |
| `__init__.py` | [__init__.py.md](__init__.py.md) | covered |
| `models.py` | [models.py.md](models.py.md) | covered |
| `compilation.py` | [compilation.py.md](compilation.py.md) | covered |
| `git.py` | [git.py.md](git.py.md) | covered |
| `reader.py` | [reader.py.md](reader.py.md) | covered |
| `validation.py` | [validation.py.md](validation.py.md) | covered |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Git observation binds the exact complete base/candidate path delta. | `observe_candidate_source_selection` | mcp/src/agents_remember/certification/repository_profiles/source_selection/git.py:37-78 |
| Decisions recompute prefix selection, applicability and identity. | `RailSourceSelection` | mcp/src/agents_remember/certification/repository_profiles/source_selection/models.py:69-94 |
| Profile validation enforces publication, command and dependency contracts. | `validate_source_applicability`; `_validate_conditional` | mcp/src/agents_remember/certification/repository_profiles/source_selection/validation.py:24-97 |

## Docs References

No configured Domain Documentation source applies to this repository-owned contract.

## Cross-Repo References

No cross-repository implementation boundary is owned by this route.

## Update History

- 2026-09-06T14:50:20+00:00 — Created the source-applicability route from actual source at c69d5171187fa1957025e393270db9f5a864ab14; distinguished path declarations from broader test dependency selection.
