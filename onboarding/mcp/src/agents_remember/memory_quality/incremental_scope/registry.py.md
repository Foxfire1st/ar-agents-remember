# mcp/src/agents_remember/memory_quality/incremental_scope/registry.py

## Governing Overview

[memory quality overview](../overview.md)

## Purpose

The CCR-R06@v2 checker-scope policy registry and the fixed dependency-owner contracts. It
enumerates one explicit scope policy per current memory checker — `incremental` or `full-only` —
and binds every edge class to the single existing product owner allowed to emit it. This is the
packet's "checker-registry version" and "policy registry" delivery
(cit:([`EDGE_OWNER_CONTRACTS`, `checker_scope_registry`], mcp/src/agents_remember/memory_quality/incremental_scope/registry.py:28-54; mcp/src/agents_remember/memory_quality/incremental_scope/registry.py:108-129)).

## Code Commentary

### Logic

`_POLICIES` declares four current policies: the drift slot, diff markers, entity alignment and table shape, all `full-only`. No selected citation resolver or scope compiler survives. `checker_scope_registry` returns the sorted population, requires exact equality with `AVAILABLE_CHECKS`, and rejects incremental policies without versions/edges or full-only policies carrying them. `checker_registry_version` fingerprints the canonical complete policy population.

### Conventions

- The registry is a static, deterministic table with a validation entry point; it is not a runtime
  mutable store.
- An unproven checker is explicitly `full-only`, never given an assumed incremental rule (the R06
  packet's open truth gap is closed by enumeration, per the L26 worker delivery).

## Invariants And Boundaries

- Declared checker population must exactly equal `AVAILABLE_CHECKS`; missing or stale entries raise
  a raw `ValueError` (registry completeness is a build-time invariant, not a scope refusal).
- `full-only` checkers must not claim incremental semantics and vice versa.
- The registry owns checker scope declarations only; it never emits edges, identities, or digests
  for dependency facts.

## Evidence

### Docs References

No configured Domain Documentation applies; the registry contracts are repository-owned.

The policy enumeration has no external authority.

### Repo-Internal References

The registry consumes the surviving memory-quality checker population: drift slot, diff markers, entity inventory alignment and table shape.

- The checker population is derived from the memory-quality package check catalog. [1]
