# dashboard/src/panels/review/reading/ReviewPage.readerLine.test.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

Exercise reader-line retention through asynchronous review and diff changes.

## Code Commentary

### Logic

Uses a deterministic column layout and held requests to check that settled blocks remain within 1px as the subject slot answers or fails, cards and lane reads land, fractional corrections accumulate, and shrinking content would clamp scrolling. Cases preserve sticky-head clearance, reserve lane hunk rows, hold skeleton/body heights through the ready commit, and release spacer room when content or the kept line changes. Later cases cover replacing a kept node, retaining excerpt content and editor identity while marks arrive, fixed-height marks-state rows on the first scroll, and the selected slot's first-read skeleton.

### Invariants And Boundaries

Heights, scroll clamping, intersections, resize reports and request timing are simulated. The cases assert the modelled line and DOM/editor continuity; they are not a fresh browser paint or visual acceptance run. Editor-internal document-line anchoring has its own companion test file.

## Evidence

- Held subject/card reads retain the next settled block across success and failure. [4]
- Fractional/clamp corrections, sticky-head clearance, lane reservations and ready/skeleton height holds. [5]
- Node replacement, vanished/surviving-line spacers, excerpt/marks continuity and selected-slot skeleton. [6]
