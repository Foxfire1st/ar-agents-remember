# mcp/src/agents_remember/application/knowledge_worklist/base_cache.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/knowledge_worklist/base_cache.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T04:44:12+02:00 |
| lastVerifiedCommitHash | `31d761a241055d67b85ef3908033856b78a86a57`|
| lastVerifiedCommitDate | 2026-09-30T05:10:40+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| The docstring's contents rule: JSON for the worklist, Markdown for the gate, v1 never read. | "held no Markdown, so its files are never read as a gate's base" | mcp/src/agents_remember/application/knowledge_worklist/base_cache.py:11-15 |
| The v2 format constant. | `FORMAT` | mcp/src/agents_remember/application/knowledge_worklist/base_cache.py:48-48 |
| What the cache holds. | `is_cached_path` | mcp/src/agents_remember/application/knowledge_worklist/base_cache.py:130-137 |
| The one read-or-convert path both consumers use. | `converted_base_files` | mcp/src/agents_remember/application/knowledge_worklist/base_cache.py:140-172 |
| The gate reads its converted K_B through it. | `onboarding_trace_sides`; `converted_base_files` | mcp/src/agents_remember/application/knowledge_worklist/onboarding_trace.py:109-157 |
| The cache holds the Markdown, and a v1 file is ignored and rewritten. | `test_the_conversion_itself_counts_for_nothing_at_the_converting_leaf` | mcp/tests/test_onboarding_trace_gate.py:552-604 |

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
| The cache location and format constants. | `CACHE_DIRECTORY_PARTS`; `MAX_FILES` | mcp/src/agents_remember/application/knowledge_worklist/base_cache.py:47-47; mcp/src/agents_remember/application/knowledge_worklist/base_cache.py:49-49 |
| The default directory and the key. | `default_base_cache_directory`; `base_cache_key` | mcp/src/agents_remember/application/knowledge_worklist/base_cache.py:53-56; mcp/src/agents_remember/application/knowledge_worklist/base_cache.py:59-60 |
| A location inside a working tree is refused before anything is created. | `open` | mcp/src/agents_remember/application/knowledge_worklist/base_cache.py:69-83 |
| A hit only for this format and key. | `load` | mcp/src/agents_remember/application/knowledge_worklist/base_cache.py:88-107 |
| Atomic writes and eviction. | `store`; `_evict` | mcp/src/agents_remember/application/knowledge_worklist/base_cache.py:109-121; mcp/src/agents_remember/application/knowledge_worklist/base_cache.py:123-127 |
| The worklist's converted K_B, now read through the shared read-or-convert path. | `_converted_base_side`; `converted_base_files` | mcp/src/agents_remember/application/knowledge_worklist/leaf.py:341-369 |
| Cached by commit, version and code commit; a refused location converts and creates nothing. | `test_converted_bases_are_cached_by_commit_version_and_code_commit` | mcp/tests/test_knowledge_worklist_leaf.py:729-763 |

## Cross-Repo References

No meaningful cross-repo references found: the cache lives in the coordination root's runtime directory.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History
- 2026-09-30T04:44:12+02:00 — 260928-MIK-L10 curator (uncommitted change set on `ar/260928-mik-l10`, code base `8a2d4b478971bf40cca0f24d5e5d24a0844bd563` plus the staged delta): No content impact: citation-only repair. This card's source is unchanged; the `_converted_base_side` row cited `leaf.py:302-326`, whose first line MIK-R10 changed, so no line shift could map it; it was re-measured to the declaration's current extent `341-369` were re-pointed by the installed fixer or, where it declined, by the exact line shift over rows byte-identical to memory HEAD. No claim was reworded, so the fixer's bullets are kept. No verification stamp was advanced.
- 2026-09-29T23:27:43+02:00 — 260928-MIK-L11 curator (uncommitted change set on `ar/260928-mik-l11`, code base `2c6f170ef07bf6767d582f76c9f9dd06bbdd06a4` plus the staged delta): No content impact: citation-only repair. Ranges into `mcp/src/agents_remember/application/knowledge_worklist/leaf.py`, moved by MIK-R11's changes, were re-pointed by the installed `memory-citations --fix` or, for rows it declined, by the exact base-to-staged line map. Claim wording unchanged. No verification stamp was advanced.
- 2026-09-29T18:59:28+00:00: Generated citation repair: `store`; `_evict` repointed to mcp/src/agents_remember/application/knowledge_worklist/base_cache.py:109-121; mcp/src/agents_remember/application/knowledge_worklist/base_cache.py:123-127. No content impact: mechanical anchor-range projection bound to citation source snapshot f243d6cd7f6b1214330608a0b5e372fb521b8035680e9d41a0f33ceb9d8057ab; claim bytes unchanged; generated by ccr-r10@v1.

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T20:47:37+02:00 — 260928-MIK-L30 curator (uncommitted change set on `ar/260928-mik-l30`, code base `719acba61e491d0b7f1ee82dbeea5314ecec5083` plus the staged delta, including the untracked-then-staged new files): **body updated for MIK-R30.** Added the section "260928-MIK-L30 One Cache For Both Consumers": `converted_base_files` (moved here from `leaf.py`), `is_cached_path`, and the v2 format that also holds onboarding Markdown, with architect rulings 2026-09-29T18:49:50 (4) and 19:23:45 (N3). The `load` and `store` Logic bullets now name v2 and the Markdown. **The caller row was reworded and re-cited**: `_converted_base_side` no longer opens `ConvertedBaseCache` itself but calls `converted_base_files`. Rows below the changed docstring were re-pointed by the installed fixer. No verification stamp was advanced.
- 2026-09-29T17:20:02+02:00 — 260928-MIK-L08 curator (uncommitted change set on `ar/260928-mik-l08`, code base `e49ba07865b3848cd36759cea6b37bba7d0d51c3` plus the working-tree delta and untracked files): created this card for the new file MIK-R08 adds.  The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
