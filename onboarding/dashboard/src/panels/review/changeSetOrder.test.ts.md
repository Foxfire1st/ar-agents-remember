# dashboard/src/panels/review/changeSetOrder.test.ts

## Governing Overview

[Route overview](overview.md)

## Purpose

Specify deterministic change-set ordering, grouping, counts and filtering over captured card reads with named synthetic overlays.

## Code Commentary

### Logic

L181 cases assert 15 changed/31 unchanged/28 not-comparable entries, role/span order, exact identities, line counts and one drawn row/card per shared region while counts remain by entry.

L104 cases pin Priority/Authored/currentness and four memory-sort sequences, unavailable-sort reasons and retained choice. Named synthetic currentness covers unrealized subjects without entries and tie-breaking by the state actually shown.

Family cases pin nesting, shared tree/column sequence and one first rendered occurrence for a multi-family invariant. Changed/All preserves explicit unchanged selection, pending counts and no-meaning-change state; filters cover all supported fields and folded groups without narrowing the model itself.

### Invariants And Boundaries

Captures and synthetic overlay inputs are distinguished in the source.

## Evidence

- Entries, line counts and shared-region drawing [1]
- Sorts, currentness, availability and family placement [2]
- View/selection/pending/filter/folded-group contracts [3]
