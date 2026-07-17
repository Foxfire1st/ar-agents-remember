# dashboard/src/data/commands.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/commands.ts`                 |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-17T02:30+02:00                           |
| lastVerifiedCommitHash | `e2b99dcd71fb6ca31f642dd61c3c16f3d3d05bf5`       |
| lastVerifiedCommitDate | 2026-07-17T02:52:07+02:00|
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
  injected actions — live panel/focus/palette actions plus the three L2/L4/L5 stub seams
  (`switchSession`, `cycleEffort`, `submitComposer`).
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
  "(stub — L2)" title suffixes are gone), and the honest stubs `effort.decrease/increase`
  (alt+,/.) and `composer.submit` (ctrl+↵) — each stub routes through an injected context action
  so L4/L5 replace the ACTION, never the command id or chord.

### Invariants And Boundaries

- One options source: the palette lists `registry.list`, chords dispatch `registry.run` — never a
  second command list.
- Registration order is presentation order; replace-by-id is the extension mechanism.
- Stub command ids and chord labels are FINAL — later leaves swap the injected action only.
- Pure module: no React, no DOM, no store reads; everything observable arrives via
  `CommandContext`.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The registry, replace-by-id unregister guard, and the default set with the stub seams. | L56-L179 | [commands.ts](commands.ts) |
| The view builds `CommandContext` (live actions + honest stubs) and dispatches chord command ids into `registry.run`. | L253-L296 | [../panels/session-cockpit/SessionsView.tsx](../panels/session-cockpit/SessionsView.tsx) |
| The palette renders `registry.list` and honors `keepsPaletteOpen` on selection. | L121-L175 | [../panels/session-cockpit/CommandPalette.tsx](../panels/session-cockpit/CommandPalette.tsx) |
| The chord tables that carry these command ids per zone. | L20-L86 | [keymap/chords.ts](keymap/chords.ts) |
| The unit suite: order, when-gating, replace-by-id, default-set routing, palette gating. | L36-L115 | [commands.test.ts](commands.test.ts) |

## Update History

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
