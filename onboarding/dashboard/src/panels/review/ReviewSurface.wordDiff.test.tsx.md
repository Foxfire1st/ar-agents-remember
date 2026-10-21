# dashboard/src/panels/review/ReviewSurface.wordDiff.test.tsx

## Governing Overview

[Owning route overview](overview.md)

## Purpose

Captured successor reviews keep invariant wording before code and the containing family guarantee in its following details area.

## Code Commentary

### Logic

- The mounted invariant review has statement, applicability and conditions.1 word-diff passages in the member center. The containing family guarantee has the sole guarantee passage in member details after that content; the exact revision labels and removed/added spoken words survive.
- Neither prose word diff is rendered in a code editor. Opening the family itself still word-diffs its guarantee.
- An explicitly synthetic metadata edit makes differing guarantee texts share one revision. The member details call that guarantee changed, include the same-revision text-diff qualification and record same_revision_text_changed; the retired rail guarantee remains absent.

### Invariants And Boundaries

These are declared component or pure-function checks over the fixtures named here. This read-only analysis did not execute the tests; jsdom or width stubs do not establish browser geometry.

## Evidence

- Declared check and its fixture assertions. [12]
- Declared check and its fixture assertions. [13]

## Historical predecessor account

The earlier account follows as provenance. Current assertions and removed journeys are described above.

