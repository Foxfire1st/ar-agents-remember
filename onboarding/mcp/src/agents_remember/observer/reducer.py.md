# mcp/src/agents_remember/observer/reducer.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/observer/reducer.py`    |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-08T14:35+02:00 |
| lastVerifiedCommitHash | `45708bbddf1ddb8a2045faa9fad88fe72603b674`       |
| lastVerifiedCommitDate | 2026-07-08T05:51:44+02:00|
| governingOverview      | `overview.md`                                    |

## Purpose

`reducer.py` is the single owner of interpretation (design §2.5): it folds event
logs (and structural snapshots) into resolved projections, so no frontend ever
reimplements lifecycle assembly (slice 3a). Since L11 the reader also owns abandon
terminality: a lifecycle anchored to a `cleanup: abandoned` enclosure projects
`abandoned` (the store's single-writer invariant forbids a foreign `lifecycle.ended`
append), and abandoned/reopened enclosures synthesize no paused persistent lifecycle
— no worktree, nothing to pause. It also *composes* derived surfaces
the runtime never stores — the analytical rollups, the attention queue, and (slice
5e) the enclosure-centered Engine Room process map — from already-read inputs, so
the served projection and a sim replay stay byte-identical.

## Code Commentary

`project_lifecycle(events, *, now)` is the pure fold — its only inputs are the
log and `now`, so "same log ⇒ same projection" holds. `events[0]` is the
self-contained `lifecycle.started` that `_seed_from_started` turns into the
initial `LifecycleProjection`; `_apply_kind` then folds each later event:
`phase-changed`→phase, `blocked`→blocked+ask, `awaiting-developer`→
awaiting-developer (task-28 turn end: the carried `summary` rides on the
projection's `ask` carrier, mirroring how the block ask rides on
`lifecycle.blocked`), `resumed`→running+ask cleared (one `resumed` arm carries
both the parked blocked path and the awaiting-developer turn end back to running),
`paused`→paused, `promoted`→fleeting=False+scope (+enclosure/repoId from the
envelope), `ended`→completed|abandoned, `tool.completed`→token sum;
`heartbeat`/unknown only advance liveness. `lastEventTs` is taken from
`events[-1].ts`.

The **inferred layer** `_project_inferred` reuses the write-side thresholds
rather than re-deriving them: a non-terminal `fleeting` lifecycle older than
`TTL_SECONDS` projects `abandoned` (mirrors `ambient._is_dormant_fleeting` — the
reducer *projects*, the sweep *prunes*); a `running` lifecycle older than
`STALE_AFTER_SECONDS` projects `paused` (mirrors `setup_progress._project_running`).
Both set `inferred=True`; a terminal state is never overridden.

Before persistent lifecycle synthesis, `project_workspace` reconciles event-backed
lifecycles against the current enclosure snapshot. Fleeting lifecycles are kept because
they do not have enclosures by default. Fresh, non-terminal, non-inferred non-fleeting
lifecycles without a materialized enclosure are kept as the promotion/gate window.
Otherwise, a non-fleeting lifecycle with an enclosure must still have that current
enclosure, and if the enclosure declares a different `lifecycleId`, the older
event-backed lifecycle is dropped from the live projection instead of rendering as a
stale standalone row. The raw append-only event log remains historical evidence; the
reducer is only removing it from the live view.

**Corrections** (design §2.1): `_index_corrections` maps a corrected event id →
replacement `state` from append-only `correction.recorded` events (v1 corrects
the `state` field, validated against the state enum); the override is applied at
the corrected event's position so later events still win.

**Action availability** is computed here, never by the UI: `_lifecycle_actions`
emits `resume` (enabled only when `blocked`); `enclosure_actions` emits
`integrate` (enabled when `closeoutStatus=="completed"` and
`integrationStatus=="not-started"`) and `cleanup` (enabled when
`integrationStatus=="completed"` and `cleanup=="pending"`), each with
`disabledReason`/`nextSafeAction`. `project_workspace` folds every log, enriches
enclosures with their actions, and rolls up `Metrics`.

