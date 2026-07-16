# dashboard/src/data/keymap/zones.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/keymap/zones.ts`             |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-17T00:20+02:00                           |
| lastVerifiedCommitHash | `ee955085a2010f62e9ad4d2bdc6aa77975daa5f3`       |
| lastVerifiedCommitDate | 2026-07-17T00:42:07+02:00|
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

- `zoneForTarget(target)` (L28-L32): nearest `[data-kbzone]` container via `closest`; `pty` and
  `composer` are recognized, everything else (unknown values, no container, null target) defaults
  to `chrome`.
- `isEditableTarget` (L35-L42): contenteditable, TEXTAREA, SELECT, and non-readOnly INPUT consume
  plain typing.
- `isPrintable` (L45-L47): single-character key with no ctrl/alt/meta; shift allowed (`?` etc.).
- `routeKey(zone, ev, target)` (L54-L58) — the contract: `pty` handles ONLY a
  `matchReservedChord` hit (everything else passes through); chrome/composer pass printable keys
  through when the target is editable (the GENERIC R7 suppression — there is deliberately no
  per-chord printable flag; review round 2 removed one from `chords.ts`), and handle everything
  else.
- `slashOpensPalette(value, selectionStart)` (L64-L67): the composer `/`-rule — true only at
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

| Finding | Citations | Source Path |
| --- | --- | --- |
| Zone resolution, editable/printable classification, the routing contract, and the `/` rule. | L28-L67 | [zones.ts](zones.ts) |
| The reserved-set gate the pty branch defers to. | L193-L199 | [reserved.ts](reserved.ts) |
| The React binding that calls `zoneForTarget`/`routeKey`/`slashOpensPalette` per event. | L39-L77 | [../../panels/session-cockpit/useKeyboardZones.ts](../../panels/session-cockpit/useKeyboardZones.ts) |
| The contract suite: PTY passthrough (incl. bare Esc + harness-owned chords), printable suppression, the `/` rule. | L35-L160 | [zones.test.ts](zones.test.ts) |

## Update History

- 2026-07-17T00:20+02:00 — Created for 260715-FEUI-L1 S4 (R5/R7): zone resolution over
  `data-kbzone` markers, the `routeKey` contract (PTY = reserved-set-only interception with
  everything else passing through; generic printable suppression in editable targets), and the
  pure `slashOpensPalette` composer rule. Verification metadata pinned to the task base until
  closeout stamps the L1 code commit.
