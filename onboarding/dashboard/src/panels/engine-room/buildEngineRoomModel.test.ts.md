# dashboard/src/panels/engine-room/buildEngineRoomModel.test.ts

## Governing Overview

[engine-room overview](overview.md)

## Purpose

Vitest suite pinning the pure `buildEngineRoomModel` builder for the enclosure-centered Engine Room process map. It locks the behaviors that keep the client seam inference-free: joining each server-composed process node to its live lifecycle by `lifecycleId`, exposing the lifecycle gate, lifting workspace-scoped providers into `workspaceEngines`, falling back to legacy per-worktree stacks only when worktree providers exist but no process nodes do, sorting active leaf enclosures ahead of cleanup/retired siblings, and (slice 5f S0) exposing `enclosureKey = worktreeGroup` stably across a fleeting→real id swap. Local `node`/`lifecycle`/`worktreeEngine` factories build minimal fixtures so each case isolates one rule.

## Code Commentary

### Logic

No exports; one `describe("buildEngineRoomModel")` block with five `it` cases plus three fixture factories.

- `node(over)` returns a minimal `EngineProcessNode` (defaults `derived` code source, `external` memory, empty edges/providers/landing, `worktreeGroup: "/w/r/grp"`) merged with overrides; the `landing: []` default (slice 5h) satisfies the new required `EngineProcessNode.landing` field, and the `ledgerRows: []` / `ledgerRowCount: 0` defaults (5h ledger popover) satisfy the new required ledger fields; `lifecycle(over)` builds a `LifecycleProjection` requiring only `id`; `worktreeEngine(id, group)` builds a worktree-scoped `ProviderNode`, tagging `role: "memory"` when `id` contains `memory`/`grepai`.
- "attaches each process to its lifecycle by lifecycleId" feeds one node with `lifecycleId: "L1"` and a matching lifecycle, asserting `processes[0].lifecycle.id === "L1"` and `usesFallback === false`.
- "exposes the lifecycle gate on the process view" feeds a matching lifecycle with `gate.kind` and asserts
  `processes[0].gate` carries it.
- "lifts workspace-scoped providers into workspaceEngines" passes a `scope: "workspace"` provider and asserts it surfaces in `workspaceEngines`.
- "falls back to groupEngines when worktree providers exist but no engineProcesses" asserts `usesFallback === true`, one `fallbackStacks` entry, zero `processes`; the converse case (a process present) asserts no fallback.
- "exposes worktreeGroup as the enclosure key" builds two models from nodes with different `id`s (`start:demo` vs `/contract.md`) but the same `worktreeGroup`, asserting both yield `enclosureKey === "/w/r/grp"` — the morph-identity invariant.
- "orders active leaf enclosures before cleanup-pending siblings for the same parent task" builds two sibling leaves with phases `worktree-started` and `cleanup-pending`, asserting the active leaf appears first.

### Invariants And Boundaries

- Pure-unit only: imports `buildEngineRoomModel` and the projection types; no React, clock, network, or filesystem.
- Fixtures stay minimal and intentional — every default in `node` exists to satisfy the type, not to drive assertions; widen overrides rather than the defaults.
- The fallback rule is mutually exclusive: `usesFallback` is true only when `engineProcesses.length === 0` and worktree stacks exist; the "does not fall back" case guards against regressing that AND.
- The `enclosureKey` case pins that identity tracks `worktreeGroup`, not the node `id`.

## Evidence

### Repo-Internal References

- `buildEngineRoomModel` under test [1]
- `node`/`lifecycle`/`worktreeEngine` fixture factories [2]
- Lifecycle join + workspace lift + fallback cases [3]
- `enclosureKey` = worktreeGroup stable-across-id-swap case [4]
- EngineProcessNode is the generated projection contract consumed by this surface. [5]
- LifecycleProjection is the generated projection contract consumed by this surface. [6]
- ProviderNode is the generated projection contract consumed by this surface. [7]

## Series-Contract Notes

The stable-key regression uses a real-node id ending in `series-contract.md`, preserving the invariant that process identity comes from `worktreeGroup` rather than the contract file path.
