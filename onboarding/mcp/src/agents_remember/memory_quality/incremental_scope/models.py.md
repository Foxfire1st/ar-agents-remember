# mcp/src/agents_remember/memory_quality/incremental_scope/models.py

## Governing Overview

[memory quality overview](../overview.md)

## Purpose

Owns strict frozen Git path/delta, task-pair, candidate identity, scope-edge and checker-policy values with one canonical JSON digest spelling. Task observations and memory candidate-pair roots come from their canonical domain owners. The former dependency snapshot, source-index observation, scope node and selected-closure manifest classes are absent.

## Code Commentary

### Logic

`GitPathChange` validates canonical relative paths and status-specific old/new paths/blobs: modified retains one path, renamed changes it. `GitTreeDelta` requires a normalized absolute root and sorted unique exact Git changes. `TaskObservationPair` retains optional base/candidate CanonicalTaskObservation values from the task-domain owner, with exact source/topology/intent identities. `ScopeCandidateIdentity` requires one code and one memory delta matching canonical pair roots and forbids changes on unchanged trees; canonical_value/digest use the strict complete payload. `ScopeEdge` retains exact content/owner/extractor/validator identities and nonblank sorted unique reasons; the removed ScopeNode namespace validator is not part of it. `CheckerScopePolicy` retains checker, mode, optional extractor/edges and nonempty reason; registry validation owns mode-specific shape. SourceIndexObservation, DependencySnapshot and ScopeManifest are absent.

### Conventions

- Every model is extra-forbidden and frozen; unknown JSON fields are never silently dropped.
- `canonical_digest` uses sorted keys, compact separators and ensure_ascii=True for one SHA-256 spelling.
- ScopeEdge reasons are sorted and deduplicated; no removed node/compiler contract is implied.

## Invariants And Boundaries

- Git changes retain exact tree/path/blob evidence rather than mtime inference.
- `ScopeCandidateIdentity` requires one code and one memory delta matching canonical pair roots and forbids changes on unchanged trees.
- These values do not produce snapshots, closure manifests or dependency compilation.

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

- observe_scope_candidate emits the surviving exact candidate identity; removed snapshot owners and manifest compiler do not survive. [4]

- Git change status and path shape are validated by the current typed model. [5]
