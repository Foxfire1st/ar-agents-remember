# dashboard/src/panels/review/ReviewKeys.test.tsx

## Governing Overview

[Owning route overview](overview.md)

## Purpose

Effective review key bindings and the scoped help shortcut remain observable through the real keymap store.

## Code Commentary

### Logic

- Rebinding review.nextChange to N updates the displayed Next block binding while Previous block keeps k; the persisted command identity remains review.nextChange.
- The help shortcut acts in the review zone, ignores search and other editable elements, the changeset zone and Ctrl-modified input, and removes its listener on unmount.

### Invariants And Boundaries

These are declared component or pure-function checks over the fixtures named here. This read-only analysis did not execute the tests; jsdom or width stubs do not establish browser geometry.

## Evidence

- Declared check and its fixture assertions. [2]
- Declared check and its fixture assertions. [3]

## Historical predecessor account

The earlier account follows as provenance. Current assertions and removed journeys are described above.

> # dashboard/src/panels/review/ReviewKeys.test.tsx
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
> Key-reference component checks effective rebound N/k, question-mark opening outside editable/other zones, modifiers, close and listener disposal. Registry completeness belongs to commands.test.ts.
>
> ### Declared Assertions
>
> - `it('opens a named key reference from a visible Keys control and shows effective bindings', async () => {`
> - `it('opens with ? outside text fields, ignores editable and other zones, and removes its listener', async () => {`
>
> This is a declaration inventory, not a collected parametrized-case total or execution result.
>
> ### Evidence Boundary
>
> The source declares these checks. This card does not attest that pytest/Vitest, a native host, a real browser or an installed producer ran on this candidate. Controlled or captured inputs qualify only the operations named above.
>
> ## Evidence
>
> - Key-reference component checks effective rebound N/k, question-mark opening outside editable/other zones, modifiers, close and listener disposal. Registry completeness belongs to commands.test.ts. (historical reference 1)
