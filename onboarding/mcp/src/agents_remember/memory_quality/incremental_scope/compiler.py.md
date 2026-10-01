# mcp/src/agents_remember/memory_quality/incremental_scope/compiler.py

## Governing Overview

[memory quality overview](../overview.md)

## Purpose

The fail-closed compiler of CCR-R06@v2's complete reverse memory dependency closure. It composes
the observed candidate and dependency snapshot into one deterministic `ScopeManifest` whose
selected nodes/edges prove every dependency of the changed roots, and refuses every unproven state
with a typed `ScopeUnprovenError` — no silent full-scan fallback and no private authority
cit:([`compile_scope_manifest`], mcp/src/agents_remember/memory_quality/incremental_scope/compiler.py:98-159).

## Code Commentary

### Logic

`dependency_edge` builds one self-verifying edge under the canonical owner contract:
contentDigest is the canonical digest of the edge payload minus the digest field
cit:([`dependency_edge`], mcp/src/agents_remember/memory_quality/incremental_scope/compiler.py:43-61).
`build_dependency_snapshot` freezes already-observed nodes/edges with per-edge-class evidence and a
self-verifying snapshot digest cit:([`build_dependency_snapshot`], mcp/src/agents_remember/memory_quality/incremental_scope/compiler.py:64-95).
`compile_scope_manifest` observes the candidate and snapshot, selects the requested checker
policies, validates candidate and snapshot, injects the two canonical task nodes
(`task:normative-intent`, `task:semantic-topology`), computes changed roots, runs the reverse
closure, and re-observes the authority to refuse `candidate-moved-during-compilation`
cit:([`compile_scope_manifest`], mcp/src/agents_remember/memory_quality/incremental_scope/compiler.py:98-159).
Validation routines refuse empty/unknown checker populations (`_selected_policies`), missing
base/candidate R01 topology or R02 intent (`_validate_candidate`), snapshot/candidate mismatches,
non-canonical ordering, and digest self-verification failures (`_validate_snapshot`,
`_validate_edges`), and changed roots without their canonical owner node (`_validate_roots`)
cit:([`_selected_policies`, `_validate_candidate`, `_validate_snapshot`, `_validate_edges`, `_validate_roots`], mcp/src/agents_remember/memory_quality/incremental_scope/compiler.py:162-323).
`_reverse_closure` performs a deterministic BFS from the changed roots over owner-validated edges,
refusing edges whose endpoints are absent cit:([`_reverse_closure`], mcp/src/agents_remember/memory_quality/incremental_scope/compiler.py:326-351).

### Conventions

- All outputs are deterministically sorted; the manifest digest covers the full canonical payload.
- `incrementalReady` is `not full_only`: the presence of any truly full-only checker keeps the
  manifest non-incremental instead of pretending reuse readiness.
- Refusal codes name the exact failing checker, node, edge class, snapshot, candidate, or owner.

## Invariants And Boundaries

- The compiler composes exact owner outputs; it cannot invent edges, identities, or content.
- Addendum: an unknown checker, missing edge class, stale/malformed index, ambiguous task/memory
  pair, unavailable topology/intent, or unclassified changed root makes the scope `unproven`.
- No semantic no-impact inference from an absent edge, and no acceptance of an incomplete manifest
  because a prior full scan passed.
- The candidate is re-observed after closure so a moved authority cannot be silently reused.

## Evidence

### Docs References

No configured Domain Documentation applies; the compiler contract is the CCR-R06@v2 packet.

The fail-closed closure contract is repository-owned.

### Repo-Internal References

The compiler is driven by the sibling candidate and owners modules and consumes the R01/R02
identity types directly.

- Candidate and dependency observations feed the compiler through the two authority protocols. [1]
- The manifest's `MCP`-visible schema and digest fields are declared in the scope models. [2]
