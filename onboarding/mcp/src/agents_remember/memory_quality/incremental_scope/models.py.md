# mcp/src/agents_remember/memory_quality/incremental_scope/models.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/incremental_scope/models.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | `1ad9d51f743c5b17de51cc46d8b29e004736022d` |
| lastVerifiedCommitDate | 2026-09-02T06:25:51+02:00 |
| governingOverview | `../overview.md` |

## Governing Overview

[memory quality overview](../overview.md)

## Purpose

Owns the immutable evidence vocabulary of CCR-R06@v2's content-addressed memory dependency scope:
the exact Git tree delta and task observation inputs, the scope candidate identity, the
owner-produced dependency snapshot, and the deterministic selected-closure manifest. Every value is
a frozen, strict pydantic model whose canonical JSON spelling is the digest input
cit:([`MANIFEST_SCHEMA`, `SNAPSHOT_SCHEMA`, `canonical_digest`], mcp/src/agents_remember/memory_quality/incremental_scope/models.py:28-36).

## Code Commentary

### Logic

`GitPathChange` validates that old/new path and blob shape match the change status and requires
canonical repository-relative POSIX paths without empty, dot, or traversal segments
cit:([`GitPathChange`], mcp/src/agents_remember/memory_quality/incremental_scope/models.py:43-80). `GitTreeDelta`
pins one code or memory delta to exact Git tree identities and a deterministically sorted, unique
change tuple cit:([`GitTreeDelta`], mcp/src/agents_remember/memory_quality/incremental_scope/models.py:83-112).
`CanonicalTaskObservation` records the task source digest and namespace plus the canonical R01
(semantic-topology/v2) and R02 (task intent) projections; `TaskObservationPair` content-addressed
base/candidate form distinguishes a leaf's door baseline from its live task observation
cit:([`CanonicalTaskObservation`, `TaskObservationPair`], mcp/src/agents_remember/memory_quality/incremental_scope/models.py:115-145).
`ScopeCandidateIdentity` demands one code and one memory delta whose roots equal the canonical
memory candidate pair roots and refuses changed roots on an unchanged tree
cit:([`ScopeCandidateIdentity`], mcp/src/agents_remember/memory_quality/incremental_scope/models.py:148-175).
`ScopeNode` restricts node ids to canonical `code:`/`memory:` paths or the two typed task nodes,
while `ScopeEdge` carries the owner-declared edge class, content digest, extractor/validator
versions, and sorted unique reasons cit:([`ScopeNode`, `ScopeEdge`], mcp/src/agents_remember/memory_quality/incremental_scope/models.py:178-229).
`SourceIndexObservation` binds a leased citation source index generation (schema v8) to exact roots
and candidate digest; `DependencySnapshot` freezes nodes, edges, per-class evidence, and a
self-verifying snapshot digest; `ScopeManifest` is the deterministic selected closure with
`incrementalReady` flag cit:([`SourceIndexObservation` .. `ScopeManifest`], mcp/src/agents_remember/memory_quality/incremental_scope/models.py:241-298).

### Conventions

- Every model is extra-forbidden and frozen; unknown JSON fields are never silently dropped.
- `canonical_digest` uses JSON dumps with sorted keys and compact separators so one canonical
  spelling yields one SHA-256 for all digest consumers.
- Edges and nodes carry reasons sorted and de-duplicated; digests are computed by the compiler
  over the same canonical payload shape used by validation.

## Invariants And Boundaries

- Changed roots are never inferred from names or mtimes — only from exact Git tree diffs and
  changed canonical task observations.
- A Snapshot/Manifest is bound to exactly one candidate digest; binding refusals happen in the
  compiler/owners, not here.
- The manifest is an evidence artifact: it records semantic-topology and task-intent digests but
  never reconstructs or overrides their canonical owners.
- Node ids outside code/memory namespaces or the two typed task identities are invalid, preventing
  fabricated dependency endpoints.

## Docs References

No configured Domain Documentation applies; the scope vocabulary is repository-owned.

| Finding | Anchor | Source |
| --- | --- | --- |
| The schema vocabulary has no external authority. | — | — |

## Repo-Internal References

The models consume the R01/R02 and memory-candidate pair authorities that CCR-R06@v2 declares as
prerequisites (`TaskIntentState`, `TaskDocumentRef`, `MemoryCandidatePairIdentity`), and their
values are produced/validated by the sibling scope modules.

| Finding | Anchor | Source |
| --- | --- | --- |
| Task intent and document ref types come from the R02 task-intent owner. | `TaskIntentState`, `TaskDocumentRef` | mcp/src/agents_remember/models/task_intent/__init__.py:55-80; mcp/src/agents_remember/models/task_document_ref.py:18-36 |
| Pair identity roots are the canonical code/memory pair authority. | `MemoryCandidatePairIdentity` | mcp/src/agents_remember/models/lifecycles/memory_candidate.py:10-36 |
| The candidate builder emits `ScopeCandidateIdentity`; owner adapters emit `DependencySnapshot`; the compiler closes the closure into `ScopeManifest`. | `observe_scope_candidate`, `observe_dependency_snapshot`, `compile_scope_manifest` | mcp/src/agents_remember/memory_quality/incremental_scope/candidate.py:51-99; mcp/src/agents_remember/memory_quality/incremental_scope/owners.py:59-97; mcp/src/agents_remember/memory_quality/incremental_scope/compiler.py:98-159 |
| Individual digest and node/edge shape behaviors are covered by the scope test suites. | `test_exact_tree_diff_classifies_add_modify_delete_and_both_rename_ends`; `test_all_five_owner_extractors_emit_exact_content_addressed_edges` | mcp/tests/test_memory_incremental_scope_candidate.py:43-70; mcp/tests/test_memory_incremental_scope_owners.py:85-163 |

## Update History

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for 1ad9d51f743c5b17de51cc46d8b29e004736022d (CCR-R06@v2/L26): created the card for the new immutable scope models introduced by the R06v2 successor leaf; no prior sidecar existed.