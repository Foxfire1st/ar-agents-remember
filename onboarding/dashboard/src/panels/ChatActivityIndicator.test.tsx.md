# dashboard/src/panels/ChatActivityIndicator.test.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/ChatActivityIndicator.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-12T17:50 |
| lastVerifiedCommitHash | `842b487b854503d95c9c2d9dce1841198ba93c7d` |
| lastVerifiedCommitDate | 2026-07-24T17:08:25+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[panels overview](overview.md)

## Purpose

Focused Vitest coverage for Operations chat activity identity, state mapping, aggregation, accessibility, and omission rules.

## Code Commentary

### Logic

The fixture creates live harness sessions with a qualified L6 leaf key. Tests pin busy, awaiting-input, stale/missing, multi-seat deterministic detail, exact-leaf isolation before lifecycle fallback, lifecycle-only fallback, and omission when no live bound harness exists.

### Conventions

The test uses a small local `session` builder and Testing Library cleanup; it tests the pure summary and the rendered `role="status"` without touching the session poller.

### Invariants And Boundaries

- Tests must distinguish chat turn state from task state and inbox acknowledgment.
- Unknown values are not silently treated as idle or working.
- Sessions with another leaf claim, terminal kind, landed status, or missing status do not invent activity.

### Todos

None.

### 2026-07-24 Curator Delta

The summary tests pin ready-without-turn as idle and starting-without-turn as unknown, preventing the
fresh-chat path from returning to a stale or alarmed label.

## Docs References

No relevant domain documentation was configured in the resolved `system/sources.md`.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No domain reference was available for this UI-local test contract. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Implementation under test. | L1-L141 | [ChatActivityIndicator.tsx](ChatActivityIndicator.tsx) |

## Cross-Repo References

No meaningful cross-repository reference exists.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No cross-repo reference. | — | — |

## Update History

- 2026-07-24T13:17:50Z — Added fresh-chat activity-summary coverage. Verification hash/date remain
  pinned to the pre-commit source stamp.

- 2026-07-12T17:50 — 260712-TRH-L6: created onboarding for the new focused activity regressions and their exact identity/precedence/omission contract. Candidate source remains uncommitted; metadata is pinned to the current code HEAD until closeout.
