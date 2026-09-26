# test_review_recorded_knowledge.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_review_recorded_knowledge.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-26T19:49:05Z |
| lastVerifiedCommitHash | `43b247d5bf30d4191f8fd5eb4dea9cfd72e4258d`|
| lastVerifiedCommitDate | 2026-09-27T00:14:33+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[overview.md](overview.md)

## Purpose

Exact historical knowledge reconstruction for a closed code-only leaf.

## Code Commentary

### Logic

Real Git memory endpoints contain the selected knowledge. The tests read and continue a family from reconstructed history, preserve operand identity across request-owned temporary paths, and leave an endpoint without knowledge source-only.

### Conventions

Use the existing owner interfaces and exact recorded identities; keep transient task evidence outside durable onboarding.

### Invariants And Boundaries

Tests are scoped executable evidence. They do not certify the mounted product journey, whole-repository quality or semantic acceptance.

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
| `test_closed_code_only_leaf_reads_recorded_knowledge_and_continues_family` owns the behavior described above. | `test_closed_code_only_leaf_reads_recorded_knowledge_and_continues_family` | mcp/tests/test_review_recorded_knowledge.py:42-93 |

## Cross-Repo References

No independent cross-repository interface is introduced by this source.

| Finding | Anchor | Source |
| --- | --- | --- |
| No additional cross-repository evidence is required. | — | — |

## Update History

- 2026-09-26T19:49:05Z — Created the regression card for this source owner.
