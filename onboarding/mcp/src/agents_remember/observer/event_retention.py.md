# mcp/src/agents_remember/observer/event_retention.py

| Field                  | Value                                               |
| ---------------------- | --------------------------------------------------- |
| repository             | agents-remember                                     |
| path                   | `mcp/src/agents_remember/observer/event_retention.py` |
| doc_type               | `file-level-onboarding`                             |
| lastUpdated            | 2026-08-11T15:20+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`          |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `overview.md`                                       |

## Governing Overview

[observer overview](overview.md)

## Purpose

`event_retention.py` owns dashboard-served raw observer event retention. The Event
River is an *agent-activity* feed, not a process-liveness keepalive, so its history
is retired by **inactivity** — seconds since the last real (non-heartbeat) activity
event — per lifecycle type, rather than by a written `lifecycle.ended` event (real
sessions almost never emit one; they die silently). Heartbeats are liveness theater
and do not count as activity, so a parked lifecycle that only keeps beating is still
"inactive" and its throwaway log can be cleaned up regardless of lifecycle type.
Active logs remain replayable, but a fresh connection only re-streams a bounded recent
window per active source rather than an entire long-lived log from byte zero.

## Code Commentary

### 260707-HFX2-L13 Live River And Complete Reclamation

Workspace compaction is no longer startup-only. It runs under the shared cross-process river lock,
rewrites only retained rows, and advances the persisted virtual base offset by the reclaimed bytes.
Fresh-connect offsets therefore use `baseOffset + physicalOffset`, matching the live SSE cursor
coordinate system. The serving layer owns the sixty-second live compaction cadence.

Lifecycle pruning now removes the whole dormant, unprotected lifecycle directory with
`shutil.rmtree` after the existing protection/dormancy gates. This closes the round-1 F7 leak where
deleting only `events.jsonl` left `heartbeat.json` and served/gate sidecars permanently unreclaimable.
The whole-directory deletion is intentional: protected or active lifecycles cannot reach this
boundary.

### 260707-HFX2-L12 CS-6 Update

`compact_workspace_river()` physically reclaims aged `workspace/events.jsonl` rows at serving startup, the one cursor-safe boundary before SSE clients and serving writers exist. The always-on live compactor remains HFX2-L13 scope because byte-offset cursors and cross-process appenders need a larger contract change.

### Logic

`lifecycle_is_dormant(path, *, now)` is the cleanup key: it reads
`_retention_facts(path)` for the last real activity timestamp and whether the
lifecycle is still fleeting, then returns true when the seconds since that activity
exceed the per-type TTL — `FLEETING_INACTIVE_TTL_SECONDS` for an un-promoted fleeting
lifecycle, `ENCLOSURE_INACTIVE_GRACE_SECONDS` for a promoted/enclosure-backed one
(both currently one hour). A log with no parseable activity is treated as not-yet-dormant.

`_retention_facts(path)` is the single-pass reader returning
`(last_real_activity_ts, is_fleeting)`: it skips `HEARTBEAT_KIND` rows entirely (a
heartbeat never advances the activity timestamp), reads `data.fleeting` off
`lifecycle.started`, and clears the fleeting flag once a `lifecycle.promoted` row is
seen. `last_activity_at(path)` exposes just that activity timestamp.

`initial_event_offsets(root, *, now)` builds the initial byte-offset map used when a
client connects without `Last-Event-ID`. A **dormant** lifecycle log starts at EOF
(`st_size`) so ancient history is never replayed; an **active** log starts at a bounded
recent window via `_first_retained_offset(cutoff=now - REPLAY_WINDOW_SECONDS)` — NOT byte
zero — so a reload keeps useful task-local history without re-streaming the whole log. The
reserved `workspace` source starts at the first row inside the workspace TTL. Cursor
resumes stay owned by `serving.events.decode_cursor`.

`prune_expired_lifecycle_event_logs(root, *, now, protected_lifecycle_ids=frozenset())`
physically unlinks `lifecycles/<id>/events.jsonl` for **any** dormant log (inactivity past
its TTL) — not only terminal ones — and attempts to remove the now-empty lifecycle directory.
`protected_lifecycle_ids` is an exemption set checked *before* dormancy: a log whose id is in
the set is skipped no matter how long it has been inactive. The dashboard passes the lifecycle
ids of every leaf in a not-yet-retired master series (from
`worktree_provider_admission.series_retained_lifecycle_ids`), so a running durable task — and
all of its sibling leaves — keep their full event history until the whole series is archived
(plus a grace window). This **supersedes** the per-log inactivity TTL for durable,
enclosure-backed work; only fleeting/standalone logs are still retired by inactivity alone.
`lifecycle_terminal_at(path)` is retained for back-compat (the explicit `lifecycle.ended`
reader) but is no longer the prune or offset gate.

`_first_retained_offset(path, *, cutoff)` returns the offset of the first event it cannot
prove is older than `cutoff`. Events whose timestamp is unparseable are **kept** (we never
silently drop an event we cannot age), so only events with a valid timestamp strictly older
than the cutoff are skipped. `_iter_event_payloads` is the complete-line JSONL iterator
(ignores malformed rows, stops at a trailing partial line, yields byte offsets); `_event_time`
normalizes ISO timestamps to UTC and accepts both `Z` and explicit offsets.

### Conventions

The module is intentionally independent of FastAPI/SSE. It works only from an
observer log root and a supplied clock so tests can pin retention behavior
without a live dashboard server.

### Invariants And Boundaries

- Retention keys on **inactivity**, not on a terminal event, so EVERY lifecycle type
  is cleanable — a dormant promoted/enclosure-backed log is retired even though it never
  wrote `lifecycle.ended` (real sessions die silently).
- **A live master series supersedes the inactivity TTL.** `protected_lifecycle_ids` is
  checked before dormancy, so a durable task in a not-yet-retired series (and its sibling
  leaves) keeps its whole history even while idle. The protection set is computed from durable
  enclosure state by the caller; this module just honors it. Without an id in that set, the
  ordinary per-type TTL applies — so fleeting/standalone logs are unaffected.
- **Heartbeats are not activity.** A parked lifecycle that only keeps beating still ages
  out; only real (non-heartbeat) events reset the inactivity clock.
- No global raw-event count cap lives here; retention is inactivity-time based, and active
  lifecycle logs are never pruned by count.
- A fresh connection replays only the recent window per active source
  (`REPLAY_WINDOW_SECONDS`), never the whole log from byte zero; dormant logs replay nothing.
- Workspace events have a separate age window because they have no lifecycle identity.
- An event whose timestamp cannot be parsed is never aged out — it is kept rather than dropped.
- The module reads only complete JSONL rows and never consumes a partial append.

### Todos

No file-local todos.

## Docs References

No relevant external documentation was found after checking the in-repo design docs.
This file implements repository-local dashboard retention policy.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation found after checking in-repo design docs for raw dashboard retention mechanics. | n/a | n/a |

## Repo-Internal References

The serving layer calls this policy before raw event replay; the focused serving
tests pin dormant pruning without a terminal event, heartbeat-skipping activity
reads, bounded active-window replay, and no global cap across parallel active
lifecycles.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fresh-connect offsets are bounded: dormant logs to EOF, active logs to the recent replay window, workspace to its TTL boundary. | `initial_event_offsets` | mcp/src/agents_remember/observer/event_retention.py:44-70 |
| `lifecycle_is_dormant` is the inactivity cleanup key; `_retention_facts`/`last_activity_at` read the last real activity and ignore heartbeats. | `lifecycle_is_dormant`; `_retention_facts`; `last_activity_at` | mcp/src/agents_remember/observer/event_retention.py:155-166; mcp/src/agents_remember/observer/event_retention.py:169-171; mcp/src/agents_remember/observer/event_retention.py:186-207 |
| Any dormant lifecycle log (inactivity past its per-type TTL) is physically removed — not only terminal ones. | `prune_expired_lifecycle_event_logs` | mcp/src/agents_remember/observer/event_retention.py:73-107 |
| `protected_lifecycle_ids` exempts a log from pruning regardless of inactivity; the projection store passes a not-yet-retired master series' leaf ids so a live durable task keeps its history. | `protected_lifecycle_ids`; `prune_expired_lifecycle_event_logs` | mcp/src/agents_remember/observer/event_retention.py:73-107 |
| The protection set is derived from durable enclosure state (a live master series) by the admission module. | `series_retained_lifecycle_ids` | mcp/src/agents_remember/observer/worktree_provider_admission.py:76-101 |
| A protected dormant log survives inactivity and is pruned only once protection is dropped. | `test_protected_lifecycle_log_survives_inactivity` | mcp/tests/test_serving_raw_events.py:334-357 |
| `_first_retained_offset` keeps unparseable-timestamp events and skips only events with a valid ts strictly older than the cutoff. | `_first_retained_offset` | mcp/src/agents_remember/observer/event_retention.py:210-223 |
| The raw SSE tailer calls retention pruning and uses retained initial offsets only when no cursor is supplied. | "async def stream_raw_events("; "offsets = await asyncio.to_thread(initial_event_offsets, root, now=now)"; "await asyncio.to_thread(prune_expired_lifecycle_event_logs, root, now=now)" | mcp/src/agents_remember/serving/events.py:232-277 |
| Raw-event tests cover dormant pruning without a terminal event, heartbeat skipping, bounded active replay, limit batches, and uncapped parallel active history. | `test_fresh_connection_does_not_cap_parallel_active_lifecycle_history`; `test_read_new_events_skips_heartbeats`; `test_read_new_events_limit_bounds_batch`; `test_dormant_promoted_lifecycle_pruned_without_terminal_event`; `test_dormant_fleeting_lifecycle_pruned_without_terminal_event`; `test_protected_lifecycle_log_survives_inactivity`; `test_initial_offsets_bound_active_replay_to_recent_window` | mcp/tests/test_serving_raw_events.py:236-262; mcp/tests/test_serving_raw_events.py:264-280; mcp/tests/test_serving_raw_events.py:282-295; mcp/tests/test_serving_raw_events.py:297-318; mcp/tests/test_serving_raw_events.py:320-332; mcp/tests/test_serving_raw_events.py:334-357; mcp/tests/test_serving_raw_events.py:374-389 |

## Cross-Repo References

No meaningful cross-repo references found. This policy is local to the observer
log layout.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-08-11T15:20+02:00 — Replaced generic retention-call anchors with the unique stream
  declaration and its exact initial-offset and pruning calls.
- 2026-08-03T03:56+02:00 — 260731-EFA-L6 W3-B10 curator: anchored 6 table citations and normalized 6 source paths; no unresolved Tier-3 claims.

- 2026-07-10T01:14+02:00 — 260707-HFX2-L13 F3/F7: made workspace-river compaction live and
  virtual-cursor-aware, then changed dormant unprotected lifecycle cleanup to reclaim the complete
  sidecar-bearing directory. Verification metadata remains pinned until closeout stamps the eventual
  L13 code commit.

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->

- 2026-07-09T19:31+02:00 — 260707-HFX2-L12: documented the CS-6 scaling/reclamation change for this file. Verification metadata pinned until closeout stamps the HFX2-L12 commit.
- 2026-06-30T00:00:00+02:00 — L5 (260628_operations-integration): `prune_expired_lifecycle_event_logs` gained a
  `protected_lifecycle_ids` exemption checked before dormancy. A not-yet-retired master series' leaf
  ids (from `series_retained_lifecycle_ids`) are passed in by `projection_store.project_and_write`, so a
  running durable task keeps its (and its siblings') full event history regardless of inactivity —
  superseding the per-type TTL for enclosure-backed work. Documented in Logic, Invariants, and
  Repo-Internal References. Verification metadata pinned until closeout stamps the L5 code commit.
- 2026-06-28T13:54+02:00 — Task 34: retention now keys on INACTIVITY per lifecycle type
  (seconds since the last real, non-heartbeat activity event), not a written `lifecycle.ended`.
  Added `lifecycle_is_dormant` (the cleanup key) / single-pass `_retention_facts` / `last_activity_at`
  and `FLEETING_INACTIVE_TTL_SECONDS`/`ENCLOSURE_INACTIVE_GRACE_SECONDS`/`REPLAY_WINDOW_SECONDS`/
  `HEARTBEAT_KIND`; prune now deletes ANY dormant log and `initial_event_offsets` bounds active replay
  to the recent window (dormant → EOF) while `_first_retained_offset` keeps unparseable-ts events.
  Verification metadata pinned until closeout stamps the task-34 code commit.
- 2026-06-28T05:38+02:00 — Created for task 29: lifecycle-aware raw Event River
  retention now owns fresh-connect offsets, one-hour terminal lifecycle pruning,
  workspace TTL replay, and complete-line parsing. Verification metadata pinned
  until closeout stamps the task-29 code commit.
