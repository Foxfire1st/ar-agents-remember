# dashboard/src/panels/review/walkedTree.test.ts

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

The unit cases of the walked tree's folding (`walkedTree.ts`, requirement MIK-R39): what each answer adds, in which order, and when the walk starts again. The cases call `advanceWalk`, `keptFamilies` and `subjectTitle` directly over served bodies, with no component mounted. 7 cases.

## Code Commentary

### Setup

- `real(name)` and `store(name)` load the payload of a captured body of the real-data set (`walkReal.*.captured.json`) and of the store-authored set (`walkStore.*.captured.json`) through `captured` of `walk.test-utils.tsx`.
- `keep(id)` and `fresh(id)` build a `TreeIntent` that keeps the tree or starts it afresh.
- `START` is the walk after the review of family FAM-R6R095RW is folded into an empty walk.

### The cases

1. **Idempotent.** The same answer folded twice changes no family, and a second call with the same walk, answer and selection returns the same walk object.
2. **Order and kept families.** Folding the review of FAM-2HBJREC2 under a keeping selection gives two families sorted by identifier; the only kept family is "Coherent intent and source review", last read for its own family subject. Folding in the other arrival order (FAM-2HBJREC2 first, then the shared member INV-2TQGXFAX) gives the same list.
3. **The kept answer.** A kept family holds, whole, the answer that last carried it, and that answer's subject is the family's `readFor`; the selected subject's own family holds the answer it was read from.
4. **Names.** `subjectTitle` returns the member's label for an invariant, the family's label for a family, and "no such record" for the identifier `no-such-record`, which the answer does not carry.
5. **An outside selection.** Under a selection that does not keep, the walk has no kept family at once and still holds the families of the answer on screen; the next answer replaces them; later answers of the same selection are folded in.
6. **Another comparison.** An answer whose after code tree differs replaces the families; the notice is `MOVED_NOTICE` when a kept family was dropped and `null` when none was.
7. **A family read twice.** The shared member's first page (two members per side of each family) and the continued page of family FAM-F00001, folded in either order, give for FAM-F00001 more than two members, the continued page's cursor, four member change facts, and the same member set in both orders.

## Evidence

- The loaders, the two kinds of selection and the starting walk. [1]
- Folding the same answer twice changes nothing. [2]
- Families are ordered by identifier whatever the arrival order, and only families outside the current context are kept. [3]
- A kept family keeps the whole answer it came from. [4]
- A subject is named as its answer names it, else by its identifier read as words. [5]
- An outside selection drops kept families at once and the next answer replaces the rest. [6]
- Another comparison starts the walk afresh and says so only when kept rows were dropped. [7]
- A family read twice keeps every member and the furthest cursor, in either order. [8]
- The function under test. [9]
