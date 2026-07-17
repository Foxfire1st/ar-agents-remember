# dashboard/src/panels/session-cockpit/VirtualizedInspectorList.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/VirtualizedInspectorList.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-17T23:54+02:00 |
| lastVerifiedCommitHash | `882fed5806d5698f05c700e39ccae5da53c29176` |
| lastVerifiedCommitDate | 2026-07-18T00:12:18+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

Provides one inspector-ledger renderer that keeps ordinary DOM list semantics through 100 rows and
switches to TanStack virtualization above that threshold without truncating the represented total.

## Code Commentary

### Logic

- At 100 rows or fewer, every row is an ordinary `ul`/`li`, preserving find and assistive-technology
  behavior for the common case.
- Above 100, the scroll viewport uses `useVirtualizer`, stable caller-supplied keys, measured rows,
  overscan, total height, and `aria-posinset`/`aria-setsize` for the retained logical set.
- Both paths share the same 2px amber raw-ledger grammar and item renderer.

### Invariants And Boundaries

- Virtualization is a rendering boundary, never a data cap; callers pass the full ordered rows.
- Interactive row state must live above this component because offscreen rows may unmount.
- Stable `rowKey` identity is required for correct row association.

### Todos

The leaf report records a nonblocking jsdom shutdown-timer flake seen only during one concurrent
full-suite/typecheck run; standalone full-suite reruns passed.

## Docs References

No Domain Documentation source is configured.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No external domain citation applies. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Threshold, ordinary list, and virtualized list implementations. | L7-L107 | [VirtualizedInspectorList.tsx](VirtualizedInspectorList.tsx) |
| Bus caller that lifts interaction state above virtual rows. | L116-L222 | [BusPane.tsx](BusPane.tsx) |
| Evidence caller for large set/receipt ledgers. | L169-L374 | [EvidencePane.tsx](EvidencePane.tsx) |

## Cross-Repo References

No meaningful cross-repo boundary is owned here.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No cross-repo evidence applies. | — | — |

## Update History

- 2026-07-17T23:54+02:00 — Created for 260715-FEUI-L7 after Round 3 reviewer PASS. Documents the
  100/101 threshold, accessible logical total, and caller-owned interaction-state boundary.
  Verification metadata remains pinned to the leaf base until closeout.
