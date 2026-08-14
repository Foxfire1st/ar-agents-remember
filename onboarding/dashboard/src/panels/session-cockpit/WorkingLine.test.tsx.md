# dashboard/src/panels/session-cockpit/WorkingLine.test.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/session-cockpit/WorkingLine.test.tsx` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-07-24T13:17:17Z |
| lastVerifiedCommitHash | `100b40d6be4a7d03eedbb1164ce54e2e8a314038`       |
| lastVerifiedCommitDate | 2026-08-14T08:23:37+02:00|
| governingOverview      | `overview.md`                                    |

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

## Docs References

No Domain Documentation source is configured for this repository; repository code and tests are the authority.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live domain-documentation source was available. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The component + pure formatter under test. | `formatApproxElapsed` | dashboard/src/panels/session-cockpit/WorkingLine.tsx:80-86 |
| The ruled pulse constant the spinner case pins. | `PULSE_ANIMATION` | dashboard/src/data/stateGrammar.ts:14-14 |
| The UA-7 reason asserted verbatim. | `STOP_TURN_DISABLED_REASON` | dashboard/src/panels/session-cockpit/lifecycleCopy.ts:65-66 |
| The working fixture. | `L6_CONTROLLED_WORKING` | dashboard/src/test/fixtures/catalogRows.ts:245-257 |
| The view-level cases (slot containment, `turn.stop` gate alignment). | "renders the WorkingLine in the reserved slot ONLY for a working focused seat" | dashboard/src/panels/session-cockpit/sessions-view/stageSurface.test.tsx:144-144 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| This file implements a repository-local contract. | — | — |

## 260715-FEUI-L5 Reliable Submit Delta

No WorkingLine behavior changed. Its session fixture gained empty `submitHistory` for the expanded
cockpit state; working-line liveness/stream assertions remain semantically unchanged.

## Current L5I Maintenance

The fallback-line suite now distinguishes the absent interrupt (no control) from an unavailable
wired interrupt (disabled honest control), retaining raw-terminal stop behavior without duplicating
the controlled composer action.

## Update History

- 2026-08-04T18:16+02:00 — 260731-EFA-L6 S18-B16 curator: repaired 5 citation rows and rewrote 6 superseded prose line citations as cit: forms; the suite had shifted, so the case ranges are re-pinned to the frozen source (formatter L36-L44 kept; render gate L47-L57, never-whimsy L59-L64, elapsed L66-L76, welded stop L85-L98, spinner L100-L109). Scoped fixer + non-fixing recheck green under the frozen snapshot; verification metadata unchanged.

- 2026-07-31T17:48+02:00 — 260731-EFA-L2 curator: re-derived the stale `formatApproxElapsed`
  self-citation — the formatter matrix `describe` is now L36-L44 (was L33-L41) after the hand-built
  session fixture gained `submitHistory`. The assertions it names are unchanged.

- 2026-07-24T13:17:17Z — Curator: recorded fallback working-line stop ownership regressions;
  verification fields remain pre-commit.

- 2026-07-17T21:39+02:00 — FEUI-L5 fixture-only refresh; no WorkingLine semantic impact.

- 2026-07-17T08:33+02:00 — No content impact: 260715-FEUI-L4 only extended this hand-built
  store-shape fixture with `snapshotLoading` and `echoEvidence`; the WorkingLine contract is
  unchanged. Verification metadata is pinned to the contract base until code commit.
- 2026-07-17T04:20+02:00 — Created for 260715-FEUI-L6 R6/R9 (6 cases): the ~-labeled formatter
  matrix, working-only render, plain-"working" (never whimsy), elapsed presence/omission with
  the sweep-bound tooltip, the welded disabled stop with the exact UA-7 reason, and the
  pulse-literal pin. Verification metadata pinned to the leaf base until closeout stamps the L6
  code commit.
