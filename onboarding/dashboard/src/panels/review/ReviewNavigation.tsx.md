# ReviewNavigation.tsx

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
a refused catalogue); the first subject is still selected if the catalogue answers later — unless the reader has
already started working (below).

**Reader engagement settles a late catalogue (L48, the O-R2-1 rule).** `engage()` is the navigation's third
signal. Once the bounded wait has released a read (`settling` false), the first gesture freezes the subject on
screen as the reader's own choice (`setChoice` with the current key and subject), so a catalogue that answers
later only fills the navigation and no longer moves the reader to its first family. `engage` is ignored while
`settling`, and its update is functional (`previous?.key === key ? previous : …`), so an explicit selection
queued by the same gesture is never overwritten. `useReaderEngagement(root, engage)` is the surface-side hook:
it attaches `pointerdown`, `keydown`, `wheel` and `touchstart` listeners **passively, in the capture phase,**
on the surface root and only reports them — it handles no event, so no reader gesture changes meaning. A
reader who has not acted is still landed on the first family, now inside the same mounted workspace (the
surface keeps its frame, see `ReviewSurface.tsx`).

### Conventions

Uses the existing owner interfaces and exact recorded identities; keeps transient task evidence outside
durable onboarding. The navigation's public shape is the `ReviewNavigation` interface (the state plus
`settling`, `observeComparison` and, since L48, `engage`); the component of the same name renders the rail.
Gestures are observed with native listeners rather than JSX handlers, which keeps the surface root a
non-interactive element.

### Invariants And Boundaries

Catalogue identity and comparison-specific family content have different owners. Loading, unreadable,
confirmed empty and explicit source-only selection remain distinct. The hold never withholds the
task-context review and source explorer beyond the bound. This module authors no knowledge or assessment.
A catalogue answering after the bound never moves a reader who has acted in the reviewer; it moves a reader
who has not acted to the first family without a remount (L48 settled review R2 observation O-R2-1 this way).
Engagement only freezes the subject already on screen — it never selects, reads or clears anything itself.

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No Domain Documentation source is configured. The implementation-specific account is grounded in the repository source below.

No configured domain source could be checked.

### Repo-Internal References

The named constructs own this behavior; reads and validation use their existing callers and models.

- The navigation shape with the read-cycle signals and the engagement signal. [1]
- The hold bound and why it exists, including that a late catalogue selects only for a reader who has not engaged. [2]
- Subject choice, the comparison-keyed catalogue, the expiring hold, the generation bump and the engagement freeze. [3]
- The passive gesture observer the surface mounts on its root. [4]
- The surface-side snapshot report. [5]
- `initialSubject` owns the default subject choice. [6]
- The rail component. [7]
- `CatalogueFamilies` owns the family rail. [8]
- The surface wires all three signals: the hold, the snapshot observation and the engagement observer on its root. [9]
- The two delayed-catalogue cases: an engaged reader is not moved, an idle reader is landed on the first family without a remount. [10]

### Cross-Repo References

No independent cross-repository interface is introduced by this source.

No additional cross-repository evidence is required.
