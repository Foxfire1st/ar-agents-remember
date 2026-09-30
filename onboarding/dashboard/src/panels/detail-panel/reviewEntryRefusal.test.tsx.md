# dashboard/src/panels/detail-panel/reviewEntryRefusal.test.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/detail-panel/reviewEntryRefusal.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T14:22:59+02:00 |
| lastVerifiedCommitHash | `59daf5055eb1ceffba89170be64ac85cabf860f4` |
| lastVerifiedCommitDate | 2026-09-30T15:02:26+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

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

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

Every anchor in a row occurs inside the range that row cites.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The header: what is exercised and the measured pre-L47 defects (line totals, a second committed request, eager catalogue).** | "+3775 −1056"; `DocChangeSetBar` | dashboard/src/panels/detail-panel/reviewEntryRefusal.test.tsx:1-15 |
| The real bar and the shipped store-seeding helpers. | `DocChangeSetBar`; `enclosure`; `seedProjection` | dashboard/src/panels/detail-panel/reviewEntryRefusal.test.tsx:20-22 |
| **The summary route's unavailable answer with the owner's refusal verbatim.** | `UNAVAILABLE`; `ABSENT_DETAIL`; `ABSENT_NEXT` | dashboard/src/panels/detail-panel/reviewEntryRefusal.test.tsx:29-47 |
| A counted or partial body whose parts sum to its totals. | `counted` | dashboard/src/panels/detail-panel/reviewEntryRefusal.test.tsx:49-65 |
| Line totals that must never appear on the Intent review control. | `COUNTERS` | dashboard/src/panels/detail-panel/reviewEntryRefusal.test.tsx:68-73 |
| The one stub and the per-route request counter. | `serve`; `urlsOf` | dashboard/src/panels/detail-panel/reviewEntryRefusal.test.tsx:80-92; dashboard/src/panels/detail-panel/reviewEntryRefusal.test.tsx:94-95 |
| The live-leaf seeding and the mount. | `liveLeaf`; `mount` | dashboard/src/panels/detail-panel/reviewEntryRefusal.test.tsx:97-112; dashboard/src/panels/detail-panel/reviewEntryRefusal.test.tsx:114-120 |
| **One control with intent counts and nothing beside it; the click opens the task context.** | "is one control with the comparison's changed-intent counts and nothing beside it" | dashboard/src/panels/detail-panel/reviewEntryRefusal.test.tsx:127-150 |
| **One summary read, no catalogue read, one committed read.** | "makes one summary read, no catalogue read and one committed change-set read" | dashboard/src/panels/detail-panel/reviewEntryRefusal.test.tsx:152-168 |
| **Missing knowledge stated briefly, never as `+0 −0`, with the refusal in a closed disclosure.** | "states missing knowledge briefly, never as +0 −0, with the owner's refusal in the disclosure" | dashboard/src/panels/detail-panel/reviewEntryRefusal.test.tsx:171-198 |
| An unreadable answer, with no invented refusal. | "says a response the route did not produce is unreadable, and invents no refusal for it" | dashboard/src/panels/detail-panel/reviewEntryRefusal.test.tsx:200-213 |
| Partial counts marked and explained. | "marks partial counts as partial and explains what they leave out" | dashboard/src/panels/detail-panel/reviewEntryRefusal.test.tsx:215-226 |
| **No re-read for unrelated publications; a re-read when this leaf's lifecycle moves.** | "ignores unrelated workspace publications and re-reads when this leaf's lifecycle moves" | dashboard/src/panels/detail-panel/reviewEntryRefusal.test.tsx:229-266 |
| A previous leaf's late answer is dropped. | "never lets an answer for a previous leaf overwrite the leaf on screen now" | dashboard/src/panels/detail-panel/reviewEntryRefusal.test.tsx:268-339 |
| **260921-ICR-L25, register B6: the unrecorded committed range shown briefly, its sentence on demand, never its zero as a total, and kept apart from measured-empty and from a refusal.** | "changeset-state"; "unrecorded"; `UNRECORDED_BODY` | dashboard/src/panels/detail-panel/reviewEntryRefusal.test.tsx:341-387 |
| The control, its summary read and the disclosure these cases drive. | `IntentReviewEntry`; `useIntentReviewSummary`; `EntryStateDetails` | dashboard/src/panels/detail-panel/intentReviewEntry.tsx:131-171; dashboard/src/data/reviewIntentSummary.ts:96-121; dashboard/src/panels/detail-panel/entryState.tsx:13-31 |
| The bar's composition and the leaf-scoped invalidation facts. | `DocChangeSetBar`; `LeafEntries`; `leafFacts` | dashboard/src/panels/detail-panel/changeSetBar.tsx:272-306; dashboard/src/panels/detail-panel/changeSetBar.tsx:315-365; dashboard/src/panels/detail-panel/changeSetBar.tsx:378-392 |

