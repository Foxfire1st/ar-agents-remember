# dashboard/src/panels/session-cockpit/VirtualizedInspectorList.test.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/VirtualizedInspectorList.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-17T23:54+02:00 |
| lastVerifiedCommitHash | `7c56c11d651972515723b4090b8174087eb5236f` |
| lastVerifiedCommitDate | 2026-08-07T20:50:27+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

Pins the exact 100-row ordinary-DOM boundary and proves that 101 rows enter virtualization while
retaining the full accessible set size.

## Code Commentary

### Logic

- The 100-row case expects ordinary list items and `data-virtualized=false`.
- The 101-row case installs the jsdom geometry seam, expects virtualization, and asserts logical
  total/position semantics rather than requiring every row in the DOM.

### Invariants And Boundaries

- The boundary is strictly `> 100`, not `>= 100`.
- Tests distinguish logical data retention from physical DOM retention.

### Todos

None recorded; the task-local concurrent jsdom shutdown residual is tracked in the curator report.

## Docs References

No Domain Documentation source is configured.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain citation applies. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| 100-row ordinary DOM case. | "keeps 100 rows as ordinary DOM list items" | dashboard/src/panels/session-cockpit/VirtualizedInspectorList.test.tsx:44-49 |
| 101-row virtualized logical-total case. | "virtualizes past 100 without slicing the accessible total" | dashboard/src/panels/session-cockpit/VirtualizedInspectorList.test.tsx:51-62 |
| Component under test. | `VirtualizedInspectorList` | dashboard/src/panels/session-cockpit/VirtualizedInspectorList.tsx:39-106 |

## Cross-Repo References

No meaningful cross-repo boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo evidence applies. | — | — |

## Update History

- 2026-08-04T11:40:58+02:00 — 260731-EFA-L6 S18-B08 curator: bound both threshold cases and the component row to current test/function anchors.

- 2026-07-17T23:54+02:00 — Created for 260715-FEUI-L7 after Round 3 reviewer PASS. Verification
  metadata remains pinned to the leaf base until closeout.
