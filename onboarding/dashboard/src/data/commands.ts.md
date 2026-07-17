# dashboard/src/data/commands.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/commands.ts`                 |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-17T21:39+02:00 |
| lastVerifiedCommitHash | `f8196d98982f834d68152d307ff8025ea69440d5`       |
| lastVerifiedCommitDate | 2026-07-17T22:08:10+02:00|
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

The **cockpit command registry** (260715-FEUI-L1 S3, R4): the single options source behind BOTH
command surfaces — the cmdk palette and chord dispatch (`data/keymap` tables carry command ids,
never functions). Commands are `(id, title, when, run)`; `when` gates visibility AND runnability
against a context snapshot the view supplies, so later leaves extend the palette by REGISTERING
commands, never by editing the palette component. Pure and React-free: actions are injected
through the context (the view owns the DOM).

## Code Commentary

### Logic

- `CommandContext` (L13-L31): view facts (`railCollapsed`/`inspectorCollapsed`/`paletteOpen`) +
  injected action seams. Panel/focus/palette, session switching, and FEUI-L4 effort cycling are
  live; `submitComposer` remains the FEUI-L5 seam.
- `Command` (L33-L44): optional `keywords` (palette search), display-only `chord` label (binding
  lives in `keymap/`), and `keepsPaletteOpen` — the palette-page-switch marker (selection keeps
  the palette open; established by `keyboard.reference`).
- `createCommandRegistry()` (L56-L80): a `Map`-backed registry. `register` replaces by id and
  returns an unregister that removes ONLY its own registration (a stale unregister can't kill a
  replacement — L61-L64). `list(ctx)` returns registration-ordered, `when`-filtered commands;
  `run(id, ctx)` honors the `when` gate and reports whether it ran.
- `registerDefaultCommands(registry)` (L87-L179) — the v1 set: `palette.open` (gated on closed,
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

## Docs References

No Domain Documentation source is configured for this repository; repository code and tests are the authority.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured live domain-documentation source was available. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The registry, replace-by-id unregister guard, and the default set with the stub seams. | L56-L179 | [commands.ts](commands.ts) |
| The view builds `CommandContext` (live actions + honest stubs) and dispatches chord command ids into `registry.run`. | L253-L296 | [../panels/session-cockpit/SessionsView.tsx](../panels/session-cockpit/SessionsView.tsx) |
| The palette renders `registry.list` and honors `keepsPaletteOpen` on selection. | L121-L175 | [../panels/session-cockpit/CommandPalette.tsx](../panels/session-cockpit/CommandPalette.tsx) |
| The chord tables that carry these command ids per zone. | L20-L86 | [keymap/chords.ts](keymap/chords.ts) |
| The unit suite: order, when-gating, replace-by-id, default-set routing, palette gating. | L36-L115 | [commands.test.ts](commands.test.ts) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| This file implements a repository-local contract. | — | — |

## 260715-FEUI-L5 Reliable Submit Delta

The command registry now owns `composer.popBack` on Alt+Up and carries an `initialQuery` when slash
text opens the palette. Pop-back delegates to the authoritative withdrawal client; it is not a local
queue splice. Palette normalization removes the leading slash exactly once so command filtering and
keyboard invocation share one query contract.

## Update History

- 2026-07-17T21:39+02:00 — FEUI-L5: documented `composer.popBack`, Alt+Up authority, and slash-
  initiated palette query normalization.

- 2026-07-17T08:33+02:00 — 260715-FEUI-L4 R7 made `effort.decrease` and
  `effort.increase` live: user-facing cycle titles and search keywords now dispatch -1/+1 into
  the exact-session effort-cycle action without opening the dialog. The composer seam remains
  stubbed for L5. Verification metadata is pinned to the contract base until L4 is committed.
- 2026-07-17T02:30+02:00 — 260715-FEUI-L2: `session.prev`/`session.next` titles dropped the
  "(stub — L2)" suffix — the commands are live (SessionsView injects a real `switchSession` that
  cycles `railModel.railCycleOrder`); ids and chords unchanged, exactly the stub-seam contract.
  L2 also registers DYNAMIC commands through this registry from the view (tree toggle,
  attention.jump, bulk-end mirrors with counts+names in the title, per-seat question triage) —
  registration stays the extension mechanism. Verification metadata pinned to the leaf base until
  closeout stamps the L2 code commit.
- 2026-07-17T00:20+02:00 — Created for 260715-FEUI-L1 S3 (R4): the pure extensible command
  registry (register/replace-by-id with stale-unregister protection, when-gated list/run,
  registration order) + `registerDefaultCommands` (palette/panels/focus live; session/effort/
  composer honest stubs for L2/L4/L5; `keepsPaletteOpen` page-switch pattern). Verification
  metadata pinned to the task base until closeout stamps the L1 code commit.
