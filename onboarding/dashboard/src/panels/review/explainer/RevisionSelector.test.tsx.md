# dashboard/src/panels/review/explainer/RevisionSelector.test.tsx

## Governing Overview

[Route overview](../../overview.md)

## Purpose

Measures the selector's rows, its agreement marking, when Compare is offered, and which revisions a refusal makes removable.

## Code Commentary

- The cases render the real selector over a fixed set of revisions and read each row's binding, kind, time and pin attributes.
- The task-total case presses removal and requires the offered choices to exclude the agreed revision and the press to carry only the ticked numbers.
- A per-revision refusal is required to offer no removal control and to say why, and a single retained revision is required to disable Compare.

## Evidence

- At the task total the refusal is named and only unpinned revisions are offered and reported [1]
- A per-revision refusal offers no control and states that removing others would not help [2]
- Compare is offered with two retained revisions, reports its press, and is disabled with one [3]
