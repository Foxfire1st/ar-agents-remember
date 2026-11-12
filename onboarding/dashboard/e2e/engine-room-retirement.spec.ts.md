# dashboard/e2e/engine-room-retirement.spec.ts

## Governing Overview

[Repository overview](../../overview.md)

There is no route-local overview for `dashboard/e2e/`, so the repository root overview is
the nearest governing ancestor, as for the sibling cards in this route.

## Purpose

The Playwright census of the retirement: it visits every dashboard entry a user can reach and
asserts that none of them is the retired engine view and that no page it reaches shows a state
of the two retired search providers.

## What The Spec Asserts

- Why it is a census rather than a mount: the header comment states that the engine view has no
  dashboard entry and no URL — it is retained in `Cockpit.tsx` for injected `initialView` tests
  only — so no spec can mount it, and a test that cannot pass stays out. The spec therefore
  censuses the reachable entries instead.
- Two shared assertions. `expectNoEngineEntry` requires zero buttons and zero links whose
  accessible name matches `/engine/i`. `expectNoProviderState` requires zero elements for the
  test ids `engine-gauge`, `official-wire`, `provider-block` and `engine-dropout`, and zero
  occurrences of the text `codegraphcontext-code`, `grepai-memory`, `CGC` and `GrepAI`
  (substring match, not exact).
- Eight test declarations: the cockpit root (navigates `/`, waits for the nav to be visible),
  the dev harness index (`/dev/`, waits for a bench link), three bench timelines, the calm
  resting state, and two dev pages (`/dev/reference`, `/dev/sprint-graph`).
- The timeline cases are `build-up` ("B5 · powered"), `memory-block` ("M3 · BLOCK") and
  `tear-down` ("D6 · stack removed"), each reached at
  `/dev/bench?scenario=<scenario>&effects=off`. The comment records why the degraded beat is
  the memory/ledger block: it is the surviving pre-contract failure mode, and the provider arcs
  — the seed fault, the reindex reroute and the provider-plan block — went with the providers,
  so a bench scenario that drove one no longer exists to link to. Timelines do not autoplay, so
  each case clicks the exact `▶` play button and settles on the end caption before asserting
  absence.
- The calm case loads `/dev/bench?state=calm&effects=off`, waits for the scenario element and
  asserts absence without playing. The dev-page cases only require a non-empty `body` before
  asserting absence.
- The header also records how the spec is meant to run — `cd dashboard && npx playwright test
  e2e/engine-room-retirement.spec.ts` under the Dagger suite — and the first-failure rail: every
  assertion fails fast with a snapshot, and selectors are fixed against the live render rather
  than retried blindly.

## Boundaries

This is source, not an execution record: nothing in it states that any case was collected, run
or passed, and this card makes no such claim.

What it asserts is absence, at the reaches it visits: no engine entry and no provider state on
those pages. It does not assert that the engine view is absent from the codebase, that the
`Cockpit.tsx` initial-view path is unreachable by every other route, or that a page outside the
visited list is clean. The provider text check is a substring match, so it would also catch
incidental prose, and the four test ids are the only provider-shaped ids it looks for.

The spec does not exercise provider behaviour — there is none to exercise — and it does not
assert the bench scenarios' visual content beyond waiting for one end caption per timeline.

## Evidence

- The header states the engine view has no entry and no URL, that no spec can mount it, and that the spec censuses reachable entries instead. [1]
- The assertion helpers: no `/engine/i` button or link, four engine/provider test ids at zero, four provider text tokens absent. [2]
- The cockpit-root and dev-harness-index cases. [3]
- The three timelines, with `memory-block` as the degraded beat and the note that the provider arcs went with the providers. [4]
- The timeline loop presses the exact play control and settles on the end caption before asserting absence. [5]
- The calm resting state and the two dev pages. [6]
