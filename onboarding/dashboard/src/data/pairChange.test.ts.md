# dashboard/src/data/pairChange.test.ts

## Governing Overview

[data overview](overview.md)

## Purpose

Exhaustive pure-machine regression suite for serialized pair changes.

## Code Commentary

### Logic

Tables cover every acceptance at both steps, confirmed and disproved unknown readbacks,
wrong-step/finished guards, model-route abort versus effort-route partial termination, two-step
progress copy, designed refusal copy, and the fix-round-3 unknown-effectiveness route copy.

### Conventions

The suite uses real shared SetResult fixtures and asserts both directives and resulting state.

### Invariants And Boundaries

Pure tests complement, but do not replace, `setClient.test.ts` production-path ordering and fetch
tests.

### Todos

None recorded.

## Evidence

### Docs References

No Domain Documentation source is configured.

No external domain citation applies.

### Repo-Internal References

- Pure machine under test. [1]
- Production driver tests that prove actual POST ordering and route siblings. [2]

### Cross-Repo References

No meaningful cross-repo references found.

No cross-repo evidence applies.
