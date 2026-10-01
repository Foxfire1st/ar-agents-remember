# dashboard/src/panels/session-cockpit/WorkingLine.test.tsx

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

The jsdom WorkingLine suite (260715-FEUI-L6 R6/R9): the turn theater's honesty contract asserted
with a frozen clock (`now` prop) over the shared `L6_CONTROLLED_WORKING` fixture.

## Code Commentary

### Logic

- **`formatApproxElapsed`** cit:([`formatApproxElapsed`], dashboard/src/panels/session-cockpit/WorkingLine.test.tsx:36-44): ~-labeled at every magnitude (`~9s`, `~119s`, `~2m14s`,
  `~1h02m`), clamped at `~0s` for negatives.
- **Render gate** cit:(["renders ONLY while the seat state is working"], dashboard/src/panels/session-cockpit/WorkingLine.test.tsx:47-57): a `turn-ended` seat renders NOTHING; the working seat renders the
  line.
- **Never whimsy** cit:(["says plain 'working' when no real activity form is known — never a whimsy verb"], dashboard/src/panels/session-cockpit/WorkingLine.test.tsx:59-64): with no real activity form the verb is exactly `working`.
- **Elapsed honesty** cit:(["shows the ~elapsed from the client turnClock"], dashboard/src/panels/session-cockpit/WorkingLine.test.tsx:66-76): `~2m14s` from `workingSince`, the sweep-bound tooltip present;
  `workingSince: null` ⇒ the elapsed span is ABSENT (never a fake clock).
- **Welded stop** cit:(["keeps the line-hosted stop for the raw-terminal path"], dashboard/src/panels/session-cockpit/WorkingLine.test.tsx:85-98): `disabled === true`, `data-disabled-reason` is the exact
  `STOP_TURN_DISABLED_REASON`, the title names UA-7.
- **Spinner ruling** cit:([`PULSE_ANIMATION`], dashboard/src/panels/session-cockpit/WorkingLine.test.tsx:100-109): aria-hidden `◐` only, and `PULSE_ANIMATION` pinned to the ruled
  `pulseSlow 2.4s ease-in-out infinite` literal — the drift net for the component's hard-coded
  Panda string (jsdom cannot assert the rendered animation; the constant pin is the acknowledged
  proxy).

### Invariants And Boundaries

`cockpitWorkingSince` builds a minimal `PerSessionCockpit` by hand — the suite depends on the
store SHAPE, not the store. FEUI-L4 therefore added only the required `snapshotLoading: false`
and empty `echoEvidence` defaults; WorkingLine behavior and assertions are unchanged. Test-only.

## Evidence

### Docs References

No Domain Documentation source is configured for this repository; repository code and tests are the authority.

No configured live domain-documentation source was available.

### Repo-Internal References

- The component + pure formatter under test. [1]
- The ruled pulse constant the spinner case pins. [2]
- The UA-7 reason asserted verbatim. [3]
- The working fixture. [4]
- The view-level cases (slot containment, `turn.stop` gate alignment). [5]

### Cross-Repo References

No meaningful cross-repo references found.

This file implements a repository-local contract.

## 260715-FEUI-L5 Reliable Submit Delta

No WorkingLine behavior changed. Its session fixture gained empty `submitHistory` for the expanded
cockpit state; working-line liveness/stream assertions remain semantically unchanged.

## Current L5I Maintenance

The fallback-line suite now distinguishes the absent interrupt (no control) from an unavailable
wired interrupt (disabled honest control), retaining raw-terminal stop behavior without duplicating
the controlled composer action.
