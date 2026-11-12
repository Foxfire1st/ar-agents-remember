# dashboard/src/panels/review/ReviewSurface.walk.test.tsx

## Governing Overview

[Owning route overview](overview.md)

## Purpose

Captured walk replies preserve kept families and occurrence selection through row clicks while the page reading column stays independent of the tree filter.

## Code Commentary

### Logic

- Seven changed member rows lead the first family and each click makes one review read; selecting the second family keeps the first whole with24 distinct members and a kept tag. With no code blocks, j reports No later block without a request.
- A shared member selected under the kept first family marks that occurrence. The kept tag is inside the family row, has last-read subject title, and the focusable row owns its accessible description.
- The selected family slot contains only that family's review; read label belongs to subject provenance, and kept tags remain in the tree. Family row selections retain the walk.
- Filtering hides/restores kept tree families and their complete member rows but leaves both family headings in the reading column.

### Invariants And Boundaries

These are declared component or pure-function checks over the fixtures named here. This read-only analysis did not execute the tests; jsdom or width stubs do not establish browser geometry.

## Evidence

- Declared check and its fixture assertions. [23]
- Declared check and its fixture assertions. [24]
- Declared check and its fixture assertions. [25]
- Declared check and its fixture assertions. [26]
- Declared check and its fixture assertions. [27]

## Historical predecessor account

The earlier account follows as provenance. Current assertions and removed journeys are described above.

> # dashboard/src/panels/review/ReviewSurface.walk.test.tsx
>
> ## Governing Overview
>
> [dashboard/src/panels route overview](overview.md)
>
> ## Purpose
>
> Seven mounted walk test blocks replay the retained MIK-L33 `walkReal` review bodies through `walk.test-utils.tsx`. The current catalogue is augmented with an explicitly synthetic outline; the real surface/client assertions cover change traversal, kept-family tagging, complete outline rows, filtering and end-message lifecycle, not a newly served outline or browser journey.
>
> Family FAM-R6R095RW has seven changes, the last of them the shared member INV-2TQGXFAX; FAM-2HBJREC2 is the other family of that member.
>
> The walked family tree on real capture data: key presses walk every change across families, the first family stays kept with its tag and counts when the second is chosen, outline rows never reset the walk, filters hide and restore kept families, and end messages appear and clear exactly once.
> ## Code Commentary
>
> ### The cases that pin the keeping
>
> 1. **By key:** J visits the seven captured changes and the second family with the asserted request counts; K returns through cached changes, and both end messages leave selection in place. The first family is kept with visible tag `kept`, 24 distinct member subjects and the same workspace node.
> 2. **By click:** selecting the shared member and then the second family keeps the first family's 24 subjects; Previous change returns to the shared member under the first family.
> 3. **Tag and reading:** the kept row's accessible description names the last-read invariant, while the selected row has no description. The old filter-scope and Family context details nodes are absent, and the centre contains only the selected family's reading.
> 4. **Outline rows:** no catalogue-subject or All-invariants list is mounted; selecting another outline family retains both families and one kept tag.
> 5. **Filter:** hiding the kept family excludes it from K traversal; clearing restores its 24 subjects, kept mark and the previous change.
>
> ### The cases that pin the end message
>
> An end message belongs to the rows the tree showed when it was said (rule 11 of the requirement).
>
> 6. **Cleared filter:** the terminal J message clears when the filter reveals the later family, and the next J reaches that family with one request.
> 7. **Same rows again:** changing and clearing a filter drops the earlier terminal message permanently; a new J at the end says it again. The predecessor held-answer `it.each` is removed, not current coverage.
>
> ### Helpers of this file
>
> - `descriptionOf(node)` computes a node's accessible description through the role query.
> - `catalogueRows(view)` lists the subject identifiers of the catalogue rows.
>
> The shared replay world supplies synthetic complete outline rows over immutable review facts. Current assertions retain J/K request counts, kept tag/description, subject-only centre, outline selections and filter-driven end-message clearing. No current case tests the retired scope-line counts, catalogue-only reset or held-answer branch.
> ## Evidence
>
> - The file's statement of its data and of what its cases pin. (historical reference 9)
> - By key: seven changes, the second family, the kept first family, the end messages, the way back, and the review requests of each press. (historical reference 10)
> - By click: the first family is kept, and the previous-change control reaches the shared member. (historical reference 11)
> - Kept tag/description, absence of old scope/detail nodes and subject-only reading. (historical reference 12)
> - One outline row per family; selection retains the walk. (historical reference 13)
> - Filtering hides and restores kept families. (historical reference 14)
> - Historical removed held-answer `it.each`, not a current witness. (historical reference 15)
> - Clearing the filter drops the terminal message before J reaches the later family. (historical reference 16)
> - Returning to the same shown rows does not revive an old end message. (historical reference 17)
> - The world and the step helper the cases use. (historical reference 18)
> - Accessible description extraction for selected rows (historical reference 19)
> - Shared-member row resolution across families (historical reference 20)
> - Kept-family row with tag and apart counts (historical reference 21)
> - Filter field journeys hiding kept families (historical reference 22)
