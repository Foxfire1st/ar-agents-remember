# dashboard/src/panels/review/changeSetOrder.test-utils.ts

## Governing Overview

[Route overview](overview.md)

## Purpose

Supply explicitly captured card answers and named synthetic overlays to the change-set model tests.

## Code Commentary

### Logic

l181Answer/l104Answer load the two retained JSON responses. cardsOf requires a recorded comparison, while entry helpers return structured clones so one case cannot mutate the capture for another.

l181Outline names the one captured changed invariant and two explicitly synthetic unchanged neighbors. L104_ROWS preserves the investigator’s fifteen ids, selectors, change kinds and effect labels in listed order.

withMemory adds zero-default entry memory values with per-invariant overrides; withSymbol adds an explicitly named entry’s symbol. Both add fields that the original captures predate.

### Invariants And Boundaries

The generated outline rows and per-case memory/symbol values are test inputs, not fields newly observed in the retained response or live knowledge.

## Evidence

- Comparison-required cards, clones and explicit synthetic rows [1]
- Recorded subject-fact ordering [2]
- Explicit post-capture test overlays [3]
