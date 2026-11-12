# dashboard/src/panels/review/ReviewDestinations.tsx

## Governing Overview

[review route overview](overview.md)

## Purpose

Project the held lane read into Code without invariant rows and render the tree's pinned Worklist/lane destinations and lane-file rows.

## Code Commentary

`treeLane` distinguishes reading, unavailable and ready. For a ready lane it takes only each unexplained/unknown destination's own bucket_files prefix, leaving the additionally attributed files out, and retains that destination for every file. A file reason uses read line counts when supplied, otherwise non-text or lane hunk counts. Reading and unavailable render explicit count states rather than presenting the internal empty arrays as measured zero.

`TreePinned` draws Worklist first with the supplied open-item count, then Code without invariant with its lane count. Nonempty destination buckets expose their own full-page actions. File rows follow in the same tree scroller, filtered by laneFileMatches; they show filename with full path as title/accessible identity, retain a reason, and use the tree-arrow focus owner. Selecting a file selects its lane place; a selected hunk of that path also marks the file current. The supplied callbacks own worklist selection, lane selection and opening the comparison viewer.

## Evidence

- ReviewDestinations.tsx current behavior at this source owner. [5]
- ReviewDestinations.tsx current behavior at this source owner. [6]
