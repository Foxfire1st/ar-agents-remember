# 07 — Prototype Review: `browser-dashboard` Branch

| Field | Value |
| --- | --- |
| Topic | What the existing mockup branch contains, what to harvest, what to discard |
| Status | Reviewed 2026-06-10; verdict: **rebuild — harvest mc2-operator as the design spec**; branch stays parked as reference, never rebased |
| Sources | `origin/browser-dashboard` @ `bb0579f` (single commit "mockups", 2026-06-05, forked from `83b147e`/2.3.3, purely additive +6,129 lines); full detail in `raw/recon-workflow-output.json` → `prototype` |

## What It Is

Four standalone, zero-dependency HTML files (~58–95KB each, inline CSS + vanilla
JS IIFE) under `dashboard/mockup/`, generated with the **Open Design**
web-prototype skill (nexu-io/open-design; vendored at
`dashboard/mockup/.od-skills/web-prototype-6b239b831b/`, with `.html.artifact.json`
sidecars and ~2.2MB of review PNGs — one, `mq0zupso`, carries red hand-drawn
annotations, i.e. a design-iteration loop, not an app).

- **mc1** "Memory Control" (SpaceX skin: pure black, D-DIN): overview with
  count-up metrics + canvas "memory constellation", memory health, retrieval,
  sessions, worktrees. 5-view IA.
- **mc2** "Agent Operations" (+ **mistral** and **operator** reskins): the richer
  6-view IA — Operations (two-axis tree + attention queue + detail panel),
  Lifecycles, Provider Health, Memory Health, Retrieval, Topology (canvas radial
  map: repos/worktrees/tasks rings, provider satellites, status comets).
- Theming proven: Mistral reskin = ~83 changed lines, Operator = ~275. The
  token-contract approach works.
- All data is mock: in-memory `WS` (workspace→repos→worktrees→tasks) and `MEM`
  models; "live" feed is a random pool on setInterval; no fetch/WS/API anywhere.

## Harvest List (carry forward)

1. **`WS` model shape** (mc2 ~line 648) — seed for the real status/projection
   schema (aligns naturally with the lifecycle entity + contract data).
2. **`MEM` model + segmented coverage bar** (current/drift/stale/missing) — maps
   1:1 onto real drift_check / route-index output.
3. **Attention Queue + detail panel UX** (renderAttn/renderDetail/resolveAttn) —
   note 06's working theory.
4. **Canvas topology renderer** (buildConstel/layout/frame, ~lines 1159–1330):
   deterministic radial layout, provider satellites, comets on real edges,
   DPR-aware resize, hover hit-testing — portable nearly unchanged; candidate
   hero element (possibly re-expressed via xyflow or kept as canvas).
5. **Operator skin oklch token sheet** (`:root` lines 9–70) — starting point to
   re-hue into the podracer palette (note 08).
6. **View metaphors**: l-01 pipeline stepper, gate pipeline with pass/warn/ready,
   two-axis operation tree, event-feed row with flash-in.
7. **Domain copy** — the view subtitles are good one-line product explanations
   (e.g. memory as "a 1-to-1 mirror of the code").
8. The vendored **Open Design skill** itself for future single-file design spikes.

## Why Rebuild (not evolve)

Design artifacts by construction: single-file prototypes, four divergent ~90KB
forks, ES5 innerHTML string-concat rendering with inconsistent escaping
(XSS-prone the moment real data flows), no components/build/tests/types, stale
content (footer pins MCP v2.3.1; fictional second repo "coordination-workbench").
The branch's value is that it solved the IA and proved the theming — both
portable as *specs*, not code.

## Provenance (developer, 2026-06-10)

The PNGs are the **Open Design iteration trail**, not after-the-fact review:
the developer seeded the session with screenshots of the older local mockup
(which is why old-mockup shots sit on this branch at all — same lineage as the
issue-#2 embed), then directed the agent iteratively, including by drawing red
annotations onto screenshots as instructions. The designated endpoint — "the
furthest I got" — is **`agents-remember-mission-control-2.html` (mc2)**. The
mistral/operator files are reskins of mc2, not later design stages.

## Iteration Screenshots (extracted to `raw/mockups/`, 6 unique of 11 files)

| File | Shows |
| --- | --- |
| `mq0sr76o-image.png` (=sr9vv, =t1rbi) | Light/cream full three-pane console "Workspace / Agent Operations" — same design family as the image embedded in issue #2 (which the developer flags as the older/wrong lineage; this branch set is canonical) |
| `mq0zupso-image.png` (=zuzif) | **Annotated (a direction to the agent, not pending feedback):** red circle around the Operation Tree's `BY REPO \| BY LIFECYCLE` pivot toggle, red arrow pointing from it to the Attention Queue column — apparently the instruction that produced the combined Attention / By repo / By lifecycle panel visible in the later dark iterations and present in mc2 |
| `mq1102jl-image.png` | Dark skin, tree pivoted **by lifecycle** — tasks grouped under the real l-01 phase names (Request / Context-Trust / Research / Build) with status (Running/Waiting/Blocked/Queued) |
| `mq1103s6-image.png` | Dark skin, same panel pivoted **by repo** (workspace → repo → branch lane → task) |
| `mq11u4y2-image.png` | Dark topology constellation: REPOS / WORKTREES / TASKS rings around the workspace core |
| `mq127psj-image.png` (=12fuuv, =13c4xy) | **Annotated:** task detail `T-119 · Build` with phase stepper (Request→Close), 4/6 checklist incl. a failed "Rebase on main — conflict" step, Artifacts & context + Checkpoint & memory blocks, and the amber "Awaiting you · conflict · 36m → Resolve" banner. Red underline swoosh beneath the artifacts/checkpoint row, directly above the banner |

Notable: the mockups already prototype **lifecycle as an organizing pivot** —
phase-grouped trees, a per-task phase stepper, and event-log rows tagged
`LIFECYCLE · L-01`. Prior art for note 01's direction — and deliberately so:
the annotations were the developer steering the design toward exactly that
coupling during the Open Design loop.

## Decisions Recorded

- **mc2 (`agents-remember-mission-control-2.html`) is the canonical design
  endpoint** — developer-designated, 2026-06-10. The earlier recon verdict
  ("treat mc2-operator as the spec") is corrected: mistral/operator are reskin
  experiments of mc2; the operator file remains useful only as a reference for
  oklch token mechanics and its tabbed-list/full-height-topology variations.
- **mc2's IA supersedes mc1.** mc1 contributes only the constellation variant and
  the jump-card overview pattern.
- Branch stays parked; nothing on it needs rebasing (purely additive); strip the
  2.2MB PNGs if it ever lands anywhere.
- Aesthetic: Operator skin is the closest *starting point*, but its
  Linear/Datadog look is explicitly what the podracer grammar (note 08) replaces.
  Keep its IA + token mechanics, swap its soul.
- Unknown still: what the red-pen annotations on `mq0zupso-image.png` say —
  check before finalizing IA (note 11).
