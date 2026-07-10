# mcp/src/agents_remember/observer/event_retention.py

| Field                  | Value                                               |
| ---------------------- | --------------------------------------------------- |
| repository             | agents-remember                                     |
| path                   | `mcp/src/agents_remember/observer/event_retention.py` |
| doc_type               | `file-level-onboarding`                             |
| lastUpdated            | 2026-07-10T01:14+02:00 |
| lastVerifiedCommitHash | `e400ed0ce98752d1b65d00de97c9b84c7ea20814`          |
| lastVerifiedCommitDate | 2026-07-10T20:04:45+02:00|
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

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found after checking in-repo design docs for raw dashboard retention mechanics. | n/a | n/a |

## Repo-Internal References

The serving layer calls this policy before raw event replay; the focused serving
tests pin dormant pruning without a terminal event, heartbeat-skipping activity
reads, bounded active-window replay, and no global cap across parallel active
lifecycles.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Fresh-connect offsets are bounded: dormant logs to EOF, active logs to the recent replay window, workspace to its TTL boundary. | L36-L61 | [event_retention.py](event_retention.py) |
| `lifecycle_is_dormant` is the inactivity cleanup key; `_retention_facts`/`last_activity_at` read the last real activity and ignore heartbeats. | L83-L135 | [event_retention.py](event_retention.py) |
| Any dormant lifecycle log (inactivity past its per-type TTL) is physically removed — not only terminal ones. | L64-L80 | [event_retention.py](event_retention.py) |
| `protected_lifecycle_ids` exempts a log from pruning regardless of inactivity; the projection store passes a not-yet-retired master series' leaf ids so a live durable task keeps its history. | L64-L91 | [event_retention.py](event_retention.py) |
| The protection set is derived from durable enclosure state (a live master series) by the admission module. | `series_retained_lifecycle_ids` | [worktree_provider_admission.py](worktree_provider_admission.py) |
| A protected dormant log survives inactivity and is pruned only once protection is dropped. | `test_protected_lifecycle_log_survives_inactivity` | [test_serving.py](../../../tests/test_serving.py) |
| `_first_retained_offset` keeps unparseable-timestamp events and skips only events with a valid ts strictly older than the cutoff. | L138-L151 | [event_retention.py](event_retention.py) |
| The raw SSE tailer calls retention pruning and uses retained initial offsets only when no cursor is supplied. | L199-L213 | [serving/events.py](../serving/events.py) |
| Raw-event tests cover dormant pruning without a terminal event, heartbeat skipping, bounded active replay, limit batches, and uncapped parallel active history. | L888-L1074 | [test_serving.py](../../../tests/test_serving.py) |

## Cross-Repo References

No meaningful cross-repo references found. This policy is local to the observer
log layout.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

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
