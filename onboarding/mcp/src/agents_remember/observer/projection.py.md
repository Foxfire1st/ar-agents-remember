# mcp/src/agents_remember/observer/projection.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/observer/projection.py` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-01T10:45+02:00 |
| lastVerifiedCommitHash | `2dea095cd68454a7a68893e37c07dbd8daa86d32`       |
| lastVerifiedCommitDate | 2026-08-09T18:00:39+02:00|
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

- `ACTIVE_STATES: tuple[LiveState, ...] = LIVE_STATES` cit:([`ACTIVE_STATES`], mcp/src/agents_remember/observer/projection.py:236-236) cit:([`LIVE_STATES`], mcp/src/agents_remember/observer/lifecycle_state.py:136-138) cit:(["def _metrics("], mcp/src/agents_remember/observer/reducer_impl/_metrics.py:27-27) — the states
  `Metrics` buckets, the live half verbatim. It is deliberately **not** a set
  difference `STATES - TERMINAL_STATES`: a subtraction re-derives the answer from
  a second list that could be wrong, whereas the live half already *is* the
  answer. `lifecycleCount` counts every lifecycle and `totalTokens` sums every
  one, so what the per-state buckets add is the live workload — a
  `completed`/`abandoned` lifecycle is history, not work in flight.
- `state_count_field(state) -> str` cit:([`state_count_field`], mcp/src/agents_remember/observer/projection.py:239-254) — the naming rule:
  `running` → `runningCount`, `awaiting-developer` → `awaitingDeveloperCount`.
  Each segment after the first has its **first character upper-cased and the rest
  left alone**; `str.capitalize` would lower-case the tail instead, which both
  disagrees with the TypeScript mirror (whose type-level `Capitalize<>` cannot
  lower-case a tail, so it renders `awaitingDEVELOPERCount`) and quietly merges
  states differing only in tail case.
- `state_count_fields(states) -> dict[str, str]` cit:([`state_count_fields`], mcp/src/agents_remember/observer/projection.py:257-279) cit:([`LifecycleVocabularyError`], mcp/src/agents_remember/observer/lifecycle_state.py:30-38) — builds the map and
  **refuses one that is not one-to-one**, raising `LifecycleVocabularyError`
  naming both colliding states. The rule is not injective (`a-b` and `aB` both
  bucket into `aBCount`), and a collision does not announce itself: `Metrics` is
  keyed by field, so two states sharing a bucket means the later count silently
  overwrites the earlier.
- `STATE_COUNT_FIELDS: dict[str, str] = state_count_fields(ACTIVE_STATES)`
  cit:(["STATE_COUNT_FIELDS,"], mcp/src/agents_remember/observer/reducer_impl/_metrics.py:14-14) — the one map the reducer's counting loop reads instead of re-enumerating buckets cit:(["def _metrics(", "**{bucket: counts[state] for state, bucket in STATE_COUNT_FIELDS.items()},"], mcp/src/agents_remember/observer/reducer_impl/_metrics.py:27-27; mcp/src/agents_remember/observer/reducer_impl/_metrics.py:49-49).

**The bug this closed.** `awaiting-developer` had no bucket. `Metrics` declared
`runningCount`/`blockedCount`/`pausedCount` only, and the reducer summed those
three by hand, so a lifecycle that had handed the turn back counted towards
`lifecycleCount` and `totalTokens` and towards *nothing else* — the rollup could
not show it. `Metrics` now declares `awaitingDeveloperCount: int = 0` cit:([`Metrics`, `awaitingDeveloperCount`], mcp/src/agents_remember/observer/projection.py:287-313) cit:(["def _metrics("], mcp/src/agents_remember/observer/reducer_impl/_metrics.py:27-27)
alongside the other three, and because `Metrics` is `extra="forbid"`, a future
live state whose bucket field was never declared **raises in the reducer** rather
than reading zero.

The `*Count` fields stay written out on `Metrics` because they are the served
contract the dashboard reads by name and pyright checks by name; what makes them
non-drifting is that the reducer fills them from the vocabulary and a test
asserts the declaration equals `STATE_COUNT_FIELDS` cit:([`STATE_COUNT_FIELDS`], mcp/src/agents_remember/observer/projection.py:282-282) cit:(["def _metrics("], mcp/src/agents_remember/observer/reducer_impl/_metrics.py:27-27).

