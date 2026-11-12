# dashboard/src/explainer/ExplainerTaskDocument.test.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

Specifies Retire on the leaf task document: a cold document reads the state, shows nothing without an explainer, retires without visiting the review page, and keeps recovery open while processes remain.

## Code Commentary

- A cold document reads the leaf's state on mount and renders nothing when the leaf has no explainer, with no post.
- Retiring from a cold document posts once with a receipt id, shows the receipt, and the control stops offering Retire afterwards.
- A half-finished retirement names the pids that remain, keeps the confirmation open, and a retry reuses the same receipt id until no process remains.

## Evidence

- A cold document reads the state and shows nothing without an explainer [1]
- Retire works from a cold document without the review page and posts a receipt id [2]
- A remainder keeps the confirmation open and the retry keeps the receipt id [3]
