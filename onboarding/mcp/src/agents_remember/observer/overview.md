# mcp/src/agents_remember/observer/ — Observable-Lifecycle Substrate And Projection Overview

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| sourceRoute            | `mcp/src/agents_remember/observer/`              |
| doc_type               | `route-local-overview`                           |
| lastUpdated | 2026-08-01T10:45+02:00 |
| lastVerifiedCommitHash | `e52edaf5b655f495580efd93306afdf922b19b51`       |
| lastVerifiedCommitDate | 2026-08-01T11:01:51+02:00|
| governingOverview      | `../../../../overview.md`                         |

## Governing Overview

[mcp/overview.md](../../../../overview.md)

## Purpose

260707-HFX2-L13 closes the L12 observer residuals: workspace appends/compaction/live reads share a
cross-process lock and virtual cursor base; lifecycle heartbeats coalesce into bounded sidecars whose
latest value is merged into normal reads/projections; dormant unprotected lifecycle cleanup reclaims
the whole sidecar-bearing directory; and task/series broadcasts are bounded summaries with full task
bodies read on demand through a confined snapshot boundary.

`observer/` is the observable session lifecycle substrate (the 3.0
browser-dashboard direction). It owns **both sides**: the **write side** — an
append-only, durable, replayable log of what happened in (or to) a lifecycle —
and the **read side** — the projection reducer that folds that log (plus
structural file snapshots) into resolved state — including, since L11, abandon
terminality read from contracts: an abandoned enclosure's lifecycle projects
`abandoned` and abandoned/reopened enclosures synthesize no paused zombie, because
the single-writer store forbids foreign `lifecycle.ended` appends — for replay/sim fixtures, the
dashboard, and any other client. The full design is
`docs/design/observable-lifecycle.md`.

Slice 2a built the write side; slice 2b adds the ambient lifecycle — the
process-singleton signal state machine, the six `lifecycle_*` signals, the
heartbeat ticker, and the TTL project-and-prune sweep. Slice 2c adds resume + the
save gate: `promote`/`attach` on the ambient, the pure `save_gate.py` vocabulary
(landing-zone scope, the `SaveDecision` boundary, `SaveGateRequired`), and the
`LifecycleState` persistence-binding fields — so a lifecycle survives chat death
and resumes from the worktree contract. Slice 3a adds the **projection read
side**: the pure reducer that folds the event logs (plus structural file
snapshots) into the resolved state tree, the shared timing leaf, and the atomic
projection store (the structural surfaces — providers, contracts, group layout).
Slice 3b adds the **analytical surfaces** — drift read from a persisted JSON
snapshot, git-free sidecar staleness, provider setup summaries/progress, route
coverage, the tool-report feed, and ledger currency — plus the derived-aggregate
rollups (the per-lifecycle token fuel gauge and the sidecar-staleness histogram).
Slice 3c adds the task-document surface (S7): `read_task_documents` projects active
JSON-primary `ar-task-document/v1` docs with optional lifecycle attachment, so the dashboard shows
task content before and after runtime binding; since L10 the leaf-enclosure attachment joins the
served enclosure `leafId` (a slugified lowercase directory name) against the doc's authored `id`
**case-insensitively**, because series leaf docs carry no `enclosures[]` refs in practice. Slice 05 (5b) adds the **attention queue**: the
reducer's `build_attention_queue` ranks what needs the human (blocked gates, down
providers, actionable drift, failed setup, stale/dormant sessions) into the derived
`Analytics.attentionQueue` — the one analytics field composed from the structural tree +
signals rather than read from an input file. Slice 5f S6 (§9) adds `_start_attention`: a pre-contract
**blocked-start** raises the same master-caution in the queue that the agent raises in chat, and
`project_workspace` now threads `engine_start_progress` into it (a happy-path beat is not an alarm).

Slice 05 (5c) completes the route's read side for the cockpit: `project_workspace` synthesizes a
paused **persistent lifecycle** for every current worktree-backed enclosure with no event log. The live
projection boundary is current enclosure ownership: fleeting lifecycles still do not need enclosures,
fresh non-terminal promotion/gate lifecycles may bridge the enclosure materialization window, but older
non-fleeting event-backed lifecycles drop from the live view when their enclosure is deleted or re-owned.
`read_providers` reads each worktree's **isolated provider stack** (surface 4) bound to
worktree/repo/role. Since 260707-HFX2-L13, `TaskDocNode` in the always-on projection is a bounded,
body-free summary with `bodyRevision`; the dashboard reads one selected full body through
`read_task_document_body`, while identity/progress/step/navigation fields remain in the summary.

Slice 5e adds the **Engine Room process map** surface: `Analytics.engineProcesses` — a second derived
analytics surface (like `attentionQueue`) composed by `reducer.build_engine_processes` into one
`EngineProcessNode` per worktree enclosure, joining the recorded contract + status guidance
(existence/dirty/freshness/provider boot) with the worktree's isolated providers and setup-progress,
carrying observed/derived/planned/missing fact-state honesty. `snapshots.read_engine_process_facts`
sources the contract facts (best-effort `status_payload`); `read_start_progress_entries` (§5.4) +
`reducer._start_process_node` surface a `worktree_start` blocked **before** its contract exists.
`WorkspaceProjection.version` bumps to 2.

Slice 5h extends this surface with the **successful-landing arc**: additive
`EngineProcessNode.landing` (a list of `LandingRefNode` — `origin/<feat>`, `origin/<base>`, the PR,
`origin/mem-main`) + `integrationStrategy`, observed best-effort by `worktrees/modules/landing.py`
(remote/PR refs) and composed by `reducer._engine_process` from the status payload's `landing` block.
Both are empty/`None` until the lifecycle reaches a landing phase, so every prior fixture and the live
feed render unchanged. Slice 5l P2 adds the display-only `LandingRefNode.at` (gh's PR milestone
timestamp — `mergedAt` once merged, else `createdAt`; `None` for branch refs); the reducer's
`LandingRefNode(**ref)` splat picks it up from the probe's emitted dict with no reducer change.

260712-TRH-L7 keeps that landing model honest without putting remote work in the projection tick:
`LandingStateRefresher` publishes bounded, exact-contract immutable observations in the background;
projection reads the latest snapshot and carries explicit missing/stale freshness fields, while
interactive status retains its fresh probe behavior. Refresher startup, cancellation, and failed-cycle
containment are lifecycle-managed by serving.

260712-PTS-L2 (master 260712-PTS) collapses the tick's contract reads to ONE shared pass. Before it,
`read_enclosures`, `read_engine_process_facts`, and drift-snapshot pruning each ran their own
`iter_leaf_enclosure_contracts` walk + `load_contract` parse every 1s tick (py-spy 2026-07-12:
2.78s/3.68s/3.40s of total time in a 15s sample). `contract_snapshot.py` builds an immutable
`ContractSnapshot` once per tick in `projection_store` and injects it into all three consumers via
keyword-only `contracts=` parameters (standalone calls still build their own, behavior-identical), on
top of a cross-tick parse cache keyed by `(mtime_ns, size, ctime_ns)` stat identity — unchanged
contract files are not re-read or re-parsed at all; parse failures are never cached (skip + retry
every tick). Cache mutation is confined to the serialized projection tick, and the cached
`WorktreeContract` instances are shared across ticks, so consumers must never mutate them. The
landing refresher and supervisor sweep deliberately keep their own passes.

Slice 05l Part 1 closes the **backend teardown-visibility** gaps in this surface. The reducer's
`_GUIDANCE_PHASE` gains `"abandoned": "abandoned"`, surfacing `worktrees/modules/guidance.py`'s new
abandoned-worktree phase to the process-map vocabulary (before, an abandoned enclosure projected the
`worktree-started` default — a fully-active phantom). And a new `reducer._is_disposed(fact)` (True when
the contract's `cleanup` is `completed`/`abandoned` = `worktree_cleanup`/`worktree_abandon` already
reclaimed the stack) now filters `build_engine_processes`, so a **disposed** enclosure drops from the
active `Analytics.engineProcesses` instead of rendering as a phantom — the frontend (05k) animates the
removal. `cleanup-pending` is intentionally kept (its de-materialise beat still needs a live node).

Slice 05m extends this Engine Room surface for the **carryover-before-cleanup** lifecycle step. The
reducer's `_GUIDANCE_PHASE` gains `"carryover-pending": "carryover-pending"`, surfacing
`worktrees/modules/guidance.py`'s new phase (between integration and cleanup, raised while the parked
memory still needs carrying home) to the process-map vocabulary. And `reducer._engine_process` maps the
additive `EngineProcessNode.carryoverDoneAt` (`_str_or_none(status.get("carryoverDoneAt"))`) — the
carryover milestone ISO time read off the OFFICIAL ledger by `guidance.carryover_done` and surfaced
through `status_payload`; `None` until carried, display-only (5k renders the seam). Both are additive,
so prior fixtures and the live feed render unchanged.

