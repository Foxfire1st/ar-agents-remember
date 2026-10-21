# dashboard/src/panels/review/codeFacts.test.tsx

## Governing Overview

[Owning route overview](overview.md)

## Purpose

Synthetic comparison-bound code facts add a code-only tree row without replacing the current node or moving focus and scroll.

## Code Commentary

### Logic

- Unknown recorded meaning remains unknown even when implementation evidence exists; it is not counted as a known code-only change.
- An explicit ancestor-scroll probe simulates native anchoring during facts arrival and checks restoration to83. The tree case now mounts changeSetModel plus ReviewTree, comparing shownInvariantIds before/after facts.
- The selected node remains identical/current/focused at the same tree scroll position; the arriving member is code changed, aggregate changed count becomes2, and a polite status says one invariant changed only in its code without duplicating the traversal status.
- Facts from another comparison remain pending; loading and unavailable summaries remain distinct.

### Invariants And Boundaries

These are declared component or pure-function checks over the fixtures named here. This read-only analysis did not execute the tests; jsdom or width stubs do not establish browser geometry.

## Evidence

- Declared check and its fixture assertions. [2]
- Declared check and its fixture assertions. [3]
- Declared check and its fixture assertions. [4]
- Declared check and its fixture assertions. [5]

## Historical predecessor account

The earlier account follows as provenance. Current assertions and removed journeys are described above.

> # dashboard/src/panels/review/codeFacts.test.tsx
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
> Synthetic leaf facts assert code-only rows only under known unchanged meaning, no unknown relabeling, late-facts row/count/announcement/traversal without selection/focus/scroll movement, and comparison-bound loading/unavailable summary. Native scroll anchoring is simulated in DOM, not browser acceptance.
>
> ### Declared Assertions
>
> - `it('does not relabel unknown recorded meaning as a code-only change', () => {`
> - `it('preserves the real ancestor scroll container across native anchoring on facts arrival', () => {`
> - `it('adds an unread member without moving the selected node, focus or scroll; traversal reaches it', () => {`
> - `it('does not use facts of another comparison and distinguishes missing and unavailable', () => {`
>
> This is a declaration inventory, not a collected parametrized-case total or execution result.
>
> ### Evidence Boundary
>
> The source declares these checks. This card does not attest that pytest/Vitest, a native host, a real browser or an installed producer ran on this candidate. Controlled or captured inputs qualify only the operations named above.
>
> ## Evidence
>
> - Synthetic leaf facts assert code-only rows only under known unchanged meaning, no unknown relabeling, late-facts row/count/announcement/traversal without selection/focus/scroll movement, and comparison-bound loading/unavailable summary. Native scroll anchoring is simulated in DOM, not browser acceptance. (historical reference 1)
