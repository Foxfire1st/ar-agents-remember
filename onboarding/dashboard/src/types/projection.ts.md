# dashboard/src/types/projection.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/types/projection.ts`              |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-09-04T20:19:44+02:00 |
| lastVerifiedCommitHash | `e375f2ebdc87f6843bc76168b646d606fa79caec` |
| lastVerifiedCommitDate | 2026-09-04T20:19:44+02:00 |
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[dashboard/src/ overview](../overview.md)

## Purpose

Generated TypeScript mirror of the served workspace projection plus its enumerable runtime
vocabularies. It carries canonical `TaskDocumentRef` values on task-aware analytics without
turning runtime session/lifecycle ids into work identity. Since 260831-CCR (commit `99dc249b`)
it also mirrors the canonical `TaskIntentIdentity` wire shape (`task-intent/v1` schema + 64-hex
digest) and attaches it optionally to the lifecycle operation projection.

## Code Commentary

### Logic

The generator emits lifecycle, task, attention, engine, and metrics wire shapes together with checked
state vocabularies. Structural additions share one `TaskDocumentRef` interface. Task documents
remain the hierarchy authority; lifecycle and hosted-occupant fields are optional runtime
attachments.

`LifecycleOperationProjection` gains the optional `taskIntent?: TaskIntentIdentity` (line 349),
and the new `TaskIntentIdentity` interface (line 687-693) mirrors the JSON Schema refinements:
the required 64-hex `digest` and the closed `schema: "task-intent/v1"` union.

### Conventions

This file is generated from the Python projection schemas; edit the model/generator and resynchronize
rather than hand-maintaining parallel declarations.

### Invariants And Boundaries

- The task-document reference is repository-qualified and level-explicit.
- Runtime ids remain projections/correlation, not structural seat identity.
- Generated TypeScript and schema artifacts must remain synchronized.
- The task-intent identity is observation-only: the dashboard never mints or mutates a digest.

### Todos

None.

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Structural analytics fields use the shared task-document reference. | `TaskDocumentRef` | dashboard/src/types/projection.ts:699-702 |
| Generated task documents carry real hierarchy and optional runtime attachment. | `TaskDocNode` | dashboard/src/types/projection.ts:648-682 |
| Execution nodes name their kind, leaf-id segment and task reference. | "export interface TaskExecutionNode {" | dashboard/src/types/projection.ts:725-729 |
| An execution endpoint carries a task reference and optional leaf id. | "export interface TaskExecutionEndpointNode {" | dashboard/src/types/projection.ts:711-714 |
| Execution edges bind predecessor and successor endpoints with a reason and optional judgment id. | "export interface TaskExecutionEdgeNode {" | dashboard/src/types/projection.ts:704-709 |
| The graph contains typed node and edge arrays. | "export interface TaskExecutionGraphNode {" | dashboard/src/types/projection.ts:716-719 |
| Workspace projection remains the generated top-level wire contract. | `WorkspaceProjection` | dashboard/src/types/projection.ts:817-830 |
| The optional canonical task-intent identity on lifecycle operations. | `taskIntent` | dashboard/src/types/projection.ts:362-362 |
| The generated `task-intent/v1` identity interface. | `TaskIntentIdentity` | dashboard/src/types/projection.ts:751-755 |

## Cross-Repo References

No cross-repository implementation dependency governs this file.

## L23 Source-Lineage Mirror

The frontend projection declares strict edge, recovery, and aggregate lineage
shapes and attaches the aggregate optionally to each Engine Process. Its closed
relations, sides, states, and `worktree_sync` tool mirror the server model; the
dashboard does not accept an open-ended string vocabulary here.

## 260815-DAG-L4 Projection Contract

The L4 delta keeps the generated dashboard contract aligned with the backend's organizational `super-to-leaf` lineage and lifecycle-operation guidance. The dashboard remains a projection consumer: it does not gain branch-mutation authority.


