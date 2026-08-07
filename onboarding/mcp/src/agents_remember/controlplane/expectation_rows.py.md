# mcp/src/agents_remember/controlplane/expectation_rows.py

| Field                  | Value                                                             |
| ---------------------- | ------------------------------------------------------------------ |
| repository             | agents-remember                                                    |
| path                   | `mcp/src/agents_remember/controlplane/expectation_rows.py`         |
| doc_type               | `file-level-onboarding`                                            |
| lastUpdated            | 2026-08-01T20:15+02:00 |
| lastVerifiedCommitHash | `b252c42cca200933d5c9c36e26de47a526a569ce`|
| lastVerifiedCommitDate | 2026-08-07T23:58:52+02:00|
| governingOverview      | `overview.md`                                                      |

## Governing Overview

[overview.md](overview.md)

## Purpose

R2 (260707-HFX2-L1): durable what-must-happen-by-when rows, written atomically at every dispatch
surface (spawn, gate open, signal post) so a deadline is a durable ROW an L2 sweep scans, never an
in-memory timer that a daemon/MCP restart would erase (the Restate durable-timer lesson).

## Code Commentary

### 260731-EFA-L5 Durable Store Contract

The `durable_store.py` module docstring records this log losing **10.20 percent** of appended rows
at the base commit under ordinary two-process operation, and that figure is quoted here on its
authority: it appears at that one site and nowhere else in the tree, unlike the 31.45 percent and
11.50 percent figures, which are carried at several independent sites. The mechanism is what a
reader can check directly, and it is the part that matters: the loss is of whole rows, so nothing on
the reader side could have detected it — the durability harness
(`mcp/tests/_store_durability.py`, driven by `test_controlplane_store_durability.py`) is what
produces a loss rate at all, and no recorded base-commit run of it is in the tree. Every
dispatch surface writes here and the supervisor sweep reclaims here, so an append landing between
the reclaim's read and its `os.replace` was silently discarded while the caller was told the row
was written. A lost expectation row is a deadline nobody is watching.

All file I/O now routes through `controlplane/durable_store.py` under `EXPECTATION_ROW_OWNERSHIP`,
which names both processes as writers and the **dashboard** as the compaction owner — the
supervisor sweep (`serving/supervisor.py`) is the only reclamation pass this log has and it needs
the folded snapshot `compact` returns.

- `append` calls `check_declared_writer()` and then holds `exclusive_access` around `append_line`,
  which fsyncs before the handle closes.
- `compact` opens `exclusive_access` and delegates to the new `_compact_locked`, so the read, the
  filter and the rewrite all happen under **one** hold of the lock. Locking only the write half
  looks safe and discards everything appended since the read.
- `_replace` no longer unlinks an emptied log, no longer builds its own pid-scoped temp and no
  longer calls `os.replace`; it delegates to `durable_store.rewrite_lines`, which refuses unless the
  calling thread holds the lock.
- `ExpectationRow` now inherits `DurableRecord`, picking up `extra="forbid"` (previously declared
  locally) plus a validated `schemaVersion`: an unknown major raises `ValidationError` at parse
  time, so the strict reader surfaces it and the tolerant reader skips it, with no version branch
  in either.

### 260731-EFA-L5 R8 The Read Split, And The Bug It Fixed

This store now carries **two readers**, and the split fixed a live defect rather than merely
tidying one.

`read` stays **strict**: a deadline row that cannot be parsed is a deadline nobody is watching, and
the L2 sweep is the only thing standing between a missed expectation and silence. Being strict is
right for the sweep.

But `observer/snapshots.py::read_expectation_rows` wrapped that strict read in
`suppress(OSError, ValueError)` — and pydantic's `ValidationError` **subclasses `ValueError`**. So
one torn line did not cost the dashboard one row; it cost the dashboard **every deadline in the
file**, and the operator was shown nothing due. The new `read_for_projection` is tolerant per row,
and `pending_for_projection` is `pending` over it; `read_expectation_rows` now calls that. The
`suppress` stays for the I/O it was there for, but it is no longer load-bearing for a malformed
row.

`_pending_rows(rows)` is the shared fold both `pending` and `pending_for_projection` run — fold by
id last-wins, keep the pending ones, order by `dueAt` — so the two readers cannot disagree about
what "pending" means. Note `pending()` now folds `read()` directly rather than going through
`current()`; the result is identical.

**Every rewrite here reads strictly.** `_compact_locked` takes its record list from `read`, never
from `read_for_projection`, so a compaction can never be the thing that erases a deadline row it
could not parse. That is what makes two policies safe rather than merely different.

### 260707-HFX2-L18 Seat-Scoped Expectations

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

Two frozen parameter objects (260731-EFA-L2) carry what an expectation *is*, separate from the
clock and identity the caller mints:

- **`ExpectationSubject(agent_id=None, lifecycle_id=None, leaf_key=None, seat_role=None)`** — who
  owes the expectation: the agent, the lifecycle it runs, and the leaf/seat it claimed. A row
  addressed to only some of these is addressed to nobody, so the dispatch surface resolves the
  whole address once.
