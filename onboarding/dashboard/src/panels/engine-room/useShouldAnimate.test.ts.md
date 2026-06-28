# dashboard/src/panels/engine-room/useShouldAnimate.test.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/engine-room/useShouldAnimate.test.ts` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-06-16T01:55                                 |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`       |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[engine-room overview](overview.md)

## Purpose

Vitest suite pinning the `shouldAnimate()` honest-motion gate for slice 5f S0. It locks the truth table that keeps motion deterministic: either the `data-effects=off` determinism flag OR the OS `prefers-reduced-motion` suppresses animation, and only their joint absence allows it.

## Code Commentary

### Logic

No exports; one `describe("shouldAnimate")` block over three cases, with a `setReduce(matches)` helper that stubs `window.matchMedia` (jsdom ships no real implementation) and an `afterEach` that clears the `data-effects` attribute between cases.

- "is false when data-effects=off, even if the OS allows motion" — `data-effects=off`, reduce=false → `false`.
- "is false when prefers-reduced-motion is set, even if effects are on" — reduce=true, `data-effects=on` → `false`.
- "is true only when effects are on and reduced-motion is off" — reduce=false, `data-effects=on` → `true`.

### Invariants And Boundaries

- Pure-unit only: no React render, no timers; it exercises the imperative `shouldAnimate()` against stubbed DOM globals.
- `setReduce` fully replaces `window.matchMedia` with a minimal `MediaQueryList` stub so the result is deterministic regardless of jsdom; `afterEach` removes `data-effects` so cases don't leak into each other.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| `shouldAnimate` under test | L3 | [useShouldAnimate.ts](useShouldAnimate.ts) |
| `setReduce` matchMedia stub | L5-L16 | [useShouldAnimate.test.ts](useShouldAnimate.test.ts) |
| The three gate cases (data-effects / reduce / both-off) | L18-L36 | [useShouldAnimate.test.ts](useShouldAnimate.test.ts) |

## Update History

- 2026-06-16T01:55 — Created for slice 5f S0: vitest pinning the `shouldAnimate()` gate truth table (data-effects / reduced-motion). Verification metadata pinned until closeout stamps the S0 code commit.
