# dashboard/src/dev/Bench.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/dev/Bench.tsx`                    |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-06-21T02:27+02:00                           |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`       |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

The DEV-only cockpit harness (`/dev/bench`, note 15) — the exact model-C `CockpitShell` mounted against
hand-authored state for the screenshot/annotate review loop and Playwright. It began as a static
**gallery** (a fixture hydrated once into the real store, switchable by `?state=`, no live stream) so the
review loop could capture every panel in every grammar state. Slice 5i turned it into a **scenario
player**: the same shell driven through phase-transition timelines through the REAL store, so the
integrated motion is verifiable end-to-end, not just static frames. Slice 6e-1 additionally wraps the tree
in a dev-only mock terminal socket so the Chats view's terminal renders live-looking with no backend.

## Code Commentary

### Logic

Reads the wanted scenario from `?scenario=` (or the legacy `?state=`, which now resolves to a folded-in
single-frame "resting" scenario). **Slice 05k** adds one legacy-name alias: a raw `?scenario=happy-build`
(or `?state=happy-build`) maps to the `build-up` timeline (`raw === "happy-build" ? "build-up" : raw`), so
the old deep link still resolves after the 5i rename. The resolved name seeds `useState` with the matching
`SCENARIOS` entry (or `SCENARIOS[0]`). A compact grouped `<select>` (replacing the old wrapped `bench__nav` button wall that
overlapped the cockpit header) lists the scenarios in three `<optgroup>`s — **Lifecycle** (`build-up`,
`tear-down`), **Failure modes** (the other multi-frame timelines), and **Resting states** (the
single-frame folded gallery) — derived by splitting `SCENARIOS` on `frames.length` and a `lifecycle` name
set. It renders the `<select>` picker (in `.bench-overlay .bench__picker`), the real `<CockpitShell />`,
and `<ScenarioPlayer key={scenario.name} scenario={scenario} />` (keyed so a scenario switch remounts the
player at frame 0). The player owns the actual store mutation (`applyFrame`); the bench only chooses the
scenario. (Before 5i this was a static gallery: it read `?state=` into `useState`, found the `GALLERY`
entry, and on change `applySnapshot(fixture.projection)`, cleared `events`, replayed `fixture.events`, and
`history.replaceState`d `?state=` so a state stayed shareable without a reload.)

**Slice 6e-1 (Task 6)** wraps the whole tree in a `TerminalSocketContext.Provider value={mockTerminalSocketFactory}`
so the **Chats view's terminal renders live-looking with no backend** (the mock echoes input + emits a
banner); production has no provider, so the real cockpit uses a same-origin WebSocket.

### Invariants And Boundaries

DEV-only — never the production cockpit; `/dev/*` is lazy-loaded and statically dropped from the production
bundle, so neither the bench nor the mock terminal socket ever ships. `?scenario=` deep links resolve only
in the initial state; later changes go through the picker. The bench renders the **real** `CockpitShell`
against the **real** store (no private copy / not a live client) so what's reviewed is the shipped cockpit.
`?effects=off` (read in `main.tsx`) freezes animation so Playwright assertions on the settled end-state
stay deterministic.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The `happy-build`→`build-up` legacy-deep-link alias (05k). | L13-L16 | [Bench.tsx](Bench.tsx) |
| Grouped `<select>` picker + mounts the player beneath the real shell. | L36-L60 | [Bench.tsx](Bench.tsx) |
| The scenario model + player it drives. | — | [scenarios.ts](scenarios.ts) · [ScenarioPlayer.tsx](ScenarioPlayer.tsx) |
| The real cockpit shell it renders (also the shell rendered against fixtures). | — | [Cockpit.tsx](../cockpit/Cockpit.tsx) |
| The gallery fixtures hydrated by the legacy `?state=` path. | — | [fixtures.ts](fixtures.ts) |
| The dev terminal mock provided via context (slice 6e-1). | — | [mockTerminalSocket.ts](mockTerminalSocket.ts) |
| Picker/player styles. | — | [dev.css](dev.css) |

## Update History

- 2026-06-21T02:27+02:00 — slice 05k: added the `happy-build`→`build-up` legacy-deep-link alias
  (`raw === "happy-build" ? "build-up" : raw`) so the old `?scenario=happy-build` link still resolves after
  the 5i timeline rename. Verification metadata pinned until closeout stamps the 05k code commit.
- 2026-06-19T23:58+02:00 — slice 5i: reworked from a static gallery (fixture hydrated once, `?state=` nav
  button wall) into a scenario player — a compact grouped `<select>` (Lifecycle / Failure modes / Resting
  states) + `<ScenarioPlayer>` driving the real shell through timelines; `?scenario=` (legacy `?state=`)
  deep link. Sidecar created this slice (the file was a pre-existing onboarding gap). Verification metadata
  pinned until closeout stamps the code commit.
- 2026-06-18T21:27 — Dev-bench review-ergonomics: replaced the full-width `bench__nav` link strip (it blocked the cockpit's top) with a compact `<select>` picker (`useState` + `history.replaceState` URL sync). Dev-only + transient (task 5's slice-5i scenario player will replace the strip). Verification metadata pinned until closeout stamps the code commit.
- 2026-06-18T16:50 — Task 6 slice 6e-1: wrapped the bench in a `TerminalSocketContext.Provider` (the dev mock socket) so the Chats view's terminal renders without a backend. Created this sidecar (the file was previously un-onboarded). Verification metadata pinned to the task base until closeout stamps the 6e-1 code commit.
