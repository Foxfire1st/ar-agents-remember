# test_serving.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_serving.py`                      |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-09-06T21:45:53+00:00 |
| lastVerifiedCommitHash | `d36109038b3f2b500c138f9dc1ea9c9f9a247489`|
| lastVerifiedCommitDate | 2026-09-06T22:21:49+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Tests overview](overview.md)

## Purpose

Protects two dashboard-serving behaviors: a subscription cannot lose a projection interleaved with its initial snapshot, and HTTP ETag revalidation returns 304 until content changes. The broad historical SSE, simulation, actions and CLI inventory was removed; this card makes no current coverage claim for those paths.

## Code Commentary

### Logic

The current evidence boundary is the source-listed behavior below. Earlier coverage claims in
history describe prior populations and must not be used to recreate removed tests or claim they
still run. The retained behavior and its fixture limits, described above, govern this card.

### Conventions

The table lists retained test definitions, not collected parametrized or subtest counts.
Inspect the cited setup and collaborators before treating a focused result as end-to-end evidence.

### Invariants And Boundaries

Preserve exact refusal, identity, and cleanup assertions rather than adding overlapping helper
cases. Coverage percentages are diagnostic and production CRAP 20 prompts review; neither implies
an obligation to restore removed cases. Full suites and whole-candidate review remain master-end
work. This source inspection does not claim a newly executed test or acceptance result.

### Todos

No additional implementation scope is opened by this memory reconciliation.

## Docs References

The repository has no configured Domain Documentation source. These claims concern its own test
fixtures and assertions, so the exact retained source is the direct evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain claim is required. | N/A | N/A |

## Repo-Internal References

Each current definition below can be inspected in the exact source file. Historical references
to removed methods are superseded by this current inventory.

| Finding | Anchor | Source |
| --- | --- | --- |
| Snapshot subscription cannot lose an interleaved projection | `test_snapshot_subscription_cannot_lose_an_interleaved_projection` | mcp/tests/test_serving.py:103-123 |
| Etag 304 cycle then new etag on content change | `test_etag_304_cycle_then_new_etag_on_content_change` | mcp/tests/test_serving.py:165-194 |

## Cross-Repo References

This card establishes test behavior, not a separate cross-repository protocol or live installation.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external evidence is needed for these assertions. | N/A | N/A |

## Update History

- 2026-09-06T21:45:53+00:00 — Reconciled the retained IAS test/helper population and exact citation ranges, preserving prior history and verification provenance; no tests or review were run.


- 2026-09-05T22:25+00:00 — L30 incoming-reference review: projected the retained source-backed claim to its current owner extent; preserved this unchanged source file's genuine verification hash/date.

- 2026-08-28T06:40+02:00 — No content impact: removed the unused `FIXTURE_DIR` constant; serving
  behavior and the surviving fixture owners documented above are unchanged.
- 2026-08-12T21:39+02:00 — L23 curator follow-up: documented the complementary drain-failure forcing case: a blocked `_tick_sync` raises after cancellation, the late failure is logged, and `CancelledError` remains public. The owner reports the drain-success, drain-failure, and crashed-watcher cases green 3/3. Verification remains closeout-owned.
- 2026-08-12T20:10+02:00 — L23 curator: documented drain-before-cancellation coverage for projector threads; verification remains closeout-owned.
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-08T22:10+02:00 — 260713-TES-L1 completion round 2 (curator): No content impact: the supervisor -> agent-notifier rename does not change the behavior this sidecar documents; reviewed current against the changed source. Verification metadata pinned until closeout stamps the 260713-TES-L1 commit.
- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: this test module was split in place into a family under 1,200 lines (L7-R5); the card remains the family entry point and the name set was reconciled item for item. Verification metadata stays pinned until closeout stamps the 260731-EFA-L7 commit.
- 2026-08-04T13:25:51+02:00 — 260731-EFA-L6 S18-B01 same-reviewer semantic-binding repair: bound the build probes to their complete run_git call bodies under the adversarial verdict, then the exact scoped fixer/check passed.

- 2026-08-02T17:12:10+02:00 — W1-B04 curator: applied 20 citation updates (19 repairs, 1 normalization; 4 prose citations); scoped recheck clean (0 findings).

