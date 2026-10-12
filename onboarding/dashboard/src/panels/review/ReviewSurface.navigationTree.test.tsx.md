# dashboard/src/panels/review/ReviewSurface.navigationTree.test.tsx

## Governing Overview

[dashboard/src/panels overview](../../overview.md)

## Purpose

The whole mounted R86 surface replays the leaf-built L37 responses with fetch replaced. Four cases assert first-change selection, Changed/All row population and tooltips/filtering without disclosures, existing comparison-viewer filters and return state, open worklist state, and in-card Full file without a changeset request. They do not assert rendered markers on that unchanged Full-file payload.

## Code Commentary

The first case derives initial selection and summary expectations through the triage helpers, checks 116 All-view DOM rows with nonempty titles, narrows them by filtering without another request and checks disclosure categories. It measures neither row height nor single-line geometry. The viewer case checks comparison-5 request selectors, presses `j` only and checks the unchanged selected row, then asserts Back restores trigger focus and assigned scroll state without another read; it does not press `k`. The worklist case preserves the selected subject with no patch node. The card case opens the Full-file host and asserts no viewer/changeset request; it does not assert hunk markers.

## Evidence

- Stored view and order reset for each case [1]

- Disclosure contract for every mounted view [2]
- First-change derivation from the captured outline [3]

- Changed and All counts from the captured outline [4]
