# dashboard/src/data/stateGrammar.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/stateGrammar.ts`             |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-17T02:30+02:00                           |
| lastVerifiedCommitHash | `e2b99dcd71fb6ca31f642dd61c3c16f3d3d05bf5`       |
| lastVerifiedCommitDate | 2026-07-17T02:52:07+02:00|
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

**THE one seat-state grammar** (260715-FEUI-L2 R14, spec §2.4 — RULED 2026-07-16): rail rows, the
HeaderStrip, the SeatInspector, and (L7) the StatusLine all read this single
`controlState × turnState × status → visual` mapping, so the same seat can never show two
different states on two surfaces. The dot is the truncation-surviving signal and must never lie:
**blocked-on-human is STEADY** (never flickers), only `working` and `failed` pulse — and a pulse
is the SLOW 2.4 s ease-in-out opacity pulse, NEVER `steps()`/on-off blinking (the developer
animation ruling; the legacy 0.6 s `steps(1)` blink in `grammar/Dot.tsx` is the app-wide offender
tracked outside this leaf).

## Code Commentary

### Logic

- **Pulse ruling as exported constants** (L12-L14): `PULSE_DURATION_S = 2.4`,
  `PULSE_TIMING = "ease-in-out"`, `PULSE_ANIMATION = "pulseSlow 2.4s ease-in-out infinite"` — so
  tests pin the ruling, not a magic string; the keyframe lives in `index.css`, the literal is
  repeated in `StateDot.tsx` for Panda static extraction (a test pins the two together).
- **`VISUALS` table** (L44-L71): key → `{word, chip?, color, pulse}`. working = cyan PULSE ·
  awaiting-input = STEADY amber `input?` · waiting = STEADY muted-amber (reserved) · failed =
  alarm PULSE · starting = cyan steady · ready = mint, NO chip · turn-ended = mint ·
  stale/landed/retired/exited = muted/dormant steady · unclassified = `—`, no chip. `chip` is the
  rail status-chip label — the status vocabulary ONLY, never the model (R6); absent ⇒ no chip.
- **`seatVisualState(input)`** (L88-L106) — precedence: terminal statuses first
  (landed/terminated→retired/exited never look alive) → `controlState==="failed"` → blocked-on-human
  (`controlPendingInteraction` OR `turnState==="awaiting-input"`) → the declared `waitingReason`
  (word `waiting(<reason>)`, chip `waiting: <reason>`) → live turn-state (working/turn-ended/stale)
  → control lifecycle (starting/ready) → `unclassified`. Server truth mirrored — an unclassified
  row renders as unclassified, never a fabricated state.
- **`waiting(reason)`** (L19, L96-L99) — the AEO reserved word, implemented RENDERED-READY with an
  explicit `waitingReason` input that NO wire field populates yet (UA-gated) — exactly the
  reserved-word posture the leaf demands.

### Invariants And Boundaries

- ONE module, ONE renderer (`panels/session-cockpit/StateDot.tsx`); no surface may derive its own
  state words/colors (the cross-surface consistency test in `SessionRail.test.tsx` locks it).
- **Chip vocabulary width — OPEN DEVELOPER RULING** (review finding 1, sev-3): the ruled §1.6b
  chip list is a closed six-word set, but `stale`/`exited`/`retired`/`starting` are real catalog
  truths and render as their own words (mirrored, not remapped — remapping would fabricate). If
  the developer wants the literal closed list, the mapping is one switch HERE.
- `stale` mirrors the sweep's own uncertainty word — hiding it would fake freshness (R15).
- Colors are podracer token roles only (`SeatStateColor`); the muted-amber is a `color-mix` in the
  renderer, not a new token.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The pulse constants, visuals table, and precedence mapping. | L12-L106 | [stateGrammar.ts](stateGrammar.ts) |
| The ONLY renderer of these visuals (Panda literal pinned to `PULSE_ANIMATION`). | L8-L49 | [../panels/session-cockpit/StateDot.tsx](../panels/session-cockpit/StateDot.tsx) |
| The `pulseSlow` keyframe + the effects-off freeze that governs it. | L91-L98 | [../index.css](../index.css) |
| The server classifier whose words this mirrors (turn state, sweep cadence). | — | [serving/turn_state.py](../../../mcp/src/agents_remember/serving/turn_state.py) |
| The unit suite: per-state mapping, precedence, waiting(reason), the no-steps pulse ruling. | L14-L103 | [stateGrammar.test.ts](stateGrammar.test.ts) |

## Update History

- 2026-07-17T02:30+02:00 — Created for 260715-FEUI-L2 (R14, dot grammar): the single seat-state
  grammar — exported pulse-ruling constants (2.4 s ease-in-out, never steps()), the closed visuals
  table with steady blocked-on-human doctrine, terminal-first precedence, the rendered-ready
  `waiting(reason)` reserved word, and the honest `stale`/`exited`/`retired`/`starting` mirror
  chips (sev-3 vocabulary-width ruling pending with the developer). Verification metadata pinned
  to the leaf base until closeout stamps the L2 code commit.
