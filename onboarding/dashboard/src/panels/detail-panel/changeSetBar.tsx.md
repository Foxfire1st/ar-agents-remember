# dashboard/src/panels/detail-panel/changeSetBar.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/detail-panel/changeSetBar.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T14:18:54+02:00 |
| lastVerifiedCommitHash | `59daf5055eb1ceffba89170be64ac85cabf860f4` |
| lastVerifiedCommitDate | 2026-09-30T15:02:26+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[panels/ overview](../overview.md)

## Purpose

The change-set bar of the DetailPanel task-document reader, extracted from `DetailPanel.tsx` by the
260731-EFA-L8 split. `ChangeSetButton` is the per-document change-set control, `DocChangeSetBar` the
compact bar rendered above the reader content, `LeafEntries` a leaf's own entries, and `leafIsLive` the
one liveness predicate. A master gets the **series** net button; a leaf gets **committed** (always),
**working** (only while its enclosure is live) and the **Intent review** (always — the live candidate
while the enclosure is live, the leaf's recorded comparison once it is closed, `ICR-R12`).

**Since `260921-ICR-L47` (`ICR-R24@v3`) the Intent review is one compact control that is not a
change-set button.** It is the separate [`IntentReviewEntry`](intentReviewEntry.tsx.md), whose
`+N −N` are the comparison's changed-intent counts from the summary route. The bar no longer reads the
subject catalogue, offers no subject picker, has no entry refresh control, prints no entry-state
paragraph, and no longer subscribes to the global analytics document. Those constructs
(`useReviewCatalogue` at the entry, `ReviewCataloguePicker`, `presenceMarker`, `ReviewEntryState`,
`ReviewCatalogueRefresh`, `reviewDependencyFacts`) are **gone**: the catalogue is now read by the
reviewer when it opens (`panels/review/ReviewNavigation.tsx`). The change-set controls' states became a
brief word with the explanation in a closed disclosure ([`entryState.tsx`](entryState.tsx.md), ICR-R16).

## Code Commentary

### Logic

**`ChangeSetButton` performs its own change-set read and threads the published generation.** Its
effect calls `leafChangeset`/`masterChangeset`/`taskChangeset` and stores the counters; for a master net
it also stores the response's `generation` as `MasterNetPins` and opens the viewer with
`{ ...target, generation }`, so the view and each file expansion read the listed generation rather than
re-resolving the live tip (L13). The master read passes `includeLeaves: true`, and `LeafAttribution`
renders `<N> leaf/leaves< · C committed>< · W working>` beside the total — or nothing when the answer
carried no breakdown (L33, R33.2).

**States of the counter read (L25/B6, L32/D01, compacted by L47).** `ChangeSetReadState` renders one
brief word inside the button, with `data-testid="changeset-state"`, `data-review-state` and, for a
failure, `data-review-code`:

- `loading` — `…`; nothing measured, nothing claimed;
- `unrecorded` — the route answered that the mode's endpoints are not recorded yet (a committed view of
  a live leaf); the total is withheld (`changesetTotal` returns `null`) because a zero of nothing is not
  a measurement;
- `known-empty` — `empty`, a measured zero;
- an answer with changed files — no state; the counters are the answer;
- a refusal, an unreadable answer or no answer — `briefProblem`'s word under the shared
  `reviewFailureToken`.

`ChangeSetStateDetails` puts the explanation beside the button in `EntryStateDetails` (a `<details>`
disclosure, closed by default, outside the button): for a failure, `problemSentence` (code, the owner's
reason, offending input, next action); for an unrecorded range, the route's own sentence. The rejection
handler files `reviewProblemFromCause(cause)` so a refusal is never swallowed.

**`LeafEntries` composes a leaf's own entries.** The `working` button only while live, then
`IntentReviewEntry` with the leaf's `repo`/`master`/`leaf`, `live` and `facts`. The Intent review is
deliberately **not** a `ChangeSetButton`: that control reads the committed change set (it caused a
second identical committed request) and would show its line totals as the review's.

