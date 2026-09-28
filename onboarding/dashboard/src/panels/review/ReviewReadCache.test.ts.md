# dashboard/src/panels/review/ReviewReadCache.test.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/ReviewReadCache.test.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-28T21:46:34+02:00 |
| lastVerifiedCommitHash |  `ae2fd5c864aa2609ae45b5c7dbbaa693569aefc6`|
| lastVerifiedCommitDate |  2026-09-28T22:11:57+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

Unit evidence for the reviewer's per-comparison cache (`ReviewReadCache.ts`, `260921-ICR-L48`): the two
stores stay within their bounds and evict least-recently-used entries, a refusal is never kept, and any
answer from another comparison generation empties both stores.

## Code Commentary

### Logic

Six cases in four blocks. The two bounds blocks are `it.each` over two input sizes each (limit + 5 and
3 × limit for reviews; limit + 1 and 2 × limit for sources), so a bound that only held at one size would
fail. The review block reads `subject-0` before every insertion to prove that reading refreshes recency:
`subject-0` survives while `subject-1` is evicted. The source block also offers a typed refusal and
asserts it is not kept. The generation case keeps a knowledge-compared review and a content answer, shows
that a task-context answer (no snapshots) does not move the snapshot pair, then observes a paged/refreshed
answer with another snapshot and asserts both stores are empty; a later code-tree change empties them
again. The last case pins `sameGeneration` and the content key's sensitivity to the after tree.

### Conventions

Real captured semantic content: `payloadAt` derives payloads from `familyReview.complete.captured.json`,
varying only the after code tree and after snapshot; `content` builds a minimal content answer. No fetch,
no rendering — the class is exercised directly, and the mounted return-without-request behaviour is pinned
by `ReviewSurface.navigation.test.tsx`.

### Invariants And Boundaries

Scoped executable evidence of the cache's own rules. It does not prove the read cycle calls `keepReview`
only for whole, identity-free answers, nor that the surface owns one cache per mount; those are pinned by
the navigation and read-cycle modules.

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
| The module's one-line statement of what it pins, and the names it imports. | `REVIEW_CACHE_LIMIT`; `SOURCE_CACHE_LIMIT`; `sameGeneration`; `sourceContentKey` | dashboard/src/panels/review/ReviewReadCache.test.ts:1-12 |
| Payloads derived from a captured review, varying only the generation fields. | `payloadAt`; "familyReview.complete.captured.json" | dashboard/src/panels/review/ReviewReadCache.test.ts:14-38 |
| Review bound at two sizes, with recency refreshed by reads. | "keeps at most the bound of reviews and evicts the least recently used (%i inserted)" | dashboard/src/panels/review/ReviewReadCache.test.ts:47-63 |
| Source bound at two sizes, and no refusal kept. | "keeps at most the bound of source answers (%i inserted) and never keeps a refusal" | dashboard/src/panels/review/ReviewReadCache.test.ts:65-81 |
| Another generation empties both stores; a task-context answer cannot move the snapshot pair. | "empties both stores when an answer belongs to another comparison generation" | dashboard/src/panels/review/ReviewReadCache.test.ts:83-99 |
| The generation comparison and the content key. | "treats code trees and compared snapshots as the generation" | dashboard/src/panels/review/ReviewReadCache.test.ts:101-110 |
| The class under test. | `ReviewReadCache`; `BoundedStore` | dashboard/src/panels/review/ReviewReadCache.ts:32-67; dashboard/src/panels/review/ReviewReadCache.ts:106-150 |

## Cross-Repo References

No cross-repository behavior is exercised in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-28T21:46:34+02:00 — 260921-ICR-L48 curator (uncommitted candidate tree `ac73216e2a763b72844a63b8c36c81f9a8b5f0e8` over code base `cb1b942af60a7ed5006ac992075d2bf96aeb9fa7`): **created this one-to-one card for the new cache unit module (6 cases).** Records the two-size bounds cases, the recency-by-read proof, the no-refusal rule, the generation-invalidation case (including that a task-context answer cannot move the snapshot pair) and the key case, and names where the mounted behaviour is pinned instead. The verification hash and date are blank because no commit contains this file yet; closeout owns the stamp.
