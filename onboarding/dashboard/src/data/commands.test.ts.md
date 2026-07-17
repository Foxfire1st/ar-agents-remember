# dashboard/src/data/commands.test.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/commands.test.ts`            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-17T21:39+02:00 |
| lastVerifiedCommitHash | `f8196d98982f834d68152d307ff8025ea69440d5`       |
| lastVerifiedCommitDate | 2026-07-17T22:08:10+02:00|
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[dashboard/src overview](../overview.md)

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

## Docs References

No Domain Documentation source is configured for this repository; repository code and tests are the authority.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured live domain-documentation source was available. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The registry + default set under test. | L56-L179 | [commands.ts](commands.ts) |
| The DOM-level palette counterpart (ctrl+k open, Enter run, Esc close + focus return). | L112-L175 | [../panels/session-cockpit/SessionsView.test.tsx](../panels/session-cockpit/SessionsView.test.tsx) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| This file implements a repository-local contract. | — | — |

## 260715-FEUI-L5 Reliable Submit Delta

The suite now proves the pop-back command dispatches the authority-backed withdrawal path and that
slash-opened palette commands receive the intended initial query. It guards the collision boundary:
composer Alt+Up is pop-back, while the chrome/session navigation chord remains separate.

## Update History

- 2026-07-17T21:39+02:00 — FEUI-L5: added command-level pop-back and slash-query regression proof.

- 2026-07-17T08:33+02:00 — 260715-FEUI-L4 R7: extended the default-routing case with both live
  cycle-effort directions. Verification metadata is pinned to the contract base until the
  uncommitted L4 code lands.
- 2026-07-17T00:20+02:00 — Created for 260715-FEUI-L1 S3/S5: registry order/gating/replace-by-id
  (incl. the stale-unregister guard) and default-set routing/gating/page-switch marker cases.
  Verification metadata pinned to the task base until closeout stamps the L1 code commit.
