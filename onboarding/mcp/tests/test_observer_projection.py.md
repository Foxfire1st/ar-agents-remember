# test_observer_projection.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_observer_projection.py`          |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-08-01T14:20+02:00 |
| lastVerifiedCommitHash | `a714114ef94eedb8042fb4caa38d9469f4767dd6`       |
| lastVerifiedCommitDate | 2026-08-01T18:06:36+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

`test_observer_projection.py` covers the observer projection read side (slice 3a):
the pure fold and its determinism, the inferred layer, append-only corrections,
precomputed action availability, workspace tree assembly, the atomic projection
write, and the structural surface readers. L11 adds abandon-terminality coverage:
an abandoned-enclosure lifecycle projects `abandoned`, and abandoned/reopened
enclosures synthesize no paused persistent lifecycle.

### 260712-TRH-L7 landing snapshot integration

The projection tests now exercise projected status receiving immutable landing facts rather than invoking remote landing probes during the recurring read.

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
`active_worktree_groups` passthrough: a group set passed as
`structure=WorkspaceStructure(..., active_worktree_groups=[...])` is stored sorted on
`WorkspaceProjection.activeWorktreeGroups` (the Topology's active scope), and the field defaults to an
empty list when that `WorkspaceStructure` field is left out. `StoreIOTests` assert log
enumeration and the atomic round-trip (no `.tmp` left). `SnapshotReaderTests`
assert provider snapshot parsing with `snapshotStaleSeconds`, enclosure reading
from a real contract, the absent-surface empties, and `project_and_write`
end-to-end. The L10 regression (`test_resolves_leaf_doc_lifecycle_from_doc_id_case_insensitively`)
seeds the real series shape — lowercase enclosure leaf id, uppercase doc id, numbered doc slug
matching neither, no lifecycleId/enclosures[] on the doc — and asserts `read_task_documents` still
attaches the enclosure's lifecycle.

#### 260731-EFA-L4 — the lifecycle-state vocabulary suites (L1625-L2013)

Five classes added between `TokenSeriesTests` and `StalenessHistogramTests`. They exist for a set
difference, not a typo: `Metrics` bucketed **three** states by hand while `State` declared **six**,
so an `awaiting-developer` lifecycle counted towards `lifecycleCount` and `totalTokens` and towards
nothing else — the rollup could not show a lifecycle that had handed the turn back.

- **`MetricsBucketVocabularyTests` (L1625-L1730)** — the coverage half. `live_states()` re-derives
  the live set as `STATES` minus `TERMINAL_STATES` rather than reading `projection.ACTIVE_STATES`
  (which *is* the live half verbatim), **so the measurement is not taken with the same instrument
  it is checking**, and a seventh state fails here.
  `test_the_vocabulary_scan_found_the_states` pins that the derivation found something, so a scan
  matching nothing cannot satisfy everything below it. `test_every_live_state_has_a_metrics_bucket`
  and `test_the_metrics_buckets_are_exactly_the_live_states` hold the two directions —
  `lifecycleCount` excluded by name as the all-states total, the one `*Count` field that is
  deliberately not per-state. `test_every_live_state_is_actually_counted` drives one real lifecycle
  per live state through `project_workspace` and requires every bucket to read `1` and the total to
  equal the number of live states — the fields existing is not the same as the reducer filling
  them. `test_an_awaiting_developer_lifecycle_is_no_longer_uncountable` pins the reported symptom.
  The `_log(state)` helper derives its event kind from the state (`lifecycle.<state>`) rather than
  from a fourth table keyed by it.
- **`StatePartitionTests` (L1733-L1797)** — deriving the bucket set as "the vocabulary minus
  `TERMINAL_STATES`" only moves the hand-written list one level down unless `TERMINAL_STATES` is
  itself tied to the vocabulary. It is: `State` is **composed** from the two halves. These hold
  `check_state_partition` to totality and disjointness (`ACTIVE_STATES == LIVE_STATES` verbatim)
  and drive its three refusals — a state filed on neither side ("neither live nor terminal"), on
  both, and a filed state missing from the vocabulary — against **synthetic** `Literal`
  vocabularies, so the guard is exercised without the real declaration having to be wrong.
- **`TerminalityIsStructuralTests` (L1800-L1917)** — totality stops a state escaping
  classification; it cannot stop one being classified **wrongly**, and a mis-filed state is the
  same defect wearing the fix. So terminality gets an observable definition and is checked against
  the fold in both directions: a terminal state is one the log reaches **only** through
  `lifecycle.ended` (`coerce_end_outcome(state) == state`), and a live state is one some event kind
  declares outright (`f"lifecycle.{state}" in _KIND_UPDATES`). `seeded_state()` asks the fold what a
  bare `lifecycle.started` projects into rather than naming it. `test_is_terminal_reads_the_same_partition`
  keeps `LifecycleState.is_terminal` and the projection from disagreeing, and
  `test_the_ambient_end_signal_accepts_exactly_the_terminal_states` holds the **write** side to the
  same set — `AmbientLifecycle.end` validates against `TERMINAL_STATES` and converts through
  `coerce_end_outcome`, so a terminal state the reducer can project but no session can write fails
  here whatever the write side is spelled in.
- **`StateVocabularyReaderTests` (L1920-L1955)** — `vocabulary_names` must read every legal
  declaration form. `get_args` alone is only correct for a **flat** `Literal`; on the union form
  (`Literal[...] | ReviewState`, a plausible way to fold a second vocabulary in) it returns
  `Literal` objects, and the first consumer to call `.split` on one dies with `AttributeError` at
  import of `agents_remember.observer` — the whole package goes down and the traceback names none
  of this. These pin the reading, the flattening of an alias composition, the by-name refusals
  (non-string member, empty declaration), and that the real declarations read as plain `str`.
- **`StateCountFieldTests` (L1958-L2013)** — the state → bucket-field naming rule, held one-to-one
  and identical to the client's. `test_a_capital_in_the_tail_survives` records why Python moved:
  `dashboard/src/types/projection.ts` derives the names with `Capitalize<Camel<Tail>>`, which
  upper-cases the first character and leaves the rest alone, while Python used `str.capitalize`,
  which lower-cases the tail — so the two copies of one rule disagreed on `awaiting-DEVELOPER`.
  TypeScript's is the rule expressible on both sides. `test_two_states_sharing_a_bucket_are_refused_rather_than_merged`
  is the reviewer's case: `awaiting-Developer` beside `awaiting-developer` produced three
  lifecycles, `awaitingDeveloperCount: 1`, and a **green** vocabulary suite, because the coverage
  tests compare per-state values that both resolve to the merged field and therefore agree with
  themselves. `state_count_fields` refuses to be built instead, and
  `test_a_merged_bucket_would_have_under_counted_the_rollup` shows the number the dashboard would
  have read.

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

**260731-EFA-L3** adds one case to that class:
`test_a_wedged_git_log_degrades_to_hash_only_rows_instead_of_failing_the_tick` (L2895-L2921). It is the
only test in this suite that patches git rather than running it: `mock.patch.object(snapshots,
"run_git", side_effect=subprocess.TimeoutExpired(cmd=["git", "log"], timeout=300))` over a real
two-commit repo with a written ledger. `TimeoutExpired` is a `SubprocessError` and a `SubprocessError`
is **not** an `OSError`, so when `snapshots._git_commit_meta` moved onto a runner that has a timeout,
its `except OSError` stopped covering the failure the timeout produces — the raise would have escaped
through `_enrich_ledger_rows` and taken down the projection tick. The case drives **both** entry points
inside one patch — `_ledger_window(...)` (worktree coupler) and `read_ledger(repo, code_root=repo)`
(official coupler) — and asserts the honest degrade rather than the absence of a crash: `total` still
equals the full ledger row count, `rows[0].codeCommit` still carries the hash, and `codeSubject` /
`memoryDate` / `node.rows[0].codeSubject` are all `None`, i.e. the enrichment is dropped and never
faked. Asserting the `LedgerNode` builder separately is deliberate — the two windowing sites call
`_git_commit_meta` through different paths, so one guard covering only one of them would pass a
single-entry-point test.
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
completed lifecycle's attention acknowledgement is pruned
(`test_project_and_write_prunes_completed_lifecycle_attention_acknowledgement`, L1504-L1538).

Since 260731-EFA-L5 (R5) that assertion is about **emptiness, not absence**. It used to end
`assertFalse(dismissals.log_path().exists())`; the unlink that made it true is the defect the leaf
removed. `AttentionDismissalStore` rewrote to empty by unlinking, so a concurrent dismisser
holding an `"a"`-mode handle wrote into an inode with no remaining links and its record vanished
with the file — no torn line, no exception, nothing for the caller to notice, and it is where the
measured **31.45%** dismissal loss came from. The three assertions that replaced it are strictly
stronger than the one they replace: `dismissals.read() == []`, `log_path().is_file()`, and
`log_path().read_bytes() == b""`. Zero bytes read back is proof the row physically left; a missing
file only proved something removed the file.

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
real contract for `read_enclosures`.

`_event` takes provenance as `by=<Attribution>` and the promotion target as
`enclosure=EnclosureRef(path, repo_id)` rather than as loose `trust`/`actor`/`enclosure`/`repo_id`
keywords. The four provenance pairs the suite uses are named module constants —
`DECLARED_BY_MODEL` (the `_event` default), `OBSERVED_BY_MODEL`, `OBSERVED_BY_SYSTEM`, and
`INFERRED_BY_SYSTEM` — so a case cannot quietly invent a fifth trust/actor combination, and
`EnclosureRef` keeps the contract path and its repo id together because a promotion carries both
or neither. The production entry points are likewise driven through their parameter objects:
`project_workspace(logs, structure=WorkspaceStructure(enclosures, providers,
active_worktree_groups), now=..., given=AnalyticalInputs(...))`,
`build_analytics(AnalyticalInputs(...))`, `build_attention_queue(lifecycles, providers,
AnalyticalInputs(...))`, `create_gate(kind, gate_id=..., now=..., anchor=GateAnchor(lifecycle_id))`
with `decide_gate(gate, GateVerdict(...), now=...)`, `default_contract(ContractTask(...),
leaf=LeafIdentity(...), code=RepoBranchPlan(...), memory=RepoBranchPlan(...))`, and
`write_start_progress(root, StartingEnclosure(...), StartBeat(...))`.

The 260731-EFA-L4 vocabulary suites add two local conventions. First, every derived set is derived
with a *different* instrument from the one under test — `live_states()` subtracts
`TERMINAL_STATES` from `STATES` rather than reading `ACTIVE_STATES`, and `seeded_state()` asks the
fold rather than naming `running` — so no assertion can agree with itself. Second, the partition
and reader guards are driven against **synthetic** `Literal` vocabularies declared as class
attributes (`StatePartitionTests.LIVE` / `.TERMINAL`, L1745-L1746) plus inline `Literal[...]`
arguments, so a refusal is exercised without the shipped declaration having to be wrong; only
`test_the_real_partition_is_total_and_disjoint` and
`test_the_real_bucket_fields_are_distinct` assert against the live vocabulary. `typing.Literal` is
imported for exactly that (L23). The `EngineProcessTests` contract fixtures ask for
`workflow_kind="light-task"`; the bare `"light"` they used is no longer a member of `WorkflowKind`.

Git is exercised for real, not mocked, everywhere except one case: the suite imports the module
object (`from agents_remember.observer import snapshots`, L43) purely so
`LedgerCommitMetaTests.test_a_wedged_git_log_degrades_to_hash_only_rows_instead_of_failing_the_tick`
can patch `snapshots.run_git` — a wedged git cannot be produced with a real repository. Patching the
module attribute rather than `kernel.git_command.run_git` is what makes the test see the binding
`snapshots.py` actually resolves at call time, so a future re-import from a different module fails it.

The 3b suites write fixture files (drift
snapshots, sidecars, setup/progress JSON, route indexes, tool reports, ledgers)
into tmp roots; `DriftSnapshotProducerTests` uses a real `git init -b` + empty
commit with a `SimpleNamespace` context. Drift snapshot fixtures and the producer
round-trip now use the shared `drift_snapshot_path` helper, and
`ProjectAndWriteAnalyticsTests.test_project_and_write_prunes_orphaned_worktree_drift_snapshots`
proves projection-time pruning keeps configured repo snapshots and active
worktree snapshots while deleting a valid snapshot for a deleted worktree.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The projection schema asserted against, including `TaskDocNode.id`, optional `TaskDocNode.lifecycleId`, `TaskDocNode.createdAt`, `SeriesSubTaskNode.createdAt`, and `SeriesNode.objective`. | `TaskDocNode` L585-L631; `SeriesSubTaskNode` L634-L649; `SeriesNode` L662-L688 | [projection.py](../src/agents_remember/observer/projection.py) |
| The structural readers under test project all active task docs, populate master objective, leaf creation-order metadata, and task `id`/`createdAt`. | `read_task_documents` L1146-L1174; `read_series_documents` L1269-L1310; `_series_subtask_nodes` L1313-L1330; `_series_subtask_created_at` L1333-L1346; `_task_doc_node` L1367-L1456 | [snapshots.py](../src/agents_remember/observer/snapshots.py) |
| The task-document reader tests assert lifecycle `createdAt`, unbound docs, master docs, and archive exclusion. | `TaskDocumentsReaderTests` L3203-L3650 | [test_observer_projection.py](test_observer_projection.py) |
| The creation-order regression writes sibling leaf task docs and expects rows sorted oldest-first by leaf `createdAt`. | `test_read_series_documents_orders_subtasks_by_leaf_creation` L3529-L3587 | [test_observer_projection.py](test_observer_projection.py) |
| The series-token regression joins master rows to sibling leaf task docs and sums bound lifecycle token totals. | `test_series_token_total_sums_linked_leaf_lifecycles` L713-L786 | [test_observer_projection.py](test_observer_projection.py) |
| The fold + inferred layer + action availability under test. | `project_lifecycle` L78-L105; `_project_inferred` L454-L468; the action-availability block (`_lifecycle_actions` L474-L483, `enclosure_actions` L486-L487, `_integrate_action` L490-L504, `_cleanup_action` L507-L521) | [reducer.py](../src/agents_remember/observer/reducer.py) |
| The provider-node helper under test for CGC repo watcher expansion, GrepAI `targetRepos`, and aggregate fallback when target evidence is absent. | `workspace_provider_nodes` L16-L39; `_cgc_repo_provider_nodes` L83-L98; `_target_repo_provider_nodes` L139-L150; `_target_repo_ids` L174-L185 | [provider_nodes.py](../src/agents_remember/observer/provider_nodes.py) |
| The active-enclosure admission helper under test for strict provider groups and broader Engine Room groups. | `admitted_worktree_groups` L24-L45; `active_enclosure_worktree_groups` L48-L73 | [worktree_provider_admission.py](../src/agents_remember/observer/worktree_provider_admission.py) |
| The admission resilience (missing-log survives) + series-retention helpers under test. | `test_active_group_survives_a_pruned_lifecycle_log`, `SeriesRetentionTests` | [test_observer_projection.py](test_observer_projection.py) |
| The `series_retained_lifecycle_ids` / `_series_is_retired` / `_contract_finalized_at` derivation the L5 cases pin. | `series_retained_lifecycle_ids` | [worktree_provider_admission.py](../src/agents_remember/observer/worktree_provider_admission.py) |
| Snapshot readers accept active worktree groups so stale worktree provider/setup/engine facts are skipped before the reducer. | `read_providers` L185-L203 with the group filter in `_worktree_providers` L218-L278; `read_engine_process_facts` L630-L689; `read_setup_progress_nodes` L1032-L1066 | [snapshots.py](../src/agents_remember/observer/snapshots.py) |
| Actionable drift rows expose repo/branch ids, drift provenance detail, and `checkedAt` signal timestamps. | `test_drift_and_failed_setup_surface` L2157-L2190 | [test_observer_projection.py](test_observer_projection.py) |
| Targetless actionable-drift dismissal suppresses only the current snapshot occurrence. | `test_dismiss_suppresses_actionable_drift_until_newer_snapshot` L2331-L2370 | [test_observer_projection.py](test_observer_projection.py) |
| The log reader + atomic writer + orchestrator under test. | `read_lifecycle_logs` L112-L154; `write_projection` L157-L164 with `_atomic_write_json` L361-L365; `project_and_write` L214-L277 | [projection_store.py](../src/agents_remember/observer/projection_store.py) |
| Projection reads active admission sets once and caches repo surfaces on a short TTL. | `REPO_SURFACE_REFRESH_TTL_SECONDS` L64-L68; the single admission/surface read inside `project_and_write` L232; L247; `_gather_repo_surfaces_cached` L334-L345 with `_repo_surface_cache_key` L348-L358 | [projection_store.py](../src/agents_remember/observer/projection_store.py) |
| Task-29 tests cover admission, inactive runtime filters, repo-surface caching, and the engine-process active-group gate. | `WorktreeProviderAdmissionTests` L239-L347; `test_read_providers_ignores_unadmitted_worktree_stacks` L1289-L1315; `test_active_group_filter_skips_parked_progress` L2686-L2700; `test_repo_surface_cache_reuses_recent_repo_reads` L3100-L3121; `test_reader_skips_inactive_engine_process_groups_when_filtered` L4077-L4106 | [test_observer_projection.py](test_observer_projection.py) |
| The drift-snapshot producer exercised by the round-trip test. | `run_drift_summary` L24-L72; `_write_drift_snapshot` L108-L150 | [onboarding_drift_check/summary.py](../src/agents_remember/memory_quality/integrity/onboarding_drift_check/summary.py) |
| The shared drift-snapshot path/pruning helper used by fixtures and projection pruning coverage. | `drift_snapshot_path` L19-L22; `prune_orphaned_drift_snapshots` L36-L69 | [drift_snapshots.py](../src/agents_remember/observer/drift_snapshots.py) |
| The shared drift-snapshot dir/schema the fixtures use. | `DRIFT_SNAPSHOT_SCHEMA` L24; `drift_snapshot_dir` L37-L39 (the file is 39 lines) | [paths.py](../src/agents_remember/observer/paths.py) |
| The lifecycle-state vocabulary under test: the composed `State`, its two halves, the partition guard, the declaration reader, and the end-outcome coercion the terminality tests drive. | `vocabulary_names` L41-L56; `check_state_partition` L73-L98; `STATES` L133-L135; `LIVE_STATES` L136-L138; `TERMINAL_STATES` L139; `DEFAULT_END_OUTCOME` L143; `coerce_end_outcome` L149-L158; `LifecycleState.is_terminal` L188-L210 | [lifecycle_state.py](../src/agents_remember/observer/lifecycle_state.py) |
| The metrics buckets and the state→field naming rule the coverage suites hold to the vocabulary. | `ACTIVE_STATES` L227; `state_count_field` L230-L245; `state_count_fields` L248-L270; `STATE_COUNT_FIELDS` L273; `Metrics` L278-L304 | [projection.py](../src/agents_remember/observer/projection.py) |
| The event-kind table `TerminalityIsStructuralTests` reads to decide which states a running session can declare about itself, and the rollup that fills the buckets. | `_KIND_UPDATES` L418-L427; `_metrics` L524-L547 | [reducer.py](../src/agents_remember/observer/reducer.py) |
| The write side held to the same terminal set — `end` validates against `TERMINAL_STATES` and converts through `coerce_end_outcome`. | `AmbientLifecycle.end` | [ambient.py](../src/agents_remember/observer/ambient.py) |
| The TypeScript mirror of the naming rule, which is why Python moved off `str.capitalize`: the field names are derived type-level with `Capitalize<Camel<Tail>>`. | `stateCountField` | [projection.ts](../../dashboard/src/types/projection.ts) |
| The sibling suite that pins the structure of the ambient end signal's vocabulary, which this file pins the behaviour of. | `EndSignalVocabularyTests` | [test_observer_ambient.py](test_observer_ambient.py) |

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

## 260718-CHATS-L5I Current Delta

Projection tests now pin the shared per-tick parse/cache path and repository-surface refresh cadence, ensuring the performance change does not change projection truth.

This entry supersedes conflicting earlier coverage notes while retaining their history; source verification metadata is deliberately unchanged until the code commit.

## 260727-CHATS-IM-L2 Current Delta

The provider-reader patch target follows its new `projection_inputs` ownership. The test still
asserts the same projection output and uncached volatile-provider behavior.

## Update History

- 2026-08-01T14:20+02:00 — 260731-EFA-L5 curator: one assertion changed in this suite and every
  line citation in the card moved with it. **Coverage:**
  `SnapshotReaderTests::test_project_and_write_prunes_completed_lifecycle_attention_acknowledgement`
  (L1504-L1538) ended `assertFalse(dismissals.log_path().exists())`; it now asserts
  `dismissals.read() == []`, `log_path().is_file()` and `log_path().read_bytes() == b""`. The
  unlink it used to prove is the defect 260731-EFA-L5 removed (R5): `_replace` called
  `path.unlink(missing_ok=True)` on an empty kept set, so a concurrent dismisser holding an
  `"a"`-mode handle wrote into an inode with no remaining links and lost the record with no torn
  line and no exception — the mechanism behind the measured **31.45%** dismissal loss, the worst
  of the six stores. The replacement is strictly stronger: zero bytes read back proves the row
  physically left, where a missing file only proved a file was removed. Rewrote the
  `AttentionDismissalTests` paragraph accordingly and named the test. **Citation repairs — 16
  ranges.** The file grew 4238 → 4246 lines: the diff replaced 7 lines with 15 at L1527, so every
  self-citation at or below L1534 shifted by exactly +8 and each was re-verified against the
  symbol it names — `MetricsBucketVocabularyTests` L1617-L1722 → **L1625-L1730**;
  `StatePartitionTests` L1725-L1789 → **L1733-L1797** (its `LIVE`/`TERMINAL` class attributes
  L1736-L1737 → **L1745-L1746**); `TerminalityIsStructuralTests` L1792-L1909 → **L1800-L1917**;
  `StateVocabularyReaderTests` L1912-L1947 → **L1920-L1955**; `StateCountFieldTests` L1950-L2005 →
  **L1958-L2013**, and the section heading's span L1617-L2005 → **L1625-L2013**;
  `test_drift_and_failed_setup_surface` L2149-L2182 → **L2157-L2190**;
  `test_dismiss_suppresses_actionable_drift_until_newer_snapshot` L2323-L2362 → **L2331-L2370**;
  `test_active_group_filter_skips_parked_progress` L2678-L2692 → **L2686-L2700**;
  `test_repo_surface_cache_reuses_recent_repo_reads` L3092-L3113 → **L3100-L3121**;
  `TaskDocumentsReaderTests` L3195-L3642 → **L3203-L3650**;
  `test_read_series_documents_orders_subtasks_by_leaf_creation` L3521-L3579 → **L3529-L3587**;
  `test_reader_skips_inactive_engine_process_groups_when_filtered` L4069-L4098 → **L4077-L4106**.
  `test_series_token_total_sums_linked_leaf_lifecycles` L713-L786,
  `WorktreeProviderAdmissionTests` L239-L347,
  `test_read_providers_ignores_unadmitted_worktree_stacks` L1289-L1315, the `snapshots` patch-seam
  import L43 and the `typing.Literal` import L23 all sit above the hunk and were re-verified
  unmoved. **One pre-existing defect corrected, not a shift:** the body cited
  `test_a_wedged_git_log_degrades_to_hash_only_rows_instead_of_failing_the_tick` at L2474-L2504,
  a range that has held neither its start nor its end since the L4 vocabulary insertion — the test
  is at **L2895-L2921** and L2474 lands inside an unrelated attention-queue case. The L3 entry
  below recorded the range correctly for its own tree; the L4 citation pass did not carry it
  forward. **Cross-file:** every `snapshots.py` row moved by −6, because this leaf shortened that
  module (1530 → 1524 lines: −6 at L123, −6 at L524, +6 at L606). `read_providers` L191-L209 →
  **L185-L203**, `_worktree_providers` L224-L284 → **L218-L278**, `read_engine_process_facts`
  L636-L695 → **L630-L689**, `read_setup_progress_nodes` L1038-L1072 → **L1032-L1066**,
  `read_task_documents` L1152-L1180 → **L1146-L1174**, `read_series_documents` L1275-L1316 →
  **L1269-L1310**, `_series_subtask_nodes` L1319-L1336 → **L1313-L1330**,
  `_series_subtask_created_at` L1339-L1352 → **L1333-L1346**, `_task_doc_node` L1373-L1462 →
  **L1367-L1456**. The Repo-Internal table's 3-column header is intact and no row changed width.
  No test was added, removed or renamed, and no other assertion changed. Verification metadata
  pinned until closeout stamps the L5 commit.

- 2026-08-01T10:40+02:00 — 260731-EFA-L4 curator (citation pass): re-verified the eight
  `projection.py` pointers after a worker inserted ten lines above them; every one moved by exactly
  +10 and none needed reshaping. `TaskDocNode` L575-L621 → L585-L631 (`id` L596, `lifecycleId` L597,
  `createdAt` L609), `SeriesSubTaskNode` L624-L639 → L634-L649 (`createdAt` L649, the class's last
  line), `SeriesNode` L652-L678 → L662-L688 (`objective` L680); `ACTIVE_STATES` L217 → L227,
  `state_count_field` L220-L235 → L230-L245, `state_count_fields` L238-L260 → L248-L270,
  `STATE_COUNT_FIELDS` L263 → L273, `Metrics` L268-L294 → L278-L304. No body text changed.
- 2026-08-01T09:35+02:00 — 260731-EFA-L4 curator: this suite gained **five vocabulary/partition
  classes** and the card gained a section for them, plus three corrections and 12 citation repairs.
  **New coverage (L1617-L2005, between `TokenSeriesTests` and `StalenessHistogramTests`):**
  `MetricsBucketVocabularyTests` (L1617-L1722) derives the live state set as `STATES` minus
  `TERMINAL_STATES` **rather than** reading `projection.ACTIVE_STATES`, so the measurement is not
  taken with the instrument it is checking; it holds both directions (every live state has a
  bucket, every `*Count` bucket except `lifecycleCount` is a live state), drives one real lifecycle
  per live state through `project_workspace` so a declared-but-undrivable state is reported rather
  than skipped, and pins the reported symptom — `awaiting-developer` was in `lifecycleCount` and
  `totalTokens` and in no bucket. `StatePartitionTests` (L1725-L1789) holds
  `check_state_partition`'s three refusals against **synthetic** `Literal` vocabularies so the
  guard is exercised without the shipped declaration being wrong.
  `TerminalityIsStructuralTests` (L1792-L1909) gives terminality an observable definition and
  checks it against the fold in both directions (`coerce_end_outcome`, `_KIND_UPDATES`), and holds
  the write side (`AmbientLifecycle.end`) to the same terminal set. `StateVocabularyReaderTests`
  (L1912-L1947) pins `vocabulary_names` across the flat, composed and union `Literal` forms — the
  union form is where bare `get_args` returns `Literal` objects and the first `.split` kills the
  whole `agents_remember.observer` import. `StateCountFieldTests` (L1950-L2005) pins the
  state→field rule against the TypeScript mirror's `Capitalize<Camel<Tail>>` and refuses two states
  that would share a bucket — the reviewer's `awaiting-Developer`/`awaiting-developer` case
  produced a merged count and a **green** vocabulary suite, because the coverage tests compare
  per-state values that both resolve to the merged field. **Corrections:** (1) the
  `## Governing Overview` line asserted "there is no route-local `mcp/tests/overview.md`" — that
  file exists in this memory tree, so the section and the `governingOverview` cell now point at it
  (`overview.md`) instead of at `../overview.md`; (2) the Conventions note cited the
  `from agents_remember.observer import snapshots` patch-seam import at L42, now **L43** (the
  `typing.Literal` import at L23 pushed it down); (3) recorded that the `EngineProcessTests`
  contract fixtures now ask for `workflow_kind="light-task"` — the bare `"light"` is no longer a
  `WorkflowKind` member. Added a Conventions paragraph for the two local conventions the new suites
  introduce (derive with a different instrument; drive guards against synthetic vocabularies).
  **Citation repairs — 12 rows.** The file grew 3825 → 4238 lines: +22 in the import block and
  +391 at L1614, so self-citations shifted by +22 below L1614 and by +413 above it, and every one
  was re-verified against the symbol it names. `TaskDocumentsReaderTests` L2782-L3043 →
  **L3195-L3642** (its END was already wrong before this leaf: at `abc7cbcc` the class ran to
  L3229, not L3043); `test_repo_surface_cache_reuses_recent_repo_reads` L2679-L2720 →
  **L3092-L3113** (END likewise wrong — L2700 at the base);
  `test_read_series_documents_orders_subtasks_by_leaf_creation` L3108-L3166 → **L3521-L3579**;
  `test_series_token_total_sums_linked_leaf_lifecycles` L691-L764 → **L713-L786**;
  `test_drift_and_failed_setup_surface` L1736-L1769 → **L2149-L2182**;
  `test_dismiss_suppresses_actionable_drift_until_newer_snapshot` L1910-L1949 → **L2323-L2362**;
  and the task-29 set L217-L325; L1267-L1293; L2265-L2279; L2679-L2720; L3656-L3685 →
  **L239-L347; L1289-L1315; L2678-L2692; L3092-L3113; L4069-L4098**. Cross-file rows moved because
  their modules changed this leaf: `projection.py` `TaskDocNode`/`SeriesSubTaskNode`/`SeriesNode`
  L487/L536/L564 → **L575-L621; L624-L639; L652-L678**; `snapshots.py` reader row
  L1149/L1272/L1316/L1336/L1370 → **L1152-L1180; L1275-L1316; L1319-L1336; L1339-L1352;
  L1373-L1462** and its group-filter row's `read_engine_process_facts` L636-L693 → **L636-L695**
  and `read_setup_progress_nodes` L1035-L1069 → **L1038-L1072** (`read_providers` L191-L209 and
  `_worktree_providers` L224-L284 re-verified unmoved); `reducer.py` `project_lifecycle` L71-L98 →
  **L78-L105**, `_project_inferred` L446-L460 → **L454-L468**, and the action-availability block
  L466/L478/L482/L499 → **L474-L483; L486-L487; L490-L504; L507-L521**; `summary.py`
  `run_drift_summary` L23-L71 → **L24-L72** and `_write_drift_snapshot` L107-L149 → **L108-L150**.
  `provider_nodes.py`, `projection_store.py`, `drift_snapshots.py`, `paths.py` and
  `worktree_provider_admission.py` were re-verified and their ranges still contain their named
  symbols. Added seven rows for the new coverage (`lifecycle_state.py`, `projection.py`'s bucket
  machinery, `reducer.py`'s `_KIND_UPDATES`/`_metrics`, `ambient.py`'s `end`, the TypeScript
  mirror, and the sibling `test_observer_ambient.py`). The Repo-Internal table's 3-column header
  from the L3 repair is intact and every new row carries three cells. Verification metadata pinned
  until closeout stamps the L4 commit.

- 2026-07-31T21:55+02:00 — 260731-EFA-L3 curator: recorded the one test this leaf added and
  repaired every line range in the card. **New coverage:**
  `LedgerCommitMetaTests::test_a_wedged_git_log_degrades_to_hash_only_rows_instead_of_failing_the_tick`
  (L2474-L2504), plus the module-object import `from agents_remember.observer import snapshots`
  (L42) that exists only to give it a patch seam. It is the sole case in the suite that patches git
  instead of running it: `mock.patch.object(snapshots, "run_git", side_effect=
  subprocess.TimeoutExpired(...))` proves that when `snapshots._git_commit_meta` moved onto a runner
  with a timeout, `TimeoutExpired` — a `SubprocessError`, which is **not** an `OSError` — no longer
  escapes to fail the projection tick. Both entry points (`_ledger_window` and `read_ledger`) are
  driven inside one patch, because each reaches `_git_commit_meta` by its own path. Added the
  paragraph under Tier 2 and a Conventions note for the patch seam. **Citation repairs — 17 rows.**
  The file grew 3796 → 3825 lines (+1 at the import, +28 at the new test), so every self-citation
  past L42 shifted and every one past L2474 shifted again: `TaskDocumentsReaderTests` L2753-L3014 →
  L2782-L3043; `test_read_series_documents_orders_subtasks_by_leaf_creation` L3079-L3137 →
  L3108-L3166; `test_series_token_total_sums_linked_leaf_lifecycles` L690-L763 → L691-L764;
  `test_drift_and_failed_setup_surface` L1735-L1768 → L1736-L1769;
  `test_dismiss_suppresses_actionable_drift_until_newer_snapshot` L1909-L1948 → L1910-L1949; and the
  task-29 set L216-L324; L1266-L1292; L2264-L2278; L2650-L2691; L3627-L3656 → L217-L325;
  L1267-L1293; L2265-L2279; L2679-L2720; L3656-L3685. Ranges into other files were stale from
  earlier restructurings and are now cited per symbol rather than as bare spans: `projection.py`
  L412-L507 held none of `TaskDocNode` (L487), `SeriesSubTaskNode` (L536) or `SeriesNode` (L564);
  `snapshots.py` L584-L736; L757-L783 held none of `read_task_documents` (L1149),
  `read_series_documents` (L1272), `_series_subtask_nodes` (L1316) or `_task_doc_node` (L1370), and
  its group-filter row L112-L203; L496-L535; L778-L805 held none of `read_providers` (L191),
  `read_engine_process_facts` (L636) or `read_setup_progress_nodes` (L1035); `reducer.py` L1-L92
  held `project_lifecycle` (L71) but neither `_project_inferred` (L446) nor the action-availability
  block (L466-L513); `provider_nodes.py` L1-L92 held `_cgc_repo_provider_nodes` (L83) but not
  `_target_repo_provider_nodes` (L139) or `_target_repo_ids` (L174); `projection_store.py` L1-L90
  held none of `read_lifecycle_logs` (L112), `write_projection` (L157), `project_and_write` (L214)
  or `_atomic_write_json` (L361), and its cache row L151-L180; L217-L240 missed
  `_gather_repo_surfaces_cached` (L334) and `REPO_SURFACE_REFRESH_TTL_SECONDS` (L68);
  `summary.py` L1-L88 missed `_write_drift_snapshot` (L107); and `paths.py` L1-L47 ran eight lines
  past a 39-line file. `drift_snapshots.py` and `worktree_provider_admission.py` did contain their
  named symbols and were narrowed to exact definition ranges rather than corrected. Two rows carry
  no line range by design (`test_active_group_survives_a_pruned_lifecycle_log` / `SeriesRetentionTests`
  and `series_retained_lifecycle_ids`) and were left naming their symbols. The Repo-Internal
  References header was `| Finding | Source Path |` while all 19 rows carried a third `Citations`
  cell — the same defect found in `snapshots.py.md` — so **none** of these ranges rendered at all;
  header and separator widened to three columns, no row content moved. No test was removed or
  renamed and no existing assertion changed. Verification metadata pinned until closeout stamps the
  L3 commit.

- 2026-07-31T16:50+02:00 — 260731-EFA-L2 curator, code-quality hardening sweep. This suite absorbed
  more parameter-object churn than any other in the leaf. `project_workspace` now takes
  `structure=WorkspaceStructure(...)` and `given=AnalyticalInputs(...)` in place of its
  `enclosures`/`providers`/`active_worktree_groups`/`gates`/`drift_snapshots`/`setup_progress`/
  `task_documents`/`series`/`sidecar_staleness`/`attention_dismissals`/`engine_process_facts`/
  `engine_start_progress` keywords; `build_analytics` and `build_attention_queue` take
  `AnalyticalInputs` too; `create_gate` takes `anchor=GateAnchor(...)` and `decide_gate` a
  `GateVerdict`; `default_contract` takes `ContractTask`/`LeafIdentity`/`RepoBranchPlan`; and
  `write_start_progress` takes `StartingEnclosure` plus `StartBeat`. Locally, the `_event` fixture
  now takes `by=<Attribution>` and `enclosure=EnclosureRef(path, repo_id)` behind four new named
  constants (`DECLARED_BY_MODEL`, `OBSERVED_BY_MODEL`, `OBSERVED_BY_SYSTEM`,
  `INFERRED_BY_SYSTEM`). Corrected the task-33 sentence, which claimed `active_worktree_groups`
  was a `project_workspace` kwarg that defaults when omitted — it is now a `WorkspaceStructure`
  field — and rewrote the Conventions section to record the fixture provenance constants and the
  parameter-object call shapes. Also repaired every self-referencing line range in
  Repo-Internal References against the current file: task-document reader tests L2753-L3014,
  creation-order regression L3079-L3137, series-token regression L690-L763, actionable-drift rows
  L1735-L1768, targetless dismissal L1909-L1948, and the task-29 set
  L216-L324; L1266-L1292; L2264-L2278; L2650-L2691; L3627-L3656. No test was added, removed, or
  renamed, and no assertion changed value.

- 2026-07-30T12:51+02:00 — 260727-CHATS-IM-L2 curator: updated the provider-reader
  patch seam to its new `projection_inputs` owner while retaining the existing projection-output
  assertion. Verification metadata remains pinned until closeout.

- 2026-07-24T13:18:47Z — 260718-CHATS-L5I curator: refreshed the regression-coverage record for the current backend/shared behavior and preserved the pre-commit verification stamp.
- 2026-07-12T17:30+02:00 — 260712-TRH-L7: projection tests cover the new network-free landing snapshot integration while preserving existing observer projection contracts.

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
