# dashboard/src/data/setAcceptance.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/setAcceptance.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-18T07:22+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview | `overview.md` |

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

## Docs References

No Domain Documentation source is configured.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain citation applies. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Route classification, reducer, readback promotion, and refetch predicate. | `classifySetResponse`, `reduceSetResult`, `resolvePendingsByReadback`, `shouldRefetchOnTurnEnded` | dashboard/src/data/setAcceptance.ts:55-70; dashboard/src/data/setAcceptance.ts:101-153; dashboard/src/data/setAcceptance.ts:204-232; dashboard/src/data/setAcceptance.ts:240-250 |
| Exhaustive acceptance, HTTP, clamp, and readback tables. | "reduceSetResult — the exhaustive acceptance × kind × clamp table" | dashboard/src/data/setAcceptance.test.ts:39-128 |
| Store snapshots and pending phases consumed by the reducer. | `PerSessionCockpit`, `PendingSet` | dashboard/src/data/sessionCockpitStore.ts:20-24; dashboard/src/data/sessionCockpitStore.ts:113-153 |
| Set acceptance vocabulary mirrored by the frontend. | `SetAcceptance`, `SetResultWire` | dashboard/src/types/harnessCapabilities.ts:86-86; dashboard/src/types/harnessCapabilities.ts:89-96 |

## Cross-Repo References

No meaningful cross-repo boundary is owned here; normalized server values are mirrored in
same-repo wire types.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo evidence applies. | — | — |

## Update History

- 2026-08-02T20:47+02:00 — 260731-EFA-L6 W2-B01 curator: anchored 4 citation rows; scoped citation fixing regenerated the source ranges.

- 2026-07-18T07:22+02:00 — FEUI-L8 manual route refactor: retargeted this direct data file card
  from the packed dashboard/src parent to the new nearest data authority overview. Source behavior
  is unchanged by this memory-only governance move; verification hash/date remain pinned.

- 2026-07-17T08:33+02:00 — Created for 260715-FEUI-L4 R2/R3/R4/R9 after final reviewer PASS.
  Verification metadata is pinned to the uncommitted leaf's contract base pending closeout.
