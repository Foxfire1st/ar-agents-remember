# dashboard/src/panels/detail-panel/changeSetBar.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/detail-panel/changeSetBar.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-22T15:08:00+02:00 |
| reviewedWorkingCandidate | candidate `ar/260921-icr-l9`, uncommitted; production line `f141d164265e926be9249acf6ae680ccf9ffae61` (this leaf's base) — the catalogue picker with totals and the `LiveLeafEntries` extraction are the uncommitted candidate (303 → 415 lines) |
| reviewedWorkingCandidate | candidate `ar/260921-icr-l16`, uncommitted; base `8ff80ce08814856c9d6fec5b19093e6540fc6d7f` |
| reviewedWorkingCandidate | candidate `ar/260921-icr-l13`, uncommitted; base `6695a2a12961ef340c8864d56f0a1ce12b51b3c5` |
| lastVerifiedCommitHash | `02957762709c9b515b4ff57f7f13524a7c0dfb8d` |
| lastVerifiedCommitDate | 2026-09-22T16:02:31+02:00|
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
re-resolving the live tip. Its rejection handler is still
`() => live && setCounters(null)` — so a failed counter read leaves the button without a total **and
without a reason**. That is the change-set client's behaviour, deliberately untouched by ICR-R16 (see
the routed-debt note below); this leaf's generation threading changes what a successful master
read carries, not what a failed one reports.

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

One routed item is recorded rather than fixed, because it is a different route, client and owner:

