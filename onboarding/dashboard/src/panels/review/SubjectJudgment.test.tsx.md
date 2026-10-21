# dashboard/src/panels/review/SubjectJudgment.test.tsx

## Governing Overview

[Owning route overview](overview.md)

## Purpose

Synthetic judgment rows and proofs remain visible while origin metadata is kept out of selected statement prose.

## Code Commentary

### Logic

- Reasons and proof facets stay outside disclosures alongside attempt and covered-entry counts; unavailable history still preserves proofs, a missing required judgment field produces an alert, and an older changed family row names its missing effect with examined-member count.
- A separate synthetic SelectedStatement receives distinct before/after origins but draws none of their task, wave, handoff-entry or leaf values and neither origin block. Origin presentation is checked in the surface provenance suite.

### Invariants And Boundaries

These are declared component or pure-function checks over the fixtures named here. This read-only analysis did not execute the tests; jsdom or width stubs do not establish browser geometry.

## Evidence

- Declared check and its fixture assertions. [2]
- Declared check and its fixture assertions. [3]
- Declared check and its fixture assertions. [4]
- Declared check and its fixture assertions. [5]
- Declared check and its fixture assertions. [6]

## Historical predecessor account

The earlier account follows as provenance. Current assertions and removed journeys are described above.

> # dashboard/src/panels/review/SubjectJudgment.test.tsx
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
> Explicit synthetic component judgment rows/proofs preserve visible reasons/facets, attempts/coverage, history-unavailable proof display, missing-required-field failure, legacy family missing effect, and statement-side origin. Not native producer acceptance.
>
> ### Declared Assertions
>
> - `it('shows judgment rows and proofs without hiding their text in disclosures', () => {`
> - `it('keeps proofs visible when judgment history is unavailable', () => {`
> - `it('reports a missing current-build field as a failed read, not no judgment', () => {`
> - `it('names the missing effect of an older changed family row', () => {`
> - `it('shows each statement sides recorded origin, including its hand-off entry', () => {`
>
> This is a declaration inventory, not a collected parametrized-case total or execution result.
>
> ### Evidence Boundary
>
> The source declares these checks. This card does not attest that pytest/Vitest, a native host, a real browser or an installed producer ran on this candidate. Controlled or captured inputs qualify only the operations named above.
>
> ## Evidence
>
> - Explicit synthetic component judgment rows/proofs preserve visible reasons/facets, attempts/coverage, history-unavailable proof display, missing-required-field failure, legacy family missing effect, and statement-side origin. Not native producer acceptance. (historical reference 1)
