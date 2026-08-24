# mcp/src/agents_remember/observer/projection.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/observer/projection.py` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-08-24T15:04+02:00 |
| lastVerifiedCommitHash | `f95487ec993b58d34911bba0206a7fa6ef9684eb` |
| lastVerifiedCommitDate | 2026-08-24T15:28:18+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[observer overview](overview.md)

## Purpose

Defines the canonical workspace projection models. It now carries structural task-document references
on task-aware analytics while preserving runtime ids only as observation/correlation.

## Code Commentary

L23 adds optional `lifecycleOperation` state to `EnclosureNode`; the browser receives task-addressed operation progress without internal operation identity.

### Logic

Task, expectation, pickup, and attention projections can expose `TaskDocumentRef` so the dashboard
joins the same real sprint/master/leaf hierarchy used by routing. `TaskDocNode` remains the
JSON-primary task view; lifecycle attachment is optional. Since 260815-DAG-L11 the sprint graph
projection is leaf-segmented: `TaskExecutionNode` (kind `master` lump or `segment` + `leafIds`)
and `TaskExecutionEndpointNode` (ref + optional segment-sampling `leafId`) mirror the persisted
schema, with before-validators lifting legacy bare refs into the uniform served shape;
`TaskExecutionEdgeNode` carries the optional `judgmentId`, and `TaskDocNode.executionWaves` derives
over execution nodes. The observer does not choose current seat occupants or authorize relations. Since
260815-DAG-L14 the task projection also carries first-class sprint structure:
`TaskSubTaskRefNode.masterRef` (the typed commanded-master link — the dashboard opens that
document directly; `None` for ordinary leaf rows and legacy slug-only rows) and `TaskSeatNode`
(role/label/identity/state, `extra="forbid"`, mirroring `tasks.document.SprintSeat`), projected
from `TaskDocument.seats`; `TaskDocNode.seats` defaults to empty so non-sprint docs are untouched.

### Conventions

The Python schema is the source for generated TypeScript and JSON schema artifacts.

### Invariants And Boundaries

- Projected task references identify work, not runtime occupants.
- Projection remains read-only evidence and cannot become routing authority.
- Generated dashboard types must be synchronized with this schema.

### Todos

None.

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Pickup and expectation analytics carry structural references. | `AgentPickupNode` | mcp/src/agents_remember/observer/projection.py:392-431 |
| Task documents remain the real projected hierarchy. | `TaskDocNode` | mcp/src/agents_remember/observer/projection.py:739-812 |
| The leaf-segmented graph projection (lump/segment nodes and sampling endpoints). | `TaskExecutionNode`; `TaskExecutionEndpointNode` | mcp/src/agents_remember/observer/projection.py:639-658; mcp/src/agents_remember/observer/projection.py:661-677 |
| Workspace projection is the schema authority consumed by generation. | `WorkspaceProjection` | mcp/src/agents_remember/observer/projection.py:1131-1153 |

## Cross-Repo References

No cross-repository implementation dependency governs this file.

## L23 Engine Process Lineage

`EngineProcessNode` now carries the optional strict source-lineage projection.
The observer exposes resolved admission facts to operations; it does not compare
branches or synthesize recovery locally.

## L23 Lifecycle Model Package Review

Observer projection now imports `LifecycleOperationProjection` from
`models.lifecycles.operation`. Engine-process composition and the task-derived source-lineage
projection remain unchanged; this is an ownership-only model move.


## 260815-DAG-L12 Render-Ready Graph View

`TaskDocNode` gains the optional `executionGraphView` field (L12-R4): the render-ready per-node sprint graph (`observer/projection_graph.TaskExecutionGraphView`) the dashboard renders directly — node kind, master ref + title, leaf ids + titles, derived wave index, mechanically derived frontier state, execution nature, and predecessors with reasons. The field is `None` for documents without a graph (backward compatible); the dashboard never joins raw refs or re-derives waves.


## 260821-CLIVE Disposable Queue And Discard History Projection