Slice 3c **reopened (R1)** adds the **series/master surface** so a series master is observable, not just
its leaves: `snapshots.read_series_documents` selects `kind == "master"` docs (keyed by task **folder**)
and builds a `SeriesNode` (full reader: `objective` + `subTasks` + `sections` + `decisions` +
`doneCount`/`totalCount` over the master's *declared* `subTasks[]`, each subtask one checkbox),
threaded through `build_analytics`/`project_workspace`/`project_and_write` into additive
`Analytics.series`. Task 17 changes Operations to project concrete active task documents first:
`read_task_documents` now includes active master/leaf/light JSON docs even before lifecycle binding, and
`TaskDocNode.lifecycleId` is optional runtime context. `TaskDocNode.id` carries the JSON-primary task id
used by clients as the authored leaf display number; `TaskDocNode.createdAt` carries task creation time,
and `SeriesSubTaskNode.createdAt` is resolved from the referenced sibling leaf JSON so clients can default
to oldest-first leaf display without parsing task-name prefixes. Task 21 adds `SeriesNode.seriesTokenTotal`,
derived by joining a master's declared sub-task files to projected sibling leaf task documents and summing
their bound lifecycle token totals; missing or unbound leaves contribute zero.

Slice 6c adds **gate projection** (the Task-6 gate/action plane): `snapshots.read_gates` folds every
lifecycle + workspace `GateStore` log, and `reducer._attach_gates` materializes each lifecycle's
latest *open* `GateRecord` onto `LifecycleProjection.gate` (a `GateNode`) while
`_gate_attention` raises a `gate-open` queue item — so the cockpit can review and decide
a durable gate, distinct from the event-derived `ask` proto-gate. L4 adds
`GateNode.evidenceRefs`, a projection pass-through for reviewer-verdict artifact
refs attached to delegated approvals.

Task 23/24/L3 turns gate/operator-inbox prompts into TTL-bound interaction surfaces. `read_gates` can compact
expired throwaway gate rows before projection, `AgentPickupNode` is the pending-inbox task-row feedback
surface, and `read_agent_pickups` projects each pending inbox entry as `waiting-for-agent` until the
5-minute pickup TTL, then `check-chat` until the developer dismisses it or the 24-hour interaction TTL
deletes it. L3 carries sender/recipient roles, message kind, artifact path, and hosted-delivery
state/session/detail through that node so agent-to-agent inbox push attempts are dashboard-visible.
Durable tasks, contracts, and ledgers remain outside this cleanup path.

**260707-HFX2-L1 (R5 projection surfacing)**: `AgentPickupNode` now also carries the R1/R4 fields
(`attemptCount`/`lastAttemptAt`/`nextAttemptAt`/`escalatedAt`/`ownerRole`/`ownerAgentId`/
`ownerLifecycleId`) straight off the underlying `OperatorInboxEntry`, so a pending pickup row
already IS the surfaced "pending/unacked signal" view — no second surface was needed for that half
of R5. A new `ExpectationRowNode` + `Analytics.expectationRows` (populated by
`snapshots.read_expectation_rows`, reading `ExpectationRowStore.pending()`) surfaces R2's durable
deadline rows for dashboard/architect observability, each stamped with a computed `overdue` flag.
Both are surfacing ONLY — an L2 predicate (a sibling leaf) reads the underlying stores directly
and never this projection; that is the #22 correctness/visibility split this leaf's R5 documents.

Slice 6g extends the task-document surface for **series navigation**: `read_series_documents` remains the
folder-keyed master aggregation surface, while `read_task_documents` projects every active JSON-primary
task document and attaches lifecycle context when direct lifecycle ids, `enclosures[].enclosurePath`, or
structured leaf/root enclosure matches exist. Task JSON scans skip `0_archive/` and `enclosures/`, so
archived roots and contract folders do not reappear in the live projection. The enclosure contract can
supply the lifecycle binding for a real JSON task document, but the contract itself is never projected as
readable task-document content.

Task 12 S2 adds repo-covered provider projection to the read side. `snapshots.read_providers` still owns
the file-surface read of workspace `current.json` and each worktree group's provider state, but provider
node construction now lives in `provider_nodes.py`: CGC `resources.watchers` rows become repo-scoped
workspace provider nodes, and GrepAI `targetRepos` derived from configured repository memory roots become
repo-scoped memory provider nodes. A single GrepAI runtime may still aggregate multiple repository
memory projects; the route projects `targetRepos` because those projects are addressable targets inside
that provider instance. Providers without explicit target evidence still fall back to one aggregate
workspace provider node.

Task 31 closes the provider-state honesty gap for live dashboards. `projection_store.project_and_write`
can call a TTL-gated provider-state refresher before reading provider snapshots, so `current.json` tracks
the actual provider stack instead of only changing after an explicit provider status call. `snapshots`
also inspects isolated worktree provider containers from the worktree provider settings, and the reducer
emits missing provider boot nodes for expected CGC/GrepAI roles when runtime/configured evidence is absent.
The provider surface therefore distinguishes observed, configured-only, failed/degraded, and missing roles.

Task 28 adds the **NOTIFY-AND-CONTINUE turn end** to this route — the new ACTIVE turn-end path that
supersedes (but parks, un-hinted) the `lifecycle_gate`/inbox stack. The write side gains a non-terminal
`awaiting-developer` state in `lifecycle_state.py` (since 260731-EFA-L4 its non-terminality is
structural rather than a second opinion: it is a member of `LiveState`, and `TERMINAL_STATES` is
built from the *other* half of the partition, so it cannot be in both) plus
`ambient.await_developer(*, summary)` / `resume_from_await` — a `block`/`resume` peer with no gate and no
wait (the model declares the turn complete and stops), `resume_from_await` kept a separate method so
`resume` keeps its blocked-only guard. The read side folds it in `reducer.py`: a
`lifecycle.awaiting-developer` arm rides the turn-end `summary` on the `ask` carrier (cleared on
`lifecycle.resumed`), `_lifecycle_attention` raises a single `info` "Turn complete — your move" item via
the new `_await_summary` helper, and its blocked branch is narrowed to `... and lifecycle.gate is None` —
the one-line dedup that fixes the gate-open/blocked-gate double-emission when a durable open gate is
already materialized by `_attach_gates`/emitted by `_gate_attention`.

Task 28 S5.2 makes attention dismissal lifecycle-scoped instead of append-only suppression history.
`AttentionDismissalStore` stores compact current acknowledgements keyed by item id; `reducer.py`
honors them only when the item lifecycle id matches and the acknowledgement is at or after the item's
`signalTs`; `projection_store.py` prunes acknowledgement rows for lifecycles outside the projected live
set on each tick. Gate-open attention is consumed by cancelling/deleting the gate source itself.

Task 29 makes the throwaway event/runtime surfaces lifecycle-aware at the backend boundary. The raw
Event River now uses `event_retention.py` for cursorless fresh-connect offsets, one-hour terminal
lifecycle pruning, and workspace age-window replay without a global count cap; the frontend no longer
adds a shorter row cap on top of this backend lifetime policy. `worktree_provider_admission.py`
derives active-enclosure worktree groups from enclosure contracts plus lifecycle logs: strict provider
groups admit only provider-relevant active lifecycle phases, while a broader active group keeps
non-terminal close/integration work visible in the Engine Room. `projection_store.py` reuses the same
lifecycle/enclosure pass, prunes expired event logs, filters stale provider/setup/engine facts before
projection, and caches repository surfaces on a short TTL so provider-state refreshes are not delayed by
repeated git probes. Task 29 S7 enriches actionable-drift attention with repository, branch,
source-root, memory-root, report-path, and checked-at provenance from the drift snapshot, and makes
actionable drift the only targetless attention class that can be dismissed. Task 34 re-keys this
raw-event retention on **inactivity** rather than the post-termination pruning above: a lifecycle's
`events.jsonl` is pruned after >1h with no real (non-heartbeat) activity (fleeting and enclosure alike,
not on `lifecycle.ended`), the `ambient.py` heartbeat ticker decays after ~10 min idle so a dormant log
goes quiet and ages out on its own, and a fresh `/api/events` connect replays only a bounded recent
window. L13 changes heartbeat storage from repeated JSONL appends to one atomic `heartbeat.json`
sidecar, merges that sidecar for reducer semantics without reparsing unchanged logs, and makes dormant
unprotected pruning reclaim the complete lifecycle directory.

Task 33 surfaces that active-enclosure admission to the dashboard Topology. `projection.py` gains the
served `WorkspaceProjection.activeWorktreeGroups: list[str]` (the worktree-group basenames with a live
enclosure lifecycle); `reducer.py`'s `project_workspace` accepts an `active_worktree_groups` kwarg and
stores it sorted on the projection; and `projection_store.project_and_write` passes the very
`active_enclosure_worktree_groups` set it already computes for the Engine Room — so the Topology and the
Engine Room share one definition of "active" while the shared `enclosures`/`lifecycles` collections keep
all-time history. `serving/delta.py` emits an `activeWorktreeGroups` whole-value delta when the set
changes.

**L5 (260628_operations-integration)** makes the **durable enclosure the source of truth for
liveness/retention**, fixing two coupled regressions introduced by Task 34's inactivity pruning. (1)
Admission no longer dies on a *missing* log: `admitted_worktree_groups` and
`active_enclosure_worktree_groups` only demote on a *present* terminal/post-phase log, so a running
worktree whose `events.jsonl` was pruned for inactivity stays in the Engine Room (before, it vanished an
hour after its last event). (2) A live master series **protects its whole history**:
`worktree_provider_admission.series_retained_lifecycle_ids` groups leaf enclosures by `(repoName,
taskName)` and returns every leaf id of any non-retired series; `projection_store.project_and_write`
reads enclosures first and passes that set to `event_retention.prune_expired_lifecycle_event_logs` as
`protected_lifecycle_ids`, exempting it from the inactivity TTL. A series retires only when every leaf
is archived (`cleanup` `completed`/`abandoned`, `ARCHIVED_CLEANUP_STATES`) **and** a one-week grace
(`MASTER_ARCHIVE_GRACE_SECONDS`, measured from the most recent finalized leaf contract mtime) has
elapsed. This durable-state retention deliberately **supersedes** the per-log inactivity TTL for
enclosure-backed work; fleeting/standalone logs (no `taskName`) keep the ordinary TTL.

## Hot Path Summary

Workspace event storage is bounded live by lock-guarded compaction plus virtual byte offsets;
lifecycle heartbeats are one coalesced sidecar per lifecycle; projection log parses survive heartbeat
ticks; and task/series broadcasts carry at most 250 body-free summaries with selected bodies loaded on
demand. Each projection tick now performs ONE shared leaf-contract enumeration+parse pass
(`contract_snapshot.py`, stat-identity cached across ticks) consumed by enclosures, engine facts, and
drift pruning. Accepted follow-ups remain explicit: task summary truncation/step-list bounds (N4), raw
sidecar timestamp compare (N6), and the workspace crash-window ordering note (N2).

## Route Model

- `events.py` — the `ar-observer-event/v1` Pydantic envelope (`Event`): the
  versioned record contract with Literal-typed `trust`/`actor` and camelCase
  wire fields. The persisted-record peer of the `models/` response contracts,
  but deliberately **not** an MCP response model (no token fields, never
  returned by a tool, not in `PUBLIC_TOOL_RESPONSE_MODELS`).
- `ulid.py` — `new_ulid()`: a local, stateless, dependency-free ULID mint
  (48-bit ms time + 80-bit random, Crockford Base32) so ids are
  lexicographically time-sortable and mintable without coordination.
- `store.py` — `EventStore`: resolves the per-lifecycle
  (`lifecycles/<id>/events.jsonl`) and workspace logs and appends events as
  JSONL.
- `event_retention.py` — raw Event River retention policy: fresh `/api/events`
  offsets for lifecycle/workspace logs, **inactivity-keyed** per-lifecycle log deletion
  (a fleeting or enclosure lifecycle log is pruned after >1h with no real, non-heartbeat
  activity — keyed on inactivity, **not** a `lifecycle.ended` event, so dormant logs age
  out on their own), and a bounded recent-window replay on a fresh connect (not
  whole-history). `prune_expired_lifecycle_event_logs` now takes a `protected_lifecycle_ids`
  exemption checked before dormancy (L5): logs in that set are never pruned by inactivity, so a
  live master series' history survives (the set comes from
  `worktree_provider_admission.series_retained_lifecycle_ids`). This backend policy is the Event
  River lifetime boundary; the dashboard keeps a memory-bounded sliding window but applies no
  shorter display cap.