## 260815-DAG-L12 Render-Ready Graph View Types

The generated mirror gains the render-ready sprint graph wire shapes (L12-R4): `TaskExecutionGraphView` (nodes), `TaskExecutionNodeView` (kind `lump`/`segment`, masterRef + masterTitle, leafIds + leafTitles, waveIndex, frontierState, optional executionNature, predecessors), and `TaskExecutionPredecessorNode` (predecessorRef + predecessorTitle + reason + optional judgmentId); `TaskDocNode` gains the optional `executionGraphView` field. Regenerated by `scripts/sync-projection-types.py`.


## 260821-CLIVE-L2 Lifecycle Operation Projection Contract

The generated TypeScript mirror now carries optional lifecycle-operation `generation`, the
`direct-landing` kind, required opaque `legalControls`, and the termination-required/unreadable
status vocabulary. These fields describe root-journal-owned operation state to dashboard consumers;
they do not make the dashboard or disposable closeout projection an operation authority.

| Finding | Anchor | Source |
| --- | --- | --- |
| The lifecycle operation wire type keeps generation optional, controls opaque, and kind/status vocabularies closed. | `LifecycleOperationProjection` | dashboard/src/types/projection.ts:331-349 |

## 260821-CLIVE Disposable Queue And Discard Audit Mirror

The generated mirror removes `AtomicBlockerNode` and the old mutable queue candidate fields.
`CloseoutQueueNode` now exposes exact-current service/source condition, bounded problems, and
generation-keyed `CloseoutProjectionMemberNode` rows; member classification is the closed
`ready | waiting | blocked` display vocabulary. These interfaces describe a disposable producer view
only and transfer no scheduling or operation authority to the browser.

`DiscardUnstartedProofNode` and `DiscardedSubTaskNode` expose audited discard-before-start evidence.
Required series and optional task-document discard count/history fields remain distinct from live
subtasks and completed progress. Supported runtime-only schema constraints are emitted immediately
above their TypeScript properties as stable `JSON Schema refinements` comments, including nested item
constraints; TypeScript shape alone is not runtime validation.

## 260824-PDLS Invalidation Outcome Mirror

`ProjectionInvalidationResult.outcome` no longer includes `not-created`. The producer always
materializes invalid-empty state when invalidating a projection, so dashboard consumers receive an
explicit non-admitting result rather than interpreting file absence as lifecycle or queue evidence.

## ARSPAWN-L4 Serving-Build Mirror

The generated `ServingBuild` interface now includes optional `sourceDigest`, `pythonExecutable`, and
`packageRoot` beside the existing version, boot, checkout, dashboard, and dirtiness fields. These
are serve-time diagnostic facts, not persisted projection authority. They let dashboard and MCP
evidence distinguish equal-version candidates and name the runtime that actually answered.

## 260831-CCR-R02 Task-Intent Mirror

The generated mirror adds the `TaskIntentIdentity` interface (closed `task-intent/v1` schema plus
64-hex digest) and attaches it optionally to `LifecycleOperationProjection`. Dashboard consumers
observe the exact identity a door/journal/operation binds; no intent authority transfers to the
browser.

## 260831-CCR-L15 Meaningful Revision Wire Field

The generated `LifecycleOperationProjection` interface gains the optional
`meaningfulRevision?: number` field (JSON Schema refinement `minimum: 1`), the
dashboard mirror of the durable CCR-R15 wait cursor that the lifecycle status-change wait tool
returns on snapshots.

## Update History

- 2026-09-05T07:19:22+00:00 — L31-MR-02 history recovery: restored the original dated L18 entry verbatim from memory commit fd41221f11dfe5ac2993520c0d7176ada59ce2ba (its recorded code provenance: f93ac631ca161e5880db3a937728cb256686b13b). This preserves sibling curation history; current body and verification metadata are unchanged.


