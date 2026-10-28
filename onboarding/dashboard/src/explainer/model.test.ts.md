# dashboard/src/explainer/model.test.ts

## Governing Overview

[Route overview](../overview.md)

## Purpose

Specifies the column's pure rules without a DOM: the selection and status words, the placeholder, the form's target and refusal, the build's percentages, later references, Retire's lists and the header's menu.

## Code Commentary

- Each case calls a rule directly with a state and expects words or rows; nothing is rendered and nothing is fetched.
- The selection cases cover a live, closed, missing and building seat, an open form, and a state that could not be read.
- The build cases assert a counting step's own percentage, the equal-weighted whole, and that only a failed build names a failed step.
- The menu case excludes a seat in another repository or master folder even when its short id matches the task's.

## Evidence

- The placeholder is selected while no seat exists, never the Worker [1]
- Send is refused with nothing to send
- Only a failed build names the failed step and its reason [3]
- The menu filters by exact repository, master and task path [4]

- Retired at the fifth freeze d59c3493: dashboard/src/explainer/model.test.ts:145-150 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 5f8398b32760677c370e3145add73cfa8388357b. Retired means the anchor no longer stands, not that the cited subject was deleted.
