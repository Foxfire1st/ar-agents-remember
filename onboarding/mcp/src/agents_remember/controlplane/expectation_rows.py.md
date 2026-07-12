# mcp/src/agents_remember/controlplane/expectation_rows.py

| Field                  | Value                                                             |
| ---------------------- | ------------------------------------------------------------------ |
| repository             | agents-remember                                                    |
| path                   | `mcp/src/agents_remember/controlplane/expectation_rows.py`         |
| doc_type               | `file-level-onboarding`                                            |
| lastUpdated            | 2026-07-10T15:07+02:00 |
| lastVerifiedCommitHash | `300664e63f2dbb5f0701d37bbc17ff5358960c77`|
| lastVerifiedCommitDate | 2026-07-12T18:11:57+02:00|
| governingOverview      | `overview.md`                                                      |

## Governing Overview

[overview.md](overview.md)

## Purpose

R2 (260707-HFX2-L1): durable what-must-happen-by-when rows, written atomically at every dispatch
surface (spawn, gate open, signal post) so a deadline is a durable ROW an L2 sweep scans, never an
in-memory timer that a daemon/MCP restart would erase (the Restate durable-timer lesson).

## Code Commentary

### 260707-HFX2-L17 Seat-Scoped Expectations

Expectation rows persist optional `seatRole` beside `leafKey`, and both pure creation and
write-at-dispatch helpers carry it. Supervisor findings can therefore retain the exact pair whose
deadline expired instead of collapsing different roles on one leaf.

### 260707-HFX2-L12 CS-6 Update

`ExpectationRowStore` gained a retention owner for met/missed rows (`compact()` keeps pending plus recent terminal rows), and `mark_missed(current=...)` lets the supervisor act phase reuse the sweep snapshot instead of re-folding the append log once per overdue finding.

### Logic

`ExpectationKind` is `briefed-by | turn-report-by | verdict-by | ack-by` — kept in sync BY HAND
with `KNOWN_EXPECTATION_KINDS` in `kernel/agentic_settings.py` (duplicated there to avoid a
kernel<->controlplane import cycle; a future refactor should watch for drift between the two).
`ExpectationRow` is a strict Pydantic snapshot: `kind`, `state` (`pending | met | missed`),
`dueAt`, the dispatch surface's own `sourceId` (a spawned session id, a gate id, or an inbox entry
id — lets a sweep or dashboard resolve straight back to the thing the row is a deadline FOR),
optional subject/leaf keys, and `metAt`/`missedAt` stamps.

`create_expectation_row(...)` / `due_at_from_sla(now=, sla_seconds=)` are pure builders.
`mark_met`/`mark_missed` are idempotent past the first transition (a `missed` row that later gets
marked `met` — or vice versa — is a no-op; the FIRST terminal transition wins).
`write_expectation_row(store, ...)` is the one-call create+append helper every dispatch surface
calls (`mcp/tools/terminal.py::_write_spawn_expectation_rows`, `mcp/tools/gates.py::
_write_verdict_by_row`, `mcp/tools/operator_inbox.py::operator_inbox_post_payload`) — so the row
is never a forgettable follow-up step to the dispatch itself.

`ExpectationRowStore` mirrors `OperatorInboxStore`'s append/read/fold shape: one JSONL log
(`workspace/expectation-rows.jsonl`), folded by row id, last-wins. `pending()` sorts by `dueAt`;
`overdue(now=)` is the L2 sweep's predicate input (pending rows already past `dueAt`);
`find_by_source(source_id, kind=)` is the write-once-consume-once lookup a dispatch surface's
fulfillment path uses (e.g. `operator_inbox_consume_payload` marks the matching `ack-by` row met).

### Conventions

Same append-only + fold-by-id pattern as `operator_inbox_store.py` / `orchestration_nudges.py`;
`_replace` (unused today, present for parity/future compaction) uses the same unique-temp +
`os.replace` atomic-write idiom as the other controlplane stores.

### Invariants And Boundaries

- This module writes/reads the durable row only; it never redelivers, escalates, or sweeps —
  that is L2's job (a sibling leaf). `mark_missed` exists so the row is STRUCTURALLY escalatable,
  not because this leaf calls it.
- Surfacing only: the dashboard/architect projection (`observer/snapshots.py::
  read_expectation_rows`) reads this store for VISIBILITY; an L2 predicate must read this store
  directly for CORRECTNESS and never the projection (R5's split).
- `ExpectationKind` here and `KNOWN_EXPECTATION_KINDS` in `kernel/agentic_settings.py` are two
  separate definitions kept in sync by convention, not by import (avoids a kernel<->controlplane
  cycle) — a new kind must be added to both.

### Todos

None.

## Docs References

No meaningful external design-doc references found yet (created this leaf).

| Finding | Citations | Source Path |
| --- | --- | --- |
| None. | N/A | N/A |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Every dispatch surface writes its expectation row in the SAME call as the dispatch itself. | L28-L48 | [expectation_rows.py](agents-remember/mcp/src/agents_remember/controlplane/expectation_rows.py) |
| `ExpectationRowStore.overdue` is the L2 sweep's predicate input; `find_by_source` is the fulfillment lookup. | L120-L156 | [expectation_rows.py](agents-remember/mcp/src/agents_remember/controlplane/expectation_rows.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| None. | N/A | N/A |

## 260712-TRH-L4 Final Candidate

This sidecar was reviewed against the final uncommitted L4 candidate. The source now participates in the explicit spawned-unbriefed → harness-ready → briefed flow; dispatch proof remains exact-session, copy-mode-aware, harness-log-confirmed, and pending without respawn when proof is absent. Catalog writers are fully serialized across one read/body/write transaction while atomic readers remain lock-free.

## Update History
- 2026-07-12T14:20:00+02:00 — 260712-TRH-L4 curator refresh: final candidate onboarding; exact-session dispatch and serialized-writer/lock-free-reader concurrency recorded.

- 2026-07-10T15:07+02:00 — 260707-HFX2-L17: added durable seat-role identity to expectation rows
  and their atomic dispatch writer.

- 2026-07-09T19:31+02:00 — 260707-HFX2-L12: documented the CS-6 scaling/reclamation change for this file. Verification metadata pinned until closeout stamps the HFX2-L12 commit.
- 2026-07-08T14:15+02:00 — 260707-HFX2-L1: created for R2 durable expectation/deadline rows —
  the store + atomic-write helper every dispatch surface (spawn, gate open, signal post) calls.
  Verification metadata pinned until closeout stamps the 260707-HFX2-L1 commit.
