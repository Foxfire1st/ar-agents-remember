# dashboard/src/panels/engine-room/buildEngineRoomModel.test.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/engine-room/buildEngineRoomModel.test.ts` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-06-24T08:09+02:00                           |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`       |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `overview.md`                                    |

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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| `buildEngineRoomModel` under test | `buildEngineRoomModel` | dashboard/src/panels/engine-room/buildEngineRoomModel.ts:33-66 |
| `node`/`lifecycle`/`worktreeEngine` fixture factories | `node`; `lifecycle`; `worktreeEngine` | dashboard/src/panels/engine-room/buildEngineRoomModel.test.ts:10-42; dashboard/src/panels/engine-room/buildEngineRoomModel.test.ts:44-58; dashboard/src/panels/engine-room/buildEngineRoomModel.test.ts:60-69 |
| Lifecycle join + workspace lift + fallback cases | `buildEngineRoomModel`; `workspaceEngines`; `fallbackStacks`; `usesFallback` | dashboard/src/panels/engine-room/buildEngineRoomModel.ts:33-66; dashboard/src/panels/engine-room/buildEngineRoomModel.ts:39-39; dashboard/src/panels/engine-room/buildEngineRoomModel.ts:59-59; dashboard/src/panels/engine-room/buildEngineRoomModel.ts:63-63 |
| `enclosureKey` = worktreeGroup stable-across-id-swap case | `enclosureKey` | dashboard/src/panels/engine-room/buildEngineRoomModel.test.ts:132-134 |
| `EngineProcessNode`, `LifecycleProjection`, `ProviderNode` fixture types | `EngineProcessNode`; `LifecycleProjection`; `ProviderNode` | dashboard/src/types/projection.ts:176-216; dashboard/src/types/projection.ts:288-306; dashboard/src/types/projection.ts:355-366 |

## Series-Contract Notes

The stable-key regression uses a real-node id ending in `series-contract.md`, preserving the invariant that process identity comes from `worktreeGroup` rather than the contract file path.

## Update History
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-03T09:35+02:00 — 260731-EFA-L6 W3-B07 curator: repaired 6 citation findings (3 missing anchors and 3 malformed sources) in the three assigned repository-reference rows; all anchors and ranges were resolved against the frozen source index.

## Update History

- 2026-06-24T08:09+02:00 — Engine Room leaf identity: added a model-level regression for active leaf ordering ahead of cleanup-pending siblings and seeded the helper with `leafId`. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: the stable-enclosure-key regression now uses a `/series-contract.md` real-node id, matching the new leaf enclosure contract path. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-23T13:45+02:00 — Task 11: added a case pinning `EngineProcessView.gate` from the joined
  lifecycle. Verification metadata pinned until closeout stamps the task-11 code commit.
- 2026-06-18T18:00+02:00 — slice 5h ledger popover: the `node` fixture factory adds the `ledgerRows: []` / `ledgerRowCount: 0` defaults to satisfy the new required `EngineProcessNode` ledger fields. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-18T08:51+02:00 — slice 5h H1: the `node` fixture factory adds the `landing: []` default to satisfy the new required `EngineProcessNode.landing` field. Verification metadata pinned until closeout stamps the 5h code commit.
- 2026-06-16T01:55 — slice 5f S0: added a fifth case pinning `enclosureKey === worktreeGroup` stable
  across a fleeting→real id swap. Verification metadata pinned until closeout stamps the S0 code commit.
- 2026-06-15T19:35 — Created for slice 5e: vitest for the pure model builder (lifecycle join, workspace lift, fallback). Verification metadata pinned until closeout stamps the 5e code commit.
