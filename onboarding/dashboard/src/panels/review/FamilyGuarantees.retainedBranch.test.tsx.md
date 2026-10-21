# dashboard/src/panels/review/FamilyGuarantees.retainedBranch.test.tsx

## Governing Overview

[Owning route overview](overview.md)

## Purpose

Synthetic component controls distinguish same revision from identical wording and keep changed guarantee panes sized to content.

## Code Commentary

### Logic

- A derived next revision with identical guarantee wording renders one after-side guarantee, a compact wording-unchanged label and closed raw-record details containing both revisions; the raw same-revision capture remains unchanged_revision.
- The changed-guarantee case mounts an empty fit DiffPane as the class reference, then compares the actual changed guarantee pane class to it (draws a changed guarantee in a fit diff pane).

### Invariants And Boundaries

These are declared component or pure-function checks over the fixtures named here. This read-only analysis did not execute the tests; jsdom or width stubs do not establish browser geometry.

## Evidence

- Declared check and its fixture assertions. [2]
- Declared check and its fixture assertions. [3]
- Declared check and its fixture assertions. [4]

## Historical predecessor account

The earlier account follows as provenance. Current assertions and removed journeys are described above.

> # dashboard/src/panels/review/FamilyGuarantees.retainedBranch.test.tsx
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
> Deliberately synthetic equal-wording/distinct-revision control retains identical_text branch for both TreeComparisonScope values; independently uses raw same-revision capture as unchanged_revision. Do not fabricate a native metadata-only capture or treat tree=false here as a surviving dataset transport.
>
> ### Declared Assertions
>
> - `it.each([false, true])('keeps distinct family revisions with equal wording distinct (tree=%s)', (tree) => {`
> - `it('retains the current raw same-revision control as unchanged revision, not identical-text', () => {`
>
> This is a declaration inventory, not a collected parametrized-case total or execution result.
>
> ### Evidence Boundary
>
> The source declares these checks. This card does not attest that pytest/Vitest, a native host, a real browser or an installed producer ran on this candidate. Controlled or captured inputs qualify only the operations named above.
>
> ## Evidence
>
> - Deliberately synthetic equal-wording/distinct-revision control retains identical_text branch for both TreeComparisonScope values; independently uses raw same-revision capture as unchanged_revision. Do not fabricate a native metadata-only capture or treat tree=false here as a surviving dataset transport. (historical reference 1)
