# dashboard/src/panels/review/explainer/MovedNotice.tsx

## Governing Overview

[Route overview](../../overview.md)

## Purpose

States that the leaf moved past the explanation's binding and offers the developer's Update press, or says plainly that no explainer has worked here so the view renewed itself.

## Code Commentary

- Two shapes reach it — the page's moved model and the watcher's published notice — and both render one notice; when the watcher's line came with its own text, that exact line is shown.
- Update is offered for a master move, or when a page or a grade exists to update; a recorded move with no work renders the renewed sentence and no control.
- The notice says the watcher saw the move and the explainer was not woken; it starts nothing itself and only calls the press it was handed.
- While a press is in flight the control reads Updating… and is disabled, so a second press cannot double the work; the counts, or the named failure, then replace it.
- Build steps and percentages are deliberately absent: those belong to the chat column.

## Evidence

- One notice is built from either the page model or the watcher's record, with the offer decided from the same answer [1]
- The published line is shown as published, and a derived line is used only when no text came with the notice [2]
- Update is offered for a master move or for a leaf that has work to update [3]
- With no offer the notice says the view renewed itself; with one it draws a control that cannot be pressed twice [4]
- The notice carries its own moved or no-explainer state, the line, an in-flight press and the press's counts or failure [5]