- 2026-08-01T14:20+02:00 — 260731-EFA-L5 curator: one assertion changed and every self-citation
  below it moved. **Coverage:**
  cit:([`test_attention_store_upserts_and_prunes_lifecycle_rows`], mcp/tests/test_serving_actions.py:355-388) ended
  `assertFalse(store.log_path().exists())` and now asserts `store.read() == []`,
  `log_path().is_file()` and `log_path().read_bytes() == b""`. That unlink is the defect
  260731-EFA-L5 removed (R5): `AttentionDismissalStore._replace` called
  `path.unlink(missing_ok=True)` on an empty kept set, and because `dismiss` is a whole-file
  read-modify-write reached from this app's own HTTP dismiss route, a concurrent dismisser holding
  a handle across the unlink wrote into an inode with no remaining links — the record disappeared
  with the file, with no error and no torn line. The claim is not weakened: emptiness through the
  reader plus zero bytes on disk proves the row physically left, where absence only proved a file
  was removed. Added a paragraph under the `ActionDismissTests` description, three
  Repo-Internal rows (the store's `dismiss`/`prune_lifecycles`/`_replace`, the contract's
  `rewrite_lines` that makes "emptied" true for every control-plane log at once,
  and the rewritten test itself). **Citation repairs — 5 ranges.** The file grew 2418 → 2428
  lines, all of it at L1432 where 7 lines became 17, so every self-citation at or below L1442
  shifted by exactly +10 and each was re-verified against the symbol it names: the actionable-drift
  dismiss row L1437-L1447; L1493-L1505 → **L1447-L1457; L1503-L1515** (its first range, L1387-L1410,
  sits above the hunk and was re-verified unmoved); Task 34 retention L1927-L1995; L2022-L2052 →
  **L1937-L2005; L2032-L2062**; raw stream L2063-L2076; L2113-L2142 → **L2073-L2086; L2123-L2152**.
  The MX-FIX-1 trio cit:([`StreamEventsTests`], mcp/tests/test_serving.py:379-477), both dirty-probe rows cit:([`BuildInfoTests`], mcp/tests/test_serving_cli.py:36-181) and the
  `_build_wire` helper cit:([`_build_wire`], mcp/tests/test_serving.py:84-92) are above the hunk and were re-verified unmoved. No test was
  added, removed or renamed. Verification metadata pinned until closeout stamps the L5 commit.

- 2026-08-01T09:15+02:00 — 260731-EFA-L4 curator: `ServingBuild.payload()` now returns the declared
  `ServingBuildPayload` model instead of a dict, so every assertion that used to index `payload()`
  goes through the new module-level helper cit:([`_build_wire`], mcp/tests/test_serving.py:84-92) —
  `build.payload().model_dump(mode="json", exclude_none=True)`, which is the stamp exactly as the
  state body carries it and the point at which the honest-unknown rule (absent, never null, never a
  fabricated "clean") is applied. Seven call sites moved: the six in `BuildInfoTests` and
  `StreamEventsTests.test_snapshot_carries_the_serving_build_stamp`. Rewrote the `BuildInfoTests`
  passage, which described `payload()` as if it were still the wire dict. No assertion changed
  value and no test was added, removed or renamed. **Citation repairs — 7 rows.** The file grew
  2407 → 2418 lines, all of it at L128-L138, so every self-citation shifted by +11 and was
  re-verified against the symbol it names: MX-FIX-1 trio L430-L492 → **L441-L503**
  (`test_snapshot_subscription_cannot_lose_an_interleaved_projection` L441 …
  `test_cancelled_waiting_stream_releases_its_subscription` L503); dirty probe
  L1034-L1058; L1060-L1079 → **L1045-L1069; L1071-L1090**
  (`test_dirty_probe_is_tri_state_and_fails_open`,
  `test_status_failure_does_not_assert_a_pristine_tree`); actionable-drift dismiss
  L1376-L1399; L1426-L1436; L1482-L1494 → **L1387-L1410; L1437-L1447; L1493-L1505**; Task 34
  retention L1916-L1984; L2011-L2041 → **L1927-L1995; L2022-L2052** (still skipping the separately
  cited protected-log test, now at L1997-L2020); raw stream ready/heartbeat
  L2052-L2065; L2102-L2131 → **L2063-L2076; L2113-L2142** (`test_streams_backlog`,
  `test_stream_does_not_emit_heartbeats`). Two cross-file rows moved because their modules changed
  this leaf: `build_info.py` L36-L39; L67-L94 → **L40; L91-L118** (`_PROBE_TIMEOUT_SECONDS` at L40,
  `_git_short_head` L91-L101, `_git_worktree_dirty` L104-L118 — the old ranges held neither probe),
  and `app.py` L181-L203; L702-L707 → **`stream_events` L300-L330**, one range that now contains
  all four claims the row makes (one subscription via `contextlib.aclosing` L319, the snapshot
  decoration `served_state_tail` L328-L329, and the SSE framing L330). `projector.py`
  L135-L178; L207-L269 was re-verified unmoved — that module is untouched by this leaf.
  Verification metadata pinned until closeout stamps the L4 commit.

