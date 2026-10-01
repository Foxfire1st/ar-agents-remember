# dashboard/src/panels/engine-room/EnclosureProcessMap.tsx

## Governing Overview

[engine-room overview](overview.md)

## Purpose

The Engine Room pod-stage **shell** for one `EngineProcessNode` (5g G1). The bird's-eye render moved out
to `EnclosureCanvas`, so this file is now a thin wrapper: a `motion.div` (`process-map`) that mounts at its
settled state (`initial={false}`) and carries the **promote-in-place** morph (gated `layout`). It renders
no HTML fleeting banner. Pre-contract or stale-base blocked-start presentation is derived and drawn
inside `EnclosureCanvas` as `FleetingEnclosure`. The shell delegates the two-world scene — official
line ↔ worktree enclosure, engine gauges, warp coupler, conduits — to
`<EnclosureCanvas node={node} workspaceEngines={…} />`.
**5g G5** adds the t18 **abandon** end-state: when `node.phase === "abandoned"` the shell renders an
`AbandonRecord` banner (full opacity, persists) above the canvas and wraps the canvas in a `dissolveShell`
(dim + grayscale) so the enclosure dissolves to a ghost while its record stays; `process-map[data-abandoned]`
flags it. **5g G6** mounts the faint blueprint-boomerang **backdrop** behind the scene (effects-gated), and
the **visual-parity pass** threads `workspaceEngines` straight through to `EnclosureCanvas` for the left
official-line engines. **5h H4** generalizes the dissolve to a `teardown` axis — abandon (failure, no
landing) **and** cleanup (`phase: "cleanup-pending"` — a landed enclosure de-materialising back into the
official line): both set `data-teardown` and render a record (abandon's `AbandonRecord` vs cleanup's
success-toned `CleanupRecord`, ✓ landed, naming the `origin-main` tip); the `data-abandoned` hook stays
abandon-only. **Slice 5i** then **splits the visual treatment**: only **abandon** wraps the canvas in the
full-dim `dissolveShell` (the whole enclosure dissolves — failure, nothing landed); a **landed cleanup**
de-materialises only the **worktree side** (the worktree refs go `planned`/detaching and the engines power
down *inside the canvas*, while main stays bright), so cleanup no longer wraps in the dim shell. The
`CleanupRecord`/`AbandonRecord` + `data-teardown` hooks are unchanged. Task 11 adds an optional
`gateNode` prop, threaded straight through to `EnclosureCanvas` so the canvas has the projected gate
identity in addition to its visual edge/phase gate bars.

## Code Commentary

### Logic

