# dashboard/src/panels/review/ReviewHeader.test.tsx

## Governing Overview

[Owning route overview](overview.md)

## Purpose

Header controls expose effective reading-block keys, return focus from the key dialog and keep the task identity readable in wrapping layouts.

## Code Commentary

### Logic

- Keys is beside Refresh; the dialog names Next block j, Previous block k, Tree [ and Chat ]. Escape and Close return focus to Keys, and Back invokes its callback once.
- The supplied task title and supplied chip slot are drawn; a missing title falls back to the leaf. The 40rem declaration case checks a wrapping title row and ellipsis on the title, without measuring a rendered viewport.
- A recognized long leaf identity draws its short L181 form with the full value in the tooltip; its label can shrink but keeps a minimum character width. A nonstandard leaf stays plain without a tooltip.

### Invariants And Boundaries

These are declared component or pure-function checks over the fixtures named here. This read-only analysis did not execute the tests; jsdom or width stubs do not establish browser geometry.

## Evidence

- Declared check and its fixture assertions. [2]
- Declared check and its fixture assertions. [3]
- Declared check and its fixture assertions. [4]
- Declared check and its fixture assertions. [5]

## Historical predecessor account

The earlier account follows as provenance. Current assertions and removed journeys are described above.

> # dashboard/src/panels/review/ReviewHeader.test.tsx
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
> Header integration checks Keys immediately beside Refresh, the displayed j/k reference, focus entry and trigger-focus return after Escape or the explicit Close button inside the dialog, visible subject identifiers/historical text and Back callback. It does not click the backdrop; these are jsdom assertions, not real-browser measurements.
>
> ### Declared Assertions
>
> - `it('mounts visible Keys beside Refresh and restores trigger focus after closing its reference', async () => {`
>
> This is a declaration inventory, not a collected parametrized-case total or execution result.
>
> ### Evidence Boundary
>
> The source declares these checks. This card does not attest that pytest/Vitest, a native host, a real browser or an installed producer ran on this candidate. Controlled or captured inputs qualify only the operations named above.
>
> ## Evidence
>
> - Header integration checks Keys immediately beside Refresh, the displayed j/k reference, focus entry and trigger-focus return after Escape or the explicit Close button inside the dialog, visible subject identifiers/historical text and Back callback. It does not click the backdrop; these are jsdom assertions, not real-browser measurements. (historical reference 1)