Closeout nodes now expose service condition, source classification/fingerprint/problems, and exact
waiting-generation members with classification, effective priority, order, and reasons. Candidate
lifecycle state, active blocker, grade mutation, and commit/certification fields are removed.
Task/master and series nodes also expose typed discarded-unstarted history and counts; `None`
distinguishes a non-master from a master with an empty audit. The shared discard node/proof models
come from the dedicated closeout projection module.

## Update History

- 2026-08-24T15:04+02:00 — Cumulative CLIVE curation: reconciled projection models with waiting-only closeout state and audited discarded task history. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.


- 2026-08-20T10:45+02:00 — 260815-DAG-L12:   `TaskDocNode` gains the optional render-ready `executionGraphView` field (L12-R4). Verified at code commit b7f2c8e2.

- 2026-08-20T04:24+02:00 — 260815-DAG-L14: `TaskSubTaskRefNode` gains the typed `masterRef`
  (commanded-master link), `TaskDocNode` gains `seats` (`TaskSeatNode`, `extra="forbid"`), and the
  served shape mirrors `tasks.document.SprintSeat`. Verified at code commit 9c3180c1.


- 2026-08-19T08:55+02:00 — 260815-DAG-L11: added `TaskExecutionNode` / `TaskExecutionEndpointNode`
  (with bare-ref lifting before-validators); `TaskExecutionEdgeNode` endpoints are now endpoint
  nodes with an optional `judgmentId`, `TaskExecutionGraphNode.nodes` carries execution nodes, and
  `TaskDocNode.executionWaves` derives over them; dashboard types are regenerated from this schema.
  Verification remains closeout-owned.

- 2026-08-18T13:00+02:00 — No content impact: 260815-DAG-L8 added the closeout-queue projection surface (closeoutQueues); the behavior this card describes is unchanged.

- 2026-08-15T02:16:50+02:00 — 260815-DAG-L1: TaskDocNode now projects declared execution nature,
  persisted reasoned graph data, and mechanically derived waves using strict graph DTOs.

- 2026-08-13T09:05+02:00 — L23 curator: reviewed the lifecycle projection import move and recorded
  its no-impact boundary; final provenance remains closeout-owned.
- 2026-08-12T20:10+02:00 — L23 curator: recorded source-lineage evidence on Engine Process nodes; verification remains closeout-owned.