- `lifecycle_state.py` — the state/phase vocabulary, the frozen `LifecycleState`
  record, the typed errors (`LifecycleError`, `GuardedStartError`,
  `LifecycleVocabularyError`), and the `coerce_phase`/`coerce_end_outcome` boundary
  validators. Pure vocabulary with no I/O, so the later projection slice can reuse it.
  Task 28: `State` gained the non-terminal `awaiting-developer` turn-end state.
  **260731-EFA-L4 declares `State` as a partition instead of one flat list.**
  `LiveState = Literal["running", "paused", "blocked", "awaiting-developer"]`,
  `EndOutcome = Literal["completed", "abandoned"]`, `TerminalState = EndOutcome`, and
  `State = Literal[LiveState, TerminalState]`. PEP 586 flattens nested `Literal`
  aliases, so `State` is exactly the same six-member union it was — `get_args(State)`
  still returns six plain strings — but the six names are now written once, on the
  halves, and `State` is composed from them. `TERMINAL_STATES` is no longer a
  `frozenset` standing beside `State` and naming two of its members a second time; it
  is `frozenset(vocabulary_names(TerminalState, ...))`, i.e. the terminal half read
  back. `STATES`/`LIVE_STATES`/`PHASES` are the same runtime read of the other
  aliases, so no module re-enumerates a vocabulary it does not own.
  `check_state_partition(live=, terminal=, whole=)` runs at import and raises
  `LifecycleVocabularyError` naming the offender for a state filed on both sides, a
  state on `State` filed on neither, and a filed state absent from `State` — the last
  of which is what makes appending a bare literal to the composition fail rather than
  quietly create an unclassified state. `vocabulary_names` is the reader underneath
  all of it: it walks flat literals, nested alias compositions and `X | Y` unions, and
  refuses any non-string member by name.
  `TerminalState` being *defined as* `EndOutcome` is the load-bearing part: terminality
  is not an opinion filed beside the states, it is "this is what `lifecycle.ended`
  writes", which is why `coerce_end_outcome` can be a membership test against
  `TERMINAL_STATES` rather than an outcome→state mapping table. It defaults an
  unrecognized or missing outcome to `DEFAULT_END_OUTCOME` (`"abandoned"`) — a policy
  for the *read* side, which parses logs it did not write.
- `save_gate.py` — the pure save-gate vocabulary: the landing-zone scope rule
  (`compute_scope` → `<repo_id>` / `0_unscoped` / `1_cross-repo`), the
  `SaveDecision` boundary (`coerce_save_decision`), and `SaveGateRequired`. No
  I/O, so the reducer can reuse the scope rule (slice 2c).
- `ambient.py` — `AmbientLifecycle`, the process-singleton current lifecycle: the
  signal state machine (start/block/resume/end/switch/phase) plus 2c
  `promote`/`attach` and the save gate, the choke-point `emit_tool` hook, the
  **activity-decaying** heartbeat ticker (task 34: it stops emitting after ~10 min with no
  real, non-heartbeat activity and resumes on the next real signal, so an idle lifecycle's
  log goes quiet and ages out under the inactivity retention), and the project-and-prune TTL
  sweep, plus the
  `ambient()`/`install_ambient`/`require_ambient`/`reset_ambient` registry. Task 28
  adds the `await_developer(*, summary)` / `resume_from_await` NOTIFY-AND-CONTINUE
  turn-end pair (no gate, no wait; a second resume path so `resume` keeps its
  blocked-only guard). 260707-HFX2-L2 adds a read-only `root` property
  (`self._store.root`) so a consumer outside this route — the MCP tool choke point in
  `mcp/tools/base.py` — can resolve the observer root and check the sibling `serving/` package's
  supervisor-sweep heartbeat on every tool call without constructing its own `McpRuntimeConfig`.
  260731-EFA-L4 puts `end(outcome)` on the shared vocabulary: it checks membership against
  `TERMINAL_STATES` and converts through `coerce_end_outcome`, so the write side has no
  outcome→state rule of its own. The two sides stay deliberately asymmetric — the WRITE side
  still *refuses* an unrecognized outcome with a `LifecycleError` naming the accepted set,
  because `coerce_end_outcome`'s default-to-abandoned leniency exists for the reducer reading
  logs it did not write, and a session ending itself must not have a typo silently recorded as
  an abandonment. The unsaved-work discard branch in the switch path keeps its literal
  `outcome="abandoned"`, which is a decision this branch makes rather than a classification;
  it is intentionally not wired to `DEFAULT_END_OUTCOME`.

The slice-3a projection read side:

- `timeutil.py` — the shared time leaf: `age_seconds`, the `Clock` alias, and the
  timing thresholds (`HEARTBEAT_SECONDS`/`STALE_AFTER_SECONDS`/`TTL_SECONDS`) the
  write side (ambient) and read side (reducer) both import, so they never drift.
- `paths.py` — `observer_root(config)`, the single store-root resolver shared by
  the writer (`server`) and the reader; dependency-light (no read-side imports).
- `drift_snapshots.py` — the shared drift-snapshot filename, exact removal, and
  worktree-orphan pruning helper used by the drift producer, projection tick,
  cleanup, and tests. Pruning consumes the shared per-tick `ContractSnapshot`
  when the projection injects one (PTS-L2), so it parses no contracts itself
  inside a tick.
- `contract_snapshot.py` — the shared per-tick leaf-enclosure-contract snapshot
  (260712-PTS-L2): `ContractSnapshot` (immutable, enumeration-ordered contracts +
  `skipped` parse failures) and `ContractSnapshotCache` (one enumeration +
  at-most-one parse per contract per tick; cross-tick parse cache keyed by
  `(mtime_ns, size, ctime_ns)` stat identity; failures never cached; entries
  pruned to the live enumeration), plus `build_contract_snapshot` for standalone
  reader calls. Mutated only inside the serialized projection tick; the cached
  contracts are shared across ticks and must never be mutated by consumers.
- `projection.py` — the projection schema (`LifecycleProjection`,
  `WorkspaceProjection`, `EnclosureNode`, `ProviderNode`, `Metrics`,
  `ActionAvailability`, slice 05 `AttentionItem` + `Analytics.attentionQueue`, and — slice 5e —
  `EngineProcessNode`/`CommitRefNode`/`ProviderBootNode`/`EngineProcessEdge` + `Analytics.engineProcesses`
  + the `EngineProcessFacts` input carrier, — R1/task 17 — `TaskDocNode.id`/`createdAt`,
  `SeriesNode`/`SeriesSubTaskNode` (including optional `createdAt`)/`SeriesSectionNode`
  + `Analytics.series`, and slice 6c `GateNode` + `LifecycleProjection.gate`): the persisted/served peer
  of `events.py`, **not** an MCP response model. Task 29 S7 adds drift-snapshot provenance fields for
  actionable-drift attention detail. 260703-L11 adds `EnclosureNode.codeWorktreeExists`/
  `memoryWorktreeExists` — worktree-existence truth stat'ed by the snapshots I/O layer, the tasks
  surface's visibility rule (`cleanup: reopened` = contract-reset-awaiting-restart, not live work).
  260703-L14 adds `TaskDocNode.orchestrates` (`list[str]`, default `[]`) — the schema's master-only
  orchestration-command list passed through by `snapshots._task_doc_node`, from which the dashboard
  derives the orchestration > master > leaf hierarchy and rank insignia (additive, no bump).
  260707-HFX2-L1 adds R1/R4 fields to `AgentPickupNode` (attempt/backoff/escalation/owner) and a new
  `ExpectationRowNode` + `Analytics.expectationRows` (R2/R5 durable deadline surfacing). `version` is 2.
  **260731-EFA-L4 makes the per-state `Metrics` buckets a function of the vocabulary.**
  `ACTIVE_STATES = LIVE_STATES` (the live half itself, deliberately *not* `STATES -
  TERMINAL_STATES`, so the answer is not re-derived from a second list that could be
  wrong); `state_count_field(state)` computes the bucket name — first segment verbatim,
  each later hyphen segment's first character upper-cased and its tail left alone, plus
  `Count`, so `awaiting-developer` → `awaitingDeveloperCount`; and `STATE_COUNT_FIELDS =
  state_count_fields(ACTIVE_STATES)` is the resulting one-to-one map. `state_count_fields`
  raises `LifecycleVocabularyError` naming both states if two ever bucket into one field —
  the transform is not injective (`a-b` and `aB` both give `aBCount`), and a shared bucket
  would make the later count overwrite the earlier in the reducer's keyword expansion, i.e.
  under-report with no field looking wrong. `Metrics` gains `awaitingDeveloperCount`, the
  bucket the turn-end state never had. The `*Count` fields stay hand-declared because they
  are the served contract the dashboard reads by name; what stops them drifting is that
  `Metrics` is `extra="forbid"` (a bucket the vocabulary needs but the model does not
  declare raises in `_metrics`, it does not become a silent zero) and that
  `MetricsBucketVocabularyTests` asserts the declared `*Count` set minus `lifecycleCount`
  equals the derived set in both directions.
  `str.capitalize` is specifically wrong here and the code says why: it lower-cases the
  tail, which both merges states differing only in tail case and disagrees with the
  TypeScript mirror's `Capitalize<>`, which cannot lower-case a tail.
