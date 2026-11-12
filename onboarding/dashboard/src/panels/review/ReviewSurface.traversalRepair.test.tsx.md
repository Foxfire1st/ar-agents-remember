# dashboard/src/panels/review/ReviewSurface.traversalRepair.test.tsx

## Governing Overview

[Owning route overview](overview.md)

## Purpose

Explicit geometry distinguishes revealing a requested tree row before its delayed read from moving the reading page or end selection.

## Code Commentary

### Logic

- At stubbed390/1280 widths a reading-column subject control selects an uncached member. Before its answer the tree scroller reveals the row above pinned rows using scrollTop only, with surface137 and window scroll unchanged.
- After the answer focus lands on the selected tree row using only preventScroll, with no row.scrollIntoView call and the surrounding positions still preserved.
- At either reading-block end j/k returns the exact No earlier/later block status while the selected/focused row, zero tree scroll and surface137 all stay in place.

### Invariants And Boundaries

These are declared component or pure-function checks over the fixtures named here. This read-only analysis did not execute the tests; jsdom or width stubs do not establish browser geometry.

## Evidence

- Declared check and its fixture assertions. [2]
- Declared check and its fixture assertions. [3]

## Historical predecessor account

The earlier account follows as provenance. Current assertions and removed journeys are described above.

> # dashboard/src/panels/review/ReviewSurface.traversalRepair.test.tsx
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
> The test uses native captured inputs and explicit jsdom geometry to declare Surface j/k checks at 390 and 1280 pixels. It expects panel scrolling and focus with preventScroll, unchanged window.scrollY, and no row.scrollIntoView call. The seeded surface.scrollTop remains 137 at 390 pixels but resets to zero at 1280 pixels; the narrow endpoint cases retain 137 and report no later/earlier change. These assertions are not real-browser ancestor-scroll proof or a fresh execution result.
>
> ### Declared Assertions
>
> - `it.each([390, 1280].flatMap((width) => [J, K].map((key) => ({ width, key }))))(`
> - `it.each([{ key: J, edge: 'later' }, { key: K, edge: 'earlier' }])(`
>
> This is a declaration inventory, not a collected parametrized-case total or execution result.
>
> ### Evidence Boundary
>
> The source declares these checks. This card does not attest that pytest/Vitest, a native host, a real browser or an installed producer ran on this candidate. Controlled or captured inputs qualify only the operations named above.
>
> ## Evidence
>
>
> - The explicit jsdom assertions preserve window scroll and avoid row.scrollIntoView; surface.scrollTop stays 137 at 390 pixels and resets to zero at 1280 pixels. Narrow endpoint assertions retain 137 and the selected, focused row. This is static assertion evidence, not real-browser proof. (historical reference 1)
>
