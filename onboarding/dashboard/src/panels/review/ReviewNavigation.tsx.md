# dashboard/src/panels/review/ReviewNavigation.tsx

## Governing Overview

[review route overview](overview.md)

## Purpose

Read the comparison-bound subject catalogue, retain only a named or reader-selected subject and observe the comparison generation shown by the surface.

## Code Commentary

`initialSubject` accepts a target only when both selector kind and identifier are present. An unnamed opening selects nothing, and a catalogue answer never selects a subject. A choice is keyed to the target's serialized identity so it cannot become another target's selection. SelectionOptions separately carries explicit keepTree and a requested review page for the surface's selection owner.

`useReviewNavigation` reads the catalogue for repo/master/leaf/history, the local generation and the optional selected comparison number. Observing the first generation records its identity; a changed generation in the same task context increments the local catalogue generation. Compatible enrichment from unknown to known knowledge snapshots records that identity without an extra generation bump. A generation observed for another task is that task's first generation.

`useObservedComparison` reports the shown payload's code trees and known knowledge snapshots, including code-only movement. `outlineUnavailableReason` preserves an outline or catalogue owner's reason once reading ends, with the unconverted-memory explanation only when neither supplied one. Catalogue identity is separate from review-supplied family content; this module renders neither navigation rows nor semantic content.

## Evidence

- ReviewNavigation.tsx current behavior at this source owner. [37]
- ReviewNavigation.tsx current behavior at this source owner. [38]
- ReviewNavigation.tsx current behavior at this source owner. [39]
- ReviewNavigation.tsx current behavior at this source owner. [40]
