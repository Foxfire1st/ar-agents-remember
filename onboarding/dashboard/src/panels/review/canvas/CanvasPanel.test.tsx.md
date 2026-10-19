# dashboard/src/panels/review/canvas/CanvasPanel.test.tsx

## Governing Overview

[governing route overview](../../overview.md)

## Purpose

The panel's own regression suite: the saved-first read starts nothing, the explicit start runs once, the side conversation records its turn, and a moved comparison is not shown as the new one.

## Code Commentary

- The captured frame states (`frameState.comparison7.captured.json` and its siblings) are the fixtures the cases read, so the assertions run against recorded server answers.
- A comparison change case proves the panel re-reads instead of reinterpreting the old answer.
- The missing-assets case proves a page whose assets are absent is shown as such rather than as ready.

## Evidence

- A saved-first read starts nothing. [1]
- The explicit start is issued once. [2]