- `reducer.py` — the pure fold: `project_lifecycle` (events → projection, with the
  inferred paused/abandoned layer, corrections, and token aggregation),
  `project_workspace` (tree assembly, including current-enclosure reconciliation for
  non-fleeting event-backed lifecycle rows), precomputed action availability, slice 05
  `build_attention_queue` (+ slice 5f S6 `_start_attention`, the blocked-start chat-parity source),
  and — slice 5e — `build_engine_processes` (the enclosure-centered process
  map joined on the worktree-group basename; slice 05l P1 filters disposed enclosures via
  `_is_disposed` and maps the `abandoned` guidance phase) + `_start_process_node` (pre-contract §5.4 synthesis).
  Task 28 adds the `lifecycle.awaiting-developer` fold arm (summary on the `ask` carrier),
  `_lifecycle_attention`'s `awaiting-developer` info item (via `_await_summary`), and the
  `... and lifecycle.gate is None` blocked-gate/gate-open dedup. Task 29 S7 keys actionable-drift
  attention by repository/branch, enriches its detail from snapshot provenance, and treats only
  actionable drift as targetless dismissible attention. 260731-EFA-L4 removes the last three
  places the reducer restated the vocabulary: `_metrics` builds its buckets as
  `Counter(lc.state for lc in lifecycles)` splatted through `STATE_COUNT_FIELDS` instead of
  three `sum(1 for lc in lifecycles if lc.state == ...)` lines (those three lines are what
  let an `awaiting-developer` lifecycle count towards `lifecycleCount` and `totalTokens` and
  towards nothing else); `_ended_updates` returns `coerce_end_outcome(event.data.get("outcome"))`
  instead of its own `"completed" if ... else "abandoned"`; and the module-level `_STATES`
  membership set is `frozenset(STATES)` rather than `frozenset(get_args(State))` — deliberately,
  because `get_args` on the *union* form (`Literal[...] | Other`) yields `Literal` objects
  rather than strings, and a set of those would match no event payload, silently dropping
  every state correction the fold applies.
- `series_tokens.py` — the pure series-token aggregate helper: indexes non-master task documents by
  series directory plus markdown filename, joins master `subTasks[].file` rows to bound leaf
  lifecycles, and returns copied `SeriesNode`s with `seriesTokenTotal`.
- `snapshots.py` — the file-surface readers reusing each producer's parser:
  structural (`read_providers` S1, `read_enclosures` S5/S6; enclosures now come from active leaf
  `enclosures/<leaf-id>/series-contract.md`, not root series contracts; since PTS-L2 the enclosure
  and engine-facts readers consume the shared per-tick `ContractSnapshot` instead of walking and
  parsing contracts themselves) from 3a, plus the
  slice-3b analytical readers (drift snapshot S9, sidecar staleness S11, setup
  summaries S2 + progress S3, route coverage S10, tool reports S12, ledger S8), the
  slice-3c task-document reader (`read_task_documents` S7, active JSON-primary docs with optional
  lifecycle attachment; leaf docs can bind through `enclosures[].enclosurePath` or structured leaf/root
  enclosure matches, contracts themselves are skipped, and task JSON scans skip archives plus enclosure
  folders), drift snapshots with `sourceRoot`, `memoryRoot`, optional `reportPath`, and `checkedAt`
  provenance,
  slice 5e `read_engine_process_facts` (contract + best-effort `status_payload` + `lifecycle_guidance`) +
  `read_start_progress_entries` (§5.4), the slice 6c `read_gates` reader (folds the `GateStore` logs for
  gate projection), plus — R1/task 17 — `read_series_documents` (`kind == "master"` docs keyed by task
  folder; the companion master aggregation surface) carrying master objective and sorting sub-task rows
  oldest-first by resolved sibling leaf `createdAt` only when every row has one.
- `provider_nodes.py` — the provider-node projection policy used by `snapshots.read_providers`: it expands
  CGC workspace current-state watcher rows and explicit GrepAI `targetRepos` into repo-scoped provider
  nodes, keeps unsupported providers aggregate, and builds isolated worktree provider nodes by
  `worktreeGroup`; configured-only worktree provider nodes stay distinct from observed runtime rows.
- `worktree_provider_admission.py` — active-enclosure admission for worktree runtime surfaces:
  strict groups for provider/setup alarms, broader non-terminal enclosure groups for Engine Room facts.
  A **missing** lifecycle log never retires a live enclosure (only a present terminal/post-phase one
  does) — the durable contract is the truth. Also derives `series_retained_lifecycle_ids` (+
  `_series_is_retired`/`_contract_finalized_at`, `ARCHIVED_CLEANUP_STATES`/`MASTER_ARCHIVE_GRACE_SECONDS`):
  every leaf id of a not-yet-retired master series, which the projection store feeds back to event
  retention as the protection set. 260731-EFA-L4 puts the module's last inline
  `{"completed", "abandoned"}` (in `_enclosure_is_provider_relevant`) onto
  `ARCHIVED_CLEANUP_STATES`, so all three archived-enclosure tests now read the one constant.
  Note the vocabulary boundary this respects rather than crosses: `ARCHIVED_CLEANUP_STATES` is
  the *contract cleanup* vocabulary (`worktrees.worktree_contract.CleanupStatus`, which also has
  `pending` and `reopened`), and it coincides with `TERMINAL_STATES` by value only — an
  enclosure being reclaimed and a lifecycle being over are different facts, so the two are
  deliberately not the same constant.
- `projection_store.py` — the I/O edge: `read_lifecycle_logs`, the atomic
  `latest-state.json`/`latest-metrics.json` writer, and the `project_and_write`
  orchestrator the serving layer drives. It prunes expired raw lifecycle event logs, derives admitted
  worktree groups before snapshot reads, and caches repository surfaces on a short TTL; live serving can
  install a TTL-gated provider refresher here before snapshot reads, while sim/tests can omit it.
  Since PTS-L2 it owns the module-level `_contract_snapshot_cache` and builds the ONE shared
  `ContractSnapshot` per tick that `read_enclosures`, drift-snapshot pruning, and
  `read_engine_process_facts` consume.

## Invariants And Boundaries

- **Single writer per lifecycle file.** A lifecycle is adopted by exactly one
  live session, so appends need no cross-process lock. Every event in a
  lifecycle file is written by that lifecycle's live owner; the only cleanup of a
  dead lifecycle is the TTL *prune* of a dormant fleeting log (a directory
  deletion), never a non-owner append.
- **Events are a persisted, versioned contract.** The envelope carries
  `schema = ar-observer-event/v1`; readers `model_validate` records back, so the
  format must round-trip. Always serialize with
  `model_dump_json(by_alias=True, exclude_none=True)`.
- **Replayability is a schema requirement.** Stable ordering (append order; ULID
  tie-break) and self-contained `lifecycle.started` events let one log replay one
  lifecycle's state alone — the same recorded log doubles as dev/test/demo/replay
  fixture.
- This route owns both sides: the write side + ambient lifecycle (signals +
  emission + heartbeat + TTL) **and** the read side — the pure reducer that owns
  interpretation (projection, state, metrics, staleness, action availability).
- The fold is pure: `project_lifecycle`/`project_workspace` take already-read
  inputs; all file I/O lives at the edge (`snapshots`, `projection_store`).
- Analytical surfaces are cheap reads (slice 3b): drift is read from a persisted
  snapshot, never re-classified in the reducer (git-per-sidecar stays in the
  on-demand drift tools); large inventories collapse to rollups + bounded samples
  so the served projection stays lean.
- **A best-effort reader on this route degrades; it never raises — and since
  260731-EFA-L3 that means catching the runner's timeout, not only `OSError`.**
  `_ledger_window` and `read_ledger` both promise that a missing, invalid or
  unreadable ledger yields an empty window or hash-only rows so the projection tick
  cannot fail. `_git_commit_meta` is the git probe underneath them, and it moved onto
  `kernel/git_command.py::run_git`, which — unlike the private copy it replaced —
  carries a timeout. `subprocess.TimeoutExpired` is a `SubprocessError` and
  `SubprocessError` is **not** a subclass of `OSError`, so a wedged `git log` would
  have escaped the old `except OSError`, travelled up through `_enrich_ledger_rows`
  and failed the whole tick. It now catches `(OSError, subprocess.SubprocessError)`.
  Any future reader here that consolidates onto the shared runner inherits the same
  obligation: the runner's failure surface is wider than a bare `subprocess.run` with
  no bound, and this route's degrade-never-raise promise is what pays for it.
- **Every lifecycle state joins the live half or the terminal half, and nothing on this
  route re-derives that split.** A seventh state is added to `LiveState` or to
  `TerminalState`; adding it to `State` directly fails `check_state_partition` at import,
  naming it. Filing it live grows `LIVE_STATES` → `ACTIVE_STATES` → `STATE_COUNT_FIELDS`,
  and `_metrics`'s splat then requires the matching `Metrics` field to exist — `extra="forbid"`
  turns a missing declaration into a `ValidationError` on the projection tick rather than a
  bucket that silently reads zero. Filing it terminal commits to it being reachable only
  through `lifecycle.ended`, because `TerminalState` *is* `EndOutcome`. What must not be
  re-introduced is a second list: a `frozenset` of terminal names beside `State`, an
  `ACTIVE_STATES` computed as `STATES - TERMINAL_STATES`, or a hand-written bucket list in
  `_metrics` — each of those is a copy that can disagree, and the `awaiting-developer` bucket
  gap is what disagreeing looked like.
- Derived states are flagged `inferred` so a renderer never shows a projected
  state as a written fact ("never pretend declared is observed").
- **Persistent lifecycle rows are current-enclosure-owned:** deleting or re-owning an enclosure removes
  the older non-fleeting lifecycle from `WorkspaceProjection.lifecycles`; fleeting lifecycles and fresh
  non-terminal promotion/gate windows are explicitly outside that deletion rule.
- **Task documents disappear only by archive/delete:** active JSON-primary task docs under
  `tasks/<repo>/...` project regardless of lifecycle binding or terminal status. Completed/abandoned
  status is filter/history state; moving the doc under `0_archive/` or deleting it is what removes it
  from Operations.
- **Masters have two surfaces:** `read_task_documents` projects the concrete active master document for
  direct selection, while `read_series_documents` also projects the folder-keyed checklist aggregation.
  Series progress reads the master's *declared* `subTasks[]`, never a slice's leaf steps. Leaf
  `series-contract.md` files are enclosure/process state, not task documents.
- **Series token totals are composed:** `seriesTokenTotal` is derived from already-projected
  task-document and lifecycle nodes, not read from the master JSON and not inferred from file names
  beyond the explicit master `subTasks[].file` join key.
- **Creation order is structured, not parsed:** task creation time comes from `ar-task-document/v1`
  `createdAt`; series sub-task ordering may use it when all referenced leaves resolve, otherwise the
  master-authored order remains authoritative.