**`DocChangeSetBar` branches on `kind` and builds the summary's invalidation facts.** `live` comes
from `leafIsLive`. `facts` is `leafFacts(...)` — `JSON.stringify` of this leaf's liveness and its
enclosure's `closeoutStatus`, `integrationStatus`, `cleanup` and `codeWorktreeExists` (found by
`leafEnclosure`) — plus `#<generation>` from `useIntentEntryGeneration()`. The generation moves when
the task detail is shown again or the reviewer refreshes (`data/intentEntryRevalidation.tsx`, the
Architect's 16:27:28 ruling on L47-R1-F2). Only the summary is keyed on `facts`; the committed and
working reads are not.

### Conventions

Small presentational components; the bar itself performs no fetch, each `ChangeSetButton` owns its
counter read and `IntentReviewEntry` owns its summary read. Failures are classified through the review
client's shared `ReviewFailure` vocabulary (`../../data/review`). Styles come from `./styles`
(`changeSetBtn`, `changeSetCounts`, and the `entryState*` classes used by the disclosure). Every
rendered state carries a `data-*` attribute so tests read state from the DOM.

### Invariants And Boundaries

- **The Intent review entry is always offered for a leaf, and no read gates it.** `live` selects which
  record it opens; the summary's answer is a label on the control, never a gate.
- **The Intent review's numbers are never change-set line totals.**
- **The entry reads no subject catalogue.** Choosing a subject and re-reading the comparison belong to
  the reviewer.
- **Invalidation is leaf-scoped.** An unrelated workspace publication does not re-read the summary; this
  leaf's own lifecycle facts, a re-show of the task detail and the reviewer's refresh do. A live push of
  a first knowledge ingest while the same panel stays open is **not** delivered (ruling 16:27:28 records
  it as a possible later enhancement).
- **`leafIsLive` is the one liveness definition** for the working button and the review's record.
- **The browser names no candidate and no dataset.** Targets carry repo/master/leaf only.
- **Brief, never swallowed (ICR-R16).** A control shows one word; the owner's code, reason, offending
  input and next action are one click away, and nothing is invented where the owner published nothing.
- **Boundary.** What a refusal code means belongs to `data/reviewTransport.ts`; what the counts mean
  belongs to the summary owner (`application/review_intent_summary.py`); whether the review can be
  opened belongs to the review surface.

### Todos

None open on this file. The earlier CLOSED item (the counter read no longer swallows its refusal
detail, L25/L32) remains closed; its rendered form is now the brief state plus disclosure.

## Docs References

The curator checked `system/sources.md`; no Domain Documentation source is configured for this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant domain documentation was found. | — | — |

## Repo-Internal References

Every anchor in a row occurs inside the range that row cites.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own statement of which entries a master and a leaf get, and that the Intent review is its own component. | "intentReviewEntry.tsx" | dashboard/src/panels/detail-panel/changeSetBar.tsx:1-7 |
| The net's leaf attribution, rendered only when the answer carried a breakdown. | `leafAttribution`; `LeafAttribution` | dashboard/src/panels/detail-panel/changeSetBar.tsx:30-38; dashboard/src/panels/detail-panel/changeSetBar.tsx:40-48 |
| The total withheld for an unrecorded range. | `changesetTotal` | dashboard/src/panels/detail-panel/changeSetBar.tsx:54-64 |
| The change-set control: its own counter read, the generation threaded into the viewer target, the unrecorded state, the refusal filed rather than swallowed, and the disclosure beside the button. | `ChangeSetButton`; `setUnrecorded`; `setProblem`; "<ChangeSetStateDetails" | dashboard/src/panels/detail-panel/changeSetBar.tsx:66-166 |
| The counter read's brief states. | `ChangeSetReadState`; `briefProblem`; "unrecorded"; "known-empty" | dashboard/src/panels/detail-panel/changeSetBar.tsx:185-233 |
| The explanation in a closed disclosure: the refusal sentence or the unrecorded sentence. | `ChangeSetStateDetails`; `problemSentence` | dashboard/src/panels/detail-panel/changeSetBar.tsx:236-259 |
| **A leaf's entries: working while live, then the Intent review control (not a change-set button).** | `LeafEntries`; `IntentReviewEntry` | dashboard/src/panels/detail-panel/changeSetBar.tsx:272-306 |
| **The bar: the master/leaf branch, the one liveness predicate, and the leaf-scoped facts plus re-validation generation the summary is keyed on.** | `DocChangeSetBar`; `useIntentEntryGeneration`; `leafFacts` | dashboard/src/panels/detail-panel/changeSetBar.tsx:315-365; dashboard/src/panels/detail-panel/changeSetBar.tsx:378-392 |
| This leaf's lifecycle facts as one comparable value. | `leafEnclosure`; `leafFacts`; `closeoutStatus` | dashboard/src/panels/detail-panel/changeSetBar.tsx:367-375; dashboard/src/panels/detail-panel/changeSetBar.tsx:378-392 |
| **The one liveness predicate both live-dependent entries read.** | `leafIsLive` | dashboard/src/panels/detail-panel/changeSetBar.tsx:397-409 |
| The Intent review control and its summary read. | `IntentReviewEntry`; `useIntentReviewSummary` | dashboard/src/panels/detail-panel/intentReviewEntry.tsx:131-171 |
| The shared brief-state and disclosure helpers. | `EntryStateDetails`; `briefProblem`; `problemSentence` | dashboard/src/panels/detail-panel/entryState.tsx:13-31; dashboard/src/panels/detail-panel/entryState.tsx:35-48; dashboard/src/panels/detail-panel/entryState.tsx:52-60 |
| The re-validation generation the facts carry. | `useIntentEntryGeneration` | dashboard/src/data/intentEntryRevalidation.tsx:57-58 |
| The change-set client the counter read belongs to. | `taskChangeset`; `TaskChangeset` | dashboard/src/data/changeset.ts:41-48; dashboard/src/data/changeset.ts:167-168 |
| The compact entry's cases: one control, request economy, brief states, leaf-scoped invalidation. | "is one control with the comparison's changed-intent counts and nothing beside it"; "makes one summary read, no catalogue read and one committed change-set read" | dashboard/src/panels/detail-panel/reviewEntryRefusal.test.tsx:127-150; dashboard/src/panels/detail-panel/reviewEntryRefusal.test.tsx:152-168 |
| The closed leaf's recorded entry and the failed-summary case. | "offers the Intent review for a closed leaf, bound to its recorded comparison"; "keeps the entry when the summary read itself fails" | dashboard/src/panels/detail-panel/changeSetBar.test.tsx:75-99; dashboard/src/panels/detail-panel/changeSetBar.test.tsx:413-444 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History
- 2026-09-30T14:18:54+02:00 — 260928-MIK-L32 curator (staged change set on `ar/260928-mik-l32`, code base `07d6584afba8a9504e4a3cf2e80eac41f68b28a9`): No content impact: this card's own source is unchanged. MIK-R32 moved lines in `dashboard/src/panels/detail-panel/intentReviewEntry.tsx`, so the citation rows into them that moved were re-pointed by the installed fixer (run once; its generated bullets are kept, since no claim was reworded) or by the exact base-to-staged line shift for the rows it declined; every re-pointed row was byte-identical to memory HEAD beforehand and was checked to hold its anchors in the new range. The fixer's normalisation also re-measured passing rows into files this leaf did not change (`dashboard/src/panels/detail-panel/changeSetBar.tsx`, `dashboard/src/panels/detail-panel/entryState.tsx`); no claim changed. No verification stamp was advanced.
- 2026-09-28T17:30:17+02:00 — 260921-ICR-L47 curator (uncommitted candidate tree `72efa4bbc169b16afe8ef249499edf79cad9940d` over code base `58e22246cc09ef0ee12095e284a111a475081c38`): the change-set control row was re-anchored after the full memory-quality run reopened it: its disclosure is a use of `ChangeSetStateDetails` inside `ChangeSetButton`, now named as the literal "<ChangeSetStateDetails"; the component's declaration keeps its own row. Claim wording unchanged.
- 2026-09-28T17:02:23+02:00 — 260921-ICR-L47 curator (uncommitted candidate tree `72efa4bbc169b16afe8ef249499edf79cad9940d` over code base `58e22246cc09ef0ee12095e284a111a475081c38`; review R2 pass-with-notes): **body rewritten — the Intent review is one compact control with changed-intent counts, and the catalogue-at-the-entry design is superseded (`ICR-R24@v3`; 555 → 412 lines).** Purpose, Logic, Conventions, Invariants and Todos now describe the current bar: `IntentReviewEntry` in `LeafEntries` instead of a `ChangeSetButton`; no catalogue read, picker, entry refresh or analytics subscription; brief change-set states with the explanation in `ChangeSetStateDetails`; leaf-scoped `leafFacts` plus the re-validation generation as the summary's invalidation (ruling 16:27:28 on L47-R1-F2). The removed constructs are named as gone. The L12 section's catalogue bullet is annotated as superseded, and the L17 section is marked superseded with what replaces it. Every reference row was re-derived from the candidate. No stamp advanced; closeout owns the real stamp.
- 2026-09-28T12:38:10+02:00 — 260921-ICR-L43 curator (uncommitted candidate tree `990a5c1a3afab15d04881475b2501ed98cddf908` over code base `a0b2c18d2b8d08ac1242a13f65bde900a190df7a`): No content impact: citation ranges into files this leaf changed (`dashboard/src/data/review.ts`, `dashboard/src/panels/review/SourceContent.test.tsx`, `mcp/tests/test-evidence-lanes.toml`, `mcp/tests/evidence-lifecycle.toml`, `mcp/tests/test_knowledge_review_source_content.py`) were re-pointed to where the same anchors now sit, each row checked valid at the base, invalid at the candidate, and valid after the base-to-candidate line mapping; claim wording unchanged. No stamp advanced.
- 2026-09-26T21:08:38+00:00: Generated citation repair: `presenceMarker` repointed to dashboard/src/panels/detail-panel/changeSetBar.tsx:355-359. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T21:08:38+00:00: Generated citation repair: `LeafEntries` repointed to dashboard/src/panels/detail-panel/changeSetBar.tsx:421-497. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T21:08:38+00:00: Generated citation repair: `leafIsLive` repointed to dashboard/src/panels/detail-panel/changeSetBar.tsx:560-572. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T20:57:44Z — Reconciled current source-owner citations and exact declarations; superseded wording is corrected in the affected reference rows.
- 2026-09-26T19:49:05Z — Reconciled the changed ownership and current behavior with the source.
- 2026-09-25T22:19:46+00:00: Generated citation repair: `presenceMarker` repointed to dashboard/src/panels/detail-panel/changeSetBar.tsx:481-485. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T23:45+02:00 — 260921-ICR-L25 curator, round 2 (uncommitted change set on `ar/260921-icr-l25-ar`, code base `d9e7e6e79ce532d16c689435ae95a63aab430f94` plus the working-tree delta, memory base `39adea206651654dbfacf2ee1bb4e2f3763b515b`; round-2 report `report-l25-round2.md` = `9446232d…`): **body update — the bar carries the leaf view's `unrecorded` state, and the routed debt this card recorded is closed rather than still open.** The Logic paragraph now records the new `unrecorded` state (`data-review-state="unrecorded"`, distinct from `known-empty`), that the route answers that state in the body instead of refusing it with a `404` (register B6), and that the control **withholds its `+0 −0` total** because a zero of nothing is not a measurement. The `### Todos` section's routed item — "the live-leaf `committed`/`working` change-set counter still swallows its own refusal detail", with the rejection handler quoted as `() => live && setCounters(null)` — is corrected to **CLOSED**: the handler is `setProblem(reviewProblemFromCause(cause))`, the suite asserts the rendered refusal, and round 2 measured the rendered half for the unrecorded answer on the mounted product (register D01); what stays unmeasured is a rendered *refusal* on a live page, which is Class 3 and named as a gap. **Citation accounting:** every row whose range this file's own insertion displaced was re-derived from each construct's declaration at this tip — `ChangeSetButton` `:47-181`, `ChangeSetReadState` `:182-237`, `ReviewCatalogueRead` `:238-257`, `ReviewEntryState` `:425-467`, `presenceMarker` `:468-477`, `ReviewCataloguePicker` `:478-533`, `LeafEntries` `:534-618`, `DocChangeSetBar` `:619-672`, `leafIsLive` `:673-688` — and the cross-file rows were re-derived too (`getJson` `changeset.ts:135` → `:144`, `TaskChangeset` `:33` → `:41-48`, `masterChangeset(` `:52` → `:93`, `includeLeaves` `:85` → `:93`). **Stamp accounting:** no verification stamp was advanced — the candidate is uncommitted, so the governed closeout owns the real stamp. No commit was made.
- 2026-09-24T23:30:00+02:00 — 260921-ICR-L33 curator (candidate `ar/260921-icr-l33-ar`, uncommitted; code base `86639933d61528387ce106dbd4d7a334bd468671` plus the working-tree delta; adversarial round 2 `verify-l33.md` = `pass`): **body update — the bar asks for the net's per-leaf breakdown and prints its attribution (R33.2).** The Logic paragraph now records the `includeLeaves: true` request, the `leaves` state and the `leafAttribution` phrase beside the total, with the absent-answer rule. **Citation accounting:** the rows this leaf's line movement displaced were re-derived against the candidate with the gate's own resolver. **Stamp accounting:** no verification stamp was advanced — the candidate is uncommitted and the governed closeout owns the real stamp.
- 2026-09-24T17:20:00+02:00 — 260921-ICR-L32 curator (uncommitted change set on `ar/260921-icr-l32-ar`, code base `71a170796f5380bd3a5b65a5c3323ca4f92b0cc0` plus the working-tree delta; gate `verify-l32-round2.md` = `pass`): **body update — the control renders the refusal it receives (D01).** `ChangeSetButton` shows the refusal's own code and reason beside a state marker while still opening what it names, and the case that pins it drives the click and asserts the rendered reason. **citation pass — the rows this leaf's own line movement displaced were re-anchored from each row's own finding message.** Every flagged range was repointed or widened to the lines that actually carry the anchor at this candidate, using the memory-quality checklist's own per-row message as the ground truth rather than adding a delta to an old number; the repair was applied row-scoped by the cited-range string, so duplicate rows were each corrected. No claim was re-worded to fit a stale pointer, no anchor or range was dropped to silence a finding, and the two legacy mechanical-projection bullets on rows this pass re-read were retired with this entry as their dated disposition, and no new projection bullet was written. No verification stamp was advanced: the candidate is uncommitted, so no commit carries this body, and the governed closeout owns the real stamp.
- 2026-09-23T00:45:00+02:00 — 260921-ICR-L10 curator: **removed a verification metadata row for a field that does not exist.** The developer ruled that field out on 2026-09-22 — it has no purpose and had spread by copy-paste — and this pass deleted it here and reworded the sentences that referred to it. The fact it carried (this card describes an uncommitted candidate whose base the verification pair names) is stated in the history entries around it. No content impact: no claim about the source changed.

- 2026-09-22T15:08:00+02:00 — 260921-ICR-L9 curator (candidate `ar/260921-icr-l9`, uncommitted; production line `f141d164265e926be9249acf6ae680ccf9ffae61`, this leaf's base): **the bar offers every catalogue row, not just the first (303 → 415 lines; `ICR-R09@v1`).** The entry read's hook is now `useReviewCatalogue` returning `ReviewCatalogueRead` — the whole list with `totalSubjects`/`invariantTotal`/`familyTotal`, the known-empty fact, or the problem — and the new `ReviewCataloguePicker` renders every row with per-row `presence` marks from `presenceMarker` (`retired · before-only` / `new · after-only`), the selection driving the Intent review button's target (first row by default, the reader's pick afterwards, a stale pick falling back) while the task-context target stays always reachable. The Purpose's "Three constructs carry that" sentence is replaced: `ReviewSubjectRead` and `useReviewSubject` **no longer exist** — their `entries?.[0]` selection was exactly the first-row-only mechanism the packet's non-conforming example names — and the live-leaf fragment moved into the extracted `LiveLeafEntries` (an eslint-complexity extraction, not a behavior change). The entry's gating rule is unchanged and restated: liveness alone, task context always reachable, read never gates. **Citation accounting:** every row into this file re-derived against the 415-line candidate — `ChangeSetButton` `:29-96`, `ReviewCatalogueRead` `:98-120`, `useReviewCatalogue` `:122-187`, `ReviewEntryState` `:189-230`, `presenceMarker` `:232-240`, `ReviewCataloguePicker` `:242-289`, `LiveLeafEntries` `:291-358`, `DocChangeSetBar` `:360-398`, `leafIsLive` `:400-415` — with four new rows for the marker, the picker, the extraction and the target construction, and the two `review.ts` rows re-pointed to `intentReviewEntries` `:403-419`; the refusal-case row's last range follows the stub's additive totals fields (`:177-209`). **Stamp accounting:** the verification pair names the leaf's base — the last real commit the reading was taken against — because the picker, the totals and the extraction exist only in this leaf's uncommitted candidate; closeout owns the stamp once the code commit exists.
- 2026-09-22T11:00:00+02:00 — 260921-ICR-L13 curator (candidate `ar/260921-icr-l13`, uncommitted; base `6695a2a12961ef340c8864d56f0a1ce12b51b3c5`): **the button threads the published generation into the viewer target (280 → 303 lines).** `ChangeSetButton` stores the master read's `generation` as `MasterNetPins` and opens `{ ...target, generation }`, so the view and its expansions read the listed generation; the rejection handler and the routed R12/R24 debt are unchanged. **Citation accounting:** every row into this file was re-derived against the moved candidate (the generation state + handlers moved everything below `:44`: `ChangeSetButton` `:28-70` → `:29-93`, `ReviewSubjectRead` `:72-83` → `:97-106`, `useReviewSubject` `:85-135` → `:116-158`, `ReviewEntryState` `:137-178` → `:163-201`, `DocChangeSetBar` `:180-260` → `:208-283`, `leafIsLive` `:262-277` → `:288-301`), and the two `changeset.ts` rows followed the client move (`taskChangeset` `:56-57` → `:78-79`). The entry-read, review-client and refusal-case rows are kept as recorded (those files are untouched by this leaf). Verification metadata is **not** advanced: the candidate is uncommitted and closeout owns the stamp.
- 2026-09-22T07:05:34+02:00 — 260921-ICR-L16 curator (candidate `ar/260921-icr-l16`, uncommitted; base `8ff80ce08814856c9d6fec5b19093e6540fc6d7f`): **the entry read's answer is now carried and printed, and this card's earlier account of "no subject means no button" is corrected rather than carried.** `useReviewSubject` returns a `ReviewSubjectRead` — `loading`, the first `entry`, a known-empty `empty` flag, or a `problem` — instead of `ReviewEntry | undefined`, so a refused read and an empty list are no longer indistinguishable and neither is discarded; the read classifies through the review client's shared decode (`reviewProblemFromRefusal`/`reviewProblemFromCause`/`unreadableAnswer`), because the route publishes its refusal in the body of a non-2xx response and `getJson` would have thrown and lost it. The new `ReviewEntryState` prints that answer beside the entry — refused with the owner's code, reason, offending input and next action; known-empty for a pair that records no subject; `network` for a transport failure with nothing invented — and returns `null` for a successful read. The reviewer entry remains gated on **liveness alone**, which is unchanged from R02, and that is why the card's earlier sentence that "a refusal, an empty list, a rejected promise … leave the subject `undefined`, so no subject means no button" has been **removed**: it described the R02 hook, not this one. Line count 186 → 280. It also records, as **routed rather than fixed**, the live-leaf counter's swallowed refusal detail (`ChangeSetButton`'s `() => live && setCounters(null)` over `data/changeset.ts` → `getJson` → `/api/changeset/task`) to R12/R24 — a different route, client and owner. Every row of the reference table was re-derived against this candidate. **Stamp accounting:** the verification pair names the **merged production line** `8ff80ce08814856c9d6fec5b19093e6540fc6d7f` (2026-09-22T00:48:09+02:00) — the line this candidate now sits on after the leaf's pair sync; what was actually read is this leaf's uncommitted working tree, and nothing in this leaf is committed, so closeout owns the stamp.
- 2026-09-21T14:59:00+02:00 — 260921-ICR-L2 curator (uncommitted change set on `ar/260921-icr-l2`, base `702714fc05363cb28eacaf101ba8384475a6aa56`): **the entry stopped depending on the subject.** The button is now gated on liveness alone; the server's recorded subject travels with the target as a refinement, and its absence (an empty list or an unreadable refusal) produces the task-context target `review: {}` instead of no button at all. That is the non-conforming example the packet names — "an empty subject list makes the source review disappear" — closed at the entry. The hook, its no-fetch-for-a-dead-leaf rule and its "a refusal is a normal answer" idiom are unchanged; what changed is what an empty answer *means*, and both comments now say it. One citation row was re-derived against this candidate. **Stamp accounting:** the verification rows still name the last real commit whose bytes this card was verified against, because nothing in this leaf is committed; claims whose evidence this leaf's change moved were re-read against the candidate and are stamp-class leftovers that only closeout can stamp.

- 2026-09-20T13:43:00+02:00 — 260915-KS-L45 curator (uncommitted change set on `ar/260915-ks-l45-ar`, base `fb719f89`): **the reviewer entry is reachable now, and this card's account of *why* it was not is the correction that matters.** The `selectorKind`/`selectorId` props are gone. A live leaf's subject is read from the server by the new `useReviewSubject` hook, which calls `intentReviewEntries(repo, master, leaf)` and keeps `result.entries?.[0]`; the gate is now `live && subject`, and the liveness half was extracted into `leafIsLive` so both gated entries read one predicate. The gate is not weakened: a refusal, an empty list, a rejected promise or a non-live leaf all leave `subject` undefined and **no subject means no button**. The card records why that matters — the prop was the unreachable part, because `taskReader.tsx` and the master header pass no selector, so `live && selectorId` could never hold on any real navigation — and records the invariant the hook's own comment states: the id is a recorded identity inside the candidate the server resolved, so the hook chooses no candidate and invents no id. The revision of the previous paragraph is retained in place below in substance: the entry is still added beside the working/committed actions and never in their place, its target still carries the subject's recorded identity rather than a filesystem path, and the reviewer entry still reports no counters. No verification stamp was advanced, because no commit contains this body.
- 2026-09-18T18:10+02:00 — 260915-KS-L22 curator (uncommitted change set on `ar/260915-ks-l22`, base `2dcacb27`): **added the reviewer entry beside the change-set actions.** `DocChangeSetBar` gained `selectorKind = "invariant"` / `selectorId` props and a third `ChangeSetButton` labelled *Intent review*, rendered only when the enclosure is live and a `selectorId` is supplied — the same liveness the working action is gated on, and never in the working or committed action's place. Its target carries `review: { selectorKind, selectorId }`, the reviewed subject's recorded identity rather than a filesystem path, because the browser does not choose the candidate. The new paragraph above states that, and states the boundary the bar keeps: it still fetches nothing itself, and the new entry's counter effect reads only the leaf or master request, so no counters are reported for a review. No reference row was touched; ranges into this source belong to the citation-reprojection engine. The metadata block above names this leaf's uncommitted candidate as what was read, and the two verification stamps are left exactly as the last real verification set them. The body was changed substantively and this entry is the history record, not a metadata-only refresh.
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the change-set bar extracted from `DetailPanel.tsx`. Verification pinned to the leaf base until closeout stamps the code commit.
## 260921-ICR-L12 Liveness Selects Which Record The Review Is Addressed To, Not Whether It Exists

`260921-ICR-L12` (`ICR-R12@v1`) changes what this bar's liveness means, and that is the whole of
its change:

- **the Intent review entry is offered for the leaf, always.** It used to be gated on the enclosure
  being live, which is the intake defect's other face: a closed leaf's worktree is gone and there is no
  way to open the review that the packet exists to make openable. `live` now selects **which record**
  the entry is addressed to — the live candidate while the enclosure is live, and the leaf's own
  recorded comparison once it is closed (`review: { …, historical: true }`, labelled "Intent review
  (recorded)") — and it is not a gate.
- **the WORKING change-set stays live-gated.** "What is not committed yet" genuinely does not exist
  once the enclosure is closed, so that button is still offered only while the leaf is live; the
  committed action and the review entry are the two that survive.
- **the catalogue read is no longer gated on liveness either**, because a closed leaf's catalogue is
  what its record holds. It remains a **refinement and never a gate**: the read's own state is printed
  beside the entry, and the entry stays openable whatever the read answered — a refusal there is a
  stated reason, not a missing control. *(Superseded by `260921-ICR-L47`: the entry reads no catalogue
  at all; the changed-intent summary is read instead, for live and closed leaves alike, and its answer
  is likewise a label and never a gate.)*
- **`LiveLeafEntries` became `LeafEntries`**, since it is no longer only the live leaf's set, and the
  `live` prop it now takes is threaded from the bar's one `leafIsLive` predicate so the working button
  and the review's record cannot come to disagree about what "live" means.

The change-set target carries no filesystem path in any branch: the browser still chooses no candidate,
and the historical entry names the record the server resolves from canonical task context.

## Update History
- 2026-09-23T04:30:48+02:00 — 260921-ICR-L12 curator (candidate `ar/260921-icr-l12`, uncommitted; production line at this leaf's base `870701b43039cd205a8c98e418382729510c3de3`, confirmed from the enclosure contract): **liveness selects which record the review is addressed to, not whether it exists (ICR-R12@v1).**
The Intent review entry is offered for every leaf — live, or bound to the leaf's recorded comparison
once the enclosure is closed — while the working change-set stays live-gated; the catalogue read is no
longer live-gated either and remains a refinement rather than a gate; `LiveLeafEntries` became
`LeafEntries` with one `live` predicate behind both decisions. **Citation accounting:** every row into
this module was re-derived against the candidate, including the rename. **Stamp accounting:** no
verification stamp was advanced — the candidate is uncommitted and the governed closeout owns the real
stamp.

## 260921-ICR-L17 The Entry Read Is Invalidated By The Workspace, Not Repeated On A Timer (superseded by 260921-ICR-L47)

`260921-ICR-L17` (`ICR-R17@v1`) made the entry's **catalogue** read re-ask when the serialized global
`analytics` projection moved (`reviewDependencyFacts`), and added an always-offered
`ReviewCatalogueRefresh` control with a stale marker. **`260921-ICR-L47` removed both**, together with
the entry's catalogue read. The measured problem was that the global projection moves on every
workspace publication, so the entry re-read on unrelated tasks, and the refresh control was a second
place to re-read the comparison.

What replaces it: the entry's changed-intent summary is keyed on **this leaf's own lifecycle facts**
(`leafFacts`) plus a local re-validation generation that moves when the task detail is shown again,
when the reviewer is left back to the entry and when the reviewer's own refresh runs (Architect ruling
2026-09-28T16:27:28+02:00, no event system). The newest-read-wins guard survives in
`useIntentReviewSummary`, so a previous leaf's late answer is dropped. The reviewer keeps its own
"Refresh subjects" control.

## Update History
- 2026-09-24T00:43:00+02:00 — 260921-ICR-L24 curator (memory worktree only; no code changed; no commits; leaf base `5f14fc6790cafc3ad2ae612c2e67f176392dc1fe` plus the working-tree delta): **two enforced citation rows re-cited to the constructs they name, wording unchanged.** The public-entry row's `review.ts` re-export block shifted down one line in this leaf's `data/review.ts`, so `unreadableAnswer` is now cited at its own re-export line (`30-30`), and `intentReviewEntries` moved out of the re-export block entirely to its own declaration extent (`699-705`), which is the range the row now carries. The two contributing ranges (`reviewProblemFromRefusal` `29-29`, `reviewProblemFromCause` `28-28`) are kept verbatim and no claim was reworded or dropped. **Stamp accounting:** no verification stamp was advanced — the candidate is uncommitted (base `5f14fc6790cafc3ad2ae612c2e67f176392dc1fe` plus the working-tree delta) and governed closeout owns the real stamp.
- 2026-09-23T06:50:00+02:00 — 260921-ICR-L17 curator (candidate `ar/260921-icr-l17`, uncommitted; production line at this leaf's base `c422dc00273d4ae7a5d8c9c8db97365b8c85d640`, confirmed from the enclosure contract): **the entry read is invalidated by the workspace projection and refreshed by the reader (`ICR-R17@v1`).** `DocChangeSetBar` subscribes to `analytics` and threads `reviewDependencyFacts` into `useReviewCatalogue`, so a publication after the panel opened is visible without closing it and an idle workspace performs no read at all; the new `ReviewCatalogueRefresh` is always offered and its mark is derived from the facts recorded with the last answer rather than from the live value (not gated on `loading`, which is what made it invisible); `catalogueAnswer` is the one pure mapping from an answer to the read state, and the newest-read-wins guard is kept so a previous leaf's answer cannot win. **Citation accounting:** the rows into this module were re-derived from each construct's own declaration on the 552-line candidate — `DocChangeSetBar` `:483`, `LeafEntries` `:398`, `ReviewEntryState` `:289`, `useReviewCatalogue` `:235`, `leafIsLive` `:537`, `ReviewCatalogueRead` `:102`, `ReviewCataloguePicker` `:342`, `presenceMarker` `:332`. **Stamp accounting:** the verification pair names this leaf's base — the last real commit the reading was taken against — because the invalidation signal and the control exist only in this leaf's uncommitted working tree; closeout owns the stamp once the code commit exists.
