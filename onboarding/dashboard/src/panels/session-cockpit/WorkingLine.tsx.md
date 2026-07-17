# dashboard/src/panels/session-cockpit/WorkingLine.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/session-cockpit/WorkingLine.tsx` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-17T04:20+02:00                           |
| lastVerifiedCommitHash | `7b62338310aff67ae8b66a450a52a1f1052137c4`       |
| lastVerifiedCommitDate | 2026-07-17T04:36:24+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

The **WorkingLine** (260715-FEUI-L6 R6, spec §1.2-2, design §9.7): the SINGLE home of turn
theater. Renders ONLY while the focused seat's grammar state is `working`
(`seatVisualState().key`), mounted by SessionsView into SessionStage's reserved slot directly
under the HeaderStrip. Anatomy, fixed: `◐ <activity form | "working"> · ~elapsed · ⏹ stop`. Turn
theater NEVER renders per rail row.

## Code Commentary

### Logic

- **Render gate** (L86, L93): `seatVisualState(session).key === "working"` — the SAME predicate
  the `turn.stop` palette command gates on (review finding 3 aligned them), so the grammar
  yields to awaiting-input/failed and the line disappears with them.
- **Activity form seam** (L66-L74): `workingActivityForm` returns the REAL form when one is
  known — no wire field carries one today (turn-state is a bit, not a verb phrase), so it
  returns undefined and the line says plain "working". NEVER whimsy verbs (spec §1.1-10); the
  seam stays typed for UA-1 reasoning headers / UA-5 states.
- **~elapsed** (L57-L64, L107-L115): `formatApproxElapsed` from L2's client `turnClock`
  (`workingSince` — the OBSERVED transition, poll/10 s-sweep bounded), `~`-labeled at every
  magnitude, `tabular-nums`, tooltip states the sweep bound; OMITTED entirely when unobserved
  (`workingSince === null`). A 1 s self-tick drives production; the `now` prop is the test seam
  (L83-L92).
- **Welded stop (UA-7)** (L116-L126): the ⏹ stop button sits at the line's fixed end position,
  `disabled` with `STOP_TURN_DISABLED_REASON` in title/aria-label/`data-disabled-reason` — the
  control names the gap until the interrupt route exists; retry/compaction states join this line
  when UA-5 exposes them.
- **Spinner** (L31-L37, L101-L103): the slow-pulse `◐` glyph ONLY — the Panda literal
  `pulseSlow 2.4s ease-in-out infinite` (the animation ruling; the test pins it to
  `stateGrammar.PULSE_ANIMATION`), `_motionReduce: none`, frozen by the unlayered
  `html[data-effects="off"]` rule in index.css. No shimmer, no braille frames, aria-hidden.

### Invariants And Boundaries

- This line is the ONLY turn-theater surface; the rail renders none of it (the rail's L6 gains
  are bell markers + tooltip hints only).
- The activity form must stay real-or-plain — a decorative gerund is a ruled violation.
- The pulse literal must track the grammar's ruled string; drift surfaces via the test's
  constant pin.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Gate, anatomy, elapsed, welded stop, spinner. | L57-L129 | [WorkingLine.tsx](WorkingLine.tsx) |
| The grammar predicate + the ruled pulse literal. | L14, L44-L106 | [../../data/stateGrammar.ts](../../data/stateGrammar.ts) |
| The client turnClock supplying `workingSince`. | L56-L81 | [../../data/sessionCockpitStore.ts](../../data/sessionCockpitStore.ts) |
| The UA-7 reason copy. | L52 | [lifecycleCopy.ts](lifecycleCopy.ts) |
| The reserved slot this line is the only tenant of. | L84-L87 | [SessionStage.tsx](SessionStage.tsx) |
| The view passing `workingLine` + the same-predicate `turn.stop` palette command. | L322-L336, L622-L626 | [SessionsView.tsx](SessionsView.tsx) |
| The jsdom suite (6 cases) + 2 view-level cases. | L33-L95 | [WorkingLine.test.tsx](WorkingLine.test.tsx) |

## Update History

- 2026-07-17T04:20+02:00 — Created for 260715-FEUI-L6 R6: the single-home turn theater in L2's
  reserved stage slot — grammar-gated render (the same predicate as the `turn.stop` palette
  command after review finding 3), real-or-plain activity form (typed seam, never whimsy),
  ~-labeled sweep-bounded tabular elapsed omitted when unobserved, the welded UA-7-gated
  disabled stop naming the gap, and the ruled slow-pulse ◐ glyph frozen under
  `data-effects="off"`. Verification metadata pinned to the leaf base until closeout stamps the
  L6 code commit.
