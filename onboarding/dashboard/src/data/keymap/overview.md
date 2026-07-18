# dashboard/src/data/keymap/ — Keyboard Zone Contract Overview

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| sourceRoute            | `dashboard/src/data/keymap/`                     |
| doc_type               | `route-local-overview`                           |
| lastUpdated            | 2026-07-18T07:22+02:00 |
| lastVerifiedCommitHash | `e3f94568a0f5f78efc5ce7c26d94e6d103caae5f`       |
| lastVerifiedCommitDate | 2026-07-18T07:47:42+02:00|
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[data overview](../overview.md) — this child owns keyboard contracts while the data overview owns
the surrounding cockpit state and authority boundaries.

## Purpose

`data/keymap/` is the **xterm-free keyboard-ownership contract** for the canonical Chats cockpit
(260715-FEUI-L1 S4, design §5.2/§5.3). Everything here is data + pure functions so vitest covers
the routing contract without a terminal, and so every consumer — the tinykeys binding
(`panels/session-cockpit/useKeyboardZones.ts`), the `?` keyboard-reference palette page
(`CommandPalette.tsx`), and the future L6 xterm `attachCustomKeyEventHandler` — reads ONE source
and can never drift apart. FEUI-L8 adds a versioned effective-keymap preference layer consumed by
those same surfaces and by CodeMirror. Three zones own keys: **chrome** (the shell — chords may be handled,
printable bindings never fire in editable targets), **composer** (the editor owns its keys; only
composer-declared chords are handled), and **pty** (EVERY key passes to the hosted harness except
exactly the bound reserved set; no bare-Esc sequence is ever claimed).

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
  intercepted.
- `focus.ts` — the F6 region cycle (rail → stage → inspector → statusline, collapsed panels drop
  out) + the region/stage-header/PTY-host focus selectors.
- `preferences.ts` — strict `cockpit.sessions.keymap.v1` persistence, same-tab external-store and
  cross-tab storage subscription, user overrides, Emacs/Vim composer profile, CodeMirror chord
  conversion, and the effective signature used for live reconfiguration. Browser-reserved,
  printable-composer, collision, and F6-removal/rebind attempts fall back with visible issues.
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

## Docs References

The curator checked `system/sources.md`; no Domain Documentation entries are configured. Keyboard
claims were therefore verified against the repository's collision records, source, and tests.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured Domain Documentation source exists for the effective keymap. | `system/sources.md` checked | — |

## Cross-Repo References

The keymap is repository-local. Vendor/browser collision evidence is recorded in `reserved.ts`, but
no cross-repository implementation source is imported or treated as governing code.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source governs this route. | Import and collision-record review | — |

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The effective-keymap preference and validation boundary. | [preferences.ts](preferences.ts) |
| The thin React binding that installs the effective tables via tinykeys. | [useKeyboardZones.ts](../../panels/session-cockpit/useKeyboardZones.ts) |
| The `?` reference/profile page that renders the same effective map. | [CommandPalette.tsx](../../panels/session-cockpit/CommandPalette.tsx) |
| The command ids the chord tables dispatch into. | [commands.ts](../commands.ts) |
| The DOM that carries the `data-kbzone`/`data-region` markers. | [SessionsView.tsx](../../panels/session-cockpit/SessionsView.tsx) |
| The live CodeMirror surface that consumes profile and chord reconfiguration. | [SessionComposer.tsx](../../panels/SessionComposer.tsx) |

## Update History

- 2026-07-18T07:22+02:00 — FEUI-L8: added the versioned effective-keymap preference layer,
  browser/Meta safety, immutable F6, same-/cross-tab updates, and Emacs/Vim CodeMirror profiles;
  moved governance under the new data overview. Verification remains pinned to the leaf base.

- 2026-07-17T21:39+02:00 — 260715-FEUI-L5 curator: replaced the future-composer note with the live
  CodeMirror consumer and documented zone-sensitive Alt+Up ownership: authoritative pop-back in the
  composer, session cycling in chrome, untouched native input in PTY.

- 2026-07-17T00:20+02:00 — Created for 260715-FEUI-L1 S4 (tinykeys zones + focus model + collision
  audit): the new `data/keymap/` slice — reserved set with per-chord five-source verification
  records (incl. the R6 chord replacement Ctrl+Alt+[ / ] → Ctrl+Alt+PageUp / PageDown), zone
  resolution + routing contract, chrome/composer chord tables, and the F6 region cycle. Review
  round 2 removed the dead `ZoneChord.printable` field (suppression is generic via `routeKey`).
  Verification metadata pinned to the task base until closeout stamps the L1 code commit.
