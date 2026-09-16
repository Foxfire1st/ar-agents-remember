# mcp/src/agents_remember/application/memory_scope.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/memory_scope.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-14T20:00+02:00 |
| lastVerifiedCommitHash |  `bb65a2073228c5e143b055a470f39c6c9e2f4d9d`|
| lastVerifiedCommitDate |  2026-09-14T19:36:04+02:00|
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
Acceptance-oriented scope may also retain a selected prepared code view and its history commits: the
prepared physical root is used only for quality reads when it matches the future candidate tree,
while the retained predecessor commits anchor current-candidate provenance; a mismatched prepared
tree yields to current logical candidate bytes, and an incomplete selected output becomes a typed
refusal (`memory_scope.py:172-274`, `_resolve_prepared_code_source`:322-361).

Acceptance-oriented quality calls use `resolve_memory_candidate_scope`: configured admission
still validates repository/enclosure authority, then the canonical pair resolver validates the
exact live code and memory checkouts. A repeated revalidation must reproduce the same pair; moved
identity returns the exact contract-addressed sync route before another scan or publication. The
leaf code base is temporary comparison provenance only. Bare configured-repository calls neither
inherit that leaf provenance nor silently replace an invalid requested leaf.

cit:([`resolve_memory_candidate_scope`], mcp/src/agents_remember/application/memory_scope.py:172-204)
cit:([`revalidate_memory_candidate_scope`], mcp/src/agents_remember/application/memory_scope.py:207-274)
cit:([`_leaf_scope`], mcp/src/agents_remember/application/memory_scope.py:277-319)

### Invariants And Boundaries

- `repo_id` and `contract_path` must resolve through configured authority; callers never provide
  arbitrary code or onboarding roots.
- Leaf scope is all-or-nothing: missing, removed, disabled, or cross-repository memory is a loud
  refusal, not an implicit official-memory check.
- The identity records resolved roots and temporary provenance before a background run is admitted.
- Prepared code is selected from the retained closeout output only when its candidate tree matches;
a stale prepared tree can preserve history context without replacing current logical candidate bytes.
- The code-base commit is comparison provenance only; this module never writes verification stamps.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies; the authority contract is repository-internal.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Frozen scope identity includes authority and both resolved trees. | `MemoryScopeIdentity` | mcp/src/agents_remember/application/memory_scope.py:60-68 |
| Official scope resolves configured repository and onboarding authority. | `resolve_memory_scope` | mcp/src/agents_remember/application/memory_scope.py:105-142 |
| Leaf scope rejects cross-repository, non-leaf, missing-memory, and removed-worktree cases without fallback. | `resolve_leaf_memory_scope` | mcp/src/agents_remember/application/memory_scope.py:145-169 |

| Acceptance scope retains a proved prepared code view and predecessor-history anchors without replacing current candidate identity. | `_resolve_prepared_code_source`; `resolve_memory_candidate_scope` | mcp/src/agents_remember/application/memory_scope.py:172-204; mcp/src/agents_remember/application/memory_scope.py:322-361 |

## Cross-Repo References

No meaningful cross-repository implementation reference applies.

## MCAR-L02 Exact Contract Carry

`MemoryScope` now retains the exact resolved `WorktreeContract` for a leaf scope. That object is
not a second resolver: it lets the post-check readiness join call the same coherence validator
against the already admitted enclosure without guessing from report paths or falling back to
official memory.

## MCAR-L03 Acceptance-Eligible Scope

`resolve_memory_candidate_scope` admits the configured leaf contract and delegates all pair facts
to the canonical resolver. The resulting scope and frozen identity carry the full pair.
`revalidate_memory_candidate_scope` rereads that exact contract and requires byte-for-byte pair
identity equality; official scope remains a separate diagnostic plane with no pair.

