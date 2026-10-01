# dashboard/src/panels/review/ReviewSurface.applicability.test.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

The mounted-surface cases for `ICR-R26@v1`'s record labels: the **real** `ReviewSurface` over the
**real** review client, with only `fetch` stubbed. Every request is built by the shipped client and
every response travels the way the browser's does — status, body, the shared decode, the component tree
— and no assertion reads a prop the test itself passed.

The defect these cases catch is the client half of F09: a record of another subject rendering beside the
selected one with nothing that says why it is there. Four cases, one property each: a record's own
treatment is mounted with the **true subject** its binding names; the labelled context row shows the
relationship that reached it and **never** the sibling's finding; the six-way counts are stated beside
the collections they filtered; a previous generation's record is labelled `historical` with the
candidate tree it examined; and a payload published **before** these labels existed still renders —
which is the additive-compatibility property the server's optional fields exist for.

## Code Commentary

### Logic

The comparison-focused cases isolate the shared catalogue hook so its additional request cannot consume a comparison fixture. The ordinary-entry catalogue/comparison interaction is covered separately by ReviewSurface.navigation.test.tsx. Assertions follow the compact labels, central display controls and changed-region default without weakening the existing record, paging or refusal contracts.

**Two label fixtures are built once and shared, and the payload is a real wire body.** `directLabel`
(`:37-47`) and `historicalLabel` (`:48-58`) are the two `ReviewDisplayedApplicability` values the cases
mount, each naming its own subject and references. `payload(labels: boolean)` (`:59-203`) assembles the
whole `KnowledgeReviewPayload` the surface consumes — both panes, the assessments, the context rows, the
six-way summaries and the revision selection — and the boolean is the **only** difference between the
two bodies: with the labels it carries the `applicability` fields, the `context` rows and the
`applicability` counts; without them it carries none, which is exactly what a body published before this
requirement looks like. `reviewed` (`:204-210`) wraps a body in the route's `review` envelope and
`response` (`:211-219`) turns it into a real `Response`, so what the client decodes is a body rather
than a fixture object.

**The four cases, one property each:**

1. `"mounts each record's own treatment and the true subject of labelled context"` (`:238-265`) — three
   assessment rows mount, the direct one prints `applicability: direct (invariant <SUBJECT>)`, the
   label also travels on the evidence pane's copy of the same record (so one selection cannot be
   displayed with two treatments in two panes), the context row states the sibling's **true subject**
   and the recorded relationship that reached it (`realization 0cca9e84 at src/batch.py`), and the
   sibling's finding text is **absent** from the document — the contamination this requirement prevents.
2. `"states the six-way counts beside the collections it filtered"` (`:267-281`) — the
   `review-applicability` block prints `supplied assessments: 4` with `direct 1`, `historical 1`,
   `context 1` and `not displayed 1`, so the filtering is visible as arithmetic on the page.
3. `"labels a previous generation's record as historical rather than as the current result"`
   (`:283-297`) — a `[data-applicability="historical"]` node exists, names the selected subject and
   carries the old candidate tree id it examined.
4. `"still renders a payload published before the labels existed"` (`:299-310`) — the unlabelled body
   renders its two assessment rows and mounts **no** context block and **no** counts block, so a client
   released before this vocabulary still works against a server that sends it.

### Conventions

The module stubs `fetch` with `vi.stubGlobal` and cleans up in `afterEach` (`:232-235`), so no global
survives a case; `mountSubject` (`:220-231`) is the one mount helper and every case reads the rendered
document rather than component state. The assertions use the same `data-testid` hooks the production
component publishes (`review-assessment`, `review-context`, `review-applicability`) plus the new
`data-applicability` attribute and the `data-context-of` attribute, so a case fails when the *rendered*
label changes rather than when a prop does.

### Invariants And Boundaries

- **The client renders what the server sent.** A missing `applicability` prints nothing extra; nothing
  is defaulted, inferred or repaired on the client, which is why the pre-label case passes.
- **A context row never carries a judgment.** The case asserts the sibling's finding text is absent from
  the whole document, not merely from one list.
- **One record, one treatment, both panes.** The same label is asserted on the knowledge pane's copy and
  on the evidence pane's copy of the same assessment.
- **The counts are rendered as the server stated them.** The client formats them and adds nothing; the
  partition itself is the server model's validator, not this module's arithmetic.
- **No browser journey is claimed here.** These are jsdom mount cases; the assembled A14/A15 acceptance
  belongs to `ICR-R25@v1` and the reviewer workspace to `ICR-R24@v1`.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- **The two label fixtures the cases mount, each naming its own subject and references.** [1]
- **The two real wire bodies: one with the labels, context rows and counts, one without any of them.** [2]
- **The envelope and the real `Response` the client decodes.** [3]
- **The one mount helper, and the cleanup that keeps no global across a case.** [4]
- **The F09 client case: the treatment and the true subject are mounted, and the sibling's finding is nowhere in the document.** [5]
- **The counts case: the six-way partition is rendered beside the collections it filtered.** [6]
- **The historical case: a previous generation is labelled and never reads as the current result.** [7]
- **The additive-compatibility case: a body published before the labels existed still renders.** [8]
- **The client vocabulary these cases mount, and the fields the surface gained.** [9]
- **The rendered labels themselves: the per-record note, the context list and the counts block.** [10]
- **The two call sites that mount them, on the knowledge pane and on the evidence pane.** [11]
- **The server-side case this client mirrors: a sibling's record is context and never the selected subject's.** [12]

### Cross-Repo References

No cross-repository behavior is implemented in this module. It mounts the dashboard's own surface over
its own origin.

No meaningful cross-repo references found.
