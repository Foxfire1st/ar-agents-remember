# dashboard/src/panels/review/laneFocus.ts

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

Pure attribution-label/count and hunk-line helpers retained across the reviewer's presentation change.
Nothing here classifies: bucket/hunk facts are server-owned. R86 removed destination grouping and focused
lane windows; change-set destinations are comparison filters instead. Surviving explorer-named label
helpers do not imply that a source explorer is still rendered.

State the unexplained-changes lane's shared presentation facts (MIK-R32) apart from its readers: the explorer labels, the technical details' attribution facts and remaining counts, and the hunk line helpers the intent markers reuse. Nothing here classifies: every bucket, hunk and class comes from the server's per-file response.
## Code Commentary

### Logic

- **Hunk lines.** `spanLabel` names a changed range or zero-line gap; `sideLines` splits side text.
  Intent markers retain these helpers for pane line measurement and accessible hunk names. There is no
  `hunkWindow`, focused-hunk cap, destination-grouping or focused-hunk selector API in this module.
- **The explorer's labels (ruling Q1, 2026-09-30T12:19:20).** `EXPLORER_LABELS` maps each bucket to the explorer's
  landed words (`attributed` → `Mapped`, `unexplained` → `Unmapped`, `attribution_unknown` → `Attribution unknown`).
  `EXPLORER_PENDING` retains the pending vocabulary. The former `explorerAttribution` function is gone;
  the constants do not classify or label a currently rendered explorer.
- **The technical details' facts (review R1 F1, ruling 13:07:38).** `laneAttributionFacts(read)` is `pending`,
  `unknown` (an unread or unavailable lane), or `read` with `partial`, the unexplained paths and the unknown paths.
  `laneCountText(name, facts)` states the landed remaining counts `unattributed_changed_paths` and
  `unknown_attribution_changed_paths` from the lane (the count of each list, marked `(partial)`), or pending or
  unknown; other counts return `undefined` and keep the landed text.

### Conventions

- Pure functions over the served shapes; no fetch, no state.
- Explorer-named helpers retain vocabulary compatibility, not a UI explorer ownership claim.

### Invariants And Boundaries

- Attribution facts/counts are taken from the held server lane, never reclassified in a label helper.
- Full-file/card intent markers retain owner hunk line measurement. The removed `LaneFileFocus` window
  surface is not a current integration or proof claim.

### Todos

No remaining focused-window implementation is asserted by this card; R86 replaced that reading surface.

- `EXPLORER_LABELS`/`EXPLORER_PENDING` retain bucket/pending vocabulary for surviving count text, not a claim that a lane and explorer are still rendered.
- `laneAttributionFacts` turns a lane read into `pending`, `unknown` (unread or unavailable) or the read paths of each bucket with the lane's partial flag; `laneCountText` states the held lane's remaining counts from those facts, and answers undefined for counts the lane does not own, keeping the landed text.
- Earlier focus-window and destination-grouping helpers are gone with the lane's own file views: R86 reads those destinations as filters of the change-set viewer instead.
## Evidence

### Docs References

No domain documentation source is configured; the requirement packet `MIK-R32@v1` and its rulings live outside the code
and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- Nothing here classifies; marks sit on the owner's hunks. [1]

- spanLabel and sideLines retain server-side hunk naming and pane line measurement; the focused-window API is retired. [6]
- Bucket and pending constants retain compatible vocabulary without a rendered explorer or explorerAttribution function. [7]
- The technical details' facts and counts from the lane (review F1). [8]

- The intent markers' use of the window helpers (MIK-L34). [10]
- The details' counts and lists from the lane. [11]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
- Explorer labels in the explorer's landed words [13]
- Pending label while the lane is read [14]
- Technical-details attribution facts from the lane [15]
- Remaining counts as the lane states them [16]
- Hunk side-line naming reused by markers [17]
- Side-text splitting reused by marker panes [18]
