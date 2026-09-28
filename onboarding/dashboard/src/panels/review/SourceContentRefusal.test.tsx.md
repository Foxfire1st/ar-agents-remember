# dashboard/src/panels/review/SourceContentRefusal.test.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/SourceContentRefusal.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-28T21:38:01+02:00 |
| lastVerifiedCommitHash | `ae2fd5c864aa2609ae45b5c7dbbaa693569aefc6` |
| lastVerifiedCommitDate | 2026-09-28T22:11:57+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

The expansion-read half of ICR-R16, **over R03's own pane**: the Source pane's transport-level failures
now render through the shared block instead of as the thrown message alone.

The boundary this module keeps is explicit in its header. R03 owns `SourceContent` and its typed-refusal
rendering (`review-source-refusal`), which is **untouched**; this module pins the *other* answer shape
the expansion route can give — a transport-level refusal or a socket that never answered — which used to
be printed as `the entry's content could not be read: 503 unavailable` with the adapter's own
instruction dropped. The `503` body is the real route's measured answer
(`sha256 c55ee098da2014aabb8784ae65ca289f0111dbdd18aa70a504553fca1635a690`, recorded as
`unwired-adapter` in this leaf's evidence run).

The module exercises the real `SourceContent` and the real `reviewSourceContent`, with only `fetch`
stubbed, against one listed entry (`src/batch.py`, `modified`, textual) at two fixed code-tree ids — so
the read is the generation the listing published, exactly as the pane receives it.

## Code Commentary

### Logic

**One entry fixture and one measured body.** `ENTRY` is a single listed inventory row as the inventory
publishes it (`path`, `status`, `content`, `mode_change`); `UNWIRED` is the route's own `503` body with
its `detail` ("the surface is not served rather than served as an empty file") and its `nextAction`
("start the dashboard through its composition root, which supplies the review adapter"). `mount()` renders
the pane with a fixed `beforeCodeTreeId`/`afterCodeTreeId` pair, and the global fetch is restored in
`afterEach`.

**Three cases pin the three things that changed.** First, an unwired adapter renders through the shared
block — `data-review-state="unavailable-history"`, `data-review-code="unavailable"`, the subject line
`this entry's content could not be opened`, and **both** the server's detail and its next action — while
asserting the **pre-fix** rendering is gone: `review-source-error` must be absent, which is the no-op
that would mean the old paragraph came back. Second, an unadmitted query renders as `validation` with its
`offendingInput` (`src/batch.py`) and its `nextAction` printed by the shared block's own test ids, and
**no** `review-retry` — a typed refusal keeps its owner's recovery route and is not offered a retry.
Third, a socket that never answered renders as `network`, and clicking `review-retry` **re-reads**: the
case asserts a second fetch and then asserts that the retry renders *whatever the read then answers* —
here R03's own typed refusal through R03's own block (`review-source-refusal`), with the shared failure
block gone. That last assertion is the seam between the two owners, pinned rather than assumed.

### Conventions

The module imports the real pane and the shipped `ReviewChangedFile` type from the public entries and
declares no production behaviour of its own. Fixtures are upper-case constants; `mount` is a
zero-argument renderer; every case is an `async` `it` inside one `describe`; `afterEach` cleans up and
restores the global fetch. Assertions read `data-review-state`, `data-review-code`, the shared block's
own test ids (`review-offending-input`, `review-next-action`, `review-retry`), R03's own
`review-source-refusal`, and the **absence** of the pre-fix `review-source-error` — so the module pins
what must not come back as well as what must appear.

### Invariants And Boundaries

- **R03's typed path is untouched.** The third case ends by asserting R03's own `review-source-refusal`
  renders through R03's own block after a retry; the module never re-specifies it.
- **The pre-fix rendering must not return.** The `review-source-error` absence assertion is the explicit
  control for the paragraph this leaf replaced.
- **A transport-level refusal carries the owner's own words.** The `503` case asserts the detail and the
  next action, not merely a state token.
- **Retry only where there is no owner-published route.** The `bad-request` case asserts no
  `review-retry`, and the `network` case asserts the retry re-reads.
- **One renderer for the failure shape.** The block this module finds by `review-failure` is the shared
  `ReviewProblemBlock` imported by the pane, not a copy declared for this pane.
- **Boundary.** It pins the expansion pane's transport-level answers only. It makes no browser-level
  claim — the A01/A13 journeys belong to R25 with R24/R17 — and it does not re-pin R03's typed refusal
  semantics, which stay R03's own tests' subject.

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

Every claim on this card is checkable in the shipped candidate: the module's own ownership statement and
provenance, the two fixtures, the one mount, the three cases, and the pane and shared renderer they
drive. Every anchor in a row occurs inside the range that row cites.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The header's own ownership statement — R03 owns the typed refusal and this module pins the other answer shape — and the provenance of the measured `503` body with its digest.** | `SourceContent`; `reviewSourceContent` | dashboard/src/panels/review/SourceContentRefusal.test.tsx:1-19 |
| The real pane under test and the wire type of the entry it receives. | `SourceContent` | dashboard/src/panels/review/SourceContentRefusal.test.tsx:19-24 |
| The one listed entry fixture, exactly as the inventory publishes a row. | `ENTRY` | dashboard/src/panels/review/SourceContentRefusal.test.tsx:21-26 |
| **The route's own `503` body, with the detail and the next action the pre-fix rendering dropped.** | `UNWIRED` | dashboard/src/panels/review/SourceContentRefusal.test.tsx:27-33 |
| The one mount, at the two code-tree ids the listing published. | `mount` | dashboard/src/panels/review/SourceContentRefusal.test.tsx:35-45 |
| The cleanup and global-fetch restore between cases. | `afterEach` | dashboard/src/panels/review/SourceContentRefusal.test.tsx:16-19; dashboard/src/panels/review/SourceContentRefusal.test.tsx:48-51 |
| **An unwired adapter rendered through the shared block with the owner's detail and next action, and the pre-fix paragraph asserted absent.** | "carries the code, reason, offending input and next action of an unwired adapter" | dashboard/src/panels/review/SourceContentRefusal.test.tsx:52-77 |
| **An unadmitted query named as `validation` with its offending input and next action, and no retry offered for a typed refusal.** | "names an unadmitted query as a validation failure rather than as the thrown message" | dashboard/src/panels/review/SourceContentRefusal.test.tsx:79-112 |
| **A socket that never answered offering the retry, and the retry rendering whatever the read then answers — here R03's own typed refusal, unchanged.** | "offers a retry for a socket that never answered, and the retry re-reads" | dashboard/src/panels/review/SourceContentRefusal.test.tsx:114-149 |
| SourceContent retains transport failures and reuses the shared problem renderer while preserving its typed expansion refusal branch; since L48 the failure is held with the request key it answers, inside `useSourceContentRead`. | `SourceContent`; `useSourceContentRead`; "function refusalBlock(refusal: ReviewRefusal) {" | dashboard/src/panels/review/SourceContent.tsx:222-271; dashboard/src/panels/review/SourceContent.tsx:180-220; dashboard/src/panels/review/SourceContent.tsx:113-125 |
| **The one block this module finds by `review-failure`, with the state and code attributes the cases read.** | `ReviewProblemBlock`; `review-offending-input`; `review-next-action`; `review-retry` | dashboard/src/panels/review/ReviewOutcome.tsx:115-177 |
| R03's own typed-refusal block, which the retry case asserts is still the renderer for a typed answer. | `refusalBlock`; `review-source-refusal` | dashboard/src/panels/review/SourceContent.tsx:113-125 |

## Cross-Repo References

No cross-repository behavior is exercised in this file. Every response is served by a stubbed
same-origin `fetch` and names one repository namespace.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-28T21:55:52+02:00 — 260921-ICR-L48 curator (uncommitted candidate tree `ac73216e2a763b72844a63b8c36c81f9a8b5f0e8` over code base `cb1b942af60a7ed5006ac992075d2bf96aeb9fa7`): **re-citation of rows whose earlier range arrived by generated projection.** The memory-quality check reopened the transport-failure row because an older *Generated citation repair* bullet in this card names `refusalBlock`, so a range written there was never shown to be reviewed. Each row was re-read against the construct it is about in this candidate, the claim still holds, and its anchor was re-bound from the bare name to the exact declaration text the curator read (`function refusalBlock(refusal: ReviewRefusal) {`), which is the check's own remedy (re-cite the location the claim is about). The generated bullets below are left untouched as the dated record of the projection. No stamp advanced.
- 2026-09-28T21:38:01+02:00 — 260921-ICR-L48 curator (uncommitted candidate tree `ac73216e2a763b72844a63b8c36c81f9a8b5f0e8` over code base `cb1b942af60a7ed5006ac992075d2bf96aeb9fa7`): **reopened claim re-read — the content read moved into `useSourceContentRead`.** L48 extracted the read into a hook that binds the answer and the failure to their request key and reads through the surface's cache; a transport failure is still retained and rendered through the shared `ReviewProblemBlock` with retry, and a typed refusal still renders through `refusalBlock`, so this module's cases pin the same behaviour. The row now names the hook and every range was re-derived from its declaration. The mechanical-repair bullet below is superseded by this re-read. No verification stamp was advanced.
- 2026-09-26T21:11:28+00:00: Generated citation repair: `refusalBlock` repointed to dashboard/src/panels/review/SourceContent.tsx:112-124. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-23T00:45:00+02:00 — 260921-ICR-L10 curator: **removed a verification metadata row for a field that does not exist.** The developer ruled that field out on 2026-09-22 — it has no purpose and had spread by copy-paste — and this pass deleted it here and reworded the sentences that referred to it. The fact it carried (this card describes an uncommitted candidate whose base the verification pair names) is stated in the history entries around it. No content impact: no claim about the source changed.

- 2026-09-22T07:05:34+02:00 — 260921-ICR-L16 curator (candidate `ar/260921-icr-l16`, uncommitted; base `8ff80ce08814856c9d6fec5b19093e6540fc6d7f`): **created.** The module is new in this leaf and this is its one-to-one card. It records the deliberate seam this module exists on: R03 owns `SourceContent` and its typed-refusal block, and this leaf's F1 fix routes only the pane's **transport-level** answers through the shared `ReviewProblemBlock` — so the card states that boundary first and then the three cases that pin it: an unwired adapter rendered with the owner's detail and next action **and** the pre-fix `review-source-error` paragraph asserted absent; an unadmitted query named as `validation` with no retry; and a socket that never answered offering a retry which then renders *whatever the read answers*, asserted through R03's own `review-source-refusal`. That last assertion is the seam itself, pinned rather than assumed. **Stamp accounting:** the verification pair names the **merged production line** `8ff80ce08814856c9d6fec5b19093e6540fc6d7f` (2026-09-22T00:48:09+02:00) — the line this candidate now sits on after the leaf's pair sync — while what was actually read is this leaf's **uncommitted** working tree at that base: this leaf's **uncommitted** candidate at that base. Nothing in this leaf is committed, so no commit contains the bytes a stamp would claim to have verified; closeout owns the stamp.
