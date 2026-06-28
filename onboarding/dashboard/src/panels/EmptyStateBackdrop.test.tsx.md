# dashboard/src/panels/EmptyStateBackdrop.test.tsx

| Field                  | Value                                              |
| ---------------------- | -------------------------------------------------- |
| repository             | agents-remember                                    |
| path                   | `dashboard/src/panels/EmptyStateBackdrop.test.tsx` |
| doc_type               | `file-level-onboarding`                            |
| lastUpdated            | 2026-06-24T13:04+02:00                             |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`                                          |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `overview.md`                                      |

## Governing Overview

[panels/ overview](overview.md)

## Purpose

Vitest + `@testing-library/react` render test pinning the shared empty-state backdrop's two contracts
(slice 07b polish): the empty-state **message always shows**, and the faint boomerang `<video>` is an
**effects-gated** atmosphere — present as a direct child of `empty-backdrop` with the given `src` + `loop`
+ `aria-hidden` when effects are on, absent entirely under calm-cockpit / reduced-motion while the
message still renders. It guards the "pure atmosphere, never state / never lost in the calm cockpit"
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

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The component under test (effects-gated empty-state backdrop with direct static video; media motion is baked into the MP4 asset). | L51-L59 | [EmptyStateBackdrop.tsx](EmptyStateBackdrop.tsx) |
| The honest-motion gate whose two branches the test exercises via `data-effects`. | L12-L37 | [engine-room/useShouldAnimate.ts](engine-room/useShouldAnimate.ts) |

## Cross-Repo References

No meaningful cross-repo references found. This is a self-contained dashboard render test.

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->

- 2026-06-24T13:04+02:00 — Updated the effects-on case after the runtime zoom wrapper was removed. The
  test now asserts the video is a direct child of `empty-backdrop` and that `empty-backdrop-zoom` is absent,
  while keeping the muted/autoplay/loop/playsInline/aria-hidden contracts. Verification metadata remains
  pinned until closeout stamps the code commit.
- 2026-06-24T12:28+02:00 — Refreshed the component citation after the compositor-hint patch shifted
  `EmptyStateBackdrop.tsx` line ranges. The test source itself did not change in this patch; it still
  pins the backdrop/wrapper/video structure introduced earlier in this leaf. Verification metadata
  remains pinned until closeout stamps the code commit.
- 2026-06-24T11:47+02:00 — Refreshed the component reference after the zoom implementation changed from
  a free-running Motion repeat to a media-clock `MotionValue` on the same `empty-backdrop-zoom` wrapper.
  The test source itself still pins the structural contract: hidden backdrop contains the zoom wrapper,
  and the static video lives inside that wrapper. Verification metadata remains pinned until closeout
  stamps the code commit.
- 2026-06-24T11:24+02:00 — Updated the effects-on case to assert the new zoom-layer structure: the
  `empty-backdrop` atmosphere contains `empty-backdrop-zoom`, and the static video lives inside that
  wrapper. The same muted/autoplay/loop/playsInline/aria-hidden contracts remain pinned. Verification
  metadata remains pinned until closeout stamps the code commit.
- 2026-06-23T04:35+02:00 — Created for slice 07b polish: render test pinning `EmptyStateBackdrop` over
  four cases — children always show; effects-on mounts the looping, muted (via the `video.muted`
  property), autoplaying, `aria-hidden` `<video>` with the given `src`; `data-effects=off` and a
  reduced-motion `matchMedia` stub each independently drop the backdrop while the message still renders
  (with an `afterEach` that clears `data-effects` and restores `window.matchMedia`). Verification
  metadata pinned until closeout stamps the slice-07b code commit.
