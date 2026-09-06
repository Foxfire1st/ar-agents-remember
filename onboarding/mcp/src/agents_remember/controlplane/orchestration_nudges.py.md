# mcp/src/agents_remember/controlplane/orchestration_nudges.py

| Field                  | Value                                                             |
| ---------------------- | ----------------------------------------------------------------- |
| repository             | agents-remember                                                   |
| path                   | `mcp/src/agents_remember/controlplane/orchestration_nudges.py`    |
| doc_type               | `file-level-onboarding`                                           |
| lastUpdated | 2026-09-05T22:25+00:00 |
| lastVerifiedCommitHash |                                                                   `7bf564a663bb61f12844dee39538dd09a1633cdb`|
| lastVerifiedCommitDate |                                                                   2026-08-10T12:28:42+02:00|
| governingOverview      | `overview.md`                                                     |

## Governing Overview

[overview.md](overview.md)

## Purpose

Persists rate-limited orchestration nudge attempts for inactivity and missing
turn-report artifacts.

## Code Commentary

### 260731-EFA-L5 Durable Store Contract

This log lost **9.20 percent** of appended rows at the base commit under ordinary two-process
operation — whole rows, never torn. Both the MCP nudge tool and the dashboard agent-notifier sweep
append here, and `replace_records` rewrote the whole file with no lock at all.

All file I/O now routes through `controlplane/durable_store.py` under
`ORCHESTRATION_NUDGE_OWNERSHIP`, which names both processes as writers and the **dashboard** as the
compaction owner. There is no production reclaim pass yet; the dashboard is named owner now, rather
than left to be decided by whoever eventually writes one, because `replace_records` is the store's
declared rewrite entry point and the supervisor is the only sweep that could ever drive it.

`append` calls `check_declared_writer()` and holds `exclusive_access` around `append_line`, which
fsyncs. `OrchestrationNudgeRecord` now inherits `DurableRecord`, picking up `extra="forbid"`
(previously declared locally) plus a validated `schemaVersion`.

### 260731-EFA-L5 `compact` Is New, And `replace_records` Now Refuses An Unlocked Caller

The module previously exposed only the raw rewrite primitive `replace_records(path, records)`. That
is exactly the defect this leaf exists to remove, reachable through the store's own public API:
`records` was chosen by a read the call did not make, so anything appended between that read and the
rewrite is discarded. Locking only the write would have looked safe and lost records.

Two changes close it:

- **`OrchestrationNudgeStore.compact(*, keep)`** is new and is the entry point to use. It holds
  **one** `exclusive_access` across the read, the filter and the rewrite, returns how many records
  were dropped, and rewrites nothing when `keep` selects everything.
- **`replace_records` now calls `require_lock_held` first** and raises `DurableStoreError` if the
  caller is not holding the log's lock. It survives for tests and for a caller that already holds
  the lock; it is no longer a way to get this wrong by accident.

A module-private `_rewrite(path, records)` is the shared delegation to `durable_store.rewrite_lines`
that both paths use. It **never unlinks**: an empty kept set is written as an empty file, so
compacting a log to zero records leaves a named inode rather than one a concurrent appender is
still writing into.

**Read policy: tolerant, and it stays tolerant.** `read()` skips a torn or unknown-major row rather
than raising, because these rows only rate-limit and audit — nothing here decides anything. The
consequence is worth stating plainly: `compact` reclaims from that tolerant read, so an unparseable
nudge row is dropped permanently by a compaction. That is safe only because this log carries no
authority.

### 260707-HFX2-L12 CS-6 Update

`OrchestrationNudgeStore.read()` is now a dashboard-tolerant reader: one torn or legacy nudge row is skipped instead of raising through the supervisor/projection path, while valid rows remain available to the rate-limit lookup.

### Logic

`OrchestrationNudgeRecord` is the strict JSONL row (`ar-orchestration-nudge/v1`).
`OrchestrationNudgeStore` writes `workspace/orchestration-nudges.jsonl`, reads the
append-only log, finds the last sent row for the same target/subject/reason tuple,
and records a new attempt as `rate-limited` when it falls inside the caller's rate
window. `nudge_message(...)` formats the manager-facing stdin text, and
`missing_artifact(...)` is the small file-existence/empty check for turn reports.

### Conventions

The store follows the existing control-plane JSONL pattern: a Pydantic row (now rooted on the
shared `DurableRecord`), a workspace-scoped log under the observer root, an append for every
attempt, and pure helpers for message/artifact policy. Since 260731-EFA-L5 it also follows the
route-wide split every one of the six stores uses: a public method takes the lock, a private half
does the read, the filter and the rewrite inside that one hold.

### Invariants And Boundaries

- Rate limiting keys on target agent/lifecycle, subject agent/lifecycle, and reason.
- Rate-limited attempts are still appended for auditability.
- This file records the nudge decision; push delivery is handled by the MCP tool
  through the operator inbox.
