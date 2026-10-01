# dashboard/src/data/stateGrammar.ts

## Governing Overview

[data overview](overview.md)

## Purpose

**THE one seat-state grammar** (spec §2.4 — ruled 2026-07-16): rail rows, the
HeaderStrip, the SeatInspector, and the StatusLine all read this single
`controlState × turnState × status → visual` mapping, so the same seat can never show two
different states on two surfaces. The dot is the truncation-surviving signal and must never lie:
**blocked-on-human is STEADY** (never flickers), only `working` and `failed` pulse — and a pulse
is the SLOW 2.4 s ease-in-out opacity pulse, NEVER `steps()`/on-off blinking (the
animation ruling; the legacy 0.6 s `steps(1)` blink in `grammar/Dot.tsx` is the app-wide offender
tracked separately).

## Code Commentary

### Logic

- **Pulse ruling as exported constants** cit:([`PULSE_DURATION_S`, `PULSE_TIMING`, `PULSE_ANIMATION`], dashboard/src/data/stateGrammar.ts:12-14): `PULSE_DURATION_S = 2.4`,
  `PULSE_TIMING = "ease-in-out"`, `PULSE_ANIMATION = "pulseSlow 2.4s ease-in-out infinite"` — so
  tests pin the ruling, not a magic string; the keyframe lives in `index.css`, the literal is
  repeated in `StateDot.tsx` for Panda static extraction (a test pins the two together).
- **`VISUALS` table** cit:([`VISUALS`], dashboard/src/data/stateGrammar.ts:44-71): key → `{word, chip?, color, pulse}`. working = cyan PULSE ·
  awaiting-input = STEADY amber `input?` · waiting = STEADY muted-amber (reserved) · failed =
  alarm PULSE · starting = cyan steady · ready = mint, NO chip · turn-ended = mint ·
  stale/landed/retired/exited = muted/dormant steady · unclassified = `—`, no chip. `chip` is the
  rail status-chip label — the status vocabulary ONLY, never the model (R6); absent ⇒ no chip.
- **`seatVisualState(input)`** cit:([`seatVisualState`], dashboard/src/data/stateGrammar.ts:101-125) — precedence: terminal statuses first
  (landed/terminated→retired/exited never look alive) → `controlState==="failed"` → blocked-on-human
  (`sessionHasPendingInteraction(input)` OR `turnState==="awaiting-input"`) → the declared
  `waitingReason` (word `waiting(<reason>)`, chip `waiting: <reason>`) → **`liveTurnWorking`** → live turn-state (working/turn-ended/stale) → control lifecycle
  (starting/ready) → `unclassified`. Server truth mirrored — an unclassified row renders as
  unclassified, never a fabricated state.
- **Plural pending counts as blocked (review N1)**: `SeatStateInput` picks up
  cit:([`controlPendingInteractions`], dashboard/src/data/stateGrammar.ts:73-93), and the blocked-on-human guard cit:([`sessionHasPendingInteraction`], dashboard/src/data/sessions.ts:574-581) calls
  `sessions.ts`'s `sessionHasPendingInteraction` — the singular parent slot OR a non-empty
  multiplexed sub-agent list — instead of reading only the singular slot. A seat blocked SOLELY on
  a sub-agent approval is STEADY amber awaiting-input, never dark; the guard still slots below the
  terminal/failed guards and above the declared wait, so the precedence doctrine is unchanged.
- **`liveTurnWorking` — the fresher-liveness input** (audit V5): a new optional
  `SeatStateInput` field carrying the conversation projection's OWN live turn signal (its SSE knows
  a streaming turn sub-second; the sweep-bounded catalog `turnState` lags ~10 s and reads a settled
  `turn-ended`). When true, `seatVisualState` returns `working` — but the guard is slotted **below**
  the terminal/fault/blocked-on-human/wait guards, so it can NEVER fake liveness over a real end
  state, a fault, a human block, or a declared wait. Undefined/false is the honest fallback to the
  catalog truth (old behavior); no wire field populates it directly — `SessionsView` computes it for
  the focused seat only (see repo-internal refs).
- **`waiting(reason)`** (L82-L83, L111-L114) — the AEO reserved word, implemented RENDERED-READY
  with an explicit `waitingReason` input that NO wire field populates yet (UA-gated) — exactly the
  reserved-word posture the leaf demands.

### Invariants And Boundaries

- ONE module, ONE renderer (`panels/session-cockpit/StateDot.tsx`); no surface may derive its own
  state words/colors (the cross-surface consistency test in `SessionRail.test.tsx` locks it).
- **Chip vocabulary width — OPEN DECISION** (review finding 1, sev-3): the ruled §1.6b
  chip list is a closed six-word set, but `stale`/`exited`/`retired`/`starting` are real catalog
  truths and render as their own words (mirrored, not remapped — remapping would fabricate). If
  the literal closed list is wanted, the mapping is one switch HERE.
- `stale` mirrors the sweep's own uncertainty word — hiding it would fake freshness (R15).
- Colors are podracer token roles only (`SeatStateColor`); the muted-amber is a `color-mix` in the
  renderer, not a new token.

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

- The pulse constants, visuals table, and precedence mapping. [1]
- The ONLY renderer of these visuals (Panda literal pinned to `PULSE_ANIMATION`). [2]
- The `pulseSlow` keyframe + the effects-off freeze that governs it. [3]
- The server classifier whose words this mirrors (turn state, sweep cadence). [4]
- The ANY-pending derivation (N1) the blocked-on-human guard now calls — singular slot OR non-empty multiplexed plural. [5]
- The SOLE producer of `liveTurnWorking` (R9): computed for the focused seat from the conversation projection status and merged into `focused`. [6]
- The unit suite: per-state mapping, precedence, waiting(reason), the no-steps pulse ruling, the R9 override winning only below terminal/fault/blocked, and the N1 agent-only-blocked pin. [7]

### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.