**State of the mirror** — the `STATE OF THE MIRROR` comment cit:(["STATE OF THE MIRROR", `Composition`, "WITHIN one half"], mcp/src/agents_remember/observer/projection.py:217-217; mcp/src/agents_remember/observer/projection.py:228-228; mcp/src/agents_remember/observer/projection.py:233-233) was
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
lower-case a tail and the runtime helper must agree with the type cit:([`LIVE_STATES`, `TERMINAL_STATES`, `LIFECYCLE_STATES`, `ACTIVE_STATES`], dashboard/src/types/projection.ts:9-9; dashboard/src/types/projection.ts:11-11; dashboard/src/types/projection.ts:13-13; dashboard/src/types/projection.ts:21-21).

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
live state), which is a weaker gate but not an absent one cit:(["def check_state_partition(", "export type ActiveState = (typeof LIVE_STATES)[number];", "TerminalState = EndOutcome"], mcp/src/agents_remember/observer/lifecycle_state.py:73-98; dashboard/src/types/projection.ts:19-19; mcp/src/agents_remember/observer/lifecycle_state.py:118-118) cit:([`LIVE_STATES`, `TERMINAL_STATES`, `StatesAreFiledOnce`], dashboard/src/types/projection.ts:9-9; dashboard/src/types/projection.ts:11-11; dashboard/src/types/projection.ts:25-25). Do not restate this
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
- cit:([`Metrics`], mcp/src/agents_remember/observer/projection.py:287-313) — workspace point counts + total tokens; slice 3b adds
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

