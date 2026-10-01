# dashboard/src/panels/session-cockpit/conversation/conversation-timeline/scrollMemory.test-utils.tsx

## Governing Overview

[session-cockpit/conversation overview](../overview.md)

## Purpose

The describe-scoped geometry and timer-hygiene shim for the split scroll-memory suites, extracted
from `renderer.test.tsx` by the 260731-EFA-L8 split. `installScrollMemoryGeometry` stubs the DOM
geometry the virtualizer needs and keeps every suite case on fake timers; teardown unmounts all
renders, clears pending Virtualizer debounce callbacks, and only then restores real timers.
`feedOf`/`pinGeometry` build feeds and pin viewport geometry for the assertions.

## Code Commentary

### Logic

`alignedTops` records the stubbed row tops; `pinGeometry` sets scrollHeight/clientHeight so
scroll-restore assertions are deterministic. The before/after hooks deliberately bracket both
React cleanup and timer restoration: TanStack's scroll-observer unsubscribe removes listeners but
does not cancel its pending 150 ms debounce, so switching to real timers before unmount can let a
callback outlive jsdom and call React after `window` is gone.

### Conventions

Test-only; installed per describe scope.

### Invariants And Boundaries

Must be restored/installed per suite to avoid leaking geometry or timer callbacks across test
files. Renders must be unmounted and pending fake timers discarded before real timers return.

### Todos

None recorded.

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

No relevant domain documentation was found.

### Repo-Internal References

- The geometry and hermetic timer hooks, plus the feed and viewport helpers. [1]

### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.
