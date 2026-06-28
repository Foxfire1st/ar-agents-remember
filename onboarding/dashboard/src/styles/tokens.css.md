# dashboard/src/styles/tokens.css

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/styles/tokens.css`                |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-06-15T17:00                                 |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`       |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
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
--font-mono; --glow-strength }`. These back `index.css`'s base layer (body/utilities) and a few Panda
`css()` text-shadows that reference `var(--glow-strength)`. `panda.config.ts` mirrors the same palette
as **typed Panda tokens** (the source the component css/recipes resolve).

### Invariants And Boundaries

Tokens only — no component/selector rules. Keep in sync with the Panda token palette in
`panda.config.ts` (two views of one palette during the migration).

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The Panda token mirror of this palette. | L30-L46 | [panda.config.ts](agents-remember/dashboard/panda.config.ts) |

## Update History

- 2026-06-15T17:00 — Created for slice 5d: `tokens.css` reduced to the `:root` design tokens (the
  1.2k-line monolith retired into co-located Panda). Verification metadata pinned until closeout
  stamps the 5d code commit.
