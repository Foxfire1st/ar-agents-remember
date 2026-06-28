# podstage.html

| Field                  | Value                                       |
| ---------------------- | ------------------------------------------- |
| repository             | agents-remember                             |
| path                   | `docs/design/engine-room/podstage.html`     |
| doc_type               | `file-level-onboarding`                     |
| lastUpdated            | 2026-06-21T23:35                            |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`  |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `overview.md`                               |

## Governing Overview

[engine-room/ design overview](overview.md)

## Purpose

`podstage.html` is the engine-room **prototype / scenario player** — the self-contained HTML mockup that
the production React engine-room canvas (`dashboard/src/panels/engine-room/`) was built from. It renders the
git-lifecycle of a worktree as a podracer cockpit (two-world canvas: official line ↔ worktree enclosure,
provider engine gauges, branch/commit nodes, conduits, code⇄memory couplers) and lets you step or play
through scripted scenarios: the **build-up** (B0→B5) and **tear-down** (D0→D6) happy paths plus a full
**failure-mode scene library**. It is the authoring ground where the choreography and the failure-primitive
vocabulary were worked out before being translated to GSAP + Motion. Its distilled, named primitives live in
the companion living spec `engine-room-visual-language.html`.

## Code Commentary

### Logic

The page is one big `<svg id="scene">` of pre-placed elements (engines, branch nodes, couplers, flow
conduit paths in `<defs>`, remote dock chips, and the failure-mode overlays) plus a `<script>` controller:

- **Primitive helpers** — small functions toggle element state: `prov(id,state)` sets an engine's runtime
  class (`dim`/`booting`/`green`/`nominal`/`off`/`fault`/`reindex`), `flow(id,on)` draws a conduit in
  (`.on`) or retracts it out (`.off`), `refuse(id,red)` flashes a seed conduit then recolours it (amber =
  reroute, red = fault), `flag`, `ghost`, `cls`.
- **Failure-mode helpers** — `gate(...)` drops a steady red gate bar + a local reason badge, `fleeting(...)`
  shows the ghost/blocked provisional enclosure, `attn(...)` the breathing attention badge, `scan(...)` the
  preflight sweep ring, `chips(...)` the recovery-choice chips, `imsg(...)` a generic indicator/reason badge
  (soft = cyan, a fallback not a fault). `clearFail()` resets them all.
- **Shared build steps** (`STEP`) — `reset`, `codeWt`, `memWt`, `enginesDim`, `charge`, `running`, `idle`,
  `idleClean` are the reusable beats both the happy build-up and the failure-recovery tails compose from.
- **Scenario arrays** — each scenario is an ordered list of beats `{k, cap, dur?, do()}`. `BUILD` (B0–B5),
  `TEAR` (D0–D6), then the failure library: `T1B` stale-base block, `T3B` memory/ledger block, `T7B`
  provider/pre-contract block, `T9B` seed fault (flicker), `T9C` reindex reroute (amber, a fallback), `T12B`
  live memory-sync block, `T14C` **terminal** integration conflict (no auto-recovery), `T18` abandon
  (dissolve, no landing).
- **Controller** — `SCENARIOS` maps the `<select>` options to those arrays; `seekTo`/`next`/`prev`/`play`/
  `pause`/`loadSeq` drive playback. A `.seeking` class disables transitions for instant scrub; `seq([...])`
  schedules staggered intra-beat reveals during play (and fires them instantly while seeking). A blueprint
  boomerang `<video>` backdrop loops behind the scene. `window.__pod` exposes the transport for inspection.

### Conventions

- **Colour-as-state**, same OKLCH tokens as the living spec: cyan = active flow, amber = settled wire /
  reindex, mint = fresh / healthy engine, red (`--alarm`) = fault / blocked, dormant = off / pruned.
- **Blocked must read differently from fault**: a `gate` is a **steady** red bar (a choice the developer
  must make); a `.prov.fault` engine **flickers** (`@keyframes flick`, capped). The attention badge breathes
  (`@keyframes attn`), never strobes.
- **Reroute vs failure**: a refused seed conduit recolours **amber** (reindex reroute, a fallback) by
  default, **red** only when `red=true` (a true fault). Soft `imsg` badges are cyan, not alarm.
- Conduits **draw in** source→target and **retract out** source→tip (`stroke-dashoffset` 100→0→-100); a
  packet rides via `offset-path`. Engines charge `scaleY` then `powerup` to green/amber.
- The primitive CSS classes (`.flowpath`, `.wire`, `.node`, `.prov`, `.e-charge`, `.coupler-g`, `.gate`,
  `.fleeting`, `.attn`, `.chip`, `.imsg`, `.scan`, `.dissolve`) are the shared vocabulary mirrored by the
  living spec and the React recipes.

### Invariants And Boundaries

- This is the **prototype that the React canvas was built from**, not shipped application code. It animates
  in CSS for portability; the production renderer re-implements the same beats in GSAP + Motion.
- The distilled, named, parameterised version of these primitives is the living spec
  `engine-room-visual-language.html`; that spec is the source of truth. This file is the working scenario
  player / scene library behind it.
- Scenario beat keys (B0–B5, D0–D6, and the T1b/T3b/T7b/T9b/T9c/T12b/T14c/T18 letters) are referenced by the
  engine-room slice work; the failure taxonomy (block vs fault vs reroute vs terminal vs abandon) is
  load-bearing for the renderer's overlays.
- Terminal scenarios (`T14C` integration conflict) deliberately offer **no auto-recovery** — only a "resolve
  manually" chip — to mirror the real all-or-nothing integration contract.

### Todos

None tracked outside active task work.

## Docs References

This is a self-contained design prototype; the only external context is the animation stack the production
renderer uses to realise it. No external documentation was required. No relevant documentation found after
checking live sources.

| Finding | Citations | Source Path |
| ------- | --------- | ----------- |
| The scenario library + transport (`SCENARIOS`, `seekTo`/`play`/`loadSeq`) defining the build-up, tear-down, and failure-mode scenes the renderer reproduces. | L710-L735 | [podstage.html](podstage.html) |

## Repo-Internal References

The prototype sits between the living spec (which distils it) and the React renderer (which reproduces it).
The two cross-links below are that proving pair.

| Finding | Citations | Source Path |
| ------- | --------- | ----------- |
| The living spec that distils this prototype's primitives into the canonical, parameterised visual language; its CSS classes mirror this file 1:1. | L11-L12, L93-L107 | [engine-room-visual-language.html](engine-room-visual-language.html) |
| The React engine-room renderer built from this prototype — the same two-world canvas, scenario beats (B0→B5 / D0→D6), and failure scenes (t12b / t14c / t18) reproduced in GSAP + Motion. | — | [dashboard/src/panels/engine-room/overview.md](../../../dashboard/src/panels/engine-room/overview.md) |

## Cross-Repo References

This is an in-repo design prototype with no cross-repository or external-system boundary. No meaningful
cross-repo references found.

| Finding | Citations | Source Path |
| ------- | --------- | ----------- |
| _None._ | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->

- 2026-06-21T23:35 — Created. File-level onboarding for the engine-room `podstage.html` prototype / scenario
  player: documented the two-world podracer canvas, the build-up (B0→B5) and tear-down (D0→D6) happy paths,
  the full failure-mode scene library (T1b stale-base, T3b memory/ledger, T7b provider/pre-contract, T9b
  seed fault, T9c reindex reroute, T12b live sync, T14c terminal integration conflict, T18 abandon), the
  failure-primitive CSS vocabulary (gate, attention badge, fleeting ghost, refused conduit, scan ring,
  dissolve), the controller/transport, and the cross-links to the living spec and the
  `dashboard/src/panels/engine-room/` renderer built from it. The source file is newly added and not yet
  committed; verification metadata pinned to repo HEAD until a commit stamps it.
