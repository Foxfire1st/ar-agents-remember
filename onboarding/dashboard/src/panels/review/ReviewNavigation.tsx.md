# ReviewNavigation.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/ReviewNavigation.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-28T17:09:38+02:00 |
| lastVerifiedCommitHash | `e66f1f3894116e0bb37b49f178d8bfcb130a7e28`|
| lastVerifiedCommitDate | 2026-09-28T20:02:47+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[overview.md](../overview.md)

## Purpose

Navigate all recorded families and invariants from inside the review workspace, using the reviewer's own
catalogue read. Since `260921-ICR-L47` (`ICR-R24@v3`) this is where the catalogue is read — once, when the
reviewer opens — because the task entry no longer reads it; and the navigation also tells the surface when
its first review read may start.

## Code Commentary

### Logic

`useReviewNavigation(target)` preserves an explicit subject from the incoming target. Otherwise it chooses
the first recorded family, then the first available invariant (`initialSubject`). A deliberate All source
changes choice remains source-only when the catalogue refreshes. `CatalogueFamilies` substitutes the loaded
family subtree once among the remaining recorded family buttons; all invariant subjects stay reachable in
their disclosure. Refusal details remain available and do not fabricate an empty family.

**Catalogue key (L47).** It calls `useReviewCatalogue({ repo, master, leaf, history, generation })`; it no
longer reads the dashboard store's analytics document. `observeComparison(snapshots)` records the first
compared snapshot pair reported under this task context and record, and bumps `generation` (re-reading the
catalogue once) only when a later pair differs — a refresh that reached a new candidate generation.
`useObservedComparison(observeComparison, shown)` is the surface-side hook that reports
`before_snapshot_digest:after_snapshot_digest` when knowledge was compared.

**Bounded first-read hold (L47, fixed for L47-R1-F1).** `settling` is true while the reviewer was opened
with no subject, the catalogue has not answered, and `SUBJECT_HOLD_MS` (750 ms) has not passed. The surface
holds its first review read while `settling`, so a prompt catalogue costs one subject read instead of a
whole-task read followed by a subject read. When the bound expires, the task-context review is read (as for
a refused catalogue); the first subject is still selected if the catalogue answers later.

### Conventions

Uses the existing owner interfaces and exact recorded identities; keeps transient task evidence outside
durable onboarding. The navigation's public shape is the `ReviewNavigation` interface (the state plus
`settling` and `observeComparison`); the component of the same name renders the rail.

### Invariants And Boundaries

Catalogue identity and comparison-specific family content have different owners. Loading, unreadable,
confirmed empty and explicit source-only selection remain distinct. The hold never withholds the
task-context review and source explorer beyond the bound. This module authors no knowledge or assessment.
A catalogue answering after the bound moves the reader to the first family and drops focus (review R2
observation O-R2-1); that remount is owned by L48 and is not settled behaviour here.

### Todos

No additional work is asserted by this card.

## Docs References

No Domain Documentation source is configured. The implementation-specific account is grounded in the repository source below.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain source could be checked. | — | — |

## Repo-Internal References

The named constructs own this behavior; reads and validation use their existing callers and models.

| Finding | Anchor | Source |
| --- | --- | --- |
| The navigation shape with the two read-cycle signals. | `ReviewNavigation`; `settling`; `observeComparison` | dashboard/src/panels/review/ReviewNavigation.tsx:20-31 |
| The hold bound and why it exists. | `SUBJECT_HOLD_MS` | dashboard/src/panels/review/ReviewNavigation.tsx:142-146 |
| Subject choice, the comparison-keyed catalogue, the expiring hold and the generation bump. | `useReviewNavigation`; `useReviewCatalogue`; `setExpired`; `setGeneration` | dashboard/src/panels/review/ReviewNavigation.tsx:149-199 |
| The surface-side snapshot report. | `useObservedComparison`; `knowledge_compared` | dashboard/src/panels/review/ReviewNavigation.tsx:202-211 |
| `initialSubject` owns the default subject choice. | `initialSubject` | dashboard/src/panels/review/ReviewNavigation.tsx:220-228 |
| The rail component. | `ReviewNavigation` | dashboard/src/panels/review/ReviewNavigation.tsx:83-140 |
| `CatalogueFamilies` owns the family rail. | `CatalogueFamilies` | dashboard/src/panels/review/ReviewNavigation.tsx:230-263 |
| The surface wires both signals. | `hold: navigation.settling`; `useObservedComparison` | dashboard/src/panels/review/ReviewSurface.tsx:810-834 |

## Cross-Repo References

No independent cross-repository interface is introduced by this source.

| Finding | Anchor | Source |
| --- | --- | --- |
| No additional cross-repository evidence is required. | — | — |

## Update History

- 2026-09-28T17:09:38+02:00 — 260921-ICR-L47 curator (uncommitted candidate tree `72efa4bbc169b16afe8ef249499edf79cad9940d` over code base `58e22246cc09ef0ee12095e284a111a475081c38`): **body update — the reviewer owns its catalogue read, keyed on the comparison, with a bounded first-read hold (`ICR-R24@v3`; L47-R1-F1).** The claim "`useReviewNavigation` owns the behavior" was re-read against the changed hook: it no longer reads analytics, returns `settling` and `observeComparison`, and `SUBJECT_HOLD_MS = 750` bounds the hold. Logic, Conventions and Invariants were extended; reference rows re-derived. No stamp advanced; closeout owns the real stamp.

- 2026-09-26T19:49:05Z — Created the in-review catalogue navigation card.
