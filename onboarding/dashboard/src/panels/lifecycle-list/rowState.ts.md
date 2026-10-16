# dashboard/src/panels/lifecycle-list/rowState.ts

## Governing Overview

[Panels overview](../overview.md)

## Purpose

Pure presentation helpers for one Operations row: `rowBand`, `shortTaskId`, `progressFigure` and `rowHover`. Shared task-status words and age rendering belong to `detail-panel/pageParts`; this module does not render the row’s mark or status word.

## Code Commentary

rowBand orders works, started, planned, terminal; tree order breaks ties. pageParts owns shared status/age, never inferred lifecycle precedence. Hover contains title, unauthored-document notice, state/stage, repository, current step, progress and contributing host event when present, including abandoned/discarded counts; it does not display entry.scope or the full document-reference path. shortTaskId strips only the exact parent.id prefix; no gate/inbox/chat priority or runtime-id guessing.

## Evidence



- The hover explicitly selects its actual rendered fields; scope and full reference path are not among them. This corrects an earlier Curator wording overstatement, not product behavior. [1]
