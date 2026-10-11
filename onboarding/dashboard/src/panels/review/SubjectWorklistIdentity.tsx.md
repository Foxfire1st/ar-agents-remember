# dashboard/src/panels/review/SubjectWorklistIdentity.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

Join the reviewer's selected subject to its canonical worklist record through the outline: labels and revisions are display, never record keys.

## Code Commentary

- `canonicalWorklistRecord` resolves the subject's canonical record id from the outline's families or invariants by `selector_id`, returning undefined unless the outline is admitted.
- `SubjectKnowledge` renders the subject's `SubjectWorklistItems` for the review comparison once a comparison and a subject (or family) are known; otherwise it renders nothing.

## Evidence

- Canonical record joined by selector id [1]
- Per-subject worklist items for the comparison [2]
