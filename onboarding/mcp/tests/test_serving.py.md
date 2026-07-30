# test_serving.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_serving.py`                      |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-07-30T12:51+02:00 |
| lastVerifiedCommitHash | `3a8ff703d796dc585b86a458daaf9eb2af6b2b31`       |
| lastVerifiedCommitDate | 2026-07-30T13:59:13+02:00|
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
build payload carries the packaged `dashboardBuild` fingerprint. Raw-event tests cover lifecycle and
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
schema version) and `/` (now the shipped React bundle, not the slice-04 placeholder); `StaticTests`
assert `dashboard_static_dir`.

**`StateEtagTests` (260703-L15 S1)** drive the `/api/state` change gate end-to-end via
`TestClient` over a mocked `project_and_write` returning a held projection (a `held[0]` closure the
test swaps mid-run, `interval=0.02` so the real tick loop publishes; since 260712-PTS-L3 the app is
built with `watch_changes=False` because this world changes only through the mocked
`project_and_write`, which no filesystem watcher can observe — the tick loop must stay
interval-paced, exactly the live contract for watcher-invisible changes whose bound is the
heartbeat instead): 200 carries a weak
`ETag: W/"…"` + `Cache-Control: no-cache`; `If-None-Match` with that tag → 304 with the SAME tag
and an EMPTY body; swapping in a volatile-only change (staleSeconds) keeps returning 304 with the
same tag after several ticks; swapping in a real change (tokens) makes a deadline-polled
`_get_until` see 200 with a NEW tag and the fresh body. Plus the `servingBuild` presence on the
state body and the pure `_if_none_match_matches` table (weak/strong forms, comma lists, `*`,
mismatch, None). **`BuildInfoTests`** pin `resolve_serving_build`: in this checkout the commit
short-hash resolves and rides `payload()`; anchored at a non-git tmp dir the commit is `None` and
OMITTED from the payload (never faked); the payload shape is camelCase (`bootedAt`). `CliTests`/`CliRunTests` assert the umbrella parser, the `dashboard`
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
rows, and prunes non-live lifecycle rows from disk, `/api/actions/dismiss` records lifecycle
acknowledgements, and `gate-open` dismiss consumes the gate by cancellation/deletion without appending an
acknowledgement marker. Task 29 extends the same suite for actionable drift: pure evaluation allows
targetless actionable-drift dismissals, the store keeps actionable-drift current acknowledgements across
lifecycle pruning, and `/api/actions/dismiss` records a targetless acknowledgement row.

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
| The app consumes one projector iterator, decorates every snapshot, preserves SSE framing, and explicitly closes the subscription. | L181-L203; L702-L707 | [serving/app.py](agents-remember/mcp/src/agents_remember/serving/app.py) |
| The forced MX-FIX-1 regressions pin the handoff mutation, failed-prime recovery, identical-state silence, later delta, and cancellation cleanup. | L395-L457 | [test_serving.py](agents-remember/mcp/tests/test_serving.py) |
| The raw event tail under test. | L125-L277 | [serving/events.py](agents-remember/mcp/src/agents_remember/serving/events.py) |
| The inactivity-based raw event retention helper under test. | — | [observer/event_retention.py](agents-remember/mcp/src/agents_remember/observer/event_retention.py) |
| The raw retention regressions: dormant pruning without a terminal event, heartbeat skipping, bounded active replay, limit batches, workspace TTL, invalid cursor fallback, and no global cap. | — | [test_serving.py](agents-remember/mcp/tests/test_serving.py) |
| Task 34 retention/heartbeat/limit coverage in `RawEventTests`: heartbeat skipping, limit batches, dormant pruning without a terminal event, active-not-pruned, and bounded active replay. | L994-L1074 | [test_serving.py](agents-remember/mcp/tests/test_serving.py) |
| L5 retention exemption: a protected dormant log survives inactivity and is pruned only once protection is dropped. | `test_protected_lifecycle_log_survives_inactivity` | [test_serving.py](agents-remember/mcp/tests/test_serving.py) |
| The `protected_lifecycle_ids` parameter under test, and the series-retention set it carries. | `prune_expired_lifecycle_event_logs`, `series_retained_lifecycle_ids` | [observer/event_retention.py](agents-remember/mcp/src/agents_remember/observer/event_retention.py) |
| Raw stream tests assert the one-shot `ready` event after backlog delivery and that heartbeats are not streamed. | L1085-L1124 | [test_serving.py](agents-remember/mcp/tests/test_serving.py) |
| The sim load/replay under test. | — | [serving/sim.py](agents-remember/mcp/src/agents_remember/serving/sim.py) |
| The action evaluation under test. | — | [serving/actions.py](agents-remember/mcp/src/agents_remember/serving/actions.py) |
| The gate write-path the `/api/actions` gate verbs drive (slice 6b). | — | [mcp/tools/gates.py](agents-remember/mcp/src/agents_remember/mcp/tools/gates.py) |
| The operator inbox store asserted by the dashboard `/api/operator-inbox` endpoint tests. | — | [controlplane/operator_inbox_store.py](agents-remember/mcp/src/agents_remember/controlplane/operator_inbox_store.py) |
| The compact attention acknowledgement store asserted by `ActionDismissTests`. | — | [controlplane/attention_dismissals.py](agents-remember/mcp/src/agents_remember/controlplane/attention_dismissals.py) |
| Actionable-drift dismiss tests cover targetless pure evaluation, store retention, and API persistence. | L558-L616; L662-L674 | [test_serving.py](agents-remember/mcp/tests/test_serving.py) |
| The CLI dispatcher + dashboard adapter under test. | — | [cli/__main__.py](agents-remember/mcp/src/agents_remember/cli/__main__.py) |
| The dashboard `run()` + `--reload` dev path + `_dev_app` factory under test. | — | [cli/dashboard.py](agents-remember/mcp/src/agents_remember/cli/dashboard.py) |

## Cross-Repo References

No meaningful cross-repository implementation source governs this repository-local test module.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The reviewed behavior is wholly repository-local. | Import and task-boundary review | — |

## 260718-CHATS-L5I Current Delta

Serving tests now cover projection-body reuse, gzip for ordinary JSON, deliberately uncompressed SSE streaming, and the opt-in heap/allocator lifecycle hooks.

This entry supersedes conflicting earlier coverage notes while retaining their history; source verification metadata is deliberately unchanged until the code commit.

## 260727-CHATS-IM-L2 Current Delta

Four deliberate `project_and_write` doubles accept the new optional `input_state` and `refresh`
keywords. They continue returning the held projection, so ETag, body-cache, gzip, and SSE tests
exercise their original behavior rather than projection internals.

## Update History

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
