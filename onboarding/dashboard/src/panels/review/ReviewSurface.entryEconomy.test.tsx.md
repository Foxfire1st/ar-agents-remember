# dashboard/src/panels/review/ReviewSurface.entryEconomy.test.tsx

## Governing Overview

[Owning route overview](overview.md)

## Purpose

Catalogue timing never delays the opening task-context review or silently chooses a subject.

## Code Commentary

### Logic

- The first case holds the catalogue, sees one subjectless review immediately, then releases a late catalogue that populates family rows without selecting one or issuing a subject read.
- An unrelated analytics publication keeps the one catalogue read. Explicitly selecting each family reads only that family review; a refresh with a deliberately changed snapshot digest causes exactly one additional catalogue read.
- A catalogue that never settles still leaves the task-context scope and tree-owned All changes reachable, with no source explorer.

### Invariants And Boundaries

These are declared component or pure-function checks over the fixtures named here. This read-only analysis did not execute the tests; jsdom or width stubs do not establish browser geometry.

## Evidence

- Declared check and its fixture assertions. [11]
- Declared check and its fixture assertions. [12]

## Historical predecessor account

The earlier account follows as provenance. Current assertions and removed journeys are described above.

> # dashboard/src/panels/review/ReviewSurface.entryEconomy.test.tsx
>
> ## Governing Overview
>
> [dashboard/src/panels route overview](overview.md)
>
> ## Purpose
>
> Holds the reviewer to the request economy that makes the compact task entry pay off (leaf
> `260921-ICR-L47`). The entry no longer reads the subject catalogue, so the reviewer opened from it carries
> no subject; these cases pin what the reviewer then does: read the catalogue **once** on entry keyed on the
> comparison, ask for the chosen subject rather than reading the whole task first, and — since L47-A2
> (L47-R1-F1) — never withhold the task-context review for longer than `SUBJECT_HOLD_MS`.
>
> ## Current verification scope
>
> The mounted 300 ms and 600 ms catalogue cases keep one catalogue read and one chosen-subject review request. The stalled catalogue still releases the bounded whole-task read; the new reuse branch is exercised by the navigation case rather than by extending this hold.
>
> ## Code Commentary
>
> ### Logic
>
> - Two independent captured family-selector answers, `subjectReview.successorFamily.captured.json` and
>   `l86.family.captured.json`, supply the families used to assemble `CATALOGUE`; `l86.task.captured.json`
>   supplies task context. `familyReview(familyId, afterSnapshot)` selects the matching family capture or
>   the task capture for null selection, refuses unknown family IDs, and only perturbs the comparison's
>   after-snapshot digest for a new candidate generation. Other routes use the shared `replyFor` dispatcher,
>   except the explicitly stubbed catalogue and source-content routes.
> - **Economy case:** mounting `ReviewSurface` makes one catalogue read and no review read until it answers;
>   then exactly one review read asks for the first family (`selectorKind=family`). Choosing another family
>   reads that family and never the catalogue again; an unrelated analytics publication does not re-read it;
>   a refresh that reaches different snapshot digests re-reads it once.
> - **Stalled-catalogue case:** on a fake clock, no review read occurs at `SUBJECT_HOLD_MS - 1`; at the next millisecond one subjectless task-context review is read. The rendered scope reports the captured changed-file count, the catalogue is requested once, All changes remains reachable, and no source explorer is mounted. No assertion renders every inventory entry.
>
> ### Conventions
>
> Only `fetch` is stubbed; requests are classified by URL path and query. The hold constant is imported from
> `ReviewNavigation`, not duplicated.
>
> ### Invariants And Boundaries
>
> - Restoring the four reviewer files to base fails the economy case (base reads the whole task first; worker
>   event E6). Making the hold unbounded fails the stalled case (`l47-evidence/a2/f1-unbounded-hold-fails.txt`).
> - It does not cover the late-catalogue jump and focus loss after the bound (review R2 observation O-R2-1),
>   which belongs to L48.
>
> ### Todos
>
> None.
>
> The first case counts catalogue against review requests after entry and selection, proving one catalogue read and subject-only review reads. The second holds the catalogue unanswered, opens the task-context review instead, and keeps the All changes row working from that answer. The catalogue is assembled from two independent recorded family-selector answers; a separate task capture supplies task context.
> ## Evidence
>
> ### Docs References
>
> No Domain Documentation source is configured for this test module.
>
> No relevant domain documentation was found.
>
> ### Repo-Internal References
>
> - The economy the cases hold the reviewer to, including the bounded wait. (historical reference 1)
> - One catalogue read, then only the chosen subject; re-read once for a new generation. (historical reference 3)
> - A stalled catalogue releases into the task-context review within the bound. (historical reference 4)
> - The hold and the comparison-keyed catalogue under test. (historical reference 5)
>
> ### Cross-Repo References
>
> No cross-repository behavior.
>
> No meaningful cross-repo references found.
>
>
> ### Clock And Settlement Evidence
>
> - Catalogue delays and the product hold run on the same fake clock. A stalled catalogue yields zero review reads at `SUBJECT_HOLD_MS - 1` and one task-context read at the next millisecond; answered catalogues remain at one chosen-subject read even after advancing past the hold. No wall-clock elapsed inequality establishes this economy. (historical reference 6)
> - Catalogue-once counting on the entry journey (historical reference 9)
> - Held-catalogue journey keeping All changes reachable (historical reference 10)
>
> - CATALOGUE is assembled from two independent family-selector captures. familyReview selects the matching family capture or the separate task capture for null selection and changes only the comparison generation digest when needed. (historical reference 2)
> - The family captures are subjectReview.successorFamily.captured.json and l86.family.captured.json; task context comes from l86.task.captured.json. (historical reference 7)
> - familyReview selects captured family or task answers, explicitly refuses uncaptured family selectors and only perturbs after_snapshot_digest. Other non-catalogue/non-source-content routes delegate to replyFor. (historical reference 8)
