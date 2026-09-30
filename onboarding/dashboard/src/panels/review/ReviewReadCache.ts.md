# dashboard/src/panels/review/ReviewReadCache.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/ReviewReadCache.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T14:18:54+02:00 |
| lastVerifiedCommitHash |  `59daf5055eb1ceffba89170be64ac85cabf860f4`|
| lastVerifiedCommitDate |  2026-09-30T15:02:26+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

What the Intent Reviewer has already read **for the comparison on screen**, so returning to a subject or
reopening a file costs no request (`260921-ICR-L48`, `ICR-R24@v3`). It holds two bounded stores — whole
subject reviews and changed-file content — and the one generation rule that empties both. It is a working
surface owned by one mounted review surface, never a record: nothing here is persisted, published or
shared between surfaces.

## Code Commentary

### Logic

**Two stores, each with the key its reader already uses.** `reviews` holds a subject's whole review under
the read cycle's own target key (task context, record, subject, `whole` position), and `sources` holds a
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
- **Not a live check.** Returning to a kept subject does not re-validate a live candidate that moved;
  each kept view stays labelled with its own trees, and the reader's refresh re-asks (review observation
  O-R1-1, by design).
- **Boundary.** It decides nothing about what is read or displayed: the read cycle decides when to ask
  and what to keep, and `SourceContent` decides how content renders.

### Todos

Review observation O-R1-5: `review()` and `source()` are called from render paths (`readOnScreen`,
`useSourceContentRead`) and refresh LRU recency there — an idempotent reorder, harmless, but a side effect
during render. Recorded as an observation, not a defect.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

The cache's rules are stated in its own header and enforced by the class; the read cycle and the content
renderer are its only callers.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The module's own statement of what is kept, under which key, when it is dropped, and its bounds.** | "WHAT IS KEPT, AND UNDER WHICH KEY"; "WHEN IT IS DROPPED"; "BOUNDS" | dashboard/src/panels/review/ReviewReadCache.ts:1-23 |
| The two bounds. | `REVIEW_CACHE_LIMIT`; `SOURCE_CACHE_LIMIT` | dashboard/src/panels/review/ReviewReadCache.ts:29-30 |
| The least-recently-used store: recency refreshed on read, oldest evicted on write. | `BoundedStore` | dashboard/src/panels/review/ReviewReadCache.ts:32-67 |
| The generation of a payload: code trees, and snapshots only when knowledge was compared. | `comparisonGenerationOf`; `knowledge_compared` | dashboard/src/panels/review/ReviewReadCache.ts:74-83 |
| Two generations differ on code trees, or on snapshots when both compared knowledge. | `sameGeneration` | dashboard/src/panels/review/ReviewReadCache.ts:88-93 |
| The content key is exactly the request's fields. | `sourceContentKey` | dashboard/src/panels/review/ReviewReadCache.ts:95-104 |
| The cache: observe empties both stores on another generation; only content answers with an expansion are kept. | `ReviewReadCache`; `observe`; `keepReview`; `forgetReview`; `keepSource` | dashboard/src/panels/review/ReviewReadCache.ts:106-150 |
| The context the content renderer reads it through; `null` outside a surface. | `ReviewReadCacheContext` | dashboard/src/panels/review/ReviewReadCache.ts:154-154 |
| The read cycle serves, keeps or only observes answers, and a refresh forgets its question. | `startRead`; `keepReview`; `observe`; `forgetReview` | dashboard/src/panels/review/ReviewReadCycle.ts:163-217; dashboard/src/panels/review/ReviewReadCycle.ts:423-439 |
| The surface owns one cache and provides it. | "new ReviewReadCache()"; "ReviewReadCacheContext.Provider" | dashboard/src/panels/review/ReviewSurface.tsx:475-476; dashboard/src/panels/review/ReviewSurface.tsx:553-553 |
| The content renderer reads through it under the request key. | `useSourceContentRead`; `sourceContentKey` | dashboard/src/panels/review/SourceContent.tsx:180-220 |
| The bounds, refusal, generation and key cases. | "keeps at most the bound of reviews and evicts the least recently used (%i inserted)"; "empties both stores when an answer belongs to another comparison generation" | dashboard/src/panels/review/ReviewReadCache.test.ts:47-110 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. It keeps answers for one repository namespace's
task context and holds no identity that ranges beyond it.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-30T14:18:54+02:00 — 260928-MIK-L32 curator (staged change set on `ar/260928-mik-l32`, code base `07d6584afba8a9504e4a3cf2e80eac41f68b28a9`): No content impact: this card's own source is unchanged. MIK-R32 moved lines in `dashboard/src/panels/review/ReviewSurface.tsx`, so the citation rows into them that moved were re-pointed by the installed fixer (run once; its generated bullets are kept, since no claim was reworded) or by the exact base-to-staged line shift for the rows it declined; every re-pointed row was byte-identical to memory HEAD beforehand and was checked to hold its anchors in the new range. The fixer's normalisation also re-measured passing rows into files this leaf did not change (`dashboard/src/panels/review/ReviewReadCache.ts`); no claim changed. No verification stamp was advanced.
- 2026-09-28T21:46:34+02:00 — 260921-ICR-L48 curator (uncommitted candidate tree `ac73216e2a763b72844a63b8c36c81f9a8b5f0e8` over code base `cb1b942af60a7ed5006ac992075d2bf96aeb9fa7`): **created this one-to-one card for the new per-comparison read cache (`ICR-R24@v3`).** It records the two keyed stores, the rule that only content answers are kept, the generation rule that empties both stores on any admitted answer from another comparison, the LRU bounds (24 reviews, 32 sources) and the one-surface lifetime, plus review observations O-R1-1 (cached returns are not a live check, by design) and O-R1-5 (recency touched during render). The verification hash and date are blank because no commit contains this file yet; closeout owns the stamp.
