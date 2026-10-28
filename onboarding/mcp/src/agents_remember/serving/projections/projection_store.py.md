# mcp/src/agents_remember/serving/projections/projection_store.py

## Governing Overview

[serving projections overview](overview.md)

## Purpose

`projection_store.py` is the reducer’s I/O edge: domain-invalidated canonical task/host, structural and analytical sources flow through pure workspace assembly and individual atomic projection-file replacement.

## Code Commentary

Semantically unchanged stable projections retain existing files. Worker-owned input state supplies canonical task sources, boot-reconciled host facts and the five native attention fact collections; subscriber publication ordering remains with Projector, not a lifecycle-log cache.


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

The projection tick has no provider-state refresher, provider/setup reader or provider snapshot
input. `ProjectionTickState` retains the input snapshot and optional landing-state reader; its
`stable` field carries the stable form computed for this tick's write/publication decision.

`project_and_write` receives the retained tick state, with a cold default. It resolves observer_root and reads input state through ProjectionReaders(repo_surfaces, landing_state) plus RefreshPass. WorkspaceStructure passes enclosures and active_worktree_groups; AnalyticalInputs passes drift, route coverage, tool reports, ledgers, canonical task_sources/host_activity, closeout queues, engine facts/start progress and source-reconciled acknowledgements to the sole reducer join. No provider input, lifecycle/series/pickup/expectation/gate fold or post-reducer dismissal prune remains.
The retained repo reader gathers route coverage and ledger using each scope's memory root and code root; no verification-age reader is restored. The input snapshot and landing reader remain separate retained collaborators on the tick object, with a cold-read default when no retained state is supplied. Landing observations retain their own owner.

Warning measures summary previews only; full bodies stay on demand. Semantic changes replace each projection file individually; pair-atomic publication/all-slot rollback are not promised. Projector owns tuple-before-notify.

Input state retains canonical full/directed sources and enclosures; task-entry production binds worktrees without lifecycle attachment.

Drift orphans require complete native branch/contract/snapshot proof. Configuration and checkout presence alone do not prove a live branch; incomplete proof retains acknowledgements/diagnostics.

**Task 29** originally split provider-runtime admission before surface reads. Those provider and
setup readers and their separate `admitted_worktree_groups` helper are now removed. The retained
`active_enclosure_worktree_groups(...)` admission feeds engine-process facts, avoiding git/status
probes for historical enclosure contracts while preserving non-terminal close/integration work in
the Engine Room. The per-repo analytical read remains behind `_gather_repo_surfaces_cached`, with a
TTL so route coverage and ledgers do not re-walk every memory tree on every projection tick.

**Task 33:** `project_and_write` also passes `active_worktree_groups=inputs.active_worktree_groups`
inside `WorkspaceStructure`, so the served `WorkspaceProjection.activeWorktreeGroups` reuses the exact
`active_enclosure_worktree_groups` set already computed for the Engine Room. The Topology constellation
and the Engine Room therefore share one definition of "active", and the task-bound and unbound worktrees preserve operational evidence for the other views.

Lifecycle event dormancy/series-retention exemptions are removed, not relocated onto the surviving River. Contract-derived admission remains independent of session logs and does not author task stage.

### 260712-TRH-L7 status-source split

The recurring projection path uses projected status plus the latest landing snapshot, while explicit interactive status retains fresh landing probing. This preserves operator freshness without making remote latency part of the one-second projection tick.


**L184 — NEW-LIMIT-FROM-REPORT-ONLY.** This is the one writer of the projection files, so the JSON encoding is decided here. The obligation this leaf records for this place is stated in the invariant named here; the card's earlier account of this file stands, and this paragraph adds what the change made true.

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
- **Retired provider inputs are absent:** the tick performs no provider status refresh and the
  reducer receives no provider/setup snapshots. Enclosure/process, drift, task/host, ledger and
  acknowledgement facts retain their own readers.
- **Drift snapshot retention is enforced at the I/O edge:** projection pruning happens
  before `read_drift_snapshots`, so the reducer receives a current snapshot list rather
  than an ever-growing set that clients merely filter.
- **Acknowledgement cleanup:** native per-kind complete source observations, not reduced lifecycle/task status, decide recovery/removal/fingerprint change. Partial failure is not health.
- **Host intake:** startup or HOST_ACTIVITY invalidation only; periodic heartbeat/full healing does not read the host.
- **Repo surfaces:** retain their cache/TTL rather than being reread on every event.
- **Slow retained surfaces:** `_gather_repo_surfaces_cached` keeps route coverage/ledger under the 120-second TTL. Declared invalidation, admission changes and pending task-refresh retry still control other acquisitions; closeout queues are retained input, not a restored gate/pickup domain.
- **Engine status probes are active-enclosure scoped:** `read_engine_process_facts` receives only
  non-terminal enclosure groups, preventing historical contracts from causing a long git/status tail.
