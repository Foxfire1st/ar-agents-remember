# dashboard/src/panels/review/ReviewReadCache.ts

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

What the intent reviewer has already read **for the comparison on screen**, so returning to a subject or reopening a file costs no request. The module holds two bounded stores (whole subject reviews and changed-file content) and the one generation rule that empties both. It is a working surface owned by one mounted review surface, never a record: nothing here is persisted, published or shared between surfaces.

## Code Commentary

### Two stores, each with the key its reader already uses

- `reviews` holds a subject's whole review under the read cycle's own target key.
- `sources` holds a changed file's content answer under `sourceContentKey(repo, master, leaf, path, beforeCodeTreeId, afterCodeTreeId)`: exactly the fields the content request names. One content answer carries both sides, so the side needs no key of its own.
- Paged questions are not kept: a roster walk is a continuation of the retained page and stays owned by the read cycle.

### Only answers are kept

`keepSource` keeps a result only when its state is `content` and it carries an expansion. The read cycle calls `keepReview` only for an admitted whole-subject answer whose read carried no refresh identity; a paged answer and a refresh's answer are observed and not kept. A refusal or a failure is asked again, because it may describe a transient state rather than the immutable comparison.

`keepUnshown` keeps an answer that was read but never shown, because its question was replaced while it was in flight. The read cycle hands it only a successful whole answer for the task context ("All source changes") whose read carried no refresh identity. An answer whose generation differs from the known one is dropped; with no known generation the answer establishes one. Once kept it is an answer like any other, so returning to "All source changes" costs no second request.

### The generation empties everything

Every kept review is read under a comparison generation: the pair of code trees and, when knowledge was compared, the pair of snapshots (`comparisonGenerationOf`). `observe(payload)` is called for every admitted answer, kept or not. When its generation is not the same as the known one (`sameGeneration`), both stores are cleared. A task-context answer compares no knowledge, so it says nothing about the snapshot pair and cannot move it: `sameGeneration` treats a missing snapshot pair as compatible, and `observe` carries the known pair forward. `forgetReview(key)` serves the reader's refresh: the read cycle forgets the question it re-asks, so a refresh always reaches the server.

`comparisonGenerationOf`, `sameGeneration` and the type `ComparisonGeneration` are exported. The walked family tree (`walkedTree.ts`) uses them to decide whether an answer belongs to the comparison its rows were read under, so the tree applies the same test as the cache.

### Bounded, least recently used

`BoundedStore` is a `Map` in insertion order: `get` re-inserts the entry to refresh its recency, and `set` evicts the oldest entries until the size is within the limit. `REVIEW_CACHE_LIMIT` is 24 and `SOURCE_CACHE_LIMIT` is 32. The cache belongs to one mounted surface (`ReviewSurface` creates it once) and is reclaimed with it.

### Conventions

`ReviewReadCache` is a plain class, constructed by the surface and handed to the read cycle. `ReviewReadCacheContext` (default `null`) is how the source content renderer finds it; content rendered outside a review surface has no provider and reads every time. `sizes` reports the two store sizes. The file is 164 lines.

### Boundaries

- An answer from another generation never survives beside the new one.
- No refusal, failure, paged answer or refresh answer is kept.
- Returning to a kept subject does not re-validate a live candidate that moved; the reader's refresh asks again.
- The cache decides nothing about what is read or displayed: the read cycle decides when to ask and what to keep, and the content renderer decides how content renders.
- `review()` and `source()` refresh recency when they are read, also when a render path reads them.

## Evidence

- The module's own statement of what is kept, under which key, when it is dropped, and its bounds. [14]
- The two bounds. [15]
- The least-recently-used store: recency refreshed on read, oldest evicted on write. [16]
- The generation of a payload, exported: code trees, and snapshots only when knowledge was compared. [17]
- Two generations differ on code trees, or on snapshots when both compared knowledge. [18]
- The content key is exactly the request's fields. [19]
- The cache: observe, keep, keep unshown, forget, and sources kept only as content with an expansion. [20]
- The context the content renderer reads it through; `null` outside a surface. [21]
- The walked tree applies the same comparison test to its rows. [22]
- The read cycle serves a kept answer, keeps a whole answer, keeps a superseded task-context answer unshown, or only observes. [23]
- A refresh forgets its question before it asks again. [24]
- The surface owns one cache and provides it. [25]
- The content renderer reads through it under the request key. [26]
- The bounds, refusal, generation and unshown-answer cases. [27]
