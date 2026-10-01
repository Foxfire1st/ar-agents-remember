# mcp/src/agents_remember/application/knowledge_worklist/base_cache.py

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
  `knowledge-worklist-base/v2` (since MIK-R30; it was `v1`) and the stored `key` matches; any read or parse failure is a miss. A hit
  touches the file's mtime.
- `store(key, files)` writes `{format, key, files}` (the converted tree's indexed JSON files and, since
  MIK-R30, its onboarding Markdown, as text) with
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

## 260928-MIK-L30 One Cache For Both Consumers (MIK-R30, Ruling 18:49:50 (4))

The onboarding gate also compares K_B as its conversion, and it needs the onboarding Markdown, which the v1
cache did not hold. The architect ruled that L08's cache is extended rather than having the gate reconvert
K_B on every run (about 30 s on the real tree):

- **`converted_base_files(memory_repository, memory_commit, *, code, version, cache_directory)`** is now the
  one read-or-convert-and-store path, used by the worklist (`leaf._converted_base_side`) and the gate
  (`onboarding_trace.onboarding_trace_sides`). It moved here from `leaf.py` unchanged in substance: it picks
  K_B's own paired code commit when the code store holds it, B otherwise, and keys the cache on (K_B commit,
  version, that code commit).
- **`is_cached_path(path)`** selects what is stored: an indexed JSON file, or Markdown under `onboarding/`
  outside any dot-directory.
- **`FORMAT` is `knowledge-worklist-base/v2`.** A v1 file holds no Markdown and would make every card look
  new to the gate, so a v1 file is ignored and rewritten, as the format rule already did for any other
  format (ruling 19:23:45 N3; pinned by a test).
- Location, key, eviction and the refusal inside a Git working tree are unchanged. The worker measured the
  gate's sides at 29.4 s cold and 0.7 to 0.8 s from the cache on the real ICR L47 scratch copy.

- The docstring's contents rule: JSON for the worklist, Markdown for the gate, v1 never read. [1]
- The v2 format constant. [2]
- What the cache holds. [3]
- The one read-or-convert path both consumers use. [4]
- The gate reads its converted K_B through it. [5]
- The cache holds the Markdown, and a v1 file is ignored and rewritten. [6]

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R08@v2` of task
`260928_maintained-invariant-knowledge` (with the architect rulings in the task's leaf document
`08_change-to-knowledge-worklist.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The key, location, contents and eviction rules. [7]
- The cache location and format constants. [8]
- The default directory and the key. [9]
- A location inside a working tree is refused before anything is created. [10]
- A hit only for this format and key. [11]
- Atomic writes and eviction. [12]
- The worklist's converted K_B, now read through the shared read-or-convert path. [13]
- Cached by commit, version and code commit; a refused location converts and creates nothing. [14]

### Cross-Repo References

No meaningful cross-repo references found: the cache lives in the coordination root's runtime directory.

No cross-repo boundary is crossed by this file.
