# dashboard/src/data/pairChange.ts

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

## Evidence

### Docs References

No Domain Documentation source is configured; the behavior is proven by repository code and tests.

No external domain citation applies.

### Repo-Internal References

- Pure state, step/result/readback transitions, route provenance, and copy. [1]
- Exhaustive acceptance, guard, readback, route, and copy tables. [2]
- I/O driver consuming directives. [3]

### Cross-Repo References

No meaningful cross-repo boundary is owned here.

No cross-repo evidence applies.
