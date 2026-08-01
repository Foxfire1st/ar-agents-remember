# mcp/src/agents_remember/observer/projection.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/observer/projection.py` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-01T10:45+02:00 |
| lastVerifiedCommitHash | `e52edaf5b655f495580efd93306afdf922b19b51`       |
| lastVerifiedCommitDate | 2026-08-01T11:01:51+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[observer overview](overview.md)

## Purpose

`projection.py` is the projection schema: the resolved-state contract the reducer
produces, written to `latest-state.json` / `latest-metrics.json` and (slice 04)
served over SSE (slice 3a). Slice 5e adds the Engine Room process map — the
enclosure-centered `EngineProcessNode` (+ `CommitRefNode`, `ProviderBootNode`,
`EngineProcessEdge`) and the `EngineProcessFacts` input carrier — and bumps the
served `WorkspaceProjection.version` from `1` to `2`.

## Code Commentary

### 260731-EFA-L4 Metrics buckets derived from the live vocabulary

This module now owns the map from lifecycle state to `Metrics` bucket field, and
derives it from `lifecycle_state`'s **live half** rather than from a hand-written
list.

- `ACTIVE_STATES: tuple[LiveState, ...] = LIVE_STATES` (L227) — the states
  `Metrics` buckets, the live half verbatim. It is deliberately **not** a set
  difference `STATES - TERMINAL_STATES`: a subtraction re-derives the answer from
  a second list that could be wrong, whereas the live half already *is* the
  answer. `lifecycleCount` counts every lifecycle and `totalTokens` sums every
  one, so what the per-state buckets add is the live workload — a
  `completed`/`abandoned` lifecycle is history, not work in flight.
- `state_count_field(state) -> str` (L230-L245) — the naming rule:
  `running` → `runningCount`, `awaiting-developer` → `awaitingDeveloperCount`.
  Each segment after the first has its **first character upper-cased and the rest
  left alone**; `str.capitalize` would lower-case the tail instead, which both
  disagrees with the TypeScript mirror (whose type-level `Capitalize<>` cannot
  lower-case a tail, so it renders `awaitingDEVELOPERCount`) and quietly merges
  states differing only in tail case.
- `state_count_fields(states) -> dict[str, str]` (L248-L270) — builds the map and
  **refuses one that is not one-to-one**, raising `LifecycleVocabularyError`
  naming both colliding states. The rule is not injective (`a-b` and `aB` both
  bucket into `aBCount`), and a collision does not announce itself: `Metrics` is
  keyed by field, so two states sharing a bucket means the later count silently
  overwrites the earlier.
- `STATE_COUNT_FIELDS: dict[str, str] = state_count_fields(ACTIVE_STATES)`
  (L273) — the one map the reducer's counting loop and the vocabulary-coverage
  tests both read instead of re-enumerating buckets.

**The bug this closed.** `awaiting-developer` had no bucket. `Metrics` declared
`runningCount`/`blockedCount`/`pausedCount` only, and the reducer summed those
three by hand, so a lifecycle that had handed the turn back counted towards
`lifecycleCount` and `totalTokens` and towards *nothing else* — the rollup could
not show it. `Metrics` now declares `awaitingDeveloperCount: int = 0` (L300-L302)
alongside the other three, and because `Metrics` is `extra="forbid"`, a future
live state whose bucket field was never declared **raises in the reducer** rather
than reading zero.

The `*Count` fields stay written out on `Metrics` because they are the served
contract the dashboard reads by name and pyright checks by name; what makes them
non-drifting is that the reducer fills them from the vocabulary and a test
asserts the declaration equals `STATE_COUNT_FIELDS`.

**State of the mirror** — the `STATE OF THE MIRROR` comment (L208-L226) was
rewritten in this leaf and now describes what holds rather than deferring a
defect. `dashboard/src/types/projection.ts` **holds the same partition, in the
same shape**: it declares `LIVE_STATES` and `TERMINAL_STATES` as the two halves,
spreads them into `LIFECYCLE_STATES` (live half first, so it enumerates in
exactly the order `STATES` does here — nothing on either side indexes the tuple,
but the two now agree for free), derives `State` from that tuple and
`ActiveState` from the live half, and sets `ACTIVE_STATES = LIVE_STATES` — the
live half itself, not a subtraction, for the same reason given above. Its
`stateCountField` matches the naming rule; Python moved to that spelling, not
the other way round, because TypeScript's type-level `Capitalize<>` cannot
lower-case a tail and the runtime helper must agree with the type.

