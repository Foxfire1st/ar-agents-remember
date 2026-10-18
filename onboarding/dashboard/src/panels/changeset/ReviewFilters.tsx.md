# dashboard/src/panels/changeset/ReviewFilters.tsx

## Governing Overview

[changeset overview](overview.md)

## Purpose

Present the reviewer's comparison-page filter controls from lane facts it already holds, independently of the ChangeSetViewer's list/diff state. This extraction adds truthful display wording without introducing a lane fetch or classification algorithm.

## Code Commentary

ReviewFilters renders nothing without review context. Otherwise it offers All, Changes without an invariant and Unknown attribution, retaining the internal all/unexplained/unknown filter tokens. A click passes the token to onFilter and aria-pressed names the selected filter.

FilterButton reads the destination through laneFiles. All counts fetched changed code files (not memory files or worklist items); destination counts are held lane-file counts. While a lane is loading the unavailable destination reads reading…; otherwise a missing destination says the change set could not be measured. A missing destination disables its button, but a measured empty array is truthy, enables selection and shows zero. This distinction avoids converting an unperformed measurement into an empty result. Non-all filters show the corresponding FILTER_NOTES below the controls. Filtering and per-file answered/open badges live in reviewChangeSet/worklistState, not here.

The caller must keep page, lane and inventory bound to the same comparison. These components do not validate tree identity, issue requests or decide whether work is answered.

## Evidence

- Destination count, named waiting state and empty-versus-missing button behavior. [1]
- No context means no controls; non-all filters show shared notes. [2]
- Lane file selection and intersection are pure held-answer helpers. [3]
- Actual viewer imports and mounts this owner. [4]
