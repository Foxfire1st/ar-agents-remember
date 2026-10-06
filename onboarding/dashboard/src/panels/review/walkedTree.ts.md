# dashboard/src/panels/review/walkedTree.ts

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

The walked tree of the intent reviewer: the list of families the family tree shows across selections (requirement MIK-R39).

The server composes a family context per selected subject: one family for a family subject, every containing family for an invariant subject. This module folds the family context of every answer the workspace shows into one list. A selection of a row the tree shows therefore adds families and member rows and removes none, and `k` can step back to every change the reader passed. The module also decides when the list starts afresh.

It makes no request and stores nothing outside the mounted reviewer. Its only input is answers that were already read.

## Code Commentary

### The data

- **`Walk`** is the state of one walk:
  - `scope` is the task context the caller names (repository, master, leaf and live or recorded view);
  - `intent` is the number of the last selection the walk applied;
  - `generation` is the comparison generation of its rows (`ComparisonGeneration` of `ReviewReadCache.ts`);
  - `source` is the answer folded in last;
  - `families` is the list of `WalkedFamily`, ascending by family identifier;
  - `current` holds the family identifiers of the latest answer's own context;
  - `replaceNext` says that the next answer replaces the list;
  - `notice` is a sentence for the reader, or `null`.
- **`WalkedFamily`** is one family of the list: `entry` (the merged family context entry), `readFor` (the subject whose answer last carried the family, taken from the answer's `knowledge.revision_selection`; absent when the answer names none) and `answer` (that answer, whole).
- **`TreeIntent`** is the reader's latest selection as the workspace numbers it: `id`, and `keep`, which is true for a selection of a row the tree shows.
- **A kept family** is a family of the list that is not in `current` (`keptFamilies`). Its rows were read for an earlier subject.

### One step: `advanceWalk`

`advanceWalk(walk, payload, scope, intent)` first applies the selection (`rebase`) and then folds the answer in (`absorb`), unless the result already has `payload` as its `source`. It is pure and idempotent: when nothing is new it returns the walk object it was given.

`rebase` has four cases:

1. The scope differs from the walk's: the result is a new walk that holds only this answer's families.
2. The selection is the one the walk already applied: nothing changes.
3. The selection keeps (`intent.keep`): the walk takes the selection's number and clears `replaceNext`. No family is removed.
4. Any other selection: the result is a new walk that holds only the families of the answer on screen, with `replaceNext` set. The kept families are gone at once, before the selection's own answer arrives, and that answer then replaces the rest.

`absorb` folds one answer in:

- It compares the answer's generation (`comparisonGenerationOf`) with the walk's through `sameGeneration`. An answer of another comparison replaces every family the walk held. `notice` is then `MOVED_NOTICE` if the walk held a kept family, and `null` otherwise.
- With `replaceNext` set it also replaces every family.
- Otherwise it merges the answer's families into the list (`mergeFamilies`).
- `current` becomes the family identifiers of this answer, and `replaceNext` is cleared.
- An answer that compares no knowledge keeps the snapshot pair the walk already holds (`carriedGeneration`).

### Merging a family read twice

- `mergeFamilies` keys the list by family identifier. A family the answer carries is merged with the stored one (`mergeEntry`), and its `readFor` and `answer` become this answer's. A family the answer does not carry is left as it is. The result is sorted ascending by family identifier, which is the server's order of families within one context, so the order in which answers arrive plays no part.
- `mergeEntry` merges the two sides with `mergeSide` and the change facts with `mergeChangeKinds` of `changeTriage.ts`. The other fields are the newer entry's. When the newer entry is `partial` and both merged sides are complete (`sideComplete`), the merged entry's state is `recorded`.
- `mergeSide` merges two reads of one side when both are `recorded` and name the same family revision; otherwise it takes the newer side. Every member either read returned stays: members are keyed by `member_id` and merged with `mergeMember` of `familyWalkMerge.ts`, and when that function declines a pair the newer member is taken. The page position is taken from the side that walked further (`progress`: the members the server counted as returned), and from the newer side when both walked equally far. The continuation control of a family therefore holds the furthest cursor.

### Names and constants

- `subjectTitle(answer, subject)` names a subject as its own answer does: a family by its `display_label`, an invariant by the `display_label` of the member row that carries its identifier. When the answer carries neither, it returns the identifier with its hyphens replaced by spaces.
- `MOVED_NOTICE` is the sentence shown when the comparison changed and kept rows were dropped.
- `NO_FAMILY_CONTEXT` is an `unavailable` family context with zero counts. The workspace hands it to the tree when the selected subject's answer carries no family context while the walk still has families.

### The hook

`useWalkedTree(payload, scope, intent)` keeps the walk in React state and calls `advanceWalk` during render. When the result is a new object it stores it in the same render (derived state, no effect) and returns it, so no frame draws a tree that lacks the answer on screen.

### Boundaries

- Rows of two comparisons are never in one list.
- The module reads no route and no browser storage. Leaving the reviewer drops the walk with the component state.
- The reading area does not read from the walk. It reads the selected subject's own answer.

## Evidence

- The state of one walk: scope, applied selection, generation, last answer, families, current context, replace flag and notice. [1]
- One family of the walk: its merged entry, the subject it was last read for and that answer. [2]
- The numbered selection and whether it keeps the tree. [3]
- One step applies the selection and folds the answer in; it returns the same walk when nothing is new. [4]
- A selection that keeps changes no family; any other selection leaves only the families of the answer on screen and marks the walk for replacement. [5]
- An answer of another comparison, or the first answer after an outside selection, replaces the families; the notice is set only when kept rows were dropped. [6]
- Families are merged by identifier and sorted by identifier. [7]
- A merged entry is `recorded` once both merged sides are complete. [8]
- Every member either read returned stays, and the side that walked further gives the page position. [9]
- The kept families are the ones outside the latest answer's context. [10]
- A subject is named by its answer's label, else by its identifier read as words. [11]
- A task-context answer leaves the walk's snapshot pair as it is. [12]
- The hook advances the walk during render and stores a new result in the same render. [13]
- The comparison test the walk uses is the read cache's. [14]
- The member merge the walk reuses. [15]
- The workspace is the hook's one caller. [16]
- The unit cases over served bodies: idempotence, order, the kept answer, names, an outside selection, another comparison, and a family read twice. [17]
