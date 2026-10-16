# dashboard/src/panels/detail-panel/pageParts.tsx

## Governing Overview

[Panels overview](../overview.md)

## Purpose

Provide the shared page-block, row, in-place text, status and progress presentation primitives used by all three document forms.

## Code Commentary

`DocView` enumerates own views; Block draws a heading/count only when composed. Shared TaskStatusKey maps served stage/activity to label and tone for task surfaces. TaskStatusWord uses activity only for a started entry, and its age display advances host-event age using the shared visible clock. Display time never decides stage or activity.

`Clip` renders Markdown in a single line with an accessible more/less control when measured overflow requires it. Without usable layout it falls back to a text-length threshold; an opened truncated summary is explicitly labelled a preview. It does not fetch content or claim the preview is a full string.

Expandable rows use `opensOn`: only a direct row Enter/Space toggles it, and a click on a nested link/button or a click ending text selection is not a request to open the row. This prevents following a register link from also changing row expansion. `StepMarks` shows individual marks up to twelve states, then switches to an aggregate progress bar. Its optional cached steps payload passes one matching major-step entry to each StepDot: with a payload, pointer rest can reveal step and nested-detail text without a request. Missing payload leaves a plain mark; populations above twelve use the aggregate bar without per-step tooltips. Callers own the alignment between states, steps and served counts.

## Boundaries

No document classification, authoritative step state, review count or task mutation is owned here. Whole-content retrieval and Back/scroll restoration belong to the reader/view layer. Presentation thresholds are not server collection limits.

## Evidence

- One-line Markdown can open in place and truthfully labels a remaining summary preview. [1]
- Link/button clicks and text selection do not trigger row expansion. [2]
- Keyboard expansion belongs to the row itself, not its nested controls. [3]

- StepMarks uses indexed cached StepDot payloads for at most twelve states; larger populations return only the aggregate ProgressBar. [4]
