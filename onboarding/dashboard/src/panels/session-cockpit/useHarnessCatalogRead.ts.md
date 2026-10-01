# dashboard/src/panels/session-cockpit/useHarnessCatalogRead.ts

## Governing Overview

[session-cockpit overview](overview.md)

## 260731-EFA-L8 Change

The react-hooks remediation added a `servingBootedAtRef` initialization-only ref so
`exhaustive-deps` passes without duplicate catalog reads; behavior is unchanged.

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

## Evidence

### Repo-Internal References

- Supplies the typed one-attempt read and result states. [1]
- Consumes the hook and renders retryable explicit states. [2]