- **The live-leaf `committed`/`working` change-set counter still swallows its own refusal detail.**
  `ChangeSetButton`'s rejection handler is `() => live && setCounters(null)` and the read goes through
  `data/changeset.ts` → `getJson` → `/api/changeset/task`, so a failed counter read simply disappears
  with no reason and no next action. That is the change-set client, not the review transport, and it is
  **routed to R12 (historical committed-leaf review) / R24 (usable review navigation)**. Measured in
  this leaf; not fixed here, to keep the blast radius to the review route.

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
| The change-set button, its own counter read, and the generation it threads from a successful master read into the viewer target. | `ChangeSetButton`; `setCounters` | dashboard/src/panels/detail-panel/changeSetBar.tsx:29-93 |
| **The routed debt this card records and does not fix: the counter read's rejection handler, on a different route and client.** | `leafChangeset`; `setCounters` | dashboard/src/panels/detail-panel/changeSetBar.tsx:6-12; dashboard/src/panels/detail-panel/changeSetBar.tsx:45-78 |
| The change-set client and route that debt belongs to, which this leaf leaves untouched. | `getJson`; `taskChangeset` | dashboard/src/data/changeset.ts:1-8; dashboard/src/data/changeset.ts:78-79 |
| **What the catalogue read answered, as the values the bar needs rather than one collapsed subject: the whole list with the server's totals, the known-empty fact, or the failure.** | `ReviewCatalogueRead`; `totalSubjects`; `invariantTotal`; `familyTotal` | dashboard/src/panels/detail-panel/changeSetBar.tsx:98-120 |
| **The hook: nothing fetched for a non-live leaf, `loading` before the read, and every answer carried — the whole catalogue with its totals, known-empty, typed refusal, transport failure or unadmitted state. It replaces `useReviewSubject`, whose `entries?.[0]` was the first-row-only mechanism the packet falsifies.** | `useReviewCatalogue`; `intentReviewEntries` | dashboard/src/panels/detail-panel/changeSetBar.tsx:122-187; dashboard/src/panels/detail-panel/changeSetBar.tsx:15-22; dashboard/src/data/review.ts:403-419 |
| **The entry read's own state printed beside the entry, with the reason, the offending input and the next action only where the owner published them, and nothing at all for a read that answered with rows.** | `ReviewEntryState`; `review-entry-state`; `data-review-state` | dashboard/src/panels/detail-panel/changeSetBar.tsx:189-230 |
| **The per-row presence marker: a retired row reads `retired · before-only`, a new one `new · after-only`, and a both-sides row is unmarked.** | `presenceMarker` | dashboard/src/panels/detail-panel/changeSetBar.tsx:232-240 |
| **The catalogue picker: every recorded subject selectable, the server's own totals beside it, and no row invented.** | `ReviewCataloguePicker` | dashboard/src/panels/detail-panel/changeSetBar.tsx:242-289 |
| **The extracted live-leaf fragment: the working button, the Intent review button whose target carries the selected row (first row by default, the reader's pick afterwards, a stale pick falling back), the picker and the entry state.** | `LiveLeafEntries` | dashboard/src/panels/detail-panel/changeSetBar.tsx:291-358 |
| **The bar's composition: the master/leaf branch, the one liveness predicate, and the live fragment that offers the working button, the reviewer entry and the entry's own state.** | `DocChangeSetBar`; `LiveLeafEntries` | dashboard/src/panels/detail-panel/changeSetBar.tsx:360-398; dashboard/src/panels/detail-panel/changeSetBar.tsx:291-358 |
| **The reviewer entry's target, built from the selected catalogue row when the server offered rows and as the task-context target when it did not — never a missing control.** | `ChangeSetButton`; `LiveLeafEntries` | dashboard/src/panels/detail-panel/changeSetBar.tsx:291-353
| **The one liveness predicate both gated entries read.** | `leafIsLive` | dashboard/src/panels/detail-panel/changeSetBar.tsx:400-415 |
| The review client's public entry, which owns the decode this bar classifies through. | `intentReviewEntries`; `reviewProblemFromRefusal`; `reviewProblemFromCause`; `unreadableAnswer` | dashboard/src/data/review.ts:22-31; dashboard/src/data/review.ts:403-419 |
| The change-set client's own comment, whose error idiom the counter read inherits. | `FilesApiError` | dashboard/src/data/changeset.ts:1-8 |
| **The four entry cases: the refusal shown with its fields while the entry is still offered, the known-empty answer, the transport failure with nothing invented, and the successful answer printing no state.** | "shows a never-initialized refusal beside the entry and still offers the entry"; "says known empty when the pair offers no subject, without calling it a failure"; "shows a transport failure with its reason, and raises no refusal body it does not have"; "carries the server's recorded subject into the entry, and prints no state for an answer" | dashboard/src/panels/detail-panel/reviewEntryRefusal.test.tsx:113-136; dashboard/src/panels/detail-panel/reviewEntryRefusal.test.tsx:137-155; dashboard/src/panels/detail-panel/reviewEntryRefusal.test.tsx:156-176; dashboard/src/panels/detail-panel/reviewEntryRefusal.test.tsx:177-209 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-09-22T15:08:00+02:00 — 260921-ICR-L9 curator (candidate `ar/260921-icr-l9`, uncommitted; production line `f141d164265e926be9249acf6ae680ccf9ffae61`, this leaf's base): **the bar offers every catalogue row, not just the first (303 → 415 lines; `ICR-R09@v1`).** The entry read's hook is now `useReviewCatalogue` returning `ReviewCatalogueRead` — the whole list with `totalSubjects`/`invariantTotal`/`familyTotal`, the known-empty fact, or the problem — and the new `ReviewCataloguePicker` renders every row with per-row `presence` marks from `presenceMarker` (`retired · before-only` / `new · after-only`), the selection driving the Intent review button's target (first row by default, the reader's pick afterwards, a stale pick falling back) while the task-context target stays always reachable. The Purpose's "Three constructs carry that" sentence is replaced: `ReviewSubjectRead` and `useReviewSubject` **no longer exist** — their `entries?.[0]` selection was exactly the first-row-only mechanism the packet's non-conforming example names — and the live-leaf fragment moved into the extracted `LiveLeafEntries` (an eslint-complexity extraction, not a behavior change). The entry's gating rule is unchanged and restated: liveness alone, task context always reachable, read never gates. **Citation accounting:** every row into this file re-derived against the 415-line candidate — `ChangeSetButton` `:29-96`, `ReviewCatalogueRead` `:98-120`, `useReviewCatalogue` `:122-187`, `ReviewEntryState` `:189-230`, `presenceMarker` `:232-240`, `ReviewCataloguePicker` `:242-289`, `LiveLeafEntries` `:291-358`, `DocChangeSetBar` `:360-398`, `leafIsLive` `:400-415` — with four new rows for the marker, the picker, the extraction and the target construction, and the two `review.ts` rows re-pointed to `intentReviewEntries` `:403-419`; the refusal-case row's last range follows the stub's additive totals fields (`:177-209`). **Stamp accounting:** the verification pair names the leaf's base — the last real commit the reading was taken against — because the picker, the totals and the extraction exist only in this leaf's uncommitted candidate; closeout owns the stamp once the code commit exists.
- 2026-09-22T11:00:00+02:00 — 260921-ICR-L13 curator (candidate `ar/260921-icr-l13`, uncommitted; base `6695a2a12961ef340c8864d56f0a1ce12b51b3c5`): **the button threads the published generation into the viewer target (280 → 303 lines).** `ChangeSetButton` stores the master read's `generation` as `MasterNetPins` and opens `{ ...target, generation }`, so the view and its expansions read the listed generation; the rejection handler and the routed R12/R24 debt are unchanged. **Citation accounting:** every row into this file was re-derived against the moved candidate (the generation state + handlers moved everything below `:44`: `ChangeSetButton` `:28-70` → `:29-93`, `ReviewSubjectRead` `:72-83` → `:97-106`, `useReviewSubject` `:85-135` → `:116-158`, `ReviewEntryState` `:137-178` → `:163-201`, `DocChangeSetBar` `:180-260` → `:208-283`, `leafIsLive` `:262-277` → `:288-301`), and the two `changeset.ts` rows followed the client move (`taskChangeset` `:56-57` → `:78-79`). The entry-read, review-client and refusal-case rows are kept as recorded (those files are untouched by this leaf). Verification metadata is **not** advanced: the candidate is uncommitted and closeout owns the stamp.
- 2026-09-22T07:05:34+02:00 — 260921-ICR-L16 curator (candidate `ar/260921-icr-l16`, uncommitted; base `8ff80ce08814856c9d6fec5b19093e6540fc6d7f`): **the entry read's answer is now carried and printed, and this card's earlier account of "no subject means no button" is corrected rather than carried.** `useReviewSubject` returns a `ReviewSubjectRead` — `loading`, the first `entry`, a known-empty `empty` flag, or a `problem` — instead of `ReviewEntry | undefined`, so a refused read and an empty list are no longer indistinguishable and neither is discarded; the read classifies through the review client's shared decode (`reviewProblemFromRefusal`/`reviewProblemFromCause`/`unreadableAnswer`), because the route publishes its refusal in the body of a non-2xx response and `getJson` would have thrown and lost it. The new `ReviewEntryState` prints that answer beside the entry — refused with the owner's code, reason, offending input and next action; known-empty for a pair that records no subject; `network` for a transport failure with nothing invented — and returns `null` for a successful read. The reviewer entry remains gated on **liveness alone**, which is unchanged from R02, and that is why the card's earlier sentence that "a refusal, an empty list, a rejected promise … leave the subject `undefined`, so no subject means no button" has been **removed**: it described the R02 hook, not this one. Line count 186 → 280. It also records, as **routed rather than fixed**, the live-leaf counter's swallowed refusal detail (`ChangeSetButton`'s `() => live && setCounters(null)` over `data/changeset.ts` → `getJson` → `/api/changeset/task`) to R12/R24 — a different route, client and owner. Every row of the reference table was re-derived against this candidate. **Stamp accounting:** the verification pair names the **merged production line** `8ff80ce08814856c9d6fec5b19093e6540fc6d7f` (2026-09-22T00:48:09+02:00) — the line this candidate now sits on after the leaf's pair sync; the `reviewedWorkingCandidate` row states what was actually read, and nothing in this leaf is committed, so closeout owns the stamp.
- 2026-09-21T14:59:00+02:00 — 260921-ICR-L2 curator (uncommitted change set on `ar/260921-icr-l2`, base `702714fc05363cb28eacaf101ba8384475a6aa56`): **the entry stopped depending on the subject.** The button is now gated on liveness alone; the server's recorded subject travels with the target as a refinement, and its absence (an empty list or an unreadable refusal) produces the task-context target `review: {}` instead of no button at all. That is the non-conforming example the packet names — "an empty subject list makes the source review disappear" — closed at the entry. The hook, its no-fetch-for-a-dead-leaf rule and its "a refusal is a normal answer" idiom are unchanged; what changed is what an empty answer *means*, and both comments now say it. One citation row was re-derived against this candidate. **Stamp accounting:** the verification rows still name the last real commit whose bytes this card was verified against, because nothing in this leaf is committed; claims whose evidence this leaf's change moved were re-read against the candidate and are stamp-class leftovers that only closeout can stamp.

- 2026-09-20T13:43:00+02:00 — 260915-KS-L45 curator (uncommitted change set on `ar/260915-ks-l45-ar`, base `fb719f89`): **the reviewer entry is reachable now, and this card's account of *why* it was not is the correction that matters.** The `selectorKind`/`selectorId` props are gone. A live leaf's subject is read from the server by the new `useReviewSubject` hook, which calls `intentReviewEntries(repo, master, leaf)` and keeps `result.entries?.[0]`; the gate is now `live && subject`, and the liveness half was extracted into `leafIsLive` so both gated entries read one predicate. The gate is not weakened: a refusal, an empty list, a rejected promise or a non-live leaf all leave `subject` undefined and **no subject means no button**. The card records why that matters — the prop was the unreachable part, because `taskReader.tsx` and the master header pass no selector, so `live && selectorId` could never hold on any real navigation — and records the invariant the hook's own comment states: the id is a recorded identity inside the candidate the server resolved, so the hook chooses no candidate and invents no id. The revision of the previous paragraph is retained in place below in substance: the entry is still added beside the working/committed actions and never in their place, its target still carries the subject's recorded identity rather than a filesystem path, and the reviewer entry still reports no counters. No verification stamp was advanced, because no commit contains this body.
- 2026-09-18T18:10+02:00 — 260915-KS-L22 curator (uncommitted change set on `ar/260915-ks-l22`, base `2dcacb27`): **added the reviewer entry beside the change-set actions.** `DocChangeSetBar` gained `selectorKind = "invariant"` / `selectorId` props and a third `ChangeSetButton` labelled *Intent review*, rendered only when the enclosure is live and a `selectorId` is supplied — the same liveness the working action is gated on, and never in the working or committed action's place. Its target carries `review: { selectorKind, selectorId }`, the reviewed subject's recorded identity rather than a filesystem path, because the browser does not choose the candidate. The new paragraph above states that, and states the boundary the bar keeps: it still fetches nothing itself, and the new entry's counter effect reads only the leaf or master request, so no counters are reported for a review. No reference row was touched; ranges into this source belong to the citation-reprojection engine. The metadata block above names this leaf's uncommitted candidate as what was read, and the two verification stamps are left exactly as the last real verification set them. The body was changed substantively and this entry is the history record, not a metadata-only refresh.
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the change-set bar extracted from `DetailPanel.tsx`. Verification pinned to the leaf base until closeout stamps the code commit.
