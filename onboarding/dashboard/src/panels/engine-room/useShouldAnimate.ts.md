# dashboard/src/panels/engine-room/useShouldAnimate.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/engine-room/useShouldAnimate.ts` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-02T01:42+02:00                           |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060`       |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[engine-room overview](overview.md)

## Purpose

The honest-motion gate for slice 5f's Engine Room animation. JS-driven GSAP/Motion are NOT frozen by the CSS `html[data-effects="off"]` switch (which only freezes CSS keyframes), so every JS animation must consult this gate and render the transition's "After" state instantly when motion is suppressed. It generalizes the inline check the topology canvas already uses (`topology/constel.ts`) into one reusable hook the Engine Room shares. Created as scaffolding in slice 5f S0; the motion slices (S2+) consume it.

## Code Commentary

### Logic

Two exports.

- `shouldAnimate()` — imperative boolean for GSAP timelines / one-off tweens. Returns `false` (skip the tween, jump to the After state) when running outside a DOM, when `document.documentElement.dataset.effects === "off"` (the `?effects=off` / `calm-cockpit` determinism flag set in `main.tsx`), or when `window.matchMedia("(prefers-reduced-motion: reduce)").matches`; otherwise `true`.
- `useShouldAnimate()` — reactive hook wrapping `shouldAnimate()` in state. An effect subscribes to the reduced-motion media query (`change`) and a `MutationObserver` watching `<html>`'s `data-effects` attribute, re-evaluating on either, and disconnects both on unmount. A component using it re-renders the moment the OS setting or the determinism flag flips.

### Invariants And Boundaries

- Reads BOTH gates — the OS `prefers-reduced-motion` AND the app determinism flag (`data-effects`); either being active suppresses motion. This is the rule that keeps Playwright snapshots deterministic under `?effects=off` even though Motion's own `reducedMotion="user"` (main.tsx) only covers the OS setting.
- SSR/test-safe: guards `typeof document/window === "undefined"` and returns `false` (no motion) in that case.
- A pure read of global DOM state; it owns no animation — callers decide what "don't animate" means (render After, no tween).

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| `shouldAnimate()` reads data-effects + prefers-reduced-motion | `shouldAnimate` | dashboard/src/panels/engine-room/useShouldAnimate.ts:12-16 |
| `useShouldAnimate()` reactive hook (media query + MutationObserver) | `useShouldAnimate` | dashboard/src/panels/engine-room/useShouldAnimate.ts:19-37 |
| The main entry checks `?effects=off` or `calm-cockpit` and sets `document.documentElement.dataset.effects` to `off`. | "effects=off"; "window.localStorage.getItem(\"calm-cockpit\")"; "document.documentElement.dataset.effects = \"off\"" | dashboard/src/main.tsx:12-12; dashboard/src/main.tsx:15-16 |
| The prior inline freeze check this generalizes | `mountConstel` | dashboard/src/topology/constel.ts:59-372 |

## Update History

- 2026-08-04T13:54+02:00 — 260731-EFA-L6 S18-B13 curator: reissued whole-claim evidence for the effects-off query, storage toggle, and HTML dataset assignment for same-reviewer closure.
- 2026-08-02T01:42+02:00 — No content impact: re-derived line range(s) that ended past the end of the file the row names (`memory_quality/style/citations`, `citation_range_out_of_bounds`). Each range was rewritten by reading the cited construct at its current location; no claim was changed to fit a range, and no range was interpolated. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-06-16T01:55 — Created for slice 5f S0: the `shouldAnimate()` / `useShouldAnimate()` honest-motion gate (reads data-effects + prefers-reduced-motion), scaffolding for the S2+ motion slices. Verification metadata pinned until closeout stamps the S0 code commit.
