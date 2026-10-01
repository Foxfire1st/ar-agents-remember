# dashboard/src/panels/session-cockpit/CockpitLiveRegions.test.tsx

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

Accessibility regression contract for the cockpit's persistent dual live regions.

## Code Commentary

### Logic

Proves that both urgency channels exist before any announcement, that messages route to the
correct region, and that repeated identical messages advance the sequence.

### Conventions

The suite exercises the real announcer stores and clears state around each case.

### Invariants And Boundaries

Polite and assertive regions remain distinct and mounted; repeat delivery cannot rely on text
changing.

### Todos

None recorded.

## Evidence

### Docs References

No Domain Documentation source is configured.

No external domain citation applies.

### Repo-Internal References

- Dual-region and repeated-message cases. [1]
- Component under test. [2]
- Announcement store under test. [3]

### Cross-Repo References

No meaningful cross-repo boundary is owned here.

No cross-repo evidence applies.
