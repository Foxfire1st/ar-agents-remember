# dashboard/src/data/pairChange.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/pairChange.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-18T07:22+02:00 |
| lastVerifiedCommitHash | `7c56c11d651972515723b4090b8174087eb5236f` |
| lastVerifiedCommitDate | 2026-08-07T20:50:27+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[data overview](overview.md)

## Purpose

Pure serialized model-plus-effort state machine: model request, acceptance evidence or readback,
then effort request, with explicit completed, aborted, and partial outcomes.

## Code Commentary

### Logic

`applyPairStepResult` advances accepted model evidence, holds `unknown` for readback, aborts a
model `unsupported`, and records an effort `unsupported` as the designed partial outcome.
`applyPairRouteError` terminates the same control flow but preserves `routeErrorStep`, so missing
SetResult evidence renders as unknown effectiveness rather than fabricated refusal/success.

### Conventions

The machine performs no I/O or timers. `PairDirective` tells `setClient.ts` whether to send effort
and whether the pair is terminal.

### Invariants And Boundaries

Effort never sends before model acceptance evidence. Route failures and evidence-backed
`unsupported` results keep distinct copy provenance; Codex queued pairs may advance both requests
before a single later readback resolves their effective state.

### Todos

None recorded. The final reviewer PASS specifically confirmed the fix-round-3 route provenance.

## Docs References

No Domain Documentation source is configured; the behavior is proven by repository code and tests.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain citation applies. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Pure state, step/result/readback transitions, route provenance, and copy. | `startPairChange`; `applyPairStepResult`; `applyPairRouteError`; `applyPairReadback`; `pairProgressCopy`; `pairRouteTerminationCopy`; `pairPartialFailureCopy` | dashboard/src/data/pairChange.ts:50-52; dashboard/src/data/pairChange.ts:58-111; dashboard/src/data/pairChange.ts:119-150; dashboard/src/data/pairChange.ts:156-196; dashboard/src/data/pairChange.ts:199-203; dashboard/src/data/pairChange.ts:207-209; dashboard/src/data/pairChange.ts:216-219 |
| Exhaustive acceptance, guard, readback, route, and copy tables. | "step 1 (model) — every acceptance"; "step 2 (effort) — every acceptance"; "readback resolution of an unknown-held step"; "route failures end the pair story"; "machine guards"; "copy (R5 — one source, tests assert the words)" | dashboard/src/data/pairChange.test.ts:30-60; dashboard/src/data/pairChange.test.ts:62-101; dashboard/src/data/pairChange.test.ts:103-123; dashboard/src/data/pairChange.test.ts:125-153; dashboard/src/data/pairChange.test.ts:155-172; dashboard/src/data/pairChange.test.ts:174-199 |
| I/O driver consuming directives. | `commitPairDirective` | dashboard/src/data/setClient.ts:352-368 |

## Cross-Repo References

No meaningful cross-repo boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo evidence applies. | — | — |

## Update History

- 2026-08-02T21:08+02:00 — 260731-EFA-L6 W2-B09 curator: repaired 3 citation entries (6 findings); no Tier-3 findings.

- 2026-07-18T07:22+02:00 — FEUI-L8 manual route refactor: retargeted this direct data file card
  from the packed dashboard/src parent to the new nearest data authority overview. Source behavior
  is unchanged by this memory-only governance move; verification hash/date remain pinned.

- 2026-07-17T08:33+02:00 — Created for 260715-FEUI-L4 R5/R9 through fix round 3; the final PASS
  confirmed route-error outcomes remain unknown-effectiveness while SetResult-backed unsupported
  keeps its existing abort/partial copy. Base metadata is a pre-code-commit placeholder.
