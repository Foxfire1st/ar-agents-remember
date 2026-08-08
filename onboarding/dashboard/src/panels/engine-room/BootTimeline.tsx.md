# dashboard/src/panels/engine-room/BootTimeline.tsx

| Field                  | Value                                                  |
| ---------------------- | ------------------------------------------------------ |
| repository             | agents-remember                                        |
| path                   | `dashboard/src/panels/engine-room/BootTimeline.tsx`    |
| doc_type               | `file-level-onboarding`                                |
| lastUpdated            | 2026-06-27T23:08+02:00                                  |
| lastVerifiedCommitHash | `1c1629fc97dd4daf352cf9b3529d210be167d2af`             |
| lastVerifiedCommitDate | 2026-08-08T22:29:45+02:00|
| governingOverview      | `overview.md`                                          |

## Governing Overview

[engine-room overview](overview.md)

## Purpose

Presentational sidebar for the slice 5e enclosure-centered Engine Room process map. Given one `EngineProcessNode`, it derives an ordered step list and per-step state, then renders them as a vertical `<ol>` timeline. The timeline runs in three modes (slice 5k F2/F4, refined in 05o): a **boot sequence** for the spin-up arc (contract anchor -> code worktree -> memory worktree/ledger -> CGC seed -> GrepAI clone -> watchers/steady state), a **steady state** label over the same completed boot checklist for a live fully-booted worktree, and a **tear-down sequence** during the landing/teardown arc (closeout -> push -> PR -> pull -> carryover -> cleanup -> retire). It reads the same projection facts (`edges`, `health`, `providers`, worktree `exists` flags, and the `landing[]` ref progression) as the map so the timeline and the map never disagree.

## Code Commentary

### Logic

`bootSteps(node)` builds the boot `Step[]` in fixed boot order (05o dev directive): a `complete` "Contract anchor" LEADS the list — the task contract is the precondition the worktree is created from, so it heads the sequence before any worktree materialises — then "Code worktree" (state from `materialized(node.codeWorktree.exists)`), then a memory step that branches on `node.memoryMode` — `external` shows the ledger-map/memory-worktree step (`materialized(node.memoryWorktree?.exists)`) while non-external modes show a `skipped` `Memory (<mode>)` row. It then appends a "CGC seed" step, an external-only "GrepAI clone" step, and a final "Watchers · steady state" step. The two edge-derived steps use the local `edge(kind)` helper, which finds the matching `node.edges` entry by `kind` and maps its `state` through `EDGE_TO_STEP` (defaulting to `pending`). `steadyState(node)` collapses `node.health` plus non-missing provider facts into the terminal step state — `complete`/`nominal` health only reads `complete` when at least one provider has `factState !== "missing"`, otherwise `pending`.

Mode selection (slice 5k F2/F4): `DISPOSE_PHASES` is the set of landing/teardown phases (`closeout-pending`, `integration-pending`, `carryover-pending`, `cleanup-pending`, `abandoned`). `BootTimeline` sets `disposing = DISPOSE_PHASES.has(node.phase)` and renders `teardownSteps(node)` instead of `bootSteps(node)` while disposing. Using the boot checklist during teardown read backwards (items reverting to "pending"), so the dispose path shows a forward-moving tear-down checklist. `teardownSteps(node)` is a fixed seven-step list — closeout · code → ledger, push → origin/feat, PR · merge, pull → main, carryover → mem-main, cleanup · de-materialise, retire branches — and `disposeFrontier(node)` returns the single ACTIVE step index `f`; each step is `complete` when `f > i`, `running` when `f === i`, else `pending`. `disposeFrontier` reads the SAME `node.landing[]` ref progression the canvas flows use (`origin-feat` resolved → `pr` merged → `origin-mem-main` pushed), so the panel's "running" row and the canvas's cyan flow always agree; `abandoned` short-circuits to retire (6) and `cleanup-pending` to cleanup (5). `carryoverDoneAt` is not yet on the TS projection (a deferred 5k-render item), so the carryover step reads the `origin-mem-main` ref instead.

