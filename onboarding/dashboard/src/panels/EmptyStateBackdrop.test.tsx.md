# dashboard/src/panels/EmptyStateBackdrop.test.tsx

## Governing Overview

[panels/ overview](overview.md)

## Purpose

Vitest + `@testing-library/react` render test pinning the shared empty-state backdrop's two contracts
(slice 07b polish): the empty-state **message always shows**, and the faint boomerang `<video>` is an
**effects-gated** atmosphere — present as a direct child of `empty-backdrop` with the given `src` + `loop` +
`aria-hidden` when effects are on, absent entirely under calm-cockpit / reduced-motion while the
message still renders. It guards the "pure atmosphere"
posture by construction.

## Code Commentary

### Logic

Four cases over `render(<EmptyStateBackdrop src=... >…</EmptyStateBackdrop>)`:

- children always render — the message text is found regardless of the backdrop;
- effects on (default jsdom: no `data-effects`, no reduced-motion) — the `empty-backdrop` testid mounts,
  its direct child `<video>` carries the exact `src` passed in, a `loop` attribute, and the
  autoplay-load-bearing trio: `muted` (asserted via the DOM **property** `video.muted`, since React 19
  reflects `muted` as a property only, never an attribute), plus the `autoplay` + `playsinline`
  attributes; the backdrop is `aria-hidden="true"` and no `empty-backdrop-zoom` wrapper exists;
- calm cockpit — setting `document.documentElement.dataset.effects = "off"` makes the backdrop testid
  query return null while `getByText` still finds the message;
- reduced motion alone — stubbing `window.matchMedia` to report `matches: true` for the reduce query
  while leaving `data-effects=on` also drops the backdrop (the gate is OR'd), the message still rendering.

`afterEach` runs RTL `cleanup`, clears the `data-effects` attribute, **and** restores the original
`window.matchMedia` so neither the calm-cockpit case nor the reduced-motion stub leaks into the next test
(both are document-/window-level shared mutable state).

### Invariants And Boundaries

Pure render assertion over the component in isolation (no store, no backend), relying on the shared
`test/setup.ts` jsdom stubs. It asserts **both** disjuncts of the effects gate at the component level
via DOM presence/absence — the real `useShouldAnimate` runs (the default jsdom environment reports
effects-on; `data-effects=off` flips the first branch and a `matchMedia` reduce stub flips the second)
— so the test exercises the gate, it does not mock it. The direct-child assertion plus explicit
`empty-backdrop-zoom` absence pins that runtime zoom stays out of the component; the `loop` + `muted` +
`aria-hidden` assertions pin the seamless-boomerang + muted-autoplay + atmosphere-not-state contracts.

### 2026-07-24 Curator Delta

The test supplies a controllable IntersectionObserver and asserts that hiding a kept-mounted backdrop
pauses its video while a re-show resumes playback.

## Evidence

### Repo-Internal References

- The component under test (effects-gated empty-state backdrop with direct static video; media motion is baked into the MP4 asset). [1]
- The honest-motion gate whose two branches the test exercises via `data-effects`. [2]

### Cross-Repo References

No meaningful cross-repo references found. This is a self-contained dashboard render test.
