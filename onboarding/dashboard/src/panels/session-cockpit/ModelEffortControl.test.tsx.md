# dashboard/src/panels/session-cockpit/ModelEffortControl.test.tsx

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

Rendered regression contract for live model/effort sourcing, corrected menus, apply routing, and
visible acceptance words.

## Code Commentary

### Logic

Proves exact-session fetching, effective trigger words, live-harness visibility, verbatim 503/409
failures, fresh-Claude nullable-effort handling, effortless-row re-gating, default pre-highlight,
model-only versus serialized pair apply, preservation of explicit effort, and queued/clamp chips.

### Conventions

Network calls are observed at the component boundary while deterministic capability snapshots and
the real cockpit store drive rendering.

### Invariants And Boundaries

The tests explicitly exclude the pre-session cache, inherited effort menus, implicit default
requests, and color-only acceptance status.

### Todos

The production sev-4 trigger-visual caveat remains documented in `ModelEffortControl.tsx.md`.

## Evidence

### Docs References

No Domain Documentation source is configured.

No external domain citation applies.

### Repo-Internal References

- Sourcing, failure, menu, apply, and chip cases. [1]
- Component under test. [2]
- Capability fixtures. [3]

### Cross-Repo References

No meaningful cross-repo boundary is owned here.

No cross-repo evidence applies.

## Current L5I Maintenance

The control tests now pin model-only trigger output when no current effort is evidenced and retain
the live-menu selection cases that distinguish actual state from launch fallback.
