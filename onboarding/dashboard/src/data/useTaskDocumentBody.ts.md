# dashboard/src/data/useTaskDocumentBody.ts

## Governing Overview

[data overview](overview.md)
frontend source overview governs this reader-state hook.

## Purpose

Owns visible task-document body hydration, availability state, and revision-aware browser-session
caching. It gives `DetailPanel` one authoritative state for rendering complete task content first and
for delaying lower-priority reader requests until the body fetch has either succeeded or failed.

## Code Commentary

### Logic

`taskDocumentBodyKey` combines `docPath` with `bodyRevision`. `useTaskDocumentBody(targetDoc)` requests
only the currently displayed document through `fetchTaskDocument`, stores the successful body payload
separately under the combined key, and merges that payload into the current summary at render time.
The effect depends on the stable path/revision identity rather than the projected `TaskDocNode` object,
so analytics projection replacement does not cancel or duplicate an unchanged request. The merge
explicitly keeps summary arrays when the response omits them. The hook reports `loading`, `available`,
or `unavailable`; `documentFor(doc)` substitutes a body only when that document's path and revision
match.

The failed-request state is recorded without an automatic retry loop. Leaving and reselecting the
document, or receiving a new `bodyRevision`, gives the hook a new effect entry and permits another
request. An effect cleanup ignores late results after the visible document changes.

### Conventions

Selection remains outside this module: `DetailPanel` resolves the one document actually shown, and
this hook owns only that document's hydration. HTTP construction stays in `taskDocuments.ts`. Consumers
use the returned state both for honest loading/fallback copy and to keep reader-ancillary request
components unmounted until body hydration reaches a terminal state.

### Invariants And Boundaries

- The always-on task projection remains summary-only; this hook does not enlarge snapshot or stream
  payloads.
- An unchanged `docPath + bodyRevision` fetches once per mounted hook cache; a revision change refetches.
- A failed key is terminal until selection or revision changes; analytics object replacement does not
  accidentally retry it.
- Summary content remains renderable while loading and is the fallback when the full body is unavailable.
- No retry timer or request fan-out is introduced here.
- The endpoint returns a full fetch-time task node. Its present scalar fields (including status, steps,
  title, and progress counters) can mask fresher summary values because `bodyRevision` hashes authored
  body fields only; this pre-existing staleness window is not solved by the hook.
- The hook does not decide which task document is visible and does not perform path confinement; those
  responsibilities stay with `DetailPanel` and the serving endpoint respectively.

### Todos

- Reviewer note: consider a follow-up to widen `bodyRevision` or prune cached payload fields if the
  product requires post-hydration progress/status freshness. This leaf preserves the existing
  endpoint and revision contract.
- The browser-session cache is revision-safe but unbounded; it has no eviction policy.

## Evidence

### Docs References

No external Domain Documentation source is configured for this memory repo.

No configured external document defines this same-repository React state seam.

### Repo-Internal References

- The hook keys requests and body-payload storage by path/revision, merges into the current summary, records terminal availability, and discards late results. [1]
- `DetailPanelImpl` resolves the displayed reader document and passes it through the body hook. [2]
- The enclosure change-set controls wait until the body reader is no longer loading. [3]
- The task-document reader delays its notes until the body reader is no longer loading. [4]
- The transport adapter owns the same-origin endpoint and non-OK rejection. [5]
- Component regressions hold the body request open, assert body-first ordering, cover full fields and fallback, and pin revision caching. [6]
- Cockpit composition regressions cover direct leaf, master, drilled, lifecycle-bound, analytics-churn, and pending A-to-B late-response selection paths. [7]

### Cross-Repo References

No meaningful cross-repo boundary exists; selection, hydration, serving, and task-document parsing all
live in `agents-remember`.

Same-repository dashboard reader state only.
