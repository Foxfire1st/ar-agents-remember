# mcp/src/agents_remember/certification/repository_profiles/source_selection/reader.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/certification/repository_profiles/source_selection/reader.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T14:50:20+00:00 |
| lastVerifiedCommitHash | c69d5171187fa1957025e393270db9f5a864ab14 |
| lastVerifiedCommitDate | 2026-09-06T16:32:29+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Source applicability overview](overview.md)

## Purpose

Reads one bounded frozen rail-source selection from a regular file and validates its declared decisions.

## Code Commentary

### Logic

`read_rail_source_selection` uses `lstat` to reject a nonregular path or a file larger than one million bytes. It reads at most the bound plus one byte and refuses oversize content, then parses `RailSourceSelection`, invoking its canonical path, matching, applicability and digest validators.

### Conventions

Consume a frozen report path within the caller’s retained-evidence policy; current Git observation remains a separate owner.

### Invariants And Boundaries

- This reader validates a retained decision; it does not recompute the Git census or authorize execution.
- Its physical checks are the explicit lstat and bounded read in this module; it does not claim an atomic descriptor identity or lock.

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
| The reader bounds bytes and delegates self-verification to the closed selection model. | `read_rail_source_selection` | mcp/src/agents_remember/certification/repository_profiles/source_selection/reader.py:15-23 |

## Cross-Repo References

No cross-repository implementation boundary is owned by this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository reference is required. | N/A | N/A |

## Update History

- 2026-09-06T14:50:20+00:00 — Created from actual source at c69d5171187fa1957025e393270db9f5a864ab14; documented selection ownership, refusal behavior and execution limits. Source verification does not claim test execution or CCR acceptance.