05o review fixes refine the right-panel sequence in three ways. First, the header is now a THREE-WAY label: `STEADY_PHASES` (`sync-needed`/`running`/`nominal`/`completed`/`live`) marks a live, fully-booted worktree — e.g. T12B live-sync, where `origin/mem-main` moved while the worktree keeps working — so it renders the same completed boot checklist under a "Steady state" label (`data-mode="steady"`), distinct from "Boot sequence" (still booting) and "Tear-down sequence" (disposing). `BootTimeline` computes `disposing` first, then `steady = !disposing && STEADY_PHASES.has(node.phase)`, and resolves `mode`/`label` to one of the three. Second, `DISPOSE_PHASES` gained `integration-blocked` (T14C), so a terminal integration conflict reads "Tear-down sequence" rather than reverting to boot. Third, `teardownSteps(node)` special-cases two terminal phases via its `at(i)` helper: a `conflict` (`integration-blocked`) marks "Closeout · code → ledger" `complete` and the "Push → origin/feat" step `blocked` (the replay onto the feat/fix source hit an all-or-nothing conflict, the arc stops there, no auto-recovery), with the rest `pending`; an `abandoned` worktree marks the BYPASSED landing steps (closeout/push/PR/pull/carryover, indices ≤4) `skipped` and only "Cleanup · de-materialise" and "Retire branches" `complete`, because an abandon does no landing — diagnostics read "abandoned without integration — no landing". Otherwise the standard `disposeFrontier`-driven `complete`/`running`/`pending` progression applies.

The `BootTimeline({ node })` component maps the selected steps to `<li>` rows styled by `timelineStep`/`timelineMark` recipes (state-keyed), labeling each with `STATE_LABEL[step.state]`. The header reads "Tear-down sequence" while disposing, "Steady state" for a live fully-booted worktree in `STEADY_PHASES`, else "Boot sequence", and a `data-mode` attribute (`"teardown"`/`"steady"`/`"boot"`) is set on the timeline root.

### Invariants And Boundaries

- Pure derivation + render: no hooks, no fetch, no side effects; all state comes from the passed `EngineProcessNode`.
- `EDGE_TO_STEP` is the single edge-state -> step-state contract (e.g. `stale`/`failed` -> `failed`, `planned`/`unknown` -> `pending`); unknown edge states fall back to `pending` via `??`.
- The memory-worktree and GrepAI-clone steps appear only when `node.memoryMode === "external"`; otherwise memory is rendered as a `skipped` placeholder and the clone step is omitted entirely.
- Mode is chosen solely by phase: `node.phase ∈ DISPOSE_PHASES` → tear-down; else `∈ STEADY_PHASES` → steady-state label over the completed boot checklist; else boot. The modes share the same `Step[]`/render path and never mix rows.
- `integration-blocked` (T14C) and `abandoned` (T18) are terminal tear-down phases: a conflict reads closeout `done` + push `blocked` (no auto-recovery), and an abandon reads the bypassed landing steps `skipped` (only cleanup/retire `done`) — neither ever reads those steps as "done".
- The tear-down checklist always moves forward (`complete` → `running` → `pending`); it never reverts boot rows to "pending". `disposeFrontier` is the single source of the active index and must stay aligned with the canvas's `landing[]`-driven flow ordering.
- Step order is positional/fixed in both `bootSteps` and `teardownSteps`; `<li>` keys use `step.label`, so step labels must stay unique within a node.
- `data-testid="boot-timeline"`, the `data-mode` attribute (`boot`/`steady`/`teardown`), and per-row `data-state` are the stable hooks for tests/visual verification.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Consumes the `EngineProcessNode` projection shape (`edges`, `health`, `providers`, `memoryMode`, `codeWorktree`/`memoryWorktree`). | "export interface EngineProcessNode {"; "function steadyState(node: EngineProcessNode): StepState {"; "node.health === \"failed\""; "node.providers.some"; "function bootSteps(node: EngineProcessNode): Step[] {"; "node.edges.find"; "node.codeWorktree.exists"; "Memory (${node.memoryMode})" | dashboard/src/panels/engine-room/BootTimeline.tsx:46-47; dashboard/src/panels/engine-room/BootTimeline.tsx:51-51; dashboard/src/panels/engine-room/BootTimeline.tsx:56-56; dashboard/src/panels/engine-room/BootTimeline.tsx:58-58; dashboard/src/panels/engine-room/BootTimeline.tsx:66-66; dashboard/src/panels/engine-room/BootTimeline.tsx:74-74; dashboard/src/types/projection.ts:172-172 |
| `EngineProcessEdge.state` is mapped through the known `EDGE_TO_STEP` values. | `EngineProcessEdge`; `EDGE_TO_STEP`; "node.edges.find"; "EDGE_TO_STEP[found.state] ?? \"pending\"" | dashboard/src/panels/engine-room/BootTimeline.tsx:20-30; dashboard/src/panels/engine-room/BootTimeline.tsx:58-59; dashboard/src/types/projection.ts:162-170 |
| `DISPOSE_PHASES`, `disposeFrontier(node)`, and `teardownSteps(node)` drive tear-down mode. | `DISPOSE_PHASES`; `disposeFrontier`; `teardownSteps` | dashboard/src/panels/engine-room/BootTimeline.tsx:86-93; dashboard/src/panels/engine-room/BootTimeline.tsx:99-112; dashboard/src/panels/engine-room/BootTimeline.tsx:114-148 |
| `timeline`, `timelineStep`, `timelineMark`, and `sectionLabel` are the state-keyed timeline style recipes declared here. | `timeline`; `timelineStep`; `timelineMark`; `sectionLabel` | dashboard/src/panels/engine-room/layout.styles.ts:482-482; dashboard/src/panels/engine-room/styles.ts:3-3; mcp/src/agents_remember/serving/harness_control_ipc.py:47-47; dashboard/src/panels/engine-room/BootTimeline.tsx:3-3; dashboard/src/panels/EngineRoom.tsx:39-39 |

