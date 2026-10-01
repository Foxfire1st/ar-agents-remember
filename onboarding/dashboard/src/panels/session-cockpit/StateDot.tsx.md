# dashboard/src/panels/session-cockpit/StateDot.tsx

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

## Evidence

### Repo-Internal References

- The cva variants + dual accessibility-mode renderer. [1]
- The grammar whose visuals this renders (single source). [2]
- The `pulseSlow` keyframe + the sovereign effects-off freeze. [3]
- The cross-surface consistency test (rail dot ≡ HeaderStrip dot). [4]
