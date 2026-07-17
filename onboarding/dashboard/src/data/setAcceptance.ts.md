# dashboard/src/data/setAcceptance.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/setAcceptance.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-17T08:33+02:00 |
| lastVerifiedCommitHash | `4293c53b9d6ef2bf0fee7aca11c2677322c4e786` |
| lastVerifiedCommitDate | 2026-07-17T10:26:02+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[dashboard/src overview](../overview.md)

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

## Docs References

No Domain Documentation source is configured.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No external domain citation applies. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Route classification, reducer, readback promotion, and refetch predicate. | L1-L250 | [setAcceptance.ts](setAcceptance.ts) |
| Exhaustive acceptance, HTTP, clamp, and readback tables. | L39-L264 | [setAcceptance.test.ts](setAcceptance.test.ts) |
| Store snapshots and pending phases consumed by the reducer. | L1-L425 | [sessionCockpitStore.ts](sessionCockpitStore.ts) |
| Set acceptance vocabulary mirrored by the frontend. | L1-L117 | [../types/harnessCapabilities.ts](../types/harnessCapabilities.ts) |

## Cross-Repo References

No meaningful cross-repo boundary is owned here; normalized server values are mirrored in
same-repo wire types.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No cross-repo evidence applies. | — | — |

## Update History

- 2026-07-17T08:33+02:00 — Created for 260715-FEUI-L4 R2/R3/R4/R9 after final reviewer PASS.
  Verification metadata is pinned to the uncommitted leaf's contract base pending closeout.
