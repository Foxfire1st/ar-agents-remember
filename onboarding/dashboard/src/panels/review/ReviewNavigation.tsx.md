# dashboard/src/panels/review/ReviewNavigation.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

Navigate all recorded families and invariants from inside the review workspace, using the reviewer's own catalogue read. The module holds the subject selection of one opened reviewer, tells the surface when its first review read may start, and renders the catalogue rail in which the family tree stands.

## Code Commentary

### The selection contract

- `ReviewSubject` is a subject by kind and identifier.
- `ReviewNavigationState` is what the workspace receives: the catalogue (with `refresh`), the selected subject and `onSelect(subject, context, options)`.
- `SelectionOptions` says how a selection treats the family tree the reader has walked (requirement MIK-R39). `keepTree` marks the selection of a row the tree shows; a selection without it starts the tree afresh. `page` asks for a page of the subject's review; a kept family's roster continuation uses it.
- Every selection this module makes itself passes no options: a catalogue row and a row of the list of all invariants call `onSelect({ kind, id })`, and "All source changes" calls `onSelect(undefined)`. They are therefore selections that start the walked tree afresh, also when the row names a subject the tree shows or the subject already selected.

### `useReviewNavigation`

`useReviewNavigation(target)` holds the choice of one task context (keyed by the whole target):

- An explicit subject in the target is the opening subject. Otherwise `initialSubject` chooses the first recorded family, then the first entry of the catalogue.
- Its own `onSelect` stores the chosen subject. A deliberate "All source changes" choice (`undefined`) stays source-only when the catalogue refreshes.
- It reads the catalogue through `useReviewCatalogue({ repo, master, leaf, history, generation })`. `observeComparison(snapshots)` records the first compared snapshot pair reported under this task context and history view, and raises `generation`, which re-reads the catalogue, only when a later pair differs. `useObservedComparison` is the surface-side hook that reports `before_snapshot_digest:after_snapshot_digest` when knowledge was compared.
- `settling` is true while the reviewer was opened with no subject, the catalogue has not answered, and `SUBJECT_HOLD_MS` (750 ms) has not passed. The surface holds its first review read while `settling`, so a prompt catalogue costs one subject read instead of a whole-task read followed by a subject read. When the bound expires the task-context review is read.
- `engage()` is called for reader gestures. Once `settling` is false, the first gesture stores the subject on screen as the reader's own choice, so a catalogue that answers later only fills the navigation and does not move the reader to its first family. `engage` does nothing while `settling`, and its update is functional, so an explicit selection queued by the same gesture is never overwritten. A reader who has not acted is still moved to the first family when the catalogue answers.

`useReaderEngagement(root, engage)` attaches `pointerdown`, `keydown`, `wheel` and `touchstart` listeners on the surface root, passively and in the capture phase. It only reports the gestures; it handles no event.

### The rail

`ReviewNavigation` (the component) renders the section `review-catalogue-navigation`: the catalogue's summary line, `CatalogueFamilies`, the disclosure "All N recorded invariants" (`review-all-invariants`), the empty and problem statements, and the two buttons "All source changes" (`review-task-source`) and "Refresh subjects". It takes `loadedFamilyIds` (the families the tree shows) and `listLoaded` (true while the tree holds a kept family) from the workspace.

`CatalogueFamilies` places the family tree (its `children`) among the catalogue's family rows:

- The tree stands at the place of the first catalogue family it shows. When it shows none, it stands after all rows.
- The tree is one child with the fixed key `tree`, inside a `Fragment` and with no element of its own around it. It keeps its identity, and so its open disclosures and scroll, wherever the walk moves the place it stands in.
- Without `listLoaded`, a family the tree shows has no catalogue row: the tree stands in for it.
- With `listLoaded`, every family keeps its catalogue row, the ones the tree shows included. Such a row is a plain `SubjectButton` (its label, no change badge). Choosing it is a selection without options, so the tree starts afresh with that family alone.

`SubjectButton` marks the row of the selected subject with `aria-current` and notes a subject present on one side only (" · before only", " · after only").

### Conventions

- Exports: `ReviewSubject`, `SelectionOptions`, `ReviewNavigationState`, the interface and the component `ReviewNavigation`, `SUBJECT_HOLD_MS`, `useReviewNavigation`, `useReaderEngagement` and `useObservedComparison`.
- Gestures are observed with native listeners, not JSX handlers.

### Invariants And Boundaries

- Catalogue identity and comparison-specific family content have different owners: the catalogue supplies identity, the review supplies family content.
- Loading, unreadable, confirmed empty and explicit source-only selection are distinct states.
- The hold never withholds the task-context review and the source explorer beyond the bound.
- A catalogue answering after the bound never moves a reader who has acted in the reviewer.
- Engagement only stores the subject already on screen. It never selects, reads or clears anything itself.
- This module authors no knowledge and no assessment.

## Evidence

- How a selection treats the walked tree, and the page a selection may ask for. [11]
- What the workspace receives: the catalogue, the subject and the selection callback with its options. [12]
- A catalogue row selects its subject with no options. [13]
- The rail: summary, family rows with the tree, all invariants, the statements and the two buttons. [14]
- The tree is one keyed child at the place of the first family it shows; with a kept family every family keeps its row. [15]
- The hold bound and why it exists. [16]
- Subject choice, the comparison-keyed catalogue, the expiring hold, the generation bump and the engagement freeze. [17]
- The passive gesture observer the surface mounts on its root. [18]
- The surface-side snapshot report. [19]
- The default subject: an explicit target, else the first family, else the first entry. [20]
- The surface's selection reads the options: `keepTree` and `page`. [21]
- The workspace passes the families the tree shows and the kept flag. [22]

- The mounted case of the catalogue rows beside a kept family and of the tree's place among them. [23]

- The two delayed-catalogue cases: an engaged reader is not moved, an idle reader is landed on the first family without a remount. [24]