**Slice-3b rollups** keep the fold pure: `token_series(events)` builds a
lifecycle's cumulative-token fuel gauge from its `tool.completed` events (set on
the projection in `project_lifecycle`). **Served bounded since 260703-L15:** past
`TOKEN_SERIES_MAX` (512) points, `_decimate_token_series` uniform-thins the older
history (first sample always kept, `cumulative` stays exact per retained sample —
still a monotonic gauge) while the newest `TOKEN_SERIES_RECENT` (256) samples stay
complete; the observer LOG keeps every event — only the served projection is
bounded (an uncapped series rode ~60 B/sample on EVERY lifecycle delta while its
agent worked: 10k tool calls ≈ 600 KB/delta). `staleness_histogram` buckets sidecar
verification ages (fed into `Metrics.stalenessHistogram`); and `build_analytics`
assembles the `Analytics` block, collapsing the full sidecar list to a bounded
stalest-first leaderboard (`_stalest`). `project_workspace` gained
keyword-optional analytical inputs (drift snapshots, sidecar staleness, setup
summaries/progress, route coverage, tool reports, agent pickups, ledgers, and — slice 3c — task
documents) — omit them and `analytics` is empty, so the 3a structural-only contract
still holds. **Task 33** adds the keyword-optional `active_worktree_groups: list[str] | None`; the
return sets `activeWorktreeGroups=sorted(active_worktree_groups or [])` on the projection — the bounded
active worktree-group set the Topology filters on. The caller (`projection_store.project_and_write`)
passes the `active_enclosure_worktree_groups` set it already computes for the Engine Room, so the two
views share one active definition; omit it and the field is an empty list (structural-only contract
unaffected).

**Slice-05 attention queue:** `build_attention_queue(lifecycles, providers,
drift_snapshots, setup_progress, start_progress)` is a pure, deterministic ranking of what needs the
human (the home-screen queue). It delegates to one small builder per source —
`_lifecycle_attention` (task-28 `awaiting-developer` info item / `blocked-gate` /
stale-session / dormant-fleeting),
`_gate_attention` (slice 6c: an open durable gate → a `gate-open` item),
`_provider_attention`, `_drift_attention`, `_setup_attention`, and — slice 5f S6 (§9) —
`_start_attention` — concatenates, and sorts
by `(severity, -waitSeconds, id)` for a total order so replay stays byte-identical. Every
`waitSeconds` is an age already computed upstream (`staleSeconds` / `snapshotStaleSeconds`
/ `heartbeatAgeSeconds`), never render time. `project_workspace` threads its inputs
(now including `engine_start_progress`) into
`build_analytics(attention_queue=…)` → the derived `Analytics.attentionQueue`.
Enclosure-derived items (pending review / worktree debt) are deferred to the hangar (5c).
`_start_attention` raises a steady `warn` **blocked-start** item for a `worktree_start` gated
before its contract was written — the same master-caution the agent raises in chat (a human-choice
gate, not a fault); a happy-path beat (no `blockedReason`) is observability, not an alarm.
Task 23/24 adds `gateId` to `_gate_attention` items so dashboard Clear/Dismiss posts can target the
actual gate record. Task 28 S5.2 adds lifecycle-scoped attention acknowledgements: `project_workspace`
accepts `attention_dismissals`, and `build_attention_queue(..., dismissals=...)` drops a row only when
the stored `AttentionDismissalRecord` matches both item id and lifecycle id and its `dismissedAt` is at
or after the row's `signalTs`; a newer `signalTs` re-surfaces the lifecycle item. Task 29 extends the
same freshness comparison to whitelisted repo-level rows: actionable drift ids include
`repository:branch`, details include memory/report/checked provenance from the drift snapshot, and
`signalTs` is the snapshot `checkedAt`. Targetless dismissal never applies to provider/setup/start rows.
`build_analytics`
also passes `agentPickups` through unchanged; pickup age/state is computed by
`snapshots.read_agent_pickups`, not inferred in the reducer or frontend. Since 260707-HFX2-L1 (R5),
`project_workspace`/`build_analytics` also accept an `expectation_rows` keyword (default `[]`),
passed through unchanged into `Analytics.expectationRows` — the durable deadline-row projection
computed entirely by `snapshots.read_expectation_rows`; the reducer performs no expectation-row
logic of its own.

