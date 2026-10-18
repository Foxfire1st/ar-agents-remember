# dashboard/src/panels/review/ReviewReadCache.ts

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

What the intent reviewer has already read **for the comparison on screen**, so returning to a subject or reopening a file costs no request. The module holds two bounded stores (whole subject reviews and changed-file content) generation changes that empty both, and a separate memory-input epoch invalidation of whole reviews. It is a working surface owned by one mounted review surface, never a record: nothing here is persisted, published or shared between surfaces.

## Unshown whole-task reuse

`keepUnshown` reuses an admitted whole-task answer whose request was superseded by initial subject selection. It never writes panes or advances an already-known incompatible generation. With no known generation the answer establishes one; a later admitted different generation clears it with both bounded stores. The read cycle admits only unpaged, non-refresh successful whole-task answers to this path. Superseded subjects/pages/refreshes/refusals/failures stay excluded; returning to All source changes can reuse the already-paid request.

## Code Commentary

### Two stores, each with the key its reader already uses

- `reviews` holds a subject's whole review under the read cycle's own target key.
- `sources` holds a changed file's content answer under `sourceContentKey(repo, master, leaf, path, beforeCodeTreeId, afterCodeTreeId)`: exactly the fields the content request names. One content answer carries both sides, so the side needs no key of its own.
- Paged questions are not kept: a roster walk is a continuation of the retained page and stays owned by the read cycle.

### Only answers are kept

`keepSource` keeps a result only when its state is `content` and it carries an expansion. The read cycle calls `keepReview` only for an admitted whole-subject answer whose read carried no refresh identity; a paged answer and a refresh's answer are observed and not kept. A refusal or a failure is asked again, because it may describe a transient state rather than the immutable comparison.

`keepUnshown` keeps an answer that was read but never shown, because its question was replaced while it was in flight. The read cycle hands it only a successful whole answer for the task context ("All source changes") whose read carried no refresh identity. An answer whose generation differs from the known one is dropped; with no known generation the answer establishes one. Once kept it is an answer like any other, so returning to "All source changes" costs no second request.

### Generation changes and live memory invalidation

Every kept review is read under a comparison generation: the pair of code trees and, when knowledge was compared, the pair of snapshots (`comparisonGenerationOf`). `observe(payload)` is called for every admitted answer, kept or not. When its generation is not the same as the known one (`sameGeneration`), both stores are cleared. A task-context answer compares no knowledge, so it says nothing about the snapshot pair and cannot move it: `sameGeneration` treats a missing snapshot pair as compatible, and `observe` carries the known pair forward. `forgetReview(key)` serves the reader's refresh: the read cycle forgets the question it re-asks, so a refresh always reaches the server.

`inputEpoch` starts at zero. `invalidateReviews()` increments it and clears only whole-review answers, leaving the source-content store and the known comparison generation intact. The mounted read cycle's memory-change callback invalidates reviews before refreshing; `startRead` captures the epoch and drops a callback whose epoch is no longer current, including the superseded-task reuse path. This is a real live-input invalidation boundary, not merely a manual refresh. It does not claim that old labelled content is immediately erased or that source bytes changed.

`comparisonGenerationOf`, `sameGeneration` and the type `ComparisonGeneration` are exported. The walked family tree (`walkedTree.ts`) uses them to decide whether an answer belongs to the comparison its rows were read under, so the tree applies the same test as the cache.

### Bounded, least recently used

`BoundedStore` is a `Map` in insertion order: `get` re-inserts the entry to refresh its recency, and `set` evicts the oldest entries until the size is within the limit. `REVIEW_CACHE_LIMIT` is 24 and `SOURCE_CACHE_LIMIT` is 32. The cache belongs to one mounted surface (`ReviewSurface` creates it once) and is reclaimed with it.

### Conventions

`ReviewReadCache` is a plain class, constructed by the surface and handed to the read cycle. `ReviewReadCacheContext` (default `null`) is how the source content renderer finds it; content rendered outside a review surface has no provider and reads every time. `sizes` reports the two store sizes. The declaration span is source-bound rather than a fixed file-length promise.

### Boundaries

- An answer from another generation never survives beside the new one.
- No refusal, failure, paged answer or refresh answer is kept.
- A cache hit alone performs no new read, but an observed memory change clears whole-review answers and invalidates earlier callbacks before refresh; source content remains keyed by its explicit tree pair.
- The cache decides nothing about what is read or displayed: the read cycle decides when to ask and what to keep, and the content renderer decides how content renders.
- `review()` and `source()` refresh recency when they are read, also when a render path reads them.

### Logic

