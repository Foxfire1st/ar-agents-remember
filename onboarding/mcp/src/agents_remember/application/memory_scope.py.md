# mcp/src/agents_remember/application/memory_scope.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/memory_scope.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T14:19+02:00 |
| lastVerifiedCommitHash |  `f95487ec993b58d34911bba0206a7fa6ef9684eb`|
| lastVerifiedCommitDate |  2026-08-24T15:28:18+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[application/overview.md](overview.md)

## Purpose

Resolves the one canonical official or leaf-local memory-quality scope. It freezes the authority
path, measured code root, onboarding root, and optional unstamped code provenance so synchronous
execution and asynchronous run identity cannot re-derive different work from the same request.

## Code Commentary

### Logic

`resolve_memory_scope` first authorizes `repo_id`. An absent contract selects the configured
official onboarding tree and configured coordination authority. A supplied contract is confined to
the coordination root and delegated to `resolve_leaf_memory_scope`, which requires a leaf contract
for the same repository, its own external-memory worktree, and a live onboarding directory. The
leaf result carries its code worktree, memory worktree, enclosure report path, managed cache
authority, and code-base commit. There is deliberately no leaf-to-official fallback.

`MemoryScopeIdentity` contains only frozen, result-affecting authority facts. `MemoryScope` pairs
that identity with the resolved `Path` and coordination objects required to execute the check.

### Invariants And Boundaries

- `repo_id` and `contract_path` must resolve through configured authority; callers never provide
  arbitrary code or onboarding roots.
- Leaf scope is all-or-nothing: missing, removed, disabled, or cross-repository memory is a loud
  refusal, not an implicit official-memory check.
- The identity records resolved roots and temporary provenance before a background run is admitted.
- The code-base commit is comparison provenance only; this module never writes verification stamps.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies; the authority contract is repository-internal.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Frozen scope identity includes authority and both resolved trees. | `MemoryScopeIdentity` | mcp/src/agents_remember/application/memory_scope.py:27-35 |
| Official scope resolves configured repository and onboarding authority. | `resolve_memory_scope` | mcp/src/agents_remember/application/memory_scope.py:51-88 |
| Leaf scope rejects cross-repository, non-leaf, missing-memory, and removed-worktree cases without fallback. | `resolve_leaf_memory_scope` | mcp/src/agents_remember/application/memory_scope.py:91-143 |

## Cross-Repo References

No meaningful cross-repository implementation reference applies.

## Update History

- 2026-08-24T14:19+02:00 — 260821-DAGQC-L2: created for the canonical frozen memory-scope authority boundary. Verification remains blank until architect-owned closeout stamps the code commit.
