# dashboard/src/panels/detail-panel/changeSetBar.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/detail-panel/changeSetBar.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-23T06:50:00+02:00 |
| lastVerifiedCommitHash | `09329a7ee598920c519b06305b73ba8e48d72c88` |
| lastVerifiedCommitDate | 2026-09-26T00:58:43+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[panels/ overview](../overview.md)

## Purpose

The change-set bar of the DetailPanel task-document reader, extracted from `DetailPanel.tsx` by the
260731-EFA-L8 split. `ChangeSetButton` is the per-document button, `DocChangeSetBar` the compact bar
rendered above the reader content, and `leafIsLive` the one liveness predicate both gated entries read.

Since ICR-R16 the bar also carries **the entry read's own answer**. The live leaf's Intent-review entry
is a refinement of the server's recorded subject, and that read can refuse; the bar now prints what it
answered — a subject, a known-empty list, a refusal or a transport failure — beside the entry, in the
owner's own words, instead of discarding it.

Since ICR-R09 the bar carries **the whole labelled subject catalogue, not just its first row**. The
read was the entries[0]-only mechanism the packet's non-conforming example names ("the API returns
multiple entries but only the first is reachable"); it now returns the complete catalogue — every
recorded invariant and family identity of both snapshots, with per-row `presence` and the labelled
totals — and every row is offered in a picker beside the entry, retired rows marked
(`retired · before-only` / `new · after-only`), the selection driving the Intent review button's
target while the task-context target (`review: {}`) stays always reachable. Six constructs carry
that: `ReviewCatalogueRead` (what the hook returns), `useReviewCatalogue` (the read),
`ReviewEntryState` (its state line), `presenceMarker` (the per-row retired/new mark),
`ReviewCataloguePicker` (the picker with totals) and `LiveLeafEntries` (the extracted composition of
the live-leaf fragment, split out of `DocChangeSetBar` to keep the eslint complexity budget).

## Code Commentary

### Logic

**`ChangeSetButton` performs its own change-set read and now threads the published generation.** Its effect calls
`leafChangeset`/`masterChangeset`/`taskChangeset` and stores the counters; for a master net it
also stores the response's `generation` as `MasterNetPins` (four endpoints, or `null` when the
payload names none), and the button opens the viewer with `{ ...target, generation }` so the
view — and each file expansion inside it — reads the listed generation rather than
re-resolving the live tip. **Since 260921-ICR-L33 it also asks for and renders the net's leaf
attribution (`R33.2`):** the master read passes `includeLeaves: true`, the response's `leaves` is kept
in its own state (`MasterChangeset["leaves"] | null`, present only when the payload carries the field),
and `leafAttribution` renders `<N> leaf/leaves< · C committed>< · W working>` in a
`changeset-leaf-attribution` span beside the total — or nothing at all when the answer carried no
breakdown, because an absent answer is not a zero. That is what makes the net total attributable to the
leaves it sums, on the same control that opens the net viewer. This leaf's generation threading changes
what a successful master read carries, not what a failed one reports.

**Since 260921-ICR-L25 the button carries the leaf view's own `state` and withholds a zero of
nothing (register B6).** A `committed` read of a live leaf has no landed commit to read yet; the route
**answers** that state in the body (`state: "unrecorded"` plus its own sentence naming the missing
endpoint and the two views that produce it) instead of refusing it with a `404`. The button stores the
sentence in its own `unrecorded` state, renders it as the control's **own** state
(`data-testid="changeset-state"`, `data-review-state="unrecorded"`, distinct from `known-empty`), and
**withholds the `+0 −0` total** — `total` is `null` whenever `unrecorded !== null`, because a zero of
nothing is not a measurement. The consequence for the rejection path is that the two are now
distinguishable end to end: an answered-but-unrecorded range names what is missing, while a genuinely
failed read still prints its own refusal with its code, reason and next action.

**`DocChangeSetBar` branches on `kind` and gates the live block on one predicate.** A master gets the
series button; a leaf gets `committed` unconditionally (its landed delta) plus, **when the leaf's
enclosure is live**, a fragment containing the `working` button, the `Intent review` button and
`ReviewEntryState`. `leafIsLive(enclosures, activeWorktreeGroups, repo, leaf)` is that one predicate,
read from the store, so the working change-set and the reviewer entry cannot come to disagree about what
"live" means.