- 2026-08-12T15:56+02:00 — 260731-EFA-L23 curator body review: reconciled this card with the exact current source delta described above; verification provenance remains closeout-owned.
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.
- 2026-08-04T16:28:49+02:00 — 260731-EFA-L6 S18-B11 same-reviewer residual correction: rebound reducer consumption, mirror contract, event envelope, and `ACTIVE_STATES` assignment to operative spans, and extended the series-token row with explicit anchors for the per-reference loop and the token summation body. Verification metadata unchanged.
- 2026-08-01T10:45+02:00 — 260731-EFA-L4 curator (post-wave source change): corrected the mirror partition narrative to the current `LIVE_STATES`, `TERMINAL_STATES`, `LIFECYCLE_STATES`, and `ACTIVE_STATES` source contract cit:([`LIVE_STATES`, `TERMINAL_STATES`, `LIFECYCLE_STATES`, `ACTIVE_STATES`], dashboard/src/types/projection.ts:9-9; dashboard/src/types/projection.ts:11-11; dashboard/src/types/projection.ts:13-13; dashboard/src/types/projection.ts:21-21). The local explanation and reference table were then rechecked against the current sources cit:(["STATE OF THE MIRROR"], mcp/src/agents_remember/observer/projection.py:223-223) cit:([`project_workspace`], mcp/src/agents_remember/observer/reducer.py:128-181) cit:([`check_state_partition`], mcp/src/agents_remember/observer/lifecycle_state.py:73-98) cit:([`### 2.5 The observer and its projections`], docs/design/observable-lifecycle.md:241-251) cit:([`## 7. Design Principles Preserved`], docs/design/observable-lifecycle.md:363-390).
- 2026-08-01T10:45+02:00 — 260731-EFA-L4 curator (post-wave source change): corrected the mirror partition narrative to the current `LIVE_STATES`, `TERMINAL_STATES`, `LIFECYCLE_STATES`, and `ACTIVE_STATES` source contract cit:([`LIVE_STATES`, `TERMINAL_STATES`, `LIFECYCLE_STATES`, `ACTIVE_STATES`], dashboard/src/types/projection.ts:9-9; dashboard/src/types/projection.ts:11-11; dashboard/src/types/projection.ts:13-13; dashboard/src/types/projection.ts:21-21). The local explanation and reference table were then rechecked against the current sources cit:(["STATE OF THE MIRROR"], mcp/src/agents_remember/observer/projection.py:223-223) cit:([`project_workspace`], mcp/src/agents_remember/observer/reducer.py:128-181) cit:([`check_state_partition`], mcp/src/agents_remember/observer/lifecycle_state.py:73-98) cit:([`### 2.5 The observer and its projections`], docs/design/observable-lifecycle.md:241-251) cit:([`## 7. Design Principles Preserved`], docs/design/observable-lifecycle.md:363-390).
- 2026-08-01T00:35+02:00 — 260731-EFA-L4 curator: documented the vocabulary-derived metrics map, the `awaitingDeveloperCount` bucket, and the collision refusal in the current source cit:([`ACTIVE_STATES`, `state_count_field`, `state_count_fields`, `STATE_COUNT_FIELDS`, `awaitingDeveloperCount`], mcp/src/agents_remember/observer/projection.py:242-242; mcp/src/agents_remember/observer/projection.py:245-260; mcp/src/agents_remember/observer/projection.py:263-285; mcp/src/agents_remember/observer/projection.py:288-288; mcp/src/agents_remember/observer/projection.py:317-317). The focused projection tests and reducer-side `_metrics` path remain the behavioral evidence cit:(["class MetricsBucketVocabularyTests(unittest.TestCase):", "class StateCountFieldTests(unittest.TestCase):", "def _metrics("], mcp/tests/test_observer_projection_metrics.py:128-128; mcp/tests/test_observer_projection_metrics.py:461-461; mcp/src/agents_remember/observer/reducer_impl/_metrics.py:27-27; mcp/tests/test_observer_projection_metrics.py:128-233; mcp/tests/test_observer_projection_metrics.py:461-516).
- 2026-08-01T00:35+02:00 — 260731-EFA-L4 curator: documented the vocabulary-derived metrics map, the `awaitingDeveloperCount` bucket, and the collision refusal in the current source cit:([`ACTIVE_STATES`, `state_count_field`, `state_count_fields`, `STATE_COUNT_FIELDS`, `awaitingDeveloperCount`], mcp/src/agents_remember/observer/projection.py:242-242; mcp/src/agents_remember/observer/projection.py:245-260; mcp/src/agents_remember/observer/projection.py:263-285; mcp/src/agents_remember/observer/projection.py:288-288; mcp/src/agents_remember/observer/projection.py:317-317). The focused projection tests and reducer-side `_metrics` path remain the behavioral evidence cit:(["class MetricsBucketVocabularyTests(unittest.TestCase):", "class StateCountFieldTests(unittest.TestCase):", "def _metrics("], mcp/tests/test_observer_projection_metrics.py:128-128; mcp/tests/test_observer_projection_metrics.py:461-461; mcp/src/agents_remember/observer/reducer_impl/_metrics.py:27-27; mcp/tests/test_observer_projection_metrics.py:128-233; mcp/tests/test_observer_projection_metrics.py:461-516).
- 2026-07-31T16:35+02:00 — No content impact: the only change to
  `mcp/src/agents_remember/observer/projection.py` since the L2 base commit is the whole-tree
  `ruff format` pass in `00e8379`, which re-wrapped 4 line(s) with no token change whatsoever.
  Checked by parsing both revisions and comparing the abstract syntax trees (identical) and the
  comment tokens (identical), so no symbol, signature, default, decorator, control-flow branch,
  docstring, or assertion this card describes has moved, and every claim this card makes about its
  own source still holds.
- 2026-07-31T00:00+02:00 — 260731-EFA-L2 attestation: this file was touched ONLY by the
  whole-tree `ruff format` pass (commit `00e8379`) — line reflow, no behaviour, contract,
  structure or responsibility change. The sidecar was re-read against the current source and
  every claim in it still holds, so it was deliberately not rewritten. Verification metadata
  pinned until closeout stamps the L2 commit.
