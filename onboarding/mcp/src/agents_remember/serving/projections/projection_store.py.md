# mcp/src/agents_remember/serving/projections/projection_store.py

## Governing Overview

[serving projections overview](overview.md)

## Purpose

`projection_store.py` is the reducer’s I/O edge: domain-invalidated canonical task/host, structural and analytical sources flow through pure workspace assembly and individual atomic projection-file replacement.

## Code Commentary

Semantically unchanged stable projections retain existing files. Worker-owned input state supplies canonical task sources and boot-reconciled host facts; subscriber publication ordering remains with Projector, not a lifecycle-log cache.


### 260712-PTS-L2 One Contract Pass Per Tick — historical acquisition account; superseded by worker-owned domain refresh below

A module-level `_contract_snapshot_cache = ContractSnapshotCache()` is retained for cold acquisition, following the module-cache discipline: it is mutated only on the
projection worker thread (ticks are serialized by the projector's awaited `asyncio.to_thread`), so no
locking is needed. `project_and_write` calls `_contract_snapshot_cache.build(coordination_root /
"tasks")` when task acquisition requires it — one shared leaf-enclosure-contract snapshot for those consumers — and hands the resulting immutable `ContractSnapshot` to all three consumers:
`read_enclosures(coordination_root, contracts=contract_snapshot)`,
`prune_orphaned_drift_snapshots(config, contracts=contract_snapshot)`, and
`read_engine_process_facts(..., contracts=contract_snapshot)`. Each of those previously ran its own
walk + `load_contract` pass (3x per tick; a py-spy 15s sample on 2026-07-12 showed them at
2.78s/3.68s/3.40s total). The cross-tick cache reuses a parsed contract while its
`(mtime_ns, size, ctime_ns)` stat identity is unchanged and prunes to the live enumeration each
build. The landing refresher and supervisor sweep are deliberately not consumers (event-loop thread
would need locks; `serving/` territory) and keep their own passes.

### Task and host sources

Session-log enumeration, parsed lifecycle caches and heartbeat-sidecar merging are removed. Retained task sources and the default-unknown host snapshot enter the one TaskEntry join; no periodic host census is implied by ordinary heartbeat/full healing.

`write_projection(root, projection)` writes `latest-state.json` (the whole
`WorkspaceProjection`) and `latest-metrics.json` (just `metrics`). Both go through
`_write_json` and the kernel `atomic_write_text`: write a sibling temporary file,
flush/fsync it and use `os.replace` — atomic on POSIX, so a polling dashboard
reader never sees a half-written file. This is deliberately stronger than the plain `write_text` of
the `setup_progress` precedent, which a concurrent reader can tear.

`ProviderStateRefresher` is the optional dashboard-owned refresh implementation for provider
current-state, and `ProviderStateRefresh` is the structural protocol the projection edge accepts.
The implementation holds a small TTL and calls `providers.status.refresh_current_provider_state`
with the same `now` the projection will use, so `logs/providers/status/.../current.json`
can be refreshed before `read_providers` computes stale age. Refresh failures are
logged and the previous snapshot is used: this containment is necessary because Docker
and provider watcher reads are external control-plane I/O, and a failed provider probe
must not stop the dashboard from projecting the rest of the workspace.

`project_and_write` receives ProjectionTickState(input_state, provider_refresher, landing_state), with a cold default. It resolves observer_root, optionally refreshes provider state, and reads input state through ProjectionReaders(repo_surfaces, landing_state) plus RefreshPass. WorkspaceStructure and AnalyticalInputs pass canonical task_sources/host_activity, worktrees/providers, analytics, engine facts, closeout and source-reconciled acknowledgements to the sole reducer join. No lifecycle/series/pickup/expectation/gate fold or post-reducer dismissal prune remains.

Warning measures summary previews only; full bodies stay on demand. Semantic changes replace each projection file individually; pair-atomic publication/all-slot rollback are not promised. Projector owns tuple-before-notify.

Input state retains canonical full/directed sources and enclosures; task-entry production binds worktrees without lifecycle attachment.

Drift orphans require complete native branch/contract/snapshot proof. Configuration and checkout presence alone do not prove a live branch; incomplete proof retains acknowledgements/diagnostics.

**Task 29:** `project_and_write` now splits worktree runtime admission before reading
runtime surfaces. `admitted_worktree_groups(enclosures)`
feeds `read_providers` and `read_setup_progress_nodes`, so contract-inactive provider-runtime files do not
produce provider nodes or provider-down attention. `active_enclosure_worktree_groups(...)`
feeds `read_engine_process_facts`, avoiding git/status probes for historical enclosure contracts
while preserving non-terminal close/integration work in the Engine Room. The same task also wraps
the per-repo analytical read behind `_gather_repo_surfaces_cached`, with a short TTL so sidecar
staleness, route coverage, and ledgers do not re-walk every memory tree on every projection tick.

**Task 33:** `project_and_write` also passes `active_worktree_groups=inputs.active_worktree_groups`
inside `WorkspaceStructure`, so the served `WorkspaceProjection.activeWorktreeGroups` reuses the exact
`active_enclosure_worktree_groups` set already computed for the Engine Room. The Topology constellation
and the Engine Room therefore share one definition of "active", and the task-bound and unbound worktrees preserve operational evidence for the other views.

Lifecycle event dormancy/series-retention exemptions are removed, not relocated onto the surviving River. Contract-derived admission remains independent of session logs and does not author task stage.

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
- **Acknowledgement cleanup:** native per-kind complete source observations, not reduced lifecycle/task status, decide recovery/removal/fingerprint change. Partial failure is not health.
- **Host intake:** startup or HOST_ACTIVITY invalidation only; periodic heartbeat/full healing does not read the host.
- **Repo surfaces:** retain their cache/TTL rather than being reread on every event.
- **Engine status probes are active-enclosure scoped:** `read_engine_process_facts` receives only
  non-terminal enclosure groups, preventing historical contracts from causing a long git/status tail.
- **Contracts refresh only when task inputs require it, and shared snapshots are read-only:**
  the worker-owned input state retains its contract snapshot on unaffected ticks. Full task refresh
  builds once; directed task refresh updates addressed contracts. The cold-read default uses the
  module contract cache. Consumers must not mutate shared `WorktreeContract` values.

## Evidence

### Repo-Internal References

- The shared store-root resolver. [1]
- project_and_write drives the pure project_workspace assembler, passing retained structural and analytical inputs. The assembler enriches enclosure actions, builds native task entries from task sources and host activity, returns their tasks/counts and unbound enclosures, and builds provider/attention/Engine Room analytics and metrics. The pure enclosure action helpers gate integrate/cleanup by durable closeout/integration/cleanup facts; there is no project_lifecycle fold. [3]
- The worker-owned state refreshes task inputs. [4]
- The worker-owned state refreshes engine facts. [5]
- The worker-owned state refreshes progress inputs. [6]
- The input state refresh pass owns its delegated task, provider, and drift refreshes before returning the projection inputs. [12]

| The pure fold consumes the threaded `engine_process_facts` / `engine_start_progress` inputs. | `project_workspace` | mcp/src/agents_remember/observer/reducer.py:128-181 |
| The atomic-write design requirement and serving placement are specified in §2.5 and §5. | `### 2.5 The observer and its projections`; `## 5. Placement and Packaging` | docs/design/observable-lifecycle.md:241-251; docs/design/observable-lifecycle.md:323-338 |
| The tick calls the TTL-gated provider refresher before `ProjectionInputState.read`, whose delegated `_refresh_providers` performs provider reads. | "tick.provider_refresher.maybe_refresh("; "inputs = state.read("; `_refresh_providers` | mcp/src/agents_remember/serving/projections/projection_inputs.py:319-338; mcp/src/agents_remember/serving/projections/projection_store.py:226-226; mcp/src/agents_remember/serving/projections/projection_store.py:228-228 |
| `ProjectionInputState.read` owns the delegated domain refreshes and returns the complete input bundle. | "def read("; "return ProjectionInputs" | mcp/src/agents_remember/serving/projections/projection_inputs.py:214-264 |
| The repo-surface cache memoizes sidecar staleness, route coverage, and ledger reads for a short TTL keyed by configured repo paths. | "_repo_surface_cache: dict[tuple[tuple[str"; "def _repo_surface_cache_key(config: McpRuntimeConfig) -> tuple[tuple[str"; "repo_surfaces=_gather_repo_surfaces_cached" | mcp/src/agents_remember/serving/projections/projection_store.py:87-87; mcp/src/agents_remember/serving/projections/projection_store.py:232-232; mcp/src/agents_remember/serving/projections/projection_store.py:349-349 |
| Admission policy is centralized in the worktree provider admission helper. | `admitted_worktree_groups` | mcp/src/agents_remember/observer/worktree_provider_admission.py:24-45 |


## 260718-CHATS-L5I Current Delta

The projection path shares a retained contract/enclosure snapshot across consumers and uses a bounded repository-surface cache. The worker-owned input state refreshes task contracts only for affected, pending or full task acquisition, preserving directed refresh rather than enumerating them on every tick.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## 260727-CHATS-IM-L2 Current Delta

`project_and_write` receives an optional worker-owned `ProjectionInputState` (now carried on
`ProjectionTickState`) plus exact `ProjectionRefresh` and consumes its complete `ProjectionInputs`.
The reducer and atomic-write boundary are unchanged; input acquisition and reclamation belong to
the state object. `state.read(...)` is called with a `ProjectionReaders(repo_surfaces=_gather_repo_surfaces_cached, landing_state=tick.landing_state)` and a
`RefreshPass(now=moment, refresh=refresh or ProjectionRefresh.full())`.

- Input acquisition and reclamation belong to the worker-owned state. [7]
- The complete acquired input bundle is represented by `ProjectionInputs`. [8]
- `project_and_write` invokes the input state rather than owning those reads itself. [9]
- On task-structure or drift invalidation, ProjectionInputState._refresh_drift passes its retained contracts and an actionable-drift observation to pruning before reading analytical snapshots. Pruning deletes valid branch-orphaned snapshots only with complete native branch/contract/snapshot proof; failure of that proof retains snapshots. A deleted checkout/worktree alone does not prove its branch is gone, and a valid changed occurrence remains visible even when a sibling read is incomplete. [10]

- The shared contract snapshot is retained across unaffected ticks, built for full task refresh and updated for directed task refresh.  Anchor: "_contract_snapshot_cache = ContractSnapshotCache()"; "def build(self"; "contract_cache=_contract_snapshot_cache"; "self._contract_cache.build(" [11]
