# dashboard/src/types/projection.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/types/projection.ts`              |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-10T01:14+02:00                           |
| lastVerifiedCommitHash | `e400ed0ce98752d1b65d00de97c9b84c7ea20814`       |
| lastVerifiedCommitDate | 2026-07-10T20:04:45+02:00|
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[dashboard/src/ overview](../overview.md)

## Purpose

Hand-maintained TypeScript mirror of the served projection contract (`mcp/.../observer/projection.py`, the source of truth — D7: pydantic codegen deferred). camelCase matches the wire form, and because the server dumps with `exclude_none=True`, every `T | None` server field is modelled as optional (`?:`). Slice 5e extends the contract with the enclosure-centered Engine Room process map: `CommitRefNode` / `ProviderBootNode` / `EngineProcessEdge` / `EngineProcessNode`, the `ProcessFactState` / `ProcessHealth` honesty enums, and the `Analytics.engineProcesses` derived surface. Slice 6g mirrors the master-navigation additions: `TaskSubTaskRefNode` (with `linkedLifecycleId` and optional `createdAt`), `TaskSectionNode`, and `subTasks` / `sections` / `masterLifecycleId` on `TaskDocNode`. Task 17 makes `TaskDocNode.lifecycleId?` optional because runtime lifecycle state is attachment, not the condition for projecting a JSON-primary task document; planning-only leaves and masters can be listed/read before a worktree exists. Task 17 also mirrors `TaskDocNode.id`, the JSON-primary task id used as the authored leaf display number when parent sub-task refs are only fallback rows. The masters surface is still also exposed as `Analytics.series: SeriesNode[]`, carrying folder-keyed master content with `createdAt`, `objective`, sections, decisions, sub-task creation metadata for default oldest-first ordering, and `seriesTokenTotal` for the server-composed leaf-lifecycle token aggregate.

## Code Commentary

### 260707-HFX2-L13 Task-Body Revision

`TaskDocNode.bodyRevision?` mirrors the server-generated digest of reader-body fields omitted from
the always-on summary. It is optional for compatibility with persisted/older projections. The detail
reader combines it with `docPath` as the on-demand body cache key; summary fields such as identity,
status, progress, steps, sub-task links, and routing metadata remain in the broadcast contract.

### Logic

Pure type module (no runtime values). The top-level shape is `WorkspaceProjection`: `version`, `generatedAt`, `lifecycles: LifecycleProjection[]`, `enclosures: EnclosureNode[]`, `providers: ProviderNode[]`, `activeWorktreeGroups: string[]` (required — the worktree-group basenames with a live enclosure lifecycle; the bounded set the Topology filters on, join key = worktree `ProviderNode.worktreeGroup` / basename of `EnclosureNode.worktreeGroup`; always present because the server default is a list, never `exclude_none`-dropped), `metrics: Metrics`, and `analytics: Analytics`. Core nodes — `LifecycleProjection` (state/phase/tokens + `stateEnteredAt`, `tokenSeries`, `actions`), `EnclosureNode`, `ProviderNode` (with `scope` workspace|worktree, `role` code|memory, optional `repoId`, and optional `worktreeGroup`), `Metrics`, plus the analytics children (`DriftSnapshotNode`, `SidecarStaleNode`, `SetupSummaryNode`, `SetupProgressNode`, `RouteCoverageNode`, `ToolReportNode`, `LedgerNode`, the `TaskDocNode` tree, and the reducer-derived `AttentionItem`). Slice 6c adds `GateNode` and the optional `LifecycleProjection.gate` — the durable gate the cockpit reviews (`decisions` = the verbs an open gate can POST). The unions `State` and `Phase` enumerate lifecycle status.

