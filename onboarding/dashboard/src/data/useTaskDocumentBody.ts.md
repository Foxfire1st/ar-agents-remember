# dashboard/src/data/useTaskDocumentBody.ts

## Governing Overview

[data overview](overview.md)
frontend source overview governs this reader-state hook.

## Purpose

Visible entry body hydration, availability and current-summary merge over store-owned bounded resources.

## Code Commentary

### Logic

`useTaskDocumentBody(entry)` requests only an addressed authored entry using repository/path/bodyRevision. Store resources deduplicate pending reads and retain bodies across navigation; one hook-local settled record permits an oversized active body without retaining it in history. A different returned revision is unavailable for the initiating key and retained only under its actual revision. The body supplies
long-form objective, nonGoals, acceptance, requirements, design, code, decisions, questions, references,
sections. `mergeFixedProse` restores nonGoals and acceptance from the body with
nullish summary fallback; empty strings remain supplied values. These fixed-prose fields, like the
other long reader content, are merged before the revision gate; absent/null response fields retain
the summary. Entry identity/stage/activity/counts remain authoritative; current summary step/review facts remain unchanged. For a matching body revision, marked truncated status/step text is restored
only when the body carries a strictly longer string; steps must agree in count and ordered IDs. A matching
review round can restore the full findings list or longer marked descriptions without replacing the
summary's whole-round counts. The hook reports `loading`, `available`,
or `unavailable`; the returned document merges the available body into the current summary.

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
- An unchanged qualified repository/path reference plus bodyRevision reuses bounded history or the active settled result; a different repository, path or requested revision selects a different key. Returned bytes are retained only under their actual bodyRevision.
- A failed key is terminal until selection or revision changes; analytics object replacement does not
  accidentally retry it.
- Summary content remains renderable while loading and is the fallback when the full body is unavailable.
- No retry timer or request fan-out is introduced here.
- A cached body never replaces the current summary's head, step states, review round or aggregate counts.
  Matching-revision hydration expands previews; an older body contributes long reader content only.
- The hook does not decide which task document is visible and does not perform path confinement; those
  responsibilities stay with `DetailPanel` and the serving endpoint respectively.

### Todos

- Body and preparation history are store-owned and bounded separately at 64 entries / 16 MiB; pending body reads are bounded too. One active oversized body is hook-local, not retained history.

## Evidence

### Docs References

No external Domain Documentation source is configured for this memory repo.

No configured external document defines this same-repository React state seam.

### Repo-Internal References





- Current TaskPage passes bodyState into ReaderHead, whose change-set controls are unmounted while loading; the deleted lifecycleBody is not its caller. [3]



- The transport adapter owns the same-origin endpoint and non-OK rejection. [5]

- Source-defined taskBody.test.tsx component assertions hold the body request open, check body-first ordering, cover long fields and fallback, and pin revision caching. Source inspection only; no fresh execution. [6]


- Fixed prose is merged by the production body hook; separate native-operand mounted DetailPanel cases start from summaries missing nonGoals/acceptance, stub transport, and declare assertions for restored fields, fixed-block order, legacy access and one body request. This is source inspection, not a new producer/test run or acceptance. [8]

- Retained body identity combines the qualified repository/path reference with the body revision, not a path-only key. [9]

### Cross-Repo References

No meaningful cross-repo boundary exists; selection, hydration, serving, and task-document parsing all
live in `agents-remember`.

Same-repository dashboard reader state only.