`EnclosureProcessMap({ node, gateNode, workspaceEngines = [], officialLedger })` is the only export — a `motion.div` (`mapWrap`, now a
positioned `overflow:hidden` stacking context) that mounts at its settled state and carries
`layout` (gated by `useShouldAnimate`; instant under `data-effects=off`), so a fleeting→real swap of
the same keyed element morphs its size in place (T4). **`initial={false}`** (2026-06-21): the wrapper no longer animates
opacity/scale up *from* `{opacity:0, scale:0.985}`; it mounts at the `animate` end-state (`opacity:1,
scale:1`) and only the `layout`/`animate` target drives subsequent change. This fixes a second-scenario-loop
bug where the whole map stranded at **opacity 0** when the scenario player remounted the wrapper through the
B0 (no-enclosure) frame — the enter never re-ran, so the old `initial` opacity-0 was never animated away. **5g G6**: when `useShouldAnimate()` is true the wrapper mounts a
`backdrop` `<div>` holding `backdropVideo` (`<video src="/assets/blueprint-boomerang.mp4">`, `aria-hidden`,
absent under reduced-motion / `data-effects=off`) beneath a `stageContent` layer that holds the scene.
Born-blocked detection and presentation are canvas-owned: `EnclosureCanvas` derives its
`fleeting` condition from current facts and renders `FleetingEnclosure` there. The body of the map is
`<EnclosureCanvas node={node} workspaceEngines={workspaceEngines} officialLedger={officialLedger} />` (the
bird's-eye); the previous linear-lane render moved into `EnclosureCanvas` and the travelling packet +
draw-on returned in G2. Slice 5h threads the optional `officialLedger?: LedgerNode` prop straight through
to `EnclosureCanvas` (resolved per repo in `EngineRoom`) for the OFFICIAL coupler's memory.md popover.
**Slice 05k** converts the abandon dissolve from a plain `<div className={dissolveShell}>` to a
`motion.div` (still `data-testid="dissolve"`): Motion now owns the dim + desaturate
(`initial={animate ? { opacity: 1, filter: "grayscale(0)" } : false}`, `animate={{ opacity: 0.4, filter:
"grayscale(0.75)" }}`, `transition` 0.6s ease-out), matching the §8 rule that the `dissolveShell` recipe is
layout-only and Motion drives the fade — under `!animate` it mounts at the dissolved end-state.
**Slice 05o** removes the HTML fleeting banner entirely: the `FleetingBanner` component, the `isFleeting`
helper, the fleeting-star style imports (`fleetingBanner`/`Label`/`Reason`/`Choices`/`Choice`), and the
`AnimatePresence` import + wrapper that rendered the banner are all gone. A pre-contract or stale-base
born-blocked enclosure (5f §2.1) is now drawn entirely **inside the canvas** as the big red
`FleetingEnclosure` box (in `EnclosureCanvas`), so this shell no longer renders an HTML banner strip — only
a short code comment marks where it lived. The `mapWrap` layout, the abandon/cleanup records, and the
abandon `dissolveShell` are unchanged. `gateNode` is not rendered as an HTML control here; it is passed
into `EnclosureCanvas` as data while the actionable secondary control lives in `DiagnosticsPanel`.

### Invariants And Boundaries

Purely presentational — all data via the `node` (+ `workspaceEngines`) props. **Honest motion (§2/§8.4):**
Motion reads `useShouldAnimate()`; under `data-effects=off` or reduced-motion the shell is an instant swap
(`layout` off, the abandon `dissolveShell` `motion.div` mounted at its dissolved
end-state via `initial={false}`) **and the backdrop is absent + lazy** — snapshot-stable. No CSS
animation/transition drives the dissolve anymore (§8): Motion owns the opacity + grayscale; the recipe is
layout-only. **Stable
identity:** the enclosure is keyed by `worktreeGroup` (S0) upstream, so the fleeting (start-progress id) →
real (contract-path id) swap reuses the element — the morph, not a remount. Provisional ≠ live. The backdrop
is `aria-hidden` pure atmosphere, never state. Shell hooks are `process-map` and `backdrop`; the
`fleeting-enclosure` hook and the scene's other hooks (`enclosure-canvas`, `branch-node`,
`engine-gauge`, `conduit`, `warp-coupler`, …) live in `EnclosureCanvas`.

## Evidence

### Repo-Internal References

- `EnclosureProcessMap` — `motion.div` shell (gated enter + `layout` morph) that delegates the scene. [1]
- The G6 backdrop (`backdrop`/`backdropVideo`/`stageContent`) mounted only when effects are on. [2]
- The shell renders no HTML fleeting banner and delegates every live scene branch to `EnclosureCanvas`. [3]
- The canvas derives its `fleeting` predicate and renders `FleetingEnclosure` for the born-blocked case. [4]
- The focused regression asserts the canvas-owned `fleeting-enclosure` exposes both stale-base recovery choices. [5]
- The bird's-eye scene (the render body, given `workspaceEngines`). [6]
- The honest-motion gate. [7]
- EngineProcessNode is the generated projection contract consumed by this surface. [8]
- ProviderNode is the generated projection contract consumed by this surface. [9]
- GateNode is the generated projection contract consumed by this surface. [10]

## Current L5I Maintenance

The process-map wrapper is observed for visibility. A hidden keep-alive room pauses the decorative
blueprint video, then resumes playback on re-show without unmounting the map.