- **Contracts refresh only when task inputs require it, and shared snapshots are read-only:**
  the worker-owned input state retains its contract snapshot on unaffected ticks. Full task refresh
  builds once; directed task refresh updates addressed contracts. The cold-read default uses the
  module contract cache. Consumers must not mutate shared `WorktreeContract` values.

## Evidence



- Projection assembly forwards only retained input fields and closeout queues. [13]



- The configured-root repository cache retains route coverage and ledger under its TTL. [14]


- Input read refreshes admitted domains and separately reads closeout queues on every input pass. [15]





- The repository cache stores route coverage and ledger; the projection edge forwards no sidecar age input and retains closeout queues. [16]




### Repo-Internal References

- The shared store-root resolver. [1]


- project_and_write drives the pure project_workspace assembler with retained structural and analytical inputs. The assembler enriches enclosure actions, builds native task entries from task sources and host activity, and returns their tasks/counts and unbound enclosures alongside retained attention/Engine Room analytics and metrics. Provider refresh and provider display inputs are absent. The pure enclosure-action helpers still gate integrate/cleanup by durable closeout/integration/cleanup facts; there is no project_lifecycle fold. [3]


- The worker-owned state refreshes task inputs. [4]
- The worker-owned state refreshes engine facts. [5]

- The worker-owned state refreshes progress inputs. [6]



- The input-state pass refreshes tasks, host activity, active enclosure engine facts, drift, start progress and workspace observations, then returns retained projection inputs; it performs no provider display-state refresh. [12]



| The pure fold consumes the threaded `engine_process_facts` / `engine_start_progress` inputs. | `project_workspace` | mcp/src/agents_remember/observer/reducer.py:128-181 |
| The atomic-write design requirement and serving placement are specified in §2.5 and §5. | `### 2.5 The observer and its projections`; `## 5. Placement and Packaging` | docs/design/observable-lifecycle.md:241-251; docs/design/observable-lifecycle.md:323-338 |

The current input-state refresh contract is recorded in reference [12]; no separate provider refresher runs before that read.
| `ProjectionInputState.read` owns the delegated domain refreshes and returns the complete input bundle. | "def read("; "return ProjectionInputs" | mcp/src/agents_remember/serving/projections/projection_inputs.py:214-264 |
| The repo-surface cache memoizes route coverage and ledger reads under the 120-second TTL keyed by configured repo paths; sidecar verification-age input is absent. | "_repo_surface_cache: dict[tuple[tuple[str"; "def _repo_surface_cache_key(config: McpRuntimeConfig) -> tuple[tuple[str"; "repo_surfaces=_gather_repo_surfaces_cached" | mcp/src/agents_remember/serving/projections/projection_store.py:87-87; mcp/src/agents_remember/serving/projections/projection_store.py:232-232; mcp/src/agents_remember/serving/projections/projection_store.py:349-349 |

- Active-enclosure admission includes only named worktree groups whose cleanup is not completed, abandoned or reopened; the removed provider admission helper is not the current owner. [17]



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
- The complete acquired input bundle is represented by `ProjectionInputs`.

Retired at the fifth freeze d59c3493: mcp/src/agents_remember/serving/projections/projection_inputs.py:161-298 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 7bf564a663bb61f12844dee39538dd09a1633cdb. Retired means the anchor no longer stands, not that the cited subject was deleted [8]
- `project_and_write` invokes the input state rather than owning those reads itself. [9]
- On task-structure or drift invalidation, ProjectionInputState._refresh_drift passes its retained contracts and an actionable-drift observation to pruning before reading analytical snapshots. Pruning deletes valid branch-orphaned snapshots only with complete native branch/contract/snapshot proof; failure of that proof retains snapshots. A deleted checkout/worktree alone does not prove its branch is gone, and a valid changed occurrence remains visible even when a sibling read is incomplete. [10]


- The shared contract snapshot is retained across unaffected ticks, built for full task refresh and updated for directed task refresh.  Anchor: "_contract_snapshot_cache = ContractSnapshotCache()"; "def build(self"; "contract_cache=_contract_snapshot_cache"; "self._contract_cache.build(" [11]


## 260928-MIK-L177 One Stable Dump Per Tick

A tick already computed the projection's stable form to decide whether to write. That value is now
carried on `ProjectionTickState.stable` and published afterwards, so the write decision and the
publication compare the same dump instead of computing it twice. The field is live only for the tick
that set it and is not part of the state a tick starts from; a tick that did not compute one leaves it
`None`, and publication then computes the form as before.

## Retirements

- Retired at the fifth freeze d59c3493: mcp/src/agents_remember/serving/projections/projection_inputs.py:161-298 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 7bf564a663bb61f12844dee39538dd09a1633cdb. Retired means the anchor no longer stands, not that the cited subject was deleted.