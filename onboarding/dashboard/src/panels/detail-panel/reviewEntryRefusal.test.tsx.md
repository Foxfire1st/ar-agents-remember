# dashboard/src/panels/detail-panel/reviewEntryRefusal.test.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/detail-panel/reviewEntryRefusal.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-22T15:15:00+02:00 |
| lastVerifiedCommitHash | `c422dc00273d4ae7a5d8c9c8db97365b8c85d640` |
| lastVerifiedCommitDate | 2026-09-23T05:16:40+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

The entry half of ICR-R16, at the **persistent, discoverable entry**: the task document's Intent-review
bar shows what the entry read answered instead of dropping it.

It drives the real `DocChangeSetBar` over the real review client with only `fetch` stubbed. The bar's
entry read goes to `/api/review/intent/entries`, whose refusals the route publishes in the body of a
non-2xx response — the read that used to be thrown away, leaving the entry with nothing to say
(`VERIFICATION.md` F08: "Entry catches this and hides itself"). The refusal body is the real route's
measured `404` for a never-initialized task (`sha256-normalized fdbabc97…`), with its code, reason,
offending input and next action verbatim; `repository_id`/`master`/`leaf_id` are the request echoes of
this module's own task context, which is what the route echoes them from.

The defect these cases catch is stated as a hook behaviour rather than a rendering one: the hook set its
subject to `undefined` on any failure, so **a refused read and an empty list were indistinguishable and
neither was ever shown** — the reader saw an entry with no reason, or (before that) no entry at all.
Every case here fails against that hook.

## Code Commentary

### Logic

