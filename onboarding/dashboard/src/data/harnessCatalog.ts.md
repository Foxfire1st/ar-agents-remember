# dashboard/src/data/harnessCatalog.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/harnessCatalog.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-18T12:43+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`|
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[data overview](overview.md)

## Purpose

This module defines and validates the narrow pre-session harness catalog read used by the launch
flow. It keeps transport, envelope, and row-shape failures distinct from a valid empty catalog.

## Code Commentary

### Logic

`readHarnessCatalog` performs one abortable `GET /api/harnesses`. It reports network, HTTP, and
protocol failures as typed error results, validates the `{harnesses: [...]}` envelope and every row,
and returns either `empty` or `ready`. A valid row contains only `id`, `name`, and `detected`; this
pre-session discovery contract deliberately does not project session/process control state.

### Conventions

The result is a discriminated union. Validation helpers stay private, and the caller supplies the
base URL and abort signal so transport lifetime remains outside the reader.

### Invariants And Boundaries

- The caller owns the `AbortSignal`, timeout policy, and retries.
- Invalid JSON, an invalid envelope, or any invalid row is a protocol error, never an empty catalog.
- Detection is server evidence; this reader does not invent readiness or control capability.

### Todos

No task-independent technical debt was identified during FEUI-L9R review.

### 2026-07-24 Curator Delta

Signal-less boot reads now share a 10-second-bounded catalog request. Caller-supplied abort signals
remain private requests so one launch dialog cannot cancel another caller; a timed-out shared request
returns the existing network-error classification and releases the key.

## Docs References

No relevant documentation was found after checking the configured sources; current claims are
proven by repository source and tests.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external or domain documentation is configured for this repository-local reader. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Owns timeout, retry, and stale-request cancellation around this pure read. | `useHarnessCatalogRead` | dashboard/src/panels/session-cockpit/useHarnessCatalogRead.ts:22-84 |
| Renders the explicit catalog states in the chooser. | `LaunchFlow` | dashboard/src/panels/session-cockpit/LaunchFlow.tsx:353-413 |
| The serving endpoint returns exactly the narrow row shape. | `api_harnesses` | mcp/src/agents_remember/serving/_app_terminal_routes.py:157-159 |

## Cross-Repo References

No meaningful cross-repository implementation source governs this repository-local HTTP reader.

| Finding | Anchor | Source |
| --- | --- | --- |
| The reviewed behavior is wholly repository-local. | — | — |

## Update History

- 2026-08-02T16:44:57+02:00 — L6 W1-B02 curator: repaired 3 repository-internal citations for the hook, chooser, and serving endpoint; no content claims changed.
- 2026-07-24T13:17:50Z — Documented bounded, signal-aware harness-catalog single-flight behavior.
  Verification hash/date remain pinned to the pre-commit source stamp.

- 2026-07-18T12:43+02:00 — FEUI-L9R: created the one-to-one card for the candidate harness-catalog
  reader; verification metadata stays blank until the code candidate is committed and closeout can
  stamp it.
