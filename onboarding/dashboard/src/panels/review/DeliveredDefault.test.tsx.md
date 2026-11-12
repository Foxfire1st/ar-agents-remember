# dashboard/src/panels/review/DeliveredDefault.test.tsx

## Governing Overview

[Owning route overview](../../../../overview.md)

## Purpose

Measure the landed leaf's reviewed page: it opens what the leaf delivered, the delivered link and the menu's delivered row leave the frame the task entry opened, and a notice read that fails says so.

## Code Commentary

The module renders the real page over the repository's captured page fixture and answers through a stubbed transport. `fixture` makes the task context name #7 by default and #8 when the read asks for the recorded comparison, and adds the delivered notice to the leaf-wide trees read: `delivered` for #7, `differs` for any other number. #7 is the exact delivered record and #8 the later history, so a page that opens the highest number opens the wrong pair.

Five cases: a default frame opens the older delivered #7 and states no line; the delivered link leaves the recorded frame the task entry opened and reaches #7; the menu's delivered row leaves that recorded frame too; a numbered row keeps the frame the delivered row leaves; and a refused leaf-wide read becomes the explicit unavailable line rather than silence.

## Invariants And Boundaries

The cases measure the page's own defaults and its notice read. They do not claim a delivery was reviewed, and the refused case supplies a typed refusal rather than a real repository failure.

## Evidence

- A default frame opens the older delivered comparison and states no line. [1]
- The delivered link leaves the recorded frame the task entry opened. [2]
- A refused notice-bearing read stays explicitly unavailable on the page. [3]
