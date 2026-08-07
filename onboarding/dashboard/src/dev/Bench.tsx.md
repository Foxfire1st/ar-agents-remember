# dashboard/src/dev/Bench.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/dev/Bench.tsx`                    |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-18T07:22+02:00                           |
| lastVerifiedCommitHash | `7c56c11d651972515723b4090b8174087eb5236f`       |
| lastVerifiedCommitDate | 2026-08-07T20:50:27+02:00|
| governingOverview      | `../overview.md`                                |

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

## Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The `happy-build`→`build-up` legacy-deep-link alias (05k). | "?scenario=happy-build" | dashboard/src/dev/Bench.tsx:20-20 |
| The grouped scenario picker is a compact selector. | `htmlFor` | dashboard/src/dev/Bench.tsx:51-51 |
| The selected scenario mounts the real cockpit shell. | "chats" | dashboard/src/dev/Bench.tsx:41-41 |
| The scenario model validates named engine-room scenarios before building frames. | "scenario player: unknown engine-room scenario" | dashboard/src/dev/scenarios.ts:35-35 |
| The real cockpit shell it renders (also the shell rendered against fixtures). | `CockpitShell` | dashboard/src/cockpit/Cockpit.tsx:385-666; dashboard/src/cockpit/Cockpit.tsx:850-850 |
| The gallery fixtures hydrated by the legacy `?state=` path. | "calm" | dashboard/src/dev/fixtures.ts:148-148 |
| The dev terminal mock provided via context (slice 6e-1). | `mockTerminalSocketFactory` | dashboard/src/dev/mockTerminalSocket.ts:65-65 |
| Picker styles. | "bench-overlay" | dashboard/src/dev/dev.css:26-26 |
| Player active-control styles. | "player__controls button.is-on" | dashboard/src/dev/dev.css:120-120 |

## FEUI-L8 Reviewed Candidate Delta

The bench now registers dedicated Chats scenarios through an authority harness and applies an exit boundary when returning to ordinary gallery scenarios. Cockpit scenarios enter Chats directly; other scenarios keep Operations.

The reviewed candidate is still uncommitted. Existing verification hash/date remain pinned to the
leaf base; closeout owns commit stamping.

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History
- 2026-08-02T20:42:26+02:00 — W2-B07 curator: repaired 8 repository-reference citations (8/8 anchored and sourced; scoped citation check clean).

- 2026-07-18T07:22+02:00 — Curated the final same-reviewer-PASS FEUI-L8 behavior above using direct
  source/test/task evidence; no Domain Documentation source is configured.

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
