# dashboard/src/data/fetchWithTimeout.ts

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

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory worktree's source registry.

No relevant external documentation is configured.

### Repo-Internal References

- The helper aborts and always clears its timer. [1]
- Shared boot reads use the helper before entering their single-flight maps. [2]

### Cross-Repo References

No meaningful cross-repository references found.

- The helper is local browser transport plumbing. [3]
