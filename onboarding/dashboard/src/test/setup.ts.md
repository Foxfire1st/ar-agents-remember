# dashboard/src/test/setup.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/test/setup.ts`                    |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-06-16T02:30                                 |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`       |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

The shared vitest (jsdom) bootstrap, wired via `vitest.config.ts` `setupFiles`. It stubs the browser
APIs jsdom omits so component-render tests (React Aria widgets, the honest-motion gate) don't crash on
missing globals. Grown in slice 5f S1 from an empty placeholder to carry those stubs.

## Code Commentary

### Logic

- Defines a minimal `window.matchMedia` stub (returns `{ matches: false, ... }` with no-op listeners)
  when one is absent — `useShouldAnimate`/`shouldAnimate` call `matchMedia("(prefers-reduced-motion …)")`,
  which jsdom does not implement.
- Defines a no-op `ResizeObserver` class when absent — React Aria components reference it.
- Assigns inert SVG geometry stubs (`getBBox`/`getTotalLength`/`getPointAtLength`) across the SVG prototype
  chain (`SVGElement`/`SVGGraphicsElement`/`SVGGeometryElement`) — GSAP's DrawSVG/MotionPath (the engine-room
  timeline, 05n) call these when the effects-on GSAP-gate test builds the context, and jsdom omits or
  stubs-them-to-throw.
- The `matchMedia`/`ResizeObserver` stubs are guarded (`typeof … === "undefined"`/`!== "function"`) so they
  only fill genuine gaps; per-test code may still replace them (e.g. `useShouldAnimate.test` swaps in its own
  `matchMedia`). The SVG geometry stubs are assigned unconditionally (jsdom's `getBBox` throws rather than
  being absent), but their return values are inert and never asserted.

### Invariants And Boundaries

Test-only — loaded by vitest `setupFiles`, never part of the production bundle. The stubs are minimal and
idempotent; they must not impose real media-query / resize behaviour (tests that need specific values
override locally).

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| `matchMedia` stub consumed by the honest-motion gate. | — | [panels/engine-room/useShouldAnimate.ts](../panels/engine-room/useShouldAnimate.ts) |
| Wired as the vitest setup file. | — | [vitest.config.ts](../../vitest.config.ts) |
| The render test that depends on these stubs. | — | [cockpit/Cockpit.test.tsx](../cockpit/Cockpit.test.tsx) |

## Update History

- 2026-06-21T09:57+02:00 — slice 05n: added inert SVG geometry stubs
  (`getBBox`/`getTotalLength`/`getPointAtLength`) across `SVGElement`/`SVGGraphicsElement`/`SVGGeometryElement`
  so GSAP DrawSVG/MotionPath (the engine-room draw-on + packet) construct without throwing under the effects-on
  `EnclosureProcessMap` GSAP-gate test — jsdom omits/throws on these. Verification metadata pinned until
  closeout stamps the 05n commit.
- 2026-06-16T02:30 — Created for slice 5f S1: added the jsdom `matchMedia` + `ResizeObserver` stubs so
  component-render tests (the new `Cockpit.test.tsx`) run. Verification metadata pinned until closeout
  stamps the S1 code commit.
