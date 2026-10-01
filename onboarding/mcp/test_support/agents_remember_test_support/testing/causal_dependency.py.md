# mcp/test_support/agents_remember_test_support/testing/causal_dependency.py

## Governing Overview

[Python test evidence infrastructure](overview.md)

## Purpose

Derives exact test nodes whose source/helper/fixture chain independently consumes a failed
high-fanout contract owner.

## Code Commentary

### Logic

The analyzer starts from explicit contract owners, traces source-derived imports and selected
helper/fixture calls into exact nodes, and emits one real chain. Observer and reporting modules are
not traversed as product causality. Owner-call recognition includes direct imports of an owner
class followed by an attribute call, preserving the real source chain without observer edges.

### Conventions

Unproven nodes are runnable, never implicitly blocked.

### Invariants And Boundaries

- Causal identity is contract plus exact node, not file membership.
- Dynamic or ambiguous dependency truth cannot authorize suppression.
- Same-file independent nodes remain visible.

### Todos

Expand the prerequisite registry only from measured high-fanout evidence.

## Evidence

### Docs References

No external contract applies.

### Repo-Internal References

`causal_preflight.py` consumes the chains; `causal_route_evidence.py` verifies dependent and
independent execution together.

### Cross-Repo References

No cross-repository boundary applies.
