# dashboard/src/panels/review/canvas/canvasModel.ts

## Governing Overview

[governing route overview](../../overview.md)

## Purpose

The panel's display model: which phase the saved state and the live attempt put the panel in, and which comparison and entrypoint a saved page belongs to.

## Code Commentary

- `panelPhase` derives the phase from the recorded state and any live attempt, so a page with a running attempt shows the build rather than an empty frame.
- `comparisonNumberOf` and `savedComparison` keep a saved page tied to the comparison number it was published against.
- `savedEntrypoint` names the file a saved page loads, so the panel never guesses an entrypoint.

## Evidence

- The phase is derived from the recorded state and the live attempt. [1]
- A saved page keeps its own comparison number and entrypoint. [2]
