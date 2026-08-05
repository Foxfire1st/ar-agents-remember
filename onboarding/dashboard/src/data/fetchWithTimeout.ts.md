# dashboard/src/data/fetchWithTimeout.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/fetchWithTimeout.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-24T13:17:50Z |
| lastVerifiedCommitHash |  `842b487b854503d95c9c2d9dce1841198ba93c7d`|
| lastVerifiedCommitDate |  2026-07-24T17:08:25+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[data overview](overview.md)

## Purpose

Abort the actual browser fetch socket after a caller-selected deadline, turning a hung transport into the
caller's ordinary rejection path.

## Code Commentary

### Logic

The helper creates one AbortController, schedules its abort with `window.setTimeout`, forwards the signal
to fetch, and clears the timer in `finally` on every settle path.

### Conventions

It deliberately uses timer-visible controller cancellation rather than `AbortSignal.timeout`, so fake-timer
tests can advance the real transport bound.

### Invariants And Boundaries

This helper does not classify errors or retry. Callers own their specific `null`, typed-error, or throw
semantics; the bound must abort the socket, not merely stop awaiting its promise.

### Todos

None.

## Docs References

No Domain Documentation entries are configured in this memory worktree's source registry.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation is configured. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The helper aborts and always clears its timer. | "export async function fetchWithTimeout" | dashboard/src/data/fetchWithTimeout.ts:15-15 |
| Shared boot reads use the helper before entering their single-flight maps. | "export function shareInflight" | dashboard/src/data/inflight.ts:21-21 |

## Cross-Repo References

No meaningful cross-repository references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| The helper is local browser transport plumbing. | "export async function fetchWithTimeout" | dashboard/src/data/fetchWithTimeout.ts:15-15 |

## Update History

- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B24 curator: replaced the `n/a` rows with exact
  anchors and fixer-generated ranges; exact non-fixing check returns zero findings.

- 2026-07-24T13:17:50Z — Created for aborting hung browser fetches. Verification hash/date remain
  pinned to the pre-commit source stamp.
