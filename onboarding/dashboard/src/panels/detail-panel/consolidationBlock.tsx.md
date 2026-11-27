# dashboard/src/panels/detail-panel/consolidationBlock.tsx

## Governing Overview

[Panels overview](../overview.md)

## Purpose

Renders the task detail page's Consolidation summary block, full-list drill-down body, and header count string from the server-projected `TaskConsolidationNode`.

## Code Commentary

`ConsolidationBlock` returns `null` when `consolidation` is absent; otherwise it displays aggregate outcome counts (`OutcomeCounts`), the listed family/rule summary plus a warning notice when `memoryRead` is false (`ListedLine`), the first `REVIEW_INLINE_BOUND` subject rows inline (`ConsolidationRow`), and a counted `MoreLink` opening `{ kind: 'consolidation' }`. When `memoryRead` is false, `outcomeCountsText` and `OutcomeCounts` display `<total> listed · outcomes not known yet`, and `ConsolidationRow` labels open rows as `listed` instead of `open`. Outcome tones mirror the Review block (`stands` -> `dim`, `corrected` -> default, `unresolved` -> `warn`, `open` -> `muted`), and each row combines optional `member of <family>` with `row.reason`. `ConsolidationViewBody` renders all rows for the drill-down view or a placeholder message while body rows have not arrived yet.

## Relationships

Consumed by `dashboard/src/panels/detail-panel/taskReader.tsx` (`ConsolidationBlock`) and `dashboard/src/panels/detail-panel/docViews.tsx` (`ConsolidationViewBody`, `outcomeCountsText`). Shares layout primitives and styles from `./pageParts`, `./pageStyles`, and `REVIEW_INLINE_BOUND` from `./taskBlocks`, and consumes `TaskConsolidationNode`/`TaskConsolidationRowNode` from `../../types/projection` populated by `serving/projections/snapshots_impl/_task_consolidation.py`.

## Evidence

- `outcomeCountsText` formats the one-line header summary, distinguishing unread memory (`<total> listed · outcomes not known yet`) from live `stands`/`corrected`/`unresolved`/`open` counts. [1]
- `ConsolidationRow` renders each subject with its outcome tone, switching an `open` badge to `listed` when `memoryRead` is false, and joins family membership with the row reason. [2]
- `ConsolidationBlock` hides itself without consolidation data, caps inline subjects at `REVIEW_INLINE_BOUND`, and exposes a counted link to `{ kind: 'consolidation' }`. [3]
- `ConsolidationViewBody` renders the complete subject list in the drill-down view or a loading placeholder when `rows` have not arrived with the document body. [4]