- **`Expectation(kind, source_id, subject=ExpectationSubject(), note=None)`** — what must happen.
  `dueAt` and the row id are minted separately by the caller; everything else about an expectation
  is here.

`create_expectation_row(expectation, *, row_id, now, due_at)` / `due_at_from_sla(now=,
sla_seconds=)` are pure builders. `mark_met`/`mark_missed` are idempotent past the first transition
(a `missed` row that later gets marked `met` — or vice versa — is a no-op; the FIRST terminal
transition wins).
`write_expectation_row(store, expectation, *, row_id, now, sla_seconds)` is the one-call
create+append helper every dispatch surface
calls (`mcp/tools/terminal.py::_write_spawn_expectation_rows`, `mcp/tools/gates.py::
_write_verdict_by_row`, `mcp/tools/operator_inbox.py::operator_inbox_post_payload`) — so the row
is never a forgettable follow-up step to the dispatch itself.

`ExpectationRowStore` mirrors `OperatorInboxStore`'s append/read/fold shape: one JSONL log
(`workspace/expectation-rows.jsonl`), folded by row id, last-wins. `pending()` sorts by `dueAt`;
`overdue(now=)` is the L2 sweep's predicate input (pending rows already past `dueAt`);
`find_by_source(source_id, kind=)` is the write-once-consume-once lookup a dispatch surface's
fulfillment path uses (e.g. `operator_inbox_consume_payload` marks the matching `ack-by` row met).

### Conventions

Same append-only + fold-by-id pattern as `operator_inbox_store.py` / `orchestration_nudges.py`.
`_replace` is no longer an unused parity stub and no longer owns an atomic-write idiom of its own:
`_compact_locked` drives it, and it delegates to the shared `durable_store.rewrite_lines`. The
public-method-takes-the-lock / `_locked`-half-does-the-work split is the route-wide convention all
six stores now follow, precisely so a rewrite cannot be reached without the lock that made its
input current.

### Invariants And Boundaries

- This module writes/reads the durable row only; it never redelivers, escalates, or sweeps —
  that is L2's job (a sibling leaf). `mark_missed` exists so the row is STRUCTURALLY escalatable,
  not because this leaf calls it.
