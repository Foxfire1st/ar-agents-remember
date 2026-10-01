# dashboard/src/panels/review/ReviewSurface.paging.test.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

The mounted-surface cases for `ICR-R10@v1`'s page control: the **real** `ReviewSurface` over the
**real** review client, with only `fetch` stubbed. Every request is built by the shipped client and
every response travels the way the browser's does — status, body, the shared decode in
`data/reviewTransport.ts`, the component tree — and no assertion reads a prop the test itself passed.

The defect these cases catch is the packet's own non-conforming example: the surface used to render a
remainder (its `locations_remaining`, and now any page's `remaining`) with **no control that reached the
rest of the collection**. The module's header names the two wrong repairs it also fails against: a
"next page" button that re-sends the cursor it is already standing on (so the page never advances), and
one that offers itself for a body that published no cursor at all (so the button fetches nothing).

## Code Commentary

### Logic

The comparison-focused cases isolate the shared catalogue hook so its additional request cannot consume a comparison fixture. The ordinary-entry catalogue/comparison interaction is covered separately by ReviewSurface.navigation.test.tsx. Assertions follow the compact labels, central display controls and changed-region default without weakening the existing record, paging or refusal contracts.

**The request is asserted, not just the render.** The advancing case asserts that the *second* request
carries the cursor the server published rather than the one the client was standing on, and that the
bounds move from `16 of 103` to `32 of 103` — the two facts that separate a working control from a
button that re-fetches its own page.

**A refused page renders the refusal rather than an empty state.** The refusal case consumes
`RECORDS_PAGE_REFUSAL_RESPONSE` — a **captured** server body (see
`recordsPageRefusal.captured.ts`) — and asserts the key's *absence* before rendering it, then the code,
both of the owner's digests read out of the captured body, the live first-page action, the absence of
the bounds sentence, and that "no remainder to reach" appears nowhere. The capture matters because the
route serializes with `exclude_none=True`: a refused page **omits** the `page` key, and a hand-built
body sending `page: null` hid exactly that difference from the round-1 case.

**One normaliser owns the two spellings of "no page".** The component reads `carriedPage(payload)`
instead of touching `payload.page`, so no consumer can reintroduce the `!== null` comparison that made
the mounted refusal unreachable for every real response.

**A reset is worded from its own refusal code.** `RESET_GLOSS` distinguishes "this comparison moved"
(`comparison_page_reset`) from "that cursor is not this collection's" (`comparison_page_unreadable`),
so a foreign cursor is never called a moved comparison.

**The two collections' totals are worded apart.** `total_basis` is the page's own field — `selection`
for the comparison, `walk` for the view — and the case asserts both spellings, because one rendered
sentence carrying two meanings is how `total` came to mean two different numbers.

### Conventions

- Only `fetch` is stubbed; the client, the decode and the component are the shipped ones.
- Page bodies are the measured shape of the real route's answer in this leaf's evidence run, and the two
  cursors are the server's own opaque strings — the client neither constructs nor parses one.
- Each case is named for the behavior it protects, and the header states the defects it fails against.

### Invariants And Boundaries

- **No next action without a published cursor.** A body with a remainder and no cursor renders no
  `review-next-page` control, whatever it reported.
- The captured body is typed `unknown` on purpose: the route sends three fields this client's review
  mirror does not declare (`evidence.channels`, `knowledge.revision_selection`, `source.attribution`),
  so annotating it would need either a cast or a lossy projection of the bytes under test.
- Not covered here: browser keyboard/focus traversal and the finished cockpit interaction
  (`ICR-R24@v1` owns those), and the assembled A16 acceptance (`ICR-R25@v1`).

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- **The module's own statement of what it exercises, of the defect it catches, and of the two wrong repairs it also fails against.** [1]
- The two opaque cursors, verbatim from the evidence run: one per collection, which is why mixing them up would be a defect. [2]
- The captured server body the refusal case renders. [3]
- **The bounds, the scope and the one action that reaches the rest.** [4]
- **The advancing case: the second request carries the cursor the server published, and the bounds move.** [5]
- **No next action for a body that published no cursor, whatever it reported.** [6]
- A named collection asked for deliberately, and a reset stated as its own action. [7]
- **The refused records page rendered from the CAPTURED body, with its code, both identities and a live first-page action.** [8]
- **A reset worded from its refusal code, so a foreign cursor is not called a moved comparison.** [9]
- **The two collections' totals kept apart in the sentence the reader sees.** [10]
- The whole review stays reachable and the selector travels through a paged request. [11]
- **The one normaliser of the two spellings of "no page", and the bounds sentence built from the page's own basis.** [12]
- The page contract on the client, including the basis field and the separate refusal. [13]
- **The control the cases drive: the page picker, the actions, the bounds line and the refusal block.** [14]
- The read target key includes page position, making a page change a distinct read. [15]
- The published page shape these bodies have: the surface's own page value and its two refusal codes. [16]

### Cross-Repo References

No cross-repository behavior is exercised in this file: the component, the client and the decode are all
this repository's, and `fetch` is the only boundary crossed.

No meaningful cross-repo references found.
