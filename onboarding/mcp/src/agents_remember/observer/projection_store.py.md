# mcp/src/agents_remember/observer/projection_store.py

| Field                  | Value                                                  |
| ---------------------- | ------------------------------------------------------ |
| repository             | agents-remember                                        |
| path                   | `mcp/src/agents_remember/observer/projection_store.py` |
| doc_type               | `file-level-onboarding`                                |
| lastUpdated            | 2026-07-09T19:31+02:00 |
| lastVerifiedCommitHash | `dbe750e4cd7fb777b8f39e7ba6279d1080502d8e`             |
| lastVerifiedCommitDate | 2026-07-09T19:42:39+02:00|
| governingOverview      | `overview.md`                                          |

## Purpose

`projection_store.py` is the reducer's I/O edge: it reads the per-lifecycle logs
plus the structural, analytical, and (slice 5e) engine surfaces, ties reading +
the pure reduction + the atomic write together, and writes the projection where
the dashboard reads it (slice 3a).

## Code Commentary

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

`project_and_write(config, *, now=None, provider_refresher=None)` is the entry the serving layer drives on
a tick (slice 04): it resolves the root via `paths.observer_root`, prunes expired
lifecycle event logs with `prune_expired_lifecycle_event_logs`, reads the lifecycle logs
+ structural snapshots (`read_enclosures`, optional provider refresh, `read_providers`), and — slice 3b — the
analytical surfaces too: the coordination-level readers (drift snapshots, setup
summaries/progress, tool reports, active task documents
(`read_task_documents`, with optional lifecycle attachment) — slice 3c) and — slice 5e — the engine
surfaces (`read_engine_process_facts(coordination_root, active_worktree_groups=...)` and
`read_start_progress_entries(coordination_root, now=...)`), plus, via
`_gather_repo_surfaces_cached`, the per-repo readers (sidecar staleness, route coverage,
ledger — now `read_ledger(scope.memory_root, code_root=scope.path)`, threading the scope's code root so
the official coupler's window carries the slice-5h Tier 2 per-side commit message/date) iterated over
`config.repositories` (each scope's `memory_root`/onboarding).
It then calls `reducer.project_workspace`, threading every surface through as a
keyword — including the slice-5e `engine_process_facts=` / `engine_start_progress=`
arguments, the R1 `series=read_series_documents(coordination_root, now=…)`
(the master series surface), and the slice-6c `gates=read_gates(coordination_root)`
argument. Task 23/24 adds `agent_pickups=read_agent_pickups(coordination_root, now=…)`, the pending
operator-inbox projection that drives task-row waiting-for-agent/check-chat feedback. Since
260707-HFX2-L1 (R5) it also threads `expectation_rows=read_expectation_rows(coordination_root,
now=moment)` — the durable deadline-row projection surfaced for dashboard/architect observability;
this is surfacing only, an L2 predicate reads `ExpectationRowStore` directly and never this
projection. Task 28 S5.2
constructs `AttentionDismissalStore(root)`, threads `attention_store.current()` into the reducer, then
calls `attention_store.prune_lifecycles(...)` with the projected non-terminal lifecycle ids before the
atomic write, so completed/abandoned lifecycle acknowledgement rows are physically removed as part of the
normal tick. It then writes atomically and returns the projection.
`McpRuntimeConfig` is imported under `TYPE_CHECKING` (config is only passed
through).

**Slice-6g / Task 17:** `enclosures` (from `read_enclosures`) is now hoisted to a local and passed both
into `project_workspace(enclosures=...)` and into
`read_task_documents(coordination_root, enclosures=...)`, so the reader can attach lifecycle context to
leaf/root task documents when structured enclosure bindings exist while still projecting unbound active
docs.

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

**Task 33:** `project_and_write` also passes `active_worktree_groups=sorted(engine_groups)` into
`project_workspace`, so the served `WorkspaceProjection.activeWorktreeGroups` reuses the exact
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

## Invariants And Boundaries

- **Atomic writes:** every projection file is written tmp + `os.replace`; readers
  never observe a torn file.
- **Root resolved once** through `paths.observer_root` (the shared path
  abstraction), never hard-coded here.
- This is the I/O edge; the fold (`reducer`) stays pure and the surface reads live
  in `snapshots`.
- **Surfaces flow through, never reshaped here:** each reader's output (including
  the slice-5e `read_engine_process_facts` / `read_start_progress_entries`) is passed
  straight into `project_workspace` as a keyword; this file adds no engine logic,
  only the read + thread.
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

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The shared store-root resolver. | [paths.py](agents-remember/mcp/src/agents_remember/observer/paths.py) |
| The append-only store whose logs are read back. | [store.py](agents-remember/mcp/src/agents_remember/observer/store.py) |
| The pure fold this drives. | [reducer.py](agents-remember/mcp/src/agents_remember/observer/reducer.py) |
| The surface readers it pulls — structural, analytical, and the slice-5e engine readers `read_engine_process_facts` / `read_start_progress_entries`. | [snapshots.py](agents-remember/mcp/src/agents_remember/observer/snapshots.py) |
| The projection-time drift snapshot pruner that removes valid snapshots for deleted worktrees before the analytical read. | [drift_snapshots.py](agents-remember/mcp/src/agents_remember/observer/drift_snapshots.py) |
| The pure fold that consumes the threaded `engine_process_facts` / `engine_start_progress` keywords (slice 5e). | [reducer.py](agents-remember/mcp/src/agents_remember/observer/reducer.py) |
| Compact lifecycle-scoped attention acknowledgement store pruned by `project_and_write`. | [controlplane/attention_dismissals.py](agents-remember/mcp/src/agents_remember/controlplane/attention_dismissals.py) |
| The atomic-write design requirement + serving placement (§2.5, §5). | [docs/design/observable-lifecycle.md](agents-remember/docs/design/observable-lifecycle.md) |
| `ProviderStateRefresher` implements the `ProviderStateRefresh` protocol, TTL-gates provider current-state refreshes, and logs probe failures before `project_and_write` reads provider snapshots. | L89-L137 | [projection_store.py](agents-remember/mcp/src/agents_remember/observer/projection_store.py) |
| Task 29 projection entry prunes expired lifecycle event logs, computes provider and engine admission groups, reads admitted provider/setup/engine surfaces, and keeps gates/pickups/task docs on the fast path. | L141-L188 | [projection_store.py](agents-remember/mcp/src/agents_remember/observer/projection_store.py) |
| The repo-surface cache memoizes sidecar staleness, route coverage, and ledger reads for a short TTL keyed by configured repo paths. | L192-L240 | [projection_store.py](agents-remember/mcp/src/agents_remember/observer/projection_store.py) |
| Admission policy is centralized in the worktree provider admission helper. | L18-L84 | [worktree_provider_admission.py](agents-remember/mcp/src/agents_remember/observer/worktree_provider_admission.py) |
| Projection tests prove cached repo surfaces do not cache provider reads. | L2283-L2324 | [test_observer_projection.py](agents-remember/mcp/tests/test_observer_projection.py) |

## Update History

- 2026-07-09T19:31+02:00 — 260707-HFX2-L12: documented the CS-6 scaling/reclamation change for this file. Verification metadata pinned until closeout stamps the HFX2-L12 commit.
- 2026-07-08T14:35+02:00 — 260707-HFX2-L1: `project_and_write` now also calls `read_expectation_rows` and threads it into `project_workspace` (R5 projection surfacing). Verification metadata pinned until closeout stamps the 260707-HFX2-L1 commit.
- 2026-06-30T00:00:00+02:00 — L5 (260628_operations-integration): `read_enclosures` hoisted above the retention prune
  so `prune_expired_lifecycle_event_logs` receives
  `protected_lifecycle_ids=series_retained_lifecycle_ids(enclosures, now=moment)`; a not-yet-retired
  master series' leaf logs are exempt from inactivity pruning. Fixes the regression where a live task's
  log was pruned and the worktree then vanished from the Engine Room. Verification metadata pinned until
  closeout stamps the L5 code commit.
- 2026-06-28T07:30+02:00 — Task 33: `project_and_write` now passes
  `active_worktree_groups=sorted(engine_groups)` into `project_workspace`, so the served
  `activeWorktreeGroups` (the Topology's active scope) reuses the same `active_enclosure_worktree_groups`
  set already computed for the Engine Room. Verification metadata pinned until closeout stamps the code
  commit.
- 2026-06-28T05:38+02:00 — Task 29: projection now prunes expired lifecycle event logs at the I/O
  edge, computes strict provider/setup admission and broader active-engine admission from enclosures +
  lifecycle logs, caches slow per-repo analytical surfaces, and leaves provider/gate/pickup/task inputs
  on the fast path. Live timing dropped a sampled projection tick from about 51.0s to about 1.1s after
  filtering historical engine-process status probes. Verification metadata pinned until closeout stamps
  the task-29 code commit.
- 2026-06-28T03:52+02:00 — Task 28 S5.2 after source sync: `project_and_write` now threads
  current attention acknowledgements into `project_workspace` and prunes acknowledgement rows for
  non-live lifecycles before writing the projection. Verification metadata pinned until closeout stamps
  the task-28 code commit.
- 2026-06-28T03:33+02:00 — Task 32 memory-mirror pruning: `project_and_write` now calls
  `prune_orphaned_drift_snapshots` before reading drift snapshots, so deleted-worktree entries are
  physically removed at the projection I/O edge. Verification metadata pinned until closeout stamps the
  task-32 code commit.
- 2026-06-27T23:08+02:00 — Task 31 provider-state honesty: documented the projector-edge `ProviderStateRefresher`, including why provider/Docker probe failures are contained to stale provider facts instead of killing the dashboard projection. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-25T13:20+02:00 — Task 23/24: threaded `read_agent_pickups` into `project_workspace` so pending inbox responses become task-row pickup feedback.
- 2026-06-24T16:39+02:00 — Task 17 projection-store route correction: `project_and_write` still only
  threads reader outputs, but the task-document reader it calls is now active-doc-first with optional
  runtime lifecycle attachment. Verification metadata pinned until closeout
  stamps the code commit.
- 2026-06-21T02:44+02:00 — Slice 6g: `project_and_write` hoists `enclosures` to a local and passes it into both `project_workspace` and `read_task_documents(..., enclosures=...)`, so masters contract-pair and cross-master links resolve. Verification metadata pinned until closeout stamps the 6g code commit.
- 2026-06-19T03:17+02:00 — slice 3c reopened (R1): `project_and_write` now also reads `read_series_documents(coordination_root, now=…)` and threads it into `project_workspace` as `series=` → `Analytics.series`. Pure read + thread (no engine logic here). Verification metadata pinned until closeout stamps the R1 code commit.
- 2026-06-18T21:25+02:00 — slice 5h Tier 2: `_gather_repo_surfaces` now passes the scope's code root to `read_ledger` (`code_root=scope.path`) so the official-coupler ledger window carries the per-side commit message/date. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-18T14:05+02:00 — Task 6 slice 6c Part A: `project_and_write` now also reads `read_gates(coordination_root)` and threads `gates=` into `project_workspace`. Verification metadata pinned until closeout stamps the 6c Part A code commit.
- 2026-06-15T19:35 — slice 5e: slice 5e: project_and_write now reads engine_process_facts + engine_start_progress and threads them into project_workspace.
- 2026-06-13T22:34: Slice 3c commit 2 — `project_and_write` first started reading task documents (`read_task_documents`) and passing them to `project_workspace`; later Task 17 made that reader active-doc-first with optional lifecycle context. Verification metadata pinned until closeout stamps the 3c commit-2 code commit.
- 2026-06-13T20:48+02:00: Slice 3b — `project_and_write` now also reads the
  analytical surfaces (coordination-level drift/setup/tool-reports + per-repo
  sidecar staleness/route coverage/ledger via `_gather_repo_surfaces`) and passes
  them to `project_workspace`. Verification metadata is pinned until closeout
  stamps the 3b code commit.
- 2026-06-13T19:30+02:00: Created for slice 3a — log reading, the atomic projection
  writer, and the `project_and_write` orchestrator. Verification metadata is pinned
  until closeout stamps the 3a code commit.
