# mcp/src/agents_remember/observer/served_store.py

## Governing Overview

[overview.md](overview.md)

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

## Evidence

### Repo-Internal References

- The ambient lifecycle owns this store and the in-memory served-set hot path. [1]
- The append-only event store this mirrors (the GateStore pattern). [2]
- The observer-root resolver that anchors the per-lifecycle path. [3]
- The application entry point consumer that records and resets served pieces. [4]
