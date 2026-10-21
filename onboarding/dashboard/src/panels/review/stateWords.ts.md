# dashboard/src/panels/review/stateWords.ts

## Governing Overview

[Route overview](overview.md)

## Purpose

Translate review response state/count tokens into reader-facing words while preserving tokens for data attributes.

## Code Commentary

### Logic

familyStateWords supplies explicit phrases for recorded, partial, no-family, no-subject and unavailable family context.

remainingWords names the four known source-pane remainder quantities. Unknown tokens pass through tokenWords, which replaces underscores with spaces.

### Invariants And Boundaries

These functions change wording only; they do not infer counts, classify states or turn unmeasured facts into zero.

## Evidence

- Family-context vocabulary [1]
- Remainder wording and generic token spelling [2]