- **Drift snapshot retention is physical, not only filtered:** configured-repo snapshots stay; valid
  worktree snapshots stay only while their leaf contract still points at an existing code worktree.
  Projection-time pruning removes valid orphaned snapshots before the analytical surface is read, and
  cleanup removes the exact snapshot for the contract it is reclaiming.
- **Raw event retention is inactivity-keyed (task 34), but a live master series supersedes it (L5):** a
  lifecycle log is pruned after >1h with no real (non-heartbeat) activity — fleeting and enclosure
  lifecycles alike — keyed on inactivity rather than a `lifecycle.ended` event, and the heartbeat ticker
  decays after ~10 min idle so a dormant lifecycle stops refreshing its own activity and ages out;
  workspace/lifecycle-less events retain only the short replay age window, and a fresh connect replays
  only a bounded recent window. **However**, every leaf of a not-yet-retired master series is passed as
  `protected_lifecycle_ids` and is exempt from this TTL — a running durable task never loses its (or a
  sibling leaf's) history; the series releases only when all leaves are archived plus the one-week
  grace. The frontend keeps a memory-bounded sliding window and virtualizes it, adding no shorter
  display cutoff.
- **The durable enclosure — not the lifecycle log — is the source of truth for liveness (L5):** a
  *missing* lifecycle log (pruned for inactivity) never retires a live enclosure from either admission
  set; only a *present*, genuinely terminal/post-phase log demotes it. This is what keeps a running
  worktree visible in the Engine Room even after its event log ages out.
- **Worktree runtime facts require active enclosure admission:** stale `provider-state.json`,
  setup-progress, or historical contract files do not page or feed process facts unless the enclosure's
  lifecycle is still active under the relevant provider/Engine Room boundary.

Since L15 the projection's now-relative `*Seconds` fields are formally classified: the serving
delta layer strips VOLATILE_AGE_FIELDS from the stable forms it diffs, and a reflection guard in
the serving tests forces every new `*Seconds` projection field to declare itself volatile or
content — an unclassified addition fails loudly instead of silently re-degrading the SSE stream.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The design this substrate implements (entities, store layout, retention, TTL project-and-prune). | [docs/design/observable-lifecycle.md](agents-remember/docs/design/observable-lifecycle.md) |
| The persisted-record envelope is the peer of the MCP response contracts. | [models/](agents-remember/mcp/src/agents_remember/models/) |
| Provider-node projection is a route-local read-side helper used by the snapshot reader. | [provider_nodes.py](provider_nodes.py) |
| Raw event retention is centralized before `/api/events` replay and projection ticks prune expired lifecycle logs. | [event_retention.py](event_retention.py) |
| Active-enclosure worktree admission gates provider/setup/runtime facts before projection. | [worktree_provider_admission.py](worktree_provider_admission.py) |
| Series token totals are composed by a reducer-side helper from projected task docs and lifecycles. | [series_tokens.py](series_tokens.py) |
| Drift snapshot pathing and worktree-orphan pruning are centralized for producer/projection/cleanup parity. | [drift_snapshots.py](drift_snapshots.py) |
| The shared per-tick contract snapshot and its cross-tick stat-identity parse cache (PTS-L2). | [contract_snapshot.py](contract_snapshot.py) |
| The span/heartbeat idiom the store generalizes (schema-versioned, atomic writes, stale projection). | [providers/setup_progress.py](agents-remember/mcp/src/agents_remember/providers/setup_progress.py) |
| The partition, coverage and terminality suites that hold the vocabulary to the buckets: `MetricsBucketVocabularyTests`, `StatePartitionTests`, `TerminalityIsStructuralTests`, `StateVocabularyReaderTests`, `StateCountFieldTests`. | [test_observer_projection.py](agents-remember/mcp/tests/test_observer_projection.py) |
| The write side's asymmetric refusal — `end()` rejects an unknown outcome instead of coercing it. | [test_observer_ambient.py](agents-remember/mcp/tests/test_observer_ambient.py) |
| The TypeScript mirror, which now carries the SAME partition shape as this route: `LIVE_STATES` / `TERMINAL_STATES` declared as halves, `LIFECYCLE_STATES` spread from them, and `ACTIVE_STATES = LIVE_STATES` rather than a difference. It refuses double-filing at compile time (`StatesAreFiledOnce`, a `never` constraint) where this route refuses it at import; the one thing it cannot follow is a duplicate WITHIN one half, which a TS tuple keeps and `Literal` collapses. | [dashboard/src/types/projection.ts](agents-remember/dashboard/src/types/projection.ts) |

## 260718-CHATS-L5I Current Route Impact

The observer now caches shared projection inputs per tick and slows repository-surface refresh to its appropriate operational cadence. It also freezes a fully observed completed landing result, validates that persisted projection before use, and returns a reopened or stale-final contract to the live sweep.

Route indexes are intentionally not regenerated during this partitioned curator pass; the manager will run the single aggregate refresh after all curator ownership is complete. Existing verification metadata remains pre-commit.

## 260727-CHATS-IM-L2 Route Impact

`projection_inputs.py` now owns fixed-slot domain snapshots and full/change/heartbeat refresh
semantics. `task_document_cache.py` owns bounded per-file parse reuse. The projection store remains
the atomic write edge, and snapshots remain the reader library; the change prevents one
lifecycle/heartbeat event from rereading unrelated task, drift, provider, repository, and Engine
Room surfaces.

## 260731-EFA-L2 Reducer Input Contract

`reducer.project_workspace` is now signed on **two frozen bundles that mirror the design's own two
slices**: `WorkspaceStructure` (3a — `enclosures`, `providers`, `active_worktree_groups`) and
`AnalyticalInputs` (3b — the sixteen analytical fields, every one defaulted). The long
keyword-optional list is gone; `given=None` is what still yields an empty `analytics`, preserving
the structural-only contract. `build_analytics(given, *, series, attention_queue,
engine_processes)` and `build_attention_queue(lifecycles, providers, given)` take the same bundle.

Two rules a future change must respect: a field belongs in `WorkspaceStructure` only if it leaves
through `WorkspaceProjection` rather than `Analytics` (which is why `active_worktree_groups` moved
there), and a new analytical input is a new defaulted field on `AnalyticalInputs`, never a new
`project_workspace` keyword.

On the read edge, `projection_store.project_and_write(config, *, now, refresh, tick)` carries its
long-lived collaborators in `ProjectionTickState`, and `ProjectionInputState.read` takes
`ProjectionReaders` + `RefreshPass`. The fold stays pure and every projected value is unchanged.

## 260731-EFA-L4 The State Vocabulary Is A Checked Partition

The defect this leaf closes on this route was not a typo, it was a **set difference**. `State`
declared six states; `Metrics` bucketed three by hand; `_metrics` counted those three with three
hand-written `sum(...)` lines. So an `awaiting-developer` lifecycle inflated `lifecycleCount` and
`totalTokens` and landed in no bucket at all — the rollup could not show a lifecycle that had
handed the turn back to the developer, and nothing anywhere failed.

The fix is structural, in three steps, each of which removes one copy that could disagree:

1. **`State` is composed, not declared.** `LiveState` and `TerminalState` hold the names;
   `State = Literal[LiveState, TerminalState]`. PEP 586 flattens nested `Literal` aliases, so the
   union is byte-for-byte the same six-member type a checker saw before — this buys checkability,
   not a new vocabulary. The state names are still hand-written, and always will be; what is gone
   is the *second* hand-written list. `check_state_partition` runs at import and refuses a state
   filed on both sides, on neither, or filed but absent from `State`.
2. **`TerminalState` IS `EndOutcome`.** A lifecycle reaches a terminal state exactly one way — by
   being ended — and `lifecycle.ended`'s `outcome` names which one. So terminality stops being an
   opinion in a set and becomes "this is what ending writes", which is why `coerce_end_outcome` is
   a membership test rather than a mapping table, and why the reducer and `AmbientLifecycle.end`
   share it instead of each carrying a `"completed" if ... else "abandoned"`.
3. **The buckets are computed from the live half.** `ACTIVE_STATES = LIVE_STATES` (not
   `STATES - TERMINAL_STATES`), `state_count_field` derives the *field name* from the state name,
   and `STATE_COUNT_FIELDS` is the one-to-one map `_metrics` splats. Two states that would collide
   on one bucket are refused where the map is built, because the splat is keyed by bucket and a
   collision would silently drop a count.

**What is genuinely derived and what is not, stated plainly.** `STATES`, `LIVE_STATES`,
`TERMINAL_STATES`, `PHASES`, `ACTIVE_STATES` and `STATE_COUNT_FIELDS` are all read out of the
`Literal` aliases at runtime (`vocabulary_names` → `get_args`); none of them is a list of strings
typed a second time. The `Metrics.*Count` *field declarations* are still hand-written, and
deliberately so — they are the served contract the dashboard reads by name and pyright checks by
name, and pydantic has no way to synthesize them from a mapping. That remaining hand-written half
is closed on both sides rather than trusted: `extra="forbid"` makes an undeclared bucket raise
inside `_metrics` on the projection tick, and `MetricsBucketVocabularyTests` asserts the declared
set equals the derived set in both directions (a bucket no state can fill fails too). The coverage
test also re-derives the live set as `STATES - TERMINAL_STATES` on purpose, so the measurement is
not taken with `ACTIVE_STATES`, the instrument it is checking.

Two smaller boundary widenings ride along in `snapshots.py`: `read_engine_process_facts` passes
`dict(lifecycle_guidance(contract))` and `_cached_local_status` passes
`dict(projected_status_payload(...))`. Both producers now return TypedDicts
(`guidance.LifecycleGuidance`, `guidance.WorktreeStatusPayload`); `EngineProcessFacts` is the
projection's untyped input carrier that the reducer folds by key name, so the widening is at the
carrier, not in the producers.

## Update History

- 2026-08-01T10:45+02:00 — 260731-EFA-L4 curator (post-wave source change), **one corrected claim
  only**: `dashboard/src/types/projection.ts` adopted this route's partition after the 09:26 entry
  below was written, so the Repo-Internal References row calling it "the TypeScript mirror that
  still carries the two-list shape this route dropped" became false. Verified against the current
  file: `LIVE_STATES` (L42) and `TERMINAL_STATES` (L48) are the halves,
  `LIFECYCLE_STATES = [...LIVE_STATES, ...TERMINAL_STATES]` (L59), and `ACTIVE_STATES = LIVE_STATES`
  (L72) — not a difference. The row now records what the two sides share and the one asymmetry that
  remains (a duplicate within one half: `Literal["a","a"]` collapses here, a TypeScript tuple does
  not, so the mirror falls back to a runtime check). `projection.py`'s "STATE OF THE MIRROR" comment
  (L194-L226) was rewritten in the same change and now says the same thing. Nothing else on this
  route was touched — the `260731-EFA-L4 The State Vocabulary Is A Checked Partition` section
  (L615-L659) was re-read and every claim in it still holds.
- 2026-08-01T09:26+02:00 — 260731-EFA-L4 curator: the state vocabulary became a **checked
  partition** and the metrics buckets became a function of it, so this route's model was corrected
  rather than attested. Recorded that `State = Literal[LiveState, TerminalState]` (PEP 586 flattens
  nested aliases — verified at runtime: `get_args(State)` returns the same six plain strings), that
  `TERMINAL_STATES` is now the terminal half read back rather than a set standing beside `State`,
  and that `check_state_partition`/`vocabulary_names`/`LifecycleVocabularyError` refuse a
  mis-filed or unfiled state at import. Recorded `TerminalState = EndOutcome` as the load-bearing
  identity that lets `coerce_end_outcome` be a membership test, and the deliberate write/read
  asymmetry (`AmbientLifecycle.end` refuses an unknown outcome; the reducer coerces it, because it
  parses logs it did not write). On the projection side, recorded `ACTIVE_STATES`,
  `state_count_field`, the collision-refusing `state_count_fields`, `STATE_COUNT_FIELDS` and the
  new `Metrics.awaitingDeveloperCount`, plus the reducer's `Counter` + splat replacing the three
  hand-written `sum(...)` lines and `_ended_updates`/`_STATES` moving onto the shared vocabulary.
  **Answered the derivation question explicitly in the body rather than leaving it implied:** the
  maps are genuinely derived at runtime; the `Metrics.*Count` field *declarations* remain
  hand-written by design and are held to the derivation by `extra="forbid"` plus a bidirectional
  test — so this is not a relocated hand-written list, but it is not a fully generated model
  either, and the card now says which is which. Added the partition invariant (what a seventh state
  must do, and which three second-lists must never come back), corrected the Task-28 parenthetical
  that still described `awaiting-developer`'s non-terminality as an absence from `TERMINAL_STATES`,
  noted `worktree_provider_admission.py`'s last inline `{"completed","abandoned"}` moving onto
  `ARCHIVED_CLEANUP_STATES` **and** why that constant is deliberately not `TERMINAL_STATES` (it is
  the contract-cleanup vocabulary, equal by value only), and recorded the two `snapshots.py`
  TypedDict boundary widenings. Added three reference rows, including the TypeScript mirror
  (`dashboard/src/types/projection.ts`, owned elsewhere and untouched here), which still carries
  the two-list shape this route dropped — verified against that file: `LIFECYCLE_STATES` and
  `TERMINAL_STATES` are two independent hand-written lists and `ACTIVE_STATES` is their difference.
  Verification metadata pinned until closeout stamps the L4 commit.

- 2026-07-31T22:45+02:00 — 260731-EFA-L3 curator (re-verification pass): **the "No route impact"
  attestation below no longer covers `snapshots.py`, which changed again after it was written.**
  `_git_commit_meta` widened `except OSError` to `except (OSError, subprocess.SubprocessError)`, and
  that is a route fact rather than a local tidy-up: the entry below attested "same `{}`-on-failure
  contract", and the failure *set* is what moved. Consolidating this probe onto
  `kernel/git_command.py::run_git` gave it a timeout it never had, and
  `subprocess.TimeoutExpired` is a `SubprocessError`, which is not an `OSError` — so a wedged
  `git log` would have escaped `_enrich_ledger_rows` and failed the projection tick, breaking the
  promise `_ledger_window` and `read_ledger` both document (an unreadable ledger degrades to
  hash-only rows, never to an exception). Recorded that as an invariant under Invariants And
  Boundaries, stated as an obligation on any future reader here that moves onto the shared runner,
  because the reasoning generalizes and the next such consolidation will not come with a comment.
  Re-checked the rest of the earlier attestation against the current source and it still holds:
  same argv, same one-`git log`-per-repo batching, same never-faked metadata, same
  `--ignore-missing` fallback to the bare hash. The reader/reducer/projection split, the pure fold
  and the surface inventory are untouched. Verification metadata pinned until closeout stamps the
  L3 commit.

- 2026-07-31T21:03+02:00 — 260731-EFA-L3 curator: No route impact: the leaf's only change under this
  route is one import line in `snapshots.py` — `run_git` now comes from
  `agents_remember.kernel.git_command` instead of `agents_remember.worktrees.modules.git`, because
  the six near-identical private copies of that function were consolidated onto the kernel owner
  (`worktrees/modules/git.py` no longer defines one; it imports the same kernel function). Checked
  the one caller,
  `_git_commit_meta`'s batched `git log --no-walk --ignore-missing --format=%H%x1f%cI%x1f%s` for
  `_enrich_ledger_rows`, against the current source: same argv, same one-subprocess-per-repo shape,
  same `{}`-on-failure contract, same never-faked metadata. Checked this overview's three git claims
  against the code — "git-free sidecar staleness" (Purpose), "provider-state refreshes are not
  delayed by repeated git probes" (Purpose) and "git-per-sidecar stays in the on-demand drift tools"
  (Invariants) — all still hold. The observer's surface inventory, reader/reducer/projection split
  and pure-fold boundary are untouched; which module the runner is imported from was never a fact
  this overview stated.
- 2026-07-31T00:00+02:00 — No route impact on behaviour: 260731-EFA-L2 re-signed the reducer and
  the projection input/write edge onto parameter objects (`WorkspaceStructure`/`AnalyticalInputs`,
  `ProjectionTickState`, `ProjectionReaders`/`RefreshPass`/`ActiveGroups`, `AmbientTiming`) and
  turned `_apply_kind` into the `_KIND_UPDATES` dispatch table. Projected output is byte-identical;
  the read/write split and the pure-fold boundary are unchanged. Detail in the per-file sidecars.
  Verification metadata pinned until closeout stamps the L2 commit.
- 2026-07-30T12:51+02:00 — 260727-CHATS-IM-L2 curator: added
  `projection_inputs.py` and `task_document_cache.py`. The serialized worker now retains
  domain-owned snapshots, refreshes only watcher-invalidated domains, advances heartbeat ages
  without heavy rereads, reparses only changed/new task documents, and reclaims deleted rows on
  the owning-domain refresh. Verification metadata remains pinned until closeout.

- 2026-07-24T13:18:47Z — 260718-CHATS-L5I curator: updated the route body for the current backend/shared behavior; aggregate route-index generation remains manager-owned.
- 2026-07-12T20:02+02:00 — 260712-PTS-L2 route impact: added `contract_snapshot.py` to the route
  model — ONE shared leaf-contract enumeration+parse pass per projection tick (built in
  `projection_store`, consumed by `read_enclosures`, `read_engine_process_facts`, and drift-snapshot
  pruning; previously three independent walks per 1s tick, py-spy 2026-07-12: 2.78s/3.68s/3.40s in a
  15s sample), with a cross-tick parse cache keyed by `(mtime_ns, size, ctime_ns)` stat identity and
  the consumers-never-mutate-contracts concurrency rule. Landing refresher and supervisor sweep
  deliberately keep their own passes. Verification metadata pinned until closeout stamps the PTS-L2
  commit.
- 2026-07-12T17:30+02:00 — 260712-TRH-L7: observer projection now consumes a network-free immutable landing snapshot; `LandingStateRefresher` owns bounded background observation, exact-contract isolation, stale carry-forward, and safe cancellation.

- 2026-07-10T01:14+02:00 — 260707-HFX2-L13 route impact: documented live virtual-cursor river
  compaction, coalesced heartbeat storage plus complete lifecycle reclamation, body-free bounded task
  summaries, and the confined on-demand body reader; retained accepted N2/N4/N6 limits. Verification
  metadata remains pinned until closeout stamps the eventual L13 code commit.

- 2026-07-09T19:31+02:00 — 260707-HFX2-L12: reviewed route impact for the CS-6 store/projection/process scaling sweep and updated the route summary for changed files. Verification metadata pinned until closeout stamps the HFX2-L12 commit.
- 2026-07-08T18:45+02:00 — 260707-HFX2-L2 route impact (small): `ambient.py`'s `AmbientLifecycle`
  gained a read-only `root` property (`self._store.root`) so the MCP tool choke point
  (`mcp/tools/base.py`) can resolve the observer root and check the sibling `serving/` package's
  supervisor-sweep heartbeat on every tool call, without constructing its own `McpRuntimeConfig`.
  One-line accessor, no new state, no change to the write/read-side contract this overview
  describes. Verification metadata pinned until closeout stamps the 260707-HFX2-L2 commit.
- 2026-07-08T14:50+02:00 — 260707-HFX2-L1 route impact: R5 projection surfacing —
  `AgentPickupNode` gained the R1 ack/backoff fields + R4 owner fields (already-derived, read
  straight off `OperatorInboxEntry`); a new `ExpectationRowNode` + `Analytics.expectationRows`
  (from `snapshots.read_expectation_rows`) surfaces R2's durable deadline rows for dashboard/
  architect observability. Surfacing only — L2 (a sibling leaf) reads the underlying stores
  directly for correctness, never this projection. Verification metadata pinned until closeout
  stamps the 260707-HFX2-L1 commit.

- 2026-07-07T10:55+02:00 — L15 route impact (body): the volatile-vs-content classification of projection *Seconds fields documented. Verification metadata pinned until closeout stamps the L15 commit.

- 2026-07-07T05:42+02:00 — 260703-L15 attestation + one bound: reviewed this overview against the
  L15 reducer change — `reducer.py`'s `token_series` now decimates the served fuel gauge past
  `TOKEN_SERIES_MAX` (512; newest 256 exact, older history uniform-thinned, log untouched). The
  route model's reducer description otherwise still holds; details live in the `reducer.py`
  sidecar. Verification metadata pinned until closeout stamps the L15 commit.
- 2026-07-06T23:59:18+02:00 — 260703-L14 (visual hierarchy + chat grouping) route impact:
  `TaskDocNode.orchestrates` (additive `list[str]`, projection.py) + the `snapshots._task_doc_node`
  pass-through — the orchestration-command relation rides the served projection so the dashboard
  can nest commanded masters under their orchestration task; no reader/admission logic changed, no
  version bump. Verification metadata pinned until closeout stamps the L14 commit.
- 2026-07-06T02:15+02:00 — 260703-L11 route impact: `EnclosureNode` gains additive
  `codeWorktreeExists`/`memoryWorktreeExists`, stat'ed by
  `snapshots._enclosure_from_contract` at snapshot time (the `status_payload`
  probes), so tasks-surface visibility is physical worktree existence — never a
  cleanup-state proxy; `cleanup: reopened` documented as
  contract-reset-awaiting-restart. Verification metadata pinned until closeout
  stamps the L11 commit.
- 2026-07-05T01:32+02:00 — No route impact: reducer phase-inference comment re-worded (lifecycle phase, not l-01 phase); no behavior change (260703-L9).
- 2026-07-04T12:32+02:00 — 260703-L4 route impact: gate projection now surfaces
  `evidenceRefs` on `GateNode`, preserving reviewer-verdict references for
  delegated approval rows. Verification metadata pinned until closeout stamps
  the L4 commit.
- 2026-07-04T12:31+02:00 - L3 route impact: pending inbox pickups now surface
  role/message/artifact and hosted-delivery metadata for dashboard-visible
  agent-to-agent comms. Verification metadata pinned until closeout stamps the
  L3 commit.
- 2026-07-03T00:35+02:00 — L11 route impact: the reducer terminalizes lifecycles anchored to cleanup=abandoned enclosures and skips persistent synthesis for abandoned/reopened enclosures (reader-projected terminality per the store's single-writer invariant).
- 2026-07-02T21:45+02:00 — L10 route impact: `snapshots.read_task_documents` binds a leaf task doc to
  its active enclosure lifecycle by a **case-insensitive** `(taskRoot, enclosure.leafId)` join against
  the doc's authored `id` (filename stem kept as a lowercased legacy alternative). Enclosure leaf ids
  are slugified lowercase directory names while doc ids are authored uppercase, and series leaf docs
  carry no `enclosures[]` refs, so the previous fallbacks were dead — active-enclosure leaf docs
  projected with `lifecycleId: null`, breaking the sidebar content binding and the viewed-leaf chat
  chain. Verification metadata pinned until closeout stamps the L10 commit.
- 2026-06-30T00:00:00+02:00 — L5 (260628_operations-integration) route impact: the **durable enclosure is the source of
  truth for liveness/retention**. Documented the L5 narrative + invariants + Route Model bullets:
  admission no longer dies on a missing (pruned) log (`admitted_worktree_groups` /
  `active_enclosure_worktree_groups` only demote on a *present* terminal/post-phase log — fixes the
  disappearing-worktree regression), and a not-yet-retired master series protects every leaf's event log
  from the inactivity TTL via `series_retained_lifecycle_ids` → `event_retention`'s
  `protected_lifecycle_ids` (retire = all leaves archived + one-week grace from the last finalized
  contract). Verification metadata pinned until closeout stamps the L5 code commit.
- 2026-06-28T13:54+02:00 — Task 34 route impact: raw Event River retention is now **inactivity-keyed**
  rather than termination-keyed — `event_retention.py` prunes a fleeting or enclosure lifecycle log after
  >1h with no real (non-heartbeat) activity (not on `lifecycle.ended`), `ambient.py`'s heartbeat ticker
  decays after ~10 min idle so a dormant lifecycle stops refreshing its own activity and ages out, and a
  fresh `/api/events` connect replays only a bounded recent window. Updated the `ambient.py` /
  `event_retention.py` Route Model bullets, the retention invariant, and the Task-29 retention narrative.
  Verification metadata pinned until closeout stamps the task-34 code commit.
- 2026-06-28T07:45+02:00 — Task 33 route impact: `projection.py`/`reducer.py`/`projection_store.py` now expose
  `WorkspaceProjection.activeWorktreeGroups`, sourced from `active_enclosure_worktree_groups` (shared with
  the Engine Room) and consumed by the dashboard Topology for active-enclosure scoping. Verification
  metadata pinned until closeout stamps the code commit.
- 2026-06-28T07:43+02:00 — Task 29 S7 route impact: actionable-drift attention now carries
  repository/branch/source/memory/report/checked-at provenance, uses checked-at as the signal time,
  and is the only targetless dismissible attention type. The raw Event River lifetime remains owned by
  backend retention, with no shorter frontend row cap. Verification metadata pinned until closeout
  stamps the task-29 code commit.
- 2026-06-28T05:38+02:00 — Task 29 route impact: added lifecycle-aware raw
  Event River retention, active-enclosure worktree provider admission, broader active Engine Room
  admission, projection-time expired-event pruning, and a short repo-surface cache so stale worktree
  runtime files no longer page or dominate refresh cost. Verification metadata pinned until closeout
  stamps the task-29 code commit.
- 2026-06-28T03:52+02:00 — Task 28 S5.2 after source sync: route now documents
  lifecycle-scoped attention acknowledgements, reducer signal anchors, and projection-time pruning of
  acknowledgement rows for non-live lifecycles. Verification metadata pinned until closeout stamps the
  task-28 code commit.
- 2026-06-28T03:33+02:00 — Task 32 memory-mirror pruning: added `drift_snapshots.py` to the
  route model and documented the physical retention boundary for configured repositories, active
  worktrees, projection pruning, and cleanup removal. Verification metadata pinned until closeout stamps
  the task-32 code commit.
- 2026-06-28T03:21+02:00 — Task 31 route impact: provider snapshots now refresh live provider current-state
  through the projection-store seam, worktree provider facts inspect isolated Docker containers from the
  provider settings, and the reducer emits `missing` provider boot nodes for expected CGC/GrepAI roles with
  no evidence. Added focused tests for provider state refresh, worktree provider inspection, missing-role
  projection, Operations nesting, and the `_inspect_result_map` CRAP regression. Verification metadata
  pinned until closeout stamps the task-31 code commit.
- 2026-06-27T22:00+02:00 — Task 28 (NOTIFY-AND-CONTINUE turn end): documented the new ACTIVE turn-end
  path across this route — the non-terminal `awaiting-developer` state in `lifecycle_state.py`, the
  `ambient.await_developer`/`resume_from_await` signal pair (no gate, no wait; `resume` keeps its
  blocked-only guard), and the reducer's `lifecycle.awaiting-developer` fold arm + `_lifecycle_attention`
  `awaiting-developer` item (`_await_summary`) + the one-line `lifecycle.gate is None` blocked-gate/gate-open
  dedup. The old `lifecycle_gate`/inbox stack is parked (kept, un-hinted). Verification metadata pinned
  until closeout stamps the code commit.
- 2026-06-26T20:18+02:00 — Task 21 series token rollup: documented `SeriesNode.seriesTokenTotal` and
  the `series_tokens.py` helper that composes the aggregate from projected sibling task documents and
  lifecycle token totals. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-26T15:13+02:00 — Task 25 lifecycle live-row cleanup: the observer route now documents
  current enclosure ownership as the live boundary for non-fleeting lifecycle rows, with explicit
  exceptions for fleeting lifecycles and fresh non-terminal promotion/gate windows. Verification metadata
  pinned until closeout stamps the code commit.
- 2026-06-26T14:16+02:00 — No route impact: task 25 only clarifies `ambient.build_ask`/`block` as the shared ask path used by `lifecycle_gate`; the observer route model is unchanged.
- 2026-06-25T13:20+02:00 — Task 23/24: observer route now covers TTL-compacted gates and `AgentPickupNode` waiting-for-agent/check-chat projection.
- 2026-06-24T18:11+02:00 — Task 17 observer route correction: `TaskDocNode.id` now exposes the
  JSON-primary task id for authored leaf labels, separate from parent `subTasks[].number` fallback data.
  Verification metadata pinned until closeout stamps the code commit.
- 2026-06-24T16:39+02:00 — Task 17 Operations route correction: active JSON task docs now project
  independently of lifecycle/enclosure binding, `TaskDocNode.lifecycleId` is optional runtime context,
  master docs project on both task-document and series surfaces, and archive/delete is the Operations
  disappearance boundary. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-24T12:21+02:00 — Task 17 route impact: the observer projection now carries task/series
  `createdAt` metadata, master `objective`, and a series-reader ordering rule that uses resolved leaf
  creation times only when complete. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-24T08:59+02:00 — Task-document correction: clarified that `read_task_documents` may use
  enclosure metadata to bind a real JSON task document to a lifecycle, but never projects
  `series-contract.md` itself as readable task content. Verification metadata pinned until closeout
  stamps the code commit.
- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: observer snapshots now read only active leaf `enclosures/<leaf-id>/series-contract.md` contracts for live enclosures/engine processes, project `enclosureId`/`leafId`/`taskRoot`, bind leaf task docs through `enclosures[].enclosurePath`, and skip `0_archive` plus enclosure folders in task JSON scans. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-23T22:31+02:00 — Task 12 S2 clarification: provider projection now documents GrepAI as one
  aggregate provider instance with individually addressable `targetRepos`, and worktree GrepAI as the
  same multi-root shape with only the active project root redirected. Verification metadata pinned until
  closeout stamps the S2 code commit.
- 2026-06-23T22:09+02:00 — Task 12 S2 correction: GrepAI workspace current state now persists
  configured repository memory-root targets as `targetRepos`, so the observer route projects those
  memory roots as repo-scoped workspace provider nodes instead of treating GrepAI as unmapped.
  Verification metadata pinned until closeout stamps the S2 code commit.
- 2026-06-23T21:46+02:00 — Task 12 S2 route impact: added `provider_nodes.py` to the read-side route
  model; `snapshots.read_providers` now delegates provider-node policy there so CGC workspace
  `resources.watchers` rows project as repo-scoped provider nodes. Later 22:09/22:31 entries document the
  GrepAI `targetRepos` correction. Verification metadata pinned until closeout stamps the S2 code commit.
- 2026-06-23T01:40+02:00 — No route impact: slice 07b v1, `ambient.emit_read_packet` now takes the read's `repo_id` (signature `emit_read_packet(repo_id, files)`) and carries it as `data.repoId` on the `read.packet` (a fact, distinct from the envelope `repoId`); the facts-only per-file projection and this route's reader/reducer/projection split are unchanged (detail in the `ambient.py` sidecar). Verification metadata pinned until closeout stamps the slice-07b code commit.
- 2026-06-23T00:53+02:00 — No route impact: slice 07 S5 retargets the `served_store.py` module docstring only — the `compact-reset.json` producer is deferred to the post-3.0 agentic-control-plane (no session-hook producer), with the controller-side consumer + `refresh=true` kept as defensive scaffolding; the `ServedRecord`/`ServedStore` surface and this route's reader/reducer/projection split are unchanged (detail in the file sidecar). Verification metadata pinned until closeout stamps the slice-07 code commit.
- 2026-06-21T06:40+02:00 — Slice 05m (carryover-before-cleanup): extended the **Engine Room** surface in this route's reducer — `_GUIDANCE_PHASE` gained `"carryover-pending": "carryover-pending"` (surfaces guidance.py's new carryover phase, between integration and cleanup, to the process-map vocabulary), and `_engine_process` maps the additive `EngineProcessNode.carryoverDoneAt` (the carryover milestone ISO time, read off the official ledger by `guidance.carryover_done` and surfaced through `status_payload`; `None` until carried, display-only — 5k renders the seam). Added a Purpose paragraph; both reducer changes are additive so prior fixtures + the live feed are unchanged. The carryover/cleanup lifecycle correctness itself lives in the `worktrees/modules/` overview. Verification metadata pinned until closeout stamps the 05m code commit.
- 2026-06-21T05:30+02:00 — Slice 05l Part 2 (landing-arc probe hardening): refreshed this route's successful-landing-arc paragraph for the display-only `LandingRefNode.at` (gh's PR milestone timestamp — mergedAt once merged, else createdAt), which the reducer's `LandingRefNode(**ref)` splat picks up from the `worktrees/modules/landing.py` probe with no reducer change, and added `origin/<base>` to the participant list. The probe-side hardening (direct `origin/<base>` `ls-remote`, `_default_branch`) lives in the `worktrees/modules/` overview; this route's reducer/schema split is otherwise unchanged. Verification metadata pinned until closeout stamps the 05l-P2 code commit.
- 2026-06-21T04:10+02:00 — Slice 05l Part 1 (backend teardown visibility): extended the **Engine Room** surface in this route's reducer — `_GUIDANCE_PHASE` gained `"abandoned": "abandoned"` (surfaces guidance.py's new abandoned phase to the process-map vocabulary), and a new `_is_disposed(fact)` (True when the contract's `cleanup` is `completed`/`abandoned`) now filters `build_engine_processes` so a disposed enclosure drops from the active `Analytics.engineProcesses` (the frontend 05k animates the removal); `cleanup-pending` is intentionally kept. No new schema or surface — additive reducer logic. Verification metadata pinned until closeout stamps the 05l-P1 code commit.
- 2026-06-21T02:44+02:00: Slice 6g — extended the task-document surface for series navigation: `read_task_documents` started taking `enclosures` for runtime attachment and resolves **cross-master links** via the new `_ref_lifecycle`/`_task_doc_node` helpers (subTask `file`→`linkedLifecycleId`; doc `master` ref→`masterLifecycleId`); `projection.TaskDocNode` gains `subTasks`/`sections`/`masterLifecycleId` + the `TaskSubTaskRefNode`/`TaskSectionNode` nodes. Later Task 17 narrowed master runtime attachment to structurally root lifecycles. Additive, no `version` bump. Verification metadata pinned until closeout stamps the 6g code commit.
- 2026-06-19T03:17+02:00 — Slice 3c reopened (R1, masters observable): added the **series/master surface** to this route — `snapshots.read_series_documents` (`kind == "master"`, keyed by task folder), the `SeriesNode`/`SeriesSubTaskNode`/`SeriesSectionNode` schema nodes + additive `Analytics.series` in `projection.py`, and the `series` threading through `build_analytics`/`project_workspace`/`project_and_write`. Later Task 17 made master docs a dual-surface case: concrete task document plus folder-keyed series aggregation. Verification metadata pinned until closeout stamps the R1 code commit.
- 2026-06-18T21:25+02:00 — No route impact: slice 5h Tier 2 enriches the ledger-window rows with the per-side commit message + committer date — one batched, best-effort `git log --no-walk --ignore-missing` per repo in the `snapshots` I/O layer (`_git_commit_meta` / `_enrich_ledger_rows`; `_ledger_window` / `read_ledger` gained `code_root`/`memory_root` params), still passed through the pure reducer. The observer's surface inventory + reader/reducer/projection split this overview describes is unchanged (best-effort git at the I/O edge is already an invariant here) — detail in the `snapshots.py` / `projection.py` / `projection_store.py` sidecars. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-18T18:00+02:00 — No route impact: slice 5h ledger popover adds additive `LedgerNode.rows` (surface 8) + `EngineProcessNode.ledgerRows`/`ledgerRowCount`, read best-effort in `snapshots` (`_ledger_window` + `read_ledger`) and passed through the pure reducer; the observer's surface inventory + reader/reducer/projection split this overview describes is unchanged — detail in the file sidecars. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-18T14:05: Task 6 slice 6c Part A — added **gate projection** to this route: `snapshots.read_gates` folds the `GateStore` logs, `reducer._attach_gates` materializes each lifecycle's latest open gate onto `LifecycleProjection.gate` (`GateNode`), and `_gate_attention` raises a `gate-open` attention item, threaded through `project_workspace` / `project_and_write`. Verification metadata pinned until closeout stamps the 6c Part A code commit.
- 2026-06-18T08:51+02:00: Slice 5h H1 — extended the Engine Room surface with the successful-landing arc: additive `LandingRefNode` + `EngineProcessNode.landing`/`integrationStrategy` in `projection.py`, the composer mapping in `reducer.py` (reads `status["landing"]`), fed by the new best-effort `worktrees/modules/landing.py` probe. Verification metadata pinned until closeout stamps the 5h code commit.
- 2026-06-16T03:25: Slice 5f S6 (§9) — closed the blocked-start observability gaps in this route's reducer: `build_attention_queue` gained a `start_progress` param + the `_start_attention` builder (a pre-contract blocked start raises the same master-caution the agent raises in chat), threaded via `project_workspace`'s `engine_start_progress`. (The happy-path start-progress emit lives in `worktrees/modules/start.py`.) Verification metadata pinned until closeout stamps the S6 code commit.
- 2026-06-15T19:35: Slice 5e — added the **Engine Room process-map** surface: `EngineProcessNode` (+ `CommitRefNode`/`ProviderBootNode`/`EngineProcessEdge`) and the derived `Analytics.engineProcesses` in `projection.py` (version 1→2), the pure `build_engine_processes` + pre-contract `_start_process_node` in `reducer.py`, and `read_engine_process_facts` + `read_start_progress_entries` (§5.4) in `snapshots.py`, threaded through `project_workspace`/`build_analytics`/`project_and_write`. Verification metadata pinned until closeout stamps the 5e code commit.
- 2026-06-14T23:30+02:00: Slice 05 (5c) — completed the read side for the cockpit: `reducer.project_workspace` synthesizes paused persistent lifecycles from worktree enclosures (note 01); `snapshots.read_providers` reads per-worktree provider stacks (surface 4) bound to worktree/repo/role; `projection`/`snapshots` carry the full task content (`TaskDocNode` + step/decision/code-example nodes) and `ProviderNode` binding fields. Verification metadata pinned until closeout stamps the 5c code commit.
- 2026-06-14T17:28+02:00: Slice 05 (5b) — added the attention-queue surface to this route: `AttentionItem` + the derived `Analytics.attentionQueue` in `projection.py`, and the pure `build_attention_queue` (+ per-source helpers) in `reducer.py`, wired through `project_workspace` with no call-edge change. Verification metadata pinned until closeout stamps the 5b code commit.
- 2026-06-13T22:34: Slice 3c commit 2 — added the task-document read side: `read_task_documents` (surface 7) in `snapshots.py`, the `TaskDocNode` schema node + `Analytics.taskDocuments`, and the reducer/store wiring (`build_analytics`/`project_workspace`/`project_and_write` gained an optional `task_documents` input). Later Task 17 made the reader active-doc-first with optional lifecycle attachment. Verification metadata pinned until closeout stamps the 3c commit-2 code commit.
- 2026-06-13T20:48+02:00: Slice 3b — added the analytical surface readers to
  `snapshots.py` (drift snapshot, sidecar staleness, setup summaries/progress,
  route coverage, tool reports, ledger), the derived-aggregate rollups
  (`token_series`, `staleness_histogram`, `build_analytics`) + the `Analytics`
  schema block, and the drift-snapshot producer write in `memory_quality`
  (`summary._write_drift_snapshot`) sharing the `paths` drift contract. The route
  now owns the full read side. Verification metadata is pinned until closeout
  stamps the 3b code commit.
- 2026-06-13T19:30+02:00: Slice 3a — added the projection **read side** to this
  route (`reducer.py`, `projection.py`, `snapshots.py`, `projection_store.py`,
  `paths.py`) plus the shared `timeutil.py` leaf (timing thresholds +
  `age_seconds` moved out of `ambient`). The route now owns interpretation, not
  just the write side; structural surfaces (providers/contracts) land in 3a,
  analytical surfaces + rollups in 3b. Verification metadata is pinned until
  closeout stamps the 3a code commit.
- 2026-06-13T18:45+02:00: Slice 2c — added `save_gate.py` (the pure save-gate
  vocabulary) to the Route Model and extended `ambient.py` with `promote`/`attach`
  and the save gate; `lifecycle_state.py` gained the persistence-binding fields.
  Resume + save gate close the write-side seams (the reducer read side still lands
  later). Verification metadata is pinned until closeout stamps the 2c code commit.
- 2026-06-13T16:41+02:00: Slice 2b — added the ambient lifecycle to this route
  (`ambient.py`, `lifecycle_state.py`): the signal state machine, choke-point
  emission, heartbeat ticker, and TTL project-and-prune sweep. Verification
  metadata is pinned until closeout stamps the 2b code commit.
- 2026-06-13T11:15+02:00: Created for slice 2a — the observable-lifecycle event
  substrate write side (`events.py`, `ulid.py`, `store.py`). Verification
  metadata is pinned until closeout stamps the 2a code commit.