| Finding | Anchor | Source |
| --- | --- | --- |
| `TaskDocNode.lifecycleId` is optional runtime attachment on the served projection node. | `TaskDocNode` | mcp/src/agents_remember/observer/projection.py:608-654 |
| The lifecycle panel uses structured `createdAt` data in its row comparator. | `compareRows` | dashboard/src/panels/lifecycle-list/LifecycleList.tsx:1179-1182 |
| `TaskDocNode.createdAt` and `SeriesSubTaskNode.createdAt` are part of the served projection contract. | `TaskDocNode`; `SeriesSubTaskNode` | mcp/src/agents_remember/observer/projection.py:608-654; mcp/src/agents_remember/observer/projection.py:657-672 |
| `SeriesNode.createdAt` and `objective` are part of the served projection contract. | `SeriesNode` | mcp/src/agents_remember/observer/projection.py:685-711 |
| `Analytics.series` carries the folder-keyed master aggregation surface while `taskDocuments` carries concrete active task documents read from JSON-primary sources. | `Analytics`; `taskDocuments`; "def read_task_documents(" | mcp/src/agents_remember/observer/projection.py:956-987; mcp/src/agents_remember/observer/snapshots_impl/_task_documents.py:48-48 |
| The series-token helper fills served `SeriesNode.seriesTokenTotal` by summing sibling lifecycle tokens for matching references. | "attach_series_token_totals("; `tokens_by_lifecycle`; "for ref in node.subTasks"; "total += tokens_by_lifecycle.get(doc.lifecycleId, 0)"; `model_copy` | mcp/src/agents_remember/observer/series_tokens.py:14-14; mcp/src/agents_remember/observer/series_tokens.py:20-20; mcp/src/agents_remember/observer/series_tokens.py:26-26; mcp/src/agents_remember/observer/series_tokens.py:29-30 |
| The snapshot reader loads the JSON-primary series documents. | "def read_series_documents(" | mcp/src/agents_remember/observer/snapshots_impl/_task_documents.py:174-174 |
| The snapshot reader builds series sub-task nodes. | "def _series_subtask_nodes(path: Path, doc: TaskDocument) -> list[SeriesSubTaskNode]:" | mcp/src/agents_remember/observer/snapshots_impl/_task_documents.py:220-220 |
| The snapshot reader derives sub-task creation order. | "def _series_subtask_created_at(base_dir: Path, ref_file: str) -> s" | mcp/src/agents_remember/observer/snapshots_impl/_task_documents.py:241-241 |
| The snapshot reader builds task-document nodes, including structured creation data. | "def _task_doc_node(" | mcp/src/agents_remember/observer/snapshots_impl/_task_documents.py:296-296 |
| The persisted-record peer this mirrors is the append-only observer-event stream, with the same not-a-response-model boundary. | `Event`; "ar-observer-event/v1"; "append-only"; `PUBLIC_TOOL_RESPONSE_MODELS` | mcp/src/agents_remember/observer/events.py:1-13; mcp/src/agents_remember/observer/events.py:39-64 |
| The reducer produces these shapes and keeps derived analytics pure. | `project_workspace` | mcp/src/agents_remember/observer/reducer.py:128-181 |
| The reducer's metrics helper keeps derived analytics pure. | "def _metrics(" | mcp/src/agents_remember/observer/reducer_impl/_metrics.py:27-27 |
| The projection schema owns the served analytics shape. | `Analytics` | mcp/src/agents_remember/observer/projection.py:956-987 |
| Workspace provider projection joins repo-covered providers. | `workspace_provider_nodes` | mcp/src/agents_remember/observer/provider_nodes.py:16-39 |
| CGC watcher evidence is converted into repo-covered provider nodes. | `_cgc_repo_provider_nodes` | mcp/src/agents_remember/observer/provider_nodes.py:83-98 |
| Generic `targetRepos` evidence is converted into repo-covered provider nodes. | `_target_repo_provider_nodes` | mcp/src/agents_remember/observer/provider_nodes.py:139-150 |
| `DriftSnapshotNode` carries checked/source/memory/report provenance for actionable-drift rows. | `DriftSnapshotNode` | mcp/src/agents_remember/observer/projection.py:316-336 |
| The state/phase vocabulary the lifecycle projection reuses: live and terminal partitions. | `check_state_partition`; `LIVE_STATES`; `TERMINAL_STATES`; `State` | mcp/src/agents_remember/observer/lifecycle_state.py:73-98; mcp/src/agents_remember/observer/lifecycle_state.py:120-120; mcp/src/agents_remember/observer/lifecycle_state.py:136-139 |
| The projection takes `ACTIVE_STATES` verbatim from the live half. | "ACTIVE_STATES: tuple[LiveState, ...] = LIVE_STATES" | mcp/src/agents_remember/observer/projection.py:236-236 |
| `LifecycleVocabularyError` is the typed collision error, while `check_state_partition` is the import-time partition refusal. | `LifecycleVocabularyError`; `check_state_partition` | mcp/src/agents_remember/observer/lifecycle_state.py:30-38; mcp/src/agents_remember/observer/lifecycle_state.py:73-98 |
| The `STATE OF THE MIRROR` comment describes the TypeScript mirror's matching partition and its remaining within-half asymmetry. | "STATE OF THE MIRROR"; `Composition`; "WITHIN one half" | mcp/src/agents_remember/observer/projection.py:217-217; mcp/src/agents_remember/observer/projection.py:228-228; mcp/src/agents_remember/observer/projection.py:233-233 |
| The TypeScript mirror's matching partition is the client-side counterpart of that comment. | `LIVE_STATES`; `TERMINAL_STATES` | dashboard/src/types/projection.ts:9-9; dashboard/src/types/projection.ts:11-11 |
| The TypeScript mirror declares `LIVE_STATES` / `TERMINAL_STATES`, spreads `LIFECYCLE_STATES`, aliases `ACTIVE_STATES`, and uses `StatesAreFiledOnce`. | `LIVE_STATES`; `TERMINAL_STATES`; `LIFECYCLE_STATES`; `ACTIVE_STATES`; `StatesAreFiledOnce` | dashboard/src/types/projection.ts:9-9; dashboard/src/types/projection.ts:11-11; dashboard/src/types/projection.ts:13-13; dashboard/src/types/projection.ts:21-21; dashboard/src/types/projection.ts:25-25 |
| The reducer counts by `STATE_COUNT_FIELDS` rather than by hand-written sums. | "def _metrics(" | mcp/src/agents_remember/observer/reducer_impl/_metrics.py:27-27 |
| The reducer-side `_metrics` path makes an undeclared bucket fail loudly through the strict metrics model. | "def _metrics(" | mcp/src/agents_remember/observer/reducer_impl/_metrics.py:27-27 |
| The bucket derivation, collision refusal, and `awaiting-developer` gap are pinned by focused tests. | `MetricsBucketVocabularyTests`; `StateCountFieldTests` | mcp/tests/test_observer_projection_metrics.py:128-233; mcp/tests/test_observer_projection_metrics.py:461-516 |
| The design places the observer and projections in §2.5. | `### 2.5 The observer and its projections` | docs/design/observable-lifecycle.md:241-251 |
| The design principles preserve reducer ownership and a client-agnostic projection API in §7. | `## 7. Design Principles Preserved` | docs/design/observable-lifecycle.md:363-390 |

