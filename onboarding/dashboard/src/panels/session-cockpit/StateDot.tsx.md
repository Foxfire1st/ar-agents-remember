# dashboard/src/panels/session-cockpit/StateDot.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/session-cockpit/StateDot.tsx` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-17T08:33+02:00                           |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060`       |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

The **cockpit state dot** (260715-FEUI-L2 R14) — the ONLY renderer of `data/stateGrammar` visuals.
Every dot surface (rail rows, HeaderStrip; the L7 StatusLine when it arrives) renders THIS
component from the same mapping, so a seat's dot can never disagree across surfaces. SeatInspector
consumes the same grammar word without rendering a dot.

## Code Commentary

### Logic

- The cit:([`dot`], dashboard/src/panels/session-cockpit/StateDot.tsx:8-36): 0.6em circle, color variants over the grammar's podracer roles (the
  mutedAmber via `color-mix` on the amber token — no new token); the `pulse: true` variant carries
  the LITERAL `animation: "pulseSlow 2.4s ease-in-out infinite"` — a literal for Panda's static
  extraction; `stateGrammar.PULSE_ANIMATION` is the same string and the cross-surface consistency
  test pins the two together — plus `_motionReduce: { animation: "none" }` (steady under
  prefers-reduced-motion, never hidden).
- cit:([`StateDot`], dashboard/src/panels/session-cockpit/StateDot.tsx:38-61) renders the comparison attributes and has
  two deliberate accessibility modes. With a label (rail), it is `role="img"` and speaks the
  state word; without one (HeaderStrip, where the word is adjacent), it remains `aria-hidden`.

### Invariants And Boundaries

- Pulse is frozen by the unlayered `html[data-effects="off"]` rule (`index.css`) AND steady under
  reduced motion — both gates verified in review.
- The Panda animation literal and `PULSE_ANIMATION` must stay byte-identical; change the ruling in
  `stateGrammar.ts` first, then here, and the pinning test must be updated deliberately.
- No consumer may style its own dot; new surfaces import this component.
- Consumers must choose the accessibility mode by context: name a truncation-surviving dot, hide
  a redundant dot beside visible text.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The cva variants + dual accessibility-mode renderer. | `dot`; `StateDot` | dashboard/src/panels/session-cockpit/StateDot.tsx:8-36; dashboard/src/panels/session-cockpit/StateDot.tsx:38-61 |
| The grammar whose visuals this renders (single source). | `PULSE_ANIMATION`; `SeatVisualState`; `seatVisualState` | dashboard/src/data/stateGrammar.ts:14-14; dashboard/src/data/stateGrammar.ts:33-42; dashboard/src/data/stateGrammar.ts:101-125 |
| The `pulseSlow` keyframe + the sovereign effects-off freeze. | `pulseSlow` | dashboard/src/index.css:94-101 |
| The cross-surface consistency test (rail dot ≡ HeaderStrip dot). | "the rail dot and the HeaderStrip dot render the SAME grammar state for the same seat" | dashboard/src/panels/session-cockpit/SessionRail.test.tsx:470-480 |

## Update History

- 2026-08-04T13:42:02+02:00 — 260731-EFA-L6 S18-B08 curator: regenerated the grammar/keyframe/test extents and retained the full keyframe/effects-off owner range from the worker ledger.

- 2026-07-17T08:33+02:00 — 260715-FEUI-L4 R8 added optional accessible naming: rail dots are
  named images carrying the grammar word, while dots next to visible words stay hidden.
  Verification metadata is pinned to the contract base until code commit.
- 2026-07-17T02:30+02:00 — Created for 260715-FEUI-L2 (R14): the single grammar renderer —
  color/pulse cva with the Panda-literal 2.4 s ease-in-out pulse pinned to
  `stateGrammar.PULSE_ANIMATION`, reduced-motion steadiness, and the data-state attributes the
  cross-surface test compares. Verification metadata pinned to the leaf base until closeout
  stamps the L2 code commit.
