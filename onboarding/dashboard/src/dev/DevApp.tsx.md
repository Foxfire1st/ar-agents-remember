# dashboard/src/dev/DevApp.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/dev/DevApp.tsx`                    |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-06-15T17:00                                 |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`       |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

The DEV-only harness router (lazy-loaded from `App` under `import.meta.env.DEV`, so it is
dead-code-eliminated from the production bundle). `/dev/reference` = the mc2 mount; `/dev/bench` =
the component gallery; otherwise a small index.

## Code Commentary

### Logic

Path-prefix routing over `window.location.pathname`. Imports `./dev.css` (the co-located dev-gallery
styles, slice 5d) and uses the global `.raw-list` utility (index.css).

### Invariants And Boundaries

DEV-only — never ships in production (the static `import.meta.env.DEV` branch in `App.tsx` drops the
chunk). Its CSS is co-located in `dev.css`, loaded only here.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The DEV-only route gate that drops this chunk in prod. | L8-L18 | [App.tsx](../App.tsx) |
| The co-located dev-gallery styles it imports. | — | [dev.css](dev.css) |

## Update History

- 2026-06-15T17:00 — Created for slice 5d: now imports the co-located `dev.css` (the dev-gallery
  styles moved out of the retired monolith). Verification metadata pinned until closeout stamps the
  5d code commit.
