# dashboard/src/data/useTaskDocumentBody.ts

## Governing Overview

[data overview](overview.md)
frontend source overview governs this reader-state hook.

## Purpose

Owns visible task-document body hydration, availability state, and revision-aware mounted-hook-instance
caching. It gives `DetailPanel` one authoritative state for rendering complete task content first and
for delaying lower-priority reader requests until the body fetch has either succeeded or failed.

## Code Commentary

### Logic

`taskDocumentBodyKey` combines `docPath` with `bodyRevision`. `useTaskDocumentBody(targetDoc)` requests
only the currently displayed document through `fetchTaskDocument`, stores the successful body payload
separately under the combined key, and merges that payload into the current summary at render time.
The effect depends on the stable path/revision identity rather than the projected `TaskDocNode` object,
so analytics projection replacement does not cancel or duplicate an unchanged request. The body supplies
long-form objective, nonGoals, acceptance, requirements, design, code, decisions, questions, references,
sections and sub-task content. `mergeFixedProse` restores nonGoals and acceptance from the body with
nullish summary fallback; empty strings remain supplied values. These fixed-prose fields, like the
other long reader content, are merged before the revision gate; absent/null response fields retain
the summary. Identity, status, progress and review facts remain
those of the current summary. For a matching body revision, marked truncated status/step text is restored
only when the body carries a strictly longer string; steps must agree in count and ordered IDs. A matching
review round can restore the full findings list or longer marked descriptions without replacing the
summary's whole-round counts. The hook reports `loading`, `available`,
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
- A cached body never replaces the current summary's head, step states, review round or aggregate counts.
  Matching-revision hydration expands previews; an older body contributes long reader content only.
- The hook does not decide which task document is visible and does not perform path confinement; those
  responsibilities stay with `DetailPanel` and the serving endpoint respectively.

### Todos

- The mounted hook instance keeps revision-safe, unbounded body/state storage with no eviction
  policy. Unmounting discards that hook-local cache; it is not browser-session persistence.

## Evidence

### Docs References

No external Domain Documentation source is configured for this memory repo.

No configured external document defines this same-repository React state seam.

### Repo-Internal References

- The hook keys requests and body-payload storage by path/revision, merges into the current summary, records terminal availability, and discards late results. [1]

- `DetailPanelImpl` delegates reader selection to `useDetailPanelState`; that state owner resolves the displayed document and calls the body hook. [2]

- The enclosure change-set controls and reader-head controls wait until the body reader is no longer loading. [3]

- The task-document reader delays its notes/reference/report readers until the body reader is no longer loading. [4]

- The transport adapter owns the same-origin endpoint and non-OK rejection. [5]

- Source-defined taskBody.test.tsx component assertions hold the body request open, check body-first ordering, cover long fields and fallback, and pin revision caching. Source inspection only; no fresh execution. [6]

- Source-defined Cockpit composition assertions cover direct leaf, master, drilled, lifecycle-bound, analytics-churn, and pending A-to-B late-response selection paths. Source inspection only; no fresh execution. [7]

- Fixed prose is merged by the production body hook; separate native-operand mounted DetailPanel cases start from summaries missing nonGoals/acceptance, stub transport, and declare assertions for restored fields, fixed-block order, legacy access and one body request. This is source inspection, not a new producer/test run or acceptance. [8]
### Cross-Repo References

No meaningful cross-repo boundary exists; selection, hydration, serving, and task-document parsing all
live in `agents-remember`.

Same-repository dashboard reader state only.
