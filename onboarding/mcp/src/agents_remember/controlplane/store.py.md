# mcp/src/agents_remember/controlplane/store.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/controlplane/store.py`  |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-31T00:00+02:00 |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d`       |
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
| governingOverview      | `overview.md`                                    |

## Purpose

`store.py` is the gate store: it resolves a gate snapshot's log path, appends
active snapshots as JSONL, folds current state, and can physically remove or
compact short-lived interaction gates when the retention policy says they are no
longer needed.

## Code Commentary

### 260707-HFX2-L12 CS-6 Update

`GateStore.compact_current()` combines the gate keep-filter and current-fold in one read, with physical rewrite gated by the caller. Projection can now read each gate log once per tick while still seeing expired/consumed rows filtered out.

`GateStore(observer_root)` holds the observer root. `log_path(lifecycle_id)`
routes to `lifecycles/<id>/gates.jsonl` beside that lifecycle's `events.jsonl`,
or `workspace/gates.jsonl` when lifecycle-less. `append(record)` creates parent
dirs on first write and appends `record.model_dump_json(by_alias=True,
exclude_none=True)`. `read(lifecycle_id)` validates the log back into
`GateRecord`s. `current(lifecycle_id)` folds the log by gate id, last snapshot
wins.

Task 23/24 added real deletion/compaction. `delete(gate_id, lifecycle_id)`
rewrites the log without that gate id, `compact(lifecycle_id, now=...)` removes
expired/open-too-long or already-consumed interaction gates according to
`interaction_retention.gate_keep_ids`, and `lifecycle_ids()` enumerates gate logs
for projection-time TTL cleanup. Rewrites are atomic tmp-write + `os.replace`;
empty logs are unlinked.

## Invariants And Boundaries

- **Append while active, compact when consumed.** Gate history is preserved while a
  gate is active or waiting for a consuming tool. Dismiss/Clear/TTL and applied
  handoffs physically remove interaction rows instead of keeping them forever.
- One writer per lifecycle file in practice (a lifecycle is owned by one live
  session) — the same single-writer assumption the event store makes.
- Co-located with the event substrate under `observer_root`; no new storage root.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The gate envelope serialized and validated here. | [records.py](agents-remember/mcp/src/agents_remember/controlplane/records.py) |
| Mirrors the observer event store (same append / read / JSONL shape). | [observer/store.py](agents-remember/mcp/src/agents_remember/observer/store.py) |

As of cycle 5 GateStore.find(gate_id) resolves one gate id across the workspace log and every lifecycle log — the seam-decide path: the deciding seat holds only the packet-carried gate id; lifecycle ids stay server-side. Cycle 6 adds `all_current()`, the cross-lifecycle enforcement fold: it merges every gate log (workspace + all lifecycles) last-wins per gate id, so identity-addressed consumers (the integrate-side master-handover guard, which matches by the gate's `enclosure`) can see a seam gate raised on a different lifecycle than the one the consuming contract anchors.

## Update History

- 2026-07-31T16:35+02:00 — No content impact: the only change to
  `mcp/src/agents_remember/controlplane/store.py` since the L2 base commit is the whole-tree `ruff
  format` pass in `00e8379`, which re-wrapped 2 line(s) with no token change whatsoever. Checked
  by parsing both revisions and comparing the abstract syntax trees (identical) and the comment
  tokens (identical), so no symbol, signature, default, decorator, control-flow branch, docstring,
  or assertion this card describes has moved, and every claim this card makes about its own source
  still holds.

- 2026-07-31T00:00+02:00 — 260731-EFA-L2 attestation: this file was touched ONLY by the
  whole-tree `ruff format` pass (commit `00e8379`) — line reflow, no behaviour, contract,
  structure or responsibility change. The sidecar was re-read against the current source and
  every claim in it still holds, so it was deliberately not rewritten. Verification metadata
  pinned until closeout stamps the L2 commit.
- 2026-07-09T19:31+02:00 — 260707-HFX2-L12: documented the CS-6 scaling/reclamation change for this file. Verification metadata pinned until closeout stamps the HFX2-L12 commit.
- 2026-07-05T19:10+02:00 - L8 builder cycle 6: added `GateStore.all_current()` — the whole-workspace fold the integrate seam guard uses (AR3-1(b)). Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T18:20+02:00 - L8 seam channel (cycle 5): GateStore.find cross-lifecycle resolution added. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-06-25T13:10+02:00 — Task 23/24: added physical gate deletion, atomic log replacement, lifecycle-log enumeration, and retention compaction for throwaway gate interactions.
- 2026-06-18T01:05+02:00 — Created for task 6 slice 6a: the append-only `GateStore`. Verification metadata pinned until closeout stamps the 6a code commit.
