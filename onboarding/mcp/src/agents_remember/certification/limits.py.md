# mcp/src/agents_remember/certification/limits.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/certification/limits.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-01T11:33+02:00 |
| lastVerifiedCommitHash | `0506b57a1a80e0b377e9cc3303e1841d3bd4799a`|
| lastVerifiedCommitDate | 2026-09-01T12:17:08+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Certification overview](overview.md)

## Purpose

Owns the one measured work budget and pre-allocation census for canonicalizing and exhaustively
validating a contributed certification registry, including dependency and artifact reachability.

## Code Commentary

### Logic

Raw admission counts declarations, cross-references, normalization memberships, and digest work.
Validation measurement then accounts for exact rail variants, queries, graph state, traversal
operations, and retained answers. Artifact queries use digest-addressed declaration variants so
conflicting same-identity registrations remain distinct. Registries with no artifact query bypass
producer catalogs and graph storage entirely.

### Conventions

The shared `131072`-unit boundary is an admission model, not a timeout. Measurement records each
cost class so refusal is attributable and testable at exact-cap boundaries.

### Invariants And Boundaries

- Expensive normalization, digest, query, and graph allocation begins only after the prospective
  storage upper bound is proved within the shared budget. This is the sole pre-allocation
  reachability refusal; later reservations account for actual traversal work without repeating a
  dominated exact-storage check.
- Raw duplicate declarations still consume admission work even when exact variants later collapse.
- Reachability is cycle-safe, retains one bounded answer per query, and accounts for storage as
  well as traversal operations.
- Zero-query input allocates no producer/query/graph state.
- Excess work refuses completely; there is no truncation, sampled validation, safe-full path, or
  repository-specific escape hatch.

### Todos

Recalibrate only from measured repository scale while preserving the same fail-closed contract.

## Docs References

No Domain Documentation source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| One constant bounds registry admission and validation work. | `REGISTRY_VALIDATION_WORK_BUDGET` | mcp/src/agents_remember/certification/limits.py:20-20 |
| Raw canonicalization admission accounts for declarations, references, membership, and digest units before allocation. | `admit_registry_canonicalization` | mcp/src/agents_remember/certification/limits.py:166-231 |
| Validation measurement returns an explicit refused census when the cheap floor already exceeds the cap. | `measure_registry_validation_work`; `_refused_work` | mcp/src/agents_remember/certification/limits.py:233-316 |
| Artifact reachability builds bounded query state only when queries exist. | `_measure_reachability`; `_empty_reachability` | mcp/src/agents_remember/certification/limits.py:382-461 |
| Singleton and shared searches retain exact bounded answers and remain cycle-safe. | `_resolve_singleton_queries`; `_resolve_shared_queries` | mcp/src/agents_remember/certification/limits.py:557-602 |

## Cross-Repo References

No repository inventory is embedded in this owner.

| Finding | Anchor | Source |
| --- | --- | --- |
| Budget accounting operates solely on the generic registry contract. | `measure_registry_validation_work` | mcp/src/agents_remember/certification/limits.py:233-300 |

## Update History

- 2026-09-01T11:33+02:00 — CCR-L11 Attempt 10 retained the prospective pre-allocation storage
  refusal and removed the later dominated exact-storage refusal. Re-read both query resolvers and
  rebound their citations to the accepted candidate. Verification remains closeout-owned.

- 2026-09-01T03:11+02:00 — Created for bounded, pre-allocation registry work accounting.
  Verification remains closeout-owned until the source candidate is committed.
