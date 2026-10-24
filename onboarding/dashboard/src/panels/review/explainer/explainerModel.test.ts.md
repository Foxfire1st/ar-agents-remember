# dashboard/src/panels/review/explainer/explainerModel.test.ts

## Governing Overview

[Route overview](../../overview.md)

## Purpose

Measures the page's pure decisions directly: labels, pinning, the removal offer, the phase, and the default compare pair.

## Code Commentary

- The cases call the pure functions with hand-built states and revision rows and assert the exact strings the page shows.
- Removal is measured against the pinned revision and against an already removed one, so both exclusions are proven rather than assumed.
- The compare default is required to pair the shown revision with the newest other retained one, and to answer nothing below two.

## Evidence

- A planned binding reads planned and never a number [1]
- The pinned revision is never removable, and a removed revision is not offered again [2]
- Removal is offered by the task total and by no other refusal [3]
- The default pair takes the shown revision and the newest other, and nothing with one revision [4]
