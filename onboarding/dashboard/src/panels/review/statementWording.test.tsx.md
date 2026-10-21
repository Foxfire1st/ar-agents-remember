# dashboard/src/panels/review/statementWording.test.tsx

## Governing Overview

[Owning route overview](overview.md)

## Purpose

Captured invariant operands and explicit successor edits distinguish identical authored wording from changed or unreadable fields.

## Code Commentary

### Logic

- A new revision with identical authored text draws one prose block and compact r2 → r3 metadata without a diff or raw successor revision ID in the reading area.
- A condition-only edit is named Changed conditions and retains the changed condition. wordingComparison separately checks exclusions, uncarried applicability and identical revision identity.
- An unresolved side keeps separate side-state lines without a single prose block; a one-sided added statement is labelled prose without a split editor.

### Invariants And Boundaries

These are declared component or pure-function checks over the fixtures named here. This read-only analysis did not execute the tests; jsdom or width stubs do not establish browser geometry.

## Evidence

- Declared check and its fixture assertions. [4]
- Declared check and its fixture assertions. [5]
- Declared check and its fixture assertions. [6]
- Declared check and its fixture assertions. [7]
- Declared check and its fixture assertions. [8]

## Historical predecessor account

The earlier account follows as provenance. Current assertions and removed journeys are described above.

> # dashboard/src/panels/review/statementWording.test.tsx
>
> ## Governing Overview
>
> [dashboard/src/panels route overview](overview.md)
>
> ## Purpose
>
> **MIK-R31 rule 3's cases (5): "wording unchanged" only when every authored text field is identical.** The knowledge
> pane and member rows start from the real served invariant review of the converted scratch leaf
> (`gitTrees.invariant.captured.json`); `successor()` derives the second revision by changing exactly the field each
> case is about, and mounts the real `SelectedStatement`.
>
> ## Code Commentary
>
> ### Logic
>
> - Identical authored text on two revisions renders once, with `revision r2 → r3` as compact metadata.
> - A condition-only revision is never labelled unchanged: the changed condition is named.
> - The decision reads every field, and a field that was not carried is never promoted to unchanged
>   (`wordingComparison` directly).
> - Review F5: when one statement side is not present, each side keeps its own state line and no single prose block is
>   shown.
> - An added statement renders as labelled prose ("Added statement"), not a split code editor.
>
> ### Conventions
>
> - The fixed successor revision ID and the display versions `r2`/`r3` are the derivation's own values, stated in the
>   file.
> - Since MIK-L35, `successor()` passes the member rows keyed by side (`MemberSides`: `{ before: [...], after:
>   [after] }`), because `SelectedStatement` now reads each side's text only from that side's own rows (review R1 F1).
>   That one line is the only change the API forced; no assertion changed (review R2 §4). These cases mount without the
>   tree-comparison scope, so they pin the dataset path's rule 3 rendering; MIK-R35's tree-path cases are in
>   `IntentWordDiff.test.tsx`.
>
> ### Invariants And Boundaries
>
> - These cases pin the 13:40 rule, including its negative (a condition-only change is not "wording unchanged"); the
>   reviewer's mutation (treating an uncarried field as identical) fails a case here.
>
> ### Todos
>
> No additional work is asserted by this card.
>
> ## Evidence
>
> ### Docs References
>
> No domain documentation source is configured; the requirement packet `MIK-R31@v1` lives outside the repositories.
>
> No configured live documentation source was available for this pass.
>
> ### Repo-Internal References
>
> - The real body the revisions start from, and the one-field successor. (historical reference 1)
> - The side-keyed member rows the one-field successor mounts with (MIK-L35). (historical reference 2)
> - The five cases. (historical reference 3)
>
> ### Cross-Repo References
>
> No cross-repo boundary is crossed by this file.
