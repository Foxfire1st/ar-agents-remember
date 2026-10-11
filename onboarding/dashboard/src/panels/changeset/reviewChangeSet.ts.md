# dashboard/src/panels/changeset/reviewChangeSet.ts

## Governing Overview

[changeset overview](overview.md)

## Purpose

`reviewChangeSet` is the reviewer's lens over a comparison change-set: it derives the lane-destination file lists, narrows a fetched change-set to one destination, and badges single rows. It uses the lane answer the reviewer already holds and reads no review route itself.

## Code Commentary

`ReviewChangePage` names the comparison, the filter and the optional file/kind; `ReviewChangeContext` pairs that page with the held lane read and the source inventory. `FILTER_NOTES` carries the one sentence each non-all filter shows above the list. `laneFiles` returns a destination's files, or undefined while the lane is loading or unavailable (so the buttons read `reading…`/`unavailable` rather than zero). `filteredChangeSet` intersects the fetched code list with the destination's paths and empties the memory half, since destinations classify code files; `all` returns the data untouched. `fileBadge` marks non-text inventory paths first, then a row's bucket or its unexplained/unknown hunk counts, else nothing.

## Evidence

- Three filters name the two lane destinations plus all [1]
- Each non-all filter explains itself in one sentence [2]
- Destination files come from the held lane, never a new read [3]
- The filter intersects code paths and empties the memory half [4]
- Rows carry bucket or hunk-count badges, non-text first [5]