> # dashboard/src/panels/review/ReviewSurface.wordDiff.test.tsx
>
> ## Governing Overview
>
> [Owning route overview](overview.md)
>
> ## Purpose
>
> Retained L37 successor operands drive four changed passages and their revision/text labels; the same-revision adversarial metadata remains explicitly synthetic.
>
> ## Code Commentary
>
> Retained L37 successor operands drive four changed passages and their revision/text labels; the same-revision adversarial metadata remains explicitly synthetic. Dataset rendering and its dataset-only same-revision control are removed rather than silently counted as tree-review coverage.
>
> ### Declared Assertions
>
> - `it("word-diffs a tree review's member statement and family guarantee in the center", async () => {`
> - `it('never calls one guarantee revision unchanged when its texts differ, anywhere on a tree review', async () => {`
>
> This is a declaration inventory, not a collected parametrized-case total or execution result.
>
> ### Evidence Boundary
>
> The source declares these checks. This card does not attest that pytest/Vitest, a native host, a real browser or an installed producer ran on this candidate. Controlled or captured inputs qualify only the operations named above.
>
> ## Prior Fixture Account — Historical Only
>
> The following account describes the earlier fixtures and assertion scope. Its present-tense clauses and numbered labels are historical, not current guarantees, current evidence or a fresh run. The current source account above states what is still exercised and what was removed.
>
> > # dashboard/src/panels/review/ReviewSurface.wordDiff.test.tsx
> >
> > ## Governing Overview
> >
> > [dashboard/src/panels route overview](overview.md)
> >
> > ## Purpose
> >
> > **MIK-R35 wired into the real review surface (3 cases).** The real `ReviewSurface` renders the real served bodies
> > of the converted scratch leaf (`gitTrees.family`, `gitTrees.invariant`, `gitTrees.entries`, `gitTrees.cards` and the
> > leaf-wide `data/reviewTrees.captured.json`; a tree comparison `review:trees:1`), with only `fetch` stubbed. The
> > family guarantee and the touched member's statement are given a successor revision. The same bodies without the
> > tree comparison's token stand for a dataset review, which keeps the landed rendering.
> >
> > ## Code Commentary
> >
> > ### Logic
> >
> > - `successor(result, tree, sameRevision)` adds a clause to the after guarantee ("…is refused by name, and the
> >   refusal says what each snapshot answered.") and, for the member review, gives the selected member a successor
> >   revision (`r3`, "is refused" → "is rejected and reported"). `sameRevision` keeps the guarantee's one revision while
> >   its text changes (MIK-R21 allows it). Without `tree`, the `review:*` limitations are dropped.
> > - `serve` answers `/trees` with the cards body when `invariants` is present and the leaf-wide body otherwise,
> >   `/entries` with the entries body, `/source-content` with a refusal, and the review reads by `selectorId`. Since
> >   MIK-L32 the surface also makes one `lane=files` read for the tree review; the stub answers it with the leaf-wide
> >   body, which carries no `lane`, so the lane's destinations read `unavailable` (never a zero) and no assertion here
> >   depends on them.
> > - **Case 1, the tree review:** the member centre holds exactly two passages, `guarantee` and `statement`; the label
> >   is "Changed statement · revision r2 → r3"; the statement reads "…is removed: refused added: rejected and reported
> >   with…"; the guarantee is `review-center-guarantee-changed` with `data-word-diff="true"` and "Changed guarantee ·
> >   revision r2 → r3"; no code editor draws the prose. The family review word-diffs its guarantee too.
> > - **Case 2, the dataset review (ruling Q3):** no passage, and the guarantee keeps its `DiffPane`.
> > - **Case 3, same-revision differing guarantee:** the tree review's centre shows the changed-guarantee label and `guarantee: same_revision_text_changed`; no rail guarantee node is mounted. The dataset-shaped fixture also has no rail guarantee node and retains a centre `DiffPane`. No surviving assertion compares before/after rail guarantee text.
> >
> > ### Conventions
> >
> > - Like `ReviewSurface.gitTrees.test.tsx`, only `fetch` is stubbed and every body is a captured one; the successor
> >   revisions are the derivation's own fixed identities (`NEXT_MEMBER`, `NEXT_FAMILY`).
> >
> > ### Invariants And Boundaries
> >
> > - The mounted cases retain centre statement/guarantee word diff and dataset-shaped non-word-diff rendering. Historical mutation G8 concerned the retired navigator guarantee; it is not a current rail-text proof in this file.
> >
> > ### Todos
> >
> > - **Resolved by MIK-L32, which landed second (ruling 2026-09-30T12:16:39):** the architect's sync note records that this
> >   file was rerun on the L35-synced tree and passes; L32's review R1 F6 had also run it on a merged scratch copy (6
> >   files, 60 tests). The stub answers the lane read with the leaf-wide body, so no `withoutLane` mirror was needed (F6
> >   accepted: the stub needs no change).
> >
> > ## Evidence
> >
> > ### Docs References
> >
> > No domain documentation source is configured; the requirement packets `MIK-R35@v1` / `ICR-R35@v1` and the leaf's
> > rulings live outside the repositories, so they are named here and not cited as rows.
> >
> > No configured live documentation source was available for this pass.
> >
> > ### Repo-Internal References
> >
> > - The five real bodies the surface is served. (historical reference 1)
> > - The successor revisions, including one guarantee revision whose text changes. (historical reference 2)
> > - The fetch stub; every `/trees` read without `invariants` gets the leaf-wide body, L32's lane read included (it reads unavailable). (historical reference 3)
> > - The tree review's two passages, and the dataset review as landed. (historical reference 4)
> > - Review R1 F2 through the real surface. (historical reference 5)
> >
> > ### Cross-Repo References
> >
> > No cross-repo boundary is crossed by this file.
> > - Successor member and family for diff journeys (historical reference 7)
> > - Selection payload with statement and guarantee (historical reference 8)
> > - Per-route captured world for entries and cards (historical reference 9)
> > - Spoken announcements of changed passages (historical reference 10)
> >
> > - When same-revision guarantee text differs, the tree review’s center states the changed text/fact; neither tree nor dataset review renders the old rail guarantee node. (historical reference 6)
>
> ## Evidence
>
> - Retained L37 successor operands drive four changed passages and their revision/text labels; the same-revision adversarial metadata remains explicitly synthetic. Dataset rendering and its dataset-only same-revision control are removed rather than silently counted as tree-review coverage. (historical reference 11)
