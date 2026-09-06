# mcp/src/agents_remember/memory_quality/incremental_scope/owners.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/incremental_scope/owners.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T00:23:26+00:00 |
| lastVerifiedCommitHash | `97e8ed2e1fae21756c3ad995c30613d4fbfcc503` |
| lastVerifiedCommitDate | 2026-09-06T02:09:33+02:00 |
| governingOverview | `../overview.md` |

## Governing Overview

[memory quality overview](../overview.md)

## Purpose

Read-only adapters over the existing dependency fact owners for CCR-R06@v2: they compose the
canonical route-index, citation source-index, entity catalog, and Git tree observations into the
immutable `DependencySnapshot`. These are the owner-bound extractors for source-to-sidecar,
source-to-governing-route, source-to-citing-memory-document, source-to-entity-manifestation, and
route-index dependency edges cit:([`observe_dependency_snapshot`], mcp/src/agents_remember/memory_quality/incremental_scope/owners.py:59-97).

## Code Commentary

### Logic

`DependencyOwnerContext` and `ContractDependencyAuthority` are the frozen adapter seam; observe
refuses roots that do not equal the candidate pair (`dependency-root-mismatch`)
cit:([`DependencyOwnerContext`, `ContractDependencyAuthority`], mcp/src/agents_remember/memory_quality/incremental_scope/owners.py:39-97).
`observe_source_index` leases one existing citation source-index generation and cross-checks
readiness, manifest, roots, snapshot and counts before accepting it. The lease, ready record and
manifest must each select the exact candidate Git tree; a policy or tree mismatch refuses as
`source-index-candidate-mismatch`. Stale or malformed generations are
`source-index-stale` / `source-index-malformed` refusals
cit:([`observe_source_index`], mcp/src/agents_remember/memory_quality/incremental_scope/owners.py:100-152).
`observe_git_nodes` reads content addresses from the exact candidate/base trees plus every diff
endpoint, refusing `git-node-missing` when no blob exists
cit:([`observe_git_nodes`, `_tree_entries`], mcp/src/agents_remember/memory_quality/incremental_scope/owners.py:155-181; mcp/src/agents_remember/memory_quality/incremental_scope/owners.py:335-344).
The five extractors map: coveredFiles to `memory:onboarding/<source>.md` sidecars; every indexed
source to its complete governing overview chain; citation claims to their citing documents (with
`citation-source-escape` refusal for resolution outside the roots); entity fingerprint evidence
paths to `entities.md`; and overview/sidecar/child-index inputs to each generated route index
cit:([`extract_file_sidecar_edges`, `extract_governing_route_edges`, `extract_citation_edges`, `extract_entity_edges`, `extract_route_index_edges`], mcp/src/agents_remember/memory_quality/incremental_scope/owners.py:184-289).
`_current_route_indexes` rebuilds the route-index owner's exact dry-run population and refuses
stale or extra/missing documents; `_require_index_matches_candidate` cross-checks the source-index
candidate-aware Git census and per-member Git blob and indexed body content against the exact
candidate tree. Census failures are typed refusals; citation extraction also supplies that explicit
tree to the citation resolver
cit:([`_current_route_indexes`, `_require_index_matches_candidate`], mcp/src/agents_remember/memory_quality/incremental_scope/owners.py:292-397).

### Conventions

- All facts come from owner outputs (Git trees, route-index JSON, citation grammar, entity
  fingerprint rows); mtimes and caller-supplied names are never read as authority.
- `_tree_entries` parses `git ls-tree -r -z` and strips the canonical trailing NUL before splitting
  records (the bounded R06 repair noted in the L26 worker delivery).
- Pairs are de-duplicated and deterministically sorted before edges are built.

## Invariants And Boundaries

- The snapshot is bound to the exact candidate digest and roots; any mismatch is a typed refusal.
- A stale or malformed route/citation/entity index population fails closed; no partial population is
  accepted and no full-scan fallback masks the refusal.
- Edge emission is restricted to the canonical owner contracts declared in the registry — owners
  never invent edge classes or authorities.
- Missing dependency facts block incremental reuse; they never silently shrink the closure.

## Docs References

No configured Domain Documentation applies; the owner adapters follow the existing memory-quality
citation and route-index contracts.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain documentation governs owner observation. | — | — |

## Repo-Internal References

The owner adapters reuse the existing citation `source_index`, route-index builder, citation
grammar (`claim_reopen`), entity fingerprint parser, and Git helpers.

| Finding | Anchor | Source |
| --- | --- | --- |
| The citation source-index lease and schema-9 ready/manifest generations with explicit candidate selection. | `source_index.RepositoryIndex`; `ReadyGeneration`; `Manifest` | mcp/src/agents_remember/memory_quality/style/citations/source_index_state.py:61-152; mcp/src/agents_remember/memory_quality/style/citations/source_index_state.py:253-298; mcp/src/agents_remember/memory_quality/style/citations/source_index.py:156-237 |
| Route-index population is generated by the existing kernel route-index owner. | `build_route_indexes` | mcp/src/agents_remember/kernel/route_index.py:184-233 |
| Citation claims and entity fingerprint rows come from existing style modules. | `claims_in`; `parse_entity_fingerprint_rows` | mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:205-221; mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/entities.py:84-115 |
| Dependency observation composes the canonical owner extractors; deleted tests do not establish present coverage. | `observe_dependency_snapshot` | mcp/src/agents_remember/memory_quality/incremental_scope/owners.py:59-97 |

## Update History

- 2026-09-06T00:23:26+00:00 — L30 recovery: Documented explicit Git-candidate source-index observation, census and citation composition; verified against actual code commit 97e8ed2e1fae21756c3ad995c30613d4fbfcc503.

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for 1ad9d51f743c5b17de51cc46d8b29e004736022d (CCR-R06@v2/L26): created the card for the new dependency-owner adapters of the R06v2 successor leaf; no prior sidecar existed.