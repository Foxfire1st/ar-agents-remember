# dashboard/src/panels/review/ReviewReadCache.ts

## Governing Overview

[review route overview](overview.md)

## Purpose

Retain bounded whole-subject review answers for one mounted surface and invalidate them by comparison generation or review-input epoch.

## Code Commentary

The review store is a 24-entry LRU: a read refreshes recency and a write evicts the oldest entry above the bound. The read cycle supplies question keys and decides whether an admitted answer is whole and reusable; paged questions, refusals and failures remain that owner's responsibility. Refresh forgets the question before re-asking.

`comparisonGenerationOf` records both code-tree IDs and knowledge snapshots only when the answer compared knowledge. `sameGeneration` requires equal tree pairs and, when both snapshot pairs are known, equal snapshot pairs. An answer without knowledge comparison does not erase a known snapshot pair. `observe` clears incompatible generations even for an answer not retained; compatible answers preserve known snapshots.

`keepUnshown` can retain a read that was superseded before display only when its generation remains compatible; it cannot move the store to an older incompatible generation. `invalidateReviews` increments inputEpoch and clears the review store so the read-cycle owner can reject old-epoch completions. This cache is mounted working state, with no persistent record or file-content store.

## Evidence

- ReviewReadCache.ts current behavior at this source owner. [32]
- ReviewReadCache.ts current behavior at this source owner. [33]
- ReviewReadCache.ts current behavior at this source owner. [34]
