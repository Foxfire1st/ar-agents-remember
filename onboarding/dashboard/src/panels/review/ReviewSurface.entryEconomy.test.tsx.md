# dashboard/src/panels/review/ReviewSurface.entryEconomy.test.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/ReviewSurface.entryEconomy.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-28T17:06:50+02:00 |
| lastVerifiedCommitHash | `e66f1f3894116e0bb37b49f178d8bfcb130a7e28` |
| lastVerifiedCommitDate | 2026-09-28T20:02:47+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

Holds the reviewer to the request economy that makes the compact task entry pay off (leaf
`260921-ICR-L47`). The entry no longer reads the subject catalogue, so the reviewer opened from it carries
no subject; these cases pin what the reviewer then does: read the catalogue **once** on entry keyed on the
comparison, ask for the chosen subject rather than reading the whole task first, and — since L47-A2
(L47-R1-F1) — never withhold the task-context review for longer than `SUBJECT_HOLD_MS`.

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

## Docs References

No Domain Documentation source is configured for this test module.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant domain documentation was found. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The economy the cases hold the reviewer to, including the bounded wait. | "the wait for the catalogue is bounded" | dashboard/src/panels/review/ReviewSurface.entryEconomy.test.tsx:1-12 |
| The catalogue fixture and the per-family review under a chosen snapshot. | `CATALOGUE`; `familyReview` | dashboard/src/panels/review/ReviewSurface.entryEconomy.test.tsx:39-68 |
| One catalogue read, then only the chosen subject; re-read once for a new generation. | "reads the catalogue once on entry, then asks the review only for the subject it chose" | dashboard/src/panels/review/ReviewSurface.entryEconomy.test.tsx:70-140 |
| A stalled catalogue releases into the task-context review within the bound. | "reads the task-context review and shows the source explorer when the catalogue never answers"; `SUBJECT_HOLD_MS` | dashboard/src/panels/review/ReviewSurface.entryEconomy.test.tsx:142-176 |
| The hold and the comparison-keyed catalogue under test. | `SUBJECT_HOLD_MS`; `useReviewNavigation` | dashboard/src/panels/review/ReviewNavigation.tsx:146-199 |

## Cross-Repo References

No cross-repository behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-28T17:06:50+02:00 — 260921-ICR-L47 curator (uncommitted candidate tree `72efa4bbc169b16afe8ef249499edf79cad9940d` over code base `58e22246cc09ef0ee12095e284a111a475081c38`): created this card for the reviewer entry-economy cases (A1) and the bounded-hold case (A2, L47-R1-F1). The verification pair names the code base; closeout owns the real stamp.
