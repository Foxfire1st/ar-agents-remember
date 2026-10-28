# dashboard/src/panels/review/ReviewSurface.narrow.test.tsx

## Governing Overview

[Owning route overview](overview.md)

## Purpose

Layout-declaration controls pin the reading column as desktop scroller and the review main as the narrow stacked-page scroller.

## Code Commentary

### Logic

- The review root declares100% height, min-height0 and hidden overflow; its40rem condition switches to automatic height/visible overflow. The reading column declares vertical auto/horizontal hidden desktop scrolling and vertical visible when stacked.
- Workspace, tree column and reading column each keep min-width0 and inherit anywhere wrapping without resetting it. Provenance retains the exact unbreakable comparison reference; the workspace has a configurable tree track and a40rem single track.
- The tree column clips both axes without becoming a scroll container, and shared button/select/input selectors exclude the tree so its own controls retain their sizing.
- The ReviewMain mount walks declared overflow ancestry: at40rem the sticky reading head's first scroller is main and the column uses clip/visible; above40rem the column is first, while main stays hidden.

### Invariants And Boundaries

These are declared component or pure-function checks over the fixtures named here. This read-only analysis did not execute the tests; jsdom or width stubs do not establish browser geometry.

## Evidence

- Declared check and its fixture assertions. [14]
- Declared check and its fixture assertions. [15]
- Declared check and its fixture assertions. [16]
- Declared check and its fixture assertions. [17]
- Declared check and its fixture assertions.

## Historical predecessor account

The earlier account follows as provenance. Current assertions and removed journeys are described above.