**The reviewer entry is offered for every live leaf, and the catalogue is a refinement rather than
a gate.** The button's target carries `review: { selectorKind, selectorId }` for the **selected
catalogue row** — which defaults to the catalogue's first row and follows the reader's own pick —
and `review: {}` when the read answered with nothing, refused, or failed — the task-context target,
which opens the review on the task's complete source change inventory. **The read never gates the
button**: the button is rendered as soon as the leaf is live, so a click that lands before the
catalogue read answers opens the whole-task review and the selected subject refines the same button
afterwards. That is the point — the entry must not depend on a knowledge read that can refuse, and
offering the entry only for a subject is exactly how a task with no knowledge lost its source
review. A selected id that outlives the catalogue (a new answer that no longer lists it) falls back
to the first row rather than opening a stale id.

**`ReviewCatalogueRead` carries every answer as a value rather than collapsing it.** `loading` is
the in-flight flag; `entries` is the whole catalogue with `totalSubjects`/`invariantTotal`/
`familyTotal` beside it (the server's own totals; a body that predates them falls back to the page
it carried, so a short catalogue still reads as the whole answer it is); `empty` is the
**known-empty** fact that the read answered `entries` with none (a fact about the datasets, not a
failure — zero subjects is a valid catalogue beside the source inventory, and the entry below
still opens that inventory); and `problem` is the read's own `ReviewFailure` for a typed refusal, a
transport-level body or an answer this client does not admit.

**`useReviewCatalogue` reads the catalogue once per live leaf and carries the answer.** It fetches
nothing for a leaf that is not live (there is no candidate to resolve, and the working change-set
is hidden for the same reason), sets `loading` before the read, and then maps the result: `entries`
→ the whole list plus its totals and `empty: entries.length === 0`; `refused` →
`reviewProblemFromRefusal(result.refusal)` or, when a refused body published no refusal,
`unreadableAnswer("refused")`; anything else → `unreadableAnswer(result.state)`; and a **thrown**
cause → `reviewProblemFromCause(cause)`. A `current` flag guards every assignment so a superseded
read cannot write into the current leaf. The route answers a refusal with its own status and the
refusal in the body, so this read goes through the review client's own decode — the hook's comment
says so, because `getJson` would have thrown and the detail would have been lost. The hook replaces
`useReviewSubject`, whose `entries?.[0]` selection **was** the first-row-only mechanism the packet
falsifies.

**`ReviewCataloguePicker` offers every row, and `presenceMarker` states which snapshot selections
reach it.** The picker renders the catalogue the read answered with — each row labelled, with the
server's own totals — and offers every recorded subject for selection, which is the falsification
of the non-conforming example made visible: a reader can select the second, third or nth row, and
a retired row is marked `retired · before-only` (and a new one `new · after-only`) rather than
hidden or merged into the live population. Rows are server identities; the picker invents none.

**`LiveLeafEntries` is the extracted live-leaf fragment.** The working button, the Intent review
button, the picker and the entry state composed into `DocChangeSetBar` crossed the lint complexity
budget once the picker arrived, so the live fragment moved into its own component; `DocChangeSetBar`
branches on `kind` and mounts `<LiveLeafEntries … />` for a live leaf exactly where the fragment
used to be. `ReviewEntryState` keeps its contract: it prints `loading`, the known-empty fact, or
the problem with the owner's code, reason, offending input and next action where published — and a
catalogue that answered with rows carries its picker and totals instead of a state line, so a
working read is not decorated with a refusal line.

**`ReviewEntryState` is the read's own state, printed rather than hidden, and it never gates the entry.**
`loading` prints `reading this candidate's recorded subjects…`; `empty` prints that no subject is
recorded for the pair and that the review opens on the task's complete source change inventory;
otherwise a `problem` prints `this candidate's recorded subjects could not be read (<code>): <detail>`,
followed by `offending input: …` and `next: …` **only when the owner published them**. Every state
carries `data-testid="review-entry-state"` and `data-review-state`, with `data-review-code` on the
refusal, so a case reads the state back out of the DOM rather than out of the text. When the read
succeeded with rows the component returns `null`: the catalogue answers through its own picker and
totals instead of a state line, and a working read is not decorated with a refusal line.

### Conventions

