# dashboard/src/explainer/ExplainerColumn.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

The review page's chat column as the leaf's explainer: it shows the explainer's chat or its placeholder, the first request's form, the build's progress and Retire's confirmation, all above one kept-mounted chat frame.

## Code Commentary

- By default, the column selects the leaf's explainer or its placeholder rather than the task's Worker. The task-scoped header menu also lists the task's other seats, and an explicit menu choice steers the retained frame to that selected seat.
- Opening reads the explainer's state once and posts nothing; a running build is re-read on a fixed cadence, and a model turn starts only from the developer's Send, from a message in the chat, or from a Regenerate with a live seat.
- The one frame stays mounted through every phase, hidden rather than unmounted, so switching phases or pages reloads neither the Paseo client nor the draft in progress.
- A failed read is said plainly with a Retry that reads again, a held first turn names its reason and detail, and neither starts anything.
- It draws state it does not own: the read and the calls live in the column's state hook, the blocks in the panels and the form, the styles in one stylesheet.

## Evidence

- The section publishes whether it shows the explainer or the placeholder [1]
- A Send aimed at an archived explainer opens the first-request form with the tray's picks instead of sending [2]
- The frame is kept mounted through every phase, so a phase switch never reloads it [3]
- The chrome orders the header, any unbound line, the read notice, the held notice, the phase's one block and Retire's receipt [4]
- A page may mount one block alone: the module re-exports the read and polling hooks, the panels, the form and the tray pick type [5]
