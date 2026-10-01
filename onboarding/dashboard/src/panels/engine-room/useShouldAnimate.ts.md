# dashboard/src/panels/engine-room/useShouldAnimate.ts

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

## Evidence

### Repo-Internal References

- `shouldAnimate()` reads data-effects + prefers-reduced-motion [1]
- `useShouldAnimate()` reactive hook (media query + MutationObserver) [2]
- The main entry checks `?effects=off` or `calm-cockpit` and sets `document.documentElement.dataset.effects` to `off`. [3]
- The prior inline freeze check this generalizes [4]
