# dashboard/src/panels/review/ReviewSurface.applicability.test.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/ReviewSurface.applicability.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-23T02:30+02:00 |
| lastVerifiedCommitHash | `63b476297708f779de8ed5c0bf3555b9d1de70c2` |
| lastVerifiedCommitDate | 2026-09-24T04:10:11+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

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

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| **The two label fixtures the cases mount, each naming its own subject and references.** | `directLabel`; `historicalLabel` | dashboard/src/panels/review/ReviewSurface.applicability.test.tsx:37-47; dashboard/src/panels/review/ReviewSurface.applicability.test.tsx:48-58 |
| **The two real wire bodies: one with the labels, context rows and counts, one without any of them.** | `payload` | dashboard/src/panels/review/ReviewSurface.applicability.test.tsx:59-203 |
| **The envelope and the real `Response` the client decodes.** | `reviewed`; `response` | dashboard/src/panels/review/ReviewSurface.applicability.test.tsx:204-210; dashboard/src/panels/review/ReviewSurface.applicability.test.tsx:211-219 |
| **The one mount helper, and the cleanup that keeps no global across a case.** | `mountSubject` | dashboard/src/panels/review/ReviewSurface.applicability.test.tsx:220-231; dashboard/src/panels/review/ReviewSurface.applicability.test.tsx:232-235 |
| **The F09 client case: the treatment and the true subject are mounted, and the sibling's finding is nowhere in the document.** | "mounts each record's own treatment and the true subject of labelled context" | dashboard/src/panels/review/ReviewSurface.applicability.test.tsx:238-265 |
| **The counts case: the six-way partition is rendered beside the collections it filtered.** | "states the six-way counts beside the collections it filtered" | dashboard/src/panels/review/ReviewSurface.applicability.test.tsx:267-281 |
| **The historical case: a previous generation is labelled and never reads as the current result.** | "labels a previous generation's record as historical rather than as the current result" | dashboard/src/panels/review/ReviewSurface.applicability.test.tsx:283-297 |
| **The additive-compatibility case: a body published before the labels existed still renders.** | "still renders a payload published before the labels existed" | dashboard/src/panels/review/ReviewSurface.applicability.test.tsx:299-310 |
| **The client vocabulary these cases mount, and the fields the surface gained.** | `ReviewDisplayedApplicability`; `ReviewContextRecord`; `ReviewApplicabilitySummary`; `ReviewKnowledgePane` | dashboard/src/data/review.ts:107-142; dashboard/src/data/review.ts:166-178; dashboard/src/data/review.ts:169-191; dashboard/src/data/review.ts:217-238 |
| **The rendered labels themselves: the per-record note, the context list and the counts block.** | `applicabilityNote`; `contextList`; `applicabilityCounts` | dashboard/src/panels/review/ReviewSurface.tsx:104-152 |
| **The two call sites that mount them, on the knowledge pane and on the evidence pane.** | `KnowledgePane`; `EvidencePane` | dashboard/src/panels/review/ReviewSurface.tsx:275-300; dashboard/src/panels/review/ReviewSurface.tsx:354-407 |
| **The server-side case this client mirrors: a sibling's record is context and never the selected subject's.** | `test_a_sibling_subjects_assessment_is_context_and_never_the_selected_subjects` | mcp/tests/test_knowledge_review_subject_isolation.py:221-252 |

## Cross-Repo References

No cross-repository behavior is implemented in this module. It mounts the dashboard's own surface over
its own origin.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-24T00:43:00+02:00 — 260921-ICR-L24 curator (memory worktree only; no code changed; no commits; leaf base `5f14fc6790cafc3ad2ae612c2e67f176392dc1fe` plus the working-tree delta): **four enforced citation rows re-cited to the constructs they name, wording unchanged.** The vocabulary row gained the two ranges its own anchors needed — `ReviewContextRecord` at `data/review.ts:166-178` and `ReviewKnowledgePane` at `:217-238` — while the two contributing ranges it already carried (`ReviewDisplayedApplicability` `107-142`, `ReviewApplicabilitySummary` `169-191`) are kept verbatim; the call-site row followed the two panes this leaf's surface shortened to their own extents (`ReviewSurface.tsx:275-300` for `KnowledgePane`, `:354-407` for `EvidencePane`). No claim was reworded or dropped and no contributing range was removed. **Stamp accounting:** no verification stamp was advanced — the candidate is uncommitted (base `5f14fc6790cafc3ad2ae612c2e67f176392dc1fe` plus the working-tree delta) and governed closeout owns the real stamp.
- 2026-09-23T02:30:00+02:00 — 260921-ICR-L26 curator (candidate `ar/260921-icr-l26`, uncommitted; production line at this leaf's base `2edad477bcd9127a90e4618d345ce34ef7e6a6d9`, confirmed from the enclosure contract): created this one-to-one card for the mounted-surface cases this leaf introduced (`ICR-R26@v1`). The card records the two real wire bodies the module builds (one labelled, one not), the four properties its cases pin — the true subject of a labelled context row and the absence of the sibling's finding, the six-way counts rendered as arithmetic, the historical label with the tree it examined, and the additive compatibility of a pre-label body — and the boundary that these are jsdom mount cases rather than the assembled A14/A15 acceptance R25 owns. **Stamp accounting:** the verification pair names the production line at this leaf's base — the last real commit the reading was taken against — because every construct this card cites exists only in this leaf's uncommitted candidate; the governed closeout owns the real stamp once the code commit exists.
