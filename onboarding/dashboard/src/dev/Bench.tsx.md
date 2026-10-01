# dashboard/src/dev/Bench.tsx

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

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

- The `happy-build`→`build-up` legacy-deep-link alias (05k). [1]
- The grouped scenario picker is a compact selector. [2]
- The selected scenario mounts the real cockpit shell. [3]
- The scenario model validates named engine-room scenarios before building frames. [4]
- The real cockpit shell it renders (also the shell rendered against fixtures). [5]
- The gallery fixtures hydrated by the legacy `?state=` path. [6]
- The dev terminal mock provided via context (slice 6e-1). [7]
- Picker styles. [8]
- Player active-control styles. [9]

### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.

## FEUI-L8 Reviewed Candidate Delta

The bench now registers dedicated Chats scenarios through an authority harness and applies an exit boundary when returning to ordinary gallery scenarios. Cockpit scenarios enter Chats directly; other scenarios keep Operations.

The reviewed candidate is still uncommitted. Existing verification hash/date remain pinned to the
leaf base; closeout owns commit stamping.