## Update History
- 2026-08-08T23:15+02:00 — 260713-TES-L1 completion round 3 (curator): body refreshed for the supervisor -> agent-notifier rename (citation ranges and/or rename wording); verification metadata pinned until closeout stamps the 260713-TES-L1 commit.

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: reviewed this sidecar against the frontend-rail change set (strict-target lint remediation: complexity, max-lines-per-function, react-hooks, jsx-a11y, and import-cycle fixes). No content impact: behavior-preserving refactor; the file's responsibilities and the claims in this card remain current. Verification metadata stays pinned until closeout stamps the code commit.

- 2026-08-04T11:43:39+02:00 — 260731-EFA-L6 S18-B03 curator: rebound projection, edge-state mapping, teardown,
  and styling references to exact anchors; corrected the edge-state claim to the source's string model
  and narrowed styling to the cited recipe declarations.

- 2026-06-27T23:08+02:00 — Task 31 provider-state honesty: steady-state completion now ignores missing provider placeholders, so an enclosure with only expected-but-unobserved providers does not read as fully booted. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-22T16:00 — Slice 05o right-panel review fixes. (a) "Contract anchor" now LEADS the boot sequence (the task contract is the precondition the worktree is created from), moved ahead of "Code worktree" and the ledger-map/memory step. (b) Three-way header via the new `STEADY_PHASES` set (`sync-needed`/`running`/`nominal`/`completed`/`live`): a live fully-booted worktree (e.g. T12B live-sync) renders "Steady state" (`data-mode="steady"`) over the completed boot checklist, distinct from "Boot sequence" and "Tear-down sequence". (c) `DISPOSE_PHASES` gained `integration-blocked` (T14C) so a terminal integration conflict reads "Tear-down sequence". (d) `teardownSteps` special-cases two terminal phases: a conflict (`integration-blocked`) marks closeout `complete` + the push/integrate step `blocked`; an abandon (`abandoned`) marks the bypassed landing steps (closeout/push/PR/pull/carryover) `skipped` and only cleanup/retire `complete`, because an abandon does no landing. Verification metadata pinned until closeout stamps the 05o code commit.
- 2026-06-21T23:35 — Slice 5k F2/F4: documented the new tear-down mode. `DISPOSE_PHASES` (closeout/integration/carryover/cleanup-pending + abandoned) switches the timeline to a forward-moving seven-step dispose checklist (`teardownSteps`) instead of reverting boot rows to "pending"; `disposeFrontier` reads the same `node.landing[]` ref progression as the canvas flows so the running row and the cyan flow agree; header becomes "Tear-down sequence" and a `data-mode` attribute is set. Added the dispose-path reference row.
- 2026-06-15T19:35 — Created for slice 5e: derives the ordered boot-sequence steps + states from an EngineProcessNode. Verification metadata pinned until closeout stamps the 5e code commit.
