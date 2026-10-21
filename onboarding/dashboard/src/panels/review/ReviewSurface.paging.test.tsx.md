# dashboard/src/panels/review/ReviewSurface.paging.test.tsx

## Governing Overview

[Owning route overview](overview.md)

## Purpose

Mounted paging controls preserve opaque continuation cursors, collection bounds and code-specific reset wording.

## Code Commentary

### Logic

- Typed synthetic review replies feed the shipped client and ReviewSurface while the catalogue hook is isolated. Page bounds name returned, remaining and scope; the next action exists only for a published cursor.
- Advancing returns exactly the published cursor in the same knowledge collection and draws the next bounds. Choosing a collection or First page sends no continuation. A foreign-cursor reset is worded separately from a moved comparison.
- The picker offers knowledge and whole review, never the retired records collection; even a synthetic stale records selection emits no records request. Walk totals remain distinct from selection totals, and an unpaged whole review retains the selected invariant parameters.
- Opening also reads summary, outline, trees and lane. The changed helper filters only /api/review/intent calls before counting page reads and inspecting their URLs; the advancing stub refuses unrelated opening reads instead of letting them consume page one.

### Invariants And Boundaries

Typed payloads and opaque literal cursors are synthetic controls, including a shortened cursor literal. This read-only analysis did not execute the suite, certify a native cursor or test browser keyboard/focus geometry.

## Evidence

- Declared check and its fixture assertions. [22]
- Declared check and its fixture assertions. [23]
- Declared check and its fixture assertions. [24]
- Declared check and its fixture assertions. [25]
- Declared check and its fixture assertions. [26]
- Declared check and its fixture assertions. [27]
- Declared check and its fixture assertions. [28]
- Declared check and its fixture assertions. [29]

## Historical predecessor account

The earlier account follows as provenance. Current assertions and removed journeys are described above.

