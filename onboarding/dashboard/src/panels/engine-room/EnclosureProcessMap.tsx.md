# dashboard/src/panels/engine-room/EnclosureProcessMap.tsx

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/engine-room/EnclosureProcessMap.tsx`  |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated | 2026-07-24T13:17:17Z |
| lastVerifiedCommitHash | `842b487b854503d95c9c2d9dce1841198ba93c7d`|
| lastVerifiedCommitDate | 2026-07-24T17:08:25+02:00|
| governingOverview      | `overview.md`                                               |

## Governing Overview

[engine-room overview](overview.md)

## Purpose

The Engine Room pod-stage **shell** for one `EngineProcessNode` (5g G1). The bird's-eye render moved out
to `EnclosureCanvas`, so this file is now a thin wrapper: a `motion.div` (`process-map`) that mounts at its
settled state (`initial={false}`) and carries the **promote-in-place** morph (gated `layout`), plus the **fleeting**
(pre-contract blocked-start) banner (§2.1). It delegates the two-world scene — official line ↔ worktree
enclosure, engine gauges, warp coupler, conduits — to `<EnclosureCanvas node={node} workspaceEngines={…} />`.
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
positioned `overflow:hidden` stacking context) that scales in on mount and carries `layout` (both
gated by `useShouldAnimate`; instant under `data-effects=off`), so a fleeting→real swap of the same keyed
element morphs its size in place (T4). **`initial={false}`** (2026-06-21): the wrapper no longer animates
opacity/scale up *from* `{opacity:0, scale:0.985}`; it mounts at the `animate` end-state (`opacity:1,
scale:1`) and only the `layout`/`animate` target drives subsequent change. This fixes a second-scenario-loop
bug where the whole map stranded at **opacity 0** when the scenario player remounted the wrapper through the
B0 (no-enclosure) frame — the enter never re-ran, so the old `initial` opacity-0 was never animated away. **5g G6**: when `useShouldAnimate()` is true the wrapper mounts a
`backdrop` `<div>` holding `backdropVideo` (`<video src="/assets/blueprint-boomerang.mp4">`, `aria-hidden`,
absent under reduced-motion / `data-effects=off`) beneath a `stageContent` layer that holds the scene.
`isFleeting(node)` is true when `missingFacts` contains a "contract not yet written" marker; the
`FleetingBanner` (block label, `node.summary` reason, `node.nextAction` recovery choice) is wrapped in
`AnimatePresence` so it **fades out in place as the node promotes**. The body of the map is
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
(banner exit instant, `layout` off, the abandon `dissolveShell` `motion.div` mounted at its dissolved
end-state via `initial={false}`) **and the backdrop is absent + lazy** — snapshot-stable. No CSS
animation/transition drives the dissolve anymore (§8): Motion owns the opacity + grayscale; the recipe is
layout-only. **Stable
identity:** the enclosure is keyed by `worktreeGroup` (S0) upstream, so the fleeting (start-progress id) →
real (contract-path id) swap reuses the element — the morph, not a remount. Provisional ≠ live. The backdrop
is `aria-hidden` pure atmosphere, never state. `data-testid` hooks (`process-map`, `fleeting-banner`,
`backdrop`) are load-bearing; the scene's own hooks (`enclosure-canvas`, `branch-node`, `engine-gauge`,
`conduit`, `warp-coupler`, …) live in `EnclosureCanvas`.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| `EnclosureProcessMap` — `motion.div` shell (gated enter + `layout` morph) that delegates the scene. | — | [EnclosureProcessMap.tsx](EnclosureProcessMap.tsx) |
| The G6 backdrop (`backdrop`/`backdropVideo`/`stageContent`) mounted only when effects are on. | — | [EnclosureProcessMap.tsx](EnclosureProcessMap.tsx) |
| `isFleeting` + `FleetingBanner` in `AnimatePresence` (T4 promotion morph, §2.1). | — | [EnclosureProcessMap.tsx](EnclosureProcessMap.tsx) |
| The bird's-eye scene (the render body, given `workspaceEngines`). | — | [EnclosureCanvas.tsx](EnclosureCanvas.tsx) |
| The honest-motion gate. | — | [useShouldAnimate.ts](useShouldAnimate.ts) |
| Projection types `EngineProcessNode` / `ProviderNode` / `GateNode`. | L251-L285 | [projection.ts](../../types/projection.ts) |

## Current L5I Maintenance

The process-map wrapper is observed for visibility. A hidden keep-alive room pauses the decorative
blueprint video, then resumes playback on re-show without unmounting the map.

## Update History

- 2026-07-24T13:17:17Z — Curator: recorded hidden-layer video pause/resume behavior; verification
  fields remain pre-commit.

- 2026-06-23T13:45+02:00 — Task 11: added optional `gateNode` prop and threaded it into
  `EnclosureCanvas`. The process map still renders no gate response control; diagnostics owns the
  secondary Respond UI. Verification metadata pinned until closeout stamps the task-11 code commit.
- 2026-06-22T10:45 — slice 05o: removed the HTML `FleetingBanner` component, the `isFleeting` helper, the
  fleeting-star style imports (`fleetingBanner`/`Label`/`Reason`/`Choices`/`Choice`), and the
  `AnimatePresence` import + wrapper that rendered the banner. A pre-contract / stale-base born-blocked
  enclosure is now drawn entirely inside the canvas as the big red `FleetingEnclosure` box (in
  `EnclosureCanvas`), so this shell no longer renders an HTML banner strip. The `mapWrap` layout, the
  abandon/cleanup records, and the dissolve shell are unchanged. Verification metadata pinned until closeout
  stamps the 05o code commit.
- 2026-06-21T23:35 — set the `mapWrap` `motion.div` `initial` to `false` (was `{opacity:0, scale:0.985}`):
  the wrapper now mounts at its `animate` end-state instead of animating up from opacity 0. Fixes a
  second-scenario-loop bug where the whole map stranded at opacity 0 on remount through the B0 (no-enclosure)
  frame — the enter animation never re-ran, so the old initial opacity-0 was never cleared. Verification
  metadata pinned until closeout stamps the code commit.
- 2026-06-21T02:27+02:00 — slice 05k: converted the abandon `dissolveShell` from a plain `<div>` to a
  `motion.div` — Motion now owns the dim + desaturate (opacity 1→0.4, `grayscale(0)`→`grayscale(0.75)`, gated
  by `useShouldAnimate`), matching §8 (CSS static; the recipe is layout-only). `data-testid="dissolve"` +
  the teardown split are unchanged. Verification metadata pinned until closeout stamps the 05k code commit.
- 2026-06-19T23:58+02:00 — slice 5i: split the teardown visual treatment — only **abandon** keeps the
  full-dim `dissolveShell`; a landed **cleanup** now de-materialises only the worktree side inside the canvas
  (main stays bright), so cleanup no longer wraps in the dim shell. Records + `data-teardown` hooks unchanged.
  Verification metadata pinned until closeout stamps the code commit.
- 2026-06-19T15:50+02:00 — slice 5h H4 cleanup teardown: generalized the abandon dissolve to a `teardown` axis — added `CleanupRecord` (success-toned, names the `origin-main` tip) and a `data-teardown` hook ("abandon" | "cleanup"); a `phase: "cleanup-pending"` enclosure now de-materialises via `dissolveShell` like abandon but reads as a successful landing. `data-abandoned` stays abandon-only. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-18T18:00+02:00 — slice 5h ledger popover: threads the optional `officialLedger?: LedgerNode` prop through to `EnclosureCanvas` (for the official coupler's popover). Verification metadata pinned until closeout stamps the code commit.
- 2026-06-17T22:45 — 5g G6 + visual-parity pass: `mapWrap` became a positioned `overflow:hidden` stacking
  context; an effects-gated `backdrop` `<div>` (the `backdropVideo` blueprint-boomerang `<video>`, absent
  under `data-effects=off`) mounts beneath a `stageContent` layer; the shell now takes `workspaceEngines`
  (default `[]`) and passes it straight to `<EnclosureCanvas>` for the left official-line engines. Added the
  `backdrop` test hook. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-17T16:15 — slice 5g G5 (t18 abandon): when `node.phase === "abandoned"` the shell renders an
  `AbandonRecord` (full-opacity, persists) and wraps `EnclosureCanvas` in a `dissolveShell` (dim + grayscale,
  on a plain wrapper so Motion's `animate` opacity can't override it; frozen under effects=off) so the
  enclosure dissolves while its record stays; added the `data-abandoned` hook. Verification metadata pinned
  until closeout stamps the G5 code commit.
- 2026-06-17T12:47 — slice 5g G1: the bird's-eye render moved out to `EnclosureCanvas`; this file is now
  the thin **shell** (the `motion.div` promote-in-place morph + the fleeting banner) and delegates the
  two-world scene to `<EnclosureCanvas>`. The linear-lane render (`CommitNode`/`SvgConduit`/`EngineUnit`)
  and its `code-lane`/`memory-lane` test hooks are retired; the travelling packet + conduit draw-on move to
  G2. Verification metadata pinned until closeout stamps the G1 code commit.
- 2026-06-16T03:40 — slice 5f S4 (power-up T8/T9): `SvgConduit` renders a gated GSAP `conduit-flow` packet that travels along a **running** conduit during clone/seed (hidden under `data-effects=off`); engine seeding/fault remain conveyed by the `engineSilhouette` indexing/down variants. Verification metadata pinned until closeout stamps the S4 code commit.
- 2026-06-16T03:35 — slice 5f S3 (T4 promotion morph): the map's `motion.div` gained gated `layout` and
  the `FleetingBanner` moved inside `AnimatePresence`, so a blocked fleeting node solidifies **in place**
  into the real enclosure (keyed-stable by `worktreeGroup`) rather than teleporting; the ghost banner
  fades out as it promotes. Deterministic under `data-effects=off`. Verification metadata pinned until
  closeout stamps the S3 code commit.
- 2026-06-16T03:05 — slice 5f S2 (birth motion): the map became a `motion.div` with a gated enter; each
  `SvgConduit` draws on via a gated GSAP `strokeDashoffset` tween; `isFleeting` + `FleetingBanner` render a
  pre-contract blocked-start node as provisional (§2.1).
- 2026-06-16T01:55 — slice 5f S0: the four conduits became `SvgConduit` (SVG `<line>` via `conduitLine`),
  replacing the 2px `<span>` conduit.
- 2026-06-15T19:35 — Created for slice 5e: the podracer diagram: official line -> worktrees -> contract coupler -> CGC/GrepAI engines, conduits state-coloured. Verification metadata pinned until closeout stamps the 5e code commit.
