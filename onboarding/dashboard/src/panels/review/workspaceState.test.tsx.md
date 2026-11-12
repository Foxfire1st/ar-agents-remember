# dashboard/src/panels/review/workspaceState.test.tsx

## Governing Overview

[Owning route overview](overview.md)

## Purpose

The workspace state hook keeps tree expansion idempotent and makes selected reading content displace the Worklist.

## Code Commentary

### Logic

- toggleGroup opens and closes a group. openGroup on the already-open group returns the identical Set reference, rather than allocating an equal replacement.
- After setWorklist(true), setChosen(family) stores that exact family selection and clears the worklist flag.

### Invariants And Boundaries

These are declared component or pure-function checks over the fixtures named here. This read-only analysis did not execute the tests; jsdom or width stubs do not establish browser geometry.

## Evidence

- Declared check and its fixture assertions. [2]
- Declared check and its fixture assertions. [3]

## Historical predecessor account

The earlier account follows as provenance. Current assertions and removed journeys are described above.

> # dashboard/src/panels/review/workspaceState.test.tsx
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
> With matchMedia stubbed true, the hook begins inline and an explicit split choice survives an ordinary rerender. A separate false stub starts split. Selecting a family leaves the fabricated common surface scrollTop unchanged. No resize, media-result transition or real-browser width measurement is performed.
>
> ### Declared Assertions
>
> - `it('starts narrow expression diffs inline and preserves the reader choice afterwards', () => {`
> - `it('keeps the narrow review scroll position during an in-tree choice', () => {`
> - `it('starts wide expression diffs side by side', () => {`
>
> This is a declaration inventory, not a collected parametrized-case total or execution result.
>
> ### Evidence Boundary
>
> The source declares these checks. This card does not attest that pytest/Vitest, a native host, a real browser or an installed producer ran on this candidate. Controlled or captured inputs qualify only the operations named above.
>
> ## Evidence
>
> - With matchMedia stubbed true, the hook begins inline and an explicit split choice survives an ordinary rerender. A separate false stub starts split. Selecting a family leaves the fabricated common surface scrollTop unchanged. No resize, media-result transition or real-browser width measurement is performed. (historical reference 1)
