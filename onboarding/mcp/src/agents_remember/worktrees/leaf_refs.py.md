# mcp/src/agents_remember/worktrees/leaf_refs.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/leaf_refs.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-11T12:25+02:00 |
| lastVerifiedCommitHash | `d9a1eb82849baea6c0b86735e772a932f4bbdc7c` |
| lastVerifiedCommitDate | 2026-08-12T00:45:15+02:00|
| governingOverview | `../../../overview.md` |

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

## Docs References

No external domain source governs this repository-local compatibility resolver.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Resolution returns canonical document identity or a typed not-found/ambiguous error. | `resolve_leaf_ref`; `LeafRefResolutionError` | mcp/src/agents_remember/worktrees/leaf_refs.py:39-68; mcp/src/agents_remember/worktrees/leaf_refs.py:88-141 |
| Contract healing uses the bounded canonical-id index. | `canonical_leaf_doc_ids`; `heal_contract_leaf_ids` | mcp/src/agents_remember/worktrees/leaf_refs.py:144-154; mcp/src/agents_remember/worktrees/worktree_contract.py:478-526 |
| Worktree start is the live caller of leaf-document resolution. | `resolve_start_leaf_doc_id` | mcp/src/agents_remember/worktrees/modules/leaf_ref_start.py:15-32 |
| Existing enclosure contracts can still be found through proven aliases or the explicit raw legacy path. | `resolve_leaf_enclosure_contract_for_ref` | mcp/src/agents_remember/worktrees/leaf_refs.py:175-222 |

## Update History

- 2026-08-11T12:25+02:00 — Removed obsolete hosted-seat references and clarified the surviving
  worktree compatibility scope. Verification remains pinned pending governed closeout.
- 2026-08-01T09:20+02:00 — The not-found/ambiguous status vocabulary was centralized at its producer.
- 2026-07-07T20:50+02:00 — Through 2026-07-12, candidate discovery, task-document validation, legacy alias
  handling, and bounded contract-heal indexing were established.
