# dashboard/src/panels/review/ReviewSurface.narrow.test.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/ReviewSurface.narrow.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-26T00:15:00+02:00 |
| lastVerifiedCommitHash | `09329a7ee598920c519b06305b73ba8e48d72c88` |
| lastVerifiedCommitDate | 2026-09-26T00:58:43+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[panels route overview](../overview.md)

## Purpose

**The regression pin for B7's narrow-width repair, asserted on the reviewer's OWN root.** This module mounts
the real `ReviewSurface` over the real review client through the real `fetch` boundary — only `fetch` is stubbed
— and then holds the DOM to the **three declarations** the round-3 layout fix consists of. It exists because the
defect it pins was a *missing declaration*, not a wrong computation: no amount of asserting rendered text could
have caught it, and jsdom cannot lay anything out to catch it either.

**Why the assertions are declarations and not a width.** The module's own header states the limit plainly:
jsdom has no layout engine, it cannot measure a 565 px pane inside a 294 px column, and a case that read
`getBoundingClientRect()` here would read zeros and **pass vacuously**. What jsdom *does* own is the style the
component writes, and that style is the whole repair. The module therefore labels itself a **pin** and points at
the measured evidence for the fix, which is the round-3 headless probe against the served bundle
(`round3/before/…` vs `round3/after/…` in the leaf's enclosure) — the pin keeps the declarations from being
dropped again; it does not claim to be the measurement.

**The two halves of the defect it pins, both measured at 320 px on the mounted product before the fix:**

- **vertical** — the reviewer supplied no scrollport of its own. The cockpit's `MAIN` is deliberately
  `overflow: hidden` (a shell decision, shared by every view), so the panel rendered 7 620 px of content into a
  706 px box that clipped it: `userScrollableCount: 0`, the window exactly viewport-height, three wheel trials
  moving nothing, and a long guarantee reachable only by the browser's programmatic focus scroll.
- **horizontal** — every complete-payload pane is a **grid item** of the disclosure, so its automatic minimum
  size is content-based unless told otherwise. The identities this surface prints are single unbreakable tokens
  (a 64-character comparison reference measured **539 px**, a repository path **565 px**), and the inherited
  `break-word` does **not** lower min-content — so one such token held the pane at 565 px inside a 294 px
  column. The defect's own signature is in this module's fixture: the `comparison.reference` is deliberately a
  single unbreakable 64-character token, so the payload is the shape that produced the defect rather than a
  smaller one.

## Code Commentary

### Logic

**One fixture builder and one mount, so the three cases cannot drift apart.** `payload()` returns a complete
`ReviewPayload` whose `comparison.reference` is one 64-character token (`:41`) and whose digests are
`"d".repeat(64)`-shaped (`:43-48`) — the measured 539 px culprit, kept because a fixture that had been made
easier would no longer exercise the shape. `reviewed` wraps it as the `ReviewResult` the client decodes, and
`mount()` stubs `fetch` with that body, renders `ReviewSurface` with the real repo/master/leaf, and **waits for
both `review-surface` and `review-details`** before returning the surface root — the second wait is what makes
the disclosure's grid present when case 3 reads it, rather than a race the case would win by luck.

**Case 1 — the reviewer's own vertical scrollport (`:140-150`).** Asserts `surface.dataset.testid` is
`review-surface`, then `surface.style.overflowY === "auto"`, `height === "100%"`, and `minHeight` **zero-length**.
The `dataset.testid` assertion is the one that names the root explicitly, and the comment says why: this is the
Intent Reviewer's surface mounted by `Cockpit`, **not** the inner `review-workspace` — the overflow this pins was
inside *this* root, which is exactly the distinction round 2's classifier got wrong.

**Case 2 — every complete-payload pane may shrink and wrap (`:152-162`).** Queries `[data-pane]` and asserts, for
each, `minWidth` zero-length and `overflowWrap === "anywhere"`. It asserts the element set is **non-empty before
comparing anything** (`:157`), so a query that silently found no panes cannot make the loop vacuous — the
failure mode a "for each of none" assertion would otherwise hide.

**Case 3 — the disclosure's grid track and the header row (`:164-177`).** Reads the disclosure's **second child**
(the first is its `<summary>`) and asserts it is a `DIV` whose `gridTemplateColumns` is `minmax(0, 1fr)`; then
reads `review-subject`, takes its parent, and asserts the header row's `flexWrap === "wrap"` and the subject's
own `overflowWrap === "anywhere"`.

**One serialisation detail, handled rather than worked around.** `isZeroLength` accepts `"0"` or `"0px"`, with
the reason in the comment: React writes a numeric `0` as `"0"` and jsdom keeps it, so the assertion is on the
**length being zero** rather than on one spelling of it. A case pinned to `"0px"` would fail against a correct
component.

### Conventions

The house idiom of this route's mounted cases: `describe`/`it` from `vitest` with `cleanup` and
`vi.unstubAllGlobals()` in `afterEach` so the stubbed global cannot leak into the next case; module-level
`REPO`/`MASTER`/`LEAF` constants reused by the fixture, the mount and the assertions; a lowercase plain function
for the one helper (`isZeroLength`); and a lower-case `mount()` that returns the DOM node the cases read rather
than the whole `RenderResult`. Every assertion is on **style or `data-` attributes**, never on prose, because
prose is not what this pin is about.

### Invariants And Boundaries

- **The root under test is named, and it is `review-surface`.** `[data-testid="review-workspace"]` is an inner
  root; a pin written against it would repeat the classification error that produced finding F1.
- **The assertions are declarations, and the module says so.** No case reads a pixel, and none may be read as
  evidence that the layout is correct at 320 px — that evidence is the served-bundle probe. A future reader who
  needs layout truth must run the browser-class route, which is Dagger-gated.
- **Non-empty input is asserted before anything is compared.** Case 2 asserts `panes.length > 0` first, so the
  loop cannot pass by iterating nothing; the same discipline is why case 3 asserts `tagName === "DIV"` on the
  grid rather than reading `style` off an optional.
- **The fixture stays hard.** The 64-character unbreakable reference is the defect's own shape; making the
  fixture easier would make the pin green about a payload that never failed.
- **Boundary.** This module measures nothing and starts no server. It owns one stubbed `fetch` and three
  assertions about the DOM `ReviewSurface` renders; the fix, its cause and its measured evidence belong to
  `ReviewSurface.tsx` and to the enclosure's probe transcripts.

### Todos

None recorded. The pin covers the declarations the round-3 fix added; whether the *rendered* narrow layout holds
at 320 px on a real browser remains a Class-3 question (the Playwright configs are Dagger-gated by
`dashboard/scripts/require-dagger-test-environment.mjs`), and this module deliberately does not claim it.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

Every claim on this card is checkable in the shipped candidate: the fixture builder and its deliberately
unbreakable reference, the mount and the two waits that make the disclosure present, the three cases by their own
names, the component each case asserts against, and the measured evidence the pin defers to. Every anchor in a
row occurs inside the range that row cites.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The fixture: a complete payload whose `comparison.reference` is one unbreakable 64-character token — the measured 539 px culprit — with the digest-shaped fields alongside it.** | `payload`; "1678adab6416222068ba391db5b8b48d7c38b5b8c859adeac36fad3d0a2a" | dashboard/src/panels/review/ReviewSurface.narrow.test.tsx:36-102 |
| The `ReviewResult` the real client decodes, and the mount that stubs only `fetch` and waits for both the surface root and the disclosure. | `reviewed`; `mount`; `review-surface`; `review-details` | dashboard/src/panels/review/ReviewSurface.narrow.test.tsx:104-130 |
| The leak guard: `cleanup()` and `vi.unstubAllGlobals()` after every case. | `afterEach`; `vi.unstubAllGlobals()` | dashboard/src/panels/review/ReviewSurface.narrow.test.tsx:132-135 |
| **The tolerated serialisations of a numeric zero, and why the assertion is on the length rather than on `"0px"`.** | `isZeroLength` | dashboard/src/panels/review/ReviewSurface.narrow.test.tsx:137-137 |
| **Case 1: the reviewer's own vertical scrollport, asserted on `review-surface` — the root that names the boundary between this surface and the inner `review-workspace`.** | "gives the reviewer its own vertical scrollport on its own root"; `overflowY`; `minHeight`; `height` | dashboard/src/panels/review/ReviewSurface.narrow.test.tsx:140-150 |
| **Case 2: every `[data-pane]` is a grid item that may shrink (`min-width: 0`) and wrap its long identities (`overflow-wrap: anywhere`), with the non-empty input asserted first so the loop cannot be vacuous.** | "lets every complete-payload pane shrink and wrap its long identities"; `data-pane`; `panes.length` | dashboard/src/panels/review/ReviewSurface.narrow.test.tsx:152-162 |
| **Case 3: the disclosure's grid track is `minmax(0, 1fr)` — not the implicit `auto` — and the header row wraps while the subject span carries its own break opportunity.** | "constrains the disclosure's grid track and wraps the header row"; `gridTemplateColumns`; `flexWrap`; `review-subject` | dashboard/src/panels/review/ReviewSurface.narrow.test.tsx:164-177 |
| The pane helper's own declaration, which the pin's first case depends on. | `pane` | dashboard/src/panels/review/ReviewSurface.tsx:89-89 |
| The pane helper's own declaration, which the pin's first case depends on. | `pane` | dashboard/src/panels/review/ReviewSurface.tsx:89-89 |
| The shared client whose read this module mounts through, and whose decode the fixture satisfies. | `ReviewPayload`; `ReviewResult` | dashboard/src/data/review.ts:425-457; dashboard/src/data/review.ts:499-505 |

## Cross-Repo References

No cross-repository behavior is exercised in this file. Every response is served by a stubbed same-origin
`fetch` and names one repository namespace.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-25T22:19:46+00:00: Generated citation repair: `ReviewPayload`; `ReviewResult` repointed to dashboard/src/data/review.ts:425-457; dashboard/src/data/review.ts:499-505. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T00:15:00+02:00 — 260921-ICR-L25 curator, round 3 (candidate `ar/260921-icr-l25-ar`; the file is **untracked** in the code worktree, so no commit contains it — code worktree HEAD is `d9e7e6e79ce532d16c689435ae95a63aab430f94` and that is the last real commit on this line; memory base `39adea206651654dbfacf2ee1bb4e2f3763b515b`): **created this one-to-one card for the new acceptance module (register B7, round 3).** The file has no previous onboarding because the file itself is new in this round, so this is a create rather than a refresh; the 1-to-1 source mapping is what obliges it. The card records the module's own stated limit (jsdom cannot lay anything out, so the cases hold the **declarations** the repair consists of and a `getBoundingClientRect()` case here would pass vacuously), the deliberately unbreakable 64-character fixture token that reproduces the defect's shape rather than a smaller one, the three cases by name, the `review-surface`-not-`review-workspace` root distinction the first case exists to name, and the non-empty-input assertion that keeps the pane loop from being vacuous. **Stamp accounting:** no verification stamp was advanced beyond naming the line's HEAD — the file is uncommitted, so the governed closeout owns the real stamp, and a stamp naming a commit that does not contain the file would be a fabricated provenance claim. No commit was made.