**What the two sides enforce differs, and only in this file's favour.**
Composition makes two of `check_state_partition`'s three refusals
*unrepresentable* on either side: a state cannot be on `State` yet filed
nowhere, nor filed yet absent from `State`. The third — one state filed on BOTH
halves — is representable in both; this file refuses it at import, the mirror at
compile time (`ActiveState & TerminalState` constrained to `never`, so `tsc -b`
fails naming the offending state — verified by mutation, `TS2344`). Where the
mirror genuinely cannot follow is a duplicate WITHIN one half: `Literal["a","a"]`
collapses to one member here, while a TypeScript tuple keeps both. The
dashboard's `contract.test.ts` catches that at runtime instead (one bucket per
live state), which is a weaker gate but not an absent one. Do not restate this
as "the mirror has not adopted the partition" — that was true before this leaf
and is not true now.

### 260707-HFX2-L13 Summary-Only Task Documents

`TaskDocNode.bodyRevision` is the SHA-256 digest of the reader-body fields omitted from the
always-on projection. The node still carries identity, status, progress, steps, sub-task links, and
routing metadata, while objective/requirements/design/code examples/decisions/open questions/
references/sections are empty in broadcast summaries and populated only by the on-demand read.
`task_documents_body_bytes` remains a guardrail and must report zero for projected summaries while
still detecting seeded full-body regressions.

### 260707-HFX2-L12 CS-6 Update

`TASK_DOCUMENTS_PAYLOAD_BUDGET_BYTES` and `task_documents_body_bytes()` characterize the `analytics.taskDocuments` body payload that still rides the always-on projection. This is an observability guardrail for F6 until HFX2-L13 moves full task bodies behind an on-demand endpoint.

The models are the persisted/served peer of `events.py` — Pydantic with
`extra="forbid"`, camelCase wire fields — and, like `events.py`, are deliberately
**not** MCP response models: no token-accounting fields, never returned by a tool,
absent from `PUBLIC_TOOL_RESPONSE_MODELS`.

