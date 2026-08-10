# dashboard/src/panels/engine-room/useShouldAnimate.test.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/engine-room/useShouldAnimate.test.ts` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-06-16T01:55                                 |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb`       |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
| governingOverview      | `overview.md`                                    |

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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| `shouldAnimate` under test | `shouldAnimate` | dashboard/src/panels/engine-room/useShouldAnimate.ts:12-16 |
| `setReduce` matchMedia stub | `setReduce` | dashboard/src/panels/engine-room/useShouldAnimate.test.ts:5-16 |
| The three gate cases (data-effects / reduce / both-off) | "is false when data-effects=off"; "is true only when effects are on and reduced-motion is off" | dashboard/src/panels/engine-room/useShouldAnimate.test.ts:23-27; dashboard/src/panels/engine-room/useShouldAnimate.test.ts:35-39 |

## Update History

- 2026-08-02T16:55+02:00 — 260731-EFA-L6 W1-B08 curator: repaired 1 repo-internal citation row and preserved verification metadata.

- 2026-06-16T01:55 — Created for slice 5f S0: vitest pinning the `shouldAnimate()` gate truth table (data-effects / reduced-motion). Verification metadata pinned until closeout stamps the S0 code commit.