## Series-Contract Notes

`EnclosureNode` now has explicit leaf identity and task-root fields, allowing the observer to serve active leaf enclosure records without making clients infer parent folders from contract paths. Leaf `series-contract.md` files are intentionally not `TaskDocNode`s; a promoted leaf needs a real `ar-task-document/v1` JSON document for the dashboard reader to show task content. `TaskDocNode.sections` can still render authored freeform sections from that JSON document. Master docs project as task documents and still project on `Analytics.series` for the legacy master surface. Master leaf ordering uses `createdAt` read from the referenced leaf JSON when available; task names remain display identity, not ordering metadata.

## Update History
- 2026-08-09T12:08+02:00 — 260713-TES-L5 curator: recorded the `AgentPickupNode` docstring
## 260713-TES-L5 Current Delta — AgentPickupNode Landing Semantics

`AgentPickupNode`'s docstring (which rides the generated projection schema) now describes a
pending dashboard response waiting for a turn-boundary landing: the system acks (N16),
`operator_inbox_consume` is an optional attribution marker, and the sweep predicates read the
stores directly and never this projection.

## Update History

- 2026-08-09T12:08+02:00 — 260713-TES-L5 curator: recorded the `AgentPickupNode` docstring
  rewrite — pending rows wait for a turn-boundary landing (N16, the system acks), consume is
  an optional attribution marker, and the sweep predicates read the stores directly and never
  this projection. Verification metadata pinned until closeout stamps the 260713-TES-L5
  commit.
- 2026-08-04T16:28:49+02:00 — 260731-EFA-L6 S18-B11 same-reviewer residual correction: rebound reducer consumption, mirror contract, event envelope, and `ACTIVE_STATES` assignment to operative spans, and extended the series-token row with explicit anchors for the per-reference loop and the token summation body. Verification metadata unchanged.
- 2026-08-01T10:45+02:00 — 260731-EFA-L4 curator (post-wave source change): corrected the mirror partition narrative to the current `LIVE_STATES`, `TERMINAL_STATES`, `LIFECYCLE_STATES`, and `ACTIVE_STATES` source contract cit:([`LIVE_STATES`, `TERMINAL_STATES`, `LIFECYCLE_STATES`, `ACTIVE_STATES`], dashboard/src/types/projection.ts:9-9; dashboard/src/types/projection.ts:11-11; dashboard/src/types/projection.ts:13-13; dashboard/src/types/projection.ts:21-21). The local explanation and reference table were then rechecked against the current sources cit:(["STATE OF THE MIRROR"], mcp/src/agents_remember/observer/projection.py:217-217) cit:([`project_workspace`], mcp/src/agents_remember/observer/reducer.py:128-181) cit:([`check_state_partition`], mcp/src/agents_remember/observer/lifecycle_state.py:73-98) cit:([`### 2.5 The observer and its projections`], docs/design/observable-lifecycle.md:241-251) cit:([`## 7. Design Principles Preserved`], docs/design/observable-lifecycle.md:363-390).
- 2026-08-01T00:35+02:00 — 260731-EFA-L4 curator: documented the vocabulary-derived metrics map, the `awaitingDeveloperCount` bucket, and the collision refusal in the current source cit:([`ACTIVE_STATES`, `state_count_field`, `state_count_fields`, `STATE_COUNT_FIELDS`, `awaitingDeveloperCount`], mcp/src/agents_remember/observer/projection.py:236-236; mcp/src/agents_remember/observer/projection.py:239-254; mcp/src/agents_remember/observer/projection.py:311-311; mcp/src/agents_remember/observer/projection.py:257-279; mcp/src/agents_remember/observer/projection.py:282-282). The focused projection tests and reducer-side `_metrics` path remain the behavioral evidence cit:(["class MetricsBucketVocabularyTests(unittest.TestCase):", "class StateCountFieldTests(unittest.TestCase):", "def _metrics("], mcp/tests/test_observer_projection_metrics.py:128-128; mcp/tests/test_observer_projection_metrics.py:461-461; mcp/src/agents_remember/observer/reducer_impl/_metrics.py:27-27; mcp/tests/test_observer_projection_metrics.py:128-233; mcp/tests/test_observer_projection_metrics.py:461-516).
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
