# mcp/src/agents_remember/certification/repository_profiles/source_selection/validation.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/certification/repository_profiles/source_selection/validation.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T14:50:20+00:00 |
| lastVerifiedCommitHash | c69d5171187fa1957025e393270db9f5a864ab14 |
| lastVerifiedCommitDate | 2026-09-06T16:32:29+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Source applicability overview](overview.md)

## Purpose

Checks repository declarations for source-selection evidence, exact command inputs and conditional execution dependencies.

## Code Commentary

### Logic

`validate_source_applicability` reports duplicate selector IDs and evidence paths, missing same-gate evidence publication, forbidden posthoc skipped exits, and command placeholders that differ from the exact declared own and conditional source-selection inputs. `source_placeholders` derives the permitted tokens from actual declarations.

`_validate_conditional` reports duplicate conditional prerequisites and requires each to also be a normal prerequisite whose owner exists in the same gate and declares source applicability. Findings accumulate into the caller’s list, preserving multiple declaration errors in one validation pass.

### Conventions

Append all declaration findings to the caller’s existing list; do not classify runtime outcomes during profile validation.

### Invariants And Boundaries

- Conditional prerequisites describe same-gate execution dependencies; they do not remove the ordinary prerequisite edge.
- A repository cannot turn a completed skipped exit into previously admitted non-applicability.
- Evidence publication and command consumption are explicit profile obligations.

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
| Declaration validation accumulates evidence, command and prerequisite findings. | `source_placeholders`; `validate_source_applicability`; `_validate_conditional` | mcp/src/agents_remember/certification/repository_profiles/source_selection/validation.py:13-97 |

## Cross-Repo References

No cross-repository implementation boundary is owned by this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository reference is required. | N/A | N/A |

## Update History

- 2026-09-06T14:50:20+00:00 — Created from actual source at c69d5171187fa1957025e393270db9f5a864ab14; documented selection ownership, refusal behavior and execution limits. Source verification does not claim test execution or CCR acceptance.
