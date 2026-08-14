# dashboard/src/panels/session-cockpit/VirtualizedInspectorList.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/VirtualizedInspectorList.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-17T23:54+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain citation applies. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Threshold, ordinary list, and virtualized list implementations. | `INSPECTOR_VIRTUALIZE_THRESHOLD` | dashboard/src/panels/session-cockpit/VirtualizedInspectorList.tsx:11-11 |
| Bus caller that lifts interaction state above virtual rows. | `pickupMatchesFocusedSeat` | dashboard/src/panels/session-cockpit/BusPane.tsx:46-60 |
| Evidence caller for large set/receipt ledgers. | `setLedgerEntryLine`; `submitEvidenceLines` | dashboard/src/panels/session-cockpit/EvidencePane.tsx:36-43; dashboard/src/panels/session-cockpit/EvidencePane.tsx:102-112 |

## Cross-Repo References

No meaningful cross-repo boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo evidence applies. | — | — |

## Update History
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: reviewed this sidecar against the frontend-rail change set (strict-target lint remediation: complexity, max-lines-per-function, react-hooks, jsx-a11y, and import-cycle fixes). No content impact: behavior-preserving refactor; the file's responsibilities and the claims in this card remain current. Verification metadata stays pinned until closeout stamps the code commit.

- 2026-08-02T17:12:10+02:00 — W1-B04 curator: repaired 3 citation claims; scoped recheck clean (0 findings).

- 2026-07-17T23:54+02:00 — Created for 260715-FEUI-L7 after Round 3 reviewer PASS. Documents the
  100/101 threshold, accessible logical total, and caller-owned interaction-state boundary.
  Verification metadata remains pinned to the leaf base until closeout.
