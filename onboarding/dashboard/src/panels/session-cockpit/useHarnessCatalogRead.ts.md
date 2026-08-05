# dashboard/src/panels/session-cockpit/useHarnessCatalogRead.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/useHarnessCatalogRead.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-18T12:43+02:00 |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060`|
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Supplies the typed one-attempt read and result states. | `HarnessCatalogRead`; `readHarnessCatalog` | dashboard/src/data/harnessCatalog.ts:13-16; dashboard/src/data/harnessCatalog.ts:45-51 |
| Consumes the hook and renders retryable explicit states. | `LaunchFlow` | dashboard/src/panels/session-cockpit/LaunchFlow.tsx:177-619 |

## Update History

- 2026-08-04T11:32:09+02:00 — 260731-EFA-L6 S18-B02 curator: replaced unanchored local references with exact source anchors and generated final citation ranges with the scoped fixer.

- 2026-07-18T12:43+02:00 — FEUI-L9R: created the one-to-one card for the candidate chooser read
  owner; verification metadata stays blank until the code candidate is committed and closeout can
  stamp it.