- **Every append and every rewrite holds the log's lock.** `append` takes `exclusive_access`;
  `compact` holds it across read, filter and rewrite; `replace_records` raises
  `DurableStoreError` when its caller does not already hold it.
- **Prefer `compact(keep=...)` over `replace_records`.** The primitive takes a list somebody else
  read; the method makes the read and the rewrite one transaction. That is the whole defect of this
  leaf in miniature.
- **`_rewrite` never unlinks.** Compacting to zero records leaves an empty file, not a missing one.
- **Tolerant reads, and therefore tolerant reclamation.** `read` skips a bad row and `compact`
  reclaims from it, so a torn row is dropped for good. Acceptable only while nothing decides on
  these rows; the moment one does, this store needs a strict read for its rewrites.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The public nudge tool records these rows and emits the manager inbox message. | `orchestration_nudge_manager_payload` | mcp/src/agents_remember/mcp/tools/orchestration.py:19-36 |
| Nudge events are written into the observer workspace event log. | `EventStore` | mcp/src/agents_remember/observer/store.py:103-171 |
| `append` at L64-L68 checks the declared writer and locks; the new `compact` at L91-L107 holds one lock across read, filter and rewrite; `replace_records` at L145-L155 raises unless the caller already holds the lock, and `_rewrite` at L158-L165 delegates to `rewrite_lines` without unlinking. | `replace_records` | mcp/src/agents_remember/controlplane/orchestration_nudges.py:143-153 |
| `ORCHESTRATION_NUDGE_OWNERSHIP` names both processes as writers and the dashboard as compaction owner even though no production reclaim pass exists yet. | `ORCHESTRATION_NUDGE_OWNERSHIP` | mcp/src/agents_remember/controlplane/durable_store.py:206-216 |


## Update History

- 2026-09-05T22:25+00:00 — L30 incoming-reference review: projected the retained source-backed claim to its current owner extent; preserved this unchanged source file's genuine verification hash/date.

- 2026-08-08T23:15+02:00 — 260713-TES-L1 completion round 3 (curator): body refreshed for the supervisor -> agent-notifier rename (citation ranges and/or rename wording); verification metadata pinned until closeout stamps the 260713-TES-L1 commit.


- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B22 curator: replaced the three `n/a`-anchor
  table citations with exact anchors and fixer-generated ranges; exact non-fixing check returns
  zero findings.

- 2026-08-01T18:30+02:00 — 260731-EFA-L5 (durable store integrity). Recorded the 9.20 percent
  measured loss and the routing of all file I/O through `durable_store.py` under
  `ORCHESTRATION_NUDGE_OWNERSHIP` (both processes write, the dashboard is named compaction owner
  ahead of any production reclaim pass). Recorded the new `OrchestrationNudgeStore.compact(keep=)`,
  which holds one lock across the read, the filter and the rewrite, and the re-armed
  `replace_records`, which now calls `require_lock_held` and raises `DurableStoreError` on an
  unlocked caller — the raw primitive was the leaf's own defect reachable through this store's
  public API. Recorded the shared `_rewrite` delegation to `rewrite_lines`, which never unlinks an
  emptied log, and that `OrchestrationNudgeRecord` now inherits `DurableRecord` for
  `extra="forbid"` plus a validated `schemaVersion`. Stated plainly that the tolerant read drives
  the rewrite here, so compaction drops an unparseable row, which is safe only because nothing
  decides on these rows. Verification metadata pinned until closeout stamps the L5 commit.
- 2026-07-31T16:35+02:00 — No content impact: the only change to
  `mcp/src/agents_remember/controlplane/orchestration_nudges.py` since the L2 base commit is the
  whole-tree `ruff format` pass in `00e8379`, which re-wrapped 2 line(s) with no token change
  whatsoever. Checked by parsing both revisions and comparing the abstract syntax trees
  (identical) and the comment tokens (identical), so no symbol, signature, default, decorator,
  control-flow branch, docstring, or assertion this card describes has moved,and every claim this
  card makes about its own source still holds.

- 2026-07-31T00:00+02:00 — 260731-EFA-L2 attestation: this file was touched ONLY by the
  whole-tree `ruff format` pass (commit `00e8379`) — line reflow, no behaviour, contract,
  structure or responsibility change. The sidecar was re-read against the current source and
  every claim in it still holds, so it was deliberately not rewritten. Verification metadata
  pinned until closeout stamps the L2 commit.
- 2026-07-09T19:31+02:00 — 260707-HFX2-L12: documented the CS-6 scaling/reclamation change for this file. Verification metadata pinned until closeout stamps the HFX2-L12 commit.
- 2026-07-04T12:31+02:00 - L3: created the orchestration nudge store card for rate-limited manager nudges. Verification metadata pinned until closeout stamps the L3 commit.