## Cross-Repo References

No cross-repository behavior is exercised in this file. Every response is served by a stubbed
same-origin `fetch` and names one repository namespace.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-30T14:22:59+02:00 — 260928-MIK-L32 curator (staged change set on `ar/260928-mik-l32`, code base `07d6584afba8a9504e4a3cf2e80eac41f68b28a9`): No content impact: this card's own source is unchanged. MIK-R32 moved lines in `dashboard/src/data/reviewIntentSummary.ts`, `dashboard/src/panels/detail-panel/intentReviewEntry.tsx`, so the citation rows into them that moved were re-pointed by the installed fixer (run once; its generated bullets are kept, since no claim was reworded) or by the exact base-to-staged line shift for the rows it declined; every re-pointed row was byte-identical to memory HEAD beforehand and was checked to hold its anchors in the new range. The fixer's normalisation also re-measured passing rows into files this leaf did not change (`dashboard/src/panels/detail-panel/reviewEntryRefusal.test.tsx`); no claim changed. No verification stamp was advanced.
- 2026-09-28T17:01:26+02:00 — 260921-ICR-L47 curator (uncommitted candidate tree `72efa4bbc169b16afe8ef249499edf79cad9940d` over code base `58e22246cc09ef0ee12095e284a111a475081c38`; review R2 pass-with-notes): **body rewritten — the module now pins the compact Intent review entry (`ICR-R24@v3`), and the catalogue-entry account is superseded.** Purpose, Logic, Conventions, Invariants and every reference row were re-derived from the rewritten module (388 lines): the summary-route fixtures, the line-total guard, the one-summary/zero-catalogue/one-committed request economy, the brief states with a closed disclosure, the partial state, leaf-scoped invalidation and the late-answer drop. The L17 section is marked superseded and states what survives. No stamp advanced; closeout owns the real stamp.
- 2026-09-28T12:38:10+02:00 — 260921-ICR-L43 curator (uncommitted candidate tree `990a5c1a3afab15d04881475b2501ed98cddf908` over code base `a0b2c18d2b8d08ac1242a13f65bde900a190df7a`): No content impact: citation ranges into files this leaf changed (`dashboard/src/data/review.ts`, `dashboard/src/panels/review/SourceContent.test.tsx`, `mcp/tests/test-evidence-lanes.toml`, `mcp/tests/evidence-lifecycle.toml`, `mcp/tests/test_knowledge_review_source_content.py`) were re-pointed to where the same anchors now sit, each row checked valid at the base, invalid at the candidate, and valid after the base-to-candidate line mapping; claim wording unchanged. No stamp advanced.
- 2026-09-26T21:08:48+00:00: Generated citation repair: `intentReviewEntries` repointed to dashboard/src/data/review.ts:709-715. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T20:57:44Z — Reconciled current source-owner citations and exact declarations; superseded wording is corrected in the affected reference rows.
- 2026-09-26T19:49:05Z — Repointed shared catalogue/grouping ownership to the extracted source; source-review entry remains available independently of knowledge.
- 2026-09-25T23:45+02:00 — 260921-ICR-L25 curator, round 2 (uncommitted change set on `ar/260921-icr-l25-ar`, code base `d9e7e6e79ce532d16c689435ae95a63aab430f94` plus the working-tree delta, memory base `39adea206651654dbfacf2ee1bb4e2f3763b515b`; round-2 report `report-l25-round2.md` = `9446232d…`): **body update — a new `describe` block with two cases for B6, and the card now carries it.** The module grew 532 → 630 lines. The block drives the bar's **committed** counter read of a live leaf whose landed commit nothing has recorded yet: the first case asserts the control renders `data-review-state="unrecorded"` with the route's own sentence reaching the reader (including both alternatives it names), that the state is **not** `known-empty` and carries no `data-review-code`, and that **no `+0 −0`** is printed beside it; the second serves a `recorded`-and-empty answer and shows the two states cannot be the same screen, because the measured-empty rendering is the one that prints the zero. The stub is the route's real `stateDetail` bytes, and `within(button)` scoping is deliberate — a live leaf's bar carries three of these controls and only this one's read is the unrecorded range. **Citation accounting:** the row into `changeSetBar.tsx` was re-derived (`useReviewCatalogue` `:337-384` → `:371-424`, `ReviewEntryState` `:391-429` → `:425-467`, `LeafEntries` `:483-532`/`:537`/`:557` → `:534-618`, `DocChangeSetBar` `:585-634` → `:619-672`, `leafIsLive` `:639-651` → `:673-688`) and the new row cites `:555-629`. **Stamp accounting:** no verification stamp was advanced — the candidate is uncommitted, so the governed closeout owns the real stamp. No commit was made.
- 2026-09-24T17:20:00+02:00 — 260921-ICR-L32 curator (uncommitted change set on `ar/260921-icr-l32-ar`, code base `71a170796f5380bd3a5b65a5c3323ca4f92b0cc0` plus the working-tree delta; gate `verify-l32-round2.md` = `pass`): **citation pass — the rows this leaf's own line movement displaced were re-anchored from each row's own finding message.** Every flagged range was repointed or widened to the lines that actually carry the anchor at this candidate, using the memory-quality checklist's own per-row message as the ground truth rather than adding a delta to an old number; the repair was applied row-scoped by the cited-range string, so duplicate rows were each corrected. No claim was re-worded to fit a stale pointer, no anchor or range was dropped to silence a finding, and the two legacy mechanical-projection bullets on rows this pass re-read were retired with this entry as their dated disposition, and no new projection bullet was written. No verification stamp was advanced: the candidate is uncommitted, so no commit carries this body, and the governed closeout owns the real stamp.
- 2026-09-23T00:45:00+02:00 — 260921-ICR-L10 curator: **removed a verification metadata row for a field that does not exist.** The developer ruled that field out on 2026-09-22 — it has no purpose and had spread by copy-paste — and this pass deleted it here and reworded the sentences that referred to it. The fact it carried (this card describes an uncommitted candidate whose base the verification pair names) is stated in the history entries around it. No content impact: no claim about the source changed.

