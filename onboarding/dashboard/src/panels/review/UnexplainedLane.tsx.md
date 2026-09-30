# dashboard/src/panels/review/UnexplainedLane.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/UnexplainedLane.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T20:14:26+02:00 |
| lastVerifiedCommitHash | `d3a22213ad3124603b0210afb7e3d049c5589b82`|
| lastVerifiedCommitDate | 2026-09-30T20:52:55+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

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

## Docs References

No domain documentation source is configured; the requirement packet `MIK-R32@v1` and its rulings live outside the code
and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The two destinations and what each lists, in the module's own words. | "no allowlist or file-type rule hides a file" | dashboard/src/panels/review/UnexplainedLane.tsx:1-13 |
| The destination on screen and the file it opened. | `LaneSelection` | dashboard/src/panels/review/UnexplainedLane.tsx:36-39 |
| The rail line: pending, unavailable, not measured or the totals. | `destinationLine` | dashboard/src/panels/review/UnexplainedLane.tsx:112-119 |
| The rail nodes. | `LaneDestinations` | dashboard/src/panels/review/UnexplainedLane.tsx:121-158 |
| The center and its read states. | `UnexplainedLaneCenter`; `LaneBody` | dashboard/src/panels/review/UnexplainedLane.tsx:170-186; dashboard/src/panels/review/UnexplainedLane.tsx:188-221 |
| The two groups, each with its note. | `DestinationFiles`; `FileGroup` | dashboard/src/panels/review/UnexplainedLane.tsx:223-248; dashboard/src/panels/review/UnexplainedLane.tsx:250-268 |
| A row's counts, the focused file, and the reason one click away. | `rowCounts`; `FileRow`; `RowReason` | dashboard/src/panels/review/UnexplainedLane.tsx:270-280; dashboard/src/panels/review/UnexplainedLane.tsx:282-318; dashboard/src/panels/review/UnexplainedLane.tsx:321-345 |
| Where the workspace mounts the rail nodes and the center. | `RailLaneDestinations`; "<UnexplainedLaneCenter" | dashboard/src/panels/review/ReviewWorkspace.tsx:540-556; dashboard/src/panels/review/ReviewWorkspace.tsx:386-395 |
| The rows in the server's order, and a focused hunk. | "lists unexplained files first, then attributed files, and opens one on its unexplained hunk" | dashboard/src/panels/review/ReviewSurface.lane.test.tsx:101-139 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T20:14:26+02:00 — 260928-MIK-L34 curator (staged change set on `ar/260928-mik-l34`, code base `904e804b07a598d5d6c66f06b7e67ddab64d9b8e`; reviews R1 to R3 changes-required, each followed by a fix round): No content impact: MIK-R34 inserted lines above the lane's mounts in `ReviewWorkspace.tsx`, so the caller row was re-pointed by the exact Git-hunk shift (`498-514` → `540-556`, `349-358` → `386-395`). In the same fixer run three rows citing this card's own unchanged source were normalised into per-declaration ranges. Claims unchanged. No stamp advanced.
- 2026-09-30T14:06:33+02:00 — 260928-MIK-L32 curator (staged change set on `ar/260928-mik-l32`, code base `07d6584afba8a9504e4a3cf2e80eac41f68b28a9`; review R1 pass-with-notes, fixes, R2 pass): created this card for the new lane component MIK-R32 adds (rules 10 and 11). The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
