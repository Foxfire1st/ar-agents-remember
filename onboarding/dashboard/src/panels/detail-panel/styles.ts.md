# dashboard/src/panels/detail-panel/styles.ts

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/detail-panel/styles.ts`               |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-07T08:19Z                                           |
| lastVerifiedCommitHash | `e66f1f3894116e0bb37b49f178d8bfcb130a7e28`                  |
| lastVerifiedCommitDate | 2026-09-28T20:02:47+02:00|
| governingOverview      | `../overview.md`                                            |

## Governing Overview

[panels/ overview](../overview.md)

## Purpose

The Panda CSS recipes of the DetailPanel, extracted from `DetailPanel.tsx` by the
260731-EFA-L8 split. Owns sizing, the phase stepper, state badges, series/sub-task
slice list, cross-master button, breadcrumb, worktree spine lanes, and reader
typography.

## Code Commentary

### Logic

Static atoms are `css({...})`; `step` and `lane` are `cva` keyed on state. All colours
go through `token(colors.*)`.

Since `260921-ICR-L47`, three classes style the brief-state disclosure the entry controls share
(`entryState.tsx`): `entryStateDetails` (inline, full-width when open), `entryStateSummary` (the bordered
`?` marker, native marker hidden) and `entryStateBody` (a bounded-width paragraph that wraps long codes).

| Finding | Anchor | Source |
| --- | --- | --- |
| The three disclosure classes. | `entryStateDetails`; `entryStateSummary`; `entryStateBody` | dashboard/src/panels/detail-panel/styles.ts:175-202 |

### Conventions

Styles stay co-located with the panel; no animation in this domain.

### Invariants And Boundaries

The `sizing` flex rule preserves the panel's fill behavior.

### Todos

None recorded.

## Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant domain documentation was found. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The panel layout/stepper/badge recipes. | `sizing`; `stepper`; `step`; `badge` | dashboard/src/panels/detail-panel/styles.ts:5-52 |
| The slice/cross/spine recipes. | `slice`; `sliceButton`; `crossButton`; `lane` | dashboard/src/panels/detail-panel/styles.ts:55-66; dashboard/src/panels/detail-panel/styles.ts:69-88; dashboard/src/panels/detail-panel/styles.ts:91-110; dashboard/src/panels/detail-panel/styles.ts:133-145 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History
- 2026-09-28T17:11:24+02:00 — 260921-ICR-L47 curator (uncommitted candidate tree `72efa4bbc169b16afe8ef249499edf79cad9940d` over code base `58e22246cc09ef0ee12095e284a111a475081c38`): **body update — three disclosure classes for the entry's brief states (`ICR-R24@v3`).** No stamp advanced.

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the styles
  module extracted from `DetailPanel.tsx`. Verification pinned to the leaf base until
  closeout stamps the code commit.