- 2026-09-05T06:38:58+00:00 — CCR L31 dashboard citation curation: re-read the scoped claims against frozen source `ea35964985f30080488270e71ac81657ac40682b`, split pooled evidence and corrected current source boundaries. Historical claims retain their recorded provenance. This is scoped claim review; existing whole-file verification metadata is unchanged.
- 2026-09-05T06:24:16+00:00: Generated citation repair: `TaskDocumentRef` repointed to dashboard/src/types/projection.ts:699-702. No content impact: mechanical anchor-range projection bound to citation source snapshot ad34c1284f637cc2e60117d5a156ddfdd2236402d2c1332758dd691c2cbef881; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-05T06:24:16+00:00: Generated citation repair: `TaskDocNode` repointed to dashboard/src/types/projection.ts:648-682. No content impact: mechanical anchor-range projection bound to citation source snapshot ad34c1284f637cc2e60117d5a156ddfdd2236402d2c1332758dd691c2cbef881; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-05T06:24:16+00:00: Generated citation repair: `WorkspaceProjection` repointed to dashboard/src/types/projection.ts:817-830. No content impact: mechanical anchor-range projection bound to citation source snapshot ad34c1284f637cc2e60117d5a156ddfdd2236402d2c1332758dd691c2cbef881; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-05T06:24:16+00:00: Generated citation repair: `taskIntent` repointed to dashboard/src/types/projection.ts:362-362. No content impact: mechanical anchor-range projection bound to citation source snapshot ad34c1284f637cc2e60117d5a156ddfdd2236402d2c1332758dd691c2cbef881; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-05T06:24:16+00:00: Generated citation repair: `TaskIntentIdentity` repointed to dashboard/src/types/projection.ts:751-755. No content impact: mechanical anchor-range projection bound to citation source snapshot ad34c1284f637cc2e60117d5a156ddfdd2236402d2c1332758dd691c2cbef881; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-04T20:19:44+02:00 — 260831-CCR-L15 Gate-5 memory pass for e375f2ebdc87f6843bc76168b646d606fa79caec (lifecycle status-change waiting): recorded the optional `meaningfulRevision` field on the generated `LifecycleOperationProjection` interface.
- 2026-09-04T10:05+02:00 — 260831-CCR-L18 Gate-5 memory pass: recorded the regenerated lifecycle envelope types (schema/state-matrix versions, incoherent status, identity/componentBindings/worker/approval/recommendedAction cells). Verified at code commit f93ac631ca161e5880db3a937728cb256686b13b.

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for 99dc249bd507 (CCR-R02@v2/L25):
  regenerated-mirror card updated for the optional `LifecycleOperationProjection.taskIntent` and
  the new `TaskIntentIdentity` interface (closed `task-intent/v1` + digest pattern with JSON Schema
  refinements); documented the observation-only boundary. Verified at code commit 99dc249bd507c20b09ece1169c2b1fa2af8e8c1b.

- 2026-08-30T15:15:36+02:00 — Regenerated the serving-build mirror with source digest,
  interpreter, and package-root identity. Verification remains closeout-owned.

- 2026-08-25T17:21+02:00 — Regenerated the TypeScript invalidation outcome union without the
  impossible `not-created` member. Verification remains closeout-owned.

- 2026-08-24T15:04+02:00 — Regenerated and documented the disposable closeout projection,
  discard audit types, and deterministic runtime-refinement comments while preserving the newer
  lifecycle-operation/root-journal mirror.

- 2026-08-24T00:51+02:00 — 260821-CLIVE-L2: documented the generated lifecycle-operation TypeScript contract and its projection-only authority boundary. Verified at code commit `1d446724`.


- 2026-08-20T10:45+02:00 — 260815-DAG-L12:   generated mirror adds `TaskExecutionGraphView`/`TaskExecutionNodeView`/`TaskExecutionPredecessorNode` and `TaskDocNode.executionGraphView` (L12-R4). Verified at code commit b7f2c8e2.

