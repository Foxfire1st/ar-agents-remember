# dashboard/src/panels/review/hunkMarkers.ts

## Governing Overview

[review route overview](overview.md)

## Purpose

Project the owner's file/hunk classification into marker labels, linked entry occurrences and placement within the source window actually drawn.

## Code Commentary

`fileMarks` produces a file-level marker for confirmed-unregistered/wholly unreadable files and otherwise one per owner hunk. `hunkMark` retains realization and proof entries separately, plus unknown lines including a linked hunk's unread changed side. It does not classify a hunk by client-side range intersection.

`markEntries` groups by kind and invariant and `addOccurrence` merges only an identical membership/family/revision occurrence across sides. Every new target copies the supplied family.reason verbatim; unknown membership without a family is distinct from a named family occurrence. Full and compact labels count those retained entries/occurrences and keep before/after side labels.

`markAnchor` finds the first changed line actually inside a drawn side window, preferring an after line and otherwise a removed before line. In unified layout a deletion's marker lands below its removed lines with its inline-after position clamped to the drawn window. A hunk with no drawn changed line has no gutter placement. Placement consumes supplied hunk spans and rendered windows and creates no new attribution.

## Evidence

- hunkMarkers.ts current behavior at this source owner. [15]
- hunkMarkers.ts current behavior at this source owner. [16]
- hunkMarkers.ts current behavior at this source owner. [17]
