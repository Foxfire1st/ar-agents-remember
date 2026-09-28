# mcp/src/agents_remember/memory/knowledge/read_anchor_memo.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/read_anchor_memo.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-28T23:11:42+02:00 |
| lastVerifiedCommitHash |  `69883386d36d7cdb7faeed5bdf275ddd66d87aea`|
| lastVerifiedCommitDate |  2026-09-28T23:28:51+02:00|
| governingOverview | `mcp/src/agents_remember/memory/overview.md` |

## Governing Overview

[memory route overview](../overview.md)

## Purpose

**A bounded, thread-safe, process-lifetime memo for facts that are functions of complete Git object
ids**, and the three tables anchor observation uses. It exists so a first visit to a review subject does
not re-ask Git and re-parse the same handful of trees and blobs for every owner that observes the same
anchors (260921-ICR-L56, ICR-R24@v3). It owns the storage, the bound and the one key-admission test;
**what may be put in it, and when, is decided by its one consumer,
[`read_anchors.py`](read_anchors.py.md)**.

## Code Commentary

### Logic

- **`is_complete_object_id(value)`** is the single admission test for a memo key: a full 40- or 64-digit
  lowercase hex id (`GIT_OBJECT_PATTERN` from `models/knowledge/base.py`, matched with `fullmatch`). A
  ref, `HEAD`, a branch name or an abbreviation names different objects over time — an abbreviation can
  even become ambiguous when an object is added — so an answer to a question asked with one is never
  remembered.
- **`BoundedMemo[K, V]`** is a least-recently-used table whose entries' total weight never exceeds
  `capacity`. `weigh` prices one value (the default prices every entry at one, making capacity an entry
  count). `put` refuses a value heavier than the whole capacity rather than evicting everything for it,
  replaces an existing key's weight, then evicts from the least-recently-used end until within the bound.
  `get` returns a **one-tuple** `(value,)` or `None`, which is what lets a remembered `None` — "the tree
  holds no entry at this path" — be told apart from a miss; a hit refreshes recency.
- **The lock guards the table only.** No caller holds it while running Git or a parser, so two threads
  that miss the same key both compute the same answer and the second `put` overwrites an equal value.
- **The three tables**, every key beginning with the repository root Git runs against (so one
  repository's answer is never served for another's):

| Table | Key | Value | Bound |
| --- | --- | --- | --- |
| `TREE_ENTRIES` | (root, tree id, confined path) | the `ls-tree` entry `(mode, kind, object id)` or `None` | 16,384 entries, unit-priced |
| `BLOB_LINES` | (root, blob id) | the blob's lines as a tuple | 32 Mi weight units: characters plus 64 per line (`_lines_weight`) |
| `BLOB_DEFINITIONS` | (root, blob id, grammar) | read-only mapping name → distinct `(start, end)` extents (`Definitions`) | 65,536 units: one per name and per extent (`_definitions_weight`) |

### Conventions

- The module docstring separates **content facts** (keyed by id, never stale, never invalidated) from
  **availability** (whether a repository still holds the object), which is never remembered here; the
  consumer probes the tree on every resolver and consults these tables only behind a probe that
  succeeded.
- Values are immutable (`tuple`, `MappingProxyType`) because one remembered answer is shared by every
  later caller.
- `clear()`, `weight` and `__len__` exist for the tests, which empty every table before and after each
  case.

### Invariants And Boundaries

- **Answers only.** A caller puts a value after an operation succeeded; a failure is never passed in, so
  an object unreadable once is asked about again and a later success is observed.
- **Only complete ids are keys**, and no key is ever invalidated because every answer is a function of
  immutable object ids.
- **The bounds are approximate weights, not a worst-case byte budget** (review L56-R1-F3). Blob lines are
  close to resident bytes for ASCII source (about 32 MiB when full) but under-price wide text: non-Latin,
  astral or surrogate-escaped characters can take two to four times their weight, so a full table holds
  on the order of 64–128 MiB. Tree entries are unit-priced whatever the path length, so a table of very
  long paths can add tens of MiB more. Typical source keeps the three tables within a few tens of MiB;
  the bounds sit far above one comparison's working set, so a review does not evict what it reuses.
- **There are three tables, not four.** An earlier attempt also remembered positive tree-existence
  probes (`TREE_EXISTS`); review blocked it (L56-R1-F1) because holding a tree is a fact about the
  repository, and it was removed. **Do not reintroduce an availability table.**
- **Boundary.** No Git, no parser, no I/O and no knowledge of anchors: this module stores and bounds.
  It is not a store, index or cache daemon; it lives and dies with the process.

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| **Content facts are functions of the id; availability is never remembered here; only complete ids are admitted; answers only.** | "What is *not* a function of the id" | mcp/src/agents_remember/memory/knowledge/read_anchor_memo.py:1-27 |
| The one admission test for a key. | `is_complete_object_id` | mcp/src/agents_remember/memory/knowledge/read_anchor_memo.py:51-54 |
| **The weight-bounded LRU table: the one-tuple hit, the refused oversized value, eviction past the bound, and a lock never held across Git or parsing.** | `BoundedMemo` | mcp/src/agents_remember/memory/knowledge/read_anchor_memo.py:61-122 |
| The definitions value shape and the two weigh functions. | `Definitions`; `_lines_weight`; `_definitions_weight` | mcp/src/agents_remember/memory/knowledge/read_anchor_memo.py:126-138 |
| **The three tables, their keys and capacities, and the approximate-weight statement above them.** | `TREE_ENTRIES`; `BLOB_LINES`; `BLOB_DEFINITIONS` | mcp/src/agents_remember/memory/knowledge/read_anchor_memo.py:141-160 |
| The complete-id pattern is the storage models' own object-id pattern (imported from `models/knowledge/base.py`), compiled once for the admission test. | `_COMPLETE_OBJECT_ID` | mcp/src/agents_remember/memory/knowledge/read_anchor_memo.py:48-48 |
| The consumer that decides what is put, keyed by root plus ids, and only after Git or the parser answered. | `_recorded_lines`; `_blob_definitions`; `_tree_entry` | mcp/src/agents_remember/memory/knowledge/read_anchors.py:387-431; mcp/src/agents_remember/memory/knowledge/read_anchors.py:491-531 |
| **The cases that pin the bound and concurrency.** | "test_the_memo_evicts_the_least_recently_used_past_its_weight_bound"; "test_concurrent_readers_share_answers_and_the_bound_holds" | mcp/tests/test_read_anchor_memo.py:301-369 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-28T23:11:42+02:00 — 260921-ICR-L56 curator (uncommitted candidate tree `0dabc51f68b613546ec971657726b97828afb69a` over code base `ae2fd5c864aa2609ae45b5c7dbbaa693569aefc6`; review R2 PASS on the unchanged A2 diff): created this one-to-one card for the new anchor-observation memo module. It records the complete-id admission test, the weight-bounded LRU table with its one-tuple hit and refusal of oversized values, the lock that is never held across Git or parsing, the three tables with their keys and bounds, the approximate-weight semantics of those bounds (review L56-R1-F3), and that there are three tables because the tree-availability table was removed (review L56-R1-F1). Verification metadata remains empty until closeout stamps the code commit.
