# dashboard/src/data/harnessCatalog.ts

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

## Evidence

### Docs References

No relevant documentation was found after checking the configured sources; current claims are
proven by repository source and tests.

No relevant external or domain documentation is configured for this repository-local reader.

### Repo-Internal References

- Owns timeout, retry, and stale-request cancellation around this pure read. [1]
- Renders the explicit catalog states in the chooser. [2]
- The serving endpoint returns exactly the narrow row shape. [3]

### Cross-Repo References

No meaningful cross-repository implementation source governs this repository-local HTTP reader.

The reviewed behavior is wholly repository-local.
