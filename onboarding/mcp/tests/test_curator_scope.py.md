# test_curator_scope.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_curator_scope.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-26T19:49:05Z |
| lastVerifiedCommitHash | `43b247d5bf30d4191f8fd5eb4dea9cfd72e4258d`|
| lastVerifiedCommitDate | 2026-09-27T00:14:33+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[overview.md](overview.md)

## Purpose

Curator scope admission, storage and retry behavior.

## Code Commentary

### Logic

The tests drive real ingest, check semantic applicability/conditions/exclusions on readback, preserve the exact retry identity, and refuse changed scope under an allocated key or missing/malformed scope before invariant writes.

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
| `test_authored_scope_survives_ingest_and_scope_change_is_not_an_exact_retry` owns the behavior described above. | `test_authored_scope_survives_ingest_and_scope_change_is_not_an_exact_retry` | mcp/tests/test_curator_scope.py:25-50 |

## Cross-Repo References

No independent cross-repository interface is introduced by this source.

| Finding | Anchor | Source |
| --- | --- | --- |
| No additional cross-repository evidence is required. | — | — |

## Update History

- 2026-09-26T19:49:05Z — Created the regression card for this source owner.