- 2026-08-20T04:38+02:00 — 260815-DAG-L14: `TaskDocNode` gains `seats: TaskSeatNode[]` (new
  `TaskSeatNode` interface: role/label/state + optional identity), `TaskSubTaskRefNode` gains the
  optional typed `masterRef: TaskDocumentRef`, and the schema mirrors both. Regenerated by
  `scripts/sync-projection-types.py`; verified at code commit 9c3180c1.


- 2026-08-19T08:55+02:00 — 260815-DAG-L11: regenerated types add `TaskExecutionNode` /
  `TaskExecutionEndpointNode`, `TaskExecutionEdgeNode.judgmentId`, and node-typed
  `executionWaves` — the leaf-segmented sprint graph surface. Verification remains closeout-owned.

- 2026-08-18T13:00+02:00 — No content impact: 260815-DAG-L8 added the closeout-queue projection surface (closeoutQueues); the behavior this card describes is unchanged.

- 2026-08-15T23:38+02:00 — Reconciled projection parity for organizational direct-super lineage and lifecycle guidance. Verification metadata remains closeout-owned.

- 2026-08-15T02:16:50+02:00 — 260815-DAG-L1: regenerated TaskDocNode types now expose optional
  execution nature/graph and required mechanically derived waves without scheduler judgment.
- 2026-08-12T20:10+02:00 — L23 curator: documented the strict dashboard lineage mirror; verification remains closeout-owned.
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-11T19:58+02:00 — Aligned the current data-contract card for `projection.ts` with task-document identity, qualified seat state, and terminal projections represented by this source.
- 2026-08-08T22:10+02:00 — 260713-TES-L1 completion round (curator): refreshed this sidecar body for the supervisor -> agent-notifier rename (module paths, identifiers, settings keys, wire keys, prose) and the compat seams; verification metadata pinned until closeout stamps the 260713-TES-L1 commit.
- 2026-08-04T13:01:29+02:00 — 260731-EFA-L6 S18-B04 — same-reviewer semantic correction: reconciled generated projection citations against the frozen source, removed unsupported or duplicate claims, and regenerated scoped citation ranges.

- 2026-08-03T23:26:43+02:00 — 260731-EFA-L6 S18-T3: rewrote the live card for generated
  provenance. Removed the deferred-codegen/`LATE MIRROR` contract, made schema-required fields
  explicit, and stopped attributing historical rationale or diagnostic commentary to generated
  source. New or rewritten source bindings are resolved by the scoped citation fixer.

- 2026-08-01T10:45+02:00 — 260731-EFA-L4 curator: reconciled the state-partition rewrite,
  compile-time uniqueness guard, runtime duplicate coverage, and moved reference ranges against
  the landed source. Corrected stale claims and contradictory counts; verification metadata remains
  pinned until closeout.

- 2026-08-01T09:05+02:00 — 260731-EFA-L4 curator: body corrected against the landed diff. Removed the
  false claim that this is a pure type module (it now exports eight vocabulary tuples plus
  `stateCountField`/`metricsFor`); removed the false `TaskSubTaskRefNode.createdAt` claim from Purpose,
  Logic and the citation table (the field moved to the new `SeriesSubTaskNode`); rewrote the slice-05o
  paragraph, which described `refusedPolarity` and a `refused` edge state as live wire signals — both
  were mirror inventions with no Python model behind them and are now REMOVED. Added the L4 subsection
  (tuple-first vocabularies, derived `Metrics` buckets, the reconciled camel rule, the two un-collapsed
  model pairs, `LATE MIRROR`, `LandingRefNode.at?` / `EngineProcessNode.carryoverDoneAt?` /
  `ExpectationRowNode`) and six invariants. Recorded three limits rather than flattening them: the
  terminal/live split is NOT a composed partition on this side (`projection.py` L199-L217 says so and
  names the fix), `SeriesSectionNode` is a slot and not a check, and the mirror-to-server link is held by
  no test because `snapshot.json` is hand-maintained. Re-derived all 12 pre-existing citations — every
  range had moved (e.g. `WorkspaceProjection` L389-L397 to L674-L689, `EngineProcessNode` L332-L373 to
  L566-L608, `ProcessFactState`/`ProcessHealth` L269-L287 to L487-L519) — and added 17 more. Verification
  metadata pinned to the leaf base until closeout stamps the L4 code commit.