Slice 5e adds the engine-room process map. `ProcessFactState` (`observed` | `derived` | `planned` | `missing` | `not-applicable`) is the honesty axis and `ProcessHealth` (`nominal` | `running` | `blocked` | `failed` | `stale` | `skipped` | `unknown` | `complete`) the rollup. `CommitRefNode` describes one checkout (branch/commit/path, `exists`, `dirty`, `behindSource`, `factState`); `ProviderBootNode` describes a per-process provider boot (id/role/`runtimeState`/`factState`) and includes `runtimeState="missing"` for expected provider slots whose runtime facts were not observed; `EngineProcessEdge` is a setup-step edge (`fromNode`/`toNode`/`kind`/`state`/`label`). `EngineProcessNode` is the enclosure pod keyed by the contract path (`id` == `EnclosureNode.enclosure`): code/memory source-vs-worktree `CommitRefNode`s, `memoryMode`, ledger + review/closeout/integration/cleanup status, setup phase fields, its `providers`/`edges`/`actions`, `missingFacts` / `sourceFiles`, and the two series-contract identities (`taskName` for the parent series task, `leafId` for the concrete leaf worktree/enclosure). `Analytics.engineProcesses: EngineProcessNode[]` carries the whole derived surface. Slice 5h adds the successful-landing arc mirror: `LandingRefNode` (`kind`/`label`/`state` + the `ProcessFactState` honesty axis + optional `detail`) and two additive `EngineProcessNode` fields — `landing?: LandingRefNode[]` (optional — a pre-5h/persisted projection omits it; a list is never dropped by `exclude_none`, so this `?:` encodes schema evolution, not the omission rule) and optional `integrationStrategy` — kept in lockstep with the `projection.py` source of truth. The 5h coupler popover then mirrors `LedgerRefNode` (`codeCommit`/`memoryCommit`), `LedgerNode.rows` (the official coupler's served window; `closeoutCount` stays the full total), and `EngineProcessNode.ledgerRows`/`ledgerRowCount` (the worktree coupler's window). **5h Tier 2** adds four optional fields to `LedgerRefNode` — `codeSubject?`/`codeDate?`/`memorySubject?`/`memoryDate?` (the per-side commit message + committer ISO date for the popover's 6 columns) — modelled `?:` to mirror the source model's `exclude_none` omission. **Slice 05o** adds the refused-conduit signal to `EngineProcessEdge`: a new `refused` member in the `state` string union plus an optional `refusedPolarity?: "amber" | "red"` field — `amber` flags a soft reroute/fallback (CGC seed → reindex), `red` a fault/conflict (GrepAI seed fault, integration conflict). It is carried only on an explicit `refused`-state edge; a `failed`/`stale` seed/integration edge derives its polarity in the renderer. This is the projection signal that drives the new refused-conduit flash (T9B red, T9C amber, T14C red), kept in lockstep with the `projection.py` source of truth (`?:` = the server's `exclude_none` omission).

Slice 6g extends `TaskDocNode` for navigation/content: `subTasks: TaskSubTaskRefNode[]` — a master's series-index row (`number`/`name`/`file`/`status`/`scope` + optional `createdAt` and `linkedLifecycleId`, set when `file` points at another master, the cross-series "→" jump target) — and `sections: TaskSectionNode[]` — ordered task-document sections (`kind`/`heading`/`body`). `TaskDocNode.id` mirrors the JSON-primary document `id` and is the clean task-specific display number for authored leaf rows; `subTasks[].number` remains a parent-row fallback for unauthored rows. `TaskDocNode.createdAt?` exposes the JSON-primary task document creation time so leaf lists can default to creation order without parsing file names. Task 17 makes `TaskDocNode.lifecycleId?` optional; a missing lifecycle id means "planning/unbound task document", not "not readable." `subTasks` are master-only, while `sections` may also carry authored freeform sections on light/subTask docs; plus `masterLifecycleId?`, the parent master's lifecycle (the "↑ parent" link). 260703-L14 adds `TaskDocNode.orchestrates?: string[]` — the orchestration-command relation (non-empty only on a master doc that IS an orchestration task; the master task names it commands, from which the dashboard derives the orchestration > master > leaf hierarchy). It mirrors a list-default server field (always dumped as `[]`), but is modelled `?:` deliberately so projections **persisted before L14** still parse — the same forward-compat exception as `landing?`, so consumers must guard (`doc.orchestrates ?? []`). `SeriesNode` mirrors folder-keyed masters in `Analytics.series`: it includes master `createdAt`, `objective`, subTasks, done/total counts, `seriesTokenTotal`, sections, decisions, `docPath`, and optional age. Task 23/24/L3 mirrors `AttentionItem.gateId?` for deletion actions and `AgentPickupNode` / `Analytics.agentPickups?` for task-row waiting-for-agent/check-chat feedback, now including sender/recipient role metadata, message kind, artifact path, and hosted-delivery state. Task 28 mirrors `AttentionItem.signalTs?`, the server-computed current-occurrence acknowledgement anchor for lifecycle-scoped dismissals. Task 29 adds `DriftSnapshotNode.checkedAt?`, `sourceRoot?`, `memoryRoot?`, and `reportPath?` so actionable-drift attention rows can identify the affected repo/memory/report and use `checkedAt` as a dismissible occurrence anchor. Optional fields mirror `exclude_none`.

### Invariants And Boundaries

- Type-only; emits no runtime values. `projection.py` is the source of truth — change it first, then mirror here in lockstep.
- Optional (`?:`) fields encode the server's `exclude_none=True` omission; never assume a `?:` field is present.
- `TaskDocNode.id` is required and comes from the JSON-primary task document id. Dashboard consumers use
  it for authored leaf display labels instead of parsing or trusting parent label strings.
- `TaskDocNode.lifecycleId?` is optional runtime binding. Consumers must not hide a task document merely
  because it has not been bound to a lifecycle/enclosure yet.
- `TaskDocNode.sections` means sections from the JSON task-document schema. It is not a projection path
  for `series-contract.md` content.
- `createdAt` is a structured ordering field supplied by the server. Consumers may sort by it when
  present, but must not derive creation order by parsing `number` or filename prefixes.
- `SeriesNode.seriesTokenTotal` is server-derived. Dashboard consumers display it; they do not recompute
  it from lifecycle gauges or task-doc rows.
- `landing?` is the exception (a list, never `exclude_none`-dropped): it is `?:` for **forward-compat** — a projection produced before slice 5h omits the field, so consumers must guard (`node.landing?.…`).
- `engineProcesses` and `attentionQueue` are derived surfaces composed server-side; the client renders them verbatim and preserves server order (no re-sort, no re-derivation).
- `AttentionItem.signalTs?` and `LifecycleProjection.stateEnteredAt` are server-computed lifecycle acknowledgement anchors. Clients forward ids/kinds only; they do not decide suppression freshness.
- `DriftSnapshotNode.checkedAt?` is the repo-level acknowledgement anchor for actionable drift; clients render/dismiss it but do not reclassify drift.
- `agentPickups` is also server-derived. Clients render the projected `waiting-for-agent` or `check-chat`
  state, role/message/delivery metadata, and do not run their own pickup TTL timers.
- `EngineProcessNode.id` is the stable enclosure id and the join key to `EnclosureNode.enclosure`; `ProviderNode.worktreeGroup` is the join key to the owning enclosure and takes precedence over `ProviderNode.repoId` in topology parenting.
- Ages (`*Seconds`) and fact-state are server-computed (never `Date.now()`); `nextAction` is display/copy-only until slice 06. Since 260703-L15 the served age fields are also *volatile* to the change gate (excluded from server diff + client merge equality — `data/servedAges.ts`), and displays advance them locally from arrival anchors.
- `servingBuild?` (260703-L15) is the ONE field NOT mirrored from `projection.py`: it is injected app-side (`serving/build_info.py` via `serving/app.py`) onto `/api/state` and the SSE snapshot only, so it is optional here and absent from persisted `latest-state.json` (a pre-L15 server also sends none).
- `supervisorHeartbeat?` (260707-HFX2-L2 R5, expanded by HFX2-L8 R6) is a SECOND app-injected, non-`projection.py` field,
  same posture as `servingBuild?`: `serving/supervisor_heartbeat.py` via `serving/app.py` attaches it
  onto `/api/state` and the SSE snapshot at RESPONSE time, deliberately excluded from the ETag
  change-gate revision (it is a live tick age, not stable content) — so `ageSeconds` can be stale
  relative to the header's cached revision until a real reconnect or another content change forces
  a fresh response. `lastTickAt: null` means the supervisor has never ticked in this workspace
  (opt-in autostart) — that is NOT `stale: true`, and consumers must not treat the two as
  equivalent. The L8 fields (`pendingInboxCount`, `redeliverableInboxCount`,
  `lastSweepDurationSeconds`) are forward storm-pressure signals, not projection-stable content.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Source of truth + `exclude_none` optional-field rule | L1-L5 | [projection.py](../../../../agents-remember/mcp/src/agents_remember/observer/projection.py) |
| `TaskSubTaskRefNode.createdAt`, `TaskDocNode.id`/`createdAt`, and `SeriesNode.seriesTokenTotal` mirror the served task/series identity, creation-order, and aggregate-token fields. | L196-L250 | [projection.ts](projection.ts) |
| `Analytics.series` carries the folder-keyed master aggregation surface alongside active task documents with optional lifecycle binding. | L375-L386 | [projection.ts](projection.ts) |
| `ProviderNode` comments mirror the served `repoId` and `worktreeGroup` binding semantics consumed by topology. | L76-L87 | [projection.ts](projection.ts) |
| `WorkspaceProjection` top-level shape | L389-L397 | [projection.ts](projection.ts) |
| `EngineProcessNode` enclosure pod (5e) | L332-L373 | [projection.ts](projection.ts) |
| `CommitRefNode` / `ProviderBootNode` / `EngineProcessEdge` (5e) | L289-L318 | [projection.ts](projection.ts) |
| `ProcessFactState` / `ProcessHealth` honesty enums (5e) | L269-L287 | [projection.ts](projection.ts) |
| Drift snapshot metadata mirrors the backend provenance fields used by actionable-drift rows. | L98-L108 | [projection.ts](projection.ts) |
| `AttentionItem.signalTs?` remains the server-computed current-occurrence anchor. | L260-L274 | [projection.ts](projection.ts) |
| `SupervisorHeartbeat` (`lastTickAt`/`ageSeconds`/`staleCutoffSeconds`/`stale` plus L8 backlog/duration fields) mirrors the app-injected wire shape `serving/app.py::_supervisor_heartbeat_payload` builds, not a `projection.py` model. | L435-L444 | [projection.ts](projection.ts) |
| The app-side payload builder this type mirrors. | `_supervisor_heartbeat_payload` | [../../../../agents-remember/mcp/src/agents_remember/serving/app.py](../../../../agents-remember/mcp/src/agents_remember/serving/app.py) |

## Series-Contract Notes

`EnclosureNode` separates leaf contract identity (`enclosureId` / `leafId`) from the containing `taskRoot`, which lets dashboard views handle root series tasks and leaf worktrees without deriving paths client-side. 260703-L11 adds the required `codeWorktreeExists` / `memoryWorktreeExists` booleans — the server-stat'ed worktree-existence truth (always on the wire: bool defaults are never `exclude_none`-dropped) that `hasLiveWorktree` filters tasks-surface visibility on, replacing every client-side cleanup-state proxy; `cleanup: reopened` means contract-reset-awaiting-restart, not live work.

## Update History

- 2026-07-10T01:14+02:00 — 260707-HFX2-L13 F6: added optional `TaskDocNode.bodyRevision`, the
  cache invalidation token for on-demand reader bodies omitted from the summary broadcast.
  Verification metadata remains pinned until closeout stamps the eventual L13 code commit.

- 2026-07-08T23:59+02:00 — 260707-HFX2-L8 (dead-seat storm observability, R6): extended
  `SupervisorHeartbeat` with `pendingInboxCount`, `redeliverableInboxCount`, and
  `lastSweepDurationSeconds`, matching the app-injected `/api/state` payload. Verification metadata
  pinned until closeout stamps the 260707-HFX2-L8 commit.
- 2026-07-08T18:45+02:00 — 260707-HFX2-L2 (supervisor sweep, R5): added `SupervisorHeartbeat`
  (`lastTickAt: string | null`, `ageSeconds: number | null`, `staleCutoffSeconds: number`,
  `stale: boolean`) and the optional `WorkspaceProjection.supervisorHeartbeat?` — a SECOND
  app-injected, non-`projection.py` field alongside `servingBuild?` (same posture: injected onto
  `/api/state`/the SSE snapshot only, excluded from the ETag revision, absent from persisted
  `latest-state.json`). `lastTickAt: null` (never ticked) is documented as distinct from
  `stale: true`. Verification metadata pinned until closeout stamps the 260707-HFX2-L2 commit.
- 2026-07-07T05:22+02:00 — 260703-L15 S3: added `ServingBuild` (`version`, `bootedAt`,
  `commit?`) and the optional `WorkspaceProjection.servingBuild?` — the app-injected boot-time
  serving stamp (NOT a `projection.py` mirror; wire-only, absent in persisted projections).
  Verification metadata pinned until closeout stamps the L15 commit.
- 2026-07-06T23:57:12+02:00 — 260703-L14 (visual hierarchy + chat grouping): mirrored
  `TaskDocNode.orchestrates?: string[]` — the orchestration-command relation from `projection.py`;
  optional for forward-compat with pre-L14 persisted projections (consumers guard with
  `?? []`). Verification metadata pinned until closeout stamps the L14 commit.
- 2026-07-06T03:00+02:00 — 260703-L11: mirrored the new required
  `EnclosureNode.codeWorktreeExists`/`memoryWorktreeExists` existence-truth flags (stat'ed server-side
  at snapshot time; the tasks-surface visibility rule). Verification metadata pinned until closeout
  stamps the L11 commit.
- 2026-07-04T12:31+02:00 - L3: mirrored the expanded `AgentPickupNode`
  metadata for agent-to-agent inbox delivery state. Verification metadata pinned
  until closeout stamps the L3 commit.
- 2026-06-28T07:32+02:00 — Task 29 S7 follow-up: mirrored drift snapshot provenance fields
  (`checkedAt`, `sourceRoot`, `memoryRoot`, `reportPath`) used for actionable-drift detail and targetless
  dismissal freshness. Verification metadata pinned until closeout stamps the task-29 code commit.
- 2026-06-28T07:30+02:00 — Task 33: mirrored the new required `WorkspaceProjection.activeWorktreeGroups:
  string[]` (the bounded active worktree-group set the Topology filters on; required because the server
  field is a list default, never `exclude_none`-dropped). Verification metadata pinned until closeout
  stamps the code commit.
- 2026-06-28T03:52+02:00 — Task 28 S5.2 after source sync: mirrored
  `LifecycleProjection.stateEnteredAt` / `AttentionItem.signalTs?` as the current-occurrence
  acknowledgement anchors for lifecycle-scoped attention dismissals. Verification metadata pinned until
  closeout stamps the task-28 code commit.
- 2026-06-27T23:08+02:00 — Task 31 provider-state honesty: mirrored `ProviderBootNode.runtimeState="missing"` for expected provider slots with no observed runtime fact. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-26T20:18+02:00 — Task 21 series token rollup: mirrored `SeriesNode.seriesTokenTotal`, the
  server-derived aggregate token count displayed by the master reader. Verification metadata pinned until
  closeout stamps the code commit.
- 2026-06-25T13:20+02:00 — Task 23/24: mirrored `AttentionItem.gateId`, `AgentPickupNode`, and `Analytics.agentPickups` for gate deletion actions and task-row pickup feedback.
- 2026-06-24T18:11+02:00 — Task 17 live-data numbering: mirrored required `TaskDocNode.id`, the
  JSON-primary task id used by dashboard labels for authored leaf rows. Verification metadata pinned
  until closeout stamps the code commit.
- 2026-06-24T16:33+02:00 — Task 17 task-document-first Operations: mirrored optional
  `TaskDocNode.lifecycleId?` and `SeriesNode.createdAt?` from the server projection so planning-only
  documents remain readable and master rows keep structured creation-order metadata. Verification
  metadata pinned until closeout stamps the code commit.
- 2026-06-24T12:21+02:00 — Task 17 projection mirror: added the optional `createdAt` ordering fields
  on task/sub-task rows, the folder-keyed `SeriesNode.objective`/master shape, and `Analytics.series`
  as the master reader surface consumed by `DetailPanel`. Verification metadata pinned until closeout
  stamps the code commit.
- 2026-06-24T08:59+02:00 — Task-document sections correction: clarified that
  `TaskDocNode.sections` mirrors JSON task-document sections, including non-master freeform sections,
  and does not carry `series-contract.md` content. Verification metadata pinned until closeout stamps
  the code commit.
- 2026-06-24T08:09+02:00 — Engine Room leaf identity: mirrored `EngineProcessNode.leafId` from the server projection so dashboard renderers can label concrete leaf enclosures separately from their parent `taskName`. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: `EnclosureNode` gained `enclosureId`, `leafId`, and `taskRoot` so dashboard views can distinguish root task folders, leaf enclosure contracts, and stable leaf identity. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-23T21:46+02:00 — Task 12 S2: clarified `ProviderNode.repoId` as covered-repo metadata for
  workspace providers and owning-repo metadata for worktree providers, with `worktreeGroup` documented as
  the precedence join key. Verification metadata pinned until closeout stamps the S2 code commit.
- 2026-06-22T11:00 — slice 05o refused-conduit signal: added a `refused` member to the `EngineProcessEdge.state` union plus an optional `refusedPolarity?: "amber" | "red"` field (amber = a soft reroute/fallback, red = a fault/conflict), the projection signal that drives the new refused-conduit flash (T9B red, T9C amber, T14C red); lockstep with projection.py (`?:` = the server's `exclude_none` omission). Verification metadata pinned until closeout stamps the 05o code commit.
- 2026-06-21T02:44+02:00 — Slice 6g: mirrored the master-navigation additions from `projection.py` — `TaskSubTaskRefNode` (+`linkedLifecycleId?`), `TaskSectionNode`, and `subTasks`/`sections`/`masterLifecycleId?` on `TaskDocNode`. Verification metadata pinned until closeout stamps the 6g code commit.
- 2026-06-19T06:39+02:00 — engine-room crash fix: relaxed `EngineProcessNode.landing` to optional (`landing?:`) — a pre-5h/persisted projection omits it, and `EnclosureCanvas` was crashing on `node.landing.find`. Forward-compat, not an `exclude_none` change. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-18T21:25+02:00 — slice 5h Tier 2: mirrored the four optional `LedgerRefNode` fields `codeSubject?`/`codeDate?`/`memorySubject?`/`memoryDate?` (lockstep with projection.py; `?:` = the server's `exclude_none` omission). Verification metadata pinned until closeout stamps the code commit.
- 2026-06-18T18:00+02:00 — slice 5h ledger popover: mirrored `LedgerRefNode` + `LedgerNode.rows` + `EngineProcessNode.ledgerRows`/`ledgerRowCount` (lockstep with projection.py). Verification metadata pinned until closeout stamps the code commit.
- 2026-06-18T14:05 — Task 6 slice 6c Part A: mirrored `GateNode` + the optional `LifecycleProjection.gate` from `projection.py`. Verification metadata pinned until closeout stamps the 6c Part A code commit.
- 2026-06-18T08:51+02:00 — slice 5h H1: mirrored `LandingRefNode` + the additive `landing[]` / `integrationStrategy?` fields on `EngineProcessNode` (lockstep with projection.py). Verification metadata pinned until closeout stamps the 5h code commit.
- 2026-06-15T19:35 — Created for slice 5e: TS mirror of the served projection contract; slice 5e adds CommitRefNode/ProviderBootNode/EngineProcessEdge/EngineProcessNode + ProcessFactState/ProcessHealth + Analytics.engineProcesses. Verification metadata pinned until closeout stamps the 5e code commit.
