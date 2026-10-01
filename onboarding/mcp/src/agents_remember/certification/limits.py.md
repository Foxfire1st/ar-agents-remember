# mcp/src/agents_remember/certification/limits.py

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

## Evidence

### Docs References

No Domain Documentation source is configured for this memory root.

No configured domain documentation could be checked.

### Repo-Internal References

- One constant bounds registry admission and validation work. [1]
- Raw canonicalization admission accounts for declarations, references, membership, and digest units before allocation. [2]
- Validation measurement returns an explicit refused census when the cheap floor already exceeds the cap. [3]
- Artifact reachability builds bounded query state only when queries exist. [4]
- Singleton and shared searches retain exact bounded answers and remain cycle-safe. [5]

### Cross-Repo References

No repository inventory is embedded in this owner.

- Budget accounting operates solely on the generic registry contract. [6]
