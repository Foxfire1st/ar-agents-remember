# mcp/src/agents_remember/observer/served_store.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/observer/served_store.py` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-02T01:05+02:00 |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb`       |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
| governingOverview      | `overview.md`                                     |

## Purpose

`served_store.py` is the append-only served-onboarding ledger (slice 07),
co-located with the observer substrate. A served record is the durable fact "this
onboarding piece was already served to this lifecycle, at this content hash" — it
lets `read_ar_files` dedup the auto-attached overview/sidecar bodies so a repeated
read does not re-spam onboarding the model already holds. The ledger is on-disk
(not only in process memory) so the dedup state survives a context compaction, in
which the same lifecycle continues in place.

## Code Commentary

### 260707-HFX2-L12 CS-6 Update

`ServedStore.read()` now skips a malformed served row instead of raising. The fallback consequence is at most re-serving an onboarding packet once, not failing `read_ar_files` or the dashboard path.

`SERVED_RECORD_SCHEMA` is the versioned wire tag (`ar-served-record/v1`).
`now_iso()` is the record timestamp (ISO 8601, UTC). `served_key(kind, path,
content_hash)` builds the dedup key folded over the log: `<kind>:<path>:<hash>`.

`ServedRecord` (a Pydantic `BaseModel`, `extra="forbid"`) is one snapshot:
`schema_version` (the lone alias — `schema` on the wire, because `schema` is an
awkward attribute name), `kind`, `path`, `hash`, and `ts`. `key()` returns its
`served_key`. The leaf fields are camelCase-free to keep the wire form small;
always dump with `model_dump_json(by_alias=True, exclude_none=True)` so
`schema_version` renders as `schema`.

`ServedStore(observer_root)` resolves and reads/writes per-lifecycle ledgers — the
GateStore pattern. `log_path(lifecycle_id)` routes to
`<observer_root>/lifecycles/<id>/served.jsonl`, beside that lifecycle's
`events.jsonl` / `gates.jsonl`. `append` creates parent dirs on first write and
appends one JSON line. `read` validates a log back into `ServedRecord`s (empty
when absent). `served_set` folds the log into the set of `<kind>:<path>:<hash>`
keys served so far.

A compaction would otherwise leave the served set stale (onboarding the model lost
to truncation would not re-serve), but a session-hook **producer** for the
`compact-reset.json` marker is **not** planned (S5 retarget): compaction-reset is a
fresh-worker / lifecycle concern (small work → new worker → new lifecycle → fresh
ledger) deferred to the post-3.0 **agentic-control-plane** follow-up, and `clear` /
a new chat already yields a fresh lifecycle and ledger. Until then `refresh=true`
is the working manual reset; the application-side marker consumer
(`application/read_files._maybe_reset_served`) stays as defensive scaffolding.

## Invariants And Boundaries

- **A record, not a public MCP response.** It carries no token fields and is never
  returned by a tool, so it is *not* registered in
  `tool_registry.PUBLIC_TOOL_RESPONSE_MODELS`.
- **Append-only and history-preserving.** The set of served keys is derived by
  folding the log; history is never rewritten in place.
- **Single writer per file.** A lifecycle is owned by one live session, so appends
  to its `served.jsonl` need no cross-process lock — the same single-writer
  assumption the event and gate stores make.
- Co-located with the observer substrate: the ledger lives under the same
  `observer_root` as the event/gate logs.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The ambient lifecycle owns this store and the in-memory served-set hot path. | `AmbientLifecycle` | mcp/src/agents_remember/observer/ambient.py:90-594 |
| The append-only event store this mirrors (the GateStore pattern). | `EventStore` | mcp/src/agents_remember/observer/store.py:103-171 |
| The observer-root resolver that anchors the per-lifecycle path. | `observer_root` | mcp/src/agents_remember/serving/projections/paths.py:32-34 |
| The application entry point consumer that records and resets served pieces. | `_maybe_reset_served` | mcp/src/agents_remember/application/read_files.py:357-381 |

## Update History

- 2026-08-03T04:00:52+02:00 — 260731-EFA-L6 W3-B06 curator: curated 10 citation findings for the served-ledger ownership, storage, path, consumer, and re-export rows.

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-09T19:31+02:00 — 260707-HFX2-L12: documented the CS-6 scaling/reclamation change for this file. Verification metadata pinned until closeout stamps the HFX2-L12 commit.
- 2026-06-23T00:53+02:00 — Slice 07 (S5): retargeted the module-docstring compact-reset note — the `compact-reset.json` **producer** is **not** planned at the session-hook level; it is deferred to the post-3.0 agentic-control-plane follow-up (fresh-worker / new-lifecycle = fresh ledger). The controller-side consumer + `refresh=true` stay as defensive scaffolding. Docstring text only; the `ServedRecord`/`ServedStore` surface is unchanged. Verification metadata pinned until closeout stamps the slice-07 code commit.
- 2026-06-22T22:33+02:00 — Created for slice 07: the `ServedRecord` + `ServedStore` per-lifecycle append-only `served.jsonl` content-hash dedup ledger (GateStore pattern, beside the events/gates logs). Verification metadata pinned until closeout stamps the slice-07 code commit.
