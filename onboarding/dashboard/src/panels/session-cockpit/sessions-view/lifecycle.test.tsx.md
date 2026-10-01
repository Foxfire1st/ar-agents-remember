# dashboard/src/panels/session-cockpit/sessions-view/lifecycle.test.tsx

## Governing Overview

[panels/session-cockpit overview](../overview.md)

## Purpose

The lifecycle/session suite split from `SessionsView.test.tsx` by the
260731-EFA-L8 test split. Pins the S5 legacy-duty parity, smart-default focus +
handoff + session cycling (L2 R9/F17), authoritative landed cleanup through rail
and palette callers (F5-S5-2), and the planned-retirement window rule (a retired seat
closes its own rail window while a bare `terminated` row and a landed session keep theirs).

## Code Commentary

### Logic

Seeds legacy/ready sessions via `test-utils.tsx` and asserts duty parity, focus
handoff, cycling, the cleanup callers' authority, and — in the fourth suite — that
retirement provenance (`retiredAt`/`retiredBySession`/`retiredReason`/`retiredEdge`)
closes a rail window that a bare `terminated` mark leaves open.

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

- The lifecycle file contains the legacy-duty, smart-default/handoff, authoritative landed-cleanup, and planned-retirement-window suites. [1]

### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.
