# dashboard/src/panels/engine-room/useShouldAnimate.test.ts

## Governing Overview

[engine-room overview](overview.md)

## Purpose

Vitest suite pinning the `shouldAnimate()` honest-motion gate for slice 5f S0. It locks the truth table that keeps motion deterministic: either the `data-effects=off` determinism flag OR the OS `prefers-reduced-motion` suppresses animation, and only their joint absence allows it.

## Code Commentary

### Logic

No exports; one `describe("shouldAnimate")` block over three cases, with a `setReduce(matches)` helper that stubs `window.matchMedia` (jsdom ships no real implementation) and an `afterEach` that clears the `data-effects` attribute between cases.

- "is false when data-effects=off" — `data-effects=off`, reduce=false → `false`.
- "is false when prefers-reduced-motion is set" — reduce=true, `data-effects=on` → `false`.
- "is true only when effects are on and reduced-motion is off" — reduce=false, `data-effects=on` → `true`.

### Invariants And Boundaries

- Pure-unit only: no React render, no timers; it exercises the imperative `shouldAnimate()` against stubbed DOM globals.
- `setReduce` fully replaces `window.matchMedia` with a minimal `MediaQueryList` stub so the result is deterministic regardless of jsdom; `afterEach` removes `data-effects` so cases don't leak into each other.

## Evidence

### Repo-Internal References

- `shouldAnimate` under test [1]
- `setReduce` matchMedia stub [2]
- The three gate cases (data-effects / reduce / both-off) [3]
