# dashboard/src/data/pairChange.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/pairChange.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-17T08:33+02:00 |
| lastVerifiedCommitHash | `4293c53b9d6ef2bf0fee7aca11c2677322c4e786` |
| lastVerifiedCommitDate | 2026-07-17T10:26:02+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[dashboard/src overview](../overview.md)

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

| Finding | Citations | Source Path |
| --- | --- | --- |
| No external domain citation applies. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Pure state, step/result/readback transitions, route provenance, and copy. | L1-L219 | [pairChange.ts](pairChange.ts) |
| Exhaustive acceptance, guard, readback, route, and copy tables. | L30-L199 | [pairChange.test.ts](pairChange.test.ts) |
| I/O driver consuming directives. | L1-L433 | [setClient.ts](setClient.ts) |

## Cross-Repo References

No meaningful cross-repo boundary is owned here.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No cross-repo evidence applies. | — | — |

## Update History

- 2026-07-17T08:33+02:00 — Created for 260715-FEUI-L4 R5/R9 through fix round 3; the final PASS
  confirmed route-error outcomes remain unknown-effectiveness while SetResult-backed unsupported
  keeps its existing abort/partial copy. Base metadata is a pre-code-commit placeholder.
