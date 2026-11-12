# dashboard/src/panels/review/reading/SubjectSection.rule.test.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

Pin where the reading-column separator rule is declared.

## Code Commentary

### Logic

Opens All view over the composed three-subject fixture and checks the first subject has no data-ruled mark while the next two do. It verifies the shared subject style declares a 1px grid-coloured top border and 1rem margin under that mark, and that the lane follows a subjects-drawn container with the corresponding conditional rule classes.

### Invariants And Boundaries

jsdom has no CSS cascade. The case checks conditional marks, DOM adjacency and rule declarations, not the visible border or spacing.

## Evidence

- Separator marks/classes occur between subjects and before the lane, not above the first subject. [2]