**Two stores, each with the key its reader already uses.** `reviews` holds a subject's whole review under
the read cycle's own target key (task context, live/recorded history selector, subject, `whole` position), and `sources` holds a
changed file's content answer under `sourceContentKey(repo, master, leaf, path, beforeCodeTreeId,
afterCodeTreeId)` — exactly the fields the content request names. One content answer carries both sides,
so the side needs no key of its own. Paged questions are never kept: a roster walk is a continuation of
the retained page and stays owned by the read cycle.

**Only answers are kept.** `keepSource` keeps a result only when `state === 'content'` and it carries an
expansion; the read cycle calls `keepReview` only for an admitted whole-subject answer that carried no
refresh identity. A refusal or failure is asked again, because it may describe a transient state rather
than the immutable comparison.

**The generation empties everything.** Every kept review is read under a comparison generation: the code
tree pair (`before_code_tree_id:after_code_tree_id`) and, when knowledge was compared, the snapshot pair
(`comparisonGenerationOf`). `observe(payload)` is called with **every** admitted answer, kept or not; when
its generation is not `sameGeneration` as the known one, both stores are cleared before anything else
happens. A task-context answer compares no knowledge, so it says nothing about the snapshot pair and
cannot move it (`sameGeneration` treats a missing snapshot pair as compatible, and `observe` carries the
known pair forward). A paged or refreshed answer is observed without being kept, and still invalidates.
`forgetReview(key)` is the reader's refresh: the read cycle forgets the question it re-asks, so a refresh
always reaches the server.

**Bounded, least recently used.** `BoundedStore` is a `Map` in insertion order; `get` re-inserts the entry
to refresh its recency, and `set` evicts the oldest entries until the size is within the limit.
`REVIEW_CACHE_LIMIT = 24` and `SOURCE_CACHE_LIMIT = 32`. The cache belongs to one mounted surface
(`ReviewSurface` creates it with `useState`) and is reclaimed with it.

### Conventions

A plain class with a context export: `ReviewReadCache` is constructed by the surface and handed to the read
cycle directly; `ReviewReadCacheContext` (default `null`) is how `SourceContent` finds it. Content rendered
outside a review surface has no provider and reads every time, as before. `sizes` exists for the bounds
cases. The module header carries the key, drop and bound rules in capitals, matching the read cycle's
header style.

### Invariants And Boundaries

- **An answer from another generation never survives.** Any admitted answer whose code trees differ, or
  whose compared snapshots differ from compared snapshots, empties both stores first.
- **Only immutable-comparison answers are kept.** No refusal, failure, paged answer or refresh answer is
  kept.
- **Bounded and reclaimed.** Both stores are capped and evict least-recently-used entries; the cache lives
  and dies with one mounted surface (the repository's bounded-resources doctrine). Re-entering the
  reviewer starts empty (worker observation O3).
- **Cache lookup is not a live check; invalidation is live.** Kept views stay labelled with their
  own trees. The memory watcher explicitly advances the input epoch and clears whole reviews before
  refresh, so older callbacks cannot refill them; the separate source cache is not cleared by this operation.
- **Boundary.** It decides nothing about what is read or displayed: the read cycle decides when to ask
  and what to keep, and `SourceContent` decides how content renders.

### Todos

Review observation O-R1-5: `review()` and `source()` are called from render paths (`readOnScreen`,
`useSourceContentRead`) and refresh LRU recency there — an idempotent reorder, harmless, but a side effect
during render. Recorded as an observation, not a defect.

## Evidence

- The module's own statement of what is kept, under which key, when it is dropped, and its bounds. [14]

- The two bounds. [15]

- The least-recently-used store: recency refreshed on read, oldest evicted on write. [16]

- The generation of a payload, exported: code trees, and snapshots only when knowledge was compared. [17]

- Two generations differ on code trees, or on snapshots when both compared knowledge. [18]

- The content key is exactly the request's fields. [19]

- The cache separates generation changes clearing both stores from input-epoch invalidation clearing whole reviews only. [20]

- The context the content renderer reads it through; `null` outside a surface. [21]

- The walked tree applies the same comparison test to its rows. [22]

- The read cycle serves a kept answer, keeps a whole answer, keeps a superseded task-context answer unshown, or only observes. [23]

- A refresh forgets its question before it asks again. [24]

- The surface owns one cache and provides it. [25]

- The content renderer reads through it under the request key. [26]

- The bounds, refusal, generation and unshown-answer cases. [27]

- Memory changes advance the review epoch before refresh; older read callbacks cannot repopulate whole-review answers. [28]

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

The cache's rules are stated in its own header and enforced by the class; the read cycle and the content
renderer are its only callers.

| Restored finding | Primary anchor | Tip range |
| --- | --- | --- |
| **The module's own statement of what is kept, under which key, when it is dropped, and its bounds.** | `ReviewReadCache` | dashboard/src/panels/review/ReviewReadCache.ts |
| The two bounds. | `REVIEW_CACHE_LIMIT` | dashboard/src/panels/review/ReviewReadCache.ts |
| The least-recently-used store: recency refreshed on read, oldest evicted on write. | `BoundedStore` | dashboard/src/panels/review/ReviewReadCache.ts |
| The generation of a payload: code trees, and snapshots only when knowledge was compared. | `comparisonGenerationOf` | dashboard/src/panels/review/ReviewReadCache.ts |
| Two generations differ on code trees, or on snapshots when both compared knowledge. | `sameGeneration` | dashboard/src/panels/review/ReviewReadCache.ts |
| The content key is exactly the request's fields. | `sourceContentKey` | dashboard/src/panels/review/ReviewReadCache.ts |
| The bounded mounted-surface cache invalidates by displayed generation; keepUnshown rejects an incompatible answer without advancing that generation, and sources are kept only as content with an expansion. | `ReviewReadCache` | dashboard/src/panels/review/ReviewReadCache.ts |
| The context the content renderer reads it through; `null` outside a surface. | `ReviewReadCacheContext` | dashboard/src/panels/review/ReviewReadCache.ts |
| The read cycle serves, keeps or only observes answers, and a refresh forgets its question. | `startRead` | dashboard/src/panels/review/ReviewReadCycle.ts |
| The surface owns one cache and provides it. | `useSurface` | dashboard/src/panels/review/ReviewSurface.tsx |
| The content renderer reads through it under the request key. | `useSourceContentRead` | dashboard/src/panels/review/SourceContent.tsx |
| The bounds, refusal, generation and key cases. | `keeps at most the bound of reviews and evicts the least recently used (%i inserted)` | dashboard/src/panels/review/ReviewReadCache.test.ts |

### Cross-Repo References

No cross-repository behavior is implemented in this file. It keeps answers for one repository namespace's
task context and holds no identity that ranges beyond it.

No meaningful cross-repo references found.
