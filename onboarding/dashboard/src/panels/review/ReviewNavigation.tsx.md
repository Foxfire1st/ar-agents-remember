# ReviewNavigation.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/ReviewNavigation.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-28T21:39:58+02:00 |
| lastVerifiedCommitHash | `ae2fd5c864aa2609ae45b5c7dbbaa693569aefc6`|
| lastVerifiedCommitDate | 2026-09-28T22:11:57+02:00|
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

## Docs References

No Domain Documentation source is configured. The implementation-specific account is grounded in the repository source below.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain source could be checked. | — | — |

## Repo-Internal References

The named constructs own this behavior; reads and validation use their existing callers and models.

| Finding | Anchor | Source |
| --- | --- | --- |
| The navigation shape with the read-cycle signals and the engagement signal. | `ReviewNavigation`; `settling`; `observeComparison`; `engage` | dashboard/src/panels/review/ReviewNavigation.tsx:20-36 |
| The hold bound and why it exists, including that a late catalogue selects only for a reader who has not engaged. | `SUBJECT_HOLD_MS`; `engage` | dashboard/src/panels/review/ReviewNavigation.tsx:147-152 |
| Subject choice, the comparison-keyed catalogue, the expiring hold, the generation bump and the engagement freeze. | `useReviewNavigation`; `useReviewCatalogue`; `setExpired`; `setGeneration`; `engage` | dashboard/src/panels/review/ReviewNavigation.tsx:155-211 |
| The passive gesture observer the surface mounts on its root. | `useReaderEngagement`; `ENGAGING_EVENTS`; `passive: true` | dashboard/src/panels/review/ReviewNavigation.tsx:213-230 |
| The surface-side snapshot report. | `useObservedComparison`; `knowledge_compared` | dashboard/src/panels/review/ReviewNavigation.tsx:233-242 |
| `initialSubject` owns the default subject choice. | `initialSubject` | dashboard/src/panels/review/ReviewNavigation.tsx:251-259 |
| The rail component. | `ReviewNavigation` | dashboard/src/panels/review/ReviewNavigation.tsx:88-145 |
| `CatalogueFamilies` owns the family rail. | `CatalogueFamilies` | dashboard/src/panels/review/ReviewNavigation.tsx:261-294 |
| The surface wires all three signals: the hold, the snapshot observation and the engagement observer on its root. | `hold: navigation.settling`; `useObservedComparison`; `useReaderEngagement` | dashboard/src/panels/review/ReviewSurface.tsx:471-496; dashboard/src/panels/review/ReviewSurface.tsx:524-527 |
| The two delayed-catalogue cases: an engaged reader is not moved, an idle reader is landed on the first family without a remount. | "does not move a reader who is working when the catalogue answers after the bounded wait"; "lands a reader who has not acted on the first family when the catalogue answers late, without remounting" | dashboard/src/panels/review/ReviewSurface.navigation.test.tsx:460-511 |

## Cross-Repo References

No independent cross-repository interface is introduced by this source.

| Finding | Anchor | Source |
| --- | --- | --- |
| No additional cross-repository evidence is required. | — | — |

## Update History
- 2026-09-28T21:39:58+02:00 — 260921-ICR-L48 curator (uncommitted candidate tree `ac73216e2a763b72844a63b8c36c81f9a8b5f0e8` over code base `cb1b942af60a7ed5006ac992075d2bf96aeb9fa7`): **body update — reader engagement settles a late catalogue (`ICR-R24@v3`; L47 review R2 observation O-R2-1, routed to L48).** Implementation **extends** the L47 contract: `engage` joins the navigation shape and freezes the subject on screen once the bounded wait has released a read, and `useReaderEngagement` observes pointer/key/wheel/touch gestures passively on the surface root. The card's L47 statement that a late catalogue moves the reader and drops focus is **superseded**: an engaged reader stays put, an idle reader is landed on the first family inside the same mounted workspace. The policy was the worker's choice requested by the L48 brief and was verified by review R1/R2. Logic, Conventions and Invariants updated; every reference row re-derived from its declaration, two rows added. No stamp advanced.

- 2026-09-28T17:09:38+02:00 — 260921-ICR-L47 curator (uncommitted candidate tree `72efa4bbc169b16afe8ef249499edf79cad9940d` over code base `58e22246cc09ef0ee12095e284a111a475081c38`): **body update — the reviewer owns its catalogue read, keyed on the comparison, with a bounded first-read hold (`ICR-R24@v3`; L47-R1-F1).** The claim "`useReviewNavigation` owns the behavior" was re-read against the changed hook: it no longer reads analytics, returns `settling` and `observeComparison`, and `SUBJECT_HOLD_MS = 750` bounds the hold. Logic, Conventions and Invariants were extended; reference rows re-derived. No stamp advanced; closeout owns the real stamp.

- 2026-09-26T19:49:05Z — Created the in-review catalogue navigation card.
