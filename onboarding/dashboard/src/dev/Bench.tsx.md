# dashboard/src/dev/Bench.tsx

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

The DEV-only cockpit harness (`/dev/bench`, note 15) — the exact model-C `CockpitShell` mounted against
hand-authored state for the screenshot/annotate review loop and Playwright. It began as a static
**gallery** (a fixture hydrated once into the real store, switchable by `?state=`, no live stream) so the
review loop could capture every panel in every grammar state. Slice 5i turned it into a **scenario
player**: the same shell driven through phase-transition timelines through the REAL store, so the
integrated motion is inspectable across scenario frames, not just static frames. The current Bench
mounts `CockpitShell initialView="operations"` directly beside the keyed `ScenarioPlayer`.

## Code Commentary

### Logic

Reads the wanted name from `?scenario=` or the legacy `?state=` spelling; both select from the same
`SCENARIOS` population, including timelines and folded-in single-frame resting scenarios. **Slice 05k** adds one legacy-name alias: a raw `?scenario=happy-build`
(or `?state=happy-build`) maps to the `build-up` timeline (`raw === "happy-build" ? "build-up" : raw`), so
the old deep link still resolves after the 5i rename. The resolved name seeds `useState` with the matching
`SCENARIOS` entry (or the first entry, `SCENARIOS[0]`). A compact grouped `<select>` (replacing the old wrapped `bench__nav` button wall that
overlapped the cockpit header) lists the scenarios in three `<optgroup>`s — **Lifecycle** (`build-up`,
`tear-down`), **Failure modes** (the other multi-frame timelines), and **Resting states** (the
single-frame folded gallery) — derived by splitting `SCENARIOS` on `frames.length` and a `lifecycle` name
set. It renders the `<select>` picker (in `.bench-overlay .bench__picker`), the real `<CockpitShell initialView="operations" />`,
and `<ScenarioPlayer key={scenario.name} scenario={scenario} />` (keyed so a scenario switch remounts the
player at frame 0). The player owns the actual store mutation (`applyFrame`); the bench only chooses the
scenario. (Before 5i this was a static gallery: it read `?state=` into `useState`, found the `GALLERY`
entry, and on change `applySnapshot(fixture.projection)`, cleared `events`, replayed `fixture.events`, and
`history.replaceState`d `?state=` so a state stayed shareable without a reload.)

The current Bench has no terminal-socket provider or Chats-specific authority-harness branch. Its
complete JSX mounts the picker, the Operations-first cockpit shell and the keyed scenario player.

### Invariants And Boundaries

DEV-only — never the production cockpit; `/dev/*` is lazy-loaded and statically dropped from the production
bundle; the current Bench composition contains no mock-terminal provider. `?scenario=` deep links resolve only
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




- The real cockpit shell it renders (also the shell rendered against fixtures). 



- Picker styles. [8]
- Player active-control styles. [9]

### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.

## Historical FEUI-L8 Card Account (Superseded)

The prior card recorded the following composition, which is absent from the current Bench module:

> The bench now registers dedicated Chats scenarios through an authority harness and applies an exit boundary when returning to ordinary gallery scenarios. Cockpit scenarios enter Chats directly; other scenarios keep Operations.

The pre-repair card also attributed this earlier wrapper to Slice 6e-1:

> **Slice 6e-1 (Task 6)** wraps the whole tree in a `TerminalSocketContext.Provider value={mockTerminalSocketFactory}`
> so the **Chats view's terminal renders live-looking with no backend** (the mock echoes input + emits a
> banner); production has no provider, so the real cockpit uses a same-origin WebSocket.

These are retained card provenance, not current composition. The following uncommitted-candidate
statement belongs to that prior FEUI-L8 account, not this memory repair.

The reviewed candidate is still uncommitted. Existing verification hash/date remain pinned to the
leaf base; closeout owns commit stamping.



- The real cockpit shell it renders (also the shell rendered against fixtures). [5]


- Retired at the fifth freeze d59c3493: dashboard/src/cockpit/Cockpit.tsx:426-707 - the bytes it recorded now occur 2 times in the file, so no single home can be named and it is not given to the likelier one. Retired means the anchor no longer stands, not that the cited subject was deleted.

- The Bench directly mounts the real cockpit shell with Operations as its initial view. [3]
- The historical gallery fixtures contribute single-frame resting scenarios; both query spellings select from SCENARIOS. [6]
- The `happy-build`→`build-up` legacy-deep-link alias (05k). Anchor: "?scenario=happy-build" [1]
- The grouped scenario picker is a compact selector. Anchor: `htmlFor` [2]
- The scenario model validates named engine-room scenarios before building frames. Anchor: "scenario player: unknown engine-room scenario" [4]