- 2026-07-12T17:30+02:00 — 260712-TRH-L7: projection reads the latest exact-contract landing snapshot and preserves additive freshness fields without performing remote work in the recurring tick.

- 2026-07-10T01:14+02:00 — 260707-HFX2-L13 F6: converted the broadcast `TaskDocNode` contract to a
  body-free summary with a body-revision digest and retained the payload-budget measurement as a
  zero-body regression guard. Verification metadata remains pinned until closeout stamps the
  eventual L13 code commit.

- 2026-07-09T19:31+02:00 — 260707-HFX2-L12: documented the CS-6 scaling/reclamation change for this file. Verification metadata pinned until closeout stamps the HFX2-L12 commit.
- 2026-07-08T14:35+02:00 — 260707-HFX2-L1: `AgentPickupNode` gained the R1 ack/backoff fields (`attemptCount`/`lastAttemptAt`/`nextAttemptAt`/`escalatedAt`) and R4 owner fields (`ownerRole`/`ownerAgentId`/`ownerLifecycleId`); added `ExpectationRowNode` + `Analytics.expectationRows` (R5 projection surfacing). Verification metadata pinned until closeout stamps the 260707-HFX2-L1 commit.
- 2026-07-06T23:58:00+02:00 — 260703-L14 (visual hierarchy + chat grouping): `TaskDocNode` gains
  additive `orchestrates: list[str]` (default `[]`) — the orchestration-command relation from the
  `ar-task-document/v1` schema, exposed so the dashboard can nest commanded masters under their
  orchestration task. No `version` bump.
  Verification metadata pinned until closeout stamps the L14 commit.
- 2026-07-06T02:05+02:00 — 260703-L11: `EnclosureNode` gains additive
  `codeWorktreeExists`/`memoryWorktreeExists` (default `False`) — worktree-existence
  truth stat'ed at snapshot time in the I/O layer, the tasks surface's visibility
  rule (existence over cleanup-proxy). Documented `cleanup: reopened` as
  contract-reset-awaiting-restart, not live work. Verification metadata pinned
  until closeout stamps the L11 commit.
- 2026-07-04T12:32+02:00 — 260703-L4: `GateNode` now carries additive
  `evidenceRefs` from the gate record so delegated approvals can surface
  reviewer verdict artifacts in the projection. Verification metadata pinned
  until closeout stamps the L4 commit.
- 2026-07-04T12:31+02:00 - L3: `AgentPickupNode` gained role/message/artifact
  and hosted-delivery metadata so the dashboard projection can display durable
  agent-to-agent inbox state. Verification metadata pinned until closeout stamps
  the L3 commit.
- 2026-06-28T07:32+02:00 — Task 29 S7 follow-up: `DriftSnapshotNode` now carries optional
  `checkedAt`, `sourceRoot`, `memoryRoot`, and `reportPath` provenance used by actionable-drift queue
  detail and targetless dismissal freshness. Verification metadata pinned until closeout stamps the
  task-29 code commit.
- 2026-06-28T07:30+02:00 — Task 33: added `WorkspaceProjection.activeWorktreeGroups: list[str]` (default
  empty) — the bounded active worktree-group basename set the Topology constellation filters on, sourced
  from `active_enclosure_worktree_groups` (shared with the Engine Room). Additive, no `version` bump.
  Verification metadata pinned until closeout stamps the code commit.
- 2026-06-28T03:52+02:00 — Task 28 S5.2 after source sync: documented
  `LifecycleProjection.stateEnteredAt` and `AttentionItem.signalTs` as the current-occurrence anchors
  for lifecycle-scoped attention acknowledgements. Verification metadata pinned until closeout stamps
  the task-28 code commit.
- 2026-06-27T23:08+02:00 — Task 31 provider-state honesty: documented `ProviderBootNode.runtimeState="missing"` for expected worktree provider slots with no observed runtime fact. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-26T20:18+02:00 — Task 21 series token rollup: `SeriesNode` now carries additive
  `seriesTokenTotal`, a reducer-composed aggregate of linked leaf lifecycle tokens for the master reader.
  Verification metadata pinned until closeout stamps the code commit.