**Task-28 turn-end branch + gate-open/blocked-gate dedup:** `_lifecycle_attention`
gains an `awaiting-developer` branch — one `info` `AttentionItem` ("Turn complete
— your move") whose `detail` is the carried turn-end summary via the new
`_await_summary(ask)` helper (the peer of `_ask_text`, reading `ask["summary"]`).
In the same pass its blocked branch is narrowed to the one-line
`elif lifecycle.state == "blocked" and lifecycle.gate is None:`. That
`and lifecycle.gate is None` is the **dedup** that fixes the gate-open/blocked-gate
double-emission: a durable open gate is already materialized onto `lifecycle.gate`
by `_attach_gates` and raised as a `gate-open` item by `_gate_attention`, so the
event-derived `blocked-gate` proto-gate item now fires only for a *bare* `block()`
with no `GateRecord`.
`stateEnteredAt` is the heartbeat-immune anchor for awaiting/blocked acknowledgement freshness, and
`AttentionItem.signalTs` carries the per-row trigger time for reducer-side acknowledgement comparison.

**Slice-05 (5c) persistent lifecycles:** `project_workspace` synthesizes a paused persistent
`LifecycleProjection` for every current worktree-backed enclosure with no event-backed lifecycle
(`_persistent_lifecycles` / `_persistent_from_enclosure`) — note 01's rule is now bounded by
current enclosure ownership. If an enclosure is deleted or re-owned by another `lifecycleId`, the
older non-fleeting event-backed lifecycle drops out of the live projection. Synthesized lifecycles
carry no events (`lastEventTs == ""`), which is how `_lifecycle_attention` tells a dormant
*persistent* worktree (the hangar's job, note 06) from a live session gone quiet — its
stale-session / dormant-fleeting branches now gate on `lastEventTs`.

### Logic

**Slice-5e Engine Room process map:** `build_engine_processes(facts, enclosures,
providers, setup_progress, start_progress)` is the pure, enclosure-centered composer
for the Engine Room map — one `EngineProcessNode` per worktree contract, **composed,
not read**. It joins three already-read inputs per worktree: the recorded contract +
status guidance (`EngineProcessFacts` = `contract`/`status`/`guidance`); the worktree's
isolated provider stack; and that group's `SetupProgressNode` boot sequence. The
provider/setup join is **on the worktree-group basename**: `EnclosureNode.worktreeGroup`
is a full path while `ProviderNode.worktreeGroup` / `SetupProgressNode.group` are the
basename, so the join key is `group_full.rsplit("/", 1)[-1]` (matching the existing
dashboard join). **Disposed enclosures are dropped (05l P1, Gap B):** the per-fact loop
filters `... for fact in facts if not _is_disposed(fact)` — the module-level
`_is_disposed(fact)` returns True when `fact.contract["cleanup"]` is `completed`/`abandoned`
(`worktree_cleanup`/`worktree_abandon` already removed the worktrees + reclaimed the provider
stack), so a torn-down enclosure leaves the active `engineProcesses` instead of rendering a
fully-active phantom — the frontend (05k) animates the removal. `cleanup-pending` is
intentionally **kept** (its de-materialise beat still needs a live node to animate).
Worktree providers are bucketed by group and sorted `(code, memory)`
via `_ROLE_ORDER`; the per-fact `_engine_process` resolves `codeSource`/`codeWorktree`
(and, in `external` mode, `memorySource`/`memoryWorktree`/`ledgerPath`) into
`CommitRefNode`s with a `factState` (`observed` on disk / `derived` recorded-but-absent /
`missing` unobservable), derives the process `phase` (`_GUIDANCE_PHASE` maps the
`lifecycle_guidance` phases — including the 05l-P1 `abandoned` → `abandoned` and the 05m
`carryover-pending` → `carryover-pending`, each surfacing a new guidance phase to the
process-map vocabulary; `_process_phase` overlays `sync-needed`/`provider-setup`),
`health` (`_process_health`), and the `edges` conduit graph (`_process_edges`:
worktree-add → cgc-seed, the `external` ledger-map → grepai-clone pair, and a
`behind_official` sync feedback edge), plus `missingFacts`/`sourceFiles` for trust
honesty. `_engine_process` maps `contract["leaf_id"]` onto `EngineProcessNode.leafId`
while keeping `task_name` as the parent series identity, so sibling leaf worktrees under
one series do not collapse into duplicate task labels downstream. The whole list is sorted
`(repoName, taskName, id)` so replay stays byte-identical. Slice 5h: `_engine_process` also maps the successful-landing arc onto the
node — `integrationStrategy` from the recorded contract (`ff-only`/`replay`, `None` until
set) and `landing` from the best-effort `status["landing"]` probe
(`worktrees/modules/landing.py`), both additive so prior fixtures are unchanged. Slice 05m:
`_engine_process` also maps `carryoverDoneAt = _str_or_none(status.get("carryoverDoneAt"))` onto the
node — the carryover milestone time from the status payload (read off the official ledger by
`guidance.carryover_done`, surfaced through `status_payload`); display-only and `None` until the
parked memory is carried home (5k renders the seam). The 5h coupler
popover then passes `fact.ledger_rows`/`ledger_row_count` straight onto `ledgerRows`/`ledgerRowCount`
— the memory.md window is loaded in the I/O layer (`snapshots._ledger_window`), so the reducer stays a
pure fold (no `load_ledger`/git here).

Task 31 makes missing worktree provider runtime explicit. `_provider_boot_nodes`
first converts observed worktree-scoped `ProviderNode`s, then adds `factState="missing"`
placeholders for the expected `code` role and, in external-memory mode, the expected
`memory` role when no matching provider fact exists. The exception is an active
`running`/`blocked` setup with no provider nodes yet, where the setup-progress state
continues to own the visual. Missing placeholders do not count as completed seed/clone
engines, and `_missing_facts` reports exactly which provider roles were not observed.

**Pre-contract start synthesis (§5.4):** `_start_process_node(entry)` synthesizes a node
for a `worktree_start` that is blocked or in flight **before its contract was ever
written** — the one start state the contract-keyed surface cannot see. It reads the start
progress dict (`phase` via `_START_PHASE`, `completedPhases`, `blockedReason`, `choices`,
`memoryMode`), marks the code worktree `observed`/`planned` from whether `code-worktree`
completed, emits the same edge skeleton (planned/blocked states), and flags
`missingFacts` ("start gated at … — contract not yet written"). `build_engine_processes`
de-dupes by group basename: once a contract anchors an enclosure, the matching
start-progress entry is dropped so the same worktree never double-renders.

**Threading through `project_workspace` + `build_analytics`:** `project_workspace` gained
two keyword-optional inputs, `engine_process_facts` and `engine_start_progress`, calls
`build_engine_processes(...)`, and threads the result into `build_analytics(engine_processes=…)`
→ the derived `Analytics.engineProcesses`. Both default empty, so the 3a structural-only
and 3b analytical-only contracts still hold. The two inputs are read at the call edge by
`snapshots.read_engine_process_facts` / `read_start_progress_entries` (the latter over
`worktrees.start_progress`) and wired in `projection_store`.

**Series threading (R1 + Task 21 token rollup):** `project_workspace` and `build_analytics` accept the
keyword-optional `series` input read at the call edge by `snapshots.read_series_documents`. Before
analytics assembly, `project_workspace` calls `attach_series_token_totals(series or [], task_docs,
lifecycles)`, which joins each master row's `file` to projected sibling leaf docs and sums their bound
lifecycle `tokens` into `SeriesNode.seriesTokenTotal`. The helper returns copied nodes, so the reducer
still composes derived analytics from already-read inputs and performs no file I/O. Defaults empty, so
prior structural/analytical callers remain unchanged.

## Invariants And Boundaries

- **Pure fold:** `project_lifecycle`/`project_workspace` take already-read inputs;
  all file I/O lives at the call edge (`projection_store`/`snapshots`).
- **Trust honesty:** derived states are flagged `inferred`; the reducer never
  presents a projected state as a written transition.
- **Thresholds are imported, not redefined** (from `timeutil`), so write and read
  agree by construction.
- **Persistent lifecycle live rows are enclosure-owned:** fleeting lifecycles do
  not need enclosures, and fresh non-terminal promotion/gate lifecycles may
  bridge the materialization window; otherwise a non-fleeting lifecycle must
  still match a current enclosure to remain in `WorkspaceProjection.lifecycles`.
- Action availability is precomputed server-side (load-bearing for slice 06). Slice
  6c materializes the durable gate too: `_attach_gates` reads each lifecycle's latest
  *open* `GateRecord` (via `snapshots.read_gates`) onto `LifecycleProjection.gate`, and
  `_gate_attention` raises a `gate-open` queue item — additive, not a rewrite.
  L4 passes the gate record's `evidenceRefs` through onto the `GateNode`; the
  reducer still interprets no evidence contents and remains a pure fold.
- Attention dismissal is source-scoped: lifecycle rows must match lifecycle id, and the only targetless
  repo-level queue kind admitted by `_is_dismissed` is actionable drift.
- **Composed, not read (slice 5e):** the Engine Room map is joined here from
  already-read facts/providers/setup, never stored by the runtime; it is deterministic
  (sorted `(repoName, taskName, id)`) so served == sim replay.
- **Group-basename join:** the provider/setup join key is the worktree-group *basename*
  (`group_full.rsplit("/", 1)[-1]`), because enclosure groups are full paths while
  provider/setup groups are basenames — keep both sides on the basename.
- **One row per worktree:** a contract-keyed node always wins; a pre-contract
  start-progress entry is rendered only until its contract exists, then de-duped by group.
- **Series token rollup stays in the fold:** master token totals are derived from the current
  `task_documents` + folded lifecycle token totals; the reducer never persists the aggregate back to
  task JSON.
- **Attention acknowledgements are lifecycle-scoped:** reducer filtering requires the dismissal record's
  lifecycle id to match the attention item lifecycle id. Provider/setup/start alarms cannot be hidden by
  orphaned dismissal rows.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The projection schema this produces. | [projection.py](agents-remember/mcp/src/agents_remember/observer/projection.py) |
| The series-token helper that enriches `SeriesNode.seriesTokenTotal` before analytics assembly. | [series_tokens.py](agents-remember/mcp/src/agents_remember/observer/series_tokens.py) |
| The event envelope + kinds it folds. | [events.py](agents-remember/mcp/src/agents_remember/observer/events.py) |
| The write-side dormancy sweep the abandoned-projection mirrors. | [ambient.py](agents-remember/mcp/src/agents_remember/observer/ambient.py) |
| The shared stale/TTL thresholds + age helper. | [timeutil.py](agents-remember/mcp/src/agents_remember/observer/timeutil.py) |
| The provider stale-projection idiom the paused-projection mirrors. | [providers/setup_progress.py](agents-remember/mcp/src/agents_remember/providers/setup_progress.py) |
| The `EngineProcessNode`/`EngineProcessFacts`/`EngineProcessEdge`/`CommitRefNode`/`ProviderBootNode` schema the 5e map composes. | [projection.py](agents-remember/mcp/src/agents_remember/observer/projection.py) |
| Reads the engine-process facts + pre-contract start-progress entries at the call edge. | [snapshots.py](agents-remember/mcp/src/agents_remember/observer/snapshots.py) |
| The pre-contract `worktree_start` progress source (§5.4) the synthesized node reads. | [worktrees/start_progress.py](agents-remember/mcp/src/agents_remember/worktrees/start_progress.py) |
| The durable gate set `_attach_gates` materializes onto lifecycles (slice 6c). | [controlplane/store.py](agents-remember/mcp/src/agents_remember/controlplane/store.py) |
| Wires the engine facts + start-progress into `project_workspace`. | [projection_store.py](agents-remember/mcp/src/agents_remember/observer/projection_store.py) |
| Missing provider placeholders are created for expected code/memory roles when no matching worktree provider facts exist. | L980-L1079; L1240-L1265 | [reducer.py](reducer.py) |
| Actionable drift queue rows carry repo/branch ids, provenance detail, and `checkedAt` signal timestamps. | L770-L800 | [reducer.py](reducer.py) |
| `_is_dismissed` admits targetless suppression only for dismissible repo-level kinds. | L568-L590 | [reducer.py](reducer.py) |
| The design: the reducer, inferred trust, corrections (§2.1, §2.5). | [docs/design/observable-lifecycle.md](agents-remember/docs/design/observable-lifecycle.md) |

As of the 260703-L9 lifecycle convergence, the phase-inference comment speaks generic lifecycle vocabulary ("the lifecycle phase") rather than naming the retired session-job skill; the inference logic itself is unchanged.

## Update History

- 2026-07-08T14:35+02:00 — 260707-HFX2-L1: `build_analytics`/`project_workspace` gained an `expectation_rows` keyword threading `ExpectationRowNode`s into `Analytics.expectationRows` (R5 projection surfacing). Verification metadata pinned until closeout stamps the 260707-HFX2-L1 commit.
- 2026-07-07T05:12+02:00 — 260703-L15 S2 (bounded served buffers): `token_series` now decimates
  past `TOKEN_SERIES_MAX` (512) via `_decimate_token_series` — newest `TOKEN_SERIES_RECENT`
  (256) exact, older history uniform-thinned with the first sample kept; cumulative stays
  monotonic. Bounds the fuel gauge riding every lifecycle delta; the observer log stays
  complete. Verification metadata pinned until closeout stamps the L15 commit.

- 2026-07-05T01:32+02:00 - L9 lifecycle convergence: phase-inference comment re-worded (lifecycle phase, not l-01 phase); behavior unchanged. Verification metadata pinned until closeout stamps the L9 commit.
- 2026-07-04T12:32+02:00 — 260703-L4: `_gate_node` passes gate
  `evidenceRefs` into the served `GateNode`, exposing delegated-approval reviewer
  evidence refs without changing reducer ownership. Verification metadata pinned
  until closeout stamps the L4 commit.
- 2026-07-03T00:30+02:00 — L11 abandon terminality: `_terminalize_abandoned_anchor_lifecycles` projects `abandoned` onto event-backed lifecycles whose anchor enclosure was abandoned, and `_persistent_lifecycles` skips `cleanup in {abandoned, reopened}` enclosures.
- 2026-06-28T07:32+02:00 — Task 29 S7 follow-up: actionable-drift attention now uses
  `repository:branch` ids, provenance-rich detail, and drift `checkedAt` as the repo-level dismissal
  anchor; `_is_dismissed` keeps targetless suppression limited to whitelisted repo rows. Verification
  metadata pinned until closeout stamps the task-29 code commit.
- 2026-06-28T07:30+02:00 — Task 33: `project_workspace` gained the keyword-optional
  `active_worktree_groups: list[str] | None` and sets `activeWorktreeGroups=sorted(active_worktree_groups
  or [])` on the returned projection — the bounded active worktree-group set for the Topology, passed by
  `projection_store` from the `active_enclosure_worktree_groups` admission already computed for the
  Engine Room. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-28T03:52+02:00 — Task 28 S5.2 after source sync: `build_attention_queue`
  now honors compact `AttentionDismissalRecord` acknowledgements only when item id and lifecycle id
  match, with `stateEnteredAt` / `signalTs` preserving current-occurrence semantics. Verification
  metadata pinned until closeout stamps the task-28 code commit.
- 2026-06-27T23:08+02:00 — Task 31 provider-state honesty: documented missing provider placeholders for expected code/memory worktree roles, keeping Engine Room honest when provider runtime facts are absent. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-27T22:00+02:00 — Task 28 (NOTIFY-AND-CONTINUE turn end + gate dedup):
  `_apply_kind` gained a `lifecycle.awaiting-developer` arm (sets state
  `awaiting-developer` and rides the turn-end `summary` on the projection's `ask`
  carrier; the `lifecycle.resumed` arm clears `ask` back to `None`).
  `_lifecycle_attention` gained an `awaiting-developer` info `AttentionItem`
  ("Turn complete — your move", `detail` via the new `_await_summary` helper) and
  its blocked branch was narrowed to
  `elif lifecycle.state == "blocked" and lifecycle.gate is None:` — the one-line
  dedup that suppresses the duplicate `blocked-gate` when a durable open gate is
  already materialized by `_attach_gates` / emitted by `_gate_attention`. The
  fold stays pure. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-26T20:18+02:00 — Task 21 series token rollup: `project_workspace` now enriches incoming
  folder-keyed series nodes through `attach_series_token_totals` before passing them into analytics.
  Verification metadata pinned until closeout stamps the code commit.
- 2026-06-26T15:13+02:00 — Task 25 lifecycle live-row cleanup: `project_workspace` now drops
  stale non-fleeting event-backed lifecycles from the live projection when their enclosure is gone
  or re-owned by a different `lifecycleId`, while keeping fleeting lifecycles and the fresh
  non-terminal promotion/gate window. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-25T13:10+02:00 — Task 23/24: `project_workspace` / `build_analytics` now pass through `agent_pickups`, and `_gate_attention` includes `gateId` so dashboard queue actions can target gate records directly.
- 2026-06-24T08:09+02:00 — Engine Room leaf identity: `_engine_process` maps `contract.leaf_id` onto `EngineProcessNode.leafId` while keeping `taskName` as the parent series label, so parallel leaves under one task no longer render as duplicate parent tasks. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-21T06:40+02:00 — slice 05m (carryover-before-cleanup): `_GUIDANCE_PHASE` gained `"carryover-pending": "carryover-pending"`, surfacing guidance.py's new carryover phase (between integration and cleanup) to the process-map vocabulary; and `_engine_process` maps `carryoverDoneAt = _str_or_none(status.get("carryoverDoneAt"))` onto the node (the carryover milestone time read off the official ledger, surfaced through `status_payload`; display-only, `None` until carried — 5k renders the seam). Both additive; the fold stays pure. Verification metadata pinned until closeout stamps the 05m code commit.
- 2026-06-21T04:10+02:00 — slice 05l P1 (backend teardown visibility): `_GUIDANCE_PHASE` gained `"abandoned": "abandoned"` (surfaces guidance.py's new abandoned phase to the process-map vocabulary), and a new module-level `_is_disposed(fact)` (True when `contract["cleanup"]` is `completed`/`abandoned`) now filters `build_engine_processes` (`... for fact in facts if not _is_disposed(fact)`) so a disposed (cleaned-up/abandoned) enclosure drops from the active `engineProcesses` instead of rendering a phantom — the frontend (05k) animates the removal. `cleanup-pending` is intentionally kept (its de-materialise beat still needs a live node). Verification metadata pinned until closeout stamps the 05l-P1 code commit.
- 2026-06-19T03:17+02:00 — slice 3c reopened (R1): `project_workspace` + `build_analytics` gained a keyword-optional `series` (list of `SeriesNode`) threaded straight into `Analytics(series=…)` — pure pass-through, read at the call edge by `read_series_documents`. Defaults empty, so prior contracts are unchanged. Verification metadata pinned until closeout stamps the R1 code commit.
- 2026-06-18T18:00+02:00 — slice 5h ledger popover: `_engine_process` passes `fact.ledger_rows`/`ledger_row_count` through to `ledgerRows`/`ledgerRowCount` (the window is loaded in `snapshots._ledger_window`, so the reducer stays a pure fold). Verification metadata pinned until closeout stamps the code commit.
- 2026-06-18T14:05 — Task 6 slice 6c Part A: `project_workspace` / `build_attention_queue` gained a `gates` input; `_attach_gates` materializes each lifecycle's latest open `GateRecord` onto `LifecycleProjection.gate`, and `_gate_attention` raises a `gate-open` attention item. The fold stays pure (gates read at the call edge by `snapshots.read_gates`). Verification metadata pinned until closeout stamps the 6c Part A code commit.
- 2026-06-18T08:51+02:00 — slice 5h H1: `_engine_process` maps the additive `integrationStrategy` (from the contract) + `landing[]` (from the best-effort `status["landing"]` remote/PR probe) onto `EngineProcessNode`. Verification metadata pinned until closeout stamps the 5h code commit.
- 2026-06-16T03:25 — slice 5f S6 (§9): `build_attention_queue` gained a `start_progress` param + the `_start_attention` builder (a pre-contract **blocked-start** raises a steady `warn` master-caution — chat parity), and `project_workspace` now threads `engine_start_progress` into it; a happy-path beat (no `blockedReason`) is not an alarm. Verification metadata pinned until closeout stamps the S6 code commit.
- 2026-06-15T19:35 — slice 5e: slice 5e: build_engine_processes (pure enclosure-centered composer joining contract facts + providers + setup + lifecycle on the worktree-group basename) + pre-contract _start_process_node synthesis; threaded through project_workspace + build_analytics.
- 2026-06-14T23:30+02:00: Slice 05 (5c) — `project_workspace` synthesizes paused persistent lifecycles from worktree enclosures (`_persistent_lifecycles`/`_persistent_from_enclosure`, note 01: a worktree-backed lifecycle persists `paused` when idle, never reaped); the attention queue's stale-session/dormant branches gate on `lastEventTs` so synthesized dormant worktrees surface in the hangar, not the queue. Verification metadata pinned until closeout stamps the 5c code commit.
- 2026-06-14T16:58+02:00: Slice 05 (5b) — added `build_attention_queue` + per-source helpers (`_lifecycle_attention` / `_provider_attention` / `_drift_attention` / `_setup_attention`) and threaded the result through `project_workspace` → `build_analytics(attention_queue=…)` → the derived `Analytics.attentionQueue`; no call-edge change (`project_and_write` already passes every input). Verification metadata pinned until closeout stamps the 5b code commit.
- 2026-06-13T22:34: Slice 3c commit 2 — `build_analytics` and `project_workspace` gained a keyword-optional `task_documents` input wired into `Analytics.taskDocuments` (empty by default, so 3a/3b callers are unaffected). The fold stays pure. Verification metadata pinned until closeout stamps the 3c commit-2 code commit.
- 2026-06-13T20:48+02:00: Slice 3b — added the analytical rollups (`token_series`
  fuel gauge, `staleness_histogram`, `build_analytics`) and extended
  `project_workspace` with keyword-optional analytical inputs (empty by default, so
  3a callers are unaffected). The fold stays pure. Verification metadata is pinned
  until closeout stamps the 3b code commit.
- 2026-06-13T19:30+02:00: Created for slice 3a — the pure fold, the inferred layer
  (paused/abandoned), the corrections fold, action availability, and workspace
  assembly. Verification metadata is pinned until closeout stamps the 3a code commit.
