# dashboard/src/data/keymap/preferences.test.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/keymap/preferences.test.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-18T07:22+02:00 |
| lastVerifiedCommitHash | `e3f94568a0f5f78efc5ce7c26d94e6d103caae5f` |
| lastVerifiedCommitDate |  2026-07-18T07:47:42+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[data/keymap overview](overview.md)

## Purpose

Pins effective-keymap persistence, validation, profile behavior, and same-/cross-tab subscription.

## Code Commentary

The suite covers valid overrides and profiles; malformed payloads; collision, printable-composer,
browser-reserved, and Meta-chord refusal; immutable F6 behavior; parser normalization; same-tab
writer notification; and browser `storage` propagation.

## Invariants And Boundaries

Tests must prove both the accepted effective binding and the visible issue for rejected input. A
test that only asserts fallback would hide why an operator preference was ignored.

## Docs References

The curator checked the memory repository's `system/sources.md`; it has no configured Domain
Documentation entries. This card was verified from its direct source/tests and the reviewed L8
task/worker/reviewer evidence.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | `system/sources.md` checked | — |

## Cross-Repo References

The suite tests a repository-local module and browser storage doubles; no cross-repository source applies.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Unit under test. | [preferences.ts](preferences.ts) |

## Update History

- 2026-07-18T07:22+02:00 — Created for FEUI-L8 effective-keymap regressions; verification metadata
  remains blank until the new source is committed.
