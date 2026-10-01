# dashboard/src/panels/session-cockpit/sessions-view/launchAndKeepAlive.test.tsx

## Governing Overview

[panels/session-cockpit overview](../overview.md)

## Purpose

The launch-flow + keep-alive suite split from `SessionsView.test.tsx` by the
260731-EFA-L8 test split. Pins the L3 R5/R6 launch flow with the failed-launch
banner, and the B1 harness↔terminal contract that keeps the PTY stack alive through
focus handoffs.

## Code Commentary

### Logic

Seeds launch attempts and asserts the five-tier launch evidence and failed-launch
verbatim surfaces; then pins the keep-alive rule (the PTY layer stays mounted
through smart-focus handoff).

### Invariants And Boundaries

Assertions preserved from the monolithic suite; terminal ledgers come from
`test-utils.tsx`.

### Todos

None recorded.

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

No relevant domain documentation was found.

### Repo-Internal References

- The launch/keep-alive suite. [1]

### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.