- 2026-09-22T15:15:00+02:00 — 260921-ICR-L9 curator (candidate `ar/260921-icr-l9`, uncommitted; production line `f141d164265e926be9249acf6ae680ccf9ffae61`, this leaf's base): **the success case's stub mirrors the catalogue wire shape additively (207 → 210 lines; `ICR-R09@v1`).** `selected_item_count: 3` became `presence: "both"` beside the additive `total_subjects`/`invariant_total`/`family_total` in the `carries the server's recorded subject…` stub — **no assertion changed**, because this module pins the entry's read-state contract, and the traversal claims for the complete catalogue live in `changeSetBar.test.tsx`'s new case. The Logic paragraph records the additive stub rule. **Citation accounting:** the rows into this file re-derived against the 210-line candidate (`entryRefusal` `:31-52` → `:39-52`; the refusal case `:112-136` → `:113-136`; the transport case `:156-175` → `:156-176`; the success case `:177-206` → `:177-209`), and the three neighbour rows that cite `changeSetBar.tsx` were re-pointed to the renamed constructs (`useReviewCatalogue`/`ReviewCatalogueRead`/`LiveLeafEntries`, which replaced `useReviewSubject`/`ReviewSubjectRead` in this leaf's candidate) plus `intentReviewEntries` at its moved `review.ts:403-419`. **Stamp accounting:** the verification pair names the leaf's base — the last real commit the reading was taken against — because the additive stub exists only in this leaf's uncommitted candidate; closeout owns the stamp once the code commit exists.
- 2026-09-22T07:05:34+02:00 — 260921-ICR-L16 curator (candidate `ar/260921-icr-l16`, uncommitted; base `8ff80ce08814856c9d6fec5b19093e6540fc6d7f`): **created.** The module is new in this leaf and this is its one-to-one card. It records the entry half of the requirement as four answers rather than four assertions: a never-initialized refusal shown with **every** published field while the entry is still offered and still opens the task context; a subject-less answer stated as known-empty rather than as a failure; a transport failure stated with its reason and with **nothing invented** where the server published nothing; and a successful answer that carries the recorded subject and prints no state at all. It also records the module's own defect statement (the hook's `undefined` subject made a refused read and an empty list indistinguishable) and its provenance (one measured route body with its `sha256-normalized` digest). The card names the routed neighbour explicitly so a later reader does not mistake it for this module's gap: the live-leaf change-set **counter** the same bar renders belongs to a different route, client and owner, and its swallowed refusal detail is routed to R12/R24. **Stamp accounting:** the verification pair names the **merged production line** `8ff80ce08814856c9d6fec5b19093e6540fc6d7f` (2026-09-22T00:48:09+02:00) — the line this candidate now sits on after the leaf's pair sync — while what was actually read is this leaf's **uncommitted** working tree at that base: this leaf's **uncommitted** candidate at that base. Nothing in this leaf is committed, so no commit contains the bytes a stamp would claim to have verified; closeout owns the stamp.

## 260921-ICR-L17 The Entry Notices A New Generation, And No Superseded Read Wins (superseded by 260921-ICR-L47)

`260921-ICR-L17` (`ICR-R17@v1`) added cases for the catalogue-based entry: re-reading the catalogue
when the analytics projection was republished, the `review-catalogue-refresh` control and its stale
marker, and a previous leaf's answer that must not win. **`260921-ICR-L47` removed that entry design**
(no catalogue at the entry, no entry refresh control, no analytics subscription), so those cases were
replaced. What L17 pinned survives in its current form: a previous leaf's late answer is still dropped,
and invalidation is now leaf-scoped (an unrelated publication re-reads nothing), as the Logic section
above records. The cockpit-level re-validation points ruled for L47-R1-F2 are pinned in
`cockpit/Cockpit.intentEntry.test.tsx`.

## Update History
- 2026-09-23T06:50:00+02:00 — 260921-ICR-L17 curator (candidate `ar/260921-icr-l17`, uncommitted; production line at this leaf's base `c422dc00273d4ae7a5d8c9c8db97365b8c85d640`, confirmed from the enclosure contract): **the entry notices a new candidate generation and no superseded read wins (`ICR-R17@v1`).** Two new `describe` blocks drive the real bar over the real client through the store's own `applyDelta("analytics", …)` channel: the self-invalidation case, the explicit refresh control, the previous-leaf race, and the pre-click marker asserted in a settled DOM with the re-read held open. **Stamp accounting:** the verification pair names this leaf's base — the last real commit the reading was taken against — because the new cases exist only in this leaf's uncommitted working tree; closeout owns the stamp once the code commit exists.
