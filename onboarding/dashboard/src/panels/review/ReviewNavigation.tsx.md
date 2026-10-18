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
- The navigation hook stores the selected subject; the workspace and outline rows own the gestures and tree context. The rail no longer renders a parallel all-invariants list or its own catalogue subject buttons.

- `initialSubject` opens on an explicit target subject when given one, else on the outline's first real change (`firstOutlineChange`, in the current tree order), else on the catalogue's first family; with no real change there is no opening subject.
### `useReviewNavigation`

`useReviewNavigation(target)` holds the choice of one task context (keyed by the whole target):

- An explicit subject in the target is the opening subject. Otherwise an admitted outline supplies its first real change in the reader's current order. An admitted outline with no real change leaves the subject unset; only without an outline does catalogue-family/first-entry fallback apply.
- Its own `onSelect` stores the chosen subject. The current All changes action opens the recorded-comparison change-set page without clearing that subject; returning restores the mounted review. Explicit source-only selection remains a distinct hook state, not a separate rail button.
- It reads the catalogue through `useReviewCatalogue`, carrying the observed comparison generation alongside task, history and local generation. `observeComparison` observes code trees as well as known snapshots; code-only moves invalidate the catalogue too. `useObservedComparison` reports `comparisonGenerationOf(shown)`. A same-generation enrichment from unknown to known snapshots updates identity without an extra local generation bump.
- `settling` is true while the reviewer was opened with no subject, the catalogue has not answered, and `SUBJECT_HOLD_MS` (750 ms) has not passed. The surface holds its first review read while `settling`, so a prompt catalogue costs one subject read instead of a whole-task read followed by a subject read. When the bound expires the task-context review is read.
- `engage()` is called for reader gestures. Once `settling` is false, the first gesture stores the subject on screen as the reader's own choice, so a catalogue that answers later only fills navigation without moving that reader. `engage` does nothing while `settling`, and its functional update never overwrites an explicit selection queued by the same gesture. An idle reader uses the arriving catalogue's outline-first opening rule.

`useReaderEngagement(root, engage)` attaches `pointerdown`, `keydown`, `wheel` and `touchstart` listeners on the surface root, passively and in the capture phase. It only reports the gestures; it handles no event.

### The rail

`ReviewNavigation` renders one `review-catalogue-navigation` section with the Families & invariants heading,
`navigationSummary`, an outline-unavailable reason when necessary, the outline tree passed as `children`,
and comparison change-set destinations passed by the workspace. Walked entries affect summary counts;
there is no `CatalogueFamilies`, `SubjectButton`, separate all-invariants disclosure or refresh-subjects button.

- `ReviewNavigation` (the component) renders the section `review-catalogue-navigation`: the `Families & invariants` heading, the summary line (`navigationSummary`: changed-family and changed-invariant counts from `outlineCounts` over the walked entries, plus the lane's unexplained/unknown file counts), the outline-unavailable reason when the counts cannot be read, then the tree (`children`) and the change-set destinations.
The current summary optionally appends caller-supplied codeSummary text without recomputing code
facts. attributionSummary keeps unavailable measurement explicit as the change set could not be
measured; otherwise it distinguishes files without an invariant from unknown-attribution files.
Neither label is a curation decision or permission to treat an unavailable count as zero.

### Conventions

- Exports: `ReviewSubject`, `SelectionOptions`, `ReviewNavigationState`, the interface and the component `ReviewNavigation`, `SUBJECT_HOLD_MS`, `useReviewNavigation`, `useReaderEngagement` and `useObservedComparison`.
- Gestures are observed with native listeners, not JSX handlers.

### Invariants And Boundaries

- Catalogue identity and comparison-specific family content have different owners: the catalogue supplies identity, the review supplies family content.
- Loading, unreadable, confirmed empty and explicit source-only selection are distinct states.
- Timer expiry releases the configured first-read hold; this is not a fresh measured wall-clock response bound or permission to restore a source explorer in the sidebar.
- A catalogue answering after the bound never moves a reader who has acted in the reviewer.
- Engagement only stores the subject already on screen. It never selects, reads or clears anything itself.
- This module authors no knowledge and no assessment.

## Evidence

- How a selection treats the walked tree, and the page a selection may ask for. [11]
- What the workspace receives: the catalogue, the subject and the selection callback with its options. [12]

- The hold bound and why it exists. [16]
- Subject choice is outline-first; full observed generation quarantines catalogue rows, the bounded hold expires and engagement preserves the reader's choice. [17]
- The passive gesture observer the surface mounts on its root. [18]
- Surface-side observation reports complete comparison generation, including code-only movement. [19]
- initialSubject keeps an explicit target, otherwise chooses the first real outlined change; no real change means no subject, with catalogue fallback only without an outline. [20]
- The surface's selection reads the options: `keepTree` and `page`. [21]
- The workspace supplies walked entries to navigation counts and catalogue outline/admission to the compact tree. [22]



- Delayed-catalogue coverage retains engagement and mounted-shell ownership; opening follows the current outline/fallback rule. [24]



- Outline-first opening subject, none without real change [28]
- Choice, settling, comparison generation and engage [30]
- Surface-side comparison generation reporting [32]

- The rail combines existing summary text with optional caller-supplied codeSummary, then open reason/tree/destination slots; it makes no new measurement. [25]
- navigationSummary derives outline counts only after catalogue admission and retains unavailable reason rather than synthesizing an empty count. [26]
- The summary combines changed-family/invariant counts with attributionSummary; an unavailable lane count says the change set could not be measured. [27]
