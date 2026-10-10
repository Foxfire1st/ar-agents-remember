# dashboard/src/panels/detail-panel/decisionPreview.test.tsx

## Governing Overview

[panels overview](../overview.md)

## Purpose

Unit tests for the decision-log preview: six entries show five with a link, five show five with no link, the five newest come first by recorded time from an unsorted log, product-written records are excluded with both counts named, and finalizer-shaped input is ordered correctly.

## Code Commentary

Six mounted cases pin the preview contract from rule 6: the five/​no-link boundary, newest-first time order (not array tail), product-record exclusion including the lifecycle-only-omitted link, and finalizer-shaped input ordered by its parsed time within the preview. The suite mounts DecisionPreview only and omits the product record; it never mounts the whole-log page (the reader's whole log puts the newest finalizer record first, muted — see the reader suite). Three time-order cases fail on an array-order revert, so the suite guards the ordering helper rather than the fixture order.

## Evidence

- Five entries show five with no link; six show five with a link. [1]
- The newest five come first by recorded time from an unsorted log. [2]
- Product-written records are excluded and both counts are named. [3]
