# mcp/src/agents_remember/observer/store.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/observer/store.py`      |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-31T00:00+02:00 |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060`       |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview      | `overview.md`                                     |

## Governing Overview

[observer overview](overview.md)

## Purpose

`store.py` is the append-only event store: it resolves a given event's log path
and appends it as one JSONL line.

## Code Commentary

### 260707-HFX2-L13 Workspace Cursor And Heartbeat Storage

Workspace appends now take a POSIX `flock` on `workspace/events.lock`, the same cross-process lock
used by physical compaction and live reads. `events.cursor.json` stores the non-negative virtual
`baseOffset`, written atomically, and `workspace_logical_size` exposes virtual EOF. This lock is
necessary rather than generic defensive code: serving and MCP processes both append while the live
compactor replaces the file, so an unlocked rewrite can lose writes or tear cursor state.

Lifecycle heartbeats no longer append to `events.jsonl`. They atomically overwrite one
`heartbeat.json` sidecar per lifecycle; `read()` merges the newest sidecar event into the validated
log, while `read_log()` and `read_heartbeat()` expose the two storage layers to the projection cache.
Real lifecycle and workspace events retain their prior JSONL routing.

### 260707-HFX2-L12 CS-6 Update

`EventStore.read()` now skips corrupt, legacy, or torn JSONL lines. That keeps one bad lifecycle event row from freezing the projection tick fleet-wide while preserving append-only write semantics for valid rows.

`EventStore(observer_root)` holds the `logs/observer/` root. `log_path(lifecycle_id)`
routes to `lifecycles/<id>/events.jsonl` when a lifecycle id is present, else the
shared `workspace/events.jsonl`. `append(event)` creates parent dirs on first
write and appends `event.model_dump_json(by_alias=True, exclude_none=True)`.
`read(lifecycle_id)` validates a log back into `Event` objects — the minimal,
validated read that proves the write format round-trips (the projection layer
will read more richly).

## Invariants And Boundaries

- **Single writer per lifecycle file.** Exclusive adoption (one live session per
  lifecycle) means appends need no cross-process lock. The only events written to
  a lifecycle file are written by its live owner; a dormant fleeting lifecycle
  past TTL is *pruned* (directory deletion), never terminated by a non-owner
  append — so the single-writer invariant holds without coordination.
- Append-only: history is never rewritten in place (corrections are later
  events, by design).

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The event envelope serialized and validated by the observer model. | "class Event" | mcp/src/agents_remember/observer/events.py:39-39 |
| The store layout, retention tiers, and TTL prune rule. | "TTL is fleeting-only" | docs/design/observable-lifecycle.md:107-107 |

## Update History

- 2026-08-02T20:42:26+02:00 — W2-B07 curator: repaired 2 repository-reference citations (2/2 anchored and sourced; scoped citation check clean).

- 2026-07-31T16:35+02:00 — No content impact: the only change to
  `mcp/src/agents_remember/observer/store.py` since the L2 base commit is the whole-tree `ruff
  format` pass in `00e8379`, which re-wrapped 3 line(s) with no token change whatsoever. Checked
  by parsing both revisions and comparing the abstract syntax trees (identical) and the comment
  tokens (identical), so no symbol, signature, default, decorator, control-flow branch, docstring,
  or assertion this card describes has moved, and every claim this card makes about its own source
  still holds.

- 2026-07-31T00:00+02:00 — 260731-EFA-L2 attestation: this file was touched ONLY by the
  whole-tree `ruff format` pass (commit `00e8379`) — line reflow, no behaviour, contract,
  structure or responsibility change. The sidecar was re-read against the current source and
  every claim in it still holds, so it was deliberately not rewritten. Verification metadata
  pinned until closeout stamps the L2 commit.
- 2026-07-10T01:14+02:00 — 260707-HFX2-L13 F3/F7: added the shared cross-process workspace-river
  lock and virtual base-offset sidecar, and coalesced lifecycle heartbeats into atomic per-lifecycle
  sidecars with merged reads. Verification metadata remains pinned until closeout stamps the eventual
  L13 code commit.

- 2026-07-09T19:31+02:00 — 260707-HFX2-L12: documented the CS-6 scaling/reclamation change for this file. Verification metadata pinned until closeout stamps the HFX2-L12 commit.
- 2026-06-13T11:15+02:00: Created for slice 2a. Verification metadata is pinned
  until closeout stamps the 2a code commit.
