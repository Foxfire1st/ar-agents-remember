# dashboard/src/panels/session-cockpit/SeatInspector.test.tsx

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

Pins the integrated inspector contract: accessible tab navigation, native hidden semantics,
off-tab Bus interaction continuity, no-focus honesty, and the carried-forward L6/L4 evidence rules.

## Code Commentary

### Logic

- Keyboard tests cover Right/Left wrap, Home/End focus movement, selected state, and stable tabpanel
  relationships.
- Draft, posted, and retained-error cases prove the same Bus instances settle on exact `entryId`s
  while the panel is inactive. Accessibility queries prove hidden controls leave the active tree.
- No-focus coverage keeps fleet Bus rows reachable while Evidence/Capabilities state their limits.
- Carried-forward cases pin archetype/raw evidence, informational retire residuals, newest-first set
  lines, explicit mark seen, and the rule that render or seat changes do not acknowledge.

### Invariants And Boundaries

- State continuity must be tested through real tab transitions, not an isolated pane render.
- Native `hidden` semantics and mounted-instance persistence are both required.

### Todos

None recorded; browser integration smoke remains a leaf-level residual.

## Evidence

### Docs References

No Domain Documentation source is configured.

No external domain citation applies.

### Repo-Internal References

- Tab navigation and hidden-panel draft retention. [1]
- Off-tab success/error settlement and no-focus Bus. [2]
- Carried L6 evidence cases. [3]
- Explicit mark-seen and seat-switch regressions. [4]
- Composition host under test. [5]

### Cross-Repo References

No meaningful cross-repo boundary is owned here.

No cross-repo evidence applies.
