# dashboard/src/panels/review/DeliveredComparison.test.tsx

## Governing Overview

[Owning route overview](../../../../overview.md)

## Purpose

Measure the landed leaf's delivered pair on the page: the one line a comparison that is not the delivered pair states, its link to the delivered view, the delivered identities in Technical details, and the comparison menu's delivered row.

## Code Commentary

The module renders `DeliveredLine`, `DeliveredFacts` and `ComparisonSelector` directly with a supplied delivered value, so it measures those parts without a server or a mounted page.

Four cases: the mismatch is stated once and its control asks for the delivered view; a matching pair shows no line and an unavailable delivery offers no delivered control; the delivered identities appear in the technical details; and the menu carries the delivered row — which asks for the delivered action rather than choosing a number — while marking which recorded number holds that pair and which number is the highest record.

The supplied statement is the resolver's own sentence shape: it names the shown number and the delivered trees and passes no verdict about the earlier record.

## Invariants And Boundaries

The cases measure presentation and the reader's own control. They assert nothing about which pair was reviewed, and the fixture's identities are literals rather than a delivery any repository records.

## Evidence

- The mismatch is stated once and its control asks for the delivered view. [1]
- A matching pair states no line, and an unavailable delivery offers no delivered control. [2]
- The delivered identities are listed in the page's technical details. [3]
- The menu carries the delivered row, which asks for the delivered action, and marks the number that holds the pair. [4]
