# mcp/src/agents_remember/serving/projections/projection_store.py

## Governing Overview

[serving projections overview](overview.md)

## Purpose

`projection_store.py` is the reducer's I/O edge: it reads the per-lifecycle logs
plus the structural, analytical, and (slice 5e) engine surfaces, ties reading +
the pure reduction + the atomic write together, and writes the projection where
the dashboard reads it (slice 3a).

## Code Commentary

### 260712-PTS-L2 One Contract Pass Per Tick

A module-level `_contract_snapshot_cache = ContractSnapshotCache()` now sits beside
`_lifecycle_log_cache`, following the same module-cache discipline: it is mutated only on the
projection worker thread (ticks are serialized by the projector's awaited `asyncio.to_thread`), so no
locking is needed. `project_and_write` calls `_contract_snapshot_cache.build(coordination_root /
"tasks")` at tick start — ONE leaf-enclosure-contract enumeration + at-most-one parse per contract
per tick — and hands the resulting immutable `ContractSnapshot` to all three consumers:
`read_enclosures(coordination_root, contracts=contract_snapshot)`,
`prune_orphaned_drift_snapshots(config, contracts=contract_snapshot)`, and
`read_engine_process_facts(..., contracts=contract_snapshot)`. Each of those previously ran its own
walk + `load_contract` pass (3x per tick; a py-spy 15s sample on 2026-07-12 showed them at
2.78s/3.68s/3.40s total). The cross-tick cache reuses a parsed contract while its
`(mtime_ns, size, ctime_ns)` stat identity is unchanged and prunes to the live enumeration each
build. The landing refresher and supervisor sweep are deliberately not consumers (event-loop thread
would need locks; `serving/` territory) and keep their own passes.

### 260707-HFX2-L13 Heartbeat-Sidecar Merge

The lifecycle-log cache now stores only parsed `events.jsonl` rows. A projection read reuses that
parse while independently reading and merging the latest `heartbeat.json` sidecar, so every heartbeat
tick remains visible to reducer staleness without changing the log fingerprint or forcing a full-log
reparse. The merge copies the cached list before appending the sidecar. Current timestamp ordering is
a raw string comparison; the round-1 reviewer accepted unifying it with `EventStore`'s parsed compare
as non-blocking N6.

### 260707-HFX2-L12 CS-6 Update

Projection now caches unchanged lifecycle logs by `(mtime_ns, size)`, rate-limits warnings for over-budget task-document body payloads, and passes the projection clock to engine-process facts so the git-status cache can bound per-tick subprocess fan-out.

`read_lifecycle_logs(root)` enumerates `lifecycles/<id>/events.jsonl` under the
store root (via `EventStore.read`), returning one validated `list[Event]` per
non-empty log.

`write_projection(root, projection)` writes `latest-state.json` (the whole
`WorkspaceProjection`) and `latest-metrics.json` (just `metrics`). Both go through
`_atomic_write_json`: write to a `<name>.<ulid>.tmp` sibling then `os.replace`
into place — atomic on POSIX, so a polling dashboard reader never sees a
half-written file. This is deliberately stronger than the plain `write_text` of
the `setup_progress` precedent, which a concurrent reader can tear.

`ProviderStateRefresher` is the optional dashboard-owned refresh implementation for provider
current-state, and `ProviderStateRefresh` is the structural protocol the projection edge accepts.
The implementation holds a small TTL and calls `providers.status.refresh_current_provider_state`
with the same `now` the projection will use, so `logs/providers/status/.../current.json`
can be refreshed before `read_providers` computes stale age. Refresh failures are
logged and the previous snapshot is used: this containment is necessary because Docker
and provider watcher reads are external control-plane I/O, and a failed provider probe
must not stop the dashboard from projecting the rest of the workspace.

`project_and_write(config, *, now=None, refresh=None, tick=None)` is the entry the serving layer
drives on a tick (slice 04). Since 260731-EFA-L2 the projector's three long-lived collaborators
travel together in the frozen `ProjectionTickState(input_state=None, provider_refresher=None,
landing_state=None)` passed as `tick=` — a tick given some of them and not others silently reverts
to a cold read, so they are one object. `tick or ProjectionTickState()` is the cold-read default.
It resolves the root via `paths.observer_root`, prunes expired
lifecycle event logs with `prune_expired_lifecycle_event_logs`, reads the lifecycle logs +
structural snapshots (`read_enclosures`, optional provider refresh, `read_providers`), and — slice 3b — the
analytical surfaces too: the coordination-level readers (drift snapshots, setup
summaries/progress, tool reports, active task documents
(`read_task_documents`, with optional lifecycle attachment) — slice 3c) and — slice 5e — the engine
surfaces (`read_engine_process_facts(coordination_root, active_worktree_groups=...)` and
`read_start_progress_entries(coordination_root, now=...)`), plus, via
`_gather_repo_surfaces_cached`, the per-repo readers (sidecar staleness, route coverage,
ledger — now `read_ledger(scope.memory_root, code_root=scope.path)`, threading the scope's code root so
the official coupler's window carries the slice-5h Tier 2 per-side commit message/date) iterated over
`config.repositories` (each scope's `memory_root`/onboarding).
It then calls `reducer.project_workspace`, threading every surface through **two bundles rather
than a keyword list** (260731-EFA-L2): `structure=WorkspaceStructure(enclosures=…, providers=…,
active_worktree_groups=…)` for the structural tree, and `given=AnalyticalInputs(…)` for every
analytical surface — drift snapshots, sidecar staleness, setup summaries/progress, route coverage,
tool reports, agent pickups, expectation rows, ledgers, task documents, series, the slice-5e
`engine_process_facts` / `engine_start_progress`, the slice-6c `gates`, and the attention
dismissals. `series` is the R1 master-series surface from `read_series_documents`; `agent_pickups`
(Task 23/24) is the pending operator-inbox projection that drives task-row
waiting-for-agent/check-chat feedback; `expectation_rows` (260707-HFX2-L1 R5) is the durable
deadline-row projection surfaced for dashboard/architect observability — surfacing only, since an
L2 predicate reads `ExpectationRowStore` directly and never this projection. Task 28 S5.2
constructs `AttentionDismissalStore(root)`, threads `attention_store.current()` into the reducer, then
calls `attention_store.prune_lifecycles(...)` with the projected non-terminal lifecycle ids before the
atomic write, so completed/abandoned lifecycle acknowledgement rows are physically removed as part of the
normal tick. It then writes atomically and returns the projection.
`McpRuntimeConfig` is imported under `TYPE_CHECKING` (config is only passed
through).

**Slice-6g / Task 17:** the enclosure list read by `ProjectionInputState` reaches both
`WorkspaceStructure(enclosures=…)` and `read_task_documents(coordination_root, enclosures=...)`, so
the reader can attach lifecycle context to leaf/root task documents when structured enclosure
bindings exist while still projecting unbound active docs.

**Task 32:** after `read_enclosures(coordination_root)` and before
`read_drift_snapshots(coordination_root, now=...)`, `project_and_write` calls
`prune_orphaned_drift_snapshots(config)`. That keeps the reducer's drift snapshot
input physically pruned: configured repo snapshots remain, current leaf
worktree snapshots remain while their code worktree still exists, and valid
worktree snapshots for deleted worktrees are removed before the projection is
written.

**Task 29:** `project_and_write` now splits worktree runtime admission before reading
runtime surfaces. `admitted_worktree_groups(enclosures, lifecycle_logs, now=...)`
feeds `read_providers` and `read_setup_progress_nodes`, so parked provider-runtime files do not
produce provider nodes or provider-down attention. `active_enclosure_worktree_groups(...)`
feeds `read_engine_process_facts`, avoiding git/status probes for historical enclosure contracts
while preserving non-terminal close/integration work in the Engine Room. The same task also wraps
the per-repo analytical read behind `_gather_repo_surfaces_cached`, with a short TTL so sidecar
staleness, route coverage, and ledgers do not re-walk every memory tree on every projection tick.

**Task 33:** `project_and_write` also passes `active_worktree_groups=inputs.active_worktree_groups`
inside `WorkspaceStructure`, so the served `WorkspaceProjection.activeWorktreeGroups` reuses the exact
`active_enclosure_worktree_groups` set already computed for the Engine Room. The Topology constellation
and the Engine Room therefore share one definition of "active", and the shared `enclosures`/`lifecycles`
collections still carry all-time history for the other views.

**L5 (260628_operations-integration):** retention is now **enclosure-aware**. `read_enclosures` is
hoisted *above* the prune call, and `prune_expired_lifecycle_event_logs` is invoked with
`protected_lifecycle_ids=series_retained_lifecycle_ids(enclosures, now=moment)`. The effect: every leaf
of a not-yet-retired master series is exempt from the inactivity TTL, so a running durable task (and its
sibling leaves) never lose their Event River history mid-task. This closed the regression where the
hour-long inactivity prune deleted a live task's log — and admission then keyed on the now-missing log,
making the worktree vanish from the Engine Room. The protection set is derived entirely from durable
enclosure state in `worktree_provider_admission`; this file only reorders the read and threads the set.

### 260712-TRH-L7 status-source split

The recurring projection path uses projected status plus the latest landing snapshot, while explicit interactive status retains fresh landing probing. This preserves operator freshness without making remote latency part of the one-second projection tick.

## Invariants And Boundaries

- **Atomic writes:** every projection file is written tmp + `os.replace`; readers
  never observe a torn file.
- **Root resolved once** through `paths.observer_root` (the shared path
  abstraction), never hard-coded here.
- This is the I/O edge; the fold (`reducer`) stays pure and the surface reads live
  in `snapshots`.
- **Surfaces flow through, never reshaped here:** each reader's output (including
  the slice-5e `read_engine_process_facts` / `read_start_progress_entries`) is packed
  straight into `WorkspaceStructure` / `AnalyticalInputs` and handed to `project_workspace`;
  this file adds no engine logic, only the read + thread. The bundles are transport, not
  transformation — assigning a field means the reducer receives that reader's output unchanged.
- **Provider refresh is an I/O-edge concern:** the optional refresher runs before
  `read_providers`, but the reducer still receives ordinary provider snapshots and
  remains deterministic for supplied inputs. Refresh probe failures degrade to the
  last persisted provider snapshot instead of failing the whole dashboard tick.
- **Drift snapshot retention is enforced at the I/O edge:** projection pruning happens
  before `read_drift_snapshots`, so the reducer receives a current snapshot list rather
  than an ever-growing set that clients merely filter.
- **Attention acknowledgement pruning is tick-bound:** `project_and_write` uses the reducer's projected
  lifecycle states as the live set and prunes `AttentionDismissalStore` rows outside that set.
- **Raw event retention is tick-bound and enclosure-aware:** dormant lifecycle event logs are pruned
  before the lifecycle log read, but `enclosures` is read first so a not-yet-retired master series'
  leaf ids are passed as `protected_lifecycle_ids` — a live durable task's history is never pruned by
  inactivity, and admission (which keys on the durable enclosure) keeps the worktree visible.
- **Slow repo surfaces are cached, not fast attention inputs:** `_gather_repo_surfaces_cached` caches
  per-repo onboarding/ledger walks, while lifecycle logs, gates, admitted providers/setup progress,
  pickups, task documents, and dismissals are still read every projection tick.
- **Engine status probes are active-enclosure scoped:** `read_engine_process_facts` receives only
  non-terminal enclosure groups, preventing historical contracts from causing a long git/status tail.
- **Contracts are read once per tick, and the shared snapshot is never mutated:** the module-level
  `_contract_snapshot_cache` is touched only inside the serialized projection tick, the published
  `ContractSnapshot` is immutable, and its `WorktreeContract` instances are shared across ticks —
  any future consumer that mutated one would corrupt cross-tick state.

## Evidence

### Repo-Internal References

- The shared store-root resolver. [1]
- The append-only store whose logs are read back. [2]
- The pure fold this drives. [3]
- The worker-owned state refreshes task inputs. [4]
- The worker-owned state refreshes engine facts. [5]
- The worker-owned state refreshes progress inputs. [6]
- Input acquisition and reclamation belong to the worker-owned state. [7]
- The complete acquired input bundle is represented by `ProjectionInputs`. [8]
- `project_and_write` invokes the input state rather than owning those reads itself. [9]
- `ProjectionInputState._refresh_drift` prunes stale drift snapshots for deleted worktrees before the analytical read. [10]
- The shared per-tick contract snapshot is built once for the projection pass. [11]
- The input state refresh pass owns its delegated task, provider, and drift refreshes before returning the projection inputs. [12]

| The pure fold consumes the threaded `engine_process_facts` / `engine_start_progress` inputs. | `project_workspace` | mcp/src/agents_remember/observer/reducer.py:128-181 |
| The compact lifecycle-scoped attention acknowledgement store is pruned by `project_and_write`. | `project_and_write` | mcp/src/agents_remember/serving/projections/projection_store.py:212-275 |
| The atomic-write design requirement and serving placement are specified in §2.5 and §5. | `### 2.5 The observer and its projections`; `## 5. Placement and Packaging` | docs/design/observable-lifecycle.md:241-251; docs/design/observable-lifecycle.md:323-338 |
| The tick calls the TTL-gated provider refresher before `ProjectionInputState.read`, whose delegated `_refresh_providers` performs provider reads. | "tick.provider_refresher.maybe_refresh("; "inputs = state.read("; `_refresh_providers` | mcp/src/agents_remember/serving/projections/projection_inputs.py:319-338; mcp/src/agents_remember/serving/projections/projection_store.py:226-226; mcp/src/agents_remember/serving/projections/projection_store.py:228-228 |
| `ProjectionInputState.read` owns the delegated domain refreshes and returns the complete input bundle. | "def read("; "return ProjectionInputs" | mcp/src/agents_remember/serving/projections/projection_inputs.py:214-264 |
| The repo-surface cache memoizes sidecar staleness, route coverage, and ledger reads for a short TTL keyed by configured repo paths. | "_repo_surface_cache: dict[tuple[tuple[str"; "def _repo_surface_cache_key(config: McpRuntimeConfig) -> tuple[tuple[str"; "repo_surfaces=_gather_repo_surfaces_cached" | mcp/src/agents_remember/serving/projections/projection_store.py:87-87; mcp/src/agents_remember/serving/projections/projection_store.py:232-232; mcp/src/agents_remember/serving/projections/projection_store.py:349-349 |
| Admission policy is centralized in the worktree provider admission helper. | `admitted_worktree_groups` | mcp/src/agents_remember/observer/worktree_provider_admission.py:24-45 |


## 260718-CHATS-L5I Current Delta

The projection path now shares one contract/enclosure parse pass per tick and uses a slower bounded repository-surface refresh cache. These changes remove repeated whole-workspace reads from the one-second projection cadence without freezing the projection's volatile fields.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## 260727-CHATS-IM-L2 Current Delta

`project_and_write` receives an optional worker-owned `ProjectionInputState` (now carried on
`ProjectionTickState`) plus exact `ProjectionRefresh` and consumes its complete `ProjectionInputs`.
The reducer and atomic-write boundary are unchanged; input acquisition and reclamation belong to
the state object. `state.read(...)` is called with a `ProjectionReaders(lifecycle=read_lifecycle_logs,
repo_surfaces=_gather_repo_surfaces_cached, landing_state=tick.landing_state)` and a
`RefreshPass(now=moment, refresh=refresh or ProjectionRefresh.full())`.
