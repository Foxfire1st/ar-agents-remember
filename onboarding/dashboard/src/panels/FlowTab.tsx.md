# dashboard/src/panels/FlowTab.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/FlowTab.tsx`               |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-06-27T18:43+02:00                           |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`       |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[panels/ overview](overview.md)

## Purpose

The **"Lifecycle Flow"** cockpit panel (task 26): a developer-facing diagnostic that draws the
BUILD-job lifecycle as a vertical flow chart in **two regimes**. It is the human-readable **SPEC** the
task-27 next-step engine (`mcp/.../tools/next_step.py`) was built to match — its `RUNDOWN`/`HEAD`/
`LINEAR` arrays encode the same regime model the engine projects. It renders the leaf-28 auto-fire
end-state (every gate tool's turn-end notification riding the call); leaf-27 implements the hint-guided
version. Pure static spec art — no store read, no props, no state.

## Code Commentary

### Logic

Three module-level constants are the whole content; the JSX just maps them.

- `RUNDOWN: { line; junction? }[]` — the **front half (non-linear)**: the one-time PROSE rundown
  `lifecycle_start` emits (reframe → research → job-selection → `⟁ task-file-exists?` → `task_doc`).
  It is prose, not per-tool hints, because the research tools fire unpredictably and the
  `task-file-exists?` junction is not a tool call (`junction: true` styles that one line cyan/mono).
- `HEAD: Node[]` — the two trust-checkpoint tools that precede the rundown (`context_packet`,
  `lifecycle_start`).
- `LINEAR: Node[]` — the **linear half** from `worktree_start --dry-run` through `lifecycle_end`.
- `interface Node { phase; tool; detail?; rides?; next?; nextStatus? }`. `next`/`nextStatus` are the
  outgoing `nextStep →` edge + its colour. `rides` names the gate whose turn-end notification
  auto-fires when that tool is called (dry-run / preview / closeout / finalize / integrate steps).
- `type Status = "current" | "proposed"` drives colour everywhere: **current = mint** (wired today,
  `guidance.lifecycle_guidance`), **proposed = amber dashed** (this leaf-26/27 series). Per-edge,
  `nextStatus` decides mint vs amber; today only the closeout→integrate→carryover→finalize→end edges
  are `current`.

Components: `ToolNode({n})` picks `ridesNode` (amber left-bar) when `n.rides` is set else `toolNode`,
tags `data-testid` `flow-gate`/`flow-node`, appends `· gate` to the phase tag, and renders the
`⊘ auto-fires lifecycle_turn_end_notification … rides this call … next AR tool clears it` rider line.
`Arrow({to,status})` draws the connector wire + `nextStep → {to}` label, `data-edge={status}`.
`FlowTab()` lays out: header + legend, a takeaway `<p>`, then the `chain` column — a start node, an
Arrow into `context_packet`, the `HEAD` nodes, the `rundownCard` (`data-testid="flow-rundown"`), a
divider, then the `LINEAR` nodes. `data-testid="flow-tab"` on the root.

### Conventions

Styling is co-located Panda **`css`/`cva`** imported from the **generated** `../../styled-system/css`
(token-keyed: `mint`/`amber`/`cyan`/`ink`/`muted`/`grid`/`bg`). `cva` variants encode the two
status colours (`swatch`, `connector`, `wire`) and the `junction` boolean (`rundownLine`). `Node`s
are keyed by `tool` in the maps; rundown lines by index.

### Invariants And Boundaries

- **Static spec, not a live read.** Unlike the other panels, it does NOT read the Zustand store or take
  props — `RUNDOWN`/`HEAD`/`LINEAR` are hardcoded. Its job is to mirror the regime model, so it must be
  kept in sync with `next_step.py` and the `lifecycle_start` rundown when either changes.
- **Does NOT render through `grammar/Panel`.** It owns its own scrolling `root` div (the route's
  "every panel renders through Panel" pattern does not apply here); it is full-bleed in the shell.
- The turn-end notification is **not a tool the agent calls** — it rides the gate tool (the `rides`
  field / amber left-bar nodes); the diagram must keep that framing.
- Tokens/styles come only from the generated `styled-system`; no global CSS, no hardcoded colours.
- Test/contract surface: `data-testid` `flow-tab`/`flow-node`/`flow-gate`/`flow-rundown` and
  `data-edge` on arrows are the stable hooks.

### Todos

None.

## Docs References

| Source | Relevance |
| --- | --- |

No relevant documentation found after checking live sources.

## Repo-Internal References

Wired as the `flow` cockpit View ("Lifecycle Flow", full-bleed) by `Cockpit.tsx`. The diagram is the
human-readable mirror of the next-step engine and of the rundown `lifecycle_start` emits.

| Finding | Source Path |
| --- | --- |
| Registers FlowTab as the `flow` View and renders it full-bleed. | [cockpit/Cockpit.tsx](agents-remember/dashboard/src/cockpit/Cockpit.tsx) |
| The next-step engine this panel is the spec for (regime model). | [tools/next_step.py](agents-remember/mcp/src/agents_remember/mcp/tools/next_step.py) |
| The single choke point that attaches `nextStep` to every in-lifecycle response. | [tools/base.py](agents-remember/mcp/src/agents_remember/mcp/tools/base.py) |
| `lifecycle_start`, which emits the front-half prose rundown. | [tools/lifecycle.py](agents-remember/mcp/src/agents_remember/mcp/tools/lifecycle.py) |
| Generated Panda `css`/`cva` this panel styles with. | [styled-system/css](agents-remember/dashboard/styled-system/css/index.mjs) |

## Cross-Repo References

No meaningful cross-repo references found.

## Update History

- 2026-06-27T18:43+02:00 — Added for task 26: new `FlowTab.tsx`, the "Lifecycle Flow" cockpit View —
  a static two-regime diagram (`RUNDOWN` front-half prose + `HEAD`/`LINEAR` node chains) that is the
  human-readable spec the task-27 `next_step.py` engine matches; mint edges = wired today, amber
  dashed = this leaf-26/27 series. Verification metadata pinned until closeout stamps the code commit.