- 2026-07-24T13:17:50Z — Documented optional dirty serving-build evidence and comment-only cleanup.
  Verification hash/date remain pinned to the pre-commit source stamp.

- 2026-07-18T12:43+02:00 — FEUI-L9R: recorded the optional app-injected dashboard fingerprint and
  its unknown-on-absence boundary; verification metadata remains pinned pending closeout.
- 2026-07-17T23:54+02:00 — 260715-FEUI-L7 mirrored optional pickup owner identity and
  redelivery/escalation timestamps/counts. Optionality preserves pre-field persisted projections;
  consumers must not synthesize missing facts. Verification metadata remains pinned to the leaf
  base until closeout.
- 2026-07-12T17:30+02:00 — 260712-TRH-L7: kept the projection wire contract in lockstep by typing stale landing facts and observed/attempt/age freshness fields.

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
- 2026-06-22T11:00 — slice 05o refused-conduit signal: added a `refused` member to the `EngineProcessEdge.state` union plus an optional `refusedPolarity?: "amber" | "red"` field (amber = a soft reroute/fallback, red = a fault/conflict), the projection signal that drives the new refused-conduit flash (T9B red, T9C amber, T14C red); lockstep with projection.py (`?` = the server's `exclude_none` omission). Verification metadata pinned until closeout stamps the 05o code commit.
- 2026-06-21T02:44+02:00 — Slice 6g: mirrored the master-navigation additions from `projection.py` — `TaskSubTaskRefNode` (+`linkedLifecycleId?`), `TaskSectionNode`, and `subTasks`/`sections`/`masterLifecycleId?` on `TaskDocNode`. Verification metadata pinned until closeout stamps the 6g code commit.
- 2026-06-19T06:39+02:00 — engine-room crash fix: relaxed `EngineProcessNode.landing` to optional (`landing?`) — a pre-5h/persisted projection omits it, and `EnclosureCanvas` was crashing on `node.landing.find`. Forward-compat, not an `exclude_none` change. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-18T21:25+02:00 — slice 5h Tier 2: mirrored the four optional `LedgerRefNode` fields `codeSubject?`/`codeDate?`/`memorySubject?`/`memoryDate?` (lockstep with projection.py; `?` = the server's `exclude_none` omission). Verification metadata pinned until closeout stamps the code commit.
- 2026-06-18T18:00+02:00 — slice 5h ledger popover: mirrored `LedgerRefNode` + `LedgerNode.rows` + `EngineProcessNode.ledgerRows`/`ledgerRowCount` (lockstep with projection.py). Verification metadata pinned until closeout stamps the code commit.
- 2026-06-18T14:05 — Task 6 slice 6c Part A: mirrored `GateNode` + the optional `LifecycleProjection.gate` from `projection.py`. Verification metadata pinned until closeout stamps the 6c Part A code commit.
- 2026-06-18T08:51+02:00 — slice 5h H1: mirrored `LandingRefNode` + the additive `landing[]` / `integrationStrategy?` fields on `EngineProcessNode` (lockstep with projection.py). Verification metadata pinned until closeout stamps the 5h code commit.
- 2026-06-15T19:35 — Created for slice 5e: TS mirror of the served projection contract; slice 5e adds CommitRefNode/ProviderBootNode/EngineProcessEdge/EngineProcessNode + ProcessFactState/ProcessHealth + Analytics.engineProcesses. Verification metadata pinned until closeout stamps the 5e code commit.
