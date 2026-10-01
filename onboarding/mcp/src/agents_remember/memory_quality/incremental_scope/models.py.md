# mcp/src/agents_remember/memory_quality/incremental_scope/models.py

## Governing Overview

[memory quality overview](../overview.md)

## Purpose

Owns the immutable evidence vocabulary of CCR-R06@v2's content-addressed memory dependency scope:
the exact Git tree delta and task observation inputs, the scope candidate identity, the
owner-produced dependency snapshot, and the deterministic selected-closure manifest. Every value is
a frozen, strict pydantic model whose canonical JSON spelling is the digest input
cit:([`MANIFEST_SCHEMA`, `SNAPSHOT_SCHEMA`, `canonical_digest`], mcp/src/agents_remember/memory_quality/incremental_scope/models.py:27-28; mcp/src/agents_remember/memory_quality/incremental_scope/models.py:31-35).

## Code Commentary

### Logic

`GitPathChange` validates that old/new path and blob shape match the change status and requires
canonical repository-relative POSIX paths without empty, dot, or traversal segments
cit:([`GitPathChange`], mcp/src/agents_remember/memory_quality/incremental_scope/models.py:43-80). `GitTreeDelta`
pins one code or memory delta to exact Git tree identities and a deterministically sorted, unique
change tuple cit:([`GitTreeDelta`], mcp/src/agents_remember/memory_quality/incremental_scope/models.py:82-111).
`CanonicalTaskObservation` records the task source digest and namespace plus the canonical R01
(semantic-topology/v2) and R02 (task intent) projections; `TaskObservationPair` content-addressed
base/candidate form distinguishes a leaf's door baseline from its live task observation
cit:(["class CanonicalTaskObservation"], mcp/src/agents_remember/models/task_document.py:44-69).
`ScopeCandidateIdentity` demands one code and one memory delta whose roots equal the canonical
memory candidate pair roots and refuses changed roots on an unchanged tree
cit:([`ScopeCandidateIdentity`], mcp/src/agents_remember/memory_quality/incremental_scope/models.py:121-148).
`ScopeNode` restricts node ids to canonical `code:`/`memory:` paths or the two typed task nodes,
while `ScopeEdge` carries the owner-declared edge class, content digest, extractor/validator
versions, and sorted unique reasons cit:([`ScopeNode`, `ScopeEdge`], mcp/src/agents_remember/memory_quality/incremental_scope/models.py:151-182; mcp/src/agents_remember/memory_quality/incremental_scope/models.py:185-202).
`SourceIndexObservation` binds a leased citation source-index generation to exact roots
and candidate digest; `DependencySnapshot` freezes nodes, edges, per-class evidence, and a
self-verifying snapshot digest; `ScopeManifest` is the deterministic selected closure with
`incrementalReady` flag cit:([`SourceIndexObservation` .. `ScopeManifest`], mcp/src/agents_remember/memory_quality/incremental_scope/models.py:214-233; mcp/src/agents_remember/memory_quality/incremental_scope/models.py:258-271).

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

### Current source-selection contract

CanonicalTaskObservation is imported from models/task_document.py, the task-domain owner of its closed immutable shape, normalized absolute task root and exact source/topology/intent identities. This module composes those observations into TaskObservationPair and ScopeCandidateIdentity; it no longer declares or publicly re-exports a duplicate task-observation class.

- `TaskObservationPair` carries the current contract described above. [1]

## Evidence

### Docs References

No configured Domain Documentation applies; the scope vocabulary is repository-owned.

The schema vocabulary has no external authority.

### Repo-Internal References

The models consume the R01/R02 and memory-candidate pair authorities that CCR-R06@v2 declares as
prerequisites (`TaskIntentState`, `TaskDocumentRef`, `MemoryCandidatePairIdentity`), and their
values are produced/validated by the sibling scope modules.

- Task intent and document ref types come from the R02 task-intent owner. [2]
- Pair identity roots are the canonical code/memory pair authority. [3]
- The candidate builder emits `ScopeCandidateIdentity`; owner adapters emit `DependencySnapshot`; the compiler closes the closure into `ScopeManifest`. [4]
- Git change status and path shape are validated by the current typed model. [5]
