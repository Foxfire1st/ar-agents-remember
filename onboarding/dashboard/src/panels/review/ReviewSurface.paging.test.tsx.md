# dashboard/src/panels/review/ReviewSurface.paging.test.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/ReviewSurface.paging.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-23T00:15:00+02:00 |
| lastVerifiedCommitHash | `972b44cc07b307929535fe7974d6a30d53c9c4f1` |
| lastVerifiedCommitDate | 2026-09-23T07:48:19+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

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

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| **The module's own statement of what it exercises, of the defect it catches, and of the two wrong repairs it also fails against.** | `ReviewSurface`; `intentReview` | dashboard/src/panels/review/ReviewSurface.paging.test.tsx:1-19 |
| The two opaque cursors, verbatim from the evidence run: one per collection, which is why mixing them up would be a defect. | `KNOWLEDGE_CURSOR`; `RECORDS_CURSOR` | dashboard/src/panels/review/ReviewSurface.paging.test.tsx:38-41 |
| The captured server body the refusal case renders. | `RECORDS_PAGE_REFUSAL_RESPONSE` | dashboard/src/panels/review/recordsPageRefusal.captured.ts:1-29 |
| **The bounds, the scope and the one action that reaches the rest.** | "states the bounds and scope of a page and offers the one action that reaches the rest" | dashboard/src/panels/review/ReviewSurface.paging.test.tsx:160-189 |
| **The advancing case: the second request carries the cursor the server published, and the bounds move.** | "advances with the cursor the server published, and keeps the same collection" | dashboard/src/panels/review/ReviewSurface.paging.test.tsx:190-235 |
| **No next action for a body that published no cursor, whatever it reported.** | "offers no next action for a page that published no cursor, whatever it reported" | dashboard/src/panels/review/ReviewSurface.paging.test.tsx:236-267 |
| A named collection asked for deliberately, and a reset stated as its own action. | "asks for a named collection deliberately, and states a reset as its own action" | dashboard/src/panels/review/ReviewSurface.paging.test.tsx:268-315 |
| **The refused records page rendered from the CAPTURED body, with its code, both identities and a live first-page action.** | "states a refused records page from the CAPTURED server body, with its code, identities and a live first-page action" | dashboard/src/panels/review/ReviewSurface.paging.test.tsx:316-373 |
| **A reset worded from its refusal code, so a foreign cursor is not called a moved comparison.** | "words a reset from its refusal code, so a foreign cursor is not called a moved comparison" | dashboard/src/panels/review/ReviewSurface.paging.test.tsx:374-442 |
| **The two collections' totals kept apart in the sentence the reader sees.** | "keeps the two collections' totals apart in the sentence the reader sees" | dashboard/src/panels/review/ReviewSurface.paging.test.tsx:443-498 |
| The whole review stays reachable and the selector travels through a paged request. | "keeps the whole review reachable and carries the selector through a paged request" | dashboard/src/panels/review/ReviewSurface.paging.test.tsx:499-514 |
| **The one normaliser of the two spellings of "no page", and the bounds sentence built from the page's own basis.** | `carriedPage`; `pageBounds`; `continuationOf`; `RESET_GLOSS` | dashboard/src/data/review.ts:548-569; dashboard/src/data/review.ts:537-543; dashboard/src/data/review.ts:578-580; dashboard/src/data/review.ts:591-595 |
| The page contract on the client, including the basis field and the separate refusal. | `ReviewCollectionPage` |dashboard/src/data/review.ts:406-425|
| **The control the cases drive: the page picker, the actions, the bounds line and the refusal block.** | `PageControls`; `PagePicker`; `PageActions`; `PageBoundsLine`; `PageRefusalBlock` | dashboard/src/panels/review/ReviewSurface.tsx:786-849; dashboard/src/panels/review/ReviewSurface.tsx:624-660; dashboard/src/panels/review/ReviewSurface.tsx:662-717; dashboard/src/panels/review/ReviewSurface.tsx:719-741; dashboard/src/panels/review/ReviewSurface.tsx:583-622 |
| The page as part of the read's target key, so a page change is its own read. | `targetKeyOf` |dashboard/src/panels/review/ReviewSurface.tsx:22-22|
| The published page shape these bodies have: the surface's own page value and its two refusal codes. | `ReviewCollectionPage`; `comparison_page_reset`; `comparison_page_unreadable` | mcp/src/agents_remember/models/knowledge/review.py:366-440; mcp/src/agents_remember/models/knowledge/review.py:149-150 |

## Cross-Repo References

No cross-repository behavior is exercised in this file: the component, the client and the decode are all
this repository's, and `fetch` is the only boundary crossed.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-23T00:15:00+02:00 — 260921-ICR-L10 curator: **created.** The module is new in this leaf
  (`ICR-R10@v1`) and this is its one-to-one card. It records the two design facts a later reader would
  otherwise have to rediscover — the refusal case is pointed at a **captured** server body because the
  route omits the `page` key rather than sending `null`, and one normaliser (`carriedPage`) owns both
  spellings of "no page" so no consumer can compare against `null` again — plus the boundary this
  module leaves to others: `ICR-R24@v1` owns keyboard/focus traversal and the finished cockpit
  interaction, and `ICR-R25@v1` assembles A16. **Stamp accounting:** the verification pair names the
  **production line at this leaf's base** `dcf35a0e0fc06bccdafd22390b7588b0aea811bc`
  (2026-09-22T20:08:58+02:00); the module and the component it drives are **uncommitted**, so closeout
  owns the real stamp.
