# dashboard/src/explainer/model.ts

## Governing Overview

[Route overview](../overview.md)

## Purpose

The explainer column's pure rules: which chat the column selects, the placeholder's words, the form's target and references, the build's steps and percentages, Retire's two lists and the header's menu.

## Code Commentary

- No network, no storage and no DOM: each function takes the state it needs and returns the words or rows to draw.
- The phase comes from the state alone — a running build wins, then an open form, then live, closed, retired or placeholder — and a placeholder, first-request or retired phase selects the placeholder.
- Send is always available: an empty request is the end-to-end review, or on a planning task the requirement and planned effects, and the form's line counts exactly what will go.
- A build's percentage weights each step equally, a counting step contributing its own ratio, and only a failed build names a failed step and reason.
- The agent menu keeps the explainer first and adds the task's other seats only when repository, master folder and task path match exactly.
- On a planned task the first-request line names the task's requirement and its planned effects, from the same constant the backend composes.

## Evidence

- A live, closed, missing or building seat selects the explainer, and no seat selects the placeholder [1]
- A running build takes precedence over an open form [2]

- Send is always available, and an empty request names the end-to-end review or, on a planning task, the requirement and planned effects. [3]
- A planned task's empty request line names its requirement and planned effects. [7]

- A build's steps average into its whole percentage [4]
- Only a failed build names a failed step and a reason [5]
- The menu holds the explainer first and excludes another task's, another repository's and another master's seats [6]


