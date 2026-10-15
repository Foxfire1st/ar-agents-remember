# dashboard/src/panels/detail-panel/decisionPreview.test.tsx

## Governing Overview

[panels overview](../overview.md)

## Purpose

Unit assertions for the decision-log preview: five authored decisions have no link; seven authored decisions show the newest five with an `all 7 decisions` link. Product records stay out of authored row numbering and link counts (`#2`/`#1`, `all 2 decisions`, and `all 1 decision`). Unsorted input and a fabricated legacy finalizer-shaped sample retain recorded-time ordering coverage.

## Code Commentary

Six mounted cases declare the preview contract: five/no-link boundary, newest-first recorded time rather than array tail, authored-only numbering/counts, and a link when only product records are omitted. This suite mounts DecisionPreview only. Its finalizer-shaped input is a hand-built legacy sample; it does not exercise or establish the current writer, which no longer adds a decision. The whole-log reader instead keeps product records behind a collapsed muted disclosure at the end (see that reader suite). The historical account of three time-order cases failing an array-order mutation is not a fresh mutation run or current acceptance result.

## Evidence

- Five authored decisions omit the link; seven show five with all 7 decisions and forward the complete original array. [1]
- Unsorted preview input selects newest authored decisions by recorded time, not the array tail; legacy finalizer-shaped input is fabricated. [2]
- Product records do not contribute to #2/#1 authored numbering or all 2/all 1 decision link counts. [3]
