# dashboard/src/panels/review/ReviewSurface.traversalRepair.test.tsx

## Governing Overview

[Owning route overview](../overview.md)

## Purpose

Document the assertion and fixture obligations declared by this test source.

## Code Commentary

The test uses native captured inputs and explicit jsdom geometry to declare Surface j/k checks at 390 and 1280 pixels. It expects panel scrolling and focus with preventScroll, unchanged window.scrollY, and no row.scrollIntoView call. The seeded surface.scrollTop remains 137 at 390 pixels but resets to zero at 1280 pixels; the narrow endpoint cases retain 137 and report no later/earlier change. These assertions are not real-browser ancestor-scroll proof or a fresh execution result.

### Declared Assertions

- `it.each([390, 1280].flatMap((width) => [J, K].map((key) => ({ width, key }))))(`
- `it.each([{ key: J, edge: 'later' }, { key: K, edge: 'earlier' }])(`

This is a declaration inventory, not a collected parametrized-case total or execution result.

### Evidence Boundary

The source declares these checks. This card does not attest that pytest/Vitest, a native host, a real browser or an installed producer ran on this candidate. Controlled or captured inputs qualify only the operations named above.

## Evidence


- The explicit jsdom assertions preserve window scroll and avoid row.scrollIntoView; surface.scrollTop stays 137 at 390 pixels and resets to zero at 1280 pixels. Narrow endpoint assertions retain 137 and the selected, focused row. This is static assertion evidence, not real-browser proof. [1]

