# dashboard/src/panels/FlowTab.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/FlowTab.tsx`               |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-06T15:40+02:00                           |
| lastVerifiedCommitHash | `d9a1eb82849baea6c0b86735e772a932f4bbdc7c`       |
| lastVerifiedCommitDate | 2026-08-12T00:45:15+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[panels overview](overview.md)

## Purpose

The **lifecycle-design canvas** (orchestration leaf 260703-L0): FlowTab is no longer the single
hardcoded build-job diagram it was at task 26. It is now a **pure segment renderer + model nav** — the
surface where a lifecycle or agent interaction is **drawn and reviewed with the developer before it is
built**. All content lives in the sibling `flowModels.ts` registry (`FLOW_MODELS` — 8 static models
since 260703-L12: router · designer · strategist · orchestrator · manager · worker · reviewer ·
comms, the converged `l-01-agent-lifecycles` doctrine; the pre-convergence build-job/frame models
died with the l-01/l-02 convergence). This file owns only the presentation: a `Segment` renderer
that draws one of four segment kinds (start / node / gate-rider node / rundown card / divider) and
a **radiogroup model nav** (the `RailToggle`/`EffectsToggle` idiom) that switches which model is
shown. It is **still zero store reads** — it takes at most an `initialModel` string prop and holds
one piece of local nav state.

Task 29 removed it from the cockpit `View` union and mode bar, and that stays true: it is **mounted
dev-only** at `/dev/flows` (see `dev/DevApp.tsx`), dead-code-eliminated from the production bundle.

## Code Commentary

### Logic

cit:([`FlowTab`], dashboard/src/panels/FlowTab.tsx:111-150) resolves the shown model against the
`flowModels.FLOW_MODELS` array: it seeds `useState` with `initialModel` only when some registered model
carries that id, else falls back to `FLOW_MODELS[0]` (the router model); an unknown id therefore
lands on the fallback rather than crashing. The root `<div>` carries `data-testid="flow-tab"`
and `data-model={model.id}`. The **model nav** is a `role="radiogroup"`
(`aria-label="Flow model"`, `data-testid="flow-nav"`) of one `role="radio"` button per model, each with
`aria-checked={m.id === model.id}`, `data-testid={\`flow-nav-${m.id}\`}`, and an `onClick` that sets the
nav state. Below the nav sit the header (`LIFECYCLE FLOW · {model.title}`) + the wired-today/this-series
legend, the model `takeaway` paragraph, and the `chain` column that maps `model.segments` through
`<Segment>`.

cit:([`Segment`], dashboard/src/panels/FlowTab.tsx:81-109) is a discriminated-union switch over `segment.kind`:

- **`start`** — a dotted pill `startNode` with the label, and, when `segment.next` is set, an
  `Arrow` to it (`segment.nextStatus ?? "proposed"`).
- **`node`** — a `ToolNode` plus the optional outgoing `Arrow`.
- **`rundown`** — a dashed `rundownCard` (`data-testid="flow-rundown"`) with a title and one
  styled line per `segment.lines` entry; a line with `junction: true` renders cyan/mono via the
  `rundownLine` cva variant.
- **`divider`** — a centered italic caption.

cit:([`ToolNode`], dashboard/src/panels/FlowTab.tsx:60-70) picks the `ridesNode` style (amber left-bar) when `n.rides` is set, else the
plain `toolNode`, and tags itself `data-testid="flow-gate"` vs `"flow-node"` accordingly. It appends
`" · gate"` to the phase tag for gate nodes, renders the monospace `tool` name and optional `detail`,
and for a gate renders a rider line = `n.ridesNote ?? DEFAULT_RIDES_NOTE(n.rides)`.
cit:([`DEFAULT_RIDES_NOTE`], dashboard/src/panels/FlowTab.tsx:57-58) is the task-26 auto-fire framing (`⊘ auto-fires
lifecycle_turn_end_notification · {rides} — rides this call … next AR tool clears it`); orchestration
models override it per node (the two adversarial seams, delegated gates, judge evidence, reframe).
cit:([`Arrow`], dashboard/src/panels/FlowTab.tsx:72-79) draws the connector wire + `nextStep → {to}` label and sets
`data-edge={status}`; the `wire`/`connector`/`swatch` cva variants encode **mint = current (wired
today)** vs **amber dashed = proposed (this series)**.

### Conventions

