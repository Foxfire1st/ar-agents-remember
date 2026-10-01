# mcp/src/agents_remember/worktrees/leaf_refs.py

## Governing Overview

[mcp overview](../../../overview.md)

## Purpose

`leaf_refs.py` is a worktree-contract compatibility resolver. It maps canonical or legacy leaf
references onto task-document ids and enclosure aliases for worktree start, contract writes, and the
explicit heal operation. It is no longer an agent-facing hosted-seat addressing boundary.

## Code Commentary

`resolve_leaf_ref` indexes active task roots, accepts qualified ids, document ids, and unambiguous
legacy aliases, and returns both the repository-qualified historical key and canonical document id.
`LeafRefResolutionError` preserves the bounded not-found/ambiguous vocabulary and suggestions for
worktree callers.

Candidate discovery reads real task documents, ignores unrelated sibling JSON, and fails loudly for
schema-marked malformed task documents. `canonical_leaf_doc_ids` gives contract healing a bounded
per-root skip index. Enclosure resolution accepts proven canonical aliases before its explicit raw
legacy fallback for already-existing contracts.

## Invariants And Boundaries

- New hosted-seat and inbox identity uses `TaskDocumentRef` plus role, not this resolver's leaf key.
- Worktree contracts persist canonical document ids; legacy aliases exist only for controlled
  migration and existing-contract loading.
- Ambiguous aliases fail closed.
- Unrelated JSON artifacts are inert; malformed task documents are not swallowed.

## Evidence

### Docs References

No external domain source governs this repository-local compatibility resolver.

No configured domain documentation was available.

### Repo-Internal References

- Resolution returns canonical document identity or a typed not-found/ambiguous error. [1]
- The bounded canonical-id skip index `canonical_leaf_doc_ids` is built per task root for contract healing. [2]
- The heal sweep `heal_contract_leaf_ids` rewrites legacy leaf ids using that per-root index. [3]
- Worktree start is the live caller of leaf-document resolution. [4]
- Existing enclosure contracts can still be found through proven aliases or the explicit raw legacy path. [5]