**One measured refusal body, declared once.** `entryRefusal` carries the real `404`'s `state:
"refused"`, `operation: "list_knowledge_review_entries"`, the request echoes, `entries: []` and the
refusal's own four fields including `offending_input: "knowledge-candidate.sqlite"`. Its reason and next
action are the two sentences the route published, kept verbatim rather than paraphrased, so a failing
assertion points at the route's own words.

**`COUNTERS` is the fixture that makes the bar's other reads inert.** The bar renders three buttons and
each performs its own change-set read; `COUNTERS` is the body those reads answer with, so a case can
assert about the entry's state without the counter reads failing. `serveEntry(status, body, statusText)`
is the one stub and it answers **only** the entries URL, letting the counter reads through — which is
what a real client would see.

**`liveLeaf()` seeds the store so the leaf reads as live**, because the entry is gated on liveness and
nothing else; `mount()` renders the bar and hands back the `onOpen` spy; `intentButton(view)` finds the
button whose text carries `Intent review` among the bar's `open-changeset` buttons rather than by index,
so the case cannot silently assert about the wrong button.

**Four cases, one per answer the read can give.** A never-initialized refusal is shown beside the entry
**and the entry is still offered** — the case asserts `data-review-state="not-initialized"`, the code,
the reason, the next action **and** the offending input (the fix round's F2), then clicks the button and
asserts it opens the **task-context** target `review: {}`, because that review needs no dataset. A
subject-less `200` says known empty without calling it a failure. A transport failure says `network`
with the reason and **raises no refusal body it does not have** — the read threw, so no `offendingInput`
or `nextAction` may be invented — and again still offers the entry. And a successful answer carries the
server's recorded subject into the entry (`selectorKind: "invariant"`, `selectorId: "inv-1"`) while
printing **no** state at all, so a working read is not decorated with a refusal line. Since
`260921-ICR-L9` the success case's stub payload mirrors the catalogue wire shape additively —
`selected_item_count: 3` became `presence: "both"` beside the additive `total_subjects`/
`invariant_total`/`family_total` — with **no assertion changed**; this leaf's own traversal claims
live in `changeSetBar.test.tsx`, not here.

### Conventions

The module imports the real bar and the shipped test helpers (`enclosure`, `seedProjection`) from
`./test-utils`, so the store it seeds is the store the dashboard really reads. Constants are upper-case;
helpers are lower-case plain functions; every case is an `async` `it` inside one `describe`, and the
global fetch is restored in `afterEach`. Assertions read `data-review-state`, `data-review-code` and
`textContent` from the DOM, plus the `onOpen` spy's recorded argument — a target, not a rendered string,
because the target is what the click actually decides.

### Invariants And Boundaries

- **The entry never gates on the read.** Every refusal case asserts the button is still present and still
  opens `review: {}`; a refusal here is a stated reason, not a missing control.
- **A refusal is printed, never swallowed.** The hook carries the read's own `ReviewFailure` through
  `reviewProblemFromRefusal`/`reviewProblemFromCause`/`unreadableAnswer`, so a refusal, an unadmitted
  answer and a transport failure all reach `ReviewEntryState` as their own token.
- **The body is the answer, whatever the status.** The entry read goes through the shared review decode;
  `getJson` would have thrown and the detail would have been lost, which is the defect this module
  pins.
- **Nothing is invented where the server published nothing.** The transport-failure case asserts the
  state carries the reason and **not** an offending input or a next action it never had.
- **A successful answer prints no state.** The subject case asserts the state element is absent, so the
  refinement is silent when it works.
- **Boundary.** It pins the entry bar's read and display. It does not drive the mounted review surface
  (`ReviewSurface.outcomes.test.tsx`), the expansion pane (`SourceContentRefusal.test.tsx`) or the
  transport contract (`data/reviewTransport.test.ts`), and it makes no browser-level claim — the
  A01/A13 journeys belong to R25 with R24/R17. The live-leaf **change-set counter** the same bar renders
  is a different route, client and owner whose own refusal detail is still swallowed; that debt is
  routed to **R12/R24** and is not this module's subject.

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

Every claim on this card is checkable in the shipped candidate: the module's own defect statement and
provenance, the one measured refusal body, the fixtures and helpers that make the bar's other reads
inert, and the four cases. Every anchor in a row occurs inside the range that row cites.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The header's own provenance and its statement of the defect — the hook's `undefined` subject made a refused read and an empty list indistinguishable — with the digest of the measured body.** | `DocChangeSetBar` | dashboard/src/panels/detail-panel/reviewEntryRefusal.test.tsx:1-25 |
| The real bar under test and the shipped store-seeding helpers. | `DocChangeSetBar`; `enclosure`; `seedProjection` | dashboard/src/panels/detail-panel/reviewEntryRefusal.test.tsx:21-25 |
| The global-fetch restore between cases. | `afterEach` | dashboard/src/panels/detail-panel/reviewEntryRefusal.test.tsx:21-25; dashboard/src/panels/detail-panel/reviewEntryRefusal.test.tsx:108-110 |
| **The one measured refusal body, with its reason, next action and offending input kept verbatim.** | `entryRefusal`; `ENTRY_DETAIL`; `ENTRY_NEXT` | dashboard/src/panels/detail-panel/reviewEntryRefusal.test.tsx:39-52 |
| The body the bar's own change-set counter reads answer with, so the entry cases are not disturbed by them. | `COUNTERS` | dashboard/src/panels/detail-panel/reviewEntryRefusal.test.tsx:54-61 |
| **The one stub, which answers the entries URL only and lets the counter reads through.** | `serveEntry` | dashboard/src/panels/detail-panel/reviewEntryRefusal.test.tsx:63-77 |
| The store seeding that makes the leaf read as live, which is the entry's only gate. | `liveLeaf` | dashboard/src/panels/detail-panel/reviewEntryRefusal.test.tsx:79-93 |
| The mount and the button lookup by its label rather than by index. | `mount`; `intentButton` | dashboard/src/panels/detail-panel/reviewEntryRefusal.test.tsx:95-105 |
| **The conforming half of the packet's example at the entry: the refusal is shown with every published field, and the entry is still offered and opens the task context.** | "shows a never-initialized refusal beside the entry and still offers the entry" | dashboard/src/panels/detail-panel/reviewEntryRefusal.test.tsx:113-136 |
| **Known empty said for a pair that records no subject, without calling it a failure.** | "says known empty when the pair offers no subject, without calling it a failure" | dashboard/src/panels/detail-panel/reviewEntryRefusal.test.tsx:137-155 |
| **A transport failure stated with its reason and with no invented offending input or next action, and the entry still offered.** | "shows a transport failure with its reason, and raises no refusal body it does not have" | dashboard/src/panels/detail-panel/reviewEntryRefusal.test.tsx:156-176 |
| **A successful answer carrying the server's recorded subject into the target and printing no state at all — the stub now mirrors the catalogue wire shape additively (`presence`/totals), with no assertion changed.** | "carries the server's recorded subject into the entry, and prints no state for an answer" | dashboard/src/panels/detail-panel/reviewEntryRefusal.test.tsx:177-209 |
| **The hook and the state renderer these cases drive: the read carried whole, and the entry never gated on it.** | `useReviewCatalogue`; `ReviewEntryState`; `ReviewCatalogueRead` | dashboard/src/panels/detail-panel/changeSetBar.tsx:122-187; dashboard/src/panels/detail-panel/changeSetBar.tsx:189-230; dashboard/src/panels/detail-panel/changeSetBar.tsx:98-120 |
| The bar's own composition, where the working change-set, the reviewer entry and the entry read's state are gated on one liveness. | `DocChangeSetBar`; `LeafEntries`; `leafIsLive` | dashboard/src/panels/detail-panel/changeSetBar.tsx:380-415; dashboard/src/panels/detail-panel/changeSetBar.tsx:301-371; dashboard/src/panels/detail-panel/changeSetBar.tsx:420-432 |
| The client the entry read goes through, which reads the refusal out of the body whatever the status. | `intentReviewEntries` |dashboard/src/data/review.ts:597-603|

## Cross-Repo References

No cross-repository behavior is exercised in this file. Every response is served by a stubbed
same-origin `fetch` and names one repository namespace.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-23T00:45:00+02:00 — 260921-ICR-L10 curator: **removed a verification metadata row for a field that does not exist.** The developer ruled that field out on 2026-09-22 — it has no purpose and had spread by copy-paste — and this pass deleted it here and reworded the sentences that referred to it. The fact it carried (this card describes an uncommitted candidate whose base the verification pair names) is stated in the history entries around it. No content impact: no claim about the source changed.

- 2026-09-22T15:15:00+02:00 — 260921-ICR-L9 curator (candidate `ar/260921-icr-l9`, uncommitted; production line `f141d164265e926be9249acf6ae680ccf9ffae61`, this leaf's base): **the success case's stub mirrors the catalogue wire shape additively (207 → 210 lines; `ICR-R09@v1`).** `selected_item_count: 3` became `presence: "both"` beside the additive `total_subjects`/`invariant_total`/`family_total` in the `carries the server's recorded subject…` stub — **no assertion changed**, because this module pins the entry's read-state contract, and the traversal claims for the complete catalogue live in `changeSetBar.test.tsx`'s new case. The Logic paragraph records the additive stub rule. **Citation accounting:** the rows into this file re-derived against the 210-line candidate (`entryRefusal` `:31-52` → `:39-52`; the refusal case `:112-136` → `:113-136`; the transport case `:156-175` → `:156-176`; the success case `:177-206` → `:177-209`), and the three neighbour rows that cite `changeSetBar.tsx` were re-pointed to the renamed constructs (`useReviewCatalogue`/`ReviewCatalogueRead`/`LiveLeafEntries`, which replaced `useReviewSubject`/`ReviewSubjectRead` in this leaf's candidate) plus `intentReviewEntries` at its moved `review.ts:403-419`. **Stamp accounting:** the verification pair names the leaf's base — the last real commit the reading was taken against — because the additive stub exists only in this leaf's uncommitted candidate; closeout owns the stamp once the code commit exists.
- 2026-09-22T07:05:34+02:00 — 260921-ICR-L16 curator (candidate `ar/260921-icr-l16`, uncommitted; base `8ff80ce08814856c9d6fec5b19093e6540fc6d7f`): **created.** The module is new in this leaf and this is its one-to-one card. It records the entry half of the requirement as four answers rather than four assertions: a never-initialized refusal shown with **every** published field while the entry is still offered and still opens the task context; a subject-less answer stated as known-empty rather than as a failure; a transport failure stated with its reason and with **nothing invented** where the server published nothing; and a successful answer that carries the recorded subject and prints no state at all. It also records the module's own defect statement (the hook's `undefined` subject made a refused read and an empty list indistinguishable) and its provenance (one measured route body with its `sha256-normalized` digest). The card names the routed neighbour explicitly so a later reader does not mistake it for this module's gap: the live-leaf change-set **counter** the same bar renders belongs to a different route, client and owner, and its swallowed refusal detail is routed to R12/R24. **Stamp accounting:** the verification pair names the **merged production line** `8ff80ce08814856c9d6fec5b19093e6540fc6d7f` (2026-09-22T00:48:09+02:00) — the line this candidate now sits on after the leaf's pair sync — while what was actually read is this leaf's **uncommitted** working tree at that base: this leaf's **uncommitted** candidate at that base. Nothing in this leaf is committed, so no commit contains the bytes a stamp would claim to have verified; closeout owns the stamp.
