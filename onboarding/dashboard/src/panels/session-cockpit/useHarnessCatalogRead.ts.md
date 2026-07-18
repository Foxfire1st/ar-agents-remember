# dashboard/src/panels/session-cockpit/useHarnessCatalogRead.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/useHarnessCatalogRead.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-18T12:43+02:00 |
| lastVerifiedCommitHash | `82f2de40a666ea00754f364cfe764cea9294235f`|
| lastVerifiedCommitDate | 2026-07-18T13:07:00+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[session-cockpit overview](overview.md)

## Purpose

This hook owns the launch chooser's lifecycle-aware harness-catalog read: one request per chooser
boot, explicit timeout, user-driven retry, and cancellation when the chooser closes or a newer read
supersedes the old one.

## Code Commentary

### Logic

An open chooser starts in `loading` and delegates one HTTP attempt to `readHarnessCatalog`. A
five-second timer aborts that attempt and produces a distinct `timeout` state. `retry` aborts the
active request before starting a new one; sequence identity prevents late results from an older
request from overwriting the current state. Closing the chooser aborts active work and returns to
`idle`. The boot identity effect deliberately replaces exactly one read when a new chooser boot is
opened.

### Conventions

Active work is represented by one controller/timeout/sequence identity object. The hook returns
state plus an explicit `retry` callback and accepts timeout as a test seam rather than global policy.

### Invariants And Boundaries

- There is no background retry loop or hidden fallback catalog.
- Timeout, transport/HTTP/protocol failure, valid empty, and ready are separately renderable facts.
- Aborted or stale requests cannot publish over a newer chooser boot.

### Todos

No task-independent technical debt was identified during FEUI-L9R review.

## Docs References

No relevant documentation was found after checking the configured sources; current claims are
proven by repository source and direct tests.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external or domain documentation is configured for this repository-local hook. | Source discovery checked | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Supplies the typed one-attempt read and result states. | L1-L74 | [data/harnessCatalog.ts](../../data/harnessCatalog.ts) |
| Consumes the hook and renders retryable explicit states. | L199-L204 | [LaunchFlow.tsx](LaunchFlow.tsx) |
| Pins cancellation, timeout, retry, and recovery behavior. | L200-L361 | [LaunchFlow.test.tsx](LaunchFlow.test.tsx) |

## Cross-Repo References

No meaningful cross-repository implementation source governs this repository-local React hook.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The reviewed behavior is wholly repository-local. | Import and task-boundary review | — |

## Update History

- 2026-07-18T12:43+02:00 — FEUI-L9R: created the one-to-one card for the candidate chooser read
  owner; verification metadata stays blank until the code candidate is committed and closeout can
  stamp it.
