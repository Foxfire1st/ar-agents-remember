# mcp/test_support/agents_remember_test_support/testing/causal_dependency.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/test_support/agents_remember_test_support/testing/causal_dependency.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-28T11:32+02:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
| governingOverview | `overview.md` |

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

## Docs References

No external contract applies.

## Repo-Internal References

`causal_preflight.py` consumes the chains; `causal_route_evidence.py` verifies dependent and
independent execution together.

## Cross-Repo References

No cross-repository boundary applies.

## Update History

- 2026-08-28T11:32+02:00 — Recognized direct imported-class attribute calls as owner calls while
  retaining exact-node, observer-independent causality.

- 2026-08-27T11:08+02:00 — Created to remove observer-induced and file-wide causality.
