# dashboard/src/panels/review/ReviewReadCache.test.ts

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

Unit evidence for the reviewer's per-comparison cache (`ReviewReadCache.ts`, `260921-ICR-L48`): the two
stores stay within their bounds and evict least-recently-used entries, a refusal is never kept, and any
answer from another comparison generation empties both stores.

## Current verification scope

The unshown-answer case additionally checks same-generation retention, rejection of an incompatible answer without moving the displayed generation, and invalidation when the first displayed answer names another generation. The existing bounds/refusal/source keys remain the same.

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

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- The module's one-line statement of what it pins, and the names it imports. [1]
- Payloads derived from a captured review, varying only the generation fields. [2]
- Review bound at two sizes, with recency refreshed by reads. [3]
- Source bound at two sizes, and no refusal kept. [4]
- Another generation empties both stores; a task-context answer cannot move the snapshot pair. [5]
- The generation comparison and the content key. [6]
- The class under test. [7]

### Cross-Repo References

No cross-repository behavior is exercised in this file.

No meaningful cross-repo references found.
