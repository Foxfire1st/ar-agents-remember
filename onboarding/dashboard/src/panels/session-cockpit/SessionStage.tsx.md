# dashboard/src/panels/session-cockpit/SessionStage.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/session-cockpit/SessionStage.tsx` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-17T08:33+02:00                           |
| lastVerifiedCommitHash | `4293c53b9d6ef2bf0fee7aca11c2677322c4e786`       |
| lastVerifiedCommitDate | 2026-07-17T10:26:02+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

The **SessionStage container** (260715-FEUI-L2 S5, spec §1.2): the stage's FIXED layer order —
HeaderStrip (always) → the WorkingLine slot (FILLED by L6 via the `workingLine` prop) → the
surface (the PTY — L6's PtySurface) → the composer (L5). L2 shipped the container + HeaderStrip;
the surface/composer stay OWNED BY SessionsView (passed as `children`) so L1's keyboard-zone
markers survive and the zone contract stays testable. FEUI-L4 adds only a controlled-popover
bridge from the view into the header's sole model/effort control.

## Code Commentary

### Logic

- **Header row** (L62-L76): `data-stage-header tabIndex={-1}` (the F6/composer-Esc focus landing
  from L1) hosting the `HeaderStrip` for the focused seat — or, with NO focused session, the
  EXPLAINED empty identity ("no focused session — pick one on the rail, or run “Launch session…”
  from the palette (ctrl+k)"; R9 — never an unexplained empty stage; copy updated by L3, which
  shipped the launcher the old "launch from Chats (cockpit launcher: L5)" hint deferred to).
  `headerExtra` renders view-owned chips after the strip (the ~80-col floor hint stays owned by
  SessionsView). The optional `controlPopover` prop is forwarded unchanged to HeaderStrip so
  palette commands open the same mounted control as the header trigger.
- **Handoff note (F17)** (L76-L80): the one-line `role="status"` amber note when the previously
  focused seat retired/landed (text built by SessionsView's handoff effect).
- **WorkingLine slot** (L84-L87): `data-slot="working-line"` directly under the header — L6's
  ONE additive optional `workingLine` prop renders the turn theater (verb, ~elapsed, ⏹ stop)
  inside it; the slot is the prop's ONLY tenant and stays zero-height when no line renders.
- **Children** (L88): the PTY surface/composer from SessionsView.

### Invariants And Boundaries

- The layer order is RULED (§1.2): header → working-line slot → surface → composer; L6/L5 fill
  slots, never reorder.
- The container never invents identity: no focused seat ⇒ the explained hint, not a blank.
- `data-stage-header` must stay on the header element — the keymap focus contract targets it.
- `controlPopover` is state plumbing only; this container never mounts a second control or owns
  snapshot/set behavior.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The layer order, control-popover bridge, empty identity, handoff note, and filled slot. | L46-L95 | [SessionStage.tsx](SessionStage.tsx) |
| The header line rendered for the focused seat. | L79-L145 | [HeaderStrip.tsx](HeaderStrip.tsx) |
| The owner passing focused/cockpit/handoff/workingLine/children + the floor chip. | L606-L657 | [SessionsView.tsx](SessionsView.tsx) |
| The slot's only tenant — L6's turn theater. | L76-L129 | [WorkingLine.tsx](WorkingLine.tsx) |
| The focus selectors that target `data-stage-header`. | — | [../../data/keymap/focus.ts](../../data/keymap/focus.ts) |
| The suite covering slot position, handoff, and the explained empty state. | L83-L107 | [HeaderStrip.test.tsx](HeaderStrip.test.tsx) |

## Update History

- 2026-07-17T08:33+02:00 — 260715-FEUI-L4 R2 added the optional controlled-popover bridge and
  forwarded it to HeaderStrip; stage order and ownership remain unchanged. Verification metadata
  is pinned to the contract base until code commit.
- 2026-07-17T06:10+02:00 — 260715-FEUI-L3: one string literal — the empty-stage identity now
  points at the palette's "Launch session…" command (the old "launch from Chats (cockpit
  launcher: L5)" copy became false the moment L3 shipped the launcher). Structure untouched.
  Verification metadata pinned to the leaf base until closeout stamps the L3 code commit.
- 2026-07-17T04:20+02:00 — 260715-FEUI-L6: the reserved WorkingLine slot is FILLED — the ONE
  additive optional `workingLine` prop (the slot's only tenant) renders L6's turn theater inside
  `data-slot="working-line"`; layer order, empty identity, and handoff note unchanged.
- 2026-07-17T02:30+02:00 — Created for 260715-FEUI-L2 S5 (R9/R10/F17): the stage container with
  the ruled layer order, the always-on header hosting HeaderStrip or the explained no-focus
  identity, the F17 handoff note, and the reserved zero-height WorkingLine slot for L6.
  Verification metadata pinned to the leaf base until closeout stamps the L2 code commit.
