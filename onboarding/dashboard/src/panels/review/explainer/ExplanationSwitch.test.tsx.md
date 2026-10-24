# dashboard/src/panels/review/explainer/ExplanationSwitch.test.tsx

## Governing Overview

[Route overview](../../overview.md)

## Purpose

Measures the switch's label and its switching: which view is reported as shown, what the build and stale marks read, and that no request is made.

## Code Commentary

- The cases render the real component and read its rendered text, its attributes and its `aria-selected` state.
- `fetch` is stubbed and required never to be called, so the claim that switching starts nothing is measured rather than assumed.
- A retired switch is pressed, and the label is required to say so while the press reports the explanation view.

## Evidence

- The two views are labelled and `aria-selected` reports which one is shown [1]
- A stale count and a build each reach the label, and no fetch is made [2]
- Pressing the explanation tab reports the switch, and a retired explainer is named in the label [3]
