# dashboard/src/panels/session-cockpit/StateDot.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/session-cockpit/StateDot.tsx` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-17T08:33+02:00                           |
| lastVerifiedCommitHash | `4293c53b9d6ef2bf0fee7aca11c2677322c4e786`       |
| lastVerifiedCommitDate | 2026-07-17T10:26:02+02:00|
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

- The `dot` cva (L8-L36): 0.6em circle, color variants over the grammar's podracer roles (the
  mutedAmber via `color-mix` on the amber token — no new token); the `pulse: true` variant carries
  the LITERAL `animation: "pulseSlow 2.4s ease-in-out infinite"` — a literal for Panda's static
  extraction; `stateGrammar.PULSE_ANIMATION` is the same string and the cross-surface consistency
  test pins the two together — plus `_motionReduce: { animation: "none" }` (steady under
  prefers-reduced-motion, never hidden).
- `StateDot({state, testId, ariaLabel?})` (L38-L61): renders the comparison attributes and has
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

| Finding | Citations | Source Path |
| --- | --- | --- |
| The cva variants + dual accessibility-mode renderer. | L8-L61 | [StateDot.tsx](StateDot.tsx) |
| The grammar whose visuals this renders (single source). | L44-L106 | [../../data/stateGrammar.ts](../../data/stateGrammar.ts) |
| The `pulseSlow` keyframe + the sovereign effects-off freeze. | L91-L98 | [../../index.css](../../index.css) |
| The cross-surface consistency test (rail dot ≡ HeaderStrip dot). | L325-L338 | [SessionRail.test.tsx](SessionRail.test.tsx) |

## Update History

- 2026-07-17T08:33+02:00 — 260715-FEUI-L4 R8 added optional accessible naming: rail dots are
  named images carrying the grammar word, while dots next to visible words stay hidden.
  Verification metadata is pinned to the contract base until code commit.
- 2026-07-17T02:30+02:00 — Created for 260715-FEUI-L2 (R14): the single grammar renderer —
  color/pulse cva with the Panda-literal 2.4 s ease-in-out pulse pinned to
  `stateGrammar.PULSE_ANIMATION`, reduced-motion steadiness, and the data-state attributes the
  cross-surface test compares. Verification metadata pinned to the leaf base until closeout
  stamps the L2 code commit.
