# mcp/src/agents_remember/certification/canonical.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/certification/canonical.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-01T03:11+02:00 |
| lastVerifiedCommitHash | `0506b57a1a80e0b377e9cc3303e1841d3bd4799a`|
| lastVerifiedCommitDate | 2026-09-01T12:17:08+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Certification overview](overview.md)

## Purpose

Owns deterministic canonicalization of repository-supplied rail and profile declarations after a
bounded raw-input admission check.

## Code Commentary

### Logic

`canonicalize_registry` first admits the raw registry against the shared work budget. It then
normalizes unordered contract members, collapses only byte-identical declarations, retains
conflicting variants for exhaustive validation, sorts the resulting catalog, and binds it to a
canonical content digest.

### Conventions

Identity and content digest jointly determine deduplication. Sort order is semantic and stable;
input declaration order is never plan authority.

### Invariants And Boundaries

- Admission happens before normalization or digest allocation.
- Exact duplicates may collapse; same-identity conflicts must remain visible to validation.
- Required artifacts, applicability, evidence, outputs, prerequisites, profiles, and rails have
  deterministic order.
- Over-budget input fails closed; it is never truncated or routed to a cheaper fallback.
- Canonicalization supplies bytes for validation and planning but does not decide correctness.

### Todos

None within canonicalization ownership.

## Docs References

No Domain Documentation source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Raw registry admission refuses excess work before normalization or digest allocation. | `canonicalize_registry` | mcp/src/agents_remember/certification/canonical.py:37-70 |
| Rail variants deduplicate only by exact normalized digest within one identity. | `_canonical_rails` | mcp/src/agents_remember/certification/canonical.py:73-82 |
| Nested contract collections are normalized before stable rail ordering. | `_normalize_rail`; `_rail_sort_key` | mcp/src/agents_remember/certification/canonical.py:100-145 |

## Cross-Repo References

No repository implementation is hardcoded here; all declarations arrive through the registry.

| Finding | Anchor | Source |
| --- | --- | --- |
| Canonicalization consumes the generic `RailRegistry` contract. | `canonicalize_registry` | mcp/src/agents_remember/certification/canonical.py:37-40 |

## Update History

- 2026-09-01T03:11+02:00 — Created for bounded deterministic registry canonicalization.
  Verification remains closeout-owned until the source candidate is committed.
