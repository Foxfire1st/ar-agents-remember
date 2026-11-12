# dashboard/src/panels/review/treeScroll.test.ts

## Governing Overview

[Owning route overview](overview.md)

## Purpose

Synthetic tree geometry checks scroll-only reveal, stable repeated reveal and clearance above the pinned Worklist lane.

## Code Commentary

### Logic

- A row below a mocked 200px tree viewport increases only the tree scroller scrollTop by the needed amount. It writes no inline panel style, leaves the surrounding surface position unchanged and never invokes scrollIntoView.
- A row above the viewport scrolls into view once; repeating the reveal leaves the already-visible position unchanged.
- A tree row is revealed above the pinned bottom Worklist lane. A lane row uses the real scroller bottom instead of treating the lane as an obstruction.

### Invariants And Boundaries

These are declared component or pure-function checks over the fixtures named here. This read-only analysis did not execute the tests; jsdom or width stubs do not establish browser geometry.

## Evidence

- Declared check and its fixture assertions. [2]
- Declared check and its fixture assertions. [3]
- Declared check and its fixture assertions. [4]

## Historical predecessor account

The earlier account follows as provenance. Current assertions and removed journeys are described above.

> # dashboard/src/panels/review/treeScroll.test.ts
>
> ## Governing Overview
>
> [Owning route overview](overview.md)
>
> ## Purpose
>
> Document the assertion and fixture obligations declared by this test source.
>
> ## Code Commentary
>
> Pure synthetic geometry tests panel fitting/upper/lower selected-row reveal and sticky traversal clearance, no ancestor scrollIntoView or changed outer surface scroll. Does not claim actual browser layout.
>
> ### Declared Assertions
>
> - `it('fits an oversized panel to its review viewport so even its last row can be revealed', () => {`
> - `it('scrolls only the tree panel enough to reveal its selected row', () => {`
> - `it('reveals an upper row below the sticky traversal controls rather than behind them', () => {`
>
> This is a declaration inventory, not a collected parametrized-case total or execution result.
>
> ### Evidence Boundary
>
> The source declares these checks. This card does not attest that pytest/Vitest, a native host, a real browser or an installed producer ran on this candidate. Controlled or captured inputs qualify only the operations named above.
>
> ## Evidence
>
> - Pure synthetic geometry tests panel fitting/upper/lower selected-row reveal and sticky traversal clearance, no ancestor scrollIntoView or changed outer surface scroll. Does not claim actual browser layout. (historical reference 1)