- Surfacing only: the dashboard/architect projection (`observer/snapshots.py::
  read_expectation_rows`) reads this store for VISIBILITY; an L2 predicate must read this store
  directly for CORRECTNESS and never the projection (R5's split).
- **Two readers, and the correctness one is strict.** `read` / `pending` / `overdue` raise on a
  torn or unknown-major row and are what the sweep uses; `read_for_projection` /
  `pending_for_projection` skip it and are for the dashboard only. Point the sweep at the tolerant
  pair and a malformed row becomes a deadline that silently stops being watched.
- **Every rewrite reads strictly.** `_compact_locked` reclaims from `read`, so compaction can never
  erase a row it could not parse.
- **The lock is held across the read and the rewrite.** `compact` opens `exclusive_access` before
  `_compact_locked` runs; `rewrite_lines` raises `DurableStoreError` if a caller skips it.
- **`_replace` never unlinks.** An empty kept set is an empty file, so a concurrent appender
  holding an open handle cannot write into an unlinked inode.
- `ExpectationKind` here and `KNOWN_EXPECTATION_KINDS` in `kernel/agentic_settings.py` are two
  separate definitions kept in sync by convention, not by import (avoids a kernel<->controlplane
  cycle) — a new kind must be added to both.

### Todos

None.

## Docs References

No meaningful external design-doc references found yet (created this leaf).

| Finding | Anchor | Source |
| --- | --- | --- |
| None. | N/A | N/A |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| `write_expectation_row` is the create-plus-append helper every dispatch surface calls, so the row is never a forgettable follow-up to the dispatch. | `write_expectation_row` | mcp/src/agents_remember/controlplane/expectation_rows.py:339-357 |
| `ExpectationRowStore.find_by_source` is the fulfillment lookup and `overdue` is the L2 sweep's predicate input. | `overdue` | mcp/src/agents_remember/controlplane/expectation_rows.py:237-247 |
| `append` checks the declared writer and holds `exclusive_access` around the fsyncing append. | "def write_expectation_row" | mcp/src/agents_remember/controlplane/expectation_rows.py:339-339 |
| The strict `read`, the tolerant `read_for_projection`, and the shared `_pending_rows` fold behind `pending` and `pending_for_projection`. | "def _pending_rows" | mcp/src/agents_remember/controlplane/expectation_rows.py:137-137 |
| `compact` holds the lock across `_compact_locked`, which reclaims from the strict read and rewrites through `_replace`. | "def append(self" | mcp/src/agents_remember/controlplane/expectation_rows.py:165-165 |
| `EXPECTATION_ROW_OWNERSHIP` names both processes as writers and the dashboard supervisor sweep as the single compaction owner. | `EXPECTATION_ROW_OWNERSHIP` | mcp/src/agents_remember/controlplane/durable_store.py:152-162 |
| `read_expectation_rows` now calls `pending_for_projection`, because `ValidationError` subclasses `ValueError` and its `suppress` used to discard every deadline in the file on one torn line. |"def read_expectation_rows"|mcp/src/agents_remember/observer/snapshots_impl/_runtime.py:193-193|

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| None. | N/A | N/A |

## 260712-TRH-L4 Final Candidate

This sidecar was reviewed against the final uncommitted L4 candidate. The source now participates in the explicit spawned-unbriefed → harness-ready → briefed flow; dispatch proof remains exact-session, copy-mode-aware, harness-log-confirmed, and pending without respawn when proof is absent. Catalog writers are fully serialized across one read/body/write transaction while atomic readers remain lock-free.

## Update History

- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B23 curator: replaced the `n/a` rows with exact
  anchors, converted the history `read_expectation_rows` citation, and corrected the
  read/projection row; exact non-fixing check returns zero findings.
- 2026-08-01T20:15+02:00 — 260731-EFA-L5 curator (correction pass). **One stale citation and one
  unsourced number.** The `EXPECTATION_ROW_OWNERSHIP` row cited `durable_store.py` **L270-L280**;
  the constant is at **L338** — the file grew 598 → 699 lines mid-pass and every range written
  earlier is off. Replaced with a symbol-name citation and no range, as this leaf's test cards do,
  because a number that was wrong within the hour is worse than no number. Re-read every other
  citation on this card against the current files and left them: `write_expectation_row` L337-L355
  cit:([`def`], mcp/src/agents_remember/controlplane/expectation_rows.py:339-339), `find_by_source`/`overdue` L219-L248 (L219, L237), `append` L165-L169 (L165), the
  read pair L137-L144; L171-L217 (`_pending_rows` L137, `read` L171, `read_for_projection` L185,
  `pending` L212, `pending_for_projection` L215), `compact` L286-L334 (L286, `_compact_locked` L299,
  `_replace` L327), and `read_expectation_rows` cit:(["def read_expectation_rows"], mcp/src/agents_remember/observer/snapshots_impl/_runtime.py:193-193). The **10.20 percent** figure
  is now attributed rather than asserted: it appears only in the `durable_store.py` docstring, unlike
  31.45 percent and 11.50 percent, which several independent sites carry. Named the harness that
  produces a loss rate and recorded that no base-commit run of it is stored in the tree, so a reader
  knows what is and is not checkable. This card's read-policy statements were already correct — the
  strict `read` drives `_compact_locked`, and the card says so — and were left unchanged.
- 2026-08-01T18:30+02:00 — 260731-EFA-L5 (durable store integrity). Recorded the 10.20 percent
  measured loss and the routing of all file I/O through `durable_store.py` under
  `EXPECTATION_ROW_OWNERSHIP` (both processes write, the dashboard supervisor sweep owns
  compaction): `append` checks the declared writer and locks, `compact` holds one lock across the
  new `_compact_locked` read-filter-rewrite half, and `_replace` delegates to `rewrite_lines` and
  no longer unlinks an emptied log. Recorded the R8 read split and the live defect it closed —
  `observer/snapshots.read_expectation_rows` wrapped the strict read in
  `suppress(OSError, ValueError)`, and because `ValidationError` subclasses `ValueError`, one torn
  line cost the dashboard every deadline in the file; it now calls the new
  `pending_for_projection`, and `_pending_rows` is the fold both readers share. Recorded that every
  rewrite still reads strictly. Corrected the stale Conventions claim that `_replace` was an unused
  parity stub with its own atomic-write idiom, and repaired both pre-existing citations, which the
  L2 parameter-object work had left pointing at moved code. Verification metadata pinned until
  closeout stamps the L5 commit.
- 2026-07-31T00:00+02:00 — 260731-EFA-L2 (gate honesty, `PLR0913` armed with no exemptions):
  added the frozen `ExpectationSubject` and `Expectation` parameter objects and re-signed both
  builders onto them — `create_expectation_row(expectation, *, row_id, now, due_at)` and
  `write_expectation_row(store, expectation, *, row_id, now, sla_seconds)`. The former
  `kind` / `source_id` / `subject_agent_id` / `subject_lifecycle_id` / `leaf_key` / `seat_role` /
  `note` keywords are gone from both; every dispatch surface constructs an `Expectation` instead.
  The written row's fields, the SLA computation and the store are unchanged. Verification metadata
  pinned until closeout stamps the L2 commit.
- 2026-07-12T14:20:00+02:00 — 260712-TRH-L4 curator refresh: final candidate onboarding; exact-session dispatch and serialized-writer/lock-free-reader concurrency recorded.

- 2026-07-10T15:07+02:00 — 260707-HFX2-L17: added durable seat-role identity to expectation rows
  and their atomic dispatch writer.

- 2026-07-09T19:31+02:00 — 260707-HFX2-L12: documented the CS-6 scaling/reclamation change for this file. Verification metadata pinned until closeout stamps the HFX2-L12 commit.
- 2026-07-08T14:15+02:00 — 260707-HFX2-L1: created for R2 durable expectation/deadline rows —
  the store + atomic-write helper every dispatch surface (spawn, gate open, signal post) calls.
  Verification metadata pinned until closeout stamps the 260707-HFX2-L1 commit.
