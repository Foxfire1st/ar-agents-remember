# dashboard/src/panels/review/UnexplainedLane.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**The unexplained-changes lane's two destinations in the reviewer's tree, and its center (MIK-R32 rule 10).**
`LaneDestinations` renders `Unexplained changes` and `Unknown attribution` in the rail after the families, each
with its file and hunk totals; `UnexplainedLaneCenter` lists the chosen destination's files in two groups and opens a
file's focused diff (`LaneFileFocus.tsx`). The lane is read only for a tree comparison; a dataset review renders none
of it and asks nothing.

## Code Commentary

### Logic

- **Rail nodes.** `LaneDestinations` is a `nav` ("Changes no recorded intent explains") with one button per
  destination; the chosen one is `aria-current` and marked. `destinationLine` gives its line: `…` while pending,
  `unavailable` when the read failed, `not measured` for an unmeasured lane, else `destinationTotals` (with
  `· partial` on a partial lane), never a zero it did not measure. `data-lane-state` carries the read's phase or the
  lane's state.
- **Center.** `UnexplainedLaneCenter` titles the destination; `LaneBody` shows "Classifying…" while pending, the
  owner's problem (`ReviewProblemBlock`) on a failed read, "The change set could not be measured, so no file is
  listed" for an unavailable lane, and otherwise the totals line with the lane's detail, the partial notice naming
  the unmeasured paths, and the files.
- **Groups.** `DestinationFiles` splits the destination (`destinationGroups`) into the bucket's own files and the
  attributed files, each a `FileGroup` with its title, count and one-line note (`GROUP_TITLES`, `GROUP_NOTES`); an
  empty destination says so in words.
- **Rows.** `FileRow` shows the path as a toggle, its status and `rowCounts` ("1 unexplained of 2 hunk(s)", and for a
  non-text change "non-text (text, mode) · gate unexplained"); `RowReason` puts the owner's reason one click away
  ("Why"): a bucket file's own reason, or an attributed file's `unknown_reasons` in the unknown destination. Opening a
  row mounts `LaneFileFocus` with the task, path, destination, inventory, layout and gate read.

### Conventions

- The order, the counts and the reasons are the server's; this file renders them and adds no filter, so no file is
  hidden (rule 11).
- The group note replaces per-row prose (the worker's browser round 1: long per-row reasons were moved behind
  "Why").

### Invariants And Boundaries

- A lane that was not read, failed or could not be measured never reads as an empty destination or a zero.
- Hunk totals never change a file total: the totals line reports files, hunks and non-text changes separately.
- Nothing here assesses, approves or explains a change.

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No domain documentation source is configured; the requirement packet `MIK-R32@v1` and its rulings live outside the code
and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The two destinations and what each lists, in the module's own words. [1]
- The destination on screen and the file it opened. [2]
- The rail line: pending, unavailable, not measured or the totals. [3]
- The rail nodes. [4]
- The center and its read states. [5]
- The two groups, each with its note. [6]
- A row's counts, the focused file, and the reason one click away. [7]
- Where the workspace mounts the rail nodes and the center. [8]
- The rows in the server's order, and a focused hunk. [9]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