- 2026-07-31T20:55+02:00 — 260731-EFA-L3 curator: `BuildInfoTests` changed seam. Both dirty-probe
  tests now patch `agents_remember.serving.build_info.run_git` instead of
  `…build_info.subprocess.run`, because the probes call the package's one git runner rather than
  spawning git themselves; `test_status_failure_does_not_assert_a_pristine_tree`'s `fake_run` was
  re-signed to `(_repo, arguments, **kwargs)` and now branches on `arguments[:1] == ["rev-parse"]`.
  Recorded that, and the tri-state/fail-open cases the card had never named. The assertions
  themselves are unchanged. The file grew from 2404 to 2407 lines, all of it at/after L1036, so the
  four self-citations below L1036 shifted by +3 and were re-verified against the symbols they
  claim: actionable-drift dismiss L1373-L1396; L1423-L1433; L1479-L1491 →
  L1376-L1399; L1426-L1436; L1482-L1494
  (`test_evaluate_action_allows_actionable_drift_without_lifecycle`,
  `test_attention_store_keeps_actionable_drift_current_acknowledgements`,
  `test_api_action_dismiss_records_actionable_drift_acknowledgement`); Task 34
  retention/heartbeat/limit L1913-L1981; L2008-L2038 → L1916-L1984; L2011-L2041
  (`test_read_new_events_skips_heartbeats` … `test_initial_offsets_bound_active_replay_to_recent_window`,
  still skipping the separately cited protected-log test, now at L1986-L2009); raw stream
  ready/heartbeat L2049-L2062; L2099-L2128 → L2052-L2065; L2102-L2131 (`test_streams_backlog`,
  `test_stream_does_not_emit_heartbeats`). `L430-L492` (the MX-FIX-1 trio) sits above the change and
  was re-verified unmoved. Verification metadata pinned until closeout stamps the L3 commit.

- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 4 self-referencing line citations against the
  now-2404-line `test_serving.py`. MX-FIX-1 regressions → L430-L492 (`StreamEventsTests`: handoff
  mutation, failed-prime recovery whose duplicate `_publish_projection(recovered)` proves
  identical-state silence before the later delta, cancellation cleanup), was L395-L457. Task 34
  retention/heartbeat/limit → L1913-L1981; L2008-L2038 in `RawEventTests` (the split skips the
  separately cited protected-log test at L1983-L2006), was L994-L1074. Raw stream ready/heartbeat →
  L2049-L2062; L2099-L2128 in `StreamRawEventsTests`, was L1085-L1124. Actionable-drift dismiss →
  L1373-L1396; L1423-L1433; L1479-L1491 in `ActionDismissTests`, was L558-L616; L662-L674.
- 2026-07-31T15:32+02:00 — 260731-EFA-L2 curator: recorded the arms this leaf added; the rest of this card was re-read against the file and remains true. Call sites in this module now build parameter objects (see the route overview) — what the suite proves is unchanged. Verification metadata pinned until closeout stamps the code commit.

- 2026-07-31T15:32+02:00 — 260731-EFA-L2 curator: corrected the `watch_changes=False` claim. That
  keyword no longer exists — `create_app` now takes `cadence: ProjectionCadence`,
  `live_inputs: LiveProjectionInputs` and `collaborators: ServingCollaborators`, and `Projector`
  takes `cadence` plus `refreshers: ProjectionRefreshers`. What the ETag suite proves is unchanged;
  only how it configures the app is. Verification metadata pinned until closeout stamps the code
  commit.

- 2026-07-31T04:28+02:00 — 260731-EFA-L1: the cockpit bundle left version control, so three
  assertions that silently depended on a committed build were rewritten — `/` is served from a
  patched stand-in bundle instead of the repository's own, `dashboardBuild` is asserted
  present-or-omitted instead of indexed, and `StaticTests` skips rather than failing in a checkout
  with no build. Added `test_root_diagnoses_a_missing_bundle_instead_of_a_bare_404` (503 + remedy +
  `no-store`, API unaffected). The deterministic version of both static states lives in the new
  `test_static.py`. Verification metadata pinned to the pre-leaf source authority until closeout
  stamps the code commit.

