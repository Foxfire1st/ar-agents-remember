# dashboard/src/data/commands.ts

## Governing Overview

[data overview](overview.md)

## Purpose

The **cockpit command registry** (260715-FEUI-L1 S3, R4): the single options source behind BOTH
command surfaces — the cmdk palette and chord dispatch (`data/keymap` tables carry command ids,
never functions). Commands are `(id, title, when, run)`; `when` gates visibility AND runnability
against a context snapshot the view supplies, so later leaves extend the palette by REGISTERING
commands, never by editing the palette component. Pure and React-free: actions are injected
through the context (the view owns the DOM).

## Code Commentary

### Logic

- cit:([`CommandContext`], dashboard/src/data/commands.ts:13-32): view facts (`railCollapsed`/`inspectorCollapsed`/`paletteOpen`) +
  injected action seams. Panel/focus/palette, session switching, and FEUI-L4 effort cycling are
  live; `submitComposer` remains the FEUI-L5 seam.
- cit:([`Command`], dashboard/src/data/commands.ts:34-45): optional `keywords` (palette search), display-only `chord` label (binding
  lives in `keymap/`), and `keepsPaletteOpen` — the palette-page-switch marker (selection keeps
  the palette open; established by `keyboard.reference`).
- cit:([`createCommandRegistry`], dashboard/src/data/commands.ts:57-81): a `Map`-backed registry. `register` replaces by id and
  returns an unregister that removes ONLY its own registration (a stale unregister can't kill a
  replacement — L61-L64). `list(ctx)` returns registration-ordered, `when`-filtered commands;
  `run(id, ctx)` honors the `when` gate and reports whether it ran.
- cit:([`registerDefaultCommands`], dashboard/src/data/commands.ts:189-192) — the v1 set: `palette.open` (gated on closed,
  ctrl+k), `keyboard.reference` (`keepsPaletteOpen`, opens the `keys` page), `rail.toggle`,
  `inspector.toggle`, `focus.nextRegion`/`prevRegion` (F6/Shift+F6), `focus.stageHeader`
  (composer Esc), `focus.exitToChrome` (PTY F6 — same landing as `focus.stageHeader`),
  `focus.terminal`, `session.prev/next` (alt+↑/↓ + the reserved ctrl+alt+pageup/pagedown — LIVE
  since 260715-FEUI-L2: the view's injected `switchSession` action cycles the rail order, and the
  "(stub — L2)" title suffixes are gone), live `effort.decrease/increase` (alt+,/.) with searchable
  cycle/thinking/reasoning keywords (260715-FEUI-L4 R7), and the remaining honest
  `composer.submit` stub (ctrl+↵). Each route uses an injected context action, so leaf work
  replaces behavior without changing the stable command id or chord.

### Invariants And Boundaries

- One options source: the palette lists `registry.list`, chords dispatch `registry.run` — never a
  second command list.
- Registration order is presentation order; replace-by-id is the extension mechanism.
- Command ids and chord labels are stable — leaf work swaps the injected action only.
- Pure module: no React, no DOM, no store reads; everything observable arrives via
  `CommandContext`.

## Evidence

### Docs References

No Domain Documentation source is configured for this repository; repository code and tests are the authority.

No configured live domain-documentation source was available.

### Repo-Internal References

- The registry, replace-by-id unregister guard, and the default set with the stub seams. [1]
- The view builds the context and dispatches chord command ids into the registry. [2]
- The palette clears its query when the selected command keeps the palette open. [3]
- The chord tables that carry these command ids per zone. [4]
- The registry suite pins registration order and when-predicate filtering. [5]
- The registry suite pins replacement-by-id and stale-unregister behavior. [6]
- The default-command suite pins live panel/focus actions and honest stubs. [7]
- The default-command suite pins palette-open gating. [8]

### Cross-Repo References

No meaningful cross-repo references found.

This file implements a repository-local contract.

## 260715-FEUI-L5 Reliable Submit Delta

The command registry now owns `composer.popBack` on Alt+Up and carries an `initialQuery` when slash
text opens the palette. Pop-back delegates to the authoritative withdrawal client; it is not a local
queue splice. Palette normalization removes the leading slash exactly once so command filtering and
keyboard invocation share one query contract.