cit:([`FlowTab`], dashboard/src/panels/FlowTab.tsx:111-150) Styling is co-located Panda **`css`/`cva`**
imported from the generated `../../styled-system/css`, token-keyed
(`mint`/`amber`/`cyan`/`ink`/`muted`/`grid`/`bg`); no global CSS, no hardcoded colours.
The model nav mirrors the repo's radiogroup toggle idiom (`RailToggle`/`EffectsToggle`) rather than a
React Aria widget, since it is a small dev-only control. Types (`FlowModel`, `FlowNode`, `FlowSegment`,
`Status`) and all content are imported from `flowModels.ts` — this file defines no model data.
Segments are keyed by array index in the map; rundown lines by index. Stable
test/contract hooks: `data-testid` `flow-tab` / `flow-nav` / `flow-nav-{id}` / `flow-node` / `flow-gate`
/ `flow-rundown`, plus `data-model` on the root, `aria-checked` on the radios, and `data-edge` on arrows.

### Invariants And Boundaries

- **Renderer + nav only; content is external.** FlowTab holds no model data — it renders whatever
  `FLOW_MODELS` contains. Adding or reshaping a drawn lifecycle is a `flowModels.ts` edit, not a change
  here. Keep the segment-kind switch and `flowModels`' `FlowSegment` union in lockstep.
- **Zero store reads, near-stateless.** Unlike the other panels it does not read the Zustand store; the
  only state is the selected nav model id, seeded from the optional `initialModel` prop. An unknown
  `initialModel` deterministically falls back to `FLOW_MODELS[0]`.
- **Dev-only surface.** It is not in the cockpit `View` union (task 29) — it is mounted at `/dev/flows`
  through `dev/DevApp.tsx` and eliminated from production. It does not render through `grammar/Panel`; it
  owns its own scrolling `root` div (full-bleed in the dev harness shell).
- **The turn-end notification is not a tool the agent calls.** The default rider line keeps the task-26
  framing (it rides the gate tool); orchestration models substitute their own `ridesNote` for the two
  adversarial seams, delegated gates, judge evidence, and reframe — but the amber left-bar always marks a
  gate/seam, never a plain call.
- **Colour semantics are fixed:** mint = wired today, amber dashed = proposed by the active series; the
  `Status` union and the cva variants are the single source of that mapping.

## Docs References

| Source | Relevance |
| --- | --- |

No relevant documentation found after checking live sources.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The flow-model registry FlowTab renders and switches between — all content + the segment/model types live here. | `FLOW_MODELS` | dashboard/src/panels/flowModels.ts:438-438 |
| The renderer + nav under test (default model, nav switching, initialModel fallback, per-model render census, invariant text). | "FlowTab canvas (unified l-01-agent-lifecycles)" | dashboard/src/panels/FlowTab.test.tsx:9-176 |
| The dev harness route that mounts FlowTab at `/dev/flows` with `initialModel` from `?model=`. | `initialModel` | dashboard/src/dev/DevApp.tsx:15-20 |
| The next-step engine the build-job model is the human-readable spec for (regime model). | `compute_next_step` | mcp/src/agents_remember/application/next_step.py:110-131 |
| Generated Panda `css`/`cva` this panel styles with. | `FlowTab` | dashboard/src/panels/FlowTab.tsx:111-150 |

## Cross-Repo References

No meaningful cross-repo references found.

## Update History

- 2026-08-02T20:53:56+02:00 — W2-B04 curator: repaired 21 citation findings; scoped check passed.

- 2026-07-06T15:40+02:00 — 260703-L12 (three-party loops, staleness de-stale — no source change): the Purpose's pre-convergence census ("8 static models" meaning build-job/frame-era; "the other seven models draw … designer, frame, …") was stale since the L8 convergence and is rewritten to the current 8-model registry (strategist joins in L12); the Logic fallback line now names the router, not build-job. Verification metadata pinned until closeout stamps the L12 commit.
- 2026-07-04T09:40+02:00 — 260703-L0 (Canvas & playground): rewrote FlowTab from the single hardcoded
  build-job diagram (`RUNDOWN`/`HEAD`/`LINEAR` module constants) into a **multi-model design canvas** — a
  pure `Segment` renderer (start / node / gate-rider with optional `ridesNote` override / rundown card /
  divider) over the externalized `flowModels.ts` `FLOW_MODELS` registry, plus a radiogroup model nav
  (`RailToggle` idiom). Added the `initialModel` prop + unknown-id fallback; the source is now mounted
  dev-only at `/dev/flows` (`?model=` deep link) and stays out of the cockpit `View` union. Still zero
  store reads. New coverage lives in `FlowTab.test.tsx`. Verification metadata pinned until closeout
  stamps the L0 commit.
- 2026-06-27T18:43+02:00 — Added for task 26: new `FlowTab.tsx`, the "Lifecycle Flow" cockpit View —
  a static two-regime diagram (`RUNDOWN` front-half prose + `HEAD`/`LINEAR` node chains) that is the
  human-readable spec the task-27 `next_step.py` engine matches; mint edges = wired today, amber
  dashed = this leaf-26/27 series. Verification metadata pinned until closeout stamps the code commit.
