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

`EDGE_OWNER_CONTRACTS` maps the five `EdgeClass` values to their canonical authority namespace and
extractor/validator versions: sidecar pairing, route index, citation model (v8 source index),
entity catalog, and route-index inputs
cit:([`EDGE_OWNER_CONTRACTS`, `EdgeOwnerContract`], mcp/src/agents_remember/memory_quality/incremental_scope/registry.py:19-25; mcp/src/agents_remember/memory_quality/incremental_scope/registry.py:28-54).
`_POLICIES` declares every current checker's one policy: drift summary, claim reopen, diff markers,
entity alignment, history order, and table shape are `full-only` (no complete selected runner or
whole-onboarding-only), while citation range resolution is `incremental` with all edge classes and
an executable extractor version cit:([`_POLICIES`], mcp/src/agents_remember/memory_quality/incremental_scope/registry.py:58-105).
`checker_scope_registry()` returns the deterministic sorted population and refuses source drift: the
declared checker set must equal `AVAILABLE_CHECKS`, incremental policies must carry an
extractor version and edge classes, and `full-only` policies must carry neither
cit:([`checker_scope_registry`], mcp/src/agents_remember/memory_quality/incremental_scope/registry.py:108-129).
`checker_registry_version()` fingerprints the whole policy population into one canonical digest
cit:([`checker_registry_version`], mcp/src/agents_remember/memory_quality/incremental_scope/registry.py:132-136).

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

The registry consumes the existing memory-quality checker names (`AVAILABLE_CHECKS`) and the
incremental citation resolver's `claim_reopen`/`range_resolution` plus document-shape and
history-order checkers.

- The checker population is derived from the memory-quality package check catalog. [1]
- The one incremental checker is citation range resolution, whose selected-document mode makes it the only executably incremental policy. [2]
- The manifest binds `checkerRegistryVersion` into every compiled scope. [3]
