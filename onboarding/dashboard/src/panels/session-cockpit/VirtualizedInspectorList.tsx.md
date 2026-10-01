# dashboard/src/panels/session-cockpit/VirtualizedInspectorList.tsx

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

## Evidence

### Docs References

No Domain Documentation source is configured.

No external domain citation applies.

### Repo-Internal References

- Threshold, ordinary list, and virtualized list implementations. [1]
- Bus caller that lifts interaction state above virtual rows. [2]
- Evidence caller for large set/receipt ledgers. [3]

### Cross-Repo References

No meaningful cross-repo boundary is owned here.

No cross-repo evidence applies.
