# mcp/src/agents_remember/controlplane/expectation_rows.py

| Field                  | Value                                                             |
| ---------------------- | ------------------------------------------------------------------ |
| repository             | agents-remember                                                    |
| path                   | `mcp/src/agents_remember/controlplane/expectation_rows.py`         |
| doc_type               | `file-level-onboarding`                                            |
| lastUpdated | 2026-08-11T09:50+02:00 |
| lastVerifiedCommitHash | `d9a1eb82849baea6c0b86735e772a932f4bbdc7c`|
| lastVerifiedCommitDate | 2026-08-12T00:45:15+02:00|
| governingOverview      | `overview.md`                                                      |

## Governing Overview

[overview.md](overview.md)

## Purpose

Stores restart-durable dispatch and gate deadline rows. A subject is structurally identified by task
document plus role, with occupant ids retained only as correlation evidence.

## Code Commentary

### Logic

`ExpectationRow` and `ExpectationSubject` preserve document/role alongside optional agent and
lifecycle correlations. Creation is pure; the caller writes the row atomically beside the dispatch
or gate action. The append-only store folds pending/met/missed snapshots and exposes a tolerant
projection read separately from strict decision reads.

### Conventions

Only actual dispatch/gate seams create expectations. Model completion or inbox consume does not.

### Invariants And Boundaries

- Deadlines are durable rows, never in-memory timers.
- Subject occupant replacement does not redefine the task-owned obligation.
- Projection tolerance is not used for decisions or rewrites.

### Todos

Legacy expectation kinds remain parse-only until a separately governed schema migration removes them.

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The durable row separates structural subject from runtime correlation. | `ExpectationRow` | mcp/src/agents_remember/controlplane/expectation_rows.py:49-69 |
| Creation records the supplied structural subject. | `create_expectation_row` | mcp/src/agents_remember/controlplane/expectation_rows.py:96-121 |
| Strict and tolerant reads have distinct authority. | `ExpectationRowStore` | mcp/src/agents_remember/controlplane/expectation_rows.py:163-214 |

## Cross-Repo References

No cross-repository implementation dependency governs this file.

## Update History

- 2026-08-10T10:35+02:00 — 260731-EFA-L9 curator repair: refreshed this staged card from the current onboarding body and re-resolved moved/deleted citations; verification metadata remains pinned until L9 closeout.\n
- 2026-08-09T13:00+02:00 — 260713-TES-L5 curator completion round (reviewer delta R-D1):
  corrected the surviving reference row that still called `overdue()` "the L2 sweep's
  predicate input" — it is a test-facing store helper on the owner-visible deadline surface;
  the relay never evaluates expectation rows, and the retention comment's "can no longer be
  surfaced as pending deadlines" wording is about the dashboard/provenance surface only.
  Verification metadata pinned until closeout stamps the 260713-TES-L5 commit.
- 2026-08-09T12:08+02:00 — 260713-TES-L5 curator: recorded the judgment-demolition disposition --
  the store is an owner-visible deadline surface (briefed-by/verdict-by only), the relay never
  evaluates expectation rows, `ack-by`/`turn-report-by` are retired to legacy parse-compat, and
  `overdue()` is a test-only primitive. Superseded the stale "L2 sweep is the only thing standing
  between a missed expectation and silence" and "sweep is the reserved caller of `mark_missed`"
  prose (reviewer F2). Verification metadata pinned until closeout stamps the 260713-TES-L5
  commit.
- 2026-08-09T01:21+02:00 — 260713-TES-L2 curator: recorded the store-retained disposition —
  the `turn-report-by` Literal stays for legacy parse compatibility while the settings surface
  and dispatch writes retire it; `briefed-by` no longer drives findings. Verification metadata
  pinned until closeout stamps the 260713-TES-L2 commit.
- 2026-08-08T22:10+02:00 — 260713-TES-L1 completion round (curator): refreshed this sidecar body for the supervisor -> agent-notifier rename (module paths, identifiers, settings keys, wire keys, prose) and the compat seams; verification metadata pinned until closeout stamps the 260713-TES-L1 commit.
- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B23 curator: replaced the `n/a` rows with exact
  anchors, converted the history `read_expectation_rows` citation, and corrected the
  read/projection row; exact non-fixing check returns zero findings.
- 2026-08-01T20:15+02:00 — 260731-EFA-L5 curator (correction pass). **One stale citation and one
  unsourced number.** The `EXPECTATION_ROW_OWNERSHIP` row cited `durable_store.py` **L270-L280**;
  the constant is at **L338** — the file grew 598 → 699 lines mid-pass and every range written
  earlier is off. Replaced with a symbol-name citation and no range, as this leaf's test cards do,
  because a number that was wrong within the hour is worse than no number. Re-read every other
  citation on this card against the current files and left them: `write_expectation_row` L337-L355
  cit:(["def write_expectation_row("], mcp/src/agents_remember/controlplane/expectation_rows.py:350-350), `find_by_source`/`overdue` L219-L248 (L219, L237), `append` L165-L169 (L165), the
  read pair L137-L144; L171-L217 (`_pending_rows` L137, `read` L171, `read_for_projection` L185,
  `pending` L212, `pending_for_projection` L215), `compact` L286-L334 (L286, `_compact_locked` L299,
  `_replace` L327), and `read_expectation_rows` cit:(["def read_expectation_rows("], mcp/src/agents_remember/serving/projections/snapshots_impl/_runtime.py:193-193). The **10.20 percent** figure
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
