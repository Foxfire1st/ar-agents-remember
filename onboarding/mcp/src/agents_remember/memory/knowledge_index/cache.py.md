# mcp/src/agents_remember/memory/knowledge_index/cache.py

## Governing Overview

[memory route overview](../overview.md)

## Purpose

**The index cache keeps one SQLite file per loaded build and memory-tree key, outside Git working trees.** Known builds keep `<loaded-source-digest>--<tree-key>.sqlite` files in one directory — by default `<coordination-root>/runtime/knowledge-index/` — reuses only its own build’s file that matches its key and format, builds anything else, evicts old files, and refuses any location inside a Git working tree.

## Code Commentary

### Logic

- `KnowledgeIndexCache(directory, max_age_seconds=…, max_bytes=…)` first walks up to the nearest existing ancestor of `directory` and runs `git rev-parse --is-inside-work-tree` there; inside a working tree it raises `MemoryTreeError` **before** creating anything, so a refused location leaves no directory behind. Otherwise it creates the directory.
- `for_directory(directory)` recomputes the tree key (`directory_key`) on every call, reuses the file for that key when it opens as that key's index, and otherwise builds from `directory_snapshot`.
- `for_git_tree(repository, revision)` resolves `revision^{tree}`, reuses or builds from `git_tree_snapshot`.
- `_reuse(key)` opens `KnowledgeIndex(path, expected_key=key)`; a mismatch is treated as absent. Reuse refreshes a zero-byte `.sqlite.used` marker while preserving the index bytes and timestamps.
- A cold known-build lookup elects one builder per resolved destination in the process. Other callers wait, then recheck reuse, or receive the builder’s error. A later lookup can try again. The builder rechecks reuse under one lock per cache directory. If the lock cannot exclude or acquisition takes 60 seconds, process-local coordination still applies. The builder atomically installs the finished temporary file, evicts, and opens the result with its key.
- `evict(keep=…)` removes files unused longer than `max_age`, then the oldest until the directory fits `max_bytes`; the file just built is kept. Eviction removes a recognized temporary file only when its builder PID is known to be gone. Registered local files and files with live or indeterminate PIDs stay.
- A cache object captures the immutable loaded source digest at construction. Without that digest, it uses a private UUID namespace and never reuses a file. Private files support dataset reopening and participate in the same eviction.
- `open_cached_index` opens only an existing index for the loaded build and writes no usage bookkeeping.
- `last_outcome` (`CacheOutcome`: key, reused, build report) records how the last lookup was served.

### Conventions

- The chosen spellings are named constants: `CACHE_DIRECTORY_PARTS` (`runtime/knowledge-index`), `DEFAULT_MAX_AGE_SECONDS` (14 days), `DEFAULT_MAX_BYTES` (1 GiB).

### Invariants And Boundaries

- **An index is never placed where it could be staged or committed**: a cache directory inside any Git working tree is refused.
- An edited working tree is never answered from the previous content: the key is recomputed on every lookup and the opened file is checked against it.
- SQLite indexes can be rebuilt from their source trees. Keep `.build.lock` and the cache directory in place while any process can use the cache.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The index's design authority is the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`) and the requirement
packet `MIK-R23@v1` of task `260928_maintained-invariant-knowledge`; both live outside the code and
memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

The cache location, the reuse-or-build rule and eviction.



- Eviction by age, then size, keeping the file just built.
- Reuse selects the loaded build’s matching tree key and index format; builds publish through a temporary file and rename.

### Cross-Repo References

No meaningful cross-repo references found: the index reads one memory tree, addressed explicitly by the caller, and nothing else.

No cross-repo boundary is crossed by this file.

- The cache contract covers location, key selection, freshness, eviction and quiescent regeneration.
- A location inside a Git working tree is refused before anything is created.  Anchor: "inside a Git working tree"

- The chosen location and eviction defaults. [2]

- Directory lookups derive the current key, and Git lookups resolve the requested tree before both enter the shared cache lookup. [4]


- Reuse selects the loaded build's matching tree key and index format; builds publish through a temporary file and rename. [6]


- The cache tests cover reuse, rebuilding after corruption or quiescent directory deletion, eviction, and refusal inside a Git working tree. [7]

- An edited working tree is never answered from the previous content. [8]