Configured-contract refusal translation consumes the canonical public projection as a strict
schema. Required status, detail, evidence, and next-action fields are indexed directly; this
caller does not reconstruct missing values or silently substitute another failure vocabulary.
An invalid projector result is therefore an implementation defect that remains loud.

## Update History

- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator (drift re-verification):
  `mcp/src/agents_remember/application/memory_scope.py` changed since the recorded verification
  commit. Re-read the card against the frozen on-disk source and re-checked its claims and cited
  ranges: nothing this card asserts is falsified by the change, so no wording changed. Verification
  metadata remains closeout-owned; no verification stamp advanced.
- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (drift re-verification): the source moved since
  the recorded verification commit (import-only: the candidate-pair resolvers now live under
  `memory_quality`). Re-read the card against the current source: every cited resolver range is
  still exact and the card never names the moved module path. No wording changed; verification
  metadata remains closeout-owned.
- 2026-09-10T03:45:55+02:00 — CCR-L42 final predecessor-history curation: reconciled current source behavior, retained-history provenance, and exact citation extents; verification metadata remains closeout-owned.

- 2026-09-10T00:00+02:00 — CCR-L42 current-candidate curation: documented selected prepared-source reads and retained history anchoring while preserving current candidate identity; verification metadata remains closeout-owned.
- 2026-09-09T12:22:46+00:00: Generated citation repair: `MemoryScopeIdentity` repointed to mcp/src/agents_remember/application/memory_scope.py:53-62. No content impact: mechanical anchor-range projection bound to citation source snapshot 06f99a0e57ce8b514dd7ed6685874da5285e3ec2e8c4a3f6a5d768b622094451; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-09T12:22:46+00:00: Generated citation repair: `resolve_memory_scope` repointed to mcp/src/agents_remember/application/memory_scope.py:98-135. No content impact: mechanical anchor-range projection bound to citation source snapshot 06f99a0e57ce8b514dd7ed6685874da5285e3ec2e8c4a3f6a5d768b622094451; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-09T12:22:46+00:00: Generated citation repair: `resolve_memory_candidate_scope` repointed to mcp/src/agents_remember/application/memory_scope.py:165-193. No content impact: mechanical anchor-range projection bound to citation source snapshot 06f99a0e57ce8b514dd7ed6685874da5285e3ec2e8c4a3f6a5d768b622094451; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-09T12:22:46+00:00: Generated citation repair: `revalidate_memory_candidate_scope` repointed to mcp/src/agents_remember/application/memory_scope.py:196-258. No content impact: mechanical anchor-range projection bound to citation source snapshot 06f99a0e57ce8b514dd7ed6685874da5285e3ec2e8c4a3f6a5d768b622094451; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-09T12:22:46+00:00: Generated citation repair: `_leaf_scope` repointed to mcp/src/agents_remember/application/memory_scope.py:261-301. No content impact: mechanical anchor-range projection bound to citation source snapshot 06f99a0e57ce8b514dd7ed6685874da5285e3ec2e8c4a3f6a5d768b622094451; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-08-30T07:05+02:00 — MCAR-L03 A008: removed caller-owned fallback reconstruction from
  configured refusal translation. The canonical projector is now the single schema authority.

- 2026-08-30T05:55+02:00 — MCAR-L03 A005: kept configured repository/enclosure authority
  mandatory while delegating live code/memory candidate identity to the shared exact-pair
  validator. Missing worktrees now retain the pair field and repair vocabulary instead of being
  flattened into a generic configured-authority refusal.

- 2026-08-29T21:46+02:00 — MCAR-L03: separated official diagnostics from strict pair-bound leaf
  acceptance and added exact revalidation. Verification remains closeout-owned.

- 2026-08-29T08:52+02:00 — Added the resolved leaf contract to memory scope for shared coherence
  validation. Verification remains closeout-owned.

- 2026-08-24T14:19+02:00 — 260821-DAGQC-L2: created for the canonical frozen memory-scope authority boundary. Verification remains blank until architect-owned closeout stamps the code commit.