Small presentational components plus one hook. The bar itself performs no change-set fetch; the one
network call this module owns is the entry read through `intentReviewEntries`. Everything the read
carries is imported from the review client's public entry (`../../data/review`), so the bar classifies
through the same table every other consumer uses rather than growing its own. Inline `style` objects
match the cockpit panels' idiom, and each rendered fact carries a `data-*` attribute.

### Invariants And Boundaries

- **The reviewer entry is gated on liveness alone.** No subject, no refusal and no transport failure
  removes the button; the read's answer is printed beside it.
- **`leafIsLive` is the one liveness definition.** The working change-set action and the reviewer entry
  both read it, so they cannot disagree.
- **The browser names no candidate and no dataset.** The target carries the repo/master/leaf the server
  resolves the candidate from plus a recorded subject when the server offered one; there is no filesystem
  path anywhere in this file.
- **A refusal keeps its own words, and nothing is invented where the owner published nothing.** The
  condensed entry line prints the code, the reason, and the offending input and next action only when
  the `ReviewFailure` carries them.
- **A successful catalogue read prints no state.** `ReviewEntryState` returns `null` for an answer
  with rows; the picker and totals are the answer's rendering.
- **The picker offers only server identities.** Every row the picker offers is one the server's
  catalogue returned — the browser names no candidate, invents no id, and adds no row the pair does
  not record.
- **Boundary.** This module owns the entry's *read and display*. What a refusal code means belongs to
  `data/reviewTransport.ts`, what the session's liveness means belongs to the dashboard store, and
  whether the review itself can be opened belongs to the review surface. It owns no change-set read of
  its own.

### Todos

None open on this file. One item this card used to record as routed debt is **closed**:

- **CLOSED — the live-leaf `committed`/`working` change-set counter no longer swallows its own
  refusal detail.** The rejection handler is now `setProblem(reviewProblemFromCause(cause))` and the
  suite asserts the **rendered** refusal rather than merely the absence of counters
  (`changeSetBar.test.tsx:626`). It was recorded here as routed to R12/R24 when ICR-R16 measured it;
  the 260921-ICR-L25 change set closed it at source and at client, and round 2 additionally measured
  the rendered half for the **unrecorded** answer on the mounted product (register D01). What remains
  unmeasured is a *rendered refusal* answer on a live page — that is Class 3 (the browser suite is
  Dagger-only) and is named as a gap rather than claimed.

## Docs References

The curator checked `system/sources.md`; no Domain Documentation source is configured for this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant domain documentation was found. | — | — |

## Repo-Internal References

Every claim on this card is checkable in the shipped candidate: the two exported components and the one
predicate, the hook and its state value, the one network call, the change-set client the counter read
belongs to, and the cases that drive the bar's entry. Every anchor in a row occurs inside the range that
row cites.

