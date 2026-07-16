# dashboard/src/data/keymap/reserved.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/keymap/reserved.ts`          |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-17T00:20+02:00                           |
| lastVerifiedCommitHash | `ee955085a2010f62e9ad4d2bdc6aa77975daa5f3`       |
| lastVerifiedCommitDate | 2026-07-17T00:42:07+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[data/keymap overview](overview.md)

## Purpose

The **PTY reserved set** (260715-FEUI-L1 S4, design §5.2): the ONLY chords the PTY zone ever
intercepts — every other key, including Esc and Esc Esc, passes through to the hosted harness
(Claude Code owns Esc Esc for rewind; Codex owns plain Esc for interrupt). The set is DATA so the
`?` reference overlay, the tinykeys binding, the future L6 xterm `attachCustomKeyEventHandler`,
and the collision-verification record all read one source and can never drift apart. This file is
also the durable home of the R6 collision-audit evidence: every chord carries a five-source
`verifiedAgainst` record (codex / pi / claude / chrome / firefox) with the observed evidence
string.

## Code Commentary

### Logic

- `PTY_RESERVED` (L62-L150): four BOUND chords — `ctrl+;` → `palette.open`, `F6` →
  `focus.exitToChrome`, `ctrl+alt+pageup` → `session.prev`, `ctrl+alt+pagedown` → `session.next`
  — plus two reserved-but-UNBOUND clipboard slots (`ctrl+c (with selection)` →
  `clipboard.copySelection`, `ctrl+shift+c` → `clipboard.copy`) that ride along as data for the
  L6 clipboard package (pane-freeze/clipboard companion spec); `matchReservedChord` never fires
  for them.
- Each bound chord carries both the human `chord` label (the `?` overlay), the `tinykeys` binding
  string, and a structural `match` (`ChordMatch`: accepted `key` values case-insensitively OR
  `code` values for layout robustness — `ctrl+;` matches `code: Semicolon` even on layouts where
  the key face differs, e.g. German `ö`).
- `matchReservedChord(ev)` (L193-L199) is the PTY zone's single gate: returns the matching BOUND
  reserved chord or `null`; null means the event belongs to the hosted harness (passthrough), no
  exceptions. Modifier flags must match exactly; key OR code may match.
- `BROWSER_FORBIDDEN` (L153-L177): the chords no zone may EVER bind because browsers reserve them
  non-preventably (ctrl+w/t/n, ctrl+tab, ctrl+1..9, alt+f4, f11, …) — asserted against
  `PTY_RESERVED` by `zones.test.ts`.

### The R6 chord replacement (the header comment, L13-L18)

The leaf's provisional session-switch pair `Ctrl+Alt+[` / `Ctrl+Alt+]` was REPLACED by
`Ctrl+Alt+PageUp` / `Ctrl+Alt+PageDown` — a collision replaces the CHORD, not the rule:

1. Pi binds `ctrl+alt+]` as `tui.editor.jumpBackward` (packages/tui/src/keybindings.ts).
2. `Ctrl+Alt+[` is independently hazardous: its legacy terminal encoding is ESC ESC (`\x1b\x1b`)
   — exactly Claude Code's rewind — so ANY interception miss would fire a destructive harness
   action.

The replacement pair encodes as distinct CSI sequences (`CSI 5;7~` / `6;7~`) that no audited
harness binds, so even a leaked event is inert. The `ctrl+shift+c` slot records the one remaining
collision: Firefox DevTools inspect-element steals it non-preventably (Chrome honors
preventDefault) — flagged to the L6 clipboard leaf (prefer selection-aware Ctrl+C +
copy-on-select).

### Conventions

Audit sources are named in the header comment: Codex `codex-rs/tui/src/keymap.rs`
`built_in_defaults()`, Pi `packages/tui/src/keybindings.ts` (+ coding-agent), Claude Code 2.1.210
installed-bundle strings, and the browser non-preventable lists. Evidence strings quote what was
observed, not a verdict alone.

### Invariants And Boundaries

- This file is the **single source** of interceptable chords: the `?` page renders it, the
  tinykeys layer binds it, and L6's xterm handler must consume `matchReservedChord` — never a
  copied list.
- No entry may claim a bare-Esc sequence, and no entry may appear in `BROWSER_FORBIDDEN`
  (both pinned by `zones.test.ts`).
- Every BOUND chord must be verified fully clear across all five sources; a discovered collision
  on a bound chord means replacing the chord (the R6 rule), never shipping it.
- `KeyEventLike` stays a structural type so tests need no real DOM events.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The reserved set, verification records, replacement notes, and the single PTY gate. | L62-L199 | [reserved.ts](reserved.ts) |
| `routeKey("pty", …)` defers entirely to `matchReservedChord`. | L54-L58 | [zones.ts](zones.ts) |
| The tinykeys binding installs only bound entries and re-checks `routeKey` before intercepting. | L54-L64 | [../../panels/session-cockpit/useKeyboardZones.ts](../../panels/session-cockpit/useKeyboardZones.ts) |
| The `?` reference page renders this set verbatim (bound + reserved-unbound rows). | L195-L205 | [../../panels/session-cockpit/CommandPalette.tsx](../../panels/session-cockpit/CommandPalette.tsx) |
| The hygiene suite: five-source records, bound-must-be-clear, no bare Esc, no browser-forbidden chord. | L84-L111 | [zones.test.ts](zones.test.ts) |

## Update History

- 2026-07-17T00:20+02:00 — Created for 260715-FEUI-L1 S4 (R5/R6): the PTY reserved set with
  per-chord five-source verification records, `matchReservedChord`, `BROWSER_FORBIDDEN`, the two
  unbound clipboard slots (Firefox ctrl+shift+c collision recorded, flagged to L6), and the R6
  chord replacement Ctrl+Alt+[ / ] → Ctrl+Alt+PageUp / PageDown (Pi collision + the ESC ESC
  encoding hazard). Verification metadata pinned to the task base until closeout stamps the L1
  code commit.
