# dashboard/src/data/keymap/zones.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/keymap/zones.ts`             |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-17T00:20+02:00                           |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060`       |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[data/keymap overview](overview.md)

## Purpose

The **keyboard-zone routing contract** (260715-FEUI-L1 S4, design §5.2) — pure logic, xterm-free,
so vitest covers it without a terminal. Three zones: **chrome** (the shell around the panes;
chords may be handled but printable-key bindings never fire in editable targets — R7),
**composer** (the editor owns its keys; only composer-declared chords are handled), **pty** (EVERY
key passes to the hosted harness except exactly the bound reserved set; no bare-Esc is ever
claimed over a live PTY). Zone membership is carried by `data-kbzone` markers on containers so the
React binding and the tests resolve zones the same way.

## Code Commentary

### Logic

- cit:([`zoneForTarget`], dashboard/src/data/keymap/zones.ts:28-32): nearest `[data-kbzone]` container via `closest`; `pty` and
  `composer` are recognized, everything else (unknown values, no container, null target) defaults
  to `chrome`.
- cit:([`isEditableTarget`], dashboard/src/data/keymap/zones.ts:35-42): contenteditable, TEXTAREA, SELECT, and non-readOnly INPUT consume
  plain typing.
- cit:([`isPrintable`], dashboard/src/data/keymap/zones.ts:45-47): single-character key with no ctrl/alt/meta; shift allowed (`?` etc.).
- cit:([`routeKey`], dashboard/src/data/keymap/zones.ts:54-58) — the contract: `pty` handles ONLY a
  `matchReservedChord` hit (everything else passes through); chrome/composer pass printable keys
  through when the target is editable (the GENERIC R7 suppression — there is deliberately no
  per-chord printable flag; review round 2 removed one from `chords.ts`), and handle everything
  else.
- cit:([`slashOpensPalette`], dashboard/src/data/keymap/zones.ts:64-67): the composer `/`-rule — true only at
  caret position 0 or right after a newline. Pure over the editor's value + caret so CM6 (L5) and
  the placeholder textarea share it.

### Invariants And Boundaries

- The PTY branch defers entirely to `reserved.ts` — this file must never grow its own PTY chord
  knowledge.
- `ZoneElementLike`/`KeyEventLike` stay structural so tests use plain objects, not DOM events.
- Suppression is generic by design: any printable chord added to the tables automatically obeys
  R7; do not reintroduce per-chord flags that could drift from this rule.
- No React, no window access — the DOM wiring lives in
  `panels/session-cockpit/useKeyboardZones.ts`.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Zone resolution, editable/printable classification, the routing contract, and the `/` rule. | `zoneForTarget` | dashboard/src/data/keymap/zones.ts:28-32 |
| The reserved-set gate the pty branch defers to. | `PTY_RESERVED` | dashboard/src/data/keymap/reserved.ts:62-150 |
| The React binding that calls `zoneForTarget`/`routeKey`/`slashOpensPalette` per event. | `useKeyboardZones` | dashboard/src/panels/session-cockpit/useKeyboardZones.ts:18-97 |
| The contract suite: PTY passthrough (incl. bare Esc + harness-owned chords), printable suppression, the `/` rule. | "passes bare Esc — and any Esc chord — to the hosted harness (Claude owns Esc Esc)"; "printable keys never fire as bindings in editable targets"; "opens the palette only at the start of a line" | dashboard/src/data/keymap/zones.test.ts:46-49; dashboard/src/data/keymap/zones.test.ts:117-120; dashboard/src/data/keymap/zones.test.ts:154-159 |

## Update History
- 2026-08-02T20:42:26+02:00 — W2-B07 curator: repaired 4 repository-reference citations (4/4 anchored and sourced; scoped citation check clean).

- 2026-07-17T00:20+02:00 — Created for 260715-FEUI-L1 S4 (R5/R7): zone resolution over
  `data-kbzone` markers, the `routeKey` contract (PTY = reserved-set-only interception with
  everything else passing through; generic printable suppression in editable targets), and the
  pure `slashOpensPalette` composer rule. Verification metadata pinned to the task base until
  closeout stamps the L1 code commit.
