# dashboard/src/panels/review/canvas/CanvasPanel.test.tsx

## Governing Overview

[Owning route overview](../overview.md)

## Purpose

Canvas controls preserve saved-first and explicit-generation behavior, sandboxed display and scope-bound evidence delivery.

## Code Commentary

### Logic

- The suite covers saved artifacts before generation, explicit generate/regenerate and stale revisions, missing-asset recovery, the iframe sandbox declarations and approved host scripts.
- Captured-evidence messages retain their exact destination and channel. Scope rotation, late frame loads and late allocations cannot revive the old scope, and the retained comparison supplies the frame context.
- The oversized-message burst control now follows the burst with one small INV-2 reference and waits for that positive listener effect. Only INV-2 reaches evidence delivery; the oversized requests produce none. This replaces a fixed 60 ms settlement delay.

### Invariants And Boundaries

Declared component and postMessage checks use synthetic events and the iframe attributes. This read-only analysis did not execute them, load a browser frame or establish a live host-script result.

## Evidence

- Declared check and its fixture assertions. [3]
- Declared check and its fixture assertions. [4]
- Declared check and its fixture assertions. [5]
- Declared check and its fixture assertions. [6]
- Declared check and its fixture assertions. [7]
- Declared check and its fixture assertions. [8]
- Declared check and its fixture assertions. [9]
- Declared check and its fixture assertions. [10]
- Declared check and its fixture assertions. [11]
- Declared check and its fixture assertions. [12]
- Declared check and its fixture assertions. [13]
- Declared check and its fixture assertions. [14]
- Declared check and its fixture assertions. [15]
- Declared check and its fixture assertions. [16]
- Declared check and its fixture assertions. [17]
- Declared check and its fixture assertions. [18]
- Declared check and its fixture assertions. [19]
- Declared check and its fixture assertions. [20]
- Declared check and its fixture assertions. [21]
- Declared check and its fixture assertions. [22]
- Declared check and its fixture assertions. [23]
- Declared check and its fixture assertions. [24]
- Declared check and its fixture assertions. [25]
- Declared check and its fixture assertions. [26]
- Declared check and its fixture assertions. [27]
- Declared check and its fixture assertions. [28]
- Declared check and its fixture assertions. [29]

## Historical predecessor account

The earlier account follows as provenance. Current assertions and removed journeys are described above.

> # dashboard/src/panels/review/canvas/CanvasPanel.test.tsx
>
> ## Governing Overview
>
> [governing route overview](../../overview.md)
>
> ## Purpose
>
> The panel's own regression suite: the saved-first read starts nothing, the explicit start runs once, the side conversation records its turn, and a moved comparison is not shown as the new one.
>
> ## Code Commentary
>
> - The captured frame states (`frameState.comparison7.captured.json` and its siblings) are the fixtures the cases read, so the assertions run against recorded server answers.
> - A comparison change case proves the panel re-reads instead of reinterpreting the old answer.
> - The missing-assets case proves a page whose assets are absent is shown as such rather than as ready.
>
> ## Evidence
>
> - A saved-first read starts nothing. (historical reference 1)
> - The explicit start is issued once. (historical reference 2)
