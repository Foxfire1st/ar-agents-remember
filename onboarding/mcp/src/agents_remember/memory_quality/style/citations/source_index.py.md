# mcp/src/agents_remember/memory_quality/style/citations/source_index.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/style/citations/source_index.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview | `../../overview.md` |

## Governing Overview

[overview](../../overview.md)

## Purpose

Persistent source acquisition for repository-wide citation anchor lookup.

## Code Commentary

### Logic

Module-level surface:

- `SourceIndexError` (class, lines 98-99) — The requested source snapshot cannot be indexed safely.
- `SourceTreeChangedError` (class, lines 102-103) — The code tree changed while an index generation was being built.
- `IndexMetrics` (class, lines 114-128) — Observable acquisition work for cold, warm, and metadata-refresh paths.
- `CachePaths` (class, lines 135-143)
- `PublicationBoundary` (class, lines 147-150)
- `RepositoryIndex` (class, lines 157-231) — A shared-lock lease on one complete immutable source snapshot.
- `cache_root` (function, lines 234-240) — One fixed-slot cache root shared by every application schema generation.
- `cache_paths` (function, lines 243-277)
- `validate_expected_snapshot` (function, lines 280-285) — Reject every spelling except the canonical lowercase SHA-256 generation id.
- `validate_operation_scope` (function, lines 288-314) — Validate document/generation authority before an operation performs any work.
- `open_repository_index` (function, lines 317-384) — Open a source index through the default safe path or an explicit frozen lease.
- `build_repository_index` (function, lines 387-394) — Explicit frozen-wave prebuild; a current generation is reused rather than rebuilt.
- `_open_expected_generation` (function, lines 397-435) — Lease one prevalidated generation without source-tree or full-manifest work.
- `_repository_index` (function, lines 438-453)
- `_open_shared_lock` (function, lines 456-462)
- `code_files` (function, lines 465-467) — The source files the citation resolver considers, in current candidate order.
- `_current_generation` (function, lines 470-497)
- `_open_database` (function, lines 500-510)
- `_ready_generation` (function, lines 513-520)
- `_validate` (function, lines 523-559)
- `_build_and_publish` (function, lines 562-570)
- `_build_once` (function, lines 573-649)
- `_validate_temporary_database` (function, lines 652-664) — Run the expensive SQLite and application checks before publication is possible.
- `_publish_generation` (function, lines 667-692) — Publish SQLite and manifest while the absent/last readiness marker is authority.
- `_tree_state` (function, lines 695-728)
- `_stable_read` (function, lines 731-742)
- `_check_source_bounds` (function, lines 745-763)
- `_snapshot_id` (function, lines 766-773)
- `_identities` (function, lines 776-777)
- `_refreshed_manifest` (function, lines 780-792)
- `_cache_bytes` (function, lines 795-800)
- `_reclaim_temps` (function, lines 803-807) — A dead publisher leaves at most one temp; the next exclusive publisher removes it.
- `_reclaim_legacy_cache_roots` (function, lines 810-839) — Remove version-named predecessors before this process can publish or query.
- `_reclaim_legacy_root` (function, lines 842-864)
- `_remove_cache_tree` (function, lines 867-874)
- `_exclusive_lock_with_timeout` (function, lines 877-888)
- `_reclamation_time_remaining` (function, lines 891-895)
- `_under` (function, lines 898-900)

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.

### Todos

None.

## Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| Defines the class `SourceIndexError` (lines 98-99) — The requested source snapshot cannot be indexed safely.. | `SourceIndexError` | mcp/src/agents_remember/memory_quality/style/citations/source_index.py:98-99 |
| Defines the class `SourceTreeChangedError` (lines 102-103) — The code tree changed while an index generation was being built.. | `SourceTreeChangedError` | mcp/src/agents_remember/memory_quality/style/citations/source_index.py:102-103 |
| Defines the class `IndexMetrics` (lines 114-128) — Observable acquisition work for cold, warm, and metadata-refresh paths.. | `IndexMetrics` | mcp/src/agents_remember/memory_quality/style/citations/source_index.py:114-128 |
| Defines the class `CachePaths` (lines 135-143). | `CachePaths` | mcp/src/agents_remember/memory_quality/style/citations/source_index.py:135-143 |
| Defines the class `PublicationBoundary` (lines 147-150). | `PublicationBoundary` | mcp/src/agents_remember/memory_quality/style/citations/source_index.py:147-150 |
| Defines the class `RepositoryIndex` (lines 157-231) — A shared-lock lease on one complete immutable source snapshot.. | `RepositoryIndex` | mcp/src/agents_remember/memory_quality/style/citations/source_index.py:157-231 |
| Defines the function `cache_root` (lines 234-240) — One fixed-slot cache root shared by every application schema generation.. | `cache_root` | mcp/src/agents_remember/memory_quality/style/citations/source_index.py:234-240 |
| Defines the function `cache_paths` (lines 243-277). | `cache_paths` | mcp/src/agents_remember/memory_quality/style/citations/source_index.py:243-277 |
| Defines the function `validate_expected_snapshot` (lines 280-285) — Reject every spelling except the canonical lowercase SHA-256 generation id.. | `validate_expected_snapshot` | mcp/src/agents_remember/memory_quality/style/citations/source_index.py:280-285 |
| Defines the function `validate_operation_scope` (lines 288-314) — Validate document/generation authority before an operation performs any work.. | `validate_operation_scope` | mcp/src/agents_remember/memory_quality/style/citations/source_index.py:288-314 |
| Defines the function `open_repository_index` (lines 317-384) — Open a source index through the default safe path or an explicit frozen lease.. | `open_repository_index` | mcp/src/agents_remember/memory_quality/style/citations/source_index.py:317-384 |
| Defines the function `build_repository_index` (lines 387-394) — Explicit frozen-wave prebuild; a current generation is reused rather than rebuilt.. | `build_repository_index` | mcp/src/agents_remember/memory_quality/style/citations/source_index.py:387-394 |
| Defines the function `_open_expected_generation` (lines 397-435) — Lease one prevalidated generation without source-tree or full-manifest work.. | `_open_expected_generation` | mcp/src/agents_remember/memory_quality/style/citations/source_index.py:397-435 |
| Defines the function `_repository_index` (lines 438-453). | `_repository_index` | mcp/src/agents_remember/memory_quality/style/citations/source_index.py:438-453 |
| Defines the function `_open_shared_lock` (lines 456-462). | `_open_shared_lock` | mcp/src/agents_remember/memory_quality/style/citations/source_index.py:456-462 |
| Defines the function `code_files` (lines 465-467) — The source files the citation resolver considers, in current candidate order.. | `code_files` | mcp/src/agents_remember/memory_quality/style/citations/source_index.py:465-467 |
| Defines the function `_current_generation` (lines 470-497). | `_current_generation` | mcp/src/agents_remember/memory_quality/style/citations/source_index.py:470-497 |
| Defines the function `_open_database` (lines 500-510). | `_open_database` | mcp/src/agents_remember/memory_quality/style/citations/source_index.py:500-510 |
| Defines the function `_ready_generation` (lines 513-520). | `_ready_generation` | mcp/src/agents_remember/memory_quality/style/citations/source_index.py:513-520 |
| Defines the function `_validate` (lines 523-559). | `_validate` | mcp/src/agents_remember/memory_quality/style/citations/source_index.py:523-559 |
| Defines the function `_build_and_publish` (lines 562-570). | `_build_and_publish` | mcp/src/agents_remember/memory_quality/style/citations/source_index.py:562-570 |
| Defines the function `_build_once` (lines 573-649). | `_build_once` | mcp/src/agents_remember/memory_quality/style/citations/source_index.py:573-649 |
| Defines the function `_validate_temporary_database` (lines 652-664) — Run the expensive SQLite and application checks before publication is possible.. | `_validate_temporary_database` | mcp/src/agents_remember/memory_quality/style/citations/source_index.py:652-664 |
| Defines the function `_publish_generation` (lines 667-692) — Publish SQLite and manifest while the absent/last readiness marker is authority.. | `_publish_generation` | mcp/src/agents_remember/memory_quality/style/citations/source_index.py:667-692 |
| Defines the function `_tree_state` (lines 695-728). | `_tree_state` | mcp/src/agents_remember/memory_quality/style/citations/source_index.py:695-728 |
| Defines the function `_stable_read` (lines 731-742). | `_stable_read` | mcp/src/agents_remember/memory_quality/style/citations/source_index.py:731-742 |
| Defines the function `_check_source_bounds` (lines 745-763). | `_check_source_bounds` | mcp/src/agents_remember/memory_quality/style/citations/source_index.py:745-763 |
| Defines the function `_snapshot_id` (lines 766-773). | `_snapshot_id` | mcp/src/agents_remember/memory_quality/style/citations/source_index.py:766-773 |
| Defines the function `_identities` (lines 776-777). | `_identities` | mcp/src/agents_remember/memory_quality/style/citations/source_index.py:776-777 |
| Defines the function `_refreshed_manifest` (lines 780-792). | `_refreshed_manifest` | mcp/src/agents_remember/memory_quality/style/citations/source_index.py:780-792 |

## Update History

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
