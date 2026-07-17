# dashboard/src/panels/session-cockpit/VirtualizedInspectorList.test.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/VirtualizedInspectorList.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-17T23:54+02:00 |
| lastVerifiedCommitHash | `882fed5806d5698f05c700e39ccae5da53c29176` |
| lastVerifiedCommitDate | 2026-07-18T00:12:18+02:00|
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

| Finding | Citations | Source Path |
| --- | --- | --- |
| No external domain citation applies. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| 100-row ordinary DOM case. | L44-L50 | [VirtualizedInspectorList.test.tsx](VirtualizedInspectorList.test.tsx) |
| 101-row virtualized logical-total case. | L51-L63 | [VirtualizedInspectorList.test.tsx](VirtualizedInspectorList.test.tsx) |
| Component under test. | L39-L107 | [VirtualizedInspectorList.tsx](VirtualizedInspectorList.tsx) |

## Cross-Repo References

No meaningful cross-repo boundary is owned here.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No cross-repo evidence applies. | — | — |

## Update History

- 2026-07-17T23:54+02:00 — Created for 260715-FEUI-L7 after Round 3 reviewer PASS. Verification
  metadata remains pinned to the leaf base until closeout.
