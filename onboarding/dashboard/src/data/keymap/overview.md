# dashboard/src/data/keymap/ — Keyboard Zone Contract Overview

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| sourceRoute            | `dashboard/src/data/keymap/`                     |
| doc_type               | `route-local-overview`                           |
| lastUpdated            | 2026-07-17T00:20+02:00                           |
| lastVerifiedCommitHash | `ee955085a2010f62e9ad4d2bdc6aa77975daa5f3`       |
| lastVerifiedCommitDate | 2026-07-17T00:42:07+02:00|
| governingOverview      | `../../overview.md`                              |

## Governing Overview

[dashboard/src overview](../../overview.md) — `data/` has no route overview of its own; the
`dashboard/src` overview governs it directly, and this overview governs the `keymap/` slice.

## Purpose

`data/keymap/` is the **pure, xterm-free keyboard-ownership contract** for the Sessions cockpit
(260715-FEUI-L1 S4, design §5.2/§5.3). Everything here is data + pure functions so vitest covers
the routing contract without a terminal, and so every consumer — the tinykeys binding
(`panels/session-cockpit/useKeyboardZones.ts`), the `?` keyboard-reference palette page
(`CommandPalette.tsx`), and the future L6 xterm `attachCustomKeyEventHandler` — reads ONE source
and can never drift apart. Three zones own keys: **chrome** (the shell — chords may be handled,
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
  `slashOpensPalette` (the pure `/`-at-line-start composer rule shared by the placeholder textarea
  and the future CM6 composer).
- `chords.ts` — the chrome/composer chord tables (`CHROME_CHORDS`, `COMPOSER_CHORDS`) with
  per-chord zone lists: harness-owned chords (Alt+↑/↓, Alt+,/.) are deliberately chrome-only so
  they always pass through over a live PTY.
- `focus.ts` — the F6 region cycle (rail → stage → inspector → statusline, collapsed panels drop
  out) + the region/stage-header/PTY-host focus selectors.
- `zones.test.ts` / `focus.test.ts` — the contract suites (PTY passthrough invariants,
  reserved-set hygiene, printable suppression, region cycle).

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
- **Pure and DOM-light** — structural `KeyEventLike`/`ZoneElementLike` surfaces keep tests free of
  real DOM events; no React, no xterm, no window access in this route.

## Hot Path Summary

The keyboard zone contract: `zoneForTarget` resolves chrome/composer/pty from `data-kbzone`
markers, `routeKey` handles a PTY key only when `matchReservedChord` matches the bound reserved
set (everything else — including Esc — passes to the harness) and suppresses printable bindings in
editable targets; `PTY_RESERVED` carries the five-source collision-verification records (the
Ctrl+Alt+PageUp/PageDown replacement pair), `CHROME_CHORDS`/`COMPOSER_CHORDS` are the zone-scoped
tables, and `nextRegion` drives the F6 cycle with collapsed panels dropping out.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The thin React binding that installs these tables via tinykeys (capture phase, ignore disabled). | [panels/session-cockpit/useKeyboardZones.ts](agents-remember/dashboard/src/panels/session-cockpit/useKeyboardZones.ts) |
| The `?` reference page that renders these same tables (one source, two surfaces). | [panels/session-cockpit/CommandPalette.tsx](agents-remember/dashboard/src/panels/session-cockpit/CommandPalette.tsx) |
| The command ids the chord tables dispatch into. | [data/commands.ts](agents-remember/dashboard/src/data/commands.ts) |
| The DOM that carries the `data-kbzone`/`data-region` markers this contract resolves. | [panels/session-cockpit/SessionsView.tsx](agents-remember/dashboard/src/panels/session-cockpit/SessionsView.tsx) |

## Update History

- 2026-07-17T00:20+02:00 — Created for 260715-FEUI-L1 S4 (tinykeys zones + focus model + collision
  audit): the new `data/keymap/` slice — reserved set with per-chord five-source verification
  records (incl. the R6 chord replacement Ctrl+Alt+[ / ] → Ctrl+Alt+PageUp / PageDown), zone
  resolution + routing contract, chrome/composer chord tables, and the F6 region cycle. Review
  round 2 removed the dead `ZoneChord.printable` field (suppression is generic via `routeKey`).
  Verification metadata pinned to the task base until closeout stamps the L1 code commit.
