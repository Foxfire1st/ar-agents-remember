# test_serving.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_serving.py`                      |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-08-01T14:20+02:00 |
| lastVerifiedCommitHash | `a714114ef94eedb8042fb4caa38d9469f4767dd6`       |
| lastVerifiedCommitDate | 2026-08-01T18:06:36+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

`test_serving.py` covers the dashboard serving layer (slice 04, commits 4a + 4b): the pure
per-entity projection diff, the shared projector's prime/current/subscribe fan-out, the SSE
event sequence (atomic current snapshot, failed-prime recovery snapshot, then deltas), explicit
subscriber cleanup, the FastAPI app endpoints via `TestClient`, the raw event
channel's byte-offset tail + cursor resume + heartbeat filtering + inactivity-based fresh-connect retention, sim-mode load/replay/determinism, the POST action
skeleton, the trusted dashboard external-inbox endpoint, the shipped static-bundle resolver, and the
umbrella `agents-remember dashboard` CLI.

### 260712-TRH-L7 refresher shutdown regression

Serving tests cover the real app lifespan with a dead landing refresher, asserting the failure is logged and `TerminalHost.shutdown()` still runs exactly once. Projector tests also pin startup, cancellation, and network-free tick integration.

## Code Commentary

### FEUI-L9R Reviewed Candidate Delta

Serving regressions now pin three runtime-truth boundaries. Static HTML carries `no-cache`, and the
build payload carries the packaged `dashboardBuild` fingerprint *when a build was placed* (see the
`BuildInfoTests` note below — since 260731-EFA-L1 that stamp is present-or-omitted, never
fabricated). Raw-event tests cover lifecycle and
workspace mid-record realignment, malformed JSON and invalid UTF-8 advancing without retry, every
non-object JSON family advancing without emission, beyond-EOF settling, successor streaming, exact
cursor progression, and ready-after-valid-object ordering.

### MX-FIX-1 Atomic Folded-State Stream Regressions

Three async regressions pin the repaired authority boundary without timing luck. The handoff case
pauses after the initial snapshot while the subscriber queue is already registered, publishes a
lifecycle mutation before the next read, and requires that exact delta plus zero subscribers after
closure. The failed-prime case registers a waiting stream while no projection exists, publishes the
first successful state, requires one build-decorated snapshot at id `1`, republishes the identical
state without a duplicate, then requires the next ordinary lifecycle delta at id `2`. The
cancellation case cancels a waiting no-snapshot stream and requires immediate queue removal.

### Logic

L15 review follow-up (L15R-1): a reflection guard partitions every projection-model `*Seconds` field into VOLATILE_AGE_FIELDS or a curated content allow-list (`ttlSeconds`) — a new now-relative field that skips the volatile set (and its client mirror) now fails loudly instead of silently re-degrading the SSE diff.

