# dashboard/src/panels/review/SourceContentRefusal.test.tsx

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

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

Every claim on this card is checkable in the shipped candidate: the module's own ownership statement and
provenance, the two fixtures, the one mount, the three cases, and the pane and shared renderer they
drive. Every anchor in a row occurs inside the range that row cites.

- **The header's own ownership statement — R03 owns the typed refusal and this module pins the other answer shape — and the provenance of the measured `503` body with its digest.** [1]
- The real pane under test and the wire type of the entry it receives. [2]
- The one listed entry fixture, exactly as the inventory publishes a row. [3]
- **The route's own `503` body, with the detail and the next action the pre-fix rendering dropped.** [4]
- The one mount, at the two code-tree ids the listing published. [5]
- The cleanup and global-fetch restore between cases. [6]
- **An unwired adapter rendered through the shared block with the owner's detail and next action, and the pre-fix paragraph asserted absent.** [7]
- **An unadmitted query named as `validation` with its offending input and next action, and no retry offered for a typed refusal.** [8]
- **A socket that never answered offering the retry, and the retry rendering whatever the read then answers — here R03's own typed refusal, unchanged.** [9]
- SourceContent retains transport failures and reuses the shared problem renderer while preserving its typed expansion refusal branch; since L48 the failure is held with the request key it answers, inside `useSourceContentRead`. [10]
- **The one block this module finds by `review-failure`, with the state and code attributes the cases read.** [11]
- R03's own typed-refusal block, which the retry case asserts is still the renderer for a typed answer. [12]

### Cross-Repo References

No cross-repository behavior is exercised in this file. Every response is served by a stubbed
same-origin `fetch` and names one repository namespace.

No meaningful cross-repo references found.