- 2026-06-25T13:10+02:00 — Task 23/24: added `AgentPickupNode`, `Analytics.agentPickups`, and `AttentionItem.gateId` for backend-backed pickup feedback and targeted gate clearing.

- 2026-06-24T18:11+02:00 — Task 17 live-data numbering: `TaskDocNode` now carries required `id` from the
  JSON-primary task document so clients can render authored leaf numbers without trusting parent
  `subTasks[].number` label strings. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-24T16:33+02:00 — Task 17 task-document-first projection: `TaskDocNode.lifecycleId` is now
  optional runtime attachment, active master/leaf/light JSON docs can project before lifecycle binding,
  and `SeriesNode.createdAt` mirrors master creation order. Verification metadata pinned until closeout
  stamps the code commit.
- 2026-06-24T12:21+02:00 — Task 17 served contract: `TaskDocNode` now carries `createdAt`, series
  sub-task rows expose optional leaf `createdAt`, and `SeriesNode` carries the master `objective` so the
  dashboard can render master content and default leaf order from structured data. Verification metadata
  pinned until closeout stamps the code commit.
- 2026-06-24T08:59+02:00 — Task-document correction: clarified that `TaskDocNode` is sourced from
  JSON-primary `ar-task-document/v1` docs, not leaf `series-contract.md`; `sections` may carry
  non-master freeform task-doc sections, but never contract content. Verification metadata
  pinned until closeout stamps the code commit.
- 2026-06-24T08:09+02:00 — Engine Room leaf identity: `EngineProcessNode` now carries `leafId` beside parent `taskName`, allowing dashboard enclosures to render the active leaf/worktree name without losing the containing series task context. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: `EnclosureNode` now carries `enclosureId`, `leafId`, and `taskRoot` so the observer can project leaf identity and root task location separately. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-23T22:09+02:00 — Task 12 S2 correction: clarified that workspace `repoId` coverage may come
  from GrepAI `targetRepos` as well as CGC watcher rows. Verification metadata will be stamped at
  closeout.
- 2026-06-23T21:46+02:00 — Task 12 S2: clarified `ProviderNode` semantics so workspace providers may
  be aggregate or repo-covered via `repoId` when backend state has per-repo evidence, while
  `worktreeGroup` remains the stronger enclosure join for isolated worktree providers. Verification
  metadata pinned until closeout stamps the S2 code commit.