`DeltaTests` assert `diff_projection`: the empty first tick, no-delta-on-unchanged, per-kind
upserts/changes/removals (lifecycle/provider/enclosure), whole-block `metrics`/`analytics`
events, and deterministic sorted removals. Task 33 extends this: the `_projection` test helper gained an
`active_worktree_groups` param, and two new cases cover the `activeWorktreeGroups` whole-value delta — a
changed set emits a single `DeltaEvent("activeWorktreeGroups", {"activeWorktreeGroups": [...]})`
(the wrapped marker the client unwraps), and an unchanged set emits nothing. **260703-L15 (the
change gate)** adds four cases: a volatile-only lifecycle change (`staleSeconds` via `model_copy`)
emits nothing; a volatile-only analytics change (a task doc's `ageSeconds`) emits nothing; a real
change emits the full current node WITH its fresh ages riding along; and the precomputed
`previous_state`/`current_state` call form produces byte-identical deltas to the pure two-argument
form. `ProjectorTests` (async) assert `prime()` sets the
latest projection — pinning `latest.version == 2` (slice 5e bumped the projection schema version
from 1 to 2) — `subscribe()` receives a broadcast, and Task 31 proves an injected provider refresher
runs before projection. `StreamEventsTests` (async) assert
`stream_events` emits an `event:snapshot` then a per-entity delta, and (L15 S3) that the snapshot
carries the injected `servingBuild` payload when a `ServingBuild` is passed. MX-FIX-1 adds forced
handoff publication, failed-prime recovery/non-duplication/later-delta, and cancellation-cleanup
cases; each asserts the subscriber set directly so generator ownership cannot regress silently.
`AppTests` use `TestClient`
(lifespan-triggered prime) for `/api/state` (asserting `body["version"] == 2`, the same bumped
schema version) and for `/` in **both** of its states, since 260731-EFA-L1 took the cockpit bundle
out of version control. `test_root_serves_dashboard_bundle` supplies its own stand-in bundle and
patches `serving.static.dashboard_static_dir` — it used to read the committed bundle straight out
of the repository, which now gives different verdicts before and after a frontend build — and
asserts only what is stable across rebuilds: the SPA mount point, the app title, and
`Cache-Control: no-cache`. `test_root_diagnoses_a_missing_bundle_instead_of_a_bare_404` patches the
resolver to `None` and requires the server to still boot, `/` to answer 503 naming the remedy with
`Cache-Control: no-store`, and `/api/state` to keep answering 200 behind the greedy mount.
`StaticTests.test_static_dir_resolves_only_a_real_built_bundle` keeps the honest half of the old
assertion — when resolution succeeds it must point at a real build (`index.html` plus `assets/`) —
and **skips** when this checkout has no build, because "never `None`" encoded the removed contract
that a 28 MB generated tree lives in git. The deterministic `None` half lives in `test_static.py`.

**`StateEtagTests` (260703-L15 S1)** drive the `/api/state` change gate end-to-end via
`TestClient` over a mocked `project_and_write` returning a held projection (a `held[0]` closure the
test swaps mid-run, `interval=0.02` so the real tick loop publishes; since 260712-PTS-L3 the app
disables the change-driven watcher because this world changes only through the mocked
`project_and_write`, which no filesystem watcher can observe — the tick loop must stay
interval-paced, exactly the live contract for watcher-invisible changes whose bound is the
heartbeat instead. **Since 260731-EFA-L2 that is expressed through parameter objects, not
keywords:** the cadence travels as `ProjectionCadence(interval=…)`, the watcher/landing switches as
`LiveProjectionInputs`, the projector's refreshers as `ProjectionRefreshers(...)`, and the four
substituted long-lived objects as one `ServingCollaborators` — the bare `watch_changes=False`
keyword no longer exists): 200 carries a weak
`ETag: W/"…"` + `Cache-Control: no-cache`; `If-None-Match` with that tag → 304 with the SAME tag
and an EMPTY body; swapping in a volatile-only change (staleSeconds) keeps returning 304 with the
same tag after several ticks; swapping in a real change (tokens) makes a deadline-polled
`_get_until` see 200 with a NEW tag and the fresh body. Plus the `servingBuild` presence on the
state body and the pure `_if_none_match_matches` table (weak/strong forms, comma lists, `*`,
mismatch, None). **`BuildInfoTests`** pin `resolve_serving_build`: in this checkout the commit
short-hash resolves and rides the wire form; anchored at a non-git tmp dir the commit is `None` and
OMITTED (never faked); the shape is camelCase (`bootedAt`). The
`dashboardBuild` assertion is now **present-or-omitted**, not an unconditional index: that only
held while the fingerprint sidecar was committed alongside the bundle, and both are now generated
at release time. **Since 260731-EFA-L4 `ServingBuild.payload()` returns the declared
`ServingBuildPayload` model rather than a dict**, so every one of these assertions goes through the
module-level helper `_build_wire(build)` (L128-L136), which is
`build.payload().model_dump(mode="json", exclude_none=True)`. That `exclude_none=True` is where the
honest-unknown rule is applied — absent, never null, never a fabricated "clean" — and it is applied
identically by `serving.served_state.served_state_tail`, so what these tests compare against is the
stamp exactly as the state body carries it. `StreamEventsTests.test_snapshot_carries_the_serving_build_stamp`
uses the same helper for the SSE snapshot's `servingBuild` key. The same class pins the dirty probe's tri-state
(`test_dirty_probe_is_tri_state_and_fails_open`: proven-dirty `True`, proven-clean `False`, and an
unprovable probe — raising or non-zero — failing OPEN to `None`) and its end-to-end consequence
(`test_status_failure_does_not_assert_a_pristine_tree`: `rev-parse` succeeds, `status` raises, so
the hash rides the wire while `dirty` stays `None` and is omitted). **Since 260731-EFA-L3 both mock
the package's one git runner, `agents_remember.serving.build_info.run_git`, not
`…build_info.subprocess.run`** — the module no longer spawns git itself, so that is where the seam
is; the substituted `fake_run` correspondingly takes `(repo, arguments, **kwargs)` and branches on
`arguments[:1] == ["rev-parse"]` rather than on a leading `"git"` argv element. What the tests prove
is unchanged. `CliTests`/`CliRunTests` assert the umbrella parser, the `dashboard`
flags, and `run()` (uvicorn/create_app mocked: launch + ConfigError + dispatch). Task 26 added
`--reload`: `CliRunTests._args` is now a `**overrides` builder seeding `reload: False`, and three
tests cover the dev path — `test_run_reload_launches_the_dev_factory` asserts `--reload` hands
uvicorn the import-string factory `agents_remember.cli.dashboard:_dev_app` with `factory=True`,
`reload=True`, and that `create_app` is NOT pre-built in this branch;
`test_run_reload_with_sim_is_rejected` asserts `--reload` + `--sim` → exit 1; and
`test_dev_app_factory_builds_from_env` calls `_dev_app()` directly, asserting it reads
`_DEV_CONFIG_ENV`/`_DEV_INTERVAL_ENV` and threads them through `load_config`/`create_app`
(`interval=2.5`). `import os` was added to support the `mock.patch.dict(os.environ, ...)` in that
last test.

The 4b additions:

- `RawEventTests` assert the pure tail (`serving.events`): cursor base64 round-trip + garbage →
  empty, new-lines-then-nothing, resume-from-cursor skips consumed, an unterminated trailing line
  waits for its newline, and multi-source ordering (lifecycles sorted, `workspace` last). Task 29
  extends the same suite so cursorless fresh connections use `initial_event_offsets`. Task 34 reworks
  retention onto **inactivity** and adds the heartbeat-filter + bounded-chunk coverage:
  `test_read_new_events_skips_heartbeats` (heartbeat lines advance the offset but are never emitted and
  not re-read on resume), `test_read_new_events_limit_bounds_batch` (`limit` returns the next bounded
  chunk), `test_dormant_promoted_lifecycle_pruned_without_terminal_event` (an enclosure-backed lifecycle
  that went quiet with NO `lifecycle.ended` is still pruned — a *recent heartbeat does not save it*),
  `test_dormant_fleeting_lifecycle_pruned_without_terminal_event`,
  `test_active_lifecycle_with_recent_activity_not_pruned`, and
  `test_initial_offsets_bound_active_replay_to_recent_window` (an active log with history older than the
  1h replay window replays only the recent row, not from byte zero). **L5** adds
  `test_protected_lifecycle_log_survives_inactivity`: a dormant, enclosure-backed log passed in
  `protected_lifecycle_ids` is exempt from pruning (it stays even though its last real activity is past
  the TTL), and dropping the protection then prunes it — proving the dormancy precondition held and that
  a live master series' history is what the protection set preserves.
  `StreamRawEventsTests` (async) assert `stream_raw_events` emits the backlog as `event` records,
  single-encoded (the SSE `data` is the parsed object, not the double-encoded JSON string), then emits a
  one-shot `ready` marker after backlog delivery; `test_stream_does_not_emit_heartbeats` proves the stream
  filters `lifecycle.heartbeat` and yields only the real `tool.completed`; and a malformed `Last-Event-ID`
  falls back to retained fresh offsets rather than replaying stale workspace history.
- `SimFixtureTests` assert `load_fixture` (sorted, missing → empty), `parse_sim_speed` (paused /
  number / errors), and `ReplayClock` (paused frozen, running advances). `SimReplayTests` assert
  `build_sim` overrides the root to a fresh dir (empty fixture → `SimError`), the progressive
  `ReplayFeeder`, that replay drives state transitions (running → blocked, tokens accrue), and
  byte-identical determinism across two independent sims.
- `ActionTests` assert the pure `evaluate_action` (202 + attribution, 409 disabled-with-reason,
  409 unknown-action, 404 unknown-target, enclosure target). `ActionEndpointTests` assert
  `POST /api/actions/{action}` via `TestClient` (404 unknown target, 422 unknown actor).
  `CliSimTests` assert the sim flags parse and the sim `run` path (clock + feeder passed,
  bad-speed and empty-fixture → exit 1).

The 6b addition: `ActionGateTests` covers the gate-decision path — the pure `evaluate_action`
emits a `GateDecisionIntent` for a gate-decision verb (and `None` for a transition), and
`POST /api/actions/approve` via `TestClient` records a developer/dashboard decision on a
pre-seeded open gate (asserting `decidedBy="developer"` + the store state) and returns
`409 no-open-gate` when none exists. Task 19 extends the same class so gate intents carry targeted
`gateId` and `note`, reject without a reason returns `400`, `/api/actions/reject` stores the
`decisionNote`, and a stale targeted gate id returns `409 stale-gate` without deciding either open
gate. Task 10 extends the same test class with
`POST /api/operator-inbox`: a successful request writes one pending `OperatorInboxStore` entry with
the lifecycle, agent, gate, ask, response, and developer/dashboard attribution; a request with no
lifecycle or agent key returns `400 bad-address`.
Task 23/24 adds serving coverage for the operator-inbox dismiss endpoint:
`POST /api/operator-inbox/{entry_id}/dismiss` deletes the pending entry and is used by the dashboard
`check chat` warning dismissal path.
Task 24 reopened extends gate-action coverage so pure evaluation allows only `cancel` with `gateId`
to omit a target, and `/api/actions/cancel` can delete a workspace-shaped gate by id.
Task 28 S5.2 adds `ActionDismissTests`: pure `dismiss` evaluation requires an `itemId` and lifecycle
scope for non-gate rows, `AttentionDismissalStore` upserts one current row, compacts legacy duplicate
rows, and prunes non-live lifecycle rows, `/api/actions/dismiss` records lifecycle
acknowledgements, and `gate-open` dismiss consumes the gate by cancellation/deletion without appending an
acknowledgement marker. Task 29 extends the same suite for actionable drift: pure evaluation allows
targetless actionable-drift dismissals, the store keeps actionable-drift current acknowledgements across
lifecycle pruning, and `/api/actions/dismiss` records a targetless acknowledgement row.

**Since 260731-EFA-L5 (R5), "prunes to nothing" is asserted as an EMPTY FILE, never a missing
one.** `test_attention_store_upserts_and_prunes_lifecycle_rows` (L1412-L1445) ended
`assertFalse(store.log_path().exists())`; that unlink is the defect the leaf removed. `dismiss` is
a whole-file read-modify-write reached from the dashboard's HTTP dismiss route, so a concurrent
dismisser holding a handle across the unlink wrote into an inode with no remaining links and the
dismissal vanished with the file — no error, no torn line. The proof that the prune happened is
unweakened and now reads as emptiness: `store.read() == []`, `log_path().is_file()`, and
`log_path().read_bytes() == b""`, against the one row that was demonstrably there a moment
earlier.

### Conventions

Third-party imports (`fastapi.testclient`) precede the `sys.path.insert(mcp/src)`; package
imports follow it (the suite idiom). An empty-`coordination_root` `McpRuntimeConfig` factory makes
`project_and_write` produce a valid empty projection in a tmp dir; the sim fixture lives at
`mcp/tests/fixtures/sim/logs/observer/...`. Async suites use `unittest.IsolatedAsyncioTestCase`,
and CLI launch tests patch `uvicorn.run` + `cli.dashboard.create_app`/`load_config` so no server
is actually started. Both CLI `run()` fixtures (`CliRunTests._args`, `CliSimTests._args`) build the
`argparse.Namespace` with every flag `run()` reads, including `reload: False`, (260703 L2) the
daemon-era keys `daemon`/`status`/`stop`: False + `no_access_log`: False, and (260712-PTS-L3)
`heartbeat: None` — `CliTests` also asserts the parsed `namespace.heartbeat` defaults to `None` —
so the fixtures stay
in lock-step with `dashboard.run()` reading those attrs; a missing attr would raise instead of
exercising the branch. Daemon dispatch itself is covered in `test_dashboard_daemon.py`, not here.

### Invariants And Boundaries

The suite requires poison records to advance without emission, accepted events to remain objects,
HTML-only revalidation, and absent build evidence to stay omitted rather than fabricated.

For the folded-state stream, publication must be observed either in the already-captured snapshot
or in the already-registered queue. First recovery must be one full build-decorated snapshot;
identical recovery emits nothing; later content changes use normal deltas; closing or cancelling a
consumer must leave no subscriber queue behind.

### Todos

No task-independent technical debt was identified during FEUI-L9R review.

## Docs References

No relevant documentation was found after checking the configured sources; the regression claims
are proven by repository source and the test suite itself.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external or domain documentation was found for this repository-local test module. | Source discovery checked | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The pure diff under test. | — | [serving/delta.py](agents-remember/mcp/src/agents_remember/serving/delta.py) |
| The `WorkspaceProjection` whose `version` field the tests pin (now `2` after slice 5e). | — | [observer/projection.py](agents-remember/mcp/src/agents_remember/observer/projection.py) |
| The projector under test owns atomic subscribe/snapshot activation, first-recovery publication, publish-before-notify ordering, and cleanup. | L135-L178; L207-L269 | [serving/projector.py](agents-remember/mcp/src/agents_remember/serving/projector.py) |
| The app consumes one projector iterator, decorates every snapshot with the serve-time tail, preserves SSE framing, and closes the subscription through `contextlib.aclosing`. | `stream_events` L300-L330 | [serving/app.py](agents-remember/mcp/src/agents_remember/serving/app.py) |
| The forced MX-FIX-1 regressions pin the handoff mutation, failed-prime recovery, identical-state silence, later delta, and cancellation cleanup. | L441-L503 | [test_serving.py](agents-remember/mcp/tests/test_serving.py) |
| The raw event tail under test. | L125-L277 | [serving/events.py](agents-remember/mcp/src/agents_remember/serving/events.py) |
| The inactivity-based raw event retention helper under test. | — | [observer/event_retention.py](agents-remember/mcp/src/agents_remember/observer/event_retention.py) |
| The raw retention regressions: dormant pruning without a terminal event, heartbeat skipping, bounded active replay, limit batches, workspace TTL, invalid cursor fallback, and no global cap. | — | [test_serving.py](agents-remember/mcp/tests/test_serving.py) |
| Task 34 retention/heartbeat/limit coverage in `RawEventTests`: heartbeat skipping, limit batches, dormant pruning without a terminal event, active-not-pruned, and bounded active replay. | L1937-L2005; L2032-L2062 | [test_serving.py](agents-remember/mcp/tests/test_serving.py) |
| L5 retention exemption: a protected dormant log survives inactivity and is pruned only once protection is dropped. | `test_protected_lifecycle_log_survives_inactivity` | [test_serving.py](agents-remember/mcp/tests/test_serving.py) |
| The `protected_lifecycle_ids` parameter under test, and the series-retention set it carries. | `prune_expired_lifecycle_event_logs`, `series_retained_lifecycle_ids` | [observer/event_retention.py](agents-remember/mcp/src/agents_remember/observer/event_retention.py) |
| Raw stream tests assert the one-shot `ready` event after backlog delivery and that heartbeats are not streamed. | L2073-L2086; L2123-L2152 | [test_serving.py](agents-remember/mcp/tests/test_serving.py) |
| The sim load/replay under test. | — | [serving/sim.py](agents-remember/mcp/src/agents_remember/serving/sim.py) |
| The action evaluation under test. | — | [serving/actions.py](agents-remember/mcp/src/agents_remember/serving/actions.py) |
| The gate write-path the `/api/actions` gate verbs drive (slice 6b). | — | [mcp/tools/gates.py](agents-remember/mcp/src/agents_remember/mcp/tools/gates.py) |
| The operator inbox store asserted by the dashboard `/api/operator-inbox` endpoint tests. | — | [controlplane/operator_inbox_store.py](agents-remember/mcp/src/agents_remember/controlplane/operator_inbox_store.py) |
| The compact attention acknowledgement store asserted by `ActionDismissTests`; `dismiss` is a whole-file read-modify-write and `prune_lifecycles` now empties the log through the contract's rewrite instead of unlinking it. | `dismiss`, `prune_lifecycles`, `_replace` | [controlplane/attention_dismissals.py](agents-remember/mcp/src/agents_remember/controlplane/attention_dismissals.py) |
| The rewrite that makes "emptied, not unlinked" true for every control-plane log at once: an empty record set is written as an empty file, never removed. | `rewrite_lines` | [controlplane/durable_store.py](agents-remember/mcp/src/agents_remember/controlplane/durable_store.py) |
| The prune-to-emptiness assertion this leaf rewrote, and the loss it used to hide. | `test_attention_store_upserts_and_prunes_lifecycle_rows` L1412-L1445 | [test_serving.py](agents-remember/mcp/tests/test_serving.py) |
| Actionable-drift dismiss tests cover targetless pure evaluation, store retention, and API persistence. | L1387-L1410; L1447-L1457; L1503-L1515 | [test_serving.py](agents-remember/mcp/tests/test_serving.py) |
| The CLI dispatcher + dashboard adapter under test. | — | [cli/__main__.py](agents-remember/mcp/src/agents_remember/cli/__main__.py) |
| The dashboard `run()` + `--reload` dev path + `_dev_app` factory under test. | — | [cli/dashboard.py](agents-remember/mcp/src/agents_remember/cli/dashboard.py) |
| `BuildInfoTests`' dirty-probe cases and the seam they patch (`agents_remember.serving.build_info.run_git`). | L1045-L1069; L1071-L1090 | [test_serving.py](agents-remember/mcp/tests/test_serving.py) |
| The probes under test: `_git_short_head` / `_git_worktree_dirty` call `run_git` with `timeout=_PROBE_TIMEOUT_SECONDS`, which is why the seam moved. | L40; L91-L118 | [serving/build_info.py](agents-remember/mcp/src/agents_remember/serving/build_info.py) |

## Cross-Repo References

No meaningful cross-repository implementation source governs this repository-local test module.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The reviewed behavior is wholly repository-local. | Import and task-boundary review | — |

## 260718-CHATS-L5I Current Delta

Serving tests now cover projection-body reuse, gzip for ordinary JSON, deliberately uncompressed SSE streaming, and the opt-in heap/allocator lifecycle hooks.

This entry supersedes conflicting earlier coverage notes while retaining their history; source verification metadata is deliberately unchanged until the code commit.

## 260727-CHATS-IM-L2 Current Delta

Four deliberate `project_and_write` doubles accept the additional optional projection inputs. They
continue returning the held projection, so ETag, body-cache, gzip, and SSE tests exercise their
original behavior rather than projection internals. Since 260731-EFA-L2 those inputs arrive as
parameter objects rather than as separate keywords; the doubles' behaviour is unchanged.

## 260731-EFA-L2 Delta — action-gate target resolution

Two arms of `evaluate_action`: an action naming **neither a lifecycle nor a gate** is
`missing-target`, and a dismiss scoped to nothing is `missing-lifecycle`. The distinction is the
point — both are 400s, and the code tells the caller which half of the address is absent. (The
recorder's own gate-id-only arm lives in `test_serving_app_routes.py::GateDecisionHelperTests`.)

## Update History

- 2026-08-01T14:20+02:00 — 260731-EFA-L5 curator: one assertion changed and every self-citation
  below it moved. **Coverage:**
  `ActionDismissTests::test_attention_store_upserts_and_prunes_lifecycle_rows` (L1412-L1445) ended
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
  `rewrite_lines` that makes "emptied, never unlinked" true for every control-plane log at once,
  and the rewritten test itself). **Citation repairs — 5 ranges.** The file grew 2418 → 2428
  lines, all of it at L1432 where 7 lines became 17, so every self-citation at or below L1442
  shifted by exactly +10 and each was re-verified against the symbol it names: the actionable-drift
  dismiss row L1437-L1447; L1493-L1505 → **L1447-L1457; L1503-L1515** (its first range, L1387-L1410,
  sits above the hunk and was re-verified unmoved); Task 34 retention L1927-L1995; L2022-L2052 →
  **L1937-L2005; L2032-L2062**; raw stream L2063-L2076; L2113-L2142 → **L2073-L2086; L2123-L2152**.
  The MX-FIX-1 trio (L441-L503), both dirty-probe rows (L1045-L1069; L1071-L1090) and the
  `_build_wire` helper (L128-L136) are above the hunk and were re-verified unmoved. No test was
  added, removed or renamed. Verification metadata pinned until closeout stamps the L5 commit.

- 2026-08-01T09:15+02:00 — 260731-EFA-L4 curator: `ServingBuild.payload()` now returns the declared
  `ServingBuildPayload` model instead of a dict, so every assertion that used to index `payload()`
  goes through the new module-level helper `_build_wire(build)` (L128-L136) —
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
