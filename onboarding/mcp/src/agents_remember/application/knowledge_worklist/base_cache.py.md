# mcp/src/agents_remember/application/knowledge_worklist/base_cache.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/knowledge_worklist/base_cache.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T17:20:02+02:00 |
| lastVerifiedCommitHash | `e40c314ca55305f7e4334b4e8e16a10297f6f175`|
| lastVerifiedCommitDate | 2026-09-29T18:13:06+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[application route overview](../overview.md)

## Purpose

**The converted-base cache: one file per converted K_B, so a leaf's runs convert it once (review R1 F6).**
When K_B is unconverted and K_C converted, K_B is compared as its conversion (MIK-R24 rule 7), which takes
about half a minute on the real memory tree. The conversion is a pure function of the memory commit, the
conversion-format version and the paired code commit (MIK-R24 rule 6), so its result is cached under exactly
that key. On the real ICR L47 range the worker measured 39.6 s cold and 6.5 s from the cache, with
byte-identical worklists.

## Code Commentary

### Logic

- **Key.** `base_cache_key(memory_commit, version, code_commit)`; the file is
  `<sha256 of the key>.json.gz`.
- **Location.** `default_base_cache_directory(coordination_root)` is
  `<coordination-root>/runtime/knowledge-worklist-bases`, beside the index cache (`runtime/knowledge-index`).
- `ConvertedBaseCache.open(directory)` walks to the nearest existing ancestor, asks Git whether it is inside
  a working tree (`rev-parse --is-inside-work-tree`), and returns `None` (no cache) when it is, or when the
  directory cannot be created. Nothing is created before that check.
- `load(key)` gunzips and parses the file, and returns the files only when `format` is
  `knowledge-worklist-base/v1` and the stored `key` matches; any read or parse failure is a miss. A hit
  touches the file's mtime.
- `store(key, files)` writes `{format, key, files}` (the converted tree's indexed JSON files as text) with
  `atomic_write_bytes` and a zero gzip mtime; a non-UTF-8 file makes the base uncacheable and a write
  failure is ignored. `_evict` then keeps the `MAX_FILES` (32) newest files.

### Conventions

- The cache is an optimization only: deleting the directory, or any file in it, loses nothing; the base is
  converted again.

### Invariants And Boundaries

- **Architect ruling on review R1 (F6).** The converted K_B is cached by K_B commit, conversion version and
  paired code commit, under the coordination runtime cache; results are unchanged.
- **Never inside a Git working tree**, so a cached base can never be staged or committed; the reviewer
  confirmed the refusal on a scratch memory clone and that the live coordination root is not a working
  tree.
- **Unconverted leaves never reach it.** The cache is only opened after the applicability probe and the
  pairing, so no production leaf creates the directory before MIK-R37.
- The key does not include the converter's build (review R2 N1): a converter fix must bump the conversion
  version, as MIK-R24 rule 6 requires.

### Todos

- Review R2 N2: `_evict` sorts by `stat()` outside any guard, so a file deleted concurrently makes `store`
  raise; `recompute_leaf_worklist` then reports an `incomplete` "worklist run" for that run. Suppressing
  `OSError` around the sort would close it.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R08@v2` of task
`260928_maintained-invariant-knowledge` (with the architect rulings in the task's leaf document
`08_change-to-knowledge-worklist.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The key, location, contents and eviction rules. | "A directory inside any Git working tree is refused" | mcp/src/agents_remember/application/knowledge_worklist/base_cache.py:1-18 |
| The cache location and format constants. | `CACHE_DIRECTORY_PARTS`; `MAX_FILES` | mcp/src/agents_remember/application/knowledge_worklist/base_cache.py:40-40; mcp/src/agents_remember/application/knowledge_worklist/base_cache.py:42-42 |
| The default directory and the key. | `default_base_cache_directory`; `base_cache_key` | mcp/src/agents_remember/application/knowledge_worklist/base_cache.py:46-49; mcp/src/agents_remember/application/knowledge_worklist/base_cache.py:52-53 |
| A location inside a working tree is refused before anything is created. | `open` | mcp/src/agents_remember/application/knowledge_worklist/base_cache.py:62-76 |
| A hit only for this format and key. | `load` | mcp/src/agents_remember/application/knowledge_worklist/base_cache.py:81-100 |
| Atomic writes and eviction. | `store`; `_evict` | mcp/src/agents_remember/application/knowledge_worklist/base_cache.py:102-120 |
| The caller that reads or fills the cache. | `_converted_base_side`; `ConvertedBaseCache` | mcp/src/agents_remember/application/knowledge_worklist/leaf.py:280-318 |
| Cached by commit, version and code commit; a refused location converts and creates nothing. | `test_converted_bases_are_cached_by_commit_version_and_code_commit` | mcp/tests/test_knowledge_worklist_leaf.py:720-754 |

## Cross-Repo References

No meaningful cross-repo references found: the cache lives in the coordination root's runtime directory.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T17:20:02+02:00 — 260928-MIK-L08 curator (uncommitted change set on `ar/260928-mik-l08`, code base `e49ba07865b3848cd36759cea6b37bba7d0d51c3` plus the working-tree delta and untracked files): created this card for the new file MIK-R08 adds.  The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