- 2026-07-30T12:51+02:00 — 260727-CHATS-IM-L2 curator: updated four explicit
  `project_and_write` test doubles for the new `input_state` and `refresh` keyword-only seam. This
  is a test-interface repair only; ETag, body-cache, gzip, and SSE expectations remain unchanged.
  Verification metadata remains pinned until closeout.

- 2026-07-24T13:18:47Z — 260718-CHATS-L5I curator: refreshed the regression-coverage record for the current backend/shared behavior and preserved the pre-commit verification stamp.

- 2026-07-18T14:16+02:00 — 260715-FEUI-MX-FIX-1: documented deterministic coverage for the
  atomic snapshot/subscription handoff, failed-prime first-recovery snapshot plus build identity,
  identical-state non-duplication, ordinary later delta, and close/cancellation queue cleanup.
  Verification metadata remains pinned until closeout stamps the candidate commit.
- 2026-07-18T12:43+02:00 — FEUI-L9R: captured HTML/build-identity assertions and the complete raw
  event cursor/invalid-record/non-object stream matrix; verification metadata remains pinned pending
  candidate closeout.
- 2026-07-12T20:24+02:00 — 260712-PTS-L3: `StateEtagTests` builds its app with
  `watch_changes=False` (a mocked `project_and_write` is watcher-invisible, so the tick loop must
  stay interval-paced), and the CLI fixtures/assertions gained the new `heartbeat: None` key
  (`CliTests` pins the parser default). The change-driven pacing behaviour itself is covered in
  `test_change_watcher.py`, not here. Verification metadata pinned until closeout stamps the
  PTS-L3 commit.
- 2026-07-12T17:30+02:00 — 260712-TRH-L7: serving tests cover Projector refresher lifecycle and real app-lifespan shutdown after a dead refresher.

- 2026-07-07T10:30+02:00 — L15 adversarial-review follow-up (L15R-1): volatile-vs-content reflection guard added for *Seconds projection fields. Verification metadata pinned until closeout stamps the L15 commit.

- 2026-07-07T05:14+02:00 — 260703-L15: `DeltaTests` gained the four change-gate cases
  (volatile-only lifecycle/analytics emit nothing; real change carries fresh ages; precomputed
  stable-state parity), `StreamEventsTests` the snapshot `servingBuild` case, and NEW
  `StateEtagTests` (the 200→ETag→304 cycle, volatile-only stays 304, real change mints a new
  tag, `servingBuild` on the body, `_if_none_match_matches` table) + `BuildInfoTests`
  (checkout hash, off-checkout None-omitted, camelCase payload). `import httpx`/`import time` and
  the `TaskDocNode` import joined the header.
  Verification metadata pinned until closeout stamps the L15 commit.
- 2026-07-03T11:45+02:00 — 260703 L2: both CLI Namespace fixtures gained the daemon-era keys
  (`daemon`/`status`/`stop`/`no_access_log`, all off) so `dashboard.run()`'s new reads stay
  exercised; no assertion changes. Verification metadata pinned until closeout stamps the code
  commit.
- 2026-06-30T00:00:00+02:00 — L5 (260628_operations-integration): added `test_protected_lifecycle_log_survives_inactivity`
  to `RawEventTests` — a dormant enclosure-backed log in `protected_lifecycle_ids` is exempt from the
  inactivity prune, and is pruned only once protection is dropped (proving the dormancy precondition and
  the live-master-series exemption). Verification metadata pinned until closeout stamps the L5 code commit.
- 2026-06-28T13:54+02:00 — Task 34: extended `RawEventTests` for the inactivity-retention rework —
  `test_read_new_events_skips_heartbeats`, `test_read_new_events_limit_bounds_batch`,
  `test_dormant_promoted_lifecycle_pruned_without_terminal_event` (a recent heartbeat does NOT save a
  dormant lifecycle), `test_dormant_fleeting_lifecycle_pruned_without_terminal_event`,
  `test_active_lifecycle_with_recent_activity_not_pruned`,
  `test_initial_offsets_bound_active_replay_to_recent_window`, plus
  `StreamRawEventsTests.test_stream_does_not_emit_heartbeats`; refreshed the `ready`/coverage citations.
  Verification metadata pinned until closeout stamps the task-34 code commit.
- 2026-06-28T07:32+02:00 — Task 29 S7 follow-up: added/recorded raw stream `ready` coverage and
  actionable-drift dismiss coverage for targetless evaluation, acknowledgement retention, and API writes.
  Verification metadata pinned until closeout stamps the task-29 code commit.
- 2026-06-28T07:30+02:00 — Task 33: the `_projection` helper gained an `active_worktree_groups` param, and
  `DeltaTests` gained coverage for the new `activeWorktreeGroups` whole-value delta (changed emits the
  wrapped marker; unchanged emits nothing). Verification metadata pinned until closeout stamps the code
  commit.
