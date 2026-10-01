# dashboard/src/data/keymap/ — Keyboard Zone Contract Overview

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| sourceRoute            | `dashboard/src/data/keymap/`                     |

## Governing Overview

[data overview](../overview.md) — this child owns keyboard contracts while the data overview owns
the surrounding cockpit state and authority boundaries.

## 260928-MIK-L33 A Fourth Zone: The Intent Reviewer's Change Traversal

MIK-R33 rule 7 (adopting ICR-R32) registers the reviewer's `j`/`k` through this route. [`zones.ts`](zones.ts.md) adds
the `review` zone to `Zone` and to `zoneForTarget`; `routeKey` routes it by the chrome/composer rule, so the printable
chords are inert in inputs, textareas, selects and contenteditable regions, and the `review` zone is never the PTY
zone. [`chords.ts`](chords.ts.md) adds `REVIEW_CHORDS` (`J` → `review.nextChange`, `K` → `review.previousChange`,
`review` zone only), and [`preferences.ts`](preferences.ts.md) puts it into `DEFAULT_BINDINGS`, so the two commands are
known, rebindable through `cockpit.sessions.keymap.v1` and listed on the `?` page (`CommandPalette.tsx`'s "Intent
reviewer" group). The binding itself is not `useKeyboardZones`'s: `panels/review/changeTraversal.ts` binds the
effective chords with tinykeys on the reviewer's `data-kbzone="review"` root (`ReviewSurface.tsx`), checking the
target's zone and `routeKey` per event. **Observations for the owner** (Todos on the cards): the two review commands
have no `data/commands.ts` registry entry, which the chord card's invariant otherwise requires, and `zones.ts`'s header
comment still says "Three zones:".

- The reviewer's zone and chords. [1]
- The reviewer's own binding on its zone. [2]

## Purpose

`data/keymap/` is the **xterm-free keyboard-ownership contract** for the canonical Chats cockpit
(260715-FEUI-L1 S4, design §5.2/§5.3). Everything here is data + pure functions so vitest covers
the routing contract without a terminal, and so every consumer — the tinykeys binding
(`panels/session-cockpit/useKeyboardZones.ts`), the `?` keyboard-reference palette page
(`CommandPalette.tsx`), and the future L6 xterm `attachCustomKeyEventHandler` — reads ONE source
and can never drift apart. FEUI-L8 adds a versioned effective-keymap preference layer consumed by
those same surfaces and by CodeMirror. Four zones own keys: **chrome** (the shell — chords may be handled,
printable bindings never fire in editable targets), **composer** (the editor owns its keys; only
composer-declared chords are handled), **pty** (EVERY key passes to the hosted harness except
exactly the bound reserved set; no bare-Esc sequence is ever claimed), and, since MIK-L33, **review** (the intent
reviewer: its own `j`/`k` fire only while focus is inside it, under the chrome rule).

## Route Model

- `reserved.ts` — `PTY_RESERVED`: the only chords the PTY zone ever intercepts (ctrl+; palette,
  F6 exit-to-chrome, ctrl+alt+pageup/pagedown session prev/next) plus two reserved-but-UNBOUND
  clipboard slots (selection-aware ctrl+c, ctrl+shift+c — flagged Firefox-non-preventable, L6).
  Every chord carries a five-source `verifiedAgainst` record (codex/pi/claude/chrome/firefox) —
  the durable R6 collision-audit evidence. `matchReservedChord` is the single PTY gate;
  `BROWSER_FORBIDDEN` lists the chords no zone may ever bind.
- `zones.ts` — `zoneForTarget` (nearest `data-kbzone` container; default chrome), `routeKey` (the
  routing contract), `isEditableTarget`/`isPrintable` (the generic R7 printable suppression), and
  `slashOpensPalette` (the pure `/`-at-line-start rule consumed by the live FEUI-L5 CodeMirror
  composer).
- `chords.ts` — the chrome/composer chord tables (`CHROME_CHORDS`, `COMPOSER_CHORDS`) with
  per-chord zone lists. Chrome Alt+↑/↓ retains session cycling; composer Alt+Up owns FEUI-L5
  authoritative pop-back. PTY receives both unchanged because only its explicit reserved set is
  intercepted. 260718-CHATS-L4 adds the `conversation.stop` chord (default `Control+Shift+Period`,
  chrome+composer zones, PTY-excluded — the R6 rebindable non-Escape stop, collision-audited as the
  sole `Control+Shift` entry) and removes the stale `turn.stop` binding.
- `focus.ts` — the F6 region cycle (rail → stage → inspector, collapsed panels drop out) + the
  region/stage-header/PTY-host focus selectors. StatusLine was removed and is no longer an F6 stop.
- `preferences.ts` — strict `cockpit.sessions.keymap.v1` persistence, same-tab external-store and
  cross-tab storage subscription, user overrides, Emacs/Vim composer profile, CodeMirror chord
  conversion, and the effective signature used for live reconfiguration. Browser-reserved,
  printable-composer, collision, and F6-removal/rebind attempts fall back with visible issues.
  260718-CHATS-L4 adds the pure `ariaKeyshortcuts(chord)` helper — it renders a validated tinykeys
  chord as the WAI-ARIA `aria-keyshortcuts` token (`Control+Shift+Period` → `Control+Shift+.`), so the
  interrupt control's advertised shortcut (`bindingFor(effective, "conversation.stop")`) follows a
  rebind and stays truthful to assistive technology.
- `zones.test.ts` / `focus.test.ts` — the contract suites (PTY passthrough invariants,
  reserved-set hygiene, printable suppression, region cycle).
- `preferences.test.ts` — effective-map parsing, validation, profile, immutable-F6, Meta/browser
  safety, and same-/cross-tab update coverage.

## Invariants And Boundaries

- **`PTY_RESERVED` is the single source of interceptable chords** — the `?` page renders it, the
  tinykeys layer binds it, and L6's xterm handler must consume `matchReservedChord`; never fork
  the list.
- **No bare-Esc claim over the PTY** — Codex binds Esc = interrupt and Claude Code owns
  Esc Esc = /rewind (both source/bundle-confirmed); `zones.test.ts` pins it.
- **The R6 rule: a collision replaces the CHORD, not the rule.** The original session-switch pair
  Ctrl+Alt+[ / Ctrl+Alt+] was replaced by Ctrl+Alt+PageUp / Ctrl+Alt+PageDown because Pi binds
  ctrl+alt+] (tui.editor.jumpBackward) and Ctrl+Alt+['s terminal encoding is ESC ESC (`\x1b\x1b`)
  — Claude Code's rewind — on any interception miss. The replacement pair encodes as distinct CSI
  sequences (`5;7~`/`6;7~`) no audited harness binds, so even a leaked event is inert.
- Every bound chord must be verified fully clear across all five sources; collisions may exist
  only on unbound reserved slots (tested).
- **Alt+Up ownership is zone-specific** — composer dispatches `composer.popBack`, chrome dispatches
  session navigation, and PTY passes the native key through. No global handler may collapse them.
- **F6 is immutable** — user preferences and Vim mode may not remove or rebind the focus escape.
  Vim owns Escape for insert/normal transitions; F6 remains active from every composer mode.
- The core routing modules remain pure/DOM-light. `preferences.ts` is the intentional browser/React
  boundary for localStorage and external-store subscription; no module in this route imports xterm.

## Hot Path Summary

The keyboard zone contract: `preferences.ts` first resolves defaults, validated overrides, and the
composer profile into one effective map; `zoneForTarget` resolves chrome/composer/pty from `data-kbzone`
markers, `routeKey` handles a PTY key only when `matchReservedChord` matches the bound reserved
set (everything else — including Esc — passes to the harness) and suppresses printable bindings in
editable targets; `PTY_RESERVED` carries the five-source collision-verification records (the
Ctrl+Alt+PageUp/PageDown replacement pair), `CHROME_CHORDS`/`COMPOSER_CHORDS` are the zone-scoped
tables (including the composer/chrome Alt+Up split), and `nextRegion` drives the F6 cycle with
collapsed panels dropping out.

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation entries are configured. Keyboard
claims were therefore verified against the repository's collision records, source, and tests.

No configured Domain Documentation source exists for the effective keymap.

### Cross-Repo References

The keymap is repository-local. Vendor/browser collision evidence is recorded in `reserved.ts`, but
no cross-repository implementation source is imported or treated as governing code.

No applicable cross-repository source governs this route.

### Repo-Internal References

- The effective-keymap preference and validation boundary. [3]
- The thin React binding that installs the effective tables via tinykeys. [4]
- The `?` reference/profile page that renders the same effective map. [5]
- The command ids the chord tables dispatch into. [6]
- The DOM that carries the `data-kbzone`/`data-region` markers. [7]
- The live CodeMirror surface that consumes profile and chord reconfiguration. [8]
