# mcp/src/agents_remember/memory/knowledge_index/cache.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge_index/cache.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T08:24:55+02:00 |
| lastVerifiedCommitHash | `aa07b1c937d1dc01ea6c51d0582eaf3871afcc8d`|
| lastVerifiedCommitDate | 2026-09-29T09:20:54+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[memory route overview](../overview.md)

## Purpose

**The index cache: one SQLite file per tree key, untracked, rebuilt when absent (MIK-R23 rules 2, 4, 5).** It keeps `<tree-key>.sqlite` files in one directory — by default `<coordination-root>/runtime/knowledge-index/` — reuses a file that matches its key and format, builds anything else, evicts old files, and refuses any location inside a Git working tree.

## Code Commentary

### Logic

- `KnowledgeIndexCache(directory, max_age_seconds=…, max_bytes=…)` first walks up to the nearest existing ancestor of `directory` and runs `git rev-parse --is-inside-work-tree` there; inside a working tree it raises `MemoryTreeError` **before** creating anything, so a refused location leaves no directory behind. Otherwise it creates the directory.
- `for_directory(directory)` recomputes the tree key (`directory_key`) on every call, reuses the file for that key when it opens as that key's index, and otherwise builds from `directory_snapshot`.
- `for_git_tree(repository, revision)` resolves `revision^{tree}`, reuses or builds from `git_tree_snapshot`.
- `_reuse(key)` opens `KnowledgeIndex(path, expected_key=key)`; a mismatch is treated as absent. Reuse refreshes the file's mtime.
- `_build(snapshot)` writes a temporary file in the cache directory and `os.replace`s it into place, so a reader never sees a half-built index and two concurrent builds both end with a whole file. It then evicts and opens the result with its key.
- `evict(keep=…)` removes files unused longer than `max_age`, then the oldest until the directory fits `max_bytes`; the file just built is kept.
- `last_outcome` (`CacheOutcome`: key, reused, build report) records how the last lookup was served.

### Conventions

- The chosen spellings are named constants: `CACHE_DIRECTORY_PARTS` (`runtime/knowledge-index`), `DEFAULT_MAX_AGE_SECONDS` (14 days), `DEFAULT_MAX_BYTES` (1 GiB).

### Invariants And Boundaries

- **An index is never placed where it could be staged or committed**: a cache directory inside any Git working tree is refused.
- An edited working tree is never answered from the previous content: the key is recomputed on every lookup and the opened file is checked against it.
- Deleting the directory, or any file in it, loses nothing: every index is rebuilt from its tree.

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The index's design authority is the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`) and the requirement
packet `MIK-R23@v1` of task `260928_maintained-invariant-knowledge`; both live outside the code and
memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

The cache location, the reuse-or-build rule and eviction.

| Finding | Anchor | Source |
| --- | --- | --- |
| The cache contract: where, what, freshness, eviction, and that deleting it loses nothing. | "Deleting the directory, or any file in it, loses nothing" | mcp/src/agents_remember/memory/knowledge_index/cache.py:1-19 |
| The chosen location and eviction defaults. | `CACHE_DIRECTORY_PARTS`; `DEFAULT_MAX_AGE_SECONDS`; `DEFAULT_MAX_BYTES`; `default_cache_directory` | mcp/src/agents_remember/memory/knowledge_index/cache.py:43-43; mcp/src/agents_remember/memory/knowledge_index/cache.py:46-47; mcp/src/agents_remember/memory/knowledge_index/cache.py:51-54 |
| A location inside a Git working tree is refused before anything is created. | `KnowledgeIndexCache`; "inside a Git working tree" | mcp/src/agents_remember/memory/knowledge_index/cache.py:66-164 |
| Lookups recompute the key and reuse or build. | `for_directory`; `for_git_tree` | mcp/src/agents_remember/memory/knowledge_index/cache.py:96-103; mcp/src/agents_remember/memory/knowledge_index/cache.py:105-114 |
| Eviction by age, then size, keeping the file just built. | `evict` | mcp/src/agents_remember/memory/knowledge_index/cache.py:116-137 |
| Reuse only for the matching key and format; build through a temporary file and a rename. | `_reuse`; `_build`; `CacheOutcome` | mcp/src/agents_remember/memory/knowledge_index/cache.py:57-63; mcp/src/agents_remember/memory/knowledge_index/cache.py:141-152; mcp/src/agents_remember/memory/knowledge_index/cache.py:154-164 |
| The cache cases: reuse, rebuild and deletion, eviction, and the working-tree refusal. | `test_the_cache_reuses_rebuilds_and_loses_nothing_when_deleted`; `test_old_and_excess_index_files_are_evicted`; `test_the_cache_is_never_placed_inside_a_git_working_tree` | mcp/tests/test_knowledge_index.py:333-354; mcp/tests/test_knowledge_index.py:357-372; mcp/tests/test_knowledge_index.py:375-382 |
| An edited working tree is never answered from the previous content. | `test_an_edited_working_tree_is_never_answered_from_the_previous_content` | mcp/tests/test_knowledge_index.py:265-279 |

## Cross-Repo References

No meaningful cross-repo references found: the index reads one memory tree, addressed explicitly by the caller, and nothing else.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T08:49:57+02:00 — 260928-MIK-L04 curator (uncommitted change set on `ar/260928-mik-l04`, code base `ffd043f1354e94a7dcf435e10b4b7224495cbcba` plus the staged delta): No content impact: this card's source is unchanged. Citation ranges into files this change set edited (`test_knowledge_index.py`) were re-pointed by the installed `memory-citations --fix` or, for multi-anchor rows it declined, by the exact base-to-working line map; no claim wording changed. No verification stamp was advanced.
- 2026-09-29T06:45:21+00:00: Generated citation repair: `test_an_edited_working_tree_is_never_answered_from_the_previous_content` repointed to mcp/tests/test_knowledge_index.py:265-279. No content impact: mechanical anchor-range projection bound to citation source snapshot 1a5c7dd5cb87835c8b4e585975574124e545ed7ed5b56804bf2cecaf1ab8ce6b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T08:24:55+02:00 — 260928-MIK-L23 curator (uncommitted change set on `ar/260928-mik-l23`, code base `ee5f14e5405505d126125830e5323f8915c8d047` plus the working-tree delta): removed the Todo about Doc14 §3. The architect has updated Doc14 §3 so that the cache lives under `<coordination-root>/runtime/knowledge-index/`, never inside a Git working tree, which matches this file. No claim about the source changed.
- 2026-09-29T08:01:17+02:00 — 260928-MIK-L23 curator (uncommitted change set on `ar/260928-mik-l23`, code base `ee5f14e5405505d126125830e5323f8915c8d047` plus the working-tree delta): created this card for the new file MIK-R23 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
