# dashboard/src/panels/detail-panel/changeSetBar.tsx

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

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is configured for this file.

No relevant domain documentation was found.

### Repo-Internal References

Every anchor in a row occurs inside the range that row cites.

- The module's own statement of which entries a master and a leaf get, and that the Intent review is its own component. [1]
- The net's leaf attribution, rendered only when the answer carried a breakdown. [2]
- The total withheld for an unrecorded range. [3]
- The change-set control: its own counter read, the generation threaded into the viewer target, the unrecorded state, the refusal filed rather than swallowed, and the disclosure beside the button. [4]
- The counter read's brief states. [5]
- The explanation in a closed disclosure: the refusal sentence or the unrecorded sentence. [6]
- **A leaf's entries: working while live, then the Intent review control (not a change-set button).** [7]
- **The bar: the master/leaf branch, the one liveness predicate, and the leaf-scoped facts plus re-validation generation the summary is keyed on.** [8]
- This leaf's lifecycle facts as one comparable value. [9]
- **The one liveness predicate both live-dependent entries read.** [10]
- The Intent review control and its summary read. [11]
- The shared brief-state and disclosure helpers. [12]
- The re-validation generation the facts carry. [13]
- The change-set client the counter read belongs to. [14]
- The compact entry's cases: one control, request economy, brief states, leaf-scoped invalidation. [15]
- The closed leaf's recorded entry and the failed-summary case. [16]

### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.

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
