# dashboard/src/panels/review/changeTriage.test.ts

## Governing Overview

[Owning route overview](overview.md)

## Purpose

Captured triage facts retain scoped counts, order and continuation merges while synthetic row-name controls keep selector keys out of displayed names.

## Code Commentary

### Logic

- The captured/synthetic triage cases preserve counts by returned primary kind, partial/unknown total wording, guarantee weight, sibling-preserving Priority/authored ordering and continuation unions with newer family facts.
- Two explicit synthetic catalogue/outline cases require a catalogue row's label as its displayed id while retaining selector_id as the key; an outline member missing from invariant rows uses its own supplied id, else the catalogue label.

### Invariants And Boundaries

These are declared component or pure-function checks over the fixtures named here. This read-only analysis did not execute the tests; jsdom or width stubs do not establish browser geometry.

## Evidence

- Declared check and its fixture assertions. [5]
- Declared check and its fixture assertions. [6]
- Declared check and its fixture assertions. [7]
- Declared check and its fixture assertions. [8]
- Declared check and its fixture assertions. [9]
- Declared check and its fixture assertions. [10]
- Declared check and its fixture assertions. [11]
- Declared check and its fixture assertions. [12]
- Declared check and its fixture assertions. [13]
- Declared check and its fixture assertions. [14]
- Declared check and its fixture assertions. [15]
- Declared check and its fixture assertions. [16]
- Declared check and its fixture assertions. [17]

## Historical predecessor account

The earlier account follows as provenance. Current assertions and removed journeys are described above.

> # dashboard/src/panels/review/changeTriage.test.ts
>
> ## Governing Overview
>
> [dashboard/src/panels route overview](overview.md)
>
> ## Purpose
>
> **The pure triage rules over the store-authored comparison's served bodies** (`triage.family`, `triage.familyPage`,
> `triage.familyContinued`, `triage.shared`; the world `mcp/tests/test_review_change_kinds.py` asserts the facts of). 11
> cases check that the tree orders, counts and merges the delivered facts and never decides one.
>
> ## Code Commentary
>
> ### Logic
>
> - **Family triage (5):** counts by delivered primary kind; a partial page scoped to its returned members with the total
>   named; a complete-looking family whose total is unknown scoped as "(total unknown)" and weighing at least `unknown`
>   (SYNTHETIC: no total; review R1 F2); a family weighed by its own revised guarantee (SYNTHETIC: every member
>   unchanged; mutation R-C3); the total said to be unknown rather than invented.
> - **Tree order (4):** changes first by weight then authored position, every sibling kept; pure authored order is the
>   family record's `members` list; families by their highest member or guarantee weight, then context order; a partial
>   family above a complete unchanged one (SYNTHETIC facts).
> - **Roster walk (2):** `mergeFamilyContinuation` keeps the facts of every member the walk returned (strengthened with a
>   SYNTHETIC gap after the walk-merge mutation first survived); two deliveries unioned with the newer family facts.
>
> ### Conventions
>
> Vitest over captured JSON read from the test's own directory; SYNTHETIC variations are labelled in the case names.
>
> ### Invariants And Boundaries
>
> Proves part of the candidate invariant recorded on `changeTriage.ts.md` (order never hides siblings; partial pages scoped).
>
> ### Todos
>
> No additional work is asserted by this card.
>
> ## Evidence
>
> ### Docs References
>
> No domain documentation source is configured; the requirement packet `MIK-R33@v1` (adopting `ICR-R32@v1`) and the architect's rulings in `33_review-triage-order-and-change-kind-badges.json` live outside the code and memory repositories, so they are named here and not cited as rows.
>
> No configured live documentation source was available for this pass.
>
> ### Repo-Internal References
>
> - The suite's statement and its bodies. (historical reference 1)
> - Family triage: counts, partial and scoped breakdowns, the guarantee's weight. (historical reference 2)
>
> ### Cross-Repo References
>
> No cross-repo boundary is crossed by this file.
>
> - Four tree-order declarations cover sibling-preserving change order, authored order, family weights and partial-family ordering. The dataset-review/no-change-facts case is absent from the candidate. (historical reference 3)
> - The two roster-walk cases retain returned member facts and union deliveries with newer family facts. (historical reference 4)
