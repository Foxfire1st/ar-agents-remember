# test_observer_projection.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_observer_projection.py`          |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-10T01:14+02:00                     |
| lastVerifiedCommitHash | `5b49fa85a51d527a5a216a88c361c08246c759d0`       |
| lastVerifiedCommitDate | 2026-07-10T05:00:02+02:00|
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[mcp overview](../overview.md) — there is no route-local `mcp/tests/overview.md`.

## Purpose

`test_observer_projection.py` covers the observer projection read side (slice 3a):
the pure fold and its determinism, the inferred layer, append-only corrections,
precomputed action availability, workspace tree assembly, the atomic projection
write, and the structural surface readers. L11 adds abandon-terminality coverage:
an abandoned-enclosure lifecycle projects `abandoned`, and abandoned/reopened
enclosures synthesize no paused persistent lifecycle.

## Code Commentary

### 260707-HFX2-L13 Summary Contract Assertions

Snapshot-reader assertions now expect task and series broadcast nodes to omit objective, sections,
and decisions while preserving structural summary fields. Full-body behavior is exercised in the
dedicated CS-6 projection suite through `read_task_document_body`.

### Logic

`FoldTests` assert the seed from `lifecycle.started`, the phase/block/resume walk,
ask retention, the task-28 `awaiting-developer` fold
(`test_awaiting_developer_then_resume`: `lifecycle.awaiting-developer` projects
state `awaiting-developer` with the `summary` on the `ask` carrier
(`ask == {"summary": …}`), and a following `lifecycle.resumed` clears it back to
`running` with `ask is None`), token aggregation, promotion to persistent, ended
outcomes, and the empty-log guard. `DeterminismTests` assert the same log + same `now` reduce to an
identical projection. `InferredLayerTests` assert fresh→running,
stale→`paused` (`inferred`), fleeting+dormant→`abandoned` (`inferred`), persistent
dormancy never auto-abandons, and a terminal state survives staleness.
`CorrectionTests` assert a `correction.recorded` overrides state and a malformed
one is ignored. `ActionAvailabilityTests` assert `resume` (blocked-only) and the
enclosure `integrate`/`cleanup` rules + `disabledReason`s. `WorkspaceTests` assert
tree assembly, metric counts, and `generatedAt`, plus (task 33) `project_workspace`'s
`active_worktree_groups` passthrough: a passed group set is stored sorted on
`WorkspaceProjection.activeWorktreeGroups` (the Topology's active scope), and the field defaults to an
empty list when the kwarg is omitted. `StoreIOTests` assert log
enumeration and the atomic round-trip (no `.tmp` left). `SnapshotReaderTests`
assert provider snapshot parsing with `snapshotStaleSeconds`, enclosure reading
from a real contract, the absent-surface empties, and `project_and_write`
end-to-end. The L10 regression (`test_resolves_leaf_doc_lifecycle_from_doc_id_case_insensitively`)
seeds the real series shape — lowercase enclosure leaf id, uppercase doc id, numbered doc slug
matching neither, no lifecycleId/enclosures[] on the doc — and asserts `read_task_documents` still
attaches the enclosure's lifecycle.

Slice 3b adds: `TokenSeriesTests` (cumulative fuel gauge from `tool.completed`; **260703-L15**
extends the suite with the served bound — `_tool_log(count)` builds token-bearing logs, a series
at exactly `TOKEN_SERIES_MAX` is untouched, and a 3000-call series decimates to the bound with
the newest `TOKEN_SERIES_RECENT` cumulative values exact, the first sample kept, the sequence
still monotonic, and the final cumulative equal to the full fold's),
`StalenessHistogramTests` (age bucketing), `AnalyticsAssemblyTests` (bounded
stalest leaderboard, `project_workspace` wiring analytics + histogram, and 3a
callers getting empty analytics), the seven reader suites
(`DriftSnapshotReaderTests`, `SidecarStalenessReaderTests`,
`SetupSummaryReaderTests`, `SetupProgressReaderTests`, `RouteCoverageReaderTests`,
`ToolReportsReaderTests`, `LedgerReaderTests`), `DriftSnapshotProducerTests` (a
git-backed round trip — the producer writes a snapshot a reader then parses), and
`ProjectAndWriteAnalyticsTests` (analytics populated end-to-end with a configured
repository). Slice 3c adds `TaskDocumentsReaderTests` (the `read_task_documents`
reader, its optional lifecycle binding, projection of active docs without lifecycle keys, master docs
as concrete task documents, archive exclusion, and inclusion in `build_analytics` and
`project_and_write`; L14 adds `test_exposes_orchestrates_on_the_task_doc_node` — a master with
`orchestrates` projects the list onto `TaskDocNode.orchestrates`, a doc without the field projects
`[]`).

Slice 05 (5b) adds `AttentionQueueTests`: the server-computed attention queue — alarms
ranked above warnings, the blocked-gate item carrying its lifecycle cross-ref + ask
detail, the inferred stale-session and dormant-fleeting items, the
provider-down / actionable-drift / failed-setup branches, and an empty queue for a calm tree.
Task 29 extends the drift branch so actionable-drift rows carry `actionable-drift:<repo>:<branch>` ids,
provenance detail from `memoryRoot`/`reportPath`, and `checkedAt` as `signalTs`.

Slice 05 (5c) extends `WorkspaceTests` (a worktree-backed enclosure with no event log now
synthesizes a paused persistent lifecycle) and adds
`test_persistent_synthesis_skips_enclosure_with_event_lifecycle` (no duplicate when an event-backed
lifecycle already exists), the Task 25 live-row cleanup cases (`test_stale_persistent_lifecycle_without_enclosure_is_removed`,
`test_terminal_persistent_lifecycle_without_enclosure_is_removed`, `test_reowned_enclosure_removes_old_event_lifecycle`,
`test_fleeting_lifecycle_does_not_need_enclosure`, `test_fresh_promotion_window_without_enclosure_is_kept`,
`test_fresh_blocked_promotion_window_without_enclosure_is_kept`, and
`test_legacy_blank_lifecycle_enclosure_keeps_event_lifecycle`), plus
`test_dormant_persistent_worktree_stays_out_of_the_attention_queue` (the attention-gate);
`SnapshotReaderTests` gains `test_read_providers_includes_per_worktree_stacks`
(surface 4 — the workspace stack plus each worktree's CGC/GrepAI bound to worktree/repo/role, a
malformed stack skipped).

Task 12 S2 extends `SnapshotReaderTests` with repo-scoped workspace provider cases:
`test_read_providers_projects_cgc_repo_watchers` pins CGC `resources.watchers` rows, and
`test_read_providers_projects_grepai_target_repos` pins GrepAI `targetRepos`. GrepAI only stays
aggregate when that current-state target evidence is absent.

Slice 5e adds `EngineProcessTests`: the enclosure-centered process map from `build_engine_processes`
— a successful external bootstrap (observed fact-states, complete boot edges, code-before-memory
engines), provider-setup running, failed setup (independent code engine + the failed phase line),
missing-status degradation, disabled-memory (no memory lane), sync-needed (behind-official → blocked +
the sync edge), the worktree-group-basename join, action reuse, determinism, and `project_workspace`
wiring (`analytics.engineProcesses`, version 2) — plus the §5.4 start-progress synthesis (a pre-contract
blocked start) and the `start_progress` write/read/clear round-trip. Slice 5f S6 (§9) adds the
attention-parity cases: a pre-contract blocked start raises a `blocked-start` `warn` item
(id/severity/detail), `project_workspace` threads it into the queue, and a happy-path beat is
observable as a synthesized node but raises no alarm. Slice 5h adds the additive-field mapping cases:
`landing`/`integrationStrategy` default empty/`None`, and a fact carrying a `status["landing"]` list +
a recorded `integration_strategy` maps onto `EngineProcessNode.landing`/`integrationStrategy`. The 5h
ledger popover adds the windowing tests: `LedgerReaderTests` gains `_ledger_window` (newest `LEDGER_WINDOW`
rows + the full total; missing/`None` → `([], 0)`) and a `read_ledger` row-windowing case, and
`EngineProcessTests` asserts `ledger_rows`/`ledger_row_count` pass through `build_engine_processes` onto
`EngineProcessNode.ledgerRows`/`ledgerRowCount` (default-empty + carried). The `_facts` helper gained
`ledger_rows`/`ledger_row_count` params. Slice 05l P1 (Gap B) adds
`EngineProcessTests.test_disposed_worktrees_drop_from_engine_processes`: a `cleanup: "pending"` fact
stays (1 node) while `cleanup: "completed"` and `cleanup: "abandoned"` facts drop (`[]`) — pinning
that a disposed enclosure leaves the active engine-room set so the frontend animates the removal, and
that `cleanup-pending` keeps its live node. Slice 05m adds
`EngineProcessTests.test_carryover_done_at_surfaces_on_the_node` (a fact whose `status` carries
`carryoverDoneAt` maps it onto `EngineProcessNode.carryoverDoneAt` — 5k renders it) and
`test_carryover_done_at_defaults_to_none` (absent → `None`). **Tier 2** adds `LedgerCommitMetaTests` (real `git init` repos):
`_git_commit_meta` batches a single probe mapping each commit → (committer ISO date, subject), drops a bogus
SHA with no HEAD fallback, and returns `{}` for a non-repo / empty input; `_ledger_window` and `read_ledger`
enrich each served row when the commits are local and leave the message/date fields `None` (the row still
served by its hash) when they are not.
Task 31 extends this area with configured-only versus live worktree provider assertions: `read_providers`
can use mocked Docker inspect data to mark a worktree stack ready, while `build_engine_processes` emits
missing code/memory provider placeholders and missing facts when a worktree expects providers but no
runtime facts match. It also covers `_inspect_result_map` directly so Docker inspect parsing handles
valid arrays, slash-prefixed names, non-dict entries, empty names, invalid JSON, non-list JSON, and
non-string input without leaving the new provider-runtime parser uncovered.
Task 29 adds `WorktreeProviderAdmissionTests`, active-group filters, direct-reader compatibility, and projection hot-path coverage:
active build lifecycles admit worktree provider/setup files, parked or terminal enclosures and
close/integration phases do not page provider alarms, non-terminal close-phase enclosures can still feed
Engine Room status, unfiltered provider reads still include worktree stacks for diagnostics, inactive
provider/setup/engine-process files are skipped when filters are supplied, and `project_and_write`
reuses the TTL-gated repo-surface cache so provider-state refreshes are not hidden behind repeated git
surface probes.

**L5 (260628_operations-integration)** adds the durable-state retention regressions.
`WorktreeProviderAdmissionTests.test_active_group_survives_a_pruned_lifecycle_log` pins the Engine Room
fix: a `cleanup:"pending"` enclosure with **no** lifecycle log (the log was pruned for inactivity) is
still returned by both `active_enclosure_worktree_groups` and `admitted_worktree_groups` — admission
keys on the durable enclosure, not the prunable log. The new `SeriesRetentionTests` cover
`series_retained_lifecycle_ids`: a live master protects every leaf including archived siblings while a
second live master is independently protected
(`test_live_master_protects_every_leaf_including_archived_siblings`); a fully-archived master with no
readable contract timestamp is released (`..._without_readable_timestamp_is_released`); an archived
master is retained inside the one-week grace and released past it (using `os.utime` on a real contract
file — `test_archived_master_is_retained_within_grace_then_released_after`); and an enclosure with no
`taskName` is never series-protected (`..._is_not_series_protected`).

Slice 3c **reopened (R1)** adds the series-master cases to `TaskDocumentsReaderTests`:
`test_read_series_documents_projects_master` (a mixed-status master → a `SeriesNode` with
`doneCount`/`totalCount` over the declared `subTasks[]` + the full render), `..._skips_leaf_docs` (a leaf
is not a series — the disjoint partition), `test_declared_subtask_status_is_authoritative_over_leaf_steps`
(a subtask marked `Completed` counts done even with an open leaf step), the missing-dir empty, and
`test_build_analytics_includes_series` (the additive `Analytics.series` wiring). Task 17 extends this
area with `TaskDocNode.createdAt`, `SeriesNode.objective`, and
`test_read_series_documents_orders_subtasks_by_leaf_creation`, which writes master rows in misleading
filename/number order plus sibling leaf docs and asserts the projected rows are oldest-first by leaf
`createdAt`. Task 21 adds a workspace-level series token rollup regression: linked leaf task documents
with lifecycle token totals sum into `Analytics.series[].seriesTokenTotal`, while a missing sibling row
contributes zero.

Slice 6c adds `GateProjectionTests` (a durable open gate materializes onto
`LifecycleProjection.gate` with its decision verbs; a decided gate is not attached; the
latest open gate wins; an open gate raises a `gate-open` attention item; no gates leaves
both clean) and `GateReaderTests` (`snapshots.read_gates` folds lifecycle + workspace gate
logs; a missing root reads empty).

Task 28 adds the NOTIFY-AND-CONTINUE attention cases:
`test_awaiting_developer_yields_one_info_item` (an `awaiting-developer` lifecycle yields
exactly one `info` attention item carrying the summary as its `detail` — no
double-emission), `test_blocked_with_open_gate_dedups_to_gate_open` (a `blocked` lifecycle
that ALSO has a durable open gate yields ONE lifecycle-lane item — the `gate-open` — and no
`blocked-gate`; the gate-open/blocked-gate dedup), and
`test_bare_block_without_gate_still_yields_blocked_gate` (PARK-not-delete: a bare `block()`
with no `GateRecord` still raises a `blocked-gate`).
`AttentionDismissalTests` pins lifecycle-scoped acknowledgement behavior: awaiting/blocked/stale/dormant
and gate-open rows suppress only when the acknowledgement record matches the lifecycle, newer turn-end
signals re-surface the item, and non-lifecycle provider alarms are not suppressible by orphaned
acknowledgement rows. Task 29 extends this suite so targetless actionable-drift acknowledgements suppress
only until a newer drift snapshot appears. `SnapshotReaderTests` adds an end-to-end `project_and_write` assertion that a
completed lifecycle prunes its attention acknowledgement file from disk.

Current `TaskDocumentsReaderTests` assert the Operations projection contract. `read_task_documents`
takes `enclosures=` for optional lifecycle binding, but projects active JSON-primary light/subTask and
master documents even when no lifecycle binding exists. `test_projects_docs_without_lifecycle_and_skips_non_task_json`,
`test_master_without_a_lifecycle_projects_as_task_document`, `test_master_stays_on_series_surface`,
`test_nested_masters_stay_on_series_surface`, and `test_archived_task_documents_are_not_projected` pin
the active-doc-first behavior, master dual-surface behavior, and archive/delete disappearance boundary.
`test_leaf_contract_alone_is_not_a_task_document` proves an active
`enclosures/<leaf-id>/series-contract.md` is enclosure state only and does not project into
`analytics.taskDocuments`. Creation-order coverage deliberately uses stored sub-task numbers that do not
match desired display order, so the test pins structured timestamps rather than string-prefix parsing.
Task 17 live-data numbering coverage also pins `TaskDocNode.id` in the projection schema/fixture path,
so clients can label authored leaves from the child task id instead of parent fallback labels.

### Conventions

Inserts `mcp/src` on `sys.path` (the suite idiom). `_event`/`_started`/`_enclosure`
build fixtures; fixed `T0`/`FRESH`/`STALE`/`DORMANT` datetimes make the staleness
windows deterministic; a local `McpRuntimeConfig` factory + `current_state_path`
back the snapshot/store tests, and `default_contract`/`write_contract` produce a
real contract for `read_enclosures`. The 3b suites write fixture files (drift
snapshots, sidecars, setup/progress JSON, route indexes, tool reports, ledgers)
into tmp roots; `DriftSnapshotProducerTests` uses a real `git init -b` + empty
commit with a `SimpleNamespace` context. Drift snapshot fixtures and the producer
round-trip now use the shared `drift_snapshot_path` helper, and
`ProjectAndWriteAnalyticsTests.test_project_and_write_prunes_orphaned_worktree_drift_snapshots`
proves projection-time pruning keeps configured repo snapshots and active
worktree snapshots while deleting a valid snapshot for a deleted worktree.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The projection schema asserted against, including `TaskDocNode.id`, optional `TaskDocNode.lifecycleId`, `TaskDocNode.createdAt`, `SeriesSubTaskNode.createdAt`, and `SeriesNode.objective`. | L412-L507 | [projection.py](../src/agents_remember/observer/projection.py) |
| The structural readers under test project all active task docs, populate master objective, leaf creation-order metadata, and task `id`/`createdAt`. | L584-L736; L757-L783 | [snapshots.py](../src/agents_remember/observer/snapshots.py) |
| The task-document reader tests assert lifecycle `createdAt`, unbound docs, master docs, and archive exclusion. | L1525-L1698 | [test_observer_projection.py](test_observer_projection.py) |
| The creation-order regression writes sibling leaf task docs and expects rows sorted oldest-first by leaf `createdAt`. | L1760-L1818 | [test_observer_projection.py](test_observer_projection.py) |
| The series-token regression joins master rows to sibling leaf task docs and sums bound lifecycle token totals. | L420-L490 | [test_observer_projection.py](test_observer_projection.py) |
| The fold + inferred layer + action availability under test. | L1-L92 | [reducer.py](../src/agents_remember/observer/reducer.py) |
| The provider-node helper under test for CGC repo watcher expansion, GrepAI `targetRepos`, and aggregate fallback when target evidence is absent. | L1-L92 | [provider_nodes.py](../src/agents_remember/observer/provider_nodes.py) |
| The active-enclosure admission helper under test for strict provider groups and broader Engine Room groups. | L18-L84 | [worktree_provider_admission.py](../src/agents_remember/observer/worktree_provider_admission.py) |
| The admission resilience (missing-log survives) + series-retention helpers under test. | `test_active_group_survives_a_pruned_lifecycle_log`, `SeriesRetentionTests` | [test_observer_projection.py](test_observer_projection.py) |
| The `series_retained_lifecycle_ids` / `_series_is_retired` / `_contract_finalized_at` derivation the L5 cases pin. | `series_retained_lifecycle_ids` | [worktree_provider_admission.py](../src/agents_remember/observer/worktree_provider_admission.py) |
| Snapshot readers accept active worktree groups so stale worktree provider/setup/engine facts are skipped before the reducer. | L112-L203; L496-L535; L778-L805 | [snapshots.py](../src/agents_remember/observer/snapshots.py) |
| Actionable drift rows expose repo/branch ids, drift provenance detail, and `checkedAt` signal timestamps. | L1439-L1468 | [test_observer_projection.py](test_observer_projection.py) |
| Targetless actionable-drift dismissal suppresses only the current snapshot occurrence. | L1604-L1629 | [test_observer_projection.py](test_observer_projection.py) |
| The log reader + atomic writer + orchestrator under test. | L1-L90 | [projection_store.py](../src/agents_remember/observer/projection_store.py) |
| Projection reads active admission sets once and caches repo surfaces on a short TTL. | L151-L180; L217-L240 | [projection_store.py](../src/agents_remember/observer/projection_store.py) |
| Task-29 tests cover admission, inactive runtime filters, repo-surface caching, and the engine-process active-group gate. | L169-L258; L1034-L1132; L1863-L1907; L2283-L2324; L3109-L3134 | [test_observer_projection.py](test_observer_projection.py) |
| The drift-snapshot producer exercised by the round-trip test. | L1-L88 | [onboarding_drift_check/summary.py](../src/agents_remember/memory_quality/integrity/onboarding_drift_check/summary.py) |
| The shared drift-snapshot path/pruning helper used by fixtures and projection pruning coverage. | L17-L60 | [drift_snapshots.py](../src/agents_remember/observer/drift_snapshots.py) |
| The shared drift-snapshot dir/schema the fixtures use. | L1-L47 | [paths.py](../src/agents_remember/observer/paths.py) |

## Series-Contract Notes

Observer projection coverage now distinguishes root series contracts from live leaf enclosure contracts,
validates new leaf identity fields, proves archives/enclosure folders are excluded from task JSON scans,
and verifies that a leaf contract itself is not a readable lifecycle task document. 260703-L11 extends
`SnapshotReaderTests` with worktree-existence coverage: a shared external-memory contract factory
(`_existence_contract`) backs `test_read_enclosures_stat_worktree_existence` (flags flip False→True as
the code/memory directories appear on disk, no contract rewrite) and
`test_read_enclosures_reopened_is_reset_awaiting_restart_not_archived` (a `cleanup=reopened` contract
still projects — it is NOT archived — but with both flags False until `worktree_start` recreates the
directories).

## Update History

- 2026-07-10T01:14+02:00 — 260707-HFX2-L13 F6: changed projection fixtures to assert summary-only
  task/series bodies and repaired the governing-overview backlink. Verification metadata remains
  pinned until closeout stamps the eventual L13 code commit.

- 2026-07-07T05:16+02:00 — 260703-L15 S2: `TokenSeriesTests` gained the served-bound coverage —
  `_tool_log` builder, at-the-bound untouched, and the 3000-sample decimation case (length ==
  `TOKEN_SERIES_MAX`, newest `TOKEN_SERIES_RECENT` exact, first sample kept, monotonic, total
  preserved); `TOKEN_SERIES_MAX`/`TOKEN_SERIES_RECENT` joined the reducer imports.
  Verification metadata pinned until closeout stamps the L15 commit.

- 2026-07-06T23:58:42+02:00 — 260703-L14 (visual hierarchy + chat grouping): added
  `TaskDocumentsReaderTests.test_exposes_orchestrates_on_the_task_doc_node` — a master doc with
  `orchestrates` projects the list onto `TaskDocNode.orchestrates`; a doc without the field
  projects `[]`. Verification metadata pinned until closeout stamps the L14 commit.
- 2026-07-06T02:20+02:00 — 260703-L11: added `SnapshotReaderTests` coverage for the
  `EnclosureNode.codeWorktreeExists`/`memoryWorktreeExists` stat-time flags and the
  reopened-is-reset-not-archived semantics (visible-again-after-restart included).
  Verification metadata pinned until closeout stamps the L11 commit.
- 2026-07-03T00:30+02:00 — L11 adds reducer coverage for abandoned-enclosure lifecycle terminalization and the persistent-synthesis skip for abandoned/reopened enclosures.
- 2026-07-02T21:45+02:00 — L10 binding repair: added
  `test_resolves_leaf_doc_lifecycle_from_doc_id_case_insensitively` — the real-world series shape
  (lowercase enclosure leaf id `260628-l7`, uppercase doc id `260628-L7`, numbered doc slug matching
  neither, no lifecycleId/enclosures[] on the doc) binds to the enclosure lifecycle. Verification
  metadata pinned until closeout stamps the L10 commit.
- 2026-06-30T00:00:00+02:00 — L5 (260628_operations-integration): added `test_active_group_survives_a_pruned_lifecycle_log`
  (a live enclosure with no lifecycle log stays in both admission sets) and the `SeriesRetentionTests`
  suite for `series_retained_lifecycle_ids` (live master protects all leaves incl. archived siblings;
  fully-archived-no-timestamp released; archived retained-within-grace then released-past-grace via
  `os.utime`; no-taskName not protected). Verification metadata pinned until closeout stamps the L5 code
  commit.
- 2026-06-28T07:32+02:00 — Task 29 S7 follow-up: added/recorded projection regressions for provenance-rich
  actionable-drift rows and targetless dismissal that re-surfaces on newer drift snapshots. Verification
  metadata pinned until closeout stamps the task-29 code commit.
- 2026-06-28T07:30+02:00 — Task 33: added `WorkspaceTests` coverage for `project_workspace`'s new
  `active_worktree_groups` passthrough (sorted onto `activeWorktreeGroups`) and the default-empty case.
  Verification metadata pinned until closeout stamps the code commit.
- 2026-06-28T05:38+02:00 — Task 29: added projection coverage for active-enclosure
  worktree provider admission, inactive provider/setup/engine-process filters, unfiltered provider
  reader compatibility, the broader Engine Room active group, and the repo-surface cache that keeps
  provider refresh on the fast path. Verification metadata pinned until closeout stamps the task-29 code commit.
- 2026-06-28T03:52+02:00 — Task 28 S5.2 after source sync: added lifecycle-scoped
  attention acknowledgement coverage, including record-shaped reducer dismissals, non-lifecycle
  provider alarms staying visible, newer turn-end re-surfacing, and `project_and_write` pruning
  completed lifecycle acknowledgement rows from disk. Verification metadata pinned until closeout
  stamps the task-28 code commit.
- 2026-06-28T03:33+02:00 — Task 32 memory-mirror pruning: drift snapshot tests now use the
  shared path helper, assert producer output lands at that path, and cover `project_and_write`
  physically pruning valid snapshots for deleted worktrees while keeping configured repos, active
  worktrees, and invalid diagnostics. Verification metadata pinned until closeout stamps the task-32
  code commit.
- 2026-06-28T03:11+02:00 — Task 31 closeout quality: added direct `_inspect_result_map` coverage for Docker inspect parser success and unusable payload cases, addressing the touched-file CRAP threshold finding. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-27T23:08+02:00 — Task 31 provider-state honesty: added observer regressions for live Docker-backed worktree provider state, configured-only static inventory, and missing provider placeholders in `EngineProcessNode.providers`. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-27T22:00+02:00 — Task 28 (NOTIFY-AND-CONTINUE turn end + gate dedup): `FoldTests` gained
  `test_awaiting_developer_then_resume` (the `awaiting-developer` fold carries `summary` on the `ask`
  carrier; `lifecycle.resumed` clears it), and the attention-queue coverage gained
  `test_awaiting_developer_yields_one_info_item` (one `info` item, no double-emission),
  `test_blocked_with_open_gate_dedups_to_gate_open` (blocked + durable open gate → one `gate-open`, no
  `blocked-gate`), and `test_bare_block_without_gate_still_yields_blocked_gate` (a bare block still yields
  `blocked-gate`). Verification metadata pinned until closeout stamps the code commit.
- 2026-06-26T20:18+02:00 — Task 21 series token rollup: workspace projection coverage now proves
  `SeriesNode.seriesTokenTotal` sums linked leaf lifecycle tokens and ignores missing sibling rows.
  Verification metadata pinned until closeout stamps the code commit.
- 2026-06-26T15:13+02:00 — Task 25 lifecycle live-row cleanup: `WorkspaceTests` now pins that stale
  or terminal non-fleeting lifecycles without a current enclosure disappear from the live projection,
  re-owned enclosures keep only the new owner, fleeting lifecycles do not require enclosures, and fresh
  running or blocked promotion/gate windows stay visible. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-24T18:11+02:00 — Task 17 live-data numbering: observer projection tests now account for
  required `TaskDocNode.id`, the child task id used by clients for authored leaf labels. Verification
  metadata pinned until closeout stamps the code commit.
- 2026-06-24T16:39+02:00 — Task 17 Operations reader tests: coverage now asserts docs without lifecycle
  binding project, master docs project as task documents while staying on the series surface, and
  archived docs are excluded so archive/delete remains the disappearance boundary. Verification metadata
  pinned until closeout stamps the code commit.
- 2026-06-24T12:21+02:00 — Task 17 projection-reader regression: test coverage now asserts task
  `createdAt`, master `objective`, and oldest-first series sub-task ordering from sibling leaf
  `createdAt` metadata instead of number or filename prefixes. Verification metadata pinned until
  closeout stamps the code commit.
- 2026-06-24T08:59+02:00 — Task-document correction: added/kept
  `test_leaf_contract_alone_is_not_a_task_document`, proving active leaf `series-contract.md` files do
  not project into `analytics.taskDocuments`; promoted leaves need real JSON-primary task documents for
  readable content. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: observer projection tests now build root/leaf series-contract fixtures, assert leaf identity fields, skip root series contracts as process nodes, and exclude archived/enclosure task JSON from task projection scans. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-23T22:31+02:00 — Clarified Task 12 S2 test wording: GrepAI `targetRepos` prove addressable
  repo/project targets for topology projection, while the no-target case remains the aggregate fallback.
  Verification metadata will be stamped at closeout.
- 2026-06-23T22:09+02:00 — Task 12 S2 correction: added
  `test_read_providers_projects_grepai_target_repos`, proving GrepAI `targetRepos` become repo-scoped
  workspace memory provider nodes while the existing no-target fallback remains aggregate. Verification
  metadata will be stamped at closeout.
- 2026-06-23T21:46+02:00 — Task 12 S2: `SnapshotReaderTests` now covers CGC `resources.watchers`
  expansion into repo-scoped workspace provider nodes. Later 22:09/22:31 entries document the GrepAI
  `targetRepos` correction and the no-target aggregate fallback. Verification metadata pinned until
  closeout stamps the S2 code commit.
- 2026-06-21T06:40+02:00 — slice 05m (carryover-before-cleanup): added `EngineProcessTests.test_carryover_done_at_surfaces_on_the_node` (a fact whose `status` carries `carryoverDoneAt` maps it onto `EngineProcessNode.carryoverDoneAt`) and `test_carryover_done_at_defaults_to_none` (absent → `None`) — pinning the display-only carryover-milestone projection. Verification metadata pinned until closeout stamps the 05m code commit.
- 2026-06-21T04:10+02:00 — slice 05l P1 (backend teardown visibility, Gap B): added `EngineProcessTests.test_disposed_worktrees_drop_from_engine_processes` — a `cleanup: "pending"` fact stays (1 node), `cleanup: "completed"`/`"abandoned"` facts drop (`[]`), pinning that `build_engine_processes` filters disposed (cleaned-up/abandoned) enclosures while keeping `cleanup-pending`'s live node. Verification metadata pinned until closeout stamps the 05l-P1 code commit.
- 2026-06-21T02:44+02:00 — Slice 6g: reworked `TaskDocumentsReaderTests` — threaded `enclosures=` through `read_task_documents` calls; split the "master skipped" case into `test_master_without_a_contract_is_skipped` + `test_master_is_contract_paired_to_series_lifecycle`; added `test_cross_master_links_resolve_to_lifecycles` (subTask `file`→`linkedLifecycleId`, doc `master` ref→`masterLifecycleId`). Verification metadata pinned until closeout stamps the 6g code commit.
- 2026-06-19T03:17+02:00 — slice 3c reopened (R1, masters observable): added the series-master cases to `TaskDocumentsReaderTests` — `read_series_documents` projects a mixed-status master (done/total over the declared `subTasks[]`), skips a leaf (disjoint partition), is authoritative over a slice's leaf steps, empties on a missing dir, and `build_analytics` carries `Analytics.series`. Verification metadata pinned until closeout stamps the R1 code commit.
- 2026-06-18T21:25+02:00 — slice 5h Tier 2: added `LedgerCommitMetaTests` (real git repos) — `_git_commit_meta` batched probe + bogus-SHA drop (no HEAD fallback) + best-effort `{}`, and `_ledger_window` / `read_ledger` row enrichment vs the honest hash-only fallback. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-18T18:00+02:00 — slice 5h ledger popover: added the windowing tests — `_ledger_window` + `read_ledger` row-windowing (`LedgerReaderTests`) and the `ledger_rows`/`ledger_row_count` pass-through (`EngineProcessTests`); `_facts` gained the ledger params. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-18T14:05 — Task 6 slice 6c Part A: added `GateProjectionTests` (gate materialized onto the lifecycle + `gate-open` attention item, all branches) and `GateReaderTests` (`read_gates` fold). Verification metadata pinned until closeout stamps the 6c Part A code commit.
- 2026-06-18T08:51+02:00: Slice 5h H1 — added the landing/integrationStrategy mapping cases to `EngineProcessTests` (default-empty + mapped-from-facts). Verification metadata pinned until closeout stamps the 5h code commit.
- 2026-06-16T03:25: Slice 5f S6 (§9) — added the blocked-start attention-parity tests to `EngineProcessTests` (`build_attention_queue` raises a `blocked-start` `warn` item; `project_workspace` threads it; a happy-path beat is observable-but-not-an-alarm). Verification metadata pinned until closeout stamps the S6 code commit.
- 2026-06-15T19:35: Slice 5e — added `EngineProcessTests` (the `build_engine_processes` process map: bootstrap / running / failed / missing / disabled / sync-needed / join / actions / determinism / wiring) plus the §5.4 start-progress synthesis + write/read/clear tests. Verification metadata pinned until closeout stamps the 5e code commit.
- 2026-06-14T23:30+02:00: Slice 05 (5c) — added persistent-lifecycle synthesis tests (`WorkspaceTests` synthesis count, dedup-skip, the dormant-worktree attention-gate) and `test_read_providers_includes_per_worktree_stacks` (surface 4 per-worktree provider read). Verification metadata pinned until closeout stamps the 5c code commit.
- 2026-06-14T17:28+02:00: Slice 05 (5b) — added `AttentionQueueTests` covering `build_attention_queue`'s severity ranking + per-source branches through `project_workspace`. Verification metadata pinned until closeout stamps the 5b code commit.
- 2026-06-14T00:16: Slice 3c commit 3 — added the defensive `test_master_is_not_projected_as_a_lifecycle` to `TaskDocumentsReaderTests` (a `kind:"master"` doc carries no `lifecycleId`, so the reader globs but skips it). Verification metadata pinned until closeout stamps the 3c commit-3 code commit.
- 2026-06-13T22:34: Slice 3c commit 2 — added the first `TaskDocumentsReaderTests` for task-document projection plus analytics/end-to-end inclusion; later Task 17 expanded that coverage to active docs with optional lifecycle binding. Verification metadata pinned until closeout stamps the 3c commit-2 code commit.
- 2026-06-13T20:48+02:00: Slice 3b — added the analytical-surface test suites
  (token series, staleness histogram, analytics assembly, the seven readers, a
  git-backed producer round trip, and `project_and_write` analytics end-to-end).
  Verification metadata is pinned until closeout stamps the 3b code commit.
- 2026-06-13T19:30+02:00: Created for slice 3a — tests for the projection read side
  (fold/determinism, inferred layer, corrections, action availability, workspace
  assembly, atomic write, structural readers). Verification metadata is pinned
  until closeout stamps the 3a code commit.
