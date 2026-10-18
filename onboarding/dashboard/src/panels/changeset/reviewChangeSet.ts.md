# dashboard/src/panels/changeset/reviewChangeSet.ts

## Governing Overview

[changeset overview](overview.md)

## Purpose

`reviewChangeSet` is the reviewer's lens over a comparison change-set: it derives the lane-destination file lists, narrows a fetched change-set to one destination, and builds badge maps with a single-row lookup wrapper. It uses the lane answer the reviewer already holds and reads no review route itself.

## Code Commentary

`ReviewChangePage` names the comparison, the filter and the optional file/kind; `ReviewChangeContext` pairs that page with the held lane read, source inventory and optional worklist. `FILTER_NOTES` carries explanatory text for each non-all filter; the unknown note adds a second sentence about curation. `laneFiles` returns a destination's files, or undefined while the lane is loading or unavailable (so the buttons read `reading…`/`unavailable` rather than zero). `filteredChangeSet` intersects the fetched code list with the destination's paths and empties the memory half, since destinations classify code files; `all` returns the data untouched. `fileBadge` looks up a path in `reviewFileBadges`, rebuilding that map on each wrapper call. `reviewFileBadges` can be reused by a list: it builds lane labels from both destinations and appends a truthy path lookup from `fileAnswers(context.worklist)` only when the page filter is `unexplained`. A final inventory pass overrides binary, symlink, submodule and mode-change paths with `non-text`, retaining any appended lookup. Unexplained buckets read `no invariant`; unexplained hunk counts read `N hunks, no invariant`. Unknown labels remain unchanged. This module does not establish how the imported lookup derives its strings.

## Evidence

- Three filters name the two lane destinations plus all [1]
- Destination files come from the held lane, never a new read [3]
- The filter intersects code paths and empties the memory half [4]

- FILTER_NOTES supplies explanatory strings for unexplained and unknown. The unknown string contains a second sentence describing attaching lines to an invariant or recording that none applies; it is presentation text, not evidence that attribution has been resolved. [2]
- fileBadge delegates to reviewFileBadges and reads the requested path. reviewFileBadges combines labels from both lane destinations with fileAnswers lookups only for the unexplained page filter, then overrides exact-inventory non-text and mode-change paths with non-text while retaining the lookup. Lane labels use no invariant or N hunks, no invariant for unexplained cases; unknown labels remain unchanged. Calling fileBadge repeatedly rebuilds the map. [5]
