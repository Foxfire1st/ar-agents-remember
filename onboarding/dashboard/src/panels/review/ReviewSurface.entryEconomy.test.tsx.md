# dashboard/src/panels/review/ReviewSurface.entryEconomy.test.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

Holds the reviewer to the request economy that makes the compact task entry pay off (leaf
`260921-ICR-L47`). The entry no longer reads the subject catalogue, so the reviewer opened from it carries
no subject; these cases pin what the reviewer then does: read the catalogue **once** on entry keyed on the
comparison, ask for the chosen subject rather than reading the whole task first, and — since L47-A2
(L47-R1-F1) — never withhold the task-context review for longer than `SUBJECT_HOLD_MS`.

## Current verification scope

The mounted 300 ms and 600 ms catalogue cases keep one catalogue read and one chosen-subject review request. The stalled catalogue still releases the bounded whole-task read; the new reuse branch is exercised by the navigation case rather than by extending this hold.

## Code Commentary

### Logic

- Fixtures come from the captured family review (`familyReview.complete.captured.json`): `CATALOGUE` lists
  its families; `familyReview(familyId, afterSnapshot)` returns that family's review under a chosen
  after-snapshot digest so a refresh can reach a "new candidate generation".
- **Economy case:** mounting `ReviewSurface` makes one catalogue read and no review read until it answers;
  then exactly one review read asks for the first family (`selectorKind=family`). Choosing another family
  reads that family and never the catalogue again; an unrelated analytics publication does not re-read it;
  a refresh that reaches different snapshot digests re-reads it once.
- **Stalled-catalogue case:** with a catalogue that never answers, a subjectless (task-context) review read
  happens within the bound and every source-inventory entry renders; the catalogue was requested once.

### Conventions

Only `fetch` is stubbed; requests are classified by URL path and query. The hold constant is imported from
`ReviewNavigation`, not duplicated.

### Invariants And Boundaries

- Restoring the four reviewer files to base fails the economy case (base reads the whole task first; worker
  event E6). Making the hold unbounded fails the stalled case (`l47-evidence/a2/f1-unbounded-hold-fails.txt`).
- It does not cover the late-catalogue jump and focus loss after the bound (review R2 observation O-R2-1),
  which belongs to L48.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation source is configured for this test module.

No relevant domain documentation was found.

### Repo-Internal References

- The economy the cases hold the reviewer to, including the bounded wait. [1]
- The catalogue fixture and the per-family review under a chosen snapshot. [2]
- One catalogue read, then only the chosen subject; re-read once for a new generation. [3]
- A stalled catalogue releases into the task-context review within the bound. [4]
- The hold and the comparison-keyed catalogue under test. [5]

### Cross-Repo References

No cross-repository behavior.

No meaningful cross-repo references found.


### Clock And Settlement Evidence

- Catalogue delays and the product hold run on the same fake clock. A stalled catalogue yields zero review reads at `SUBJECT_HOLD_MS - 1` and one task-context read at the next millisecond; answered catalogues remain at one chosen-subject read even after advancing past the hold. No wall-clock elapsed inequality establishes this economy. [6]
