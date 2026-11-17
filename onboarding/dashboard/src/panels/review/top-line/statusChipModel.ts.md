# dashboard/src/panels/review/top-line/statusChipModel.ts

## Governing Overview

[Route overview](../overview.md)

## Purpose

Compose the status chip’s label, tone and four rows from the review owners’ movement and staleness measurements.

## Code Commentary

### Logic

chipFacts always builds rows for Sync movement, External Git movement, Subject staleness and Bound comparison. A leaf the task list reports as planning returns the grey planned chip with the reason that nothing is built yet, before the reading and failure branches; otherwise loading takes the reading state, and a supplied failure takes unavailable with the first sentence of its detail.

Measured branch movement takes warning precedence, followed by stale comparison, unavailable movement, both movements current, then not measured. Explanations remain the first sentence of an owner’s reason/statement.

localTime formats a valid instant in the reader’s local time at minute precision, omits the current year and retains another year. Invalid time is returned verbatim. The comparison row names the shown number/time and separately states an older number’s latest/read-only relation.

### Invariants And Boundaries

It reads no clock and measures no Git state; callers supply now, the admitted payload, comparison and latest number. Neither missing nor partially measured movement becomes current.

## Evidence

- State wording, explicit measurement absence and supplied-date time formatting [1]
- Warning/measurement precedence and owner prose [2]

- The four rows are built first; a planning leaf returns the planned chip before loading and failure, and otherwise loading or failure chooses the state. [3]
