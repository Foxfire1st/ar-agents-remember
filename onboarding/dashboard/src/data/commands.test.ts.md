# dashboard/src/data/commands.test.ts

## Governing Overview

[data overview](overview.md)

## Purpose

The command-registry unit suite (260715-FEUI-L1 S3/S5, extended by FEUI-L4): registration order,
when-gating, replace-by-id semantics, and the default command routing contract, including the live
cycle-effort directions.

## Code Commentary

### Logic

A `ctx()` factory builds a `CommandContext` with `vi.fn()` actions. The describes pin:

- **createCommandRegistry** — `list` keeps registration order and filters by `when`; `run` honors
  the gate and reports ran/not-ran (unknown id = false); replace-by-id + the stale-unregister
  guard (unregistering the FIRST registration must not remove its replacement — the second run
  still fires).
- **registerDefaultCommands** — the v1 id census is present; commands route into the injected
  actions (`rail.toggle` → `toggleRail`, `focus.nextRegion` → `cycleRegion(1)`,
  `keyboard.reference` → `openPalette("keys")`, `session.next` → `switchSession(1)`);
  FEUI-L4 additionally pins `effort.decrease` → `cycleEffort(-1)` and
  `effort.increase` → `cycleEffort(1)` so both chords use the live no-dialog action;
  `palette.open` is gated on the palette being closed; `keyboard.reference` is the only default
  marked `keepsPaletteOpen`.

### Invariants And Boundaries

Pure logic suite — the rendered palette behavior (open/close/focus-return/pages) lives in
`SessionsView.test.tsx`. Test-only.

## Evidence

### Docs References

No Domain Documentation source is configured for this repository; repository code and tests are the authority.

No configured live domain-documentation source was available.

### Repo-Internal References

- The registry + default set under test. [1]
- The DOM-level palette counterpart (ctrl+k open, Enter run, Esc close + focus return). [2]

### Cross-Repo References

No meaningful cross-repo references found.

This file implements a repository-local contract.

## 260715-FEUI-L5 Reliable Submit Delta

The suite now proves the pop-back command dispatches the authority-backed withdrawal path and that
slash-opened palette commands receive the intended initial query. It guards the collision boundary:
composer Alt+Up is pop-back, while the chrome/session navigation chord remains separate.