> # dashboard/src/panels/review/ReviewSurface.narrow.test.tsx
>
> ## Governing Overview
>
> [panels route overview](overview.md)
>
> ## Purpose
>
> **The regression pin for B7's narrow-width repair, asserted on the reviewer's OWN root.** This module mounts
> the real `ReviewSurface` over the real review client through the real `fetch` boundary — `fetch` is stubbed and the catalogue hook is explicitly mocked
> — and then holds the DOM to the **three declarations** the round-3 layout fix consists of. It exists because the
> defect it pins was a *missing declaration*, not a wrong computation: no amount of asserting rendered text could
> have caught it, and jsdom cannot lay anything out to catch it either.
>
> **Why the assertions are declarations and not a width.** The module's own header states the limit plainly:
> jsdom has no layout engine, it cannot measure a 565 px pane inside a 294 px column, and a case that read
> `getBoundingClientRect()` here would read zeros and **pass vacuously**. What jsdom *does* own is the style the
> component writes, and that style is the whole repair. The module therefore labels itself a **pin** and points at
> the measured evidence for the fix, which is the round-3 headless probe against the served bundle
> (`round3/before/…` vs `round3/after/…` in the leaf's enclosure) — the pin keeps the declarations from being
> dropped again; it does not claim to be the measurement.
>
> **The two halves of the defect it pins, both measured at 320 px on the mounted product before the fix:**
>
> - **vertical** — the reviewer supplied no scrollport of its own. The cockpit's `MAIN` is deliberately
>   `overflow: hidden` (a shell decision, shared by every view), so the panel rendered 7 620 px of content into a
>   706 px box that clipped it: `userScrollableCount: 0`, the window exactly viewport-height, three wheel trials
>   moving nothing, and a long guarantee reachable only by the browser's programmatic focus scroll.
> - **horizontal** — every complete-payload pane is a **grid item** of the disclosure, so its automatic minimum
>   size is content-based unless told otherwise. The identities this surface prints are single unbreakable tokens
>   (a 64-character comparison reference measured **539 px**, a repository path **565 px**), and the inherited
>   `break-word` does **not** lower min-content — so one such token held the pane at 565 px inside a 294 px
>   column. The defect's own signature is in this module's fixture: the `comparison.reference` is deliberately one
>   unbreakable sixty-character token, the shape that produced the defect rather than a smaller one.
>
> ## Code Commentary
>
> ### Logic
>
> The comparison-focused cases isolate the shared catalogue hook so its additional request cannot consume a comparison fixture. The ordinary-entry catalogue/comparison interaction is covered separately by ReviewSurface.navigation.test.tsx. Assertions follow the compact labels, central display controls and changed-region default without weakening the existing record, paging or refusal contracts.
>
> `payload()` retains the unbreakable comparison reference. The mount waits for both the real surface and provenance details before returning the surface root. The current second and third cases assert reading-area/workspace Panda atomic classes and header declarations, not the removed inline technical panes or a disclosure's second-child grid.
>
> **Case 1 — the reviewer's own vertical scrollport (`:140-150`).** Asserts `surface.dataset.testid` is
> `review-surface`, then `surface.style.overflowY === "auto"`, `height === "100%"`, and `minHeight` **zero-length**.
> The `dataset.testid` assertion is the one that names the root explicitly, and the comment says why: this is the
> Intent Reviewer's surface mounted by `Cockpit`, **not** the inner `review-workspace` — the overflow this pins was
> inside *this* root, which is exactly the distinction round 2's classifier got wrong.
>
> **Case 2 — reading-area declaration pins.** Exactly three scope-header/centre-column/unselected nodes are selected. The surface carries `ov-wrap_anywhere`; each selected node carries `min-w_0`, writes no local overflow-wrap style and has no resetting `ov-wrap_` class. The scope displays the fixture reference.
>
> **Case 3 — provenance details and workspace declaration pins.** Details are labelled `provenance` and retain the fixture reference. The workspace carries the two-track grid class and narrow one-track media class, the root header wraps, and surface/scope classes retain anywhere wrap and min-width zero. These are DOM/style/class assertions; jsdom proves no pixel geometry.
>
> **One serialisation detail, handled rather than worked around.** `isZeroLength` accepts `"0"` or `"0px"`, with
> the reason in the comment: React writes a numeric `0` as `"0"` and jsdom keeps it, so the assertion is on the
> **length being zero** rather than on one spelling of it. A case pinned to `"0px"` would fail against a correct
> component.
>
> ### Conventions
>
> The house idiom of this route's mounted cases: `describe`/`it` from `vitest` with `cleanup` and
> `vi.unstubAllGlobals()` in `afterEach` so the stubbed global cannot leak into the next case; module-level
> `REPO`/`MASTER`/`LEAF` constants reused by the fixture, the mount and the assertions; a lowercase plain function
> for the one helper (`isZeroLength`); and a lower-case `mount()` that returns the DOM node the cases read rather
> than the whole `RenderResult`. The cases primarily assert **style, classes and `data-` attributes** and also check that scope and provenance text retain the fixture reference. They measure no layout geometry.
>
> ### Invariants And Boundaries
>
> - **The root under test is named, and it is `review-surface`.** `[data-testid="review-workspace"]` is an inner
>   root; a pin written against it would repeat the classification error that produced finding F1.
> - **The assertions are declarations, and the module says so.** No case reads a pixel, and none may be read as
>   evidence that the layout is correct at 320 px — that evidence is the served-bundle probe. A future reader who
>   needs layout truth must run the browser-class route, which is Dagger-gated.
> - The second case asserts an exact nonempty set of three reading-area nodes before checking their atomic classes. The third asserts the workspace grid exists before checking its classes. Neither case reads layout geometry.
> - **The fixture stays hard.** The sixty-character unbreakable reference is the defect's own shape; making the
>   fixture easier would make the pin green about a payload that never failed.
> - **Boundary.** This module measures nothing and starts no server. It owns one stubbed `fetch` and three
>   assertions about the DOM `ReviewSurface` renders; the fix, its cause and its measured evidence belong to
>   `ReviewSurface.tsx` and to the enclosure's probe transcripts.
>
> ### Todos
>
> None recorded. The pin covers the declarations the round-3 fix added; whether the *rendered* narrow layout holds
> at 320 px on a real browser remains a Class-3 question (the Playwright configs are Dagger-gated by
> `dashboard/scripts/require-dagger-test-environment.mjs`), and this module deliberately does not claim it.
>
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
> Every claim on this card is checkable in the shipped candidate: the fixture builder and its deliberately
> unbreakable reference, the mount and the two waits that make the disclosure present, the three cases by their own
> names, the component each case asserts against, and the measured evidence the pin defers to. Every anchor in a
> row occurs inside the range that row cites.
>
> - **The fixture: a complete payload whose `comparison.reference` is one unbreakable sixty-character token — the measured 539 px culprit — with the digest-shaped fields alongside it.** (historical reference 1)
>
>
> - The constructed ReviewResult and real mount wait for the surface and disclosure; fetch and the catalogue hook are isolated, and layout assertions do not measure geometry. (historical reference 2)
>
> - The teardown cleans the mounted tree and restores stubbed globals. (historical reference 3)
> - **The tolerated serialisations of a numeric zero, and why the assertion is on the length rather than on `"0px"`.** (historical reference 4)
> - The own-root scrollport case checks the reviewer height and vertical overflow boundary. (historical reference 5)
> - The pane helper's own declaration, which the pin's first case depends on (moved unchanged into `ReviewRecordPanes.tsx` by L48). (historical reference 8)
> - The pane helper's own declaration, which the pin's first case depends on (moved unchanged into `ReviewRecordPanes.tsx` by L48). (historical reference 9)
> - The shared client whose read this module mounts through, and whose decode the fixture satisfies. (historical reference 10)
>
> ### Cross-Repo References
>
> No cross-repository behavior is exercised in this file. Every response is served by a stubbed same-origin
> `fetch` and names one repository namespace.
>
> No meaningful cross-repo references found.
> - Complete payload with the unbreakable reference token (historical reference 11)
> - Admitted review wrapper served to the mount (historical reference 12)
> - Mount through the real surface and fetch boundary (historical reference 13)
>
> - Case 2 asserts exactly three reading-area nodes, their min-width-zero atomic classes, inherited anywhere wrapping without local resets, and the scope's fixture reference. (historical reference 6)
> - Case 3 checks provenance details and reference text, workspace wide/narrow grid classes, header wrapping and surface/scope wrapping classes. It does not assert the old disclosure-grid inline style. (historical reference 7)

- Retired at the fifth freeze d59c3493: dashboard/src/panels/review/ReviewSurface.narrow.test.tsx:251-270 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 10e466b17feee2530c06b2670fef496c6c9e755f. Retired means the anchor no longer stands, not that the cited subject was deleted.
