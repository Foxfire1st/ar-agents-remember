# dashboard/src/panels/session-cockpit/StateDot.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/session-cockpit/StateDot.tsx` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-17T02:30+02:00                           |
| lastVerifiedCommitHash | `e2b99dcd71fb6ca31f642dd61c3c16f3d3d05bf5`       |
| lastVerifiedCommitDate | 2026-07-17T02:52:07+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

The **cockpit state dot** (260715-FEUI-L2 R14) — the ONLY renderer of `data/stateGrammar` visuals.
Every surface (rail rows, HeaderStrip, SeatInspector; the L7 StatusLine when it arrives) renders
THIS component from the same mapping, so a seat's dot can never disagree across surfaces.

## Code Commentary

### Logic

- The `dot` cva (L8-L36): 0.6em circle, color variants over the grammar's podracer roles (the
  mutedAmber via `color-mix` on the amber token — no new token); the `pulse: true` variant carries
  the LITERAL `animation: "pulseSlow 2.4s ease-in-out infinite"` — a literal for Panda's static
  extraction; `stateGrammar.PULSE_ANIMATION` is the same string and the cross-surface consistency
  test pins the two together — plus `_motionReduce: { animation: "none" }` (steady under
  prefers-reduced-motion, never hidden).
- `StateDot({state, testId})` (L38-L49): renders the span with `data-state`/`data-state-color`/
  `data-state-pulse` attributes (the cross-surface test's comparison surface), `aria-hidden` (the
  dot is reinforced by the state word/chips, never the only signal).

### Invariants And Boundaries

- Pulse is frozen by the unlayered `html[data-effects="off"]` rule (`index.css`) AND steady under
  reduced motion — both gates verified in review.
- The Panda animation literal and `PULSE_ANIMATION` must stay byte-identical; change the ruling in
  `stateGrammar.ts` first, then here, and the pinning test must be updated deliberately.
- No consumer may style its own dot; new surfaces import this component.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The cva variants + the attribute-carrying renderer. | L8-L49 | [StateDot.tsx](StateDot.tsx) |
| The grammar whose visuals this renders (single source). | L44-L106 | [../../data/stateGrammar.ts](../../data/stateGrammar.ts) |
| The `pulseSlow` keyframe + the sovereign effects-off freeze. | L91-L98 | [../../index.css](../../index.css) |
| The cross-surface consistency test (rail dot ≡ HeaderStrip dot). | L325-L338 | [SessionRail.test.tsx](SessionRail.test.tsx) |

## Update History

- 2026-07-17T02:30+02:00 — Created for 260715-FEUI-L2 (R14): the single grammar renderer —
  color/pulse cva with the Panda-literal 2.4 s ease-in-out pulse pinned to
  `stateGrammar.PULSE_ANIMATION`, reduced-motion steadiness, and the data-state attributes the
  cross-surface test compares. Verification metadata pinned to the leaf base until closeout
  stamps the L2 code commit.
