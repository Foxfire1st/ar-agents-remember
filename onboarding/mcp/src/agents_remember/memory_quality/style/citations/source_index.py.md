# mcp/src/agents_remember/memory_quality/style/citations/source_index.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/style/citations/source_index.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T02:22:00+02:00 |
| lastVerifiedCommitHash | `97e8ed2e1fae21756c3ad995c30613d4fbfcc503` |
| lastVerifiedCommitDate | 2026-09-06T02:09:33+02:00 |
| governingOverview | `../../overview.md` |

## Governing Overview

[overview](../../overview.md)

## Purpose

Acquire and lease a persistent citation source index while keeping ordinary filesystem freshness checks and explicit Git-candidate selection distinct.

## Code Commentary

### Logic

`open_repository_index` validates the current generation under a shared lock, upgrades to the existing exclusive publisher lock when needed, and returns a shared-lock `RepositoryIndex` lease. Ordinary acquisition enumerates the eligible filesystem population and stats its files; changed identities cause content checks, a metadata-only manifest refresh when bytes match, or a rebuilt generation when content differs.

When `Trees` carries a candidate tree, `_tree_state` delegates population and working-byte proof to its `GitSourceCandidate`. Ordinary traversal remains Git-independent and retains eligible dirty, untracked, and ignored files; it excludes its declared directories/suffixes and VCS marker files, including a linked checkout's `.git` file.

An explicit `expected_snapshot` opens only the existing matching generation. It reads bounded readiness and database metadata, verifies roots and candidate selection, and performs no source census, manifest deserialization, rebuild, or fallback. This path requires the caller to keep the source wave frozen after an integrity-checked build.

Builds apply the shared source bounds, read stable content, populate and validate a temporary database, reobserve source identities, and publish database/manifest/readiness through the existing publication protocol. The content snapshot hashes indexed paths and content hashes; candidate-tree identity is carried and checked separately. `RepositoryIndex.candidate_tree` exposes that selection to downstream consumers.

### Conventions

`source_index_state` owns source identities, manifests, readiness, errors, and input limits; `source_index_database` owns storage and anchor queries. Unmanaged caches use four fixed slots selected by the code/memory roots. Managed namespace authority remains with `source_index_cache`; candidate trees do not allocate additional cache roots.

### Invariants And Boundaries

- Readiness, manifest, database, and requested roots/candidate selection must agree before a generation is used; equal indexed content does not waive a different candidate-tree identity.
- A shared index lease protects immutable index publication, not source files. An expected snapshot is an explicit frozen-wave assertion.
- Input limits are checked before build-time file-body reads. Candidate Git hashing enforces the same limits in its own owner; it is separate from the Python source-read telemetry recorded here.

### Todos

None.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| A generation is leased with query telemetry and its candidate selection. | `RepositoryIndex` | mcp/src/agents_remember/memory_quality/style/citations/source_index.py:156-237 |
| Managed authority or root-keyed fixed slots select cache storage. | `cache_paths` | mcp/src/agents_remember/memory_quality/style/citations/source_index.py:249-283 |
| Default acquisition validates, refreshes, or rebuilds under the existing locks. | `open_repository_index` | mcp/src/agents_remember/memory_quality/style/citations/source_index.py:323-390 |
| Frozen acquisition uses bounded published metadata and refuses an unavailable expected snapshot. | `_open_expected_generation` | mcp/src/agents_remember/memory_quality/style/citations/source_index.py:403-442 |
| Readiness must match both roots and the exact candidate selection. | `_ready_generation` | mcp/src/agents_remember/memory_quality/style/citations/source_index.py:522-532 |
| Changed source identities drive content and metadata refresh decisions. | `_validate` | mcp/src/agents_remember/memory_quality/style/citations/source_index.py:535-572 |
| A bounded, validated temporary database is tied to repeated source observations before publication. | `_build_once` | mcp/src/agents_remember/memory_quality/style/citations/source_index.py:586-664 |
| Candidate census and ordinary filesystem traversal retain separate selection semantics. | `_tree_state` | mcp/src/agents_remember/memory_quality/style/citations/source_index.py:710-755 |
| Snapshot identity hashes indexed paths and content hashes. | `_snapshot_id` | mcp/src/agents_remember/memory_quality/style/citations/source_index.py:772-779 |

## Update History

- 2026-09-06T02:22:00+02:00 — L30 recovery source review: Documented candidate census acquisition and frozen-generation identity checks while preserving ordinary filesystem freshness, fixed cache slots, and publication ownership. Verified against prepared code commit `97e8ed2e1fae21756c3ad995c30613d4fbfcc503`; source review does not claim Gate-5 execution or recovery acceptance.

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
