# dashboard/src/styles/tokens.css

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/styles/tokens.css`                |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-06T23:57:18+02:00                           |
| lastVerifiedCommitHash | `e358c4ac520d94ae2e597ae3cbe186e07a4d1063`       |
| lastVerifiedCommitDate | 2026-07-07T05:26:14+02:00|
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

The global design-token CSS-var layer — the podracer OKLCH palette (note 08) as `:root` vars. As of
slice 5d this is **all** `tokens.css` holds (it was the ~1,200-line monolith; every component style
moved to co-located Panda).

## Code Commentary

### Logic

`:root { color-scheme: dark; --bg/--bg-panel/--ink/--grid; --amber/--cyan/--alarm/--mint/--dormant;
--font-mono; --glow-strength }`, plus — 260703-L14 — the six **rank-insignia tier vars** from the
approved V4 sketch: `--gold` `oklch(0.87 0.15 95)` / `--gold-dim` / `--gold-ghost` (the orchestration
tier: chevrons, hairline, row wash) and `--purple` `oklch(0.76 0.14 305)` / `--purple-dim` /
`--purple-ghost` (management). These back `index.css`'s base layer (body/utilities) and a few Panda
`css()` text-shadows that reference `var(--glow-strength)`. `panda.config.ts` mirrors the same palette
as **typed Panda tokens** (the source the component css/recipes resolve — the L14 components consume
the Panda `gold*`/`purple*` tokens, not these vars).

### Invariants And Boundaries

Tokens only — no component/selector rules. Keep in sync with the Panda token palette in
`panda.config.ts` (two views of one palette during the migration).

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The Panda token mirror of this palette. | L30-L46 | [panda.config.ts](agents-remember/dashboard/panda.config.ts) |

## Update History

- 2026-07-06T23:57:18+02:00 — 260703-L14 (visual hierarchy + chat grouping): added the six rank-insignia
  tier vars (`--gold`/`--gold-dim`/`--gold-ghost`, `--purple`/`--purple-dim`/`--purple-ghost` — the
  V4 sketch's OKLCH values), mirrored as typed Panda tokens in `panda.config.ts` (two views of one
  palette, unchanged rule). Verification metadata pinned until closeout stamps the L14 commit.
- 2026-06-15T17:00 — Created for slice 5d: `tokens.css` reduced to the `:root` design tokens (the
  1.2k-line monolith retired into co-located Panda). Verification metadata pinned until closeout
  stamps the 5d code commit.
