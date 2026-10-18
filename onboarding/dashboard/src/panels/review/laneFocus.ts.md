# dashboard/src/panels/review/laneFocus.ts

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

Pure attribution-label/count and hunk-line helpers retained across the reviewer's presentation change.
Nothing here classifies: bucket/hunk facts are server-owned. R86 removed destination grouping and focused
lane windows; change-set destinations are comparison filters instead. Surviving explorer-named label
helpers do not imply that a source explorer is still rendered.

State the unexplained-changes lane's shared presentation facts (MIK-R32) apart from its readers: the explorer labels, the open main-page attribution facts and remaining counts, and the hunk line helpers the intent markers reuse. Nothing here classifies: every bucket, hunk and class comes from the server's per-file response.
## Code Commentary

### Logic

- **Hunk lines.** `spanLabel` names a changed range or zero-line gap; `sideLines` splits side text.
  Intent markers retain these helpers for pane line measurement and accessible hunk names. There is no
  `hunkWindow`, focused-hunk cap, destination-grouping or focused-hunk selector API in this module.
- **The explorer's labels (ruling Q1, 2026-09-30T12:19:20).** `EXPLORER_LABELS` maps each bucket to the explorer's
  landed words (`attributed` → `Mapped`, `unexplained` → `Unmapped`, `attribution_unknown` → `Attribution unknown`).
  `EXPLORER_PENDING` retains the pending vocabulary. The former `explorerAttribution` function is gone;
  the constants do not classify or label a currently rendered explorer.
- **The open main-page facts (review R1 F1, ruling 13:07:38).** `laneAttributionFacts(read)` is `pending`,
  `unknown` (an unread or unavailable lane), or `read` with `partial`, the unexplained paths and the unknown paths.
  `laneCountText(name, facts)` labels `unattributed_changed_paths` as `changed files without an invariant`
  and `unknown_attribution_changed_paths` as `changed files of unknown attribution`. Read facts use each
  destination-file list's length with an optional ` (partial)` suffix. Pending facts use `Attribution pending`;
  unknown facts use `the change set could not be measured`. Other count names return `undefined`.

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
- `laneAttributionFacts` retains pending/unknown/read states and derives paths from the two destination file lists with the lane's partial flag. `laneCountText` labels their lengths as changed files without an invariant or changed files of unknown attribution, uses the explicit pending/unmeasured wording above, and returns undefined for names it does not own.
- Earlier focus-window and destination-grouping helpers are gone with the lane's own file views: R86 reads those destinations as filters of the change-set viewer instead.
## Evidence

### Docs References

No domain documentation source is configured; the requirement packet `MIK-R32@v1` and its rulings live outside the code
and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

### Cross-Repo References

No cross-repo boundary is crossed by this file.

- These presentation helpers do not classify; supplied server hunks own the marks' positions. [1]
- spanLabel and sideLines retain range/gap naming and side-text line splitting; no focused-window API is restored. [6]
- Explorer-named constants preserve vocabulary only, not a current explorer implementation. [7]
- Held lane reads preserve pending/unknown/read states; destination file lists, partialness and owned count formatting remain distinct responsibilities. [8]
- IntentMarkers imports and actually calls spanLabel for hunk names/attributes and sideLines for full-side/excerpt extent measurement. [10]
- The current ReviewMainFacts—not the closed technical details—uses held lane facts for openly marked remaining counts and preserves fallback for unowned names. [11]
- Explorer label vocabulary remains the mapped/unmapped/unknown constants. [13]
- Pending vocabulary remains Attribution pending. [14]
- laneAttributionFacts derives paths from the two held destination file lists and keeps loading/unavailable/missing-list states explicit. [15]
- laneCountText replaces raw field prefixes with changed-files-without-an-invariant or unknown-attribution labels, preserves pending/unmeasured wording and partial list lengths, and returns undefined for unowned names. [16]
- Server hunk spans retain single-line/range/zero-line-gap naming. [17]
- Side text splits on newline and removes one final empty split item. [18]
