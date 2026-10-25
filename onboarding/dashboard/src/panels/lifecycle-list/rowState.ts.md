# dashboard/src/panels/lifecycle-list/rowState.ts

## Governing Overview

[Panels overview](../overview.md)

## Purpose

Pure presentation helpers for one Operations row: `rowBand`, `shortTaskId`, `progressFigure` and `rowHover`. Shared task-status words and age rendering belong to `detail-panel/pageParts`; this module does not render the row’s mark or status word.

## Code Commentary

rowBand orders works, started, planned, terminal; tree order breaks ties, except inside the started band, where the rows the host timed order newest first by their host event time and the rows it did not time keep the server's order (MIK-R174). pageParts owns shared status/age, never inferred lifecycle precedence. Hover contains title, unauthored-document notice, state/stage, repository, current step, progress and contributing host event when present, including abandoned/discarded counts; it does not display entry.scope or the full document-reference path. shortTaskId strips only the exact parent.id prefix; no gate/inbox/chat priority or runtime-id guessing.

MIK-R174 adds `rowOrder` and `hostTime`: inside the started band the rows the host timed order newest first and the rows it did not time keep the server's order; `hostTime` returns null for a missing or unparsable `eventAt`, so no row's time is invented as zero or as now. Every other band keeps the server's order, and a time still orders nothing in the shown figure.


**L184 — INV-7GVWYD.** This module builds the row's reading, so the one-reading claim is realized here. The obligation this leaf records for this place is stated in the invariant named here; the card's earlier account of this file stands, and this paragraph adds what the change made true.

## Evidence

- A missing host time orders nothing and is never turned into zero or now. [2]
- The started band orders timed rows newest first, untimed rows in the server's order. [3]


- The hover explicitly selects its actual rendered fields; scope and full reference path are not among them. This corrects an earlier Curator wording overstatement, not product behavior. [1]
