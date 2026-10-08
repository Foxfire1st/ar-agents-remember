# dashboard/src/panels/session-cockpit/conversation/conversation-timeline/baseline.test.tsx

## Governing Overview

[session-cockpit/conversation overview](../overview.md)

## Purpose

The 10k tool-heavy DOM/interaction baseline suite split from `renderer.test.tsx` by
the 260731-EFA-L8 test split. Pins the R5.2/R5.10/L4.4 bounded-DOM invariant and the
axe pass at depth.

## Code Commentary

### Logic

Mounts 10,000 rotating items through the landed renderer and asserts the mounted DOM
stays bounded (`> 0`, `< 80`, AND `< total/100`), `aria-posinset` rides the 1-based
server ordinal, `aria-setsize="10000"` is honest, and a second `it` runs axe over
the deep feed.

### Invariants And Boundaries

The baseline asserts mounted DOM size, ordinal/ARIA honesty and accessibility at depth. It has no elapsed mount-time ceiling: the bounded DOM is the portable correctness assertion, and this jsdom suite makes no browser latency claim.

### Todos

None recorded.

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

No relevant domain documentation was found.

### Repo-Internal References

- The 10k baseline suite. [1]

### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.