- 2026-06-21T06:40+02:00 — slice 05m (carryover-before-cleanup): `EngineProcessNode` gained the additive `carryoverDoneAt: str | None = None` — the carryover milestone ISO time (the parked memory carried into official memory, read off the official ledger by `guidance.carryover_done`, surfaced through `status_payload`); `None` until carried, display-only (5k renders the seam). The `phase` field comment gained `carryover-pending` (between `integration-blocked` and `cleanup-pending`). Both additive, so prior fixtures + the live feed are unchanged. Verification metadata pinned until closeout stamps the 05m code commit.
- 2026-06-21T05:30+02:00 — slice 5l P2 (landing-arc probe hardening): `LandingRefNode` gained `at: str | None = None` — gh's PR milestone timestamp (`mergedAt` once merged, else `createdAt`; `None` for branch refs). Additive + display-only (the frontend renders it in 05k); the reducer's `LandingRefNode(**ref)` splat picks it up from the `worktrees/modules/landing.py` probe with no reducer change. Verification metadata pinned until closeout stamps the 05l-P2 code commit.
- 2026-06-21T02:44+02:00 — Slice 6g (dashboard master/sub-task navigation): added `TaskSubTaskRefNode` (+`linkedLifecycleId`) and `TaskSectionNode`; `TaskDocNode` gained `subTasks`/`sections` (a master's series index + ordered render plan) and `masterLifecycleId` (parent-series link for the breadcrumb). Additive, no `version` bump. Verification metadata pinned until closeout stamps the 6g code commit.
- 2026-06-19T03:17+02:00 — slice 3c reopened (R1, masters observable): added `SeriesSubTaskNode` / `SeriesSectionNode` / `SeriesNode` (the series-master surface, folder-keyed — a full reader carrying subTasks + sections + decisions + `doneCount`/`totalCount` over the master's declared `subTasks[]`) and the additive `Analytics.series` field. Later Task 17 reworked master docs to also project as concrete `TaskDocNode`s. Verification metadata pinned until closeout stamps the R1 code commit.
- 2026-06-18T21:25+02:00 — slice 5h Tier 2: `LedgerRefNode` gained four optional fields — `codeSubject` / `codeDate` / `memorySubject` / `memoryDate` (the per-side commit message + committer ISO date for the popover's 6 columns). Additive + `exclude_none`, so the wire is unchanged when a side isn't probed (honest hash-only fallback, never faked). Verification metadata pinned until closeout stamps the code commit.
- 2026-06-18T18:00+02:00 — slice 5h ledger popover (both couplers): added `LedgerRefNode` + `LEDGER_WINDOW=25`; `EngineProcessNode` gained `ledgerRows`/`ledgerRowCount` (worktree coupler) and `LedgerNode` gained `rows` (official coupler — `closeoutCount` stays the full total); `EngineProcessFacts` carries `ledger_rows`/`ledger_row_count` so the window is read in the I/O layer and the reducer stays pure. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-18T14:05+02:00 — Task 6 slice 6c Part A: added `GateNode` + `LifecycleProjection.gate` (the durable gate materialized onto a lifecycle for the dashboard's review surface; distinct from the `ask` proto-gate). Append-only, no `version` bump. Verification metadata pinned until closeout stamps the 6c Part A code commit.
- 2026-06-18T08:51+02:00 — slice 5h H1: added `LandingRefNode` (remote/PR landing participant with a `factState` honesty axis) + additive `landing[]` / `integrationStrategy` on `EngineProcessNode` (default-empty → G1–G5 fixtures + the live feed unchanged); the live `landing[]` is observed best-effort in `worktrees/modules/landing.py` and composed by the reducer. Verification metadata pinned until closeout stamps the 5h code commit.
- 2026-06-15T19:35 — slice 5e: slice 5e: new CommitRefNode/ProviderBootNode/EngineProcessEdge/EngineProcessNode models + EngineProcessFacts carrier; Analytics.engineProcesses; WorkspaceProjection.version 1->2.
- 2026-06-14T23:30+02:00: Slice 05 (5c) — `ProviderNode` gained `scope`/`role`/`repoId`/`worktreeGroup` (per-worktree provider binding); added `TaskStepNode`/`TaskSubStepNode`/`TaskDecisionNode`/`TaskCodeExampleNode` and the `TaskDocNode` content fields (`steps`/`objective`/`requirements`/`design`/`codeExamples`/`decisions`/`openQuestions`/`references`) so the dashboard reads the full task content. Verification metadata pinned until closeout stamps the 5c code commit.
- 2026-06-14T16:58+02:00: Slice 05 (5b) — added `AttentionItem` and the derived `Analytics.attentionQueue` (the home-screen attention queue, computed server-side by the reducer; the one analytics field derived from the structural tree rather than read from an input file). Verification metadata pinned until closeout stamps the 5b code commit.
- 2026-06-13T22:34: Slice 3c commit 2 — added `TaskDocNode` and the `Analytics.taskDocuments` field (surface 7): a task document's per-lifecycle step/substep progress, read from the JSON-primary doc. Verification metadata pinned until closeout stamps the 3c commit-2 code commit.
- 2026-06-13T20:48+02:00: Slice 3b — added the analytical nodes
  (`DriftSnapshotNode`/`SidecarStaleNode`/`SetupSummaryNode`/`SetupProgressNode`/
  `RouteCoverageNode`/`ToolReportNode`/`LedgerNode`) + the `Analytics` container,
  per-lifecycle `tokenSeries` (`TokenSample`), and `Metrics.stalenessHistogram`.
  The served document stays lean (counts + bounded leaderboards, not raw
  inventories). Verification metadata is pinned until closeout stamps the 3b code
  commit.
- 2026-06-13T19:30+02:00: Created for slice 3a — the projection schema
  (lifecycle/enclosure/provider nodes, metrics, action availability, workspace
  tree). Verification metadata is pinned until closeout stamps the 3a code commit.
