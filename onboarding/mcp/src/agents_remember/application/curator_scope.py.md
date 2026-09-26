# curator_scope.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/curator_scope.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-26T19:49:05Z |
| lastVerifiedCommitHash | `43b247d5bf30d4191f8fd5eb4dea9cfd72e4258d`|
| lastVerifiedCommitDate | 2026-09-27T00:14:33+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[overview.md](overview.md)

## Purpose

Validate the curator-authored semantic scope carried into an invariant revision.

## Code Commentary

### Logic

read_curator_scope accepts exactly applicability, conditions and exclusions. Applicability must be nonblank text within the revision prose limit; both clause fields must be lists of nonblank strings. Empty lists explicitly record that the curator examined the boundary and found no clauses. CuratorScope carries normalized text into the existing invariant model fields.

### Conventions

Use the existing owner interfaces and exact recorded identities; keep transient task evidence outside durable onboarding.

### Invariants And Boundaries

Missing or malformed scope is unfinished curation, not a workflow sentence or default applicability. This helper changes no database schema and migrates no historical record.

### Todos

No additional work is asserted by this card.

## Docs References

No Domain Documentation source is configured. The implementation-specific account is grounded in the repository source below.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain source could be checked. | — | — |

## Repo-Internal References

The named constructs own this behavior; reads and validation use their existing callers and models.

| Finding | Anchor | Source |
| --- | --- | --- |
| `CuratorScope` owns the behavior described above. | `CuratorScope` | mcp/src/agents_remember/application/curator_scope.py:11-22 |
| `read_curator_scope` owns the behavior described above. | `read_curator_scope` | mcp/src/agents_remember/application/curator_scope.py:25-53 |

## Cross-Repo References

No independent cross-repository interface is introduced by this source.

| Finding | Anchor | Source |
| --- | --- | --- |
| No additional cross-repository evidence is required. | — | — |

## Update History

- 2026-09-26T19:49:05Z — Created the semantic-scope admission card.
