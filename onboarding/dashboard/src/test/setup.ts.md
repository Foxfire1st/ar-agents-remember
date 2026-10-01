# dashboard/src/test/setup.ts

## Governing Overview

[dashboard/src overview](../overview.md)

## 260731-EFA-L8 Change

The setup-level unhandled-error trap (R10) now records window
`error`/`unhandledrejection`, `process` unhandledRejection, and `console.error`
(React act/suspense dev warnings filtered) and fails the owning test via
`afterEach`. It proved itself by catching the live canvas exception (the review's
exact finding) and the CodeMirror vim cursor measurement exception; both are now
stubbed (inert canvas Proxy context, empty rect list).

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
- Defines an inert `Element.prototype.scrollIntoView` when absent (260715-FEUI-L1) — cmdk (the
  sessions command palette) calls it on the selected item; tests assert selection state, never
  scroll geometry.
- Assigns inert SVG geometry stubs (`getBBox`/`getTotalLength`/`getPointAtLength`) across the SVG prototype
  chain (`SVGElement`/`SVGGraphicsElement`/`SVGGeometryElement`) — GSAP's DrawSVG/MotionPath (the engine-room
  timeline, 05n) call these when the effects-on GSAP-gate test builds the context, and **jsdom omits them**
  (it does not stub-them-to-throw — see the pinned citation in the next bullet). Note that in jsdom 25.0.1
  `globalThis.SVGGeometryElement` is itself `undefined`, so the loop's `if (!proto) continue` skips that
  third entry entirely: only `SVGElement.prototype` and `SVGGraphicsElement.prototype` actually receive stubs.
- The `matchMedia`/`ResizeObserver` stubs are guarded (`typeof … === "undefined"`/`!== "function"`) so they
  only fill genuine gaps; per-test code may still replace them (e.g. `useShouldAnimate.test` swaps in its own
  `matchMedia`). The SVG geometry stubs are assigned **unconditionally**, and their return values are inert
  and never asserted. The reason this file once gave for that asymmetry — "jsdom's `getBBox` throws rather
  than being absent" — is **false**. Nothing throws: there is no method to throw. Pinned: **jsdom 25.0.1**
  (`dashboard/package.json` declares `"jsdom": "^25.0.1"`). In jsdom's own source, `getBBox`,
  `getTotalLength` and `getPointAtLength` appear **zero** times anywhere under `jsdom/lib/`;
  `lib/jsdom/living/nodes/SVGGraphicsElement-impl.js:7` is the entire implementation
  (`class SVGGraphicsElementImpl extends SVGElementImpl {}` — an empty body); and the interface registry at
  `lib/jsdom/living/interfaces.js:114-120` exposes `SVGElement`/`SVGGraphicsElement`/`SVGSVGElement`/
  `SVGTitleElement` with **no `SVGGeometryElement` entry**. Measured in a `new JSDOM(...)` window: all three
  methods are `typeof undefined` on `<svg>` and `<path>` instances *and* on `SVGElement.prototype` /
  `SVGGraphicsElement.prototype` (`"getBBox" in path` is `false`; no own property either);
  `window.SVGGeometryElement` and `window.SVGPathElement` are `undefined`; and `path.getBBox()` raises the
  ordinary `TypeError: path.getBBox is not a function` — the calling-undefined error, not a jsdom throw.
- **Risk carried by the unconditional assignment** (260731-EFA-L4): because the methods are *absent* rather
  than throwing, the unconditional assignment is pure gap-filling **today**. But if a future jsdom minor
  ships a real `getBBox`/`getTotalLength`/`getPointAtLength` (or starts defining `SVGGeometryElement`), this
  same unconditional assignment will **silently overwrite the real implementation** with the inert stub —
  tests would keep passing against fabricated geometry with no signal that anything changed. The guarded
  `typeof … === "undefined"` pattern used ~20 lines earlier for `matchMedia`/`ResizeObserver` would be immune
  to that. Switching `setup.ts` to the guarded pattern is test-infrastructure work outside 260731-EFA-L4's
  scope; it is recorded here so the next jsdom bump weighs it.

### Invariants And Boundaries

Test-only — loaded by vitest `setupFiles`, never part of the production bundle. The stubs are minimal and
idempotent; they must not impose real media-query / resize behaviour (tests that need specific values
override locally).

### 2026-07-24 Curator Delta

The jsdom setup now supplies inert media `play`/`pause` methods. Visibility-gating tests can assert their
calls without relying on browser playback that jsdom does not implement.

## Evidence

### Repo-Internal References

- `matchMedia` stub consumed by the honest-motion gate. [1]
- Wired as the vitest setup file. [2]
- The render test that depends on these stubs. [3]
