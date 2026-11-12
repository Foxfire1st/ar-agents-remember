# dashboard/src/panels/review/top-line/ComparisonSelector.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

Render the review's numbered comparison menu, its delivered row and the change-set tray-pick control.

## Code Commentary

### Logic

The controlled menu lists every integer from latest down to 1, marks the shown number with its recorded time, and invokes onChoose only for a different number after closing. `DeliveredOption` is the menu's first row: it names the delivered pair and the number that holds it, marks `shown === resolved` — whether the page currently shows its own resolved default, which is not the same question as whether the delivered pair is the shown view (`aria-current` at `ComparisonSelector.tsx:157` and the `shown`/`default` span at `:162` both test that equality), and asks for the delivered action rather than choosing a number, so it leaves a recorded frame the target opened while a numbered row keeps that frame.

A recorded number is labelled `delivered` when its four trees are the delivered pair, `latest` when it is the highest record, and `read-only` otherwise, so a delivered pair held at a lower number is not called the latest record. The delivered row is offered only when the notice answers `delivered` or `differs`: an unestablishable delivery has no view to offer.

Only the shown comparison receives its recorded time, because the supplied answer does not list other comparisons' times. The comparison label and tray-add slot reserve width from first paint; a supplied pick renders AddToTray next to the label. The optional button ref also serves the status popover anchor.

### Invariants And Boundaries

It derives available number rows from the supplied latest number and the delivered value, and owns no comparison fetch, candidate resolution or recording operation.

## Evidence

- Reserved widths [1]
- Shown time, current row and latest/read-only labels [2]
- Descending menu, selection callback and tray pick [3]

- The delivered pair has its own row that asks for the delivered action, and a numbered row keeps the frame that action leaves. [4]
- A recorded number is labelled delivered, latest or read-only from the supplied delivered value and highest number. [5]
