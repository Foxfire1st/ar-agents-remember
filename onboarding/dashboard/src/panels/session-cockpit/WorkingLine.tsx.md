# dashboard/src/panels/session-cockpit/WorkingLine.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/session-cockpit/WorkingLine.tsx` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-20T22:30+02:00                           |
| lastVerifiedCommitHash | `9e6c15d2b2bb663fcd10e26d77d0e4d2795829bd`       |
| lastVerifiedCommitDate | 2026-07-20T22:32:02+02:00|
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

## 260718-CHATS-L4 Reviewed Candidate Delta

An optional `interrupt` prop (the `ConversationInterrupt` from `useConversationControls`) is added,
backward-compatible: absent (the pre-L4 tests, RailChat) → the existing disabled placeholder with
`STOP_TURN_DISABLED_REASON`; present → an actionable stop gated on real turn + capability evidence.
The enabled control carries `aria-keyshortcuts` DERIVED from the effective keymap (review F25), rests at
demoted destructive weight (muted border, amber only on hover/focus — A6), and its tooltip is an honest
action tooltip (`Stop the current turn · <effective chord>`) — the known-stale L1 capability reason is
never surfaced (F24). The not-working / catalog-lag placeholder falls back to the honest pre-L4 constant
rather than the stale L1 text. The welded ⏹ position and the working-only render gate are unchanged.

The reviewed candidate is uncommitted; existing verification hash/date remain pinned; closeout owns
commit stamping.

## Update History

- 2026-07-20T22:30+02:00 — 260718-CHATS-L4 curator: recorded the optional `interrupt` prop — absent
  keeps the pre-L4 disabled placeholder (existing tests unchanged); present renders an evidence-gated
  actionable stop with keymap-derived `aria-keyshortcuts` (F25), demoted weight (A6), and an honest
  action tooltip that never leaks the stale L1 reason (F24). Verification metadata remains pinned to the
  leaf base until closeout stamps the L4 commit.
- 2026-07-17T04:20+02:00 — Created for 260715-FEUI-L6 R6: the single-home turn theater in L2's
  reserved stage slot — grammar-gated render (the same predicate as the `turn.stop` palette
  command after review finding 3), real-or-plain activity form (typed seam, never whimsy),
  ~-labeled sweep-bounded tabular elapsed omitted when unobserved, the welded UA-7-gated
  disabled stop naming the gap, and the ruled slow-pulse ◐ glyph frozen under
  `data-effects="off"`. Verification metadata pinned to the leaf base until closeout stamps the
  L6 code commit.