| Finding | Anchor | Source |
| --- | --- | --- |
| The change-set button, its own counter read, the generation it threads from a successful master read into the viewer target, and (260921-ICR-L25) the `unrecorded` state it carries and the total it withholds. | `ChangeSetButton`; `setCounters`; `setUnrecorded` | dashboard/src/panels/detail-panel/changeSetBar.tsx:12-181 |
| **The leaf view's own answered-but-unrecorded state, printed as its own state beside the entry and never as a measured empty one.** | `ChangeSetReadState`; `data-review-state`; "unrecorded" | dashboard/src/panels/detail-panel/changeSetBar.tsx:182-237 |
| **The CLOSED item this card used to record as routed debt: the counter read's rejection handler now carries the refusal's own code and reason, and the suite asserts the rendered refusal.** | `leafChangeset`; `setProblem`; `reviewProblemFromCause` | dashboard/src/panels/detail-panel/changeSetBar.tsx:12-104; dashboard/src/panels/detail-panel/changeSetBar.tsx:12-138; dashboard/src/panels/detail-panel/changeSetBar.tsx:12-418 |
| The change-set client the counter read belongs to, which now carries `state`/`stateDetail` through to the caller. | `getJson`; `taskChangeset`; `TaskChangeset` | dashboard/src/data/changeset.ts:144-149; dashboard/src/data/changeset.ts:167-167; dashboard/src/data/changeset.ts:224-234; dashboard/src/data/changeset.ts:41-48 |
| **What the catalogue read answered, as the values the bar needs rather than one collapsed subject: the whole list with the server's totals, the known-empty fact, or the failure.** | `ReviewCatalogueRead`; `totalSubjects`; `invariantTotal`; `familyTotal` | dashboard/src/panels/detail-panel/changeSetBar.tsx:238-257; dashboard/src/panels/detail-panel/changeSetBar.tsx:241-241; dashboard/src/panels/detail-panel/changeSetBar.tsx:242-242; dashboard/src/panels/detail-panel/changeSetBar.tsx:243-243 |
| **The hook: nothing fetched for a non-live leaf, `loading` before the read, and every answer carried — the whole catalogue with its totals, known-empty, typed refusal, transport failure or unadmitted state. It replaces `useReviewSubject`, whose `entries?.[0]` was the first-row-only mechanism the packet falsifies.** | `useReviewCatalogue`; `intentReviewEntries` | dashboard/src/panels/detail-panel/changeSetBar.tsx:15-22; dashboard/src/panels/detail-panel/changeSetBar.tsx:337-384 |
| **The entry read's own state printed beside the entry, with the reason, the offending input and the next action only where the owner published them, and nothing at all for a read that answered with rows.** | `ReviewEntryState`; `review-entry-state`; `data-review-state` | dashboard/src/panels/detail-panel/changeSetBar.tsx:425-467 |
| **The per-row presence marker: a retired row reads `retired · before-only`, a new one `new · after-only`, and a both-sides row is unmarked.** | `presenceMarker` | dashboard/src/panels/detail-panel/changeSetBar.tsx:481-485 |
| **The catalogue picker: every recorded subject selectable, the server's own totals beside it, and no row invented.** | `ReviewCataloguePicker` | dashboard/src/panels/detail-panel/changeSetBar.tsx:478-533 |
| **The extracted live-leaf fragment: the working button, the Intent review button whose target carries the selected row (first row by default, the reader's pick afterwards, a stale pick falling back), the picker and the entry state.** | `LeafEntries` | dashboard/src/panels/detail-panel/changeSetBar.tsx:534-618 |
| **The bar's composition: the master/leaf branch, the one liveness predicate, and the live fragment that offers the working button, the reviewer entry and the entry's own state.** | `DocChangeSetBar`; `LeafEntries` | dashboard/src/panels/detail-panel/changeSetBar.tsx:619-672; dashboard/src/panels/detail-panel/changeSetBar.tsx:534-618 |
| **The reviewer entry's target, built from the selected catalogue row when the server offered rows and as the task-context target when it did not — never a missing control.** | `ChangeSetButton`; `LeafEntries` | dashboard/src/panels/detail-panel/changeSetBar.tsx:47-181; dashboard/src/panels/detail-panel/changeSetBar.tsx:534-618 |
| **The one liveness predicate both gated entries read.** | `leafIsLive` |dashboard/src/panels/detail-panel/changeSetBar.tsx:673-688|
| The review client's public entry, which owns the decode this bar classifies through. | `intentReviewEntries`; `reviewProblemFromRefusal`; `reviewProblemFromCause`; `unreadableAnswer` | dashboard/src/data/review.ts:28-28; dashboard/src/data/review.ts:30-30; dashboard/src/data/review.ts:29-29; dashboard/src/data/review.ts:699-705 |
| The change-set client's own comment, whose error idiom the counter read inherits, and the `state`/`stateDetail` pair its leaf view now carries. | `FilesApiError`; `TaskChangeset` | dashboard/src/data/changeset.ts:144-144; dashboard/src/data/changeset.ts:41-48; dashboard/src/data/changeset.ts:1-8 |
| **The four entry cases: the refusal shown with its fields while the entry is still offered, the known-empty answer, the transport failure with nothing invented, and the successful answer printing no state.** | "shows a never-initialized refusal beside the entry and still offers the entry"; "says known empty when the pair offers no subject, without calling it a failure"; "shows a transport failure with its reason, and raises no refusal body it does not have"; "carries the server's recorded subject into the entry, and prints no state for an answer" | dashboard/src/panels/detail-panel/reviewEntryRefusal.test.tsx:113-136; dashboard/src/panels/detail-panel/reviewEntryRefusal.test.tsx:137-155; dashboard/src/panels/detail-panel/reviewEntryRefusal.test.tsx:156-176; dashboard/src/panels/detail-panel/reviewEntryRefusal.test.tsx:177-209 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History
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
  stated reason, not a missing control.
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

## 260921-ICR-L17 The Entry Read Is Invalidated By The Workspace, Not Repeated On A Timer

`260921-ICR-L17` (`ICR-R17@v1`) closes the packet's second defect at this bar: the catalogue read used to
depend on the props alone, so the only way to discover data published after the panel opened was to
close and reopen it.

**The invalidation signal is the store's own projection.** `DocChangeSetBar` subscribes to
`s.analytics` and threads `reviewDependencyFacts(analytics)` — the projection serialised to a string, or
`"no-projection"` — down to `LeafEntries` and into `useReviewCatalogue`. `/api/state` and its delta
channel republish that projection whenever the task documents, drift snapshots, ledgers or series a
repository records move, and the store keeps its identity while nothing changed and replaces it when
anything did, so an idle workspace performs **no read at all**: an equal projection serialises to an
equal string, and the effect's dependency does not change. The comment is explicit that this is a
subscription to an existing channel and not a poll, and that it reports the **workspace facts moved** —
never that the candidate changed, because the projection carries no candidate digest and claiming a new
generation here would assert a measurement nobody made.

**The reader's own control.** `ReviewCatalogueRefresh` is always offered. It carries
`data-catalogue-stale`, and its mark is derived from `read.facts !== facts` — the facts recorded **with
the last answer**, not the live value — which is what makes it a statement about the list beside it.
It is deliberately **not** gated on `loading`: gating it there made the mark appear and vanish inside
one flush, so the reader was never told at all.

**Two more rules the read keeps.** `catalogueAnswer` is the pure mapping from one route answer to the
read state (a body this client does not admit is answered as the failure it is rather than read as a
catalogue), and `useReviewCatalogue` keeps the newest-read-wins sequence guard, so a response for a
previous leaf can never overwrite the catalogue of the leaf on screen now.


## Update History
- 2026-09-24T00:43:00+02:00 — 260921-ICR-L24 curator (memory worktree only; no code changed; no commits; leaf base `5f14fc6790cafc3ad2ae612c2e67f176392dc1fe` plus the working-tree delta): **two enforced citation rows re-cited to the constructs they name, wording unchanged.** The public-entry row's `review.ts` re-export block shifted down one line in this leaf's `data/review.ts`, so `unreadableAnswer` is now cited at its own re-export line (`30-30`), and `intentReviewEntries` moved out of the re-export block entirely to its own declaration extent (`699-705`), which is the range the row now carries. The two contributing ranges (`reviewProblemFromRefusal` `29-29`, `reviewProblemFromCause` `28-28`) are kept verbatim and no claim was reworded or dropped. **Stamp accounting:** no verification stamp was advanced — the candidate is uncommitted (base `5f14fc6790cafc3ad2ae612c2e67f176392dc1fe` plus the working-tree delta) and governed closeout owns the real stamp.
- 2026-09-23T06:50:00+02:00 — 260921-ICR-L17 curator (candidate `ar/260921-icr-l17`, uncommitted; production line at this leaf's base `c422dc00273d4ae7a5d8c9c8db97365b8c85d640`, confirmed from the enclosure contract): **the entry read is invalidated by the workspace projection and refreshed by the reader (`ICR-R17@v1`).** `DocChangeSetBar` subscribes to `analytics` and threads `reviewDependencyFacts` into `useReviewCatalogue`, so a publication after the panel opened is visible without closing it and an idle workspace performs no read at all; the new `ReviewCatalogueRefresh` is always offered and its mark is derived from the facts recorded with the last answer rather than from the live value (not gated on `loading`, which is what made it invisible); `catalogueAnswer` is the one pure mapping from an answer to the read state, and the newest-read-wins guard is kept so a previous leaf's answer cannot win. **Citation accounting:** the rows into this module were re-derived from each construct's own declaration on the 552-line candidate — `DocChangeSetBar` `:483`, `LeafEntries` `:398`, `ReviewEntryState` `:289`, `useReviewCatalogue` `:235`, `leafIsLive` `:537`, `ReviewCatalogueRead` `:102`, `ReviewCataloguePicker` `:342`, `presenceMarker` `:332`. **Stamp accounting:** the verification pair names this leaf's base — the last real commit the reading was taken against — because the invalidation signal and the control exist only in this leaf's uncommitted working tree; closeout owns the stamp once the code commit exists.