- 2026-06-28T05:38+02:00 — Task 29: added raw Event River retention coverage for
  cursorless fresh-connect offsets, one-hour terminal lifecycle pruning, workspace age-window replay,
  malformed cursor fallback to retained offsets, and no hard event-count cap across parallel active
  lifecycle logs. Verification metadata pinned until closeout stamps the task-29 code commit.
- 2026-06-28T03:52+02:00 — Task 28 S5.2 after source sync: added `ActionDismissTests`
  coverage for lifecycle-scoped dismiss evaluation, compact store upsert/prune, legacy duplicate
  compaction, lifecycle acknowledgement writes, and gate-open consumption by gate deletion. Verification
  metadata pinned until closeout stamps the task-28 code commit.
- 2026-06-27T23:08+02:00 — Task 31 provider-state honesty: added projector coverage that `provider_refresher.maybe_refresh` runs during `prime()` before projection. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-27T18:43+02:00 — Task 26 `--reload`: made `CliRunTests._args` a `**overrides` builder and seeded `reload: False` in both the `CliRunTests` and `CliSimTests` Namespace fixtures (stale fixtures lacked the attr `dashboard.run()` now reads); added `import os` and three `CliRunTests` tests — `test_run_reload_launches_the_dev_factory` (uvicorn gets the `agents_remember.cli.dashboard:_dev_app` import-string factory with `factory=True`/`reload=True`, `create_app` not called), `test_run_reload_with_sim_is_rejected` (reload+sim → exit 1), and `test_dev_app_factory_builds_from_env` (`_dev_app` reads the dev config/interval env and threads them through `load_config`/`create_app`).
- 2026-06-25T14:02+02:00 — Task 24 reopened: added coverage for gate-id-only cancel evaluation and `/api/actions/cancel` deleting a workspace-shaped gate by id.
- 2026-06-25T13:20+02:00 — Task 23/24: added coverage for `POST /api/operator-inbox/{entry_id}/dismiss`, the dashboard delete path for stale pickup warnings.
- 2026-06-25T07:17+02:00 — Task 19: extended serving tests for targeted gate ids, rejection notes, missing-reason reject validation, stale-gate 409 responses, and persisted `decisionNote`. Verification metadata pinned until closeout stamps the task-19 code commit.
- 2026-06-23T15:05+02:00 — Task 10 dashboard fallback: added `ActionGateTests` coverage for `POST /api/operator-inbox`, including persisted pending entry attribution and the 400 no-address path. Verification metadata pinned until closeout stamps the task-10 code commit.
- 2026-06-18T12:10+02:00 — Task 6 slice 6b: added `ActionGateTests` (the pure `evaluate_action` gate-decision intent + the `POST /api/actions/approve` developer-attributed write via `gate_decide_for_lifecycle`, incl. the 409 no-open-gate path). Verification metadata pinned until closeout stamps the 6b code commit.
- 2026-06-15T19:35 — slice 5e: slice 5e: projection version assertions updated 1->2.
- 2026-06-14T23:30+02:00 — Slice 05 (5c): `StreamRawEventsTests.test_streams_backlog` now asserts the raw channel is single-encoded (the SSE `data` is the parsed object, matching the events.py fix). Verification metadata pinned until closeout stamps the 5c code commit.
- 2026-06-14T15:52+02:00 — Updated for slice 5a: `AppTests` now asserts `/` serves the shipped React bundle (`#root` mount + app title) rather than the slice-04 placeholder text, and `StaticTests` asserts the bundle's `assets/` dir; the two tests were renamed (`test_root_serves_dashboard_bundle`, `test_static_dir_resolves_to_shipped_bundle`). Verification metadata pinned until closeout stamps the 5a code commit.
- 2026-06-14T11:30+02:00 — Updated for slice 04 commit 4b: added `RawEventTests` /
  `StreamRawEventsTests` (raw channel), `SimFixtureTests` / `SimReplayTests` (sim load + replay +
  determinism), `ActionTests` / `ActionEndpointTests` (POST skeleton), and `CliSimTests`; noted
  the `mcp/tests/fixtures/sim` fixture. Verification metadata pinned until closeout stamps the 4b
  code commit.
- 2026-06-14T11:30+02:00 — Created for slice 04 commit 4a: tests for the serving layer (delta,
  projector, stream_events, app endpoints, static, CLI). Verification metadata pinned until
  closeout stamps the 4a code commit.