> # dashboard/src/panels/review/ReviewSurface.paging.test.tsx
>
> ## Governing Overview
>
> [dashboard/src/panels route overview](overview.md)
>
> ## Purpose
>
> The mounted-surface cases for `ICR-R10@v1`'s page control: the **real** `ReviewSurface` over the
> **real** review client, with `fetch` stubbed and the catalogue hook isolated for comparison-focused cases. Every request is built by the shipped client and
> every response travels the way the browser's does — status, body, the shared decode in
> `data/reviewTransport.ts`, the component tree — and no assertion reads a prop the test itself passed.
>
> The defect these cases catch is the packet's own non-conforming example: the surface used to render a
> remainder (its `locations_remaining`, and now any page's `remaining`) with **no control that reached the
> rest of the collection**. The module's header names the two wrong repairs it also fails against: a
> "next page" button that re-sends the cursor it is already standing on (so the page never advances), and
> one that offers itself for a body that published no cursor at all (so the button fetches nothing).
>
> ## Code Commentary
>
> ### Logic
>
> The comparison-focused cases isolate the shared catalogue hook so its additional request cannot consume a comparison fixture. The ordinary-entry catalogue/comparison interaction is covered separately by ReviewSurface.navigation.test.tsx. Assertions follow the compact labels, central display controls and changed-region default without weakening the existing record, paging or refusal contracts.
>
> **The request is asserted, not just the render.** The advancing case asserts that the *second* request
> carries the cursor the server published rather than the one the client was standing on, and that the
> bounds move from `16 of 103` to `32 of 103` — the two facts that separate a working control from a
> button that re-fetches its own page.
>
> **The retired records collection cannot be asked for: the control is gone and no such request goes out.** The picker offers `knowledge` only — `records` left with the review matrix (MIK-R74 rule 1) — and the case asserts no `pageOf=records` request is ever issued; a stale attempt resolves to the whole review with no collection paged and no refusal rendered. The reset case asks `pageOf=knowledge` deliberately and states the reset as its own action, with the first page one click away.
>
> **One normaliser owns the two spellings of "no page".** The component reads `carriedPage(payload)`
> instead of touching `payload.page`, so no consumer can reintroduce the `!== null` comparison that made
> the mounted refusal unreachable for every real response.
>
> **A reset is worded from its own refusal code.** `RESET_GLOSS` distinguishes "this comparison moved"
> (`comparison_page_reset`) from "that cursor is not this collection's" (`comparison_page_unreadable`),
> so a foreign cursor is never called a moved comparison.
>
> **The two total bases are worded apart on knowledge pages.** `total_basis` is the page's own field — `selection`
> for the comparison, `walk` for the view — and the case asserts both spellings, because one rendered
> sentence carrying two meanings is how `total` came to mean two different numbers.
>
> ### Conventions
>
> - `fetch` and the comparison-focused catalogue hook are isolated; the review client, decode and component are the shipped ones.
> - Page bodies are typed synthetic `ReviewPayload` fixtures carrying judgment. The two cursor literals are treated as opaque strings; the client neither constructs nor parses them. The shortened `KNOWLEDGE_CURSOR` literal does not establish verbatim native-cursor provenance.
> - Each case is named for the behavior it protects, and the header states the defects it fails against.
>
> ### Invariants And Boundaries
>
> - **No next action without a published cursor.** A body with a remainder and no cursor renders no
>   `review-next-page` control, whatever it reported.
> - `payloadWith(page)` returns `ReviewPayload` and supplies a `judgment` object. These synthetic payloads exercise the mounted paging behavior.
> - Not covered here: browser keyboard/focus traversal and the finished cockpit interaction
>   (`ICR-R24@v1` owns those), and the assembled A16 acceptance (`ICR-R25@v1`).
>
> ### Todos
>
> None recorded.
>
> Cursor fixtures supply opaque strings through a typed fetch signature. `RECORDS_CURSOR` is reused as the next knowledge cursor. Cases assert bounds lines, control labels, knowledge continuation, reset wording from refusal codes, and the retired records collection earning no request or refusal. The closing case carries the selector on an unpaged whole-review request.
> ## Evidence
>
> ### Docs References
>
> No domain documentation source is configured for this repository (`system/sources.md` carries no
> `Domain Documentation` entries). The statements below are grounded in repository source only.
>
> No configured domain documentation could be checked.
>
> ### Repo-Internal References
>
>
> - The mounted cases use the shipped ReviewSurface and review client with fetch stubbed; useReviewCatalogue is additionally isolated for comparison-focused cases. (historical reference 1)
>
>
> - The paging fixtures retain KNOWLEDGE_CURSOR and RECORDS_CURSOR as opaque strings; no client-side cursor decoding is asserted. (historical reference 2)
>
> - No captured refused-records body exists: the retired collection earns no request, so no refusal is rendered from a capture.
>
> - **The bounds, the scope and the one action that reaches the rest.** (historical reference 4)
>
>
> - **The advancing case: the second request carries the cursor the server published, and the bounds move.** (historical reference 5)
>
>
> - **No next action for a body that published no cursor, whatever it reported.** (historical reference 6)
>
>
> - A named collection asked for deliberately, and a reset stated as its own action. (historical reference 7)
>
>
> - The retired records page earns no request and renders no refusal: records left with the review matrix (MIK-R74 rule 1). (historical reference 8)
>
>
> - **A reset worded from its refusal code, so a foreign cursor is not called a moved comparison.** (historical reference 9)
>
>
> - The bounds sentence distinguishes walk from selection totals on the surviving knowledge collection. (historical reference 10)
>
>
>
>
> - **The one normaliser of the two spellings of "no page", and the bounds sentence built from the page's own basis.** (historical reference 12)
>
>
> - The page contract on the client, including the basis field and the separate refusal. (historical reference 13)
>
>
> - **The control the cases drive: the page picker, the actions, the bounds line and the refusal block.** (historical reference 14)
>
>
> - The read target key includes page position, making a page change a distinct read. (historical reference 15)
>
>
> - The published page shape these bodies have: the surface's own page value and its two refusal codes. (historical reference 16)
>
>
> ### Cross-Repo References
>
> No cross-repository behavior is exercised in this file: the component, the client and the decode are all
> this repository's, and `fetch` is the only boundary crossed.
>
> No meaningful cross-repo references found.
>
>
>
> - Typed fetch signature for paged requests (historical reference 19)
>
>
> - The stubbed published-shape case distinguishes foreign-cursor reset wording from a moved comparison; it does not test an automatic repair journey. (historical reference 21)
>
> - Despite its historical test title, the closing case supplies a null page, asserts whole-review bounds and absent paging controls, and requires selector parameters with no pageOf parameter. (historical reference 11)
> - RECORDS_CURSOR is an opaque fixture literal reused as the continuation of the second knowledge page; it does not demonstrate a records-page journey. (historical reference 17)
> - payloadWith returns a typed synthetic ReviewPayload, including judgment and a nullable page. (historical reference 18)
> - mountSubject supplies repository, master, leaf and invariant selector props without an initial page selection; cases use it for both paging and whole-review checks. (historical reference 20)
