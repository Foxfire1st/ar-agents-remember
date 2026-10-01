# dashboard/src/panels/session-cockpit/conversation/conversation-timeline/upscrollAnchor.test.tsx

## Governing Overview

[session-cockpit/conversation overview](../overview.md)

## Purpose

The upscroll-anchor suite split from `renderer.test.tsx` by the 260731-EFA-L8 test
split. Pins the B3 upscroll anchor preservation: the reader's visible row survives
older-page prepends and measurement changes.

## Code Commentary

### Logic

Prepends older pages while the reader is scrolled up and asserts the anchored row
stays at the same visual position.

### Invariants And Boundaries

Assertions preserved from the monolithic suite.

### Todos

None recorded.

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

No relevant domain documentation was found.

### Repo-Internal References

- The upscroll-anchor suite. [1]

### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.
