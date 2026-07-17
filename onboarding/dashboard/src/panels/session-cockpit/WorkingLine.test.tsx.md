# dashboard/src/panels/session-cockpit/WorkingLine.test.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/session-cockpit/WorkingLine.test.tsx` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-17T21:39+02:00 |
| lastVerifiedCommitHash | `f8196d98982f834d68152d307ff8025ea69440d5`       |
| lastVerifiedCommitDate | 2026-07-17T22:08:10+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

The jsdom WorkingLine suite (260715-FEUI-L6 R6/R9): the turn theater's honesty contract asserted
with a frozen clock (`now` prop) over the shared `L6_CONTROLLED_WORKING` fixture.

## Code Commentary

### Logic

- **`formatApproxElapsed`** (L33-L41): ~-labeled at every magnitude (`~9s`, `~119s`, `~2m14s`,
  `~1h02m`), clamped at `~0s` for negatives.
- **Render gate** (L44-L54): a `turn-ended` seat renders NOTHING; the working seat renders the
  line.
- **Never whimsy** (L56-L61): with no real activity form the verb is exactly `working`.
- **Elapsed honesty** (L63-L73): `~2m14s` from `workingSince`, the sweep-bound tooltip present;
  `workingSince: null` ⇒ the elapsed span is ABSENT (never a fake clock).
- **Welded stop** (L75-L83): `disabled === true`, `data-disabled-reason` is the exact
  `STOP_TURN_DISABLED_REASON`, the title names UA-7.
- **Spinner ruling** (L85-L94): aria-hidden `◐` only, and `PULSE_ANIMATION` pinned to the ruled
  `pulseSlow 2.4s ease-in-out infinite` literal — the drift net for the component's hard-coded
  Panda string (jsdom cannot assert the rendered animation; the constant pin is the acknowledged
  proxy).

### Invariants And Boundaries

`cockpitWorkingSince` builds a minimal `PerSessionCockpit` by hand — the suite depends on the
store SHAPE, not the store. FEUI-L4 therefore added only the required `snapshotLoading: false`
and empty `echoEvidence` defaults; WorkingLine behavior and assertions are unchanged. Test-only.

## Docs References

No Domain Documentation source is configured for this repository; repository code and tests are the authority.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured live domain-documentation source was available. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The component + pure formatter under test. | L57-L129 | [WorkingLine.tsx](WorkingLine.tsx) |
| The ruled pulse constant the spinner case pins. | L14 | [../../data/stateGrammar.ts](../../data/stateGrammar.ts) |
| The UA-7 reason asserted verbatim. | L52 | [lifecycleCopy.ts](lifecycleCopy.ts) |
| The working fixture. | L179-L194 | [../../test/fixtures/catalogRows.ts](../../test/fixtures/catalogRows.ts) |
| The view-level cases (slot containment, `turn.stop` gate alignment). | L320-L400 | [SessionsView.test.tsx](SessionsView.test.tsx) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| This file implements a repository-local contract. | — | — |

## 260715-FEUI-L5 Reliable Submit Delta

No WorkingLine behavior changed. Its session fixture gained empty `submitHistory` for the expanded
cockpit state; working-line liveness/stream assertions remain semantically unchanged.

## Update History

- 2026-07-17T21:39+02:00 — FEUI-L5 fixture-only refresh; no WorkingLine semantic impact.

- 2026-07-17T08:33+02:00 — No content impact: 260715-FEUI-L4 only extended this hand-built
  store-shape fixture with `snapshotLoading` and `echoEvidence`; the WorkingLine contract is
  unchanged. Verification metadata is pinned to the contract base until code commit.
- 2026-07-17T04:20+02:00 — Created for 260715-FEUI-L6 R6/R9 (6 cases): the ~-labeled formatter
  matrix, working-only render, plain-"working" (never whimsy), elapsed presence/omission with
  the sweep-bound tooltip, the welded disabled stop with the exact UA-7 reason, and the
  pulse-literal pin. Verification metadata pinned to the leaf base until closeout stamps the L6
  code commit.
