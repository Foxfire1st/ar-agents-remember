# dashboard/src/data/setAcceptance.ts

## Governing Overview

[data overview](overview.md)

## Purpose

Pure SetResult honesty table, set-route HTTP classifier, and snapshot-readback promotion rules.

## Code Commentary

### Logic

`classifySetResponse` keeps valid HTTP-200 `unknown`/`unsupported` results as evidence while
separating 404, 409, 503, malformed, and transport outcomes. `reduceSetResult` is exhaustive over
all five acceptances plus clamp/no-value edges. `resolvePendingsByReadback` confirms queued values
only when echoed and resolves unknown values either way after their one readback.

### Conventions

The effective marker moves only through returned `effectiveValue` or later snapshot truth;
requests and pending phases never stand in for effectiveness.

### Invariants And Boundaries

Clamp means echo-verified with differing non-null requested/effective values. Attention is limited
to unsupported, unknown, clamp, and defensive echo-without-value evidence.

### Todos

None recorded.

## Evidence

### Docs References

No Domain Documentation source is configured.

No external domain citation applies.

### Repo-Internal References

- Route classification, reducer, readback promotion, and refetch predicate. [1]
- Exhaustive acceptance, HTTP, clamp, and readback tables. [2]
- Store snapshots and pending phases consumed by the reducer. [3]
- Set acceptance vocabulary mirrored by the frontend. [4]

### Cross-Repo References

No meaningful cross-repo boundary is owned here; normalized server values are mirrored in
same-repo wire types.

No cross-repo evidence applies.
