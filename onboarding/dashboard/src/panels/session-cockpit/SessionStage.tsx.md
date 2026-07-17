# dashboard/src/panels/session-cockpit/SessionStage.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/session-cockpit/SessionStage.tsx` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-17T02:30+02:00                           |
| lastVerifiedCommitHash | `e2b99dcd71fb6ca31f642dd61c3c16f3d3d05bf5`       |
| lastVerifiedCommitDate | 2026-07-17T02:52:07+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

The **SessionStage container** (260715-FEUI-L2 S5, spec §1.2): the stage's FIXED layer order —
HeaderStrip (always) → the reserved WorkingLine slot (rendered by L6) → the surface (the PTY, L6)
→ the composer (L5). This leaf ships the container + HeaderStrip; the PTY/composer placeholders
stay OWNED BY SessionsView (passed as `children`) so L1's keyboard-zone markers survive and the
zone contract stays testable.

## Code Commentary

### Logic

- **Header row** (L62-L75): `data-stage-header tabIndex={-1}` (the F6/composer-Esc focus landing
  from L1) hosting the `HeaderStrip` for the focused seat — or, with NO focused session, the
  EXPLAINED empty identity ("no focused session — pick one on the rail, or launch from Chats";
  R9 — never an unexplained empty stage). `headerExtra` renders view-owned chips after the strip
  (the ~80-col floor hint stays owned by SessionsView).
- **Handoff note (F17)** (L76-L80): the one-line `role="status"` amber note when the previously
  focused seat retired/landed (text built by SessionsView's handoff effect).
- **WorkingLine slot** (L81-L83): `data-slot="working-line"` directly under the header —
  zero-height until L6 renders the turn theater (verb, ~elapsed, ⏹ stop) into it.
- **Children** (L84): the PTY/composer placeholders from SessionsView.

### Invariants And Boundaries

- The layer order is RULED (§1.2): header → working-line slot → surface → composer; L6/L5 fill
  slots, never reorder.
- The container never invents identity: no focused seat ⇒ the explained hint, not a blank.
- `data-stage-header` must stay on the header element — the keymap focus contract targets it.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The layer order, empty identity, handoff note, and reserved slot. | L46-L87 | [SessionStage.tsx](SessionStage.tsx) |
| The header line rendered for the focused seat. | L79-L145 | [HeaderStrip.tsx](HeaderStrip.tsx) |
| The owner passing focused/cockpit/handoff/children + the floor chip. | L546-L590 | [SessionsView.tsx](SessionsView.tsx) |
| The focus selectors that target `data-stage-header`. | — | [../../data/keymap/focus.ts](../../data/keymap/focus.ts) |
| The suite covering slot position, handoff, and the explained empty state. | L83-L107 | [HeaderStrip.test.tsx](HeaderStrip.test.tsx) |

## Update History

- 2026-07-17T02:30+02:00 — Created for 260715-FEUI-L2 S5 (R9/R10/F17): the stage container with
  the ruled layer order, the always-on header hosting HeaderStrip or the explained no-focus
  identity, the F17 handoff note, and the reserved zero-height WorkingLine slot for L6.
  Verification metadata pinned to the leaf base until closeout stamps the L2 code commit.
