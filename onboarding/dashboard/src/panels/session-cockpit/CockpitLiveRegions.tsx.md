# dashboard/src/panels/session-cockpit/CockpitLiveRegions.tsx

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

Persistent screen-reader live-region bridge for cockpit polite and assertive announcements.

## Code Commentary

### Logic

Subscribes to both announcer channels and renders one visually hidden `aria-live="polite"` status
and one `aria-live="assertive"` alert. Each persistent region exposes the announcement sequence
through `data-announce-seq`, so identical repeated messages still produce an observable DOM update.

### Conventions

Both regions mount before the first message and remain in the tree; callers publish through the
shared announcer rather than creating local live regions.

### Invariants And Boundaries

Visual toast/chip state is separate from auditory urgency. This component renders text only and
does not decide which events deserve polite or assertive delivery.

### Todos

None recorded; the announcer transition caveat is recorded on `announcer.ts.md`.

## Evidence

### Docs References

No Domain Documentation source is configured.

No external domain citation applies.

### Repo-Internal References

- Persistent polite/assertive DOM bridge. [1]
- Mount-before-message and repeated-message coverage. [2]
- Refcounted announcement stores. [3]

### Cross-Repo References

No meaningful cross-repo boundary is owned here.

No cross-repo evidence applies.

## FEUI-L8 Reviewed Candidate Delta

Polite and assertive messages render through sequence-keyed spans. Repeating identical text therefore replaces an accessibility-tree node instead of relying on an unchanged text node.

The reviewed candidate is still uncommitted. Existing verification hash/date remain pinned to the
leaf base; closeout owns commit stamping.