- `ActionAvailability` — one action's `{action, enabled, disabledReason?,
  nextSafeAction?}`; the reducer decides safety, never the UI (load-bearing for
  slice 06).
- `LifecycleProjection` — one lifecycle's folded state: id/state/phase/fleeting,
  enclosure/repoId/scope, `tokens`, `startedAt`/`lastEventTs`/`stateEnteredAt`/`staleSeconds`, the
  `inferred` flag (True ⇒ state was *derived*, not written — keeps "never pretend
  declared is observed" enforceable from data), the open block `ask`, the durable
  `gate` (slice 6c), `actions`, and (slice 3b) `tokenSeries` — the cumulative-token
  fuel gauge folded from the log's `tool.completed` events. Fleeting lifecycles carry
  no enclosure; persistent ones carry the full detail, so the slice-05 visual split
  falls out of the shape.
- `GateNode` (slice 6c) — a durable gate materialized onto `LifecycleProjection.gate`:
  the persisted `GateRecord` (`controlplane`) the cockpit reviews —
  `id`/`kind`/`state`/`decidedBy`/`decidedVia`/`packet`/`ts` plus `decisions` (the
  decision verbs the cockpit may POST for an *open* gate, empty once decided). Distinct
  from the event-derived `ask` proto-gate; the reducer attaches each lifecycle's latest
  *open* gate, read by `snapshots.read_gates` from the `GateStore`. L4 adds
  `evidenceRefs`, passed through from the gate record so clients can see
  reviewer-verdict artifact references even before dedicated gate-responder polish lands.
- `EnclosureNode` — a worktree enclosure (contract + group), cross-referenced to
  its lifecycle by `lifecycleId` (`""` for a legacy contract). L11 adds the
  worktree-existence truth `codeWorktreeExists` / `memoryWorktreeExists` (default
  `False`): stat'ed in the I/O layer at snapshot time
  (`snapshots._enclosure_from_contract`), matching how `worktree_status` reports
  existence (`contract.code_worktree.exists()`;
  `memory_worktree.exists()`/`False` when the contract has no memory worktree).
  The tasks surface (Hangar + LifecycleList) filters visibility on these flags,
  never on a cleanup-state proxy. Reopened-state semantics: `cleanup: reopened`
  (written by `task_reopen`) means contract-reset-awaiting-restart — the leaf's
  worktrees are gone until the next `worktree_start` recreates them — NOT live
  work, and NOT archived like `completed`/`abandoned` (the leaf is coming back);
  the node still projects so clients can see the reset, but both existence flags
  read `False` until restart.
- `ProviderNode` — a provider current-state snapshot with `snapshotStaleSeconds`
  (the snapshot is call-triggered, so its age is surfaced, never faked as live).
  Workspace provider nodes may be aggregate or repo-covered (`repoId`) when backend
  state has real per-repo evidence (CGC watcher rows or GrepAI `targetRepos`);
  worktree providers carry `worktreeGroup`, which remains the enclosure join key.
- `Metrics` (L278-L304) — workspace point counts + total tokens; slice 3b adds
  `stalenessHistogram` (sidecar verification-age buckets). **260731-EFA-L4 makes
  the per-state buckets derived rather than hand-listed** — see the next section.
- `TokenSample` — one `{ts, cumulative}` point on a lifecycle's token fuel gauge
  (slice 3b).
- The **slice-3b analytical nodes** (`DriftSnapshotNode`, `SidecarStaleNode`,
  `SetupSummaryNode`, `SetupProgressNode`, `RouteCoverageNode`, `ToolReportNode`,
  `LedgerNode`) and their `Analytics` container hold charts/feeds for specific
  cockpit panels. Slice 3c adds `TaskDocNode` (and `Analytics.taskDocuments`): a
  task document's active JSON-primary progress/content (surface 7), read from the
  `ar-task-document/v1` doc only. `TaskDocNode.lifecycleId` is optional runtime attachment, so planning
  documents can project before a lifecycle/enclosure exists. A `series-contract.md` is enclosure
  state, not readable task-document content. Kept lean: drift carries classification *counts* (rows stay in
  the snapshot file), and the full sidecar list collapses to the histogram +
  `Analytics.stalestSidecars` (a bounded leaderboard) so the served document stays
  small. Task 29 adds optional `checkedAt`, `sourceRoot`, `memoryRoot`, and `reportPath` to
  `DriftSnapshotNode`; those fields are provenance for actionable-drift queue rows and `checkedAt` is
  the repo-level dismissal anchor.
- `AttentionItem` + `Analytics.attentionQueue` (slice 05) — the home-screen
  attention queue: a reducer-ranked cross-section of what needs the human (blocked
  gates, down providers, actionable drift, failed setup, stale/dormant sessions),
  each with `severity` / `lane` / a server-computed `waitSeconds` and `*Id` /
  `enclosure` cross-refs back into the structural tree. Task 28 S5.2 adds `signalTs`, the
  triggering-signal timestamp the reducer uses to honor a lifecycle acknowledgement for the current
  occurrence and re-surface the item on a newer signal. Task 29 also uses `signalTs` for repo-level
  actionable-drift rows, sourced from `DriftSnapshotNode.checkedAt`. It is *derived* analytics (composed from the
  tree + signals, not read from an input file), so a structural-only caller can still see a non-empty
  queue.
- `AgentPickupNode` + `Analytics.agentPickups` (task 23/24/L3) — pending dashboard responses waiting for
  agent-side operator-inbox consumption. It carries entry/lifecycle/agent/gate ids, sender/recipient
  role metadata, message kind, artifact path, hosted delivery state, delivered session id/detail,
  server-computed age, pickup TTL, and state (`waiting-for-agent` or `check-chat`) without echoing the
  message body. Since 260707-HFX2-L1, it also carries the R1 ack/backoff fields
  (`attemptCount`/`lastAttemptAt`/`nextAttemptAt`/`escalatedAt`) and the R4 routed-owner fields
  (`ownerRole`/`ownerAgentId`/`ownerLifecycleId`), read straight off the underlying
  `OperatorInboxEntry` — a pending pickup row already IS the "pending/unacked signal" view, so no
  second surface was needed for that half of R5.
  `AttentionItem` also carries optional `gateId` so dashboard Clear/Dismiss actions can target gate
  records directly.
- `ExpectationRowNode` + `Analytics.expectationRows` (260707-HFX2-L1, R2/R5) — one durable
  what-must-happen-by-when row (`controlplane/expectation_rows.py::ExpectationRow`) projected for
  dashboard/architect observability: `kind` (`briefed-by`/`turn-report-by`/`verdict-by`/`ack-by`),
  `state`, `sourceId` (the dispatch surface's own id this row is a deadline FOR), optional
  subject/leaf keys, `dueAt`, and a server-computed `overdue` flag. Surfacing only — an L2
  predicate (a sibling leaf) reads `ExpectationRowStore` directly for correctness and never this
  node.
- **Slice-05 (5c) detail surfaces:** `ProviderNode` gained `scope`/`role`/`repoId`/`worktreeGroup`
  so a provider can be bound to a workspace repo, or to a worktree + repo + role (the workspace stack
  vs a worktree's isolated CGC/GrepAI). Task 12 S2 gives `repoId` an active workspace meaning for
  current-state repo coverage: CGC watcher rows and GrepAI configured `targetRepos`;
  `worktreeGroup` stays the stronger enclosure join when present.
  `TaskDocNode` gained the full task content — `steps` (`TaskStepNode` + `TaskSubStepNode`),
  `objective`/`requirements`/`design`, `codeExamples` (`TaskCodeExampleNode`), `decisions`
  (`TaskDecisionNode`), `openQuestions`, `references` — so the dashboard renders the task to read it
  in the UI rather than the filesystem.
- **Slice-5e Engine Room process map** — the enclosure (not a provider card) is
  the unit of the Engine Room, modeled as a state-backed process:
  - `CommitRefNode` — one side of an official-line/worktree pair (`branch` @
    `commit` at `path`, with `exists`/`dirty`/`behindSource`). Its `factState`
    (`observed` | `derived` | `planned` | `missing` | `not-applicable`) is the
    honesty axis the cockpit colours/animates from, so a planned path is never
    rendered as a live one.
  - `ProviderBootNode` — one isolated engine in a worktree's runtime, CGC (`code`)
    or GrepAI (`memory`), carrying its `runtimeState` health + `factState`; `missing`
    is now an explicit runtime state for expected-but-unobserved provider slots. The
    boot *sequence* lives on the owning `EngineProcessNode` (one setup-progress
    file per worktree group), this node is the engine's identity + current health.
  - `EngineProcessEdge` — one conduit in the process map (`fromNode`/`toNode`,
    `kind` ∈ git-base/worktree-add/ledger-map/contract-anchor/cgc-seed/grepai-clone/
    watcher-start/sync/closeout/integration/cleanup), with a fact-backed `state`
    (running/failed/planned/…) so an animated conduit always means an observed
    transition.
  - `EngineProcessNode` — one worktree enclosure as a state-backed process:
    contract id/group/task/lifecycle, parent `taskName`, leaf `leafId`, `phase` + `health`, the code/memory source +
    worktree `CommitRefNode`s, `memoryMode`, the reused slice-3b provider-boot
    sequence (`setupState`/`currentPhase`/`completedPhases`/`failedPhases`/
    `heartbeatAgeSeconds`/`seedFallback`/`retryArgs`), `providers`
    (`ProviderBootNode`s), `edges`, `actions`, `nextAction`/`summary`, and
    `missingFacts`/`sourceFiles`. Composed (like `attentionQueue`) from contract +
    status guidance + provider boot + lifecycle, **not** read from a new file. Slice
    5h adds two additive fields — `landing: list[LandingRefNode]` and
    `integrationStrategy` (`ff-only`/`replay`) — empty/`None` until the lifecycle reaches a
    landing phase, so every prior fixture and the live feed render unchanged. Slice 05m
    adds the additive `carryoverDoneAt: str | None = None` — the carryover milestone (ISO
    time the parked memory was carried into official memory, read off the official ledger
    by `guidance.carryover_done` and surfaced through `status_payload`); `None` until
    carried, display-only (5k renders the seam). The `phase` comment gains
    `carryover-pending` (between `integration-blocked` and `cleanup-pending`). The leaf identity
    is separate from the parent series task so multiple live leaves from one series can be rendered
    and selected independently.
  - `LandingRefNode` (slice 5h) — one remote/PR participant in the successful-landing
    arc (`origin/<feat>`, `origin/<base>`, `origin/mem-main`, the PR): `kind`/`label`/`state` + a
    `factState` honesty axis (like `CommitRefNode`) so a *planned* PR is never animated as observed.
    Slice 5l P2 adds `at: str | None = None` — gh's PR milestone timestamp (`mergedAt` once merged,
    else `createdAt`); `None` for branch refs. Display-only (the frontend renders it in 05k); the
    reducer's `LandingRefNode(**ref)` splat picks it up automatically from the probe's emitted dict.
  - `LedgerRefNode` + `LEDGER_WINDOW` (slice 5h coupler popover) — one memory.md ledger row
    (`codeCommit`/`memoryCommit`); `LEDGER_WINDOW = 25` is the served cap (the popover defaults to 8 and
    expands in place to ≤25, then the file). `EngineProcessNode` gains `ledgerRows: list[LedgerRefNode]` +
    `ledgerRowCount` (the WORKTREE coupler's window, from its own `memory.md`); `LedgerNode` gains
    `rows: list[LedgerRefNode]` (the OFFICIAL coupler's window, from the repo ledger — `closeoutCount` stays
    the full total); and `EngineProcessFacts` carries `ledger_rows`/`ledger_row_count` so the windowing is
    read in the I/O layer (`snapshots.py`) and the reducer stays a pure fold. **Tier 2** adds four optional
    fields to `LedgerRefNode` — `codeSubject`/`codeDate`/`memorySubject`/`memoryDate` (the per-side commit
    message + committer ISO date for the popover's 6 columns), probed best-effort in `snapshots.py` and,
    since the projection dumps `exclude_none=True`, omitted from the wire when a commit isn't local (never
    faked — the row falls back to the hash alone).
  - `EngineProcessFacts` — a frozen `@dataclass` *input* carrier (not a served
    node): the raw per-enclosure facts (`contract` = pure `contract_payload` dump,
    `guidance` = pure `lifecycle_guidance`, `status` = best-effort `status_payload`
    or `None` when its git probes could not run). Defined here so the reducer's
    pure `build_engine_processes` stays free of any I/O-layer dependency while
    sharing the carrier with the I/O reader (`snapshots.py`).
  - `Analytics.engineProcesses` — the served list of `EngineProcessNode`s; the
    second *derived* analytics surface (with `attentionQueue`), composed by the
    reducer from the structural tree + signals rather than read from an input file.
- **Slice 3c reopened (R1) — masters surface.** `SeriesNode` + `Analytics.series`: a series master's
  progress, keyed by its task **folder** (never a lifecycle). `SeriesSubTaskNode` is one checkbox
  (`number`/`name`/`file`/`status`/`scope`; `status` is the ⬜/🔨/✅ lever), `SeriesSectionNode` is one
  ordered render section. `doneCount`/`totalCount` roll up the master's *declared* `subTasks[]` (a slice
  marked `Completed` counts done regardless of its own leaf steps). Carries the full master render
  (`objective` + `subTasks` + `sections` + `decisions`, reusing `TaskDecisionNode`) so legacy clients can
  keep using the series reader, while master docs also project as `TaskDocNode`s for direct Operations
  selection. `TaskDocNode.id` exposes the JSON-primary task id so authored leaf labels can show the
  task-specific number even when parent sub-task ref labels are fallback-only metadata.
  `TaskDocNode.createdAt` and `SeriesSubTaskNode.createdAt` expose JSON-primary creation timestamps for
  default oldest-first display without parsing task-name prefixes. `SeriesNode.seriesTokenTotal` is the
  additive master aggregate of tokens spent by linked leaf lifecycles, composed by the reducer from
  projected sibling task docs and lifecycle token totals. Masters carry `lifecycleId=None` unless a root
  lifecycle is structurally attached.
- `WorkspaceProjection` — the whole tree: linked flat collections (lifecycles,
  enclosures, providers) + `metrics` + the analytics block + `generatedAt`. Its
  `version` is now `2` (slice 5e; was `1`) — the served-contract version clients
  read. Task 33 adds `activeWorktreeGroups: list[str]` (default empty): the
  worktree-group basenames whose enclosure lifecycle is still active, sourced from
  the same `active_enclosure_worktree_groups` admission the Engine Room uses. The
  shared `enclosures`/`lifecycles` lists keep all-time history; this is the bounded
  active set the Topology constellation filters on. Join key = the worktree-group
  basename (matches the worktree-scoped `ProviderNode.worktreeGroup` and
  `Path(EnclosureNode.worktreeGroup).name`). Additive — no `version` bump.
- **Slice-6g task-document navigation nodes** — `TaskSubTaskRefNode` (a master's series-index row:
  `number`/`name`/`file`/`status`/`scope` + `linkedLifecycleId`, set when the row's `file` points at
  another master so the dashboard renders a cross-series "→" jump) and `TaskSectionNode`
  (`kind`/`heading`/`body` — one ordered render section; masters use them for render plans, while
  non-master task docs may carry freeform sections from the task-document schema). `TaskDocNode` gains
  `subTasks` + `sections` (series index/render-plan fields or authored non-master freeform sections)
  and `masterLifecycleId` (the parent
  master's lifecycle when this doc's `master` ref points at another series — drives a "↑ parent
  series" breadcrumb). Additive — no `version` bump.
- **L14 orchestration-command relation** — `TaskDocNode.orchestrates` (`list[str]`, default `[]`):
  the pass-through of the task doc's master-only `orchestrates` field. Non-empty only on a master
  that IS an orchestration task; each entry names a master task it commands, and the dashboard
  derives the orchestration > master > leaf hierarchy (and rank insignia) from it. Additive — no
  `version` bump; docs without the field project `[]`.

### 260712-TRH-L7 projected landing snapshot

Projection assembly receives the latest landing facts as an input and does not call remote probes. Exact-contract fact state and freshness fields are carried into the engine-process model without changing the reducer's local-state publication cadence.

## Invariants And Boundaries

- **Client-agnostic** (North-Star #2): no dashboard-bespoke fields; a TUI or an
  agent are equal clients.
- **Linked flat collections, not deep nesting** — cross-reference by id
  (`enclosure.lifecycleId`, `provider.repoId`); keeps multi-repo enclosures
  (North-Star #4) from being keyed to a single repo.
- Persisted/served contract, not an MCP response model.
- **Lean served document** (slice 3b): raw inventories (drift rows, the full
  sidecar list) stay in their source files; the projection carries rollups +
  bounded samples (the histogram + the stalest-sidecar leaderboard).
- **Derived surfaces are composed, never read from a file** — `attentionQueue`
  and (slice 5e) `engineProcesses` are folded by the reducer from the structural
  tree + signals, so a structural-only caller still sees them populated.
- **`factState` is the honesty axis** (slice 5e) — `CommitRefNode`/`ProviderBootNode`
  and the `EngineProcessEdge.state` distinguish observed/derived/planned/missing/
  not-applicable so the cockpit never animates a planned path as a live one; same
  "never pretend declared is observed" rule as `LifecycleProjection.inferred`.
- **`EngineProcessFacts` is an input carrier, not a served node** — it lives in
  this module (which both `snapshots.py` and `reducer.py` import) purely so the
  reducer's `build_engine_processes` stays I/O-free.
- **`WorkspaceProjection.version` is the served-contract version** — bumped 1 → 2
  in slice 5e; clients gate on it.
- **The `Metrics` per-state buckets are the live vocabulary, not a list**
  (260731-EFA-L4). `ACTIVE_STATES` is `LIVE_STATES` verbatim and
  `STATE_COUNT_FIELDS` is derived from it; a new live state grows a bucket here,
  a count in the reducer, and — via `extra="forbid"` — a loud reducer failure if
  the field was never declared. Never re-derive the bucket set by subtracting
  `TERMINAL_STATES`, and never add a `*Count` field the vocabulary does not
  produce.
- **The bucket map must stay one-to-one.** `state_count_fields` refuses a
  colliding map at import rather than letting one `Metrics` field silently count
  two states; a collision is a naming problem in the state vocabulary, so it is
  fixed by renaming a state, not by special-casing here.
- **Creation order is structured data** — task/series consumers may use `createdAt` when it is present,
  but must not infer ordering from stored sub-task `number` strings or filename prefixes.
- **Series token totals are derived data** — `SeriesNode.seriesTokenTotal` is served on the folder-keyed
  master surface but is computed outside the schema from projected leaf lifecycle tokens; the master JSON
  does not persist it.
- **Task document existence is archive/delete based** — active docs under `tasks/<repo>/...` project
  regardless of terminal status; docs moved under `0_archive/` or deleted disappear from the active
  projection.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| `TaskDocNode.lifecycleId` is optional runtime attachment; `createdAt` remains structured ordering data. | `TaskDocNode` L585-L631 | [projection.py](projection.py) |
| `TaskDocNode.createdAt`, `SeriesSubTaskNode.createdAt`, and `SeriesNode.createdAt`/`objective` are part of the served projection contract. | `SeriesSubTaskNode` L634-L649; `SeriesNode` L662-L688 | [projection.py](projection.py) |
| `Analytics.series` carries the folder-keyed master aggregation surface while `taskDocuments` carries concrete active task documents. | `Analytics` L933-L964 (`taskDocuments` L957; `series` L964) | [projection.py](projection.py) |
| `SeriesNode.seriesTokenTotal` is the served aggregate field filled by the reducer-side token helper. | L662-L688 (`seriesTokenTotal` L684) | [projection.py](projection.py) |
| The snapshot reader populates task `createdAt`, master objective, and sub-task creation order from JSON-primary task docs. | `read_series_documents` L1275-L1316; `_series_subtask_nodes`/`_series_subtask_created_at` L1319-L1352; `_task_doc_node` L1373-L1462 (`createdAt=doc.createdAt` L1405) | [snapshots.py](snapshots.py) |
| The persisted-record peer this mirrors (same not-a-response-model boundary). | L1-L64 (the whole file) | [events.py](events.py) |
| The reducer that produces these shapes and keeps derived analytics pure. | L1-L92 | [reducer.py](reducer.py) |
| The provider projection helper that creates repo-covered workspace `ProviderNode`s from CGC watcher evidence and generic `targetRepos`. | `workspace_provider_nodes` L16-L39; `_cgc_repo_provider_nodes` L83-L98; `_target_repo_provider_nodes` L139-L150 | [provider_nodes.py](provider_nodes.py) |
| `DriftSnapshotNode` carries checked/source/memory/report provenance for actionable-drift rows. | L307-L327 | [projection.py](projection.py) |
| The state/phase vocabulary the lifecycle projection reuses — since 260731-EFA-L4 the live/terminal partition and `LIVE_STATES`, which `ACTIVE_STATES` is verbatim. | L101-L158 | [lifecycle_state.py](lifecycle_state.py) |
| `LifecycleVocabularyError` — the typed error `state_count_fields` raises on a colliding bucket map — and `check_state_partition`, the import-time refusal this module's comment contrasts with the mirror's compile-time one. | `LifecycleVocabularyError` L30-L38; `check_state_partition` L73-L98 | [lifecycle_state.py](lifecycle_state.py) |
| The rewritten `STATE OF THE MIRROR` comment: the TypeScript mirror now holds the same partition in the same shape, both sides refuse double-filing (import-time here, compile-time there), and a duplicate within one half is the one asymmetry left. | comment L194-L226 (mirror paragraph L208-L226) | [projection.py](projection.py) |
| The mirror the comment describes: `LIVE_STATES` / `TERMINAL_STATES` as halves, `LIFECYCLE_STATES` spread from them, `ACTIVE_STATES = LIVE_STATES`, and the `StatesAreFiledOnce` compile-time partition check. | L42; L48; L59; L72; L88-L90 | [dashboard/src/types/projection.ts](../../../../dashboard/src/types/projection.ts.md) |
| The reducer counts by `STATE_COUNT_FIELDS` rather than by three hand-written sums; `Metrics(extra="forbid")` is what turns a missing bucket into a raise. | `_metrics` L524-L547 | [reducer.py](reducer.py) |
| The bucket derivation, the collision refusal, and the `awaiting-developer` gap are pinned by test. | `MetricsBucketVocabularyTests` L1617-L1722; `StateCountFieldTests` L1950-L2005 | [test_observer_projection.py](../../../tests/test_observer_projection.py) |
| The design: the reducer as the single owner of interpretation and the client-agnostic projection API (§2.5), restated as design principle 2 (§7). | §2.5 L241-L248; §7 L363-L390 (principle 2 at L370-L371) | [docs/design/observable-lifecycle.md](../../../../docs/design/observable-lifecycle.md.md) |

## Series-Contract Notes

`EnclosureNode` now has explicit leaf identity and task-root fields, allowing the observer to serve active leaf enclosure records without making clients infer parent folders from contract paths. Leaf `series-contract.md` files are intentionally not `TaskDocNode`s; a promoted leaf needs a real `ar-task-document/v1` JSON document for the dashboard reader to show task content. `TaskDocNode.sections` can still render authored freeform sections from that JSON document. Master docs project as task documents and still project on `Analytics.series` for the legacy master surface. Master leaf ordering uses `createdAt` read from the referenced leaf JSON when available; task names remain display identity, not ordering metadata.

## Update History
- 2026-08-01T10:45+02:00 — 260731-EFA-L4 curator (post-wave source change): the `STATE OF THE
  MIRROR` comment was rewritten after the 00:35 entry below, and this card carried its old text as
  fact. **Corrected the false claim.** The card said the TypeScript mirror "has *not* adopted the
  partition … `LIFECYCLE_STATES` as one list of six and `TERMINAL_STATES` as a second list of two
  beside it, with `ACTIVE_STATES` the subtraction". Verified against
  `dashboard/src/types/projection.ts`: `LIVE_STATES` (L42) and `TERMINAL_STATES` (L48) are the
  halves, `LIFECYCLE_STATES = [...LIVE_STATES, ...TERMINAL_STATES]` (L59), and
  `ACTIVE_STATES = LIVE_STATES` (L72) — the same shape this file has, with no subtraction. The
  paragraph now records what the comment (L194-L226) actually says, including the asymmetry it
  names: both sides make two of `check_state_partition`'s three refusals unrepresentable; this file
  refuses double-filing at import and the mirror refuses it at compile time (`ActiveState &
  TerminalState` constrained to `never` — I reproduced the failure on a scratch copy and got
  `TS2344: Type '"completed"' does not satisfy the constraint 'never'.`); and a duplicate WITHIN one
  half is the one thing the mirror cannot follow, caught by `contract.test.ts` at runtime instead.
  Added an explicit "do not restate this as un-adopted" note so the old wording is not readopted.
  **Citation repairs.** The comment rewrite grew this file by 10 lines, so every in-file range at or
  below it was off by exactly that: `ACTIVE_STATES` L217 → L227, `state_count_field` L220-L235 →
  L230-L245, `state_count_fields` L238-L260 → L248-L270, `STATE_COUNT_FIELDS` L263 → L273, `Metrics`
  L268-L294 → L278-L304, `awaitingDeveloperCount` L290-L292 → L300-L302, `DriftSnapshotNode`
  L297-L317 → L307-L327, `TaskDocNode` L575-L621 → L585-L631, `SeriesSubTaskNode` L624-L639 →
  L634-L649, `SeriesNode` L652-L678 → L662-L688 (`seriesTokenTotal` L674 → L684), `Analytics`
  L923-L954 → L933-L964 (`taskDocuments` L947 → L957, `series` L954 → L964). Two rows were wrong in
  kind rather than by offset. The `lifecycle_state.py` row cited L101-L158 for a claim that also
  named `LifecycleVocabularyError`, which is at **L30-L38** — outside the range; it is now two rows,
  the second citing `LifecycleVocabularyError` L30-L38 and `check_state_partition` L73-L98. And the
  design-doc row cited **L91-L118; L332-L344** for "the reducer + client-agnostic projections
  (§2.5, §7)": L91-L118 is §1.4/§1.5 (Phases, Fleeting vs persistent) and L332-L344 straddles §5/§6
  — neither section is the one named. §2.5 is **L241-L248** and §7 is **L363-L390** (the
  client-agnostic principle at L370-L371); repaired, and the link corrected to the `.md.md` sidecar
  it should have pointed at. Re-checked and still landing unchanged: `snapshots.py` (all four
  helpers), `events.py` L1-L64, `reducer.py` L1-L92 and `_metrics` L524-L547, all three
  `provider_nodes.py` helpers, and both `test_observer_projection.py` classes. Added two rows (the
  rewritten comment, and the mirror declarations it describes).
- 2026-08-01T00:35+02:00 — 260731-EFA-L4 curator: the card described `Metrics` as "workspace point
  counts + total tokens" and did not mention that this module had gained a module-level API.
  Verified against the diff and the current source and added a section for it: `ACTIVE_STATES`
  (L217, `LIVE_STATES` verbatim — not a set difference), `state_count_field` (L220-L235, whose
  first-char-only upper-casing is what keeps it agreeing with the TypeScript mirror's
  `Capitalize<>`), `state_count_fields` (L238-L260, which refuses a non-injective map by naming
  both colliding states), and `STATE_COUNT_FIELDS` (L263). Recorded the bug this closed —
  `awaiting-developer` had no bucket, so a lifecycle that handed the turn back inflated
  `lifecycleCount`/`totalTokens` and landed nowhere; `Metrics` now declares
  `awaitingDeveloperCount` (L290-L292) and `extra="forbid"` turns a future missing bucket into a
  reducer raise. Also recorded the mirror's un-adopted state (`dashboard/src/types/projection.ts`
  still keeps two lists and a subtraction), which is deliberately out of scope here. Added two
  invariants. **Citation repairs** — every range in the reference table was re-checked and eight
  did not land on their symbol: `Analytics.series`/`taskDocuments` L711-L740 → L923-L954
  (`taskDocuments` L947, `series` L954); `SeriesNode.seriesTokenTotal` L497-L523 → L652-L678
  (`seriesTokenTotal` L674); `DriftSnapshotNode` L199-L220 → L297-L317; the snapshots reader row
  L635-L717; L752-L763 → `read_series_documents` L1275-L1316, `_series_subtask_nodes`/
  `_series_subtask_created_at` L1319-L1352, `_task_doc_node` L1373-L1462 (`createdAt` L1405);
  `events.py` L1-L77 → L1-L64 (the file is 64 lines, so the range overshot the file);
  `provider_nodes.py` L1-L92 → named per helper, because L1-L92 excluded
  `_target_repo_provider_nodes` (L139-L150), the half of the claim about generic `targetRepos`;
  `lifecycle_state.py` L1-L19 → L101-L158 (L1-L19 is now only the module docstring — the
  vocabulary moved below the partition helpers); and the two rows citing `projection.py` with no
  range got their classes named. The `reducer.py` L1-L92 and design-doc ranges were re-checked and
  still land. Added three reference rows (the reducer's `_metrics`, and the two test classes that
  pin the derivation).
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
