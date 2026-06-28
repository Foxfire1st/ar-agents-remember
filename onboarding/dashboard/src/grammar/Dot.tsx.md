# dashboard/src/grammar/Dot.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/grammar/Dot.tsx`                  |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-06-15T17:00                                 |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`       |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[grammar/ overview](overview.md)

## Purpose

`Dot` is the state/severity dot — colour-carries lifecycle state (running/blocked/paused/…) or
attention severity (alarm/warn/info), note 08 ("state by colour, never chrome").

## Code Commentary

### Logic

A Panda `cva` with a `variant` map; the base is nominal amber. `blocked`/`alarm` add the shared
`pulse` animation (≤3 flashes/s, WCAG 2.3.1). The component takes a free `variant: string`; a
`KNOWN` Set guards which variants resolve (unknown → base), so a new state never throws.

### Invariants And Boundaries

Presentational, `aria-hidden`. The `pulse` keyframe is the shared global one (`index.css`) and
freezes under `?effects=off`.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The shared `pulse` keyframe used by blocked/alarm. | L66-L75 | [index.css](../index.css) |

## Update History

- 2026-06-15T17:00 — Created for slice 5d: `Dot` migrated to a Panda `cva` (was `.dot--*` classes).
  Verification metadata pinned until closeout stamps the 5d code commit.
