# dashboard/src/data/commands.test.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/commands.test.ts`            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-17T08:33+02:00                           |
| lastVerifiedCommitHash | `4293c53b9d6ef2bf0fee7aca11c2677322c4e786`       |
| lastVerifiedCommitDate | 2026-07-17T10:26:02+02:00|
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

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The registry + default set under test. | L56-L179 | [commands.ts](commands.ts) |
| The DOM-level palette counterpart (ctrl+k open, Enter run, Esc close + focus return). | L112-L175 | [../panels/session-cockpit/SessionsView.test.tsx](../panels/session-cockpit/SessionsView.test.tsx) |

## Update History

- 2026-07-17T08:33+02:00 — 260715-FEUI-L4 R7: extended the default-routing case with both live
  cycle-effort directions. Verification metadata is pinned to the contract base until the
  uncommitted L4 code lands.
- 2026-07-17T00:20+02:00 — Created for 260715-FEUI-L1 S3/S5: registry order/gating/replace-by-id
  (incl. the stale-unregister guard) and default-set routing/gating/page-switch marker cases.
  Verification metadata pinned to the task base until closeout stamps the L1 code commit.
