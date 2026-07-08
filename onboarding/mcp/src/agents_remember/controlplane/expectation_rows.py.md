# mcp/src/agents_remember/controlplane/expectation_rows.py

| Field                  | Value                                                             |
| ---------------------- | ------------------------------------------------------------------ |
| repository             | agents-remember                                                    |
| path                   | `mcp/src/agents_remember/controlplane/expectation_rows.py`         |
| doc_type               | `file-level-onboarding`                                            |
| lastUpdated            | 2026-07-08T14:15+02:00                                             |
| lastVerifiedCommitHash | `45708bbddf1ddb8a2045faa9fad88fe72603b674`|
| lastVerifiedCommitDate | 2026-07-08T05:51:44+02:00|
| governingOverview      | `overview.md`                                                      |

## Governing Overview

[overview.md](overview.md)

## Purpose

R2 (260707-HFX2-L1): durable what-must-happen-by-when rows, written atomically at every dispatch
surface (spawn, gate open, signal post) so a deadline is a durable ROW an L2 sweep scans, never an
in-memory timer that a daemon/MCP restart would erase (the Restate durable-timer lesson).

## Code Commentary

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

## Update History

- 2026-07-08T14:15+02:00 — 260707-HFX2-L1: created for R2 durable expectation/deadline rows —
  the store + atomic-write helper every dispatch surface (spawn, gate open, signal post) calls.
  Verification metadata pinned until closeout stamps the 260707-HFX2-L1 commit.
