# dashboard/src/panels/detail-panel/reviewEntryRefusal.test.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

The mounted pin for the task document's **compact Intent review entry** (`ICR-R24@v3`, leaf
`260921-ICR-L47`), and for the entry half of ICR-R16 (brief states, never swallowed) and ICR-R17 (the
entry re-reads only for its own comparison). It drives the real `DocChangeSetBar` over the real review
and change-set clients with only `fetch` stubbed. The Intent review control reads
`/api/review/intent/summary`, which answers every typed state with 200 and the state in the body.

Its header records the defects measured on the installed dashboard before L47, which every case here
fails against: the Intent review reused the change-set button and so printed the change set's
code+memory **line totals** (`+3775 −1056` on L41) and made a second identical committed request; the
entry read the whole subject catalogue before the reviewer was opened and re-read it whenever the
serialized global analytics document moved; and it printed whole backend explanations inside and beside
itself.

Before L47 this module pinned the catalogue-based entry (a refusal paragraph beside the entry, a
known-empty line, a subject picker and an analytics-driven refresh). That design is **superseded**; the
module was rewritten, and those cases no longer exist.

## Code Commentary

### Logic

**Fixtures.** `UNAVAILABLE` is the summary route's `unavailable` answer carrying the real
never-initialized refusal (`candidate_dataset_absent`, its detail and next action verbatim, offending
input `knowledge-candidate.sqlite`). `counted(added, removed, extra)` builds a counted (or, with
`unresolved`, partial) body whose parts sum to its totals. `COUNTERS` carries change-set **line totals
that must never appear** on the Intent review control. `serve(summaries)` answers the summary route
with each answer in turn and every other route with `COUNTERS`; `urlsOf` counts requests per route;
`liveLeaf` seeds a live enclosure; `mount` renders the bar and returns the `onOpen` spy.

**The compact entry.** One control, `⇄ Intent review+4 −2`, whose text never contains the line totals;
the removed constructs (subject picker, catalogue totals, entry state paragraph, entry refresh control)
are asserted absent; a click opens the task-context target `review: {}`. **Request economy:** selecting
a live leaf makes exactly one summary read, zero catalogue (`/api/review/intent/entries`) reads, one
committed and one working change-set read — three requests in all.

**Brief states (ICR-R16).** Missing knowledge shows `no knowledge yet` with
`data-review-state="not-initialized"` and `data-review-code="candidate_dataset_absent"`, never a
`+N −N`; the code, reason, offending input and next action are inside a closed `<details>` disclosure;
the control still opens the review. A body the route did not produce (a 502) is `unreadable` with its
status in the disclosure and no invented refusal. A partial answer shows its counts plus `partial`, and
the disclosure says how many subjects were left out.

**Invalidation (ICR-R17).** An unrelated workspace publication (the analytics delta) causes no summary
re-read, while a move in this leaf's own lifecycle facts does; an answer for a previous leaf, held open
until after the bar moved to another leaf, is dropped.

**Committed counter state (B6, from L25).** A committed read of a leaf whose range nothing recorded
shows the brief `unrecorded` state, the route's sentence only in the disclosure, and never its zero as a
total; it stays apart from a measured-empty range and from a refusal.

### Conventions

It imports the real bar and the shipped `enclosure`/`seedProjection` helpers from `./test-utils`, so
the store it seeds is the store the dashboard reads. Assertions read `data-intent-state`,
`data-review-state`, `data-review-code`, element text and the `onOpen` spy's recorded target; the
disclosure is asserted closed by default. Global fetch is restored in `afterEach`.

### Invariants And Boundaries

- **The Intent review numbers are intent counts, never line totals.** The line-total fixture exists
  to catch exactly that regression.
- **The entry reads no catalogue.** Selecting a leaf makes one summary read; the catalogue belongs to
  the reviewer.
- **Unavailable is never `+0 −0`.** A refused summary shows a brief word and no numbers.
- **The entry never gates on its read.** Every state still opens `review: {}`.
- **Nothing is invented.** An unreadable answer carries no refusal fields it never had.
- **Boundary.** It does not drive the reviewer (`panels/review/ReviewSurface.entryEconomy.test.tsx`
  owns the reviewer's catalogue economy) or the cockpit-level re-validation triggers
  (`cockpit/Cockpit.intentEntry.test.tsx`).

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

Every anchor in a row occurs inside the range that row cites.

- **The header: what is exercised and the measured pre-L47 defects (line totals, a second committed request, eager catalogue).** [1]
- The real bar and the shipped store-seeding helpers. [2]
- **The summary route's unavailable answer with the owner's refusal verbatim.** [3]
- A counted or partial body whose parts sum to its totals. [4]
- Line totals that must never appear on the Intent review control. [5]
- The one stub and the per-route request counter. [6]
- The live-leaf seeding and the mount. [7]
- **One control with intent counts and nothing beside it; the click opens the task context.** [8]
- **One summary read, no catalogue read, one committed read.** [9]
- **Missing knowledge stated briefly, never as `+0 −0`, with the refusal in a closed disclosure.** [10]
- An unreadable answer, with no invented refusal. [11]
- Partial counts marked and explained. [12]
- **No re-read for unrelated publications; a re-read when this leaf's lifecycle moves.** [13]
- A previous leaf's late answer is dropped. [14]
- **260921-ICR-L25, register B6: the unrecorded committed range shown briefly, its sentence on demand, never its zero as a total, and kept apart from measured-empty and from a refusal.** [15]
- The control, its summary read and the disclosure these cases drive. [16]
- The bar's composition and the leaf-scoped invalidation facts. [17]

### Cross-Repo References

No cross-repository behavior is exercised in this file. Every response is served by a stubbed
same-origin `fetch` and names one repository namespace.

No meaningful cross-repo references found.

## 260921-ICR-L17 The Entry Notices A New Generation, And No Superseded Read Wins (superseded by 260921-ICR-L47)

`260921-ICR-L17` (`ICR-R17@v1`) added cases for the catalogue-based entry: re-reading the catalogue
when the analytics projection was republished, the `review-catalogue-refresh` control and its stale
marker, and a previous leaf's answer that must not win. **`260921-ICR-L47` removed that entry design**
(no catalogue at the entry, no entry refresh control, no analytics subscription), so those cases were
replaced. What L17 pinned survives in its current form: a previous leaf's late answer is still dropped,
and invalidation is now leaf-scoped (an unrelated publication re-reads nothing), as the Logic section
above records. The cockpit-level re-validation points ruled for L47-R1-F2 are pinned in
`cockpit/Cockpit.intentEntry.test.tsx`.
